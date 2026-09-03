#!/usr/bin/env python3
"""Render the measured MTK PD three-stage pipeline from a runner log."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

import plotly.graph_objects as go


DEFAULT_LOG = Path(
    "/root/autodl-tmp/pd_docs/backend/mtk/oppo_mt6989_result/"
    "mtk_14chunk_full_pipeline_20260807/extracted/release_ab/sync/stderr.txt"
)

TIMESTAMP_RE = re.compile(r"I (\d+):(\d+):(\d+)\.(\d+)")
START_RE = re.compile(r"MTK three-stage pipeline started: chunks=(\d+)")
EXEC_START_RE = re.compile(r"MTK three-stage: execute=(\d+)")
E2E_START_RE = re.compile(r"three-stage prefill pipeline started: .*?shards=(\d+)")
E2E_EXEC_START_RE = re.compile(r"stage-major three-stage pipeline: execute index=(\d+)")
CHUNK_RE = re.compile(
    r"chunk=(\d+) "
    r"rebuild_ms=([\d.]+) "
    r"load_ms=([\d.]+) "
    r"pipeline_wait_ms=([\d.]+) "
    r"execute_ms=([\d.]+) "
    r"kv_pack_ms=([\d.]+) "
    r"release_ms=([\d.]+)"
)
SUMMARY_RE = re.compile(
    r"stage-major summary: chunks=(\d+).*?"
    r"initial_chunk_wait_ms=([\d.]+).*?"
    r"active_prefill_ms=([\d.]+).*?"
    r"pure_npu_execute_ms=([\d.]+).*?"
    r"total_ms=([\d.]+)"
)
E2E_REBUILD_RE = re.compile(
    r"PD E2E shard rebuild: index=(\d+).*?rebuild_ms=([\d.]+)"
)
E2E_EXECUTION_RE = re.compile(
    r"PD E2E shard execution: index=(\d+) "
    r"pipeline_wait_ms=([\d.]+) execute_ms=([\d.]+)"
)
E2E_LIFECYCLE_RE = re.compile(
    r"PD E2E shard lifecycle: index=(\d+) "
    r"qnn_load_method_ms=([\d.]+).*?release_ms=([\d.]+)"
)
E2E_KV_PACK_RE = re.compile(r"async KV handoff packed: shard=(\d+).*?ms=([\d.]+)")
E2E_SETUP_RE = re.compile(r"PD E2E shard setup: .*?pipeline_wait_ms=([\d.]+)")
E2E_TIMING_RE = re.compile(
    r"PD E2E timing: .*?qnn_prefill_ms=([\d.]+) handoff_ms=([\d.]+)"
)
E2E_END_RE = re.compile(r"incremental KV handoff complete:")


@dataclass(frozen=True)
class ChunkTiming:
    chunk: int
    rebuild: float
    load: float
    pipeline_wait: float
    execute: float
    kv_pack: float
    release: float


@dataclass(frozen=True)
class TraceData:
    chunks: list[ChunkTiming]
    execute_starts: dict[int, float]
    observed_pipeline_ms: float
    initial_wait_ms: float
    active_prefill_ms: float
    pure_npu_ms: float
    reported_total_ms: float


def timestamp_ms(line: str) -> float | None:
    match = TIMESTAMP_RE.search(line)
    if not match:
        return None
    hours, minutes, seconds, micros = map(int, match.groups())
    return ((hours * 60 + minutes) * 60 + seconds) * 1000 + micros / 1000


def parse_trace(path: Path) -> TraceData:
    pipeline_start: float | None = None
    summary_time: float | None = None
    execute_absolute: dict[int, float] = {}
    chunks: list[ChunkTiming] = []
    summary_values: tuple[float, float, float, float] | None = None
    e2e_rebuild: dict[int, float] = {}
    e2e_execution: dict[int, tuple[float, float]] = {}
    e2e_lifecycle: dict[int, tuple[float, float]] = {}
    e2e_kv_pack: dict[int, float] = {}
    e2e_pipeline_wait: float | None = None
    e2e_prefill: float | None = None
    e2e_handoff: float | None = None
    e2e_end: float | None = None

    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        stamp = timestamp_ms(line)
        if START_RE.search(line) or E2E_START_RE.search(line):
            pipeline_start = stamp

        execute_match = EXEC_START_RE.search(line) or E2E_EXEC_START_RE.search(line)
        if execute_match and stamp is not None:
            chunk = int(execute_match.group(1))
            execute_absolute.setdefault(chunk, stamp)

        chunk_match = CHUNK_RE.search(line)
        if chunk_match:
            values = chunk_match.groups()
            chunks.append(
                ChunkTiming(
                    chunk=int(values[0]),
                    rebuild=float(values[1]),
                    load=float(values[2]),
                    pipeline_wait=float(values[3]),
                    execute=float(values[4]),
                    kv_pack=float(values[5]),
                    release=float(values[6]),
                )
            )

        summary_match = SUMMARY_RE.search(line)
        if summary_match:
            summary_time = stamp
            summary_values = tuple(map(float, summary_match.groups()[1:]))

        rebuild_match = E2E_REBUILD_RE.search(line)
        if rebuild_match:
            e2e_rebuild[int(rebuild_match.group(1))] = float(rebuild_match.group(2))

        execution_match = E2E_EXECUTION_RE.search(line)
        if execution_match:
            e2e_execution[int(execution_match.group(1))] = (
                float(execution_match.group(2)),
                float(execution_match.group(3)),
            )

        lifecycle_match = E2E_LIFECYCLE_RE.search(line)
        if lifecycle_match:
            e2e_lifecycle[int(lifecycle_match.group(1))] = (
                float(lifecycle_match.group(2)),
                float(lifecycle_match.group(3)),
            )

        kv_pack_match = E2E_KV_PACK_RE.search(line)
        if kv_pack_match:
            e2e_kv_pack[int(kv_pack_match.group(1))] = float(kv_pack_match.group(2))

        setup_match = E2E_SETUP_RE.search(line)
        if setup_match:
            e2e_pipeline_wait = float(setup_match.group(1))

        timing_match = E2E_TIMING_RE.search(line)
        if timing_match:
            e2e_prefill = float(timing_match.group(1))
            e2e_handoff = float(timing_match.group(2))

        if E2E_END_RE.search(line):
            e2e_end = stamp

    if not chunks and e2e_rebuild:
        ids = sorted(e2e_rebuild)
        missing = [
            chunk
            for chunk in ids
            if chunk not in e2e_execution or chunk not in e2e_lifecycle
        ]
        if missing:
            raise SystemExit(f"Incomplete E2E timing records for chunks {missing} in {path}")
        chunks = [
            ChunkTiming(
                chunk=chunk,
                rebuild=e2e_rebuild[chunk],
                load=e2e_lifecycle[chunk][0],
                pipeline_wait=e2e_execution[chunk][0],
                execute=e2e_execution[chunk][1],
                kv_pack=e2e_kv_pack.get(chunk, 0.0),
                release=e2e_lifecycle[chunk][1],
            )
            for chunk in ids
        ]

    if summary_values is None and e2e_prefill is not None:
        pure_npu = sum(chunk.execute for chunk in chunks)
        observed = (
            e2e_end - pipeline_start
            if e2e_end is not None and pipeline_start is not None
            else e2e_prefill
        )
        summary_time = (pipeline_start + observed) if pipeline_start is not None else None
        summary_values = (
            e2e_pipeline_wait or 0.0,
            e2e_prefill,
            pure_npu,
            e2e_prefill + (e2e_handoff or 0.0),
        )

    if pipeline_start is None or summary_time is None or summary_values is None:
        raise SystemExit(f"Could not find pipeline start and summary in {path}")
    if not chunks:
        raise SystemExit(f"Could not find per-chunk timings in {path}")

    chunks.sort(key=lambda item: item.chunk)
    expected = list(range(len(chunks)))
    actual = [item.chunk for item in chunks]
    if actual != expected:
        raise SystemExit(f"Expected contiguous chunks {expected}; found {actual}")

    execute_starts = {
        chunk: stamp - pipeline_start for chunk, stamp in execute_absolute.items()
    }
    initial_wait, active_prefill, pure_npu, reported_total = summary_values
    return TraceData(
        chunks=chunks,
        execute_starts=execute_starts,
        observed_pipeline_ms=summary_time - pipeline_start,
        initial_wait_ms=initial_wait,
        active_prefill_ms=active_prefill,
        pure_npu_ms=pure_npu,
        reported_total_ms=reported_total,
    )


def build_intervals(trace: TraceData) -> list[dict[str, float | int | str]]:
    intervals: list[dict[str, float | int | str]] = []
    rebuild_end = 0.0
    load_end = 0.0

    for timing in trace.chunks:
        chunk = timing.chunk
        if chunk >= 2 and chunk - 2 in trace.execute_starts:
            rebuild_start = max(rebuild_end, trace.execute_starts[chunk - 2])
        else:
            rebuild_start = rebuild_end
        rebuild_end = rebuild_start + timing.rebuild
        intervals.append(
            dict(
                phase="Rebuild",
                row=2.8,
                chunk=chunk,
                start=rebuild_start,
                duration=timing.rebuild,
            )
        )

        if chunk == 0:
            load_start = rebuild_end
        else:
            previous_execute = trace.execute_starts.get(chunk - 1, 0.0)
            load_start = max(rebuild_end, previous_execute, load_end)
        load_end = load_start + timing.load
        intervals.append(
            dict(
                phase="QNN Load",
                row=1.4,
                chunk=chunk,
                start=load_start,
                duration=timing.load,
            )
        )

        fallback_start = load_end
        execute_start = trace.execute_starts.get(chunk, fallback_start)
        cursor = execute_start
        for phase, duration in (
            ("NPU Execute", timing.execute),
            ("KV Pack", timing.kv_pack),
            ("Release", timing.release),
        ):
            intervals.append(
                dict(
                    phase=phase,
                    row=0.0,
                    chunk=chunk,
                    start=cursor,
                    duration=duration,
                )
            )
            cursor += duration

    return intervals


def create_figure(trace: TraceData, source: Path, title: str) -> go.Figure:
    intervals = build_intervals(trace)
    colors = {
        "Rebuild": "#3976D2",
        "QNN Load": "#8D63C7",
        "NPU Execute": "#F28E2B",
        "KV Pack": "#21A6A1",
        "Release": "#8A929A",
    }
    figure = go.Figure()

    for phase in colors:
        tasks = [item for item in intervals if item["phase"] == phase]
        figure.add_trace(
            go.Bar(
                name=phase,
                orientation="h",
                y=[item["row"] for item in tasks],
                x=[item["duration"] for item in tasks],
                base=[item["start"] for item in tasks],
                width=1.02,
                marker=dict(color=colors[phase], line=dict(color="white", width=0.7)),
                text=[f"C{item['chunk']}" for item in tasks],
                textposition="inside",
                insidetextanchor="middle",
                textfont=dict(size=22, color="white"),
                customdata=[[item["chunk"], item["start"]] for item in tasks],
                hovertemplate=(
                    "Chunk %{customdata[0]}<br>"
                    + phase
                    + "<br>start=%{customdata[1]:.3f} ms"
                    "<br>duration=%{x:.3f} ms<extra></extra>"
                ),
            )
        )

    execute0 = trace.execute_starts.get(0)
    if execute0 is not None:
        figure.add_vline(
            x=execute0,
            line_dash="dot",
            line_color="#444",
            annotation_text=f"first execute ({execute0:.1f} ms)",
            annotation_font_size=20,
        )

    source_label = source.as_posix().replace("/root/autodl-tmp/", "")
    note = (
        f"Measured durations from {source_label}. "
        "Execute starts use log timestamps; Rebuild/Load placement is reconstructed "
        "from rebuild-ahead=2 and load-ahead=1 dependencies. "
        f"Observed pipeline={trace.observed_pipeline_ms:.3f} ms; "
        f"initial wait={trace.initial_wait_ms:.3f} ms; "
        f"active prefill={trace.active_prefill_ms:.3f} ms."
    )
    figure.add_annotation(
        x=0,
        y=-0.26,
        xref="paper",
        yref="paper",
        text=note,
        showarrow=False,
        align="left",
        font=dict(size=18, color="#333"),
    )
    figure.update_layout(
        title=dict(text=title, x=0.5, font=dict(size=36)),
        width=2800,
        height=900,
        barmode="overlay",
        bargap=0,
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(l=220, r=80, t=120, b=210),
        legend=dict(
            orientation="h",
            x=0.5,
            xanchor="center",
            y=1.08,
            font=dict(size=21),
        ),
        xaxis=dict(
            title=dict(text="Time since three-stage pipeline start (ms)", font=dict(size=25)),
            tickfont=dict(size=20),
            showgrid=True,
            gridcolor="#E4E7EB",
            rangemode="tozero",
        ),
        yaxis=dict(
            tickmode="array",
            tickvals=[0.0, 1.4, 2.8],
            ticktext=["Stage 3: Execute / Post", "Stage 2: QNN Load", "Stage 1: Rebuild"],
            tickfont=dict(size=23),
            range=[-0.65, 3.45],
            showgrid=False,
            zeroline=False,
        ),
        uniformtext=dict(minsize=14, mode="hide"),
    )
    return figure


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render a measured MTK rebuild/load/execute three-stage trace."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_LOG)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("vis/.preview/generated/pd-mtk-real-3stage-14chunk.png"),
    )
    parser.add_argument(
        "--title",
        default="Measured MTK PD Three-Stage Pipeline — 14 Chunks, 128 Tokens",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    source = args.input.expanduser().resolve()
    output = args.output.expanduser().resolve()
    trace = parse_trace(source)
    figure = create_figure(trace, source, args.title)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == ".html":
        figure.write_html(output)
    else:
        figure.write_image(output, width=figure.layout.width, height=figure.layout.height)
    print(f"Wrote {output}")
    print(
        f"chunks={len(trace.chunks)} observed_pipeline_ms={trace.observed_pipeline_ms:.3f} "
        f"active_prefill_ms={trace.active_prefill_ms:.3f}"
    )


if __name__ == "__main__":
    main()
