"""Command-line simulation for the minimal three-node model."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from .model import Parameters, State, collective_mode, euler_step, intrinsic_distance_matrix


def run(steps: int, dt: float, output: Path) -> None:
    if steps <= 0:
        raise ValueError("steps must be positive")

    params = Parameters()
    state = State(
        x=np.array([0.8, -0.25, 0.45], dtype=np.float64),
        s=np.array([0.2, -0.1, 0.1], dtype=np.float64),
        q=np.array([0.0, 0.05, -0.05], dtype=np.float64),
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "step",
                "time",
                "x0",
                "x1",
                "x2",
                "s01",
                "s02",
                "s12",
                "q01",
                "q02",
                "q12",
                "collective_mode",
                "d01",
                "d02",
                "d12",
            ]
        )

        for step in range(steps + 1):
            distance = intrinsic_distance_matrix(state, params)
            writer.writerow(
                [
                    step,
                    step * dt,
                    *state.x.tolist(),
                    *state.s.tolist(),
                    *state.q.tolist(),
                    collective_mode(state.x),
                    distance[0, 1],
                    distance[0, 2],
                    distance[1, 2],
                ]
            )
            if step < steps:
                state = euler_step(state, params, dt)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--dt", type=float, default=0.005)
    parser.add_argument("--output", type=Path, default=Path("run.csv"))
    args = parser.parse_args()
    run(steps=args.steps, dt=args.dt, output=args.output)


if __name__ == "__main__":
    main()
