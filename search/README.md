# CCF A/B paper database

This directory contains a queryable SQLite index for papers published by every
CCF-A and CCF-B conference and journal. The checked-in venue catalog follows the
official CCF 2026 seventh edition; paper metadata is fetched incrementally from
DBLP.

## What is included

- `venues.json`: 338 unique venues and 340 CCF classification entries.
  - 190 conference entries.
  - 150 journal classification entries representing 148 unique journals.
  - TOMM and DKE each occur in two CCF directions, so classifications must not
    be deduplicated by venue name.
- `paper_db.py`: zero-dependency database initializer, DBLP synchronizer, and
  query CLI.
- `papers.db`: local generated database (ignored by Git). It can always be
  recreated from `venues.json`.

The ten direction codes are `DS`, `NW`, `SC`, `SE`, `DB`, `CT`, `CG`, `AI`,
`HI`, and `MX`. Run `directions` to see their full English names.

## Quick start

Run commands from the repository root:

```bash
python3 search/paper_db.py init
python3 search/paper_db.py directions

# Find all CCF-A database conferences.
python3 search/paper_db.py venues \
  --category DB --rank A --type conference

# Pull all 2025 titles for those conferences from DBLP.
python3 search/paper_db.py sync \
  --category DB --rank A --type conference --year 2025

# Query the cached titles offline.
python3 search/paper_db.py papers \
  --category DB --rank A --type conference --year 2025 \
  --format titles --limit 0

# Search across cached titles and emit machine-readable JSON Lines.
python3 search/paper_db.py papers \
  --search "large language model" --format jsonl --limit 1000

# Query a year range. Repeated search groups are ORed; comma-separated terms
# inside one group are ANDed.
python3 search/paper_db.py papers \
  --category DS --category SE --category DB \
  --from-year 2024 --to-year 2026 \
  --search-group agent --search-group "LLM,system" --limit 0

# Preview the candidate count without calling a model.
python3 search/paper_db.py semantic-filter \
  --topic "efficient LLM inference systems" \
  --category DS --rank A --year 2025 --dry-run

# Optionally enrich DOI-backed papers with Crossref abstracts, then ask
# DEEPSEEK_FLASH to score topical relevance.
python3 search/paper_db.py semantic-filter \
  --topic "efficient LLM inference systems" \
  --category DS --rank A --year 2025 \
  --fetch-abstracts --threshold 0.65 --format jsonl
```

All filters can be combined. Use a stable ID such as `conference/sigmod` with
`--venue` for one venue. `sync --all-years` is supported, but it is deliberately
explicit because a direction-wide historical import can be large and places
substantial load on DBLP. `--max-venues 1` is useful for a smoke test.

The synchronizer is idempotent: DBLP record keys are upserted, and papers may be
linked to more than one catalog classification without duplicate paper rows.
Successful `venue + year` syncs are reused by default, so repeating the same
query does not call DBLP again. Pass `sync --refresh` only when a forced refresh
is intended.
Failed venue pulls are recorded in `sync_run` and do not roll back successful
venues. A venue without a usable DBLP stream is reported as skipped rather than
silently treated as an empty venue.

All 190 conferences and 144 of the 148 journals have DBLP streams. The four
cataloged exceptions are BCRA, Cognition, JASA, and JSLHR; they remain queryable
as venues, while `sync` explicitly skips them instead of returning misleading
zero-paper results.

## Model-assisted semantic filtering

`semantic-filter` reads the following OpenAI- or Anthropic-compatible model
profile from the repository-root `.env` file. Existing process environment
variables take precedence over file values.

```dotenv
DEEPSEEK_FLASH_TYPE=anthropic
DEEPSEEK_FLASH_BASE_URL=https://example.com/anthropic
DEEPSEEK_FLASH_AUTH_TOKEN=secret-or-empty-for-an-authless-endpoint
DEEPSEEK_FLASH_MODEL=deepseek-model-name
DEEPSEEK_FLASH_MAX_TOKENS=4096
```

The token is never stored in SQLite or printed. A non-empty token is sent as a
Bearer token; an empty token supports trusted endpoints without authentication.
The command sends title plus the cached abstract, if present, in batches. With
`--fetch-abstracts`, missing DOI-backed abstracts are first requested from
Crossref and cached. Papers without an available abstract are conservatively
screened by title alone.

Every completed model call set creates a `semantic_run`; per-paper relevance,
score, and reason are stored in `semantic_result`. Use `--dry-run` before broad
screening, and use `--limit 0` only when intentionally sending every matched
paper to the configured model.

Semantic evaluations are checkpointed after every batch and reused by default
when model, topic, title, and abstract fingerprint match. This makes interrupted
large screens resumable and lets overlapping later queries avoid repeated model
calls. Use `--refresh-semantic` only to force re-evaluation. `--workers` enables
bounded parallel requests; keep the default of one unless the configured model
endpoint supports concurrency.

The reproducible 2024--2026 agent-for-systems search can be resumed with:

```bash
search/run_agent_for_systems.sh
```

Refine the selected papers from that broad pass and render a stored run as
Markdown:

```bash
AGENT_REFINE_SOURCE_RUN=6 search/refine_agent_for_systems.sh
python3 search/render_semantic_run.py --run-id 14 \
  --title "Agent for Systems (2024-2026)" > search/results/example.md
```

`--from-semantic-run ID` restricts `papers` or `semantic-filter` to papers that
were selected at the source run's stored threshold. This supports multi-stage
screening without exporting and re-importing IDs.

## Database layout

```text
category 1---* classification *---1 venue
                                      | 1---* venue_stream
                                      |
                                      *
                                  paper_venue *---1 paper
```

Useful tables are:

- `category`: the ten CCF directions.
- `venue`: one row per unique conference or journal.
- `classification`: CCF direction and A/B rank for a venue.
- `venue_stream`: one or more DBLP streams for renamed or merged venues.
- `paper`: deduplicated DBLP paper metadata and title.
- `paper_venue`: paper-to-venue links.
- `sync_run`: update history, counts, and errors.
- `semantic_run` and `semantic_result`: reproducible topic-screening results.

You can also query the database directly:

```sql
SELECT p.year, p.title
FROM paper AS p
JOIN paper_venue AS pv ON pv.paper_id = p.id
JOIN classification AS c ON c.venue_id = pv.venue_id
WHERE c.category_code = 'DS' AND c.rank = 'A'
ORDER BY p.year DESC, p.title;
```

## Maintaining the catalog

The ranking source is the [CCF recommended venue catalog][ccf]. The checked-in
data was extracted from the [official seventh-edition PDF][snapshot], including
the April 9 erratum mentioned on the release page. When CCF publishes a new
edition:

1. Update `ccf_catalog_version`, sources, venues, and classifications in
   `venues.json`.
2. Preserve venue IDs (`conference/<dblp-key>` or `journal/<dblp-key>`) whenever
   DBLP identity has not changed.
3. Run `python3 search/paper_db.py init`; this migrates catalog data without
   deleting papers for retained venue IDs.
4. Verify `stats`, direction/rank counts, and a one-venue sync before a broad
   refresh.

[ccf]: https://www.ccf.org.cn/Academic_Evaluation/By_category/
[snapshot]: https://www.ccf.org.cn/ccf/contentcore/resource/download?ID=112CF3BF7E1140ACEB271ADAED12A67ADFABB8FF099E40C2759502A85C8A281F
