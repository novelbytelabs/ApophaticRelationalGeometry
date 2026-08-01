"""Command-line simulation for implemented three-node ARG models.

This is an exploratory standalone simulator, not the Phase 6 pilot runner.
Outputs are accepted only from a clean Git checkout and are committed atomically
with a completion manifest. Caller-controlled environment provenance is not
accepted.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict
import json
import os
from pathlib import Path
import tempfile
from typing import Any

import numpy as np

from .attestation import build_attestation, write_canonical_json_bytes
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
from .protocol import canonical_json_sha256, file_sha256

STANDALONE_PROTOCOL_ID = "ARG-STANDALONE-SIM-v1"
STANDALONE_PROTOCOL_VERSION = "1.0.0"
STANDALONE_SPLIT = "exploratory"
INTEGRATOR_ID = "fixed_step_classical_rk4"
IMPLEMENTATION_PATHS = (
    "src/apophatic_geometry/model.py",
    "src/apophatic_geometry/models.py",
    "src/apophatic_geometry/protocol.py",
    "src/apophatic_geometry/attestation.py",
    "src/apophatic_geometry/simulate.py",
)


def reference_initial_state() -> State:
    """Return the frozen contract-v1.0 reference initial state."""

    return State(
        x=np.array([0.8, -0.25, 0.45], dtype=np.float64),
        s=np.array([0.2, -0.1, 0.1], dtype=np.float64),
        q=np.array([0.0, 0.05, -0.05], dtype=np.float64),
    )


def _configuration_payload(
    model_id: ModelId,
    params: Parameters,
    state: State,
    steps: int,
    dt: float,
) -> dict[str, Any]:
    projected = model_id in {ModelId.MP, ModelId.MFP}
    return {
        "protocol_id": STANDALONE_PROTOCOL_ID,
        "protocol_version": STANDALONE_PROTOCOL_VERSION,
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
        "integrator": INTEGRATOR_ID,
        "observation_cadence_steps": 1,
        "split": STANDALONE_SPLIT,
    }


def _fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _write_temp_bytes(parent: Path, prefix: str, content: bytes) -> Path:
    descriptor, raw_path = tempfile.mkstemp(prefix=prefix, suffix=".tmp", dir=parent)
    path = Path(raw_path)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException:
        path.unlink(missing_ok=True)
        raise
    return path


def run(
    steps: int,
    dt: float,
    output: Path,
    model: ModelId | str = ModelId.MF,
    *,
    repo_root: Path | str = Path.cwd(),
) -> dict[str, Any]:
    """Run one attested exploratory simulation and atomically commit its files."""

    if steps <= 0:
        raise ValueError("steps must be positive")
    if not np.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be finite and positive")

    output = Path(output).resolve()
    completion_path = Path(f"{output}.complete.json")
    if output.exists() or completion_path.exists():
        raise FileExistsError("run output and completion manifest must not already exist")
    output.parent.mkdir(parents=True, exist_ok=True)

    model_id = parse_model_id(model)
    params = Parameters()
    params.validate()
    state = reference_initial_state()
    target = (
        ProjectionTarget.from_state(state)
        if model_id in {ModelId.MP, ModelId.MFP}
        else None
    )

    attestation = build_attestation(
        repo_root,
        integrator=INTEGRATOR_ID,
        implementation_paths=IMPLEMENTATION_PATHS,
    )
    configuration_payload = _configuration_payload(model_id, params, state, steps, dt)
    configuration_hash = canonical_json_sha256(configuration_payload)
    execution_hash = canonical_json_sha256(
        {
            "configuration_hash": configuration_hash,
            "attestation_sha256": attestation["attestation_sha256"],
        }
    )
    config_id = f"standalone-{configuration_hash[:16]}"

    last_raw_residual: float | str = ""
    last_post_residual: float | str = ""
    last_retraction_magnitude: float | str = ""
    if target is not None:
        if model_id is ModelId.MP:
            initial_residual = projected_derivative(
                state, params, target
            ).constraint_residual
        else:
            initial_residual = combined_projected_derivative(
                state, params, target
            ).constraint_residual
        last_raw_residual = initial_residual
        last_post_residual = initial_residual
        last_retraction_magnitude = 0.0

    csv_descriptor, csv_name = tempfile.mkstemp(
        prefix=f".{output.name}.", suffix=".tmp", dir=output.parent
    )
    temp_csv = Path(csv_name)
    temp_manifest: Path | None = None
    csv_replaced = False
    manifest_replaced = False
    actual_data_rows = 0

    try:
        with os.fdopen(csv_descriptor, "w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [
                    "protocol_id",
                    "protocol_version",
                    "split",
                    "config_id",
                    "inferential_unit",
                    "integrator",
                    "dt_or_tolerance_profile",
                    "source_commit",
                    "source_tree_sha256",
                    "protocol_lock_sha256",
                    "runtime_environment_sha256",
                    "attestation_sha256",
                    "configuration_hash",
                    "execution_hash",
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
                    mechanism_fields = [
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]

                writer.writerow(
                    [
                        STANDALONE_PROTOCOL_ID,
                        STANDALONE_PROTOCOL_VERSION,
                        STANDALONE_SPLIT,
                        config_id,
                        "standalone-single-run",
                        INTEGRATOR_ID,
                        f"dt={dt:.17g}",
                        attestation["source_commit"],
                        attestation["source_tree_sha256"],
                        attestation["protocol_lock"]["file_sha256"],
                        attestation["runtime_environment_sha256"],
                        attestation["attestation_sha256"],
                        configuration_hash,
                        execution_hash,
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
                actual_data_rows += 1

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

            handle.flush()
            os.fsync(handle.fileno())

        expected_data_rows = steps + 1
        if actual_data_rows != expected_data_rows:
            raise RuntimeError(
                f"row-count mismatch: {actual_data_rows} != {expected_data_rows}"
            )
        output_sha256 = file_sha256(temp_csv)
        completion = {
            "completion_status": "COMPLETE",
            "protocol_id": STANDALONE_PROTOCOL_ID,
            "protocol_version": STANDALONE_PROTOCOL_VERSION,
            "split": STANDALONE_SPLIT,
            "config_id": config_id,
            "configuration_hash": configuration_hash,
            "execution_hash": execution_hash,
            "integrator": INTEGRATOR_ID,
            "expected_data_rows": expected_data_rows,
            "actual_data_rows": actual_data_rows,
            "expected_csv_rows_including_header": expected_data_rows + 1,
            "output_name": output.name,
            "output_sha256": output_sha256,
            "attestation": attestation,
        }
        temp_manifest = _write_temp_bytes(
            output.parent,
            f".{completion_path.name}.",
            write_canonical_json_bytes(completion),
        )

        os.replace(temp_csv, output)
        csv_replaced = True
        os.replace(temp_manifest, completion_path)
        manifest_replaced = True
        _fsync_directory(output.parent)
        return completion
    except BaseException:
        temp_csv.unlink(missing_ok=True)
        if temp_manifest is not None:
            temp_manifest.unlink(missing_ok=True)
        if manifest_replaced:
            completion_path.unlink(missing_ok=True)
        if csv_replaced:
            output.unlink(missing_ok=True)
        raise


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
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="clean Git checkout root used to derive source attestation",
    )
    args = parser.parse_args()
    run(
        steps=args.steps,
        dt=args.dt,
        output=args.output,
        model=args.model,
        repo_root=args.repo_root,
    )


if __name__ == "__main__":
    main()
