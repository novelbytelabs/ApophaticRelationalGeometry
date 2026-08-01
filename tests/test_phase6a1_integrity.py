from __future__ import annotations

import csv
import json
import os
from pathlib import Path
import re

import numpy as np
import pytest

from apophatic_geometry.attestation import build_attestation
from apophatic_geometry.model import (
    Parameters,
    State,
    conductances,
    intrinsic_edge_lengths,
    sigmoid,
)
from apophatic_geometry.protocol import (
    PROTOCOL_ID,
    file_sha256,
    load_json,
    verify_lock,
)
from apophatic_geometry import simulate


REPO_ROOT = Path(__file__).resolve().parents[1]


def _fake_attestation(source_marker: str = "a") -> dict[str, object]:
    marker = source_marker * 64
    return {
        "attestation_version": "TEST-FIXTURE-NOT-SCIENTIFIC-EVIDENCE",
        "source_commit": "1" * 40,
        "source_tree_sha256": marker,
        "protocol_lock": {"file_sha256": "2" * 64},
        "runtime_environment_sha256": "3" * 64,
        "attestation_sha256": marker,
    }


def test_state_copies_inputs_and_exposes_read_only_arrays() -> None:
    input_x = np.array([1.0, 2.0, 3.0])
    input_s = np.array([0.1, 0.2, 0.3])
    input_q = np.array([-0.1, 0.0, 0.1])
    state = State(x=input_x, s=input_s, q=input_q)

    input_x[0] = 99.0
    input_s[1] = 88.0
    input_q[2] = 77.0

    assert state.x.tolist() == [1.0, 2.0, 3.0]
    assert state.s.tolist() == [0.1, 0.2, 0.3]
    assert state.q.tolist() == [-0.1, 0.0, 0.1]
    assert not state.x.flags.writeable
    assert not state.s.flags.writeable
    assert not state.q.flags.writeable

    with pytest.raises(ValueError):
        state.x[0] = -1.0
    with pytest.raises(ValueError):
        state.s[0] = -1.0
    with pytest.raises(ValueError):
        state.q[0] = -1.0


def test_extreme_finite_geometry_fails_closed() -> None:
    params = Parameters()
    for q_value in (-1000.0, 1000.0):
        state = State(
            x=np.array([1.0, 0.0, -1.0]),
            s=np.zeros(3),
            q=np.full(3, q_value),
        )
        with pytest.raises(FloatingPointError):
            conductances(state)
        with pytest.raises(FloatingPointError):
            intrinsic_edge_lengths(state, params)


@pytest.mark.parametrize("s_value", [-1000.0, 1000.0])
def test_extreme_finite_sigmoid_fails_closed(s_value: float) -> None:
    with pytest.raises(FloatingPointError):
        sigmoid(np.full(3, s_value))


@pytest.mark.parametrize("token", ["NaN", "Infinity", "-Infinity"])
def test_strict_json_rejects_nonstandard_constants(
    tmp_path: Path, token: str
) -> None:
    path = tmp_path / "invalid.json"
    path.write_text(f'{{"value": {token}}}', encoding="utf-8")
    with pytest.raises(ValueError, match="non-standard JSON constant"):
        load_json(path)


def test_lock_verification_accepts_only_root_confined_regular_files(
    tmp_path: Path,
) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    inside = root / "inside.txt"
    inside.write_text("inside", encoding="utf-8")
    valid = {
        "protocol_id": PROTOCOL_ID,
        "files": {"inside.txt": file_sha256(inside)},
    }
    verify_lock(root, valid)

    outside = tmp_path / "outside.txt"
    outside.write_text("outside", encoding="utf-8")
    traversal = {
        "protocol_id": PROTOCOL_ID,
        "files": {"../outside.txt": file_sha256(outside)},
    }
    with pytest.raises(ValueError, match="escapes repository root"):
        verify_lock(root, traversal)

    absolute = {
        "protocol_id": PROTOCOL_ID,
        "files": {str(outside.resolve()): file_sha256(outside)},
    }
    with pytest.raises(ValueError, match="must be non-empty and relative"):
        verify_lock(root, absolute)

    if hasattr(os, "symlink"):
        link = root / "outside-link.txt"
        try:
            link.symlink_to(outside)
        except OSError:
            return
        symlink_escape = {
            "protocol_id": PROTOCOL_ID,
            "files": {"outside-link.txt": file_sha256(outside)},
        }
        with pytest.raises(ValueError, match="escapes repository root"):
            verify_lock(root, symlink_escape)


def test_attestation_derives_commit_and_ignores_source_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("ARG_SOURCE_COMMIT", "deadbeef")
    attestation = build_attestation(
        REPO_ROOT,
        integrator="audit-test-integrator",
        implementation_paths=("src/apophatic_geometry/attestation.py",),
    )
    source_commit = str(attestation["source_commit"])
    assert re.fullmatch(r"[0-9a-f]{40}", source_commit)
    assert source_commit != "deadbeef"
    assert len(str(attestation["source_tree_sha256"])) == 64
    assert len(str(attestation["runtime_environment_sha256"])) == 64
    assert len(str(attestation["attestation_sha256"])) == 64


def test_failed_simulation_leaves_no_final_artifact(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(simulate, "build_attestation", lambda *args, **kwargs: _fake_attestation())
    output = tmp_path / "failed.csv"
    completion = Path(f"{output}.complete.json")

    with pytest.raises((FloatingPointError, ValueError)):
        simulate.run(
            steps=1,
            dt=np.finfo(np.float64).max,
            output=output,
            model="mf",
            repo_root=REPO_ROOT,
        )

    assert not output.exists()
    assert not completion.exists()
    assert not list(tmp_path.glob("*.tmp"))
    assert not list(tmp_path.glob(".*.tmp"))


def test_successful_simulation_is_completion_attested_and_hash_bound(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    current = {"value": _fake_attestation("a")}
    monkeypatch.setattr(
        simulate,
        "build_attestation",
        lambda *args, **kwargs: current["value"],
    )

    first = tmp_path / "first.csv"
    first_manifest = simulate.run(
        steps=1,
        dt=0.005,
        output=first,
        model="mf",
        repo_root=REPO_ROOT,
    )
    assert first.exists()
    first_completion = Path(f"{first}.complete.json")
    assert first_completion.exists()
    loaded = load_json(first_completion)
    assert loaded == first_manifest
    assert loaded["completion_status"] == "COMPLETE"
    assert loaded["expected_data_rows"] == 2
    assert loaded["actual_data_rows"] == 2
    assert loaded["output_sha256"] == file_sha256(first)

    with first.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 2
    assert {row["integrator"] for row in rows} == {simulate.INTEGRATOR_ID}
    assert {row["protocol_id"] for row in rows} == {
        simulate.STANDALONE_PROTOCOL_ID
    }
    first_configuration_hash = rows[0]["configuration_hash"]
    first_execution_hash = rows[0]["execution_hash"]

    current["value"] = _fake_attestation("b")
    second = tmp_path / "second.csv"
    simulate.run(
        steps=1,
        dt=0.005,
        output=second,
        model="mf",
        repo_root=REPO_ROOT,
    )
    with second.open("r", encoding="utf-8", newline="") as handle:
        second_rows = list(csv.DictReader(handle))

    assert second_rows[0]["configuration_hash"] == first_configuration_hash
    assert second_rows[0]["execution_hash"] != first_execution_hash


def test_completion_manifest_is_standard_json(tmp_path: Path) -> None:
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps({"status": "COMPLETE"}), encoding="utf-8")
    assert load_json(path) == {"status": "COMPLETE"}
