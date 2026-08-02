#!/usr/bin/env python3
"""Run the blinded full-pilot H6 conditioning diagnostic.

This tool integrates only the frozen pilot MP trajectories at the protocol's
reference RK4 step and evaluates the exact same-state node identity. It never
computes the primary MF-vs-MP effect, never opens the confirmatory split, and
never writes a scientific result archive.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
from typing import Any

from apophatic_geometry.model import State
from apophatic_geometry.models import ModelId
from apophatic_geometry.pilot_gates import same_state_identity_assessment
from apophatic_geometry.pilot_integrators import integrate_rk4
from apophatic_geometry.pilot_manifest import (
    build_pilot_configurations,
    frozen_parameters,
    load_frozen_bundle,
)


def _source_commit(root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError("H6 diagnostic requires a Git checkout")
    return result.stdout.strip()


def run(repo_root: Path) -> dict[str, Any]:
    root = repo_root.resolve(strict=True)
    bundle = load_frozen_bundle(root)
    params = frozen_parameters(bundle)
    configurations = build_pilot_configurations(bundle)
    policy = bundle.protocol["time_and_sampling"]
    horizon = float(policy["horizon"])
    observation_interval = float(policy["observation_interval"])
    reference_dt = float(policy["reference_rk4_dt"])
    commit = _source_commit(root)

    records: list[dict[str, Any]] = []
    all_passed = True
    for configuration in configurations:
        trajectory = integrate_rk4(
            configuration,
            params,
            ModelId.MP,
            bundle=bundle,
            dt=reference_dt,
            horizon=horizon,
            observation_interval=observation_interval,
            source_commit=commit,
        )
        assessments = [
            same_state_identity_assessment(
                State.unpack(vector), params, configuration.c0
            )
            for vector in trajectory.states
        ]
        passed = all(item.passed for item in assessments)
        all_passed = all_passed and passed
        records.append(
            {
                "config_id": configuration.config_id,
                "direction_id": configuration.direction_id,
                "configuration_hash": configuration.configuration_hash,
                "passed": passed,
                "cancellation_dominated_observations": sum(
                    item.regime == "cancellation_dominated"
                    for item in assessments
                ),
                "maximum_absolute_error": max(
                    item.absolute_error for item in assessments
                ),
                "maximum_forward_relative_error": max(
                    item.forward_relative_error for item in assessments
                ),
                "maximum_backward_error": max(
                    item.backward_error for item in assessments
                ),
                "maximum_radiality_error": max(
                    item.radiality_error for item in assessments
                ),
                "minimum_conditioning_ratio": min(
                    item.conditioning_ratio for item in assessments
                ),
            }
        )

    result = {
        "diagnostic_id": "ARG-P6B2-H6-CONDITIONING-v1",
        "source_commit": commit,
        "protocol_id": bundle.protocol["protocol_id"],
        "protocol_version": bundle.protocol["protocol_version"],
        "split": "pilot",
        "model": "mp",
        "integrator": "RK4",
        "dt": reference_dt,
        "horizon": horizon,
        "observation_interval": observation_interval,
        "configuration_count": len(records),
        "primary_effect_computed": False,
        "confirmatory_access": False,
        "passed": all_passed,
        "configurations": records,
    }
    if not all_passed:
        raise RuntimeError(json.dumps(result, sort_keys=True, allow_nan=False))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.repo_root)
    rendered = json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n"
    if args.output is not None:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
