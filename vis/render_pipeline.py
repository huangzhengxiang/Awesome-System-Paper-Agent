#!/usr/bin/env python3
"""Render a styled pipeline-parallel schedule with the vendored simulator."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any


VIS_DIR = Path(__file__).resolve().parent
UPSTREAM_DIR = VIS_DIR / "PP-Schedule-Visualization"
if not (UPSTREAM_DIR / "src" / "visualizer.py").is_file():
    raise SystemExit(
        "PP-Schedule-Visualization is missing; run "
        "`git submodule update --init --recursive`."
    )
sys.path.insert(0, str(UPSTREAM_DIR))

from src.execution_model import ScheduleConfig  # noqa: E402
from src.strategies import (  # noqa: E402
    generate_1f1b_interleave_overlap_schedule,
    generate_1f1b_interleave_schedule,
    generate_1f1b_overlap_schedule,
    generate_1f1b_schedule,
    generate_dualpipe_schedule,
    generate_dualpipe_v_schedule,
    generate_zero_bubble_1p_schedule,
)
from src.visualizer import (  # noqa: E402
    convert_schedule_to_visualization_format,
    create_pipeline_figure,
)


STRATEGIES: dict[str, tuple[Any, str, bool]] = {
    "1f1b": (generate_1f1b_schedule, "standard", False),
    "interleave": (generate_1f1b_interleave_schedule, "interleave", False),
    "zb1p": (generate_zero_bubble_1p_schedule, "standard", True),
    "1f1b_overlap": (generate_1f1b_overlap_schedule, "standard", False),
    "1f1b_interleave_overlap": (
        generate_1f1b_interleave_overlap_schedule,
        "interleave",
        False,
    ),
    "dualpipe": (generate_dualpipe_schedule, "dualpipe", True),
    "dualpipe_v": (generate_dualpipe_v_schedule, "dualpipe_v", True),
}


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return parsed


def nonnegative_float(value: str) -> float:
    parsed = float(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be non-negative")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render a static pipeline-parallel schedule with readable labels."
    )
    parser.add_argument("--strategy", choices=STRATEGIES, default="1f1b")
    parser.add_argument("--stages", type=positive_int, default=3)
    parser.add_argument(
        "--devices",
        type=positive_int,
        help="Physical devices; defaults to the stage count.",
    )
    parser.add_argument("--microbatches", type=positive_int, default=6)
    parser.add_argument("--forward-time", type=float, default=1.0)
    parser.add_argument("--backward-time", type=float, default=2.0)
    parser.add_argument("--p2p-latency", type=nonnegative_float, default=0.0)
    parser.add_argument(
        "--stage-gap",
        type=nonnegative_float,
        default=0.4,
        help="Vertical gap between stage/device rows, in row-height units.",
    )
    parser.add_argument("--label-font-size", type=positive_int, default=22)
    parser.add_argument("--axis-font-size", type=positive_int, default=20)
    parser.add_argument("--legend-font-size", type=positive_int, default=18)
    parser.add_argument("--title-font-size", type=positive_int, default=30)
    parser.add_argument("--width", type=positive_int, default=2400)
    parser.add_argument("--height", type=positive_int)
    parser.add_argument("--title")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output .png/.svg/.pdf/.webp or .html path.",
    )
    return parser


def validate_topology(strategy: str, devices: int, stages: int, batches: int) -> None:
    if stages % devices:
        raise SystemExit("--stages must be divisible by --devices")
    if strategy in {"1f1b", "1f1b_overlap", "zb1p", "dualpipe"} and stages != devices:
        raise SystemExit(f"{strategy} requires --stages == --devices")
    if strategy == "dualpipe":
        if devices % 2:
            raise SystemExit("dualpipe requires an even --devices value")
        if batches < devices:
            raise SystemExit("dualpipe requires --microbatches >= --devices")
    if strategy == "dualpipe_v" and (devices % 2 or stages != 2 * devices):
        raise SystemExit("dualpipe_v requires even devices and stages == 2 * devices")


def spread_rows(figure: Any, row_count: int, gap: float) -> None:
    """Insert vertical whitespace while preserving each operation's height."""
    pitch = 1.0 + gap

    for shape in figure.layout.shapes:
        center = (float(shape.y0) + float(shape.y1)) / 2
        row = round(center)
        shape.y0 = row * pitch + (float(shape.y0) - row)
        shape.y1 = row * pitch + (float(shape.y1) - row)

    for annotation in figure.layout.annotations:
        value = float(annotation.y)
        row = round(value)
        annotation.y = row * pitch + (value - row)

    for trace in figure.data:
        if trace.y:
            trace.y = tuple(
                None if value is None else round(float(value)) * pitch
                for value in trace.y
            )

    figure.update_yaxes(
        tickvals=[index * pitch for index in reversed(range(row_count))],
        range=[-0.65, (row_count - 1) * pitch + 0.65],
    )


def style_figure(figure: Any, args: argparse.Namespace, devices: int) -> None:
    spread_rows(figure, devices, args.stage_gap)
    for annotation in figure.layout.annotations:
        annotation.font.size = args.label_font_size

    height = args.height or max(
        720, int(220 + devices * (90 + args.stage_gap * 55))
    )
    title = args.title or (
        f"{args.stages}-Stage {args.strategy} Pipeline Parallelism "
        f"({args.microbatches} Microbatches)"
    )
    figure.update_layout(
        title=dict(text=title, font=dict(size=args.title_font_size)),
        width=args.width,
        height=height,
        margin=dict(l=130, r=250, t=100, b=100),
        legend=dict(
            font=dict(size=args.legend_font_size),
            title=dict(font=dict(size=args.legend_font_size)),
        ),
    )
    figure.update_xaxes(
        title=dict(text="Time", font=dict(size=args.axis_font_size)),
        tickfont=dict(size=args.axis_font_size),
    )
    figure.update_yaxes(
        title=dict(text="Device / Stage", font=dict(size=args.axis_font_size)),
        tickfont=dict(size=args.axis_font_size),
    )


def main() -> None:
    args = build_parser().parse_args()
    devices = args.devices or args.stages
    validate_topology(args.strategy, devices, args.stages, args.microbatches)

    factory, placement, split_backward = STRATEGIES[args.strategy]
    config = ScheduleConfig(
        num_devices=devices,
        num_stages=args.stages,
        num_batches=args.microbatches,
        p2p_latency=args.p2p_latency,
        placement_strategy=placement,
        split_backward=split_backward,
        op_times={
            "forward": args.forward_time,
            "backward": args.backward_time,
            "backward_D": args.backward_time / 2,
            "backward_W": args.backward_time / 2,
        },
    )
    schedule = factory(config)
    schedule.execute()
    data = convert_schedule_to_visualization_format(schedule)
    figure = create_pipeline_figure(data, show_progress=False)
    style_figure(figure, args, devices)

    output = args.output or (
        VIS_DIR
        / ".preview"
        / "generated"
        / f"{args.strategy}-{args.stages}-stage-{args.microbatches}-microbatches.png"
    )
    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == ".html":
        figure.write_html(output)
    else:
        figure.write_image(output, width=figure.layout.width, height=figure.layout.height)

    print(f"Wrote {output}")
    print(
        f"strategy={args.strategy} devices={devices} stages={args.stages} "
        f"microbatches={args.microbatches} "
        f"makespan={schedule.get_total_execution_time():g}"
    )


if __name__ == "__main__":
    main()
