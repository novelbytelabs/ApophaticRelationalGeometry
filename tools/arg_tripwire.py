#!/usr/bin/env python3
"""Independent ARG defensive tripwire for a clean repository checkout.

This is deliberately separate from the production test suite. It checks that
critical manifests are non-empty and hash-valid, that no execution data or
authorization exists, that generated model outputs are nonconstant and match a
separately written reference, and that the new defensive guards fail closed.
"""

from __future__ import annotations

import argparse
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any

import numpy as np


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_json_sha256(path: Path) -> str:
    value = json.loads(
        path.read_text(encoding="utf-8"),
        parse_constant=lambda token: (_ for _ in ()).throw(
            ValueError(f"non-standard JSON constant: {token}")
        ),
    )
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def check_lock(root: Path, path: Path) -> None:
    lock = json.loads(path.read_text(encoding="utf-8"))
    files = lock.get("files")
    if not isinstance(files, dict) or not files:
        raise AssertionError(f"empty lock file set: {path}")
    for relative, expected in files.items():
        target = (root / relative).resolve(strict=True)
        target.relative_to(root)
        actual = canonical_json_sha256(target) if target.suffix == ".json" else sha256(target)
        if actual != expected:
            raise AssertionError(f"lock mismatch: {relative}")


def run_probe(root: Path) -> dict[str, Any]:
    sys.path.insert(0, str(root / "src"))
    sys.path.insert(0, str(root))
    from apophatic_geometry.attestation import AttestationError, require_clean_tracked_tree
    from apophatic_geometry.model import Parameters, State
    from apophatic_geometry.models import ModelId, ProjectionTarget, derivatives_for_model, rk4_step
    from apophatic_geometry.pilot import PilotArchiveWriter, frozen_parameters, integrate_rk4, load_frozen_bundle, smoke_configuration
    from tests.reference_equations import reference_derivative, reference_rk4_step

    report: dict[str, Any] = {}
    params = Parameters()
    state = State(
        x=np.array([0.8, -0.25, 0.45]),
        s=np.array([0.2, -0.1, 0.1]),
        q=np.array([0.0, 0.05, -0.05]),
    )
    changed = State(x=state.x + np.array([0.01, 0.0, 0.0]), s=state.s, q=state.q)
    report["nonconstant_output"] = not np.array_equal(
        derivatives_for_model(state, params, ModelId.MF).pack(),
        derivatives_for_model(changed, params, ModelId.MF).pack(),
    )

    rng = np.random.Generator(np.random.PCG64(20260801))
    max_derivative = 0.0
    max_step = 0.0
    for _ in range(32):
        x = rng.normal(size=3)
        x = x / np.linalg.norm(x) * rng.uniform(np.sqrt(3e-6), np.sqrt(3.0))
        sample = State(x=x, s=rng.uniform(-2, 2, 3), q=rng.uniform(-1, 1, 3))
        target = ProjectionTarget.from_state(sample)
        for model in ModelId:
            projected = model in {ModelId.MP, ModelId.MFP}
            kwargs = {"target": target} if projected else {}
            got = derivatives_for_model(sample, params, model, **kwargs).pack()
            ref = reference_derivative(
                sample,
                params,
                model.value,
                c0=target.c0 if projected else None,
            ).pack()
            max_derivative = max(max_derivative, float(np.max(np.abs(got - ref))))
            np.testing.assert_allclose(got, ref, rtol=1e-12, atol=1e-13)
            got_step = rk4_step(sample, params, 0.001, model, **kwargs).pack()
            ref_step = reference_rk4_step(
                sample,
                params,
                0.001,
                model.value,
                c0=target.c0 if projected else None,
            ).pack()
            max_step = max(max_step, float(np.max(np.abs(got_step - ref_step))))
            np.testing.assert_allclose(got_step, ref_step, rtol=1e-12, atol=1e-13)
    report["differential_max_derivative_abs"] = max_derivative
    report["differential_max_step_abs"] = max_step

    raw = np.array([1.0, 2.0, 3.0])
    frozen = State(x=raw, s=np.zeros(3), q=np.zeros(3))
    raw[0] = 9.0
    report["state_immutable"] = frozen.x[0] == 1.0 and not frozen.x.flags.writeable

    shadow = root / "numpy.py"
    if shadow.exists():
        raise AssertionError("unexpected pre-existing shadow file")
    shadow.write_text("raise RuntimeError('shadow')\n", encoding="utf-8")
    try:
        try:
            require_clean_tracked_tree(root)
        except AttestationError:
            report["untracked_shadow_rejected"] = True
        else:
            report["untracked_shadow_rejected"] = False
    finally:
        shadow.unlink(missing_ok=True)

    bundle = load_frozen_bundle(root)
    smoke = smoke_configuration(bundle)
    trajectory = integrate_rk4(
        smoke,
        frozen_parameters(bundle),
        ModelId.MF,
        dt=0.001,
        horizon=0.001,
        observation_interval=0.001,
        source_commit="tripwire",
    )
    report["trajectory_arrays_read_only"] = all(
        not array.flags.writeable for array in trajectory.raw_arrays().values()
    )

    manifest = {
        "runner_id": "ARG-P6-PILOT-RUNNER-v1",
        "runner_version": "1.1.0",
        "protocol_id": "ARG-P5-COMP-v1",
        "protocol_version": "1.0.0",
        "split": "pilot",
        "configuration_count": 1,
        "configuration_hashes": {"tripwire": "1" * 64},
        "expected_trajectory_records": 1,
        "expected_summary_records": 1,
        "confirmatory_execution": "BLOCKED",
        "run_identity_sha256": "2" * 64,
        "attestation_sha256": "3" * 64,
        "source_tree_sha256": "4" * 64,
        "runtime_environment_sha256": "5" * 64,
        "protocol_lock": {"file_sha256": "6" * 64},
        "implementation_files": {"tripwire": "7" * 64},
    }
    with tempfile.TemporaryDirectory(prefix="arg-tripwire-archive-") as temporary:
        writer = PilotArchiveWriter(Path(temporary) / "archive", manifest)
        try:
            writer.finalize()
        except RuntimeError:
            report["empty_archive_rejected"] = True
        else:
            report["empty_archive_rejected"] = False

    if not all(value is True for key, value in report.items() if isinstance(value, bool)):
        raise AssertionError(report)
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    if not (root / ".git").exists():
        raise SystemExit("tripwire requires a clean Git checkout")
    if (root / "protocol/phase6_runner_v1/EXECUTION_AUTHORIZATION.json").exists():
        raise SystemExit("execution authorization is forbidden during hardening")
    if (root / "artifacts/phase6_pilot").exists():
        raise SystemExit("pilot artifacts are forbidden during hardening")

    check_lock(root, root / "protocol/phase5_v1/LOCK.json")
    check_lock(root, root / "protocol/phase6_runner_v1/INTEGRITY_BASELINE.json")

    tests = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=root,
        env={
            "PATH": __import__("os").environ.get("PATH", ""),
            "PYTHONPATH": f"{root / 'src'}:{root}",
            "PYTHONNOUSERSITE": "1",
            "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1",
            "PYTHONHASHSEED": "0",
            "OMP_NUM_THREADS": "1",
            "OPENBLAS_NUM_THREADS": "1",
            "MKL_NUM_THREADS": "1",
        },
        text=True,
        capture_output=True,
        timeout=180,
    )
    if tests.returncode != 0:
        raise SystemExit(tests.stdout + tests.stderr)

    report = run_probe(root)
    print(json.dumps(report, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
