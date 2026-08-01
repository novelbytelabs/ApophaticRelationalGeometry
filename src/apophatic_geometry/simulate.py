"""Command-line simulation for implemented three-node ARG models."""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict
import hashlib
import json
import os
from pathlib import Path

import numpy as np

from .model import Parameters, State, collective_mode, intrinsic_distance_matrix
from .models import (
    CONTRACT_VERSION,
    ModelId,
    ProjectionTarget,
    combined_projected_derivative,
    combined_projected_rk4_step,
    parse_model_id,
    projected_derivative,
    projected_rk4_step,
    rk4_step,
)


def reference_initial_state() -> State:
    """Return the frozen contract-v1.0 reference initial state."""

    return State(
        x=np.array([0.8, -0.25, 0.45], dtype=np.float64),
        s=np.array([0.2, -0.1, 0.1], dtype=np.float64),
        q=np.array([0.0, 0.05, -0.05], dtype=np.float64),
    )


def _configuration_hash(
    model_id: ModelId,
    params: Parameters,
    state: State,
    steps: int,
    dt: float,
) -> str:
    projected = model_id in {ModelId.MP, ModelId.MFP}
    payload = {
        "contract_version": CONTRACT_VERSION,
        "model_id": model_id.value,
        "parameters": asdict(params),
        "initial_state": {
            "x": state.x.tolist(),
            "s": state.s.tolist(),
            "q": state.q.tolist(),
        },
        "projection_target_c0": collective_mode(state.x) if projected else None,
        "steps": steps,
        "dt": dt,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def run(
    steps: int,
    dt: float,
    output: Path,
    model: ModelId | str = ModelId.MF,
) -> None:
    if steps <= 0:
        raise ValueError("steps must be positive")
    if not np.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be finite and positive")

    model_id = parse_model_id(model)
    params = Parameters()
    state = reference_initial_state()
    target = (
        ProjectionTarget.from_state(state)
        if model_id in {ModelId.MP, ModelId.MFP}
        else None
    )
    configuration_hash = _configuration_hash(model_id, params, state, steps, dt)
    source_commit = os.environ.get("ARG_SOURCE_COMMIT", "unavailable")

    last_raw_residual: float | str = ""
    last_post_residual: float | str = ""
    last_retraction_magnitude: float | str = ""
    if target is not None:
        if model_id is ModelId.MP:
            initial_residual = projected_derivative(state, params, target).constraint_residual
        else:
            initial_residual = combined_projected_derivative(
                state, params, target
            ).constraint_residual
        last_raw_residual = initial_residual
        last_post_residual = initial_residual
        last_retraction_magnitude = 0.0

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "source_commit",
                "configuration_hash",
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
                "constraint_residual",
                "normalized_tangency_residual",
                "projection_correction_norm",
                "projection_denominator",
                "feedback_norm",
                "node_feedback_norm",
                "local_proposal_norm",
                "combined_proposal_norm",
                "pre_retraction_constraint_residual",
                "post_retraction_constraint_residual",
                "retraction_magnitude",
            ]
        )

        for step in range(steps + 1):
            distance = intrinsic_distance_matrix(state, params)
            if model_id is ModelId.MP and target is not None:
                projection = projected_derivative(state, params, target)
                mechanism_fields: list[float | str] = [
                    projection.constraint_residual,
                    projection.normalized_tangency_residual,
                    projection.correction_norm,
                    projection.denominator,
                    "",
                    "",
                    float(np.linalg.norm(projection.proposal.pack())),
                    "",
                    last_raw_residual,
                    last_post_residual,
                    last_retraction_magnitude,
                ]
            elif model_id is ModelId.MFP and target is not None:
                combined = combined_projected_derivative(state, params, target)
                mechanism_fields = [
                    combined.constraint_residual,
                    combined.normalized_tangency_residual,
                    combined.correction_norm,
                    combined.denominator,
                    combined.feedback_norm,
                    combined.node_feedback_norm,
                    float(np.linalg.norm(combined.local_proposal.pack())),
                    float(np.linalg.norm(combined.proposal.pack())),
                    last_raw_residual,
                    last_post_residual,
                    last_retraction_magnitude,
                ]
            else:
                mechanism_fields = ["", "", "", "", "", "", "", "", "", "", ""]

            writer.writerow(
                [
                    source_commit,
                    configuration_hash,
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
                    *mechanism_fields,
                ]
            )

            if step < steps:
                if model_id is ModelId.MP and target is not None:
                    result = projected_rk4_step(state, params, dt, target)
                    state = result.state
                    last_raw_residual = result.raw_constraint_residual
                    last_post_residual = result.post_constraint_residual
                    last_retraction_magnitude = result.retraction_magnitude
                elif model_id is ModelId.MFP and target is not None:
                    result = combined_projected_rk4_step(state, params, dt, target)
                    state = result.state
                    last_raw_residual = result.raw_constraint_residual
                    last_post_residual = result.post_constraint_residual
                    last_retraction_magnitude = result.retraction_magnitude
                else:
                    state = rk4_step(state, params, dt, model=model_id)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--dt", type=float, default=0.005)
    parser.add_argument(
        "--model",
        choices=[member.value for member in ModelId],
        default=ModelId.MF.value,
        help="implemented model identifier",
    )
    parser.add_argument("--output", type=Path, default=Path("run.csv"))
    args = parser.parse_args()
    run(steps=args.steps, dt=args.dt, output=args.output, model=args.model)


if __name__ == "__main__":
    main()
