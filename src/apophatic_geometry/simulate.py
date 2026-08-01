"""Command-line simulation for implemented three-node ARG models."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np

from .model import Parameters, State, collective_mode, intrinsic_distance_matrix
from .models import CONTRACT_VERSION, ModelId, parse_model_id, rk4_step


def reference_initial_state() -> State:
    """Return the frozen contract-v1.0 reference initial state."""

    return State(
        x=np.array([0.8, -0.25, 0.45], dtype=np.float64),
        s=np.array([0.2, -0.1, 0.1], dtype=np.float64),
        q=np.array([0.0, 0.05, -0.05], dtype=np.float64),
    )


def run(
    steps: int,
    dt: float,
    output: Path,
    model: ModelId | str = ModelId.MF,
) -> None:
    if steps <= 0:
        raise ValueError("steps must be positive")

    model_id = parse_model_id(model)
    params = Parameters()
    state = reference_initial_state()

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "model_id",
                "contract_version",
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
                    model_id.value,
                    CONTRACT_VERSION,
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
                state = rk4_step(state, params, dt, model=model_id)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--dt", type=float, default=0.005)
    parser.add_argument(
        "--model",
        choices=[ModelId.M0.value, ModelId.MF.value],
        default=ModelId.MF.value,
        help="implemented model identifier",
    )
    parser.add_argument("--output", type=Path, default=Path("run.csv"))
    args = parser.parse_args()
    run(steps=args.steps, dt=args.dt, output=args.output, model=args.model)


if __name__ == "__main__":
    main()
