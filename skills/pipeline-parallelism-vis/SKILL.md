---
name: pipeline-parallelism-vis
description: Configure, run, and compare interactive pipeline-parallel training schedule visualizations in this repository. Use when a user wants a 2-stage, 3-stage, or multi-stage PP timeline; wants to compare 1F1B, interleaved, zero-bubble, overlap, or DualPipe schedules; or wants to vary microbatches, latency, or stage-specific operation costs.
---

# Pipeline Parallelism Visualization

Use `<repo>/vis/PP-Schedule-Visualization`, which is a pinned third-party
submodule. Resolve `<repo>` as the directory containing this skill's parent
`skills/` directory. Keep work inside the submodule invocation interface; do not
copy its simulator into the parent repository.

## Workflow

1. Check that `<repo>/vis/PP-Schedule-Visualization/main.py` exists. If it does
   not, initialize submodules from `<repo>` with
   `git submodule update --init --recursive` after obtaining any authorization
   required for network access.
2. Read `<repo>/vis/README.md` for the local strategy constraints and examples.
   Read the upstream README only when the user needs an advanced strategy or
   option not covered there.
3. Run commands from `<repo>/vis/PP-Schedule-Visualization`; Hydra configuration
   and the upstream asset paths assume that working directory.
4. Use `uv run app.py` for interactive exploration. Use
   `uv run python main.py key=value ...` when parameters should be reproducible.
5. For a readable static artifact, run `<repo>/vis/render_pipeline.py` with the
   Python environment that provides the upstream dependencies. Adjust
   `--label-font-size`, `--axis-font-size`, `--legend-font-size`,
   `--title-font-size`, and `--stage-gap` when requested. Prefer SVG for papers
   and PNG for quick previews.
6. For a measured MTK PD rebuild/load/execute trace, use
   `<repo>/vis/render_pd_trace.py` on the runner log. Distinguish durations read
   directly from the log from start positions reconstructed from pipeline
   dependencies, and put that distinction in the figure note. Do not substitute
   the training-schedule simulator for measured PD data.
7. Report the selected strategy, devices, stages, microbatches (`num_batches`),
   operation costs, P2P latency, and the local dashboard URL.

For ordinary N-stage 1F1B, set `num_devices=N` and `num_stages=N`. This covers
2-stage, 3-stage, and larger pipelines. For virtual pipeline stages on fewer
devices, use `strategy=interleave`, require `num_stages` to be divisible by
`num_devices`, and explain the physical-device/virtual-stage distinction.

Do not force every request into the most advanced strategy. Use `1f1b` as the
clear baseline, then add `interleave`, `zb1p`, overlap variants, or DualPipe when
the user asks for comparison or their topology calls for it. Preserve upstream
assertions: standard 1F1B/overlap/zero-bubble require stages equal devices;
DualPipe requires an even device count and stages equal devices; DualPipe-V
requires an even device count and twice as many stages as devices.

Starting a dashboard is a long-running local process. Keep its session alive
while the user is using it, state the URL, and stop only the process started for
this request when asked.
