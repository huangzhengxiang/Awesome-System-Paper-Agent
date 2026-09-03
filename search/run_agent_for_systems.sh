#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
batch_size="${AGENT_SEARCH_BATCH_SIZE:-20}"
workers="${AGENT_SEARCH_WORKERS:-2}"
max_attempts="${AGENT_SEARCH_MAX_ATTEMPTS:-10}"
output="${AGENT_SEARCH_OUTPUT:-$repo_dir/search/results/agent_for_systems_2024_2026.title_pass.jsonl}"

topic='AI or LLM agents used to operate, optimize, debug, configure, tune, manage, repair, secure, or otherwise automate computer systems, computer architecture, operating systems, distributed/cloud systems, databases, compilers, networks, storage, and software infrastructure. Include autonomous, self-managing, self-healing, self-driving, and automated systems whose main contribution is automation of computing systems. Exclude unrelated user agents, recommender agents, generic multi-agent application research, LLM serving/inference without an automation or agent contribution, code generation without systems operation, and automation in non-computing application domains.'

groups=(
  agent copilot 'autonomous system' 'automated system' 'system automation'
  autonomic self-managing self-healing self-driving self-configur self-optimi autotun
  'AI-driven' 'AI driven' 'generative file system'
)
contexts=(
  system database kernel compiler cloud network debug optimiz configur tun operat
  manage repair diagnos schedul
)
args=()
for group in "${groups[@]}"; do
  args+=(--search-group "$group")
done
for prefix in LLM 'large language model'; do
  for context in "${contexts[@]}"; do
    args+=(--search-group "$prefix,$context")
  done
done

mkdir -p "$(dirname "$output")"
partial_output="$output.partial"
for ((attempt = 1; attempt <= max_attempts; attempt++)); do
  if python3 "$repo_dir/search/paper_db.py" semantic-filter \
    --topic "$topic" \
    --category DS --category SE --category DB \
    --from-year 2024 --to-year 2026 \
    "${args[@]}" \
    --limit 0 --batch-size "$batch_size" --workers "$workers" \
    --threshold 0.65 --format jsonl > "$partial_output"; then
    mv "$partial_output" "$output"
    exit 0
  fi
  printf 'semantic run attempt %d/%d failed; resuming cached work\n' \
    "$attempt" "$max_attempts" >&2
  sleep "$((attempt * 5))"
done
exit 1
