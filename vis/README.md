# System Visualization

Visualization tools are vendored as pinned Git submodules so that this repository
can expose mature system tooling without copying or silently forking upstream
implementations.

## Pipeline parallelism

[PP-Schedule-Visualization](PP-Schedule-Visualization) emulates and renders
pipeline-parallel training schedules in an interactive Dash/Plotly UI. The
submodule is MIT licensed and supports 1F1B, interleaved 1F1B, zero-bubble,
computation/communication overlap, DualPipe, and DualPipe-V.

Initialize the tool after cloning this repository:

```bash
git submodule update --init --recursive
cd vis/PP-Schedule-Visualization
```

The upstream project uses `uv`. Start the interactive parameter editor with:

```bash
uv run app.py
```

The default address is <http://127.0.0.1:8050/>. The UI lets you change stage,
device, microbatch, latency, and operation-time parameters.

The Hydra CLI is convenient for reproducible figures:

```bash
# 2-stage 1F1B
uv run python main.py strategy=1f1b num_devices=2 num_stages=2 num_batches=4

# 3-stage 1F1B
uv run python main.py strategy=1f1b num_devices=3 num_stages=3 num_batches=6

# 8-stage 1F1B
uv run python main.py strategy=1f1b num_devices=8 num_stages=8 num_batches=16

# 8 virtual stages interleaved over 4 devices
uv run python main.py strategy=interleave num_devices=4 num_stages=8 num_batches=8
```

### Configuration constraints

| Strategy | Stage/device relationship | Additional constraints |
| --- | --- | --- |
| `1f1b`, `1f1b_overlap`, `zb1p` | stages = devices | positive batch count |
| `interleave`, `1f1b_interleave_overlap` | stages divisible by devices | multiple stages per device enable interleaving |
| `dualpipe` | stages = devices | even device count; batches at least devices |
| `dualpipe_v` | stages = 2 x devices | even device count |

Operation costs can be uniform or stage-specific. For example:

```bash
uv run python main.py \
  strategy=1f1b num_devices=3 num_stages=3 num_batches=8 \
  p2p_latency=0.1 op_times.forward=0.8 op_times.backward=1.6
```

### Readable static figures

The repository adapter keeps the upstream scheduling implementation while adding
publication-friendly font and row-spacing controls:

```bash
python vis/render_pipeline.py \
  --strategy 1f1b \
  --stages 3 \
  --microbatches 6
```

The publication-oriented defaults are label/axis/legend/title font sizes
`22/20/18/30`, width `2400`, stage gap `0.4`, and a minimum height of `720`.
Every value remains configurable; `--stage-gap 0` retains contiguous upstream
rows, while larger values add vertical whitespace without changing operation
durations. Use `--output figure.svg` for
vector output or `--output figure.html` for an interactive standalone figure.
The default output goes to the ignored `vis/.preview/generated/` directory.

### Measured MTK PD traces

`render_pd_trace.py` parses real per-chunk MTK runner logs instead of generating
a synthetic training schedule:

```bash
python vis/render_pd_trace.py \
  --input /root/autodl-tmp/pd_docs/backend/mtk/oppo_mt6989_result/\
mtk_14chunk_full_pipeline_20260807/extracted/release_ab/sync/stderr.txt \
  --output vis/.preview/generated/pd-mtk-real-3stage-14chunk.png
```

The three rows are the actual PD stages: rebuild PTE, load the QNN
method/context, and execute plus KV pack/release. Bar lengths are measured
per-chunk durations. Execute starts come directly from log timestamps; rebuild
and load positions are reconstructed from the logged `rebuild_ahead=2` and
`load_ahead=1` dependencies. The figure reports both the observed pipeline
window and the runner's active-Prefill metric so these two timing scopes are not
confused.

See the [upstream README](PP-Schedule-Visualization/README.md) for all strategies,
screenshots, and advanced parameters.
