---
name: ccf-paper-search
description: Query, update, and semantically screen the repository's CCF-A/B conference and journal paper database. Use when a user wants venues or paper titles by CCF direction/rank/year, wants DBLP paper metadata pulled, or gives a research topic for DEEPSEEK_FLASH-assisted relevance filtering.
---

# CCF Paper Search

Operate the database through `<repo>/search/paper_db.py`; do not reproduce venue
lists or query SQLite manually unless the CLI cannot express the request. Resolve
`<repo>` as the directory containing this skill's parent `skills/` directory.

## Workflow

1. Run `python3 <repo>/search/paper_db.py stats` to inspect cached coverage.
2. Translate the requested direction to a code with `directions`, then inspect
   matching venues with `venues`. Combine `--category`, `--rank`, `--type`, and
   `--venue` rather than filtering command output by hand.
3. If the requested papers are not cached, run `sync` with an explicit `--year`.
   `sync` reuses successful non-empty venue/year cache entries by default; use
   `--refresh` only when the user asks to update already cached data. Never treat
   an `ok` run with `fetched_count=0` as authoritative: the CLI must retry DBLP
   and then any configured official-site fallback on the next sync.
   Use `--all-years` only when the user clearly requests historical coverage;
   direction-wide history can be large and should not be inferred from “find
   papers about a topic.”
4. For plain retrieval, use `papers`. Use `--format titles --limit 0` when the
   user asks for every cached title.
5. For a topic request, first run `semantic-filter` with the same filters and
   `--dry-run`. Then run it for real, normally with `--fetch-abstracts`, after
   making the candidate scope visible. Retain the default candidate cap unless
   the user requests broader screening.

Both network stages cache by default. `sync` reuses successful non-empty
venue/year pulls. If DBLP is empty, it checks configured official adapters (for
example, USENIX technical-session pages) before recording the result. On a fresh
sync, configured official sources also enrich matching DBLP records with
abstracts and are merged by normalized title rather than inserted as duplicates.
`semantic-filter` checkpoints batches and reuses evaluations when the model,
topic, title, and abstract fingerprint match. Use `--refresh` or
`--refresh-semantic` only when the user explicitly needs fresh data or scoring.
For Boolean-like lexical prefilters, repeat `--search-group`: groups are ORed,
while comma-separated terms within a group are ANDed. Use `--from-year` and
`--to-year` for an inclusive range.

For a conservative second pass, use `--from-semantic-run ID` to take only the
papers selected by the broad source run. Store the refined run, then generate a
readable list with `search/render_semantic_run.py --run-id ID`. The renderer
groups papers by year and deduplicates identical titles across DBLP publication
records while leaving the raw database results intact.

The model command reads only the `DEEPSEEK_FLASH_*` profile from `<repo>/.env`
and follows its OpenAI- or Anthropic-compatible API type. Never print, copy, or
persist its auth token. An empty token is valid only for an endpoint that permits
unauthenticated requests. If the endpoint returns 401/403, report that the
profile needs a token; do not borrow credentials from another profile.

Treat model relevance as an aid rather than ground truth. Report the topic,
filters, threshold, number screened, number selected, and semantic run ID. Note
when papers were judged from title alone because no abstract was available.

Read [references/commands-and-schema.md](references/commands-and-schema.md) when
constructing advanced filters, diagnosing the database, or querying stored
semantic results from SQLite.
