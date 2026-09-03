#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_run="${AGENT_REFINE_SOURCE_RUN:-6}"
batch_size="${AGENT_REFINE_BATCH_SIZE:-20}"
workers="${AGENT_REFINE_WORKERS:-2}"
max_attempts="${AGENT_REFINE_MAX_ATTEMPTS:-10}"
fetch_abstracts="${AGENT_REFINE_FETCH_ABSTRACTS:-0}"
output="${AGENT_REFINE_OUTPUT:-$repo_dir/search/results/agent_for_systems_2024_2026.refined.jsonl}"

topic='Strictly select papers whose primary research contribution directly automates the operation of computer systems or software infrastructure. Include AI/LLM agents, agentic AIOps/SRE, autonomous or self-managing systems, and automated methods for configuring, tuning, scheduling, diagnosing, debugging, securing, repairing, or recovering databases, operating systems, distributed/cloud systems, networks, storage, compilers, and computer architecture. Require a concrete systems-management or infrastructure-automation contribution. Exclude generic multi-agent or reinforcement-learning applications, user/recommender agents, ordinary code generation and general program repair, software-development assistants without systems-operation impact, LLM inference/serving optimizations without an agentic automation contribution, and automation in non-computing domains. Be conservative when evidence is only a title.'

mkdir -p "$(dirname "$output")"
partial_output="$output.partial"
abstract_args=()
if [[ "$fetch_abstracts" == "1" ]]; then
  abstract_args=(--fetch-abstracts --abstract-delay 0.1)
fi
for ((attempt = 1; attempt <= max_attempts; attempt++)); do
  if python3 "$repo_dir/search/paper_db.py" semantic-filter \
    --topic "$topic" \
    --category DS --category SE --category DB \
    --from-year 2024 --to-year 2026 \
    --from-semantic-run "$source_run" \
    "${abstract_args[@]}" \
    --limit 0 --batch-size "$batch_size" --workers "$workers" \
    --threshold 0.75 --format jsonl > "$partial_output"; then
    mv "$partial_output" "$output"
    exit 0
  fi
  printf 'refinement attempt %d/%d failed; resuming cached work\n' \
    "$attempt" "$max_attempts" >&2
  sleep "$((attempt * 5))"
done
exit 1
