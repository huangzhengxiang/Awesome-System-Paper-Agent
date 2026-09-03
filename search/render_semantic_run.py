#!/usr/bin/env python3
"""Render one stored semantic screening run as a Markdown paper list."""

from __future__ import annotations

import argparse
import json
import sqlite3
from collections import Counter
from pathlib import Path


def markdown_text(value: object) -> str:
    text = str(value or "").replace("\n", " ").strip()
    for char in ("\\", "`", "*", "[", "]"):
        text = text.replace(char, "\\" + char)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=Path(__file__).with_name("papers.db"))
    parser.add_argument("--run-id", type=int, required=True)
    parser.add_argument("--title", default="Semantic paper screening results")
    args = parser.parse_args()

    connection = sqlite3.connect(args.db)
    connection.row_factory = sqlite3.Row
    run = connection.execute(
        "SELECT * FROM semantic_run WHERE id=?", (args.run_id,)
    ).fetchone()
    if run is None:
        raise SystemExit(f"semantic run {args.run_id} does not exist")
    raw_rows = connection.execute(
        """SELECT p.id, p.title, p.year, p.url, p.abstract,
                  sr.score, sr.reason,
                  group_concat(DISTINCT coalesce(v.short_name, v.name)) venues,
                  group_concat(DISTINCT c.category_code || '-' || c.rank) ccf_tags
           FROM semantic_result sr
           JOIN paper p ON p.id=sr.paper_id
           JOIN paper_venue pv ON pv.paper_id=p.id
           JOIN venue v ON v.id=pv.venue_id
           JOIN classification c ON c.venue_id=v.id
           WHERE sr.run_id=? AND sr.relevant=1 AND sr.score>=?
           GROUP BY p.id
           ORDER BY p.year DESC, sr.score DESC, p.title""",
        (args.run_id, run["threshold"]),
    ).fetchall()
    deduplicated: dict[str, dict[str, object]] = {}
    for raw_row in raw_rows:
        row = dict(raw_row)
        key = str(row["title"]).rstrip(". ").casefold()
        previous = deduplicated.get(key)
        if previous is None:
            deduplicated[key] = row
            continue
        previous["venues"] = ",".join(sorted(set(
            str(previous["venues"]).split(",") + str(row["venues"]).split(",")
        )))
        previous["ccf_tags"] = ",".join(sorted(set(
            str(previous["ccf_tags"]).split(",") + str(row["ccf_tags"]).split(",")
        )))
        if float(row["score"]) > float(previous["score"]):
            previous.update({
                "score": row["score"], "reason": row["reason"], "url": row["url"]
            })
        if row["abstract"] and not previous["abstract"]:
            previous["abstract"] = row["abstract"]
    rows = sorted(
        deduplicated.values(),
        key=lambda row: (-int(row["year"] or 0), -float(row["score"]), str(row["title"])),
    )
    filters = json.loads(run["filters_json"])
    year_counts = Counter(row["year"] for row in rows)
    abstract_count = sum(bool(row["abstract"]) for row in rows)

    print(f"# {markdown_text(args.title)}")
    print()
    print(
        f"> DeepSeek semantic run `{run['id']}`; generated from the local CCF A/B "
        "paper database. Scores measure estimated topical relevance, not paper quality."
    )
    print()
    print(f"- Model: `{markdown_text(run['model'])}`")
    print(f"- Topic: {markdown_text(run['topic'])}")
    print(
        f"- Scope: categories `{', '.join(filters.get('category') or [])}`, "
        f"years `{filters.get('from_year')}–{filters.get('to_year')}`, "
        f"source run `{filters.get('from_semantic_run')}`"
    )
    print(f"- Threshold: `{run['threshold']:.2f}`")
    print(
        f"- Screened: `{run['expected_count']}`; selected records: "
        f"`{len(raw_rows)}`; unique titles: `{len(rows)}`"
    )
    print(
        f"- Evidence: `{abstract_count}` selected papers had cached abstracts; "
        f"`{len(rows) - abstract_count}` were judged conservatively from titles."
    )
    print()

    emitted = 0
    for year in sorted(year_counts, reverse=True):
        print(f"## {year} ({year_counts[year]})")
        print()
        index = 0
        for row in rows:
            if row["year"] != year:
                continue
            index += 1
            title = markdown_text(row["title"])
            url = row["url"] or ""
            linked_title = f"[{title}]({url})" if url else title
            venue = markdown_text(row["venues"])
            tags = markdown_text(row["ccf_tags"])
            print(
                f"{index}. **{linked_title}** — {venue}; `{tags}`; "
                f"score `{row['score']:.2f}`"
            )
            print(f"   - {markdown_text(row['reason'])}")
            emitted += 1
            if emitted < len(rows):
                print()

    connection.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
