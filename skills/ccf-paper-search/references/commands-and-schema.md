# Commands and schema

Run all examples from the repository root.

## Direction codes

| Code | Direction |
| --- | --- |
| DS | Computer architecture, parallel/distributed computing, storage |
| NW | Computer networks |
| SC | Network and information security |
| SE | Software engineering, system software, programming languages |
| DB | Databases, data mining, information retrieval |
| CT | Theoretical computer science |
| CG | Computer graphics and multimedia |
| AI | Artificial intelligence |
| HI | Human-computer interaction and ubiquitous computing |
| MX | Interdisciplinary, comprehensive, and emerging topics |

## Common operations

```bash
python3 search/paper_db.py venues --category DS --rank A --type conference
python3 search/paper_db.py sync --category DS --rank A --type conference --year 2025
python3 search/paper_db.py papers --category DS --rank A --year 2025 --format titles --limit 0
```

`sync` skips successful non-empty `venue + year` runs by default. Zero-paper runs
are retried and execute DBLP followed by configured official-site fallbacks. Add
`--refresh` only for an intentional re-fetch of a non-empty cache; `papers` and
`semantic-filter` always query local data.

During a fresh sync, a configured official adapter is checked even when DBLP is
non-empty, allowing official abstracts to enrich matching records. Matching uses
normalized title, venue, and year so the two sources do not create duplicates.

Topic screening uses cached papers; it does not implicitly sync them:

```bash
python3 search/paper_db.py semantic-filter \
  --topic "distributed training fault tolerance" \
  --category DS --rank A --year 2025 --dry-run

python3 search/paper_db.py semantic-filter \
  --topic "distributed training fault tolerance" \
  --category DS --rank A --year 2025 \
  --fetch-abstracts --threshold 0.65 --format jsonl
```

Relevant controls:

- `--limit N`: candidate cap; `0` means unlimited.
- `--batch-size N`: papers per model request, default 20.
- `--workers N`: concurrent model requests, default 1.
- `--threshold FLOAT`: emitted relevance threshold, default 0.65.
- `--from-year` / `--to-year`: inclusive paper-year bounds.
- `--search-group`: repeatable OR group; comma-separated terms within it are
  required together, e.g. `--search-group agent --search-group "LLM,system"`.
- `--refresh-semantic`: bypass matching per-paper semantic cache entries.
- `--from-semantic-run ID`: restrict candidates to papers selected by an earlier
  run at that run's threshold, enabling broad-pass then strict-pass workflows.
- `--include-rejected`: emit rejected papers as well as selected ones.
- `--max-abstract-chars N`: per-paper abstract truncation, default 3000.
- `--env-file PATH`: global option placed before the subcommand when a different
  dotenv file is required.

`DEEPSEEK_FLASH_TYPE` may be `openai` or `anthropic`; the CLI selects the matching
chat-completions or messages request/response format.

## Storage model

- `category`, `venue`, and `classification` contain the CCF catalog.
- `venue_stream` maps renamed or merged venues to one or more DBLP streams.
- `venue_official_source` stores first-party fallback adapter configurations.
- `paper` stores deduplicated metadata, titles, and optional abstracts.
- `paper_venue` maps papers to catalog venues.
- `sync_run` records update attempts, counts, and the metadata sources used.
- `semantic_run` stores topic, model, filters, threshold, progress, and status.
- `semantic_result` stores relevance, score, reason, and the input fingerprint
  used for safe model-result cache reuse.

Inspect a prior semantic run directly when needed:

```sql
SELECT p.year, p.title, sr.score, sr.relevant, sr.reason
FROM semantic_result AS sr
JOIN paper AS p ON p.id = sr.paper_id
WHERE sr.run_id = ?
ORDER BY sr.score DESC, p.title;
```

Render a run as a Markdown paper list:

```bash
python3 search/render_semantic_run.py --run-id 14 \
  --title "Agent for Systems (2024-2026)" > search/results/example.md
```
