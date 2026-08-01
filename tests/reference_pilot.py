"""Independent Phase 6 reconstruction used only by tests.

This module intentionally does not import the production planner, runner,
archive writer, checksum writer, or summary code.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

import numpy as np

from apophatic_geometry.model import Parameters, State
from reference_equations import reference_rk4_step

_PROTOCOL_ID = "ARG-P5-COMP-v1"


def _canonical_hash(value: Any) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def independent_pilot_ids(manifest: Mapping[str, Any]) -> tuple[str, ...]:
    directions = manifest["directions"]
    hashes = {
        str(entry["direction_id"]): hashlib.sha256(
            f"{entry['direction_id']}|{_PROTOCOL_ID}".encode("utf-8")
        ).hexdigest()
        for entry in directions
    }
    pilot = {
        direction_id
        for direction_id, _ in sorted(hashes.items(), key=lambda item: item[1])[:10]
    }
    tags = {str(key): str(value) for key, value in manifest["configuration_rule"]["c0_tags"].items()}
    identifiers = []
    for direction_id in sorted(pilot):
        for c0 in manifest["generation"]["c0_levels"]:
            identifiers.append(f"p5-{direction_id}-c{tags[str(c0)]}")
    return tuple(sorted(identifiers))


def independent_configuration_hashes(manifest: Mapping[str, Any]) -> dict[str, str]:
    pilot_ids = set(independent_pilot_ids(manifest))
    directions = {str(entry["direction_id"]): entry for entry in manifest["directions"]}
    s0 = np.asarray(manifest["generation"]["shared_s0"], dtype=np.float64)
    q0 = np.asarray(manifest["generation"]["shared_q0"], dtype=np.float64)
    tags = {str(key): str(value) for key, value in manifest["configuration_rule"]["c0_tags"].items()}
    result: dict[str, str] = {}
    for direction_id, entry in directions.items():
        direction = np.asarray(entry["unit_vector"], dtype=np.float64)
        for raw_c0 in manifest["generation"]["c0_levels"]:
            c0 = float(raw_c0)
            config_id = f"p5-{direction_id}-c{tags[str(raw_c0)]}"
            if config_id not in pilot_ids:
                continue
            state = State(x=np.sqrt(3.0 * c0) * direction, s=s0.copy(), q=q0.copy())
            payload = {
                "protocol_id": _PROTOCOL_ID,
                "protocol_version": "1.0.0",
                "contract_version": "1.0",
                "config_id": config_id,
                "direction_id": direction_id,
                "split": "pilot",
                "c0": c0,
                "initial_state": {
                    "x": state.x.tolist(),
                    "s": state.s.tolist(),
                    "q": state.q.tolist(),
                },
            }
            result[config_id] = _canonical_hash(payload)
    return result


def independent_reference_trajectory(
    initial_state: State,
    params: Parameters,
    model: str,
    *,
    c0: float,
    dt: float,
    horizon: float,
    observation_interval: float,
) -> np.ndarray:
    steps = int(round(horizon / dt))
    stride = int(round(observation_interval / dt))
    if not np.isclose(steps * dt, horizon, rtol=0.0, atol=1.0e-12):
        raise ValueError("invalid independent horizon")
    if stride <= 0 or not np.isclose(stride * dt, observation_interval, rtol=0.0, atol=1.0e-12):
        raise ValueError("invalid independent observation interval")
    state = initial_state
    rows = [state.pack()]
    for step in range(steps):
        state = reference_rk4_step(
            state,
            params,
            dt,
            model,
            c0=c0 if model in {"mp", "mfp"} else None,
        )
        if (step + 1) % stride == 0:
            rows.append(state.pack())
    return np.asarray(rows, dtype=np.float64)


def independent_file_hashes(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.name == "checksums.sha256":
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        result[str(path.relative_to(root))] = digest
    return result
