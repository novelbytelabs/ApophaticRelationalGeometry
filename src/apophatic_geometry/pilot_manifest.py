"""Frozen-manifest loading, pilot reconstruction, and execution authorization."""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import re
import subprocess
from typing import Any, Mapping, Sequence

import numpy as np

from .model import Parameters, State, collective_mode
from .models import CONTRACT_VERSION
from .pilot_types import (
    CONFIRMATORY_SPLIT,
    EXECUTION_AUTHORIZATION_PATH,
    EXPECTED_PILOT_CONFIGURATIONS,
    EXPECTED_PILOT_DIRECTIONS,
    PILOT_SPLIT,
    RUNNER_ID,
    RUNNER_VERSION,
    SMOKE_SPLIT,
    ConfirmatoryAccessError,
    FrozenProtocolBundle,
    PilotConfiguration,
    ProtocolIntegrityError,
)
from .protocol import (
    PROTOCOL_ID,
    PROTOCOL_VERSION,
    canonical_json_sha256,
    load_json,
    validate_initial_condition_manifest,
    validate_protocol_manifest,
    verify_lock,
)

INTEGRITY_BASELINE_PATH = Path(
    "protocol/phase6_runner_v1/INTEGRITY_BASELINE.json"
)
EXECUTION_ENVIRONMENT_PATH = Path(
    "protocol/phase6_runner_v1/EXECUTION_ENVIRONMENT.json"
)
_HEX_40 = re.compile(r"^[0-9a-f]{40}$")
_HEX_64 = re.compile(r"^[0-9a-f]{64}$")


def _strict_json(path: Path) -> Mapping[str, Any]:
    value = load_json(path)
    if not isinstance(value, Mapping):
        raise ProtocolIntegrityError(f"expected JSON object: {path}")
    return value


def _all_permutations() -> tuple[tuple[int, int, int], ...]:
    return (
        (0, 1, 2),
        (0, 2, 1),
        (1, 0, 2),
        (1, 2, 0),
        (2, 0, 1),
        (2, 1, 0),
    )


def _validate_parameter_manifest(manifest: Mapping[str, Any]) -> None:
    if manifest.get("protocol_id") != PROTOCOL_ID:
        raise ValueError("parameter manifest has wrong protocol_id")
    if manifest.get("status") != "FROZEN_NO_FITTING":
        raise ValueError("parameter manifest is not frozen")
    policy = manifest.get("policy")
    if not isinstance(policy, Mapping):
        raise ValueError("parameter policy is missing")
    if policy.get("fitting") != "none" or policy.get("tuning") != "none":
        raise ValueError("parameter fitting or tuning is not permitted")
    raw = manifest.get("parameters")
    if not isinstance(raw, Mapping) or set(raw) != set(asdict(Parameters())):
        raise ValueError("parameter keys differ from the frozen model")
    params = Parameters(**{name: float(value) for name, value in raw.items()})
    params.validate()
    if not all(np.isfinite(value) for value in asdict(params).values()):
        raise ValueError("parameter manifest contains non-finite values")


def _validate_intervention_manifest(manifest: Mapping[str, Any]) -> None:
    if manifest.get("protocol_id") != PROTOCOL_ID:
        raise ValueError("intervention manifest has wrong protocol_id")
    if manifest.get("status") != "FROZEN_NO_EXECUTION":
        raise ValueError("intervention manifest is not frozen")
    permutations = manifest.get("relabeling_tripwire", {}).get("permutations")
    expected = [list(value) for value in _all_permutations()]
    if permutations != expected:
        raise ValueError("relabeling permutation schedule differs from the frozen protocol")
    ablations = manifest.get("adaptive_substrate_ablations")
    ids = (
        {str(entry.get("id")) for entry in ablations}
        if isinstance(ablations, list)
        else set()
    )
    if ids != {"freeze_s", "freeze_q", "freeze_sq"}:
        raise ValueError("adaptive-substrate ablation schedule differs from the frozen protocol")


def load_frozen_bundle(repo_root: str | Path) -> FrozenProtocolBundle:
    """Verify LOCK.json before loading any configuration-bearing manifest."""

    root = Path(repo_root).resolve()
    protocol_root = root / "protocol" / "phase5_v1"
    lock = _strict_json(protocol_root / "LOCK.json")
    try:
        verify_lock(root, lock)
    except (OSError, ValueError, TypeError) as exc:
        raise ProtocolIntegrityError(str(exc)) from exc

    protocol = _strict_json(protocol_root / "protocol.json")
    parameters = _strict_json(protocol_root / "parameters.json")
    initial_conditions = _strict_json(protocol_root / "initial_conditions.json")
    interventions = _strict_json(protocol_root / "interventions.json")
    try:
        validate_protocol_manifest(protocol)
        validate_initial_condition_manifest(initial_conditions)
        _validate_parameter_manifest(parameters)
        _validate_intervention_manifest(interventions)
    except (ValueError, TypeError, KeyError) as exc:
        raise ProtocolIntegrityError(str(exc)) from exc
    return FrozenProtocolBundle(
        repo_root=root,
        protocol=protocol,
        parameters=parameters,
        initial_conditions=initial_conditions,
        interventions=interventions,
        lock=lock,
    )


def frozen_parameters(bundle: FrozenProtocolBundle) -> Parameters:
    raw = bundle.parameters["parameters"]
    if not isinstance(raw, Mapping):
        raise ProtocolIntegrityError("frozen parameters are missing")
    return Parameters(**{name: float(value) for name, value in raw.items()})


def configuration_payload(
    config_id: str,
    direction_id: str,
    split: str,
    c0: float,
    state: State,
) -> dict[str, Any]:
    return {
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "contract_version": CONTRACT_VERSION,
        "config_id": config_id,
        "direction_id": direction_id,
        "split": split,
        "c0": float(c0),
        "initial_state": {
            "x": state.x.tolist(),
            "s": state.s.tolist(),
            "q": state.q.tolist(),
        },
    }


def build_pilot_configurations(
    bundle: FrozenProtocolBundle,
) -> tuple[PilotConfiguration, ...]:
    """Reconstruct exactly the 50 pilot configurations and no others."""

    manifest = bundle.initial_conditions
    directions = manifest["directions"]
    generation = manifest["generation"]
    rule = manifest["configuration_rule"]
    c0_levels = [float(value) for value in generation["c0_levels"]]
    tags = {str(key): str(value) for key, value in rule["c0_tags"].items()}
    s0 = np.asarray(generation["shared_s0"], dtype=np.float64)
    q0 = np.asarray(generation["shared_q0"], dtype=np.float64)

    configurations: list[PilotConfiguration] = []
    for entry in directions:
        if entry.get("split") != PILOT_SPLIT:
            continue
        direction_id = str(entry["direction_id"])
        direction = np.asarray(entry["unit_vector"], dtype=np.float64)
        for c0 in c0_levels:
            tag = tags.get(str(c0)) or tags.get(format(c0, ".1f"))
            if tag is None:
                raise ProtocolIntegrityError(f"missing c0 tag for {c0}")
            config_id = f"p5-{direction_id}-c{tag}"
            state = State(
                x=np.sqrt(3.0 * c0) * direction,
                s=s0.copy(),
                q=q0.copy(),
            )
            payload = configuration_payload(
                config_id, direction_id, PILOT_SPLIT, c0, state
            )
            configurations.append(
                PilotConfiguration(
                    config_id=config_id,
                    direction_id=direction_id,
                    split=PILOT_SPLIT,
                    c0=c0,
                    initial_state=state,
                    configuration_hash=canonical_json_sha256(payload),
                )
            )

    configurations.sort(key=lambda item: item.config_id)
    ids = [item.config_id for item in configurations]
    directions_seen = {item.direction_id for item in configurations}
    if len(configurations) != EXPECTED_PILOT_CONFIGURATIONS:
        raise ProtocolIntegrityError("pilot configuration reconstruction is incomplete")
    if len(set(ids)) != len(ids):
        raise ProtocolIntegrityError("pilot configuration reconstruction contains duplicates")
    if len(directions_seen) != EXPECTED_PILOT_DIRECTIONS:
        raise ProtocolIntegrityError("pilot direction reconstruction is incomplete")
    if any(item.split != PILOT_SPLIT for item in configurations):
        raise ConfirmatoryAccessError("non-pilot configuration entered the pilot plan")
    return tuple(configurations)


def smoke_configuration(bundle: FrozenProtocolBundle) -> PilotConfiguration:
    """Return the manifest-declared smoke-only state, excluded from inference."""

    smoke = bundle.initial_conditions.get("smoke_only")
    if not isinstance(smoke, Mapping) or smoke.get("excluded_from_inference") is not True:
        raise ProtocolIntegrityError("smoke-only configuration is missing or not excluded")
    state = State(
        x=np.asarray(smoke["x0"], dtype=np.float64),
        s=np.asarray(smoke["s0"], dtype=np.float64),
        q=np.asarray(smoke["q0"], dtype=np.float64),
    )
    c0 = collective_mode(state.x)
    payload = configuration_payload(
        "smoke-only", "smoke-only", SMOKE_SPLIT, c0, state
    )
    return PilotConfiguration(
        config_id="smoke-only",
        direction_id="smoke-only",
        split=SMOKE_SPLIT,
        c0=c0,
        initial_state=state,
        configuration_hash=canonical_json_sha256(payload),
    )


def authorize_pilot_batch(
    configurations: Sequence[PilotConfiguration],
) -> tuple[PilotConfiguration, ...]:
    """Reject mixed or confirmatory input before any integration begins."""

    batch = tuple(configurations)
    if not batch:
        raise ConfirmatoryAccessError("empty pilot batch is not authorized")
    if any(item.split != PILOT_SPLIT for item in batch):
        raise ConfirmatoryAccessError("pilot runner accepts pilot configurations only")
    ids = [item.config_id for item in batch]
    if len(set(ids)) != len(ids):
        raise ConfirmatoryAccessError("duplicate configuration identifiers are not authorized")
    return batch


def require_complete_pilot_batch(
    configurations: Sequence[PilotConfiguration],
) -> tuple[PilotConfiguration, ...]:
    batch = authorize_pilot_batch(configurations)
    if len(batch) != EXPECTED_PILOT_CONFIGURATIONS:
        raise ConfirmatoryAccessError(
            f"full pilot execution requires exactly {EXPECTED_PILOT_CONFIGURATIONS} configurations"
        )
    if len({item.direction_id for item in batch}) != EXPECTED_PILOT_DIRECTIONS:
        raise ConfirmatoryAccessError("full pilot execution requires all frozen pilot directions")
    return batch


def _run_git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def _verify_integrity_baseline(root: Path, phase4_commit: str) -> Mapping[str, Any]:
    path = root / INTEGRITY_BASELINE_PATH
    if not path.is_file():
        raise ProtocolIntegrityError("remediated integrity baseline is missing")
    baseline = _strict_json(path)
    required = {
        "baseline_id": "ARG-P6-INTEGRITY-BASELINE-v1",
        "status": "FROZEN_NO_EXECUTION",
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "phase4_model_implementation_commit": phase4_commit,
        "scientific_equations_changed": False,
        "trajectory_data_generated": False,
        "confirmatory_execution": "BLOCKED",
    }
    for key, expected in required.items():
        if baseline.get(key) != expected:
            raise ProtocolIntegrityError(f"integrity baseline mismatch: {key}")
    files = baseline.get("files")
    if not isinstance(files, Mapping) or not files:
        raise ProtocolIntegrityError("integrity baseline file set is missing")
    if any(
        not isinstance(path_name, str)
        or not isinstance(digest, str)
        or _HEX_64.fullmatch(digest) is None
        for path_name, digest in files.items()
    ):
        raise ProtocolIntegrityError("integrity baseline contains an invalid path or digest")
    try:
        verify_lock(root, {"protocol_id": PROTOCOL_ID, "files": dict(files)})
    except (OSError, ValueError, TypeError) as exc:
        raise ProtocolIntegrityError(f"integrity baseline verification failed: {exc}") from exc
    return baseline


def verify_model_baseline(repo_root: str | Path, protocol: Mapping[str, Any]) -> str:
    """Verify unchanged canonical equations plus the remediated integrity baseline."""

    root = Path(repo_root).resolve()
    phase4_commit = str(protocol.get("model_implementation_commit", ""))
    if _HEX_40.fullmatch(phase4_commit) is None:
        raise ProtocolIntegrityError("model implementation commit is missing")
    top = _run_git(root, "rev-parse", "--show-toplevel")
    if top.returncode != 0 or Path(top.stdout.strip()).resolve() != root:
        raise ProtocolIntegrityError("runner requires the repository root of a Git checkout")
    present = _run_git(root, "cat-file", "-e", f"{phase4_commit}^{{commit}}")
    if present.returncode != 0:
        raise ProtocolIntegrityError("model baseline commit is unavailable; fetch full history")

    # The canonical four-model equations remain byte-identical to Phase 4.
    # model.py may differ only through the separately frozen integrity baseline,
    # because Phase 6A.1 adds domain guards and immutable state handling there.
    changed_equations = _run_git(
        root,
        "diff",
        "--quiet",
        phase4_commit,
        "--",
        "src/apophatic_geometry/models.py",
    )
    if changed_equations.returncode != 0:
        raise ProtocolIntegrityError(
            "canonical model equations differ from the frozen Phase 4 baseline"
        )
    _verify_integrity_baseline(root, phase4_commit)

    dirty = _run_git(root, "status", "--porcelain", "--untracked-files=no")
    if dirty.returncode != 0 or dirty.stdout.strip():
        raise ProtocolIntegrityError("pilot execution requires a clean tracked working tree")
    head = _run_git(root, "rev-parse", "HEAD")
    source_commit = head.stdout.strip()
    if head.returncode != 0 or _HEX_40.fullmatch(source_commit) is None:
        raise ProtocolIntegrityError("unable to resolve source commit")
    return source_commit


def validate_execution_authorization(
    repo_root: str | Path,
    source_commit: str,
) -> Mapping[str, Any]:
    """Require a committed authorization for an already verified runner commit."""

    root = Path(repo_root).resolve()
    path = root / EXECUTION_AUTHORIZATION_PATH
    if not path.is_file():
        raise ProtocolIntegrityError(
            "pilot execution record is absent; runner verification does not authorize execution"
        )
    authorization = _strict_json(path)
    required = {
        "authorization_id": "ARG-P6-PILOT-EXEC-v1",
        "status": "AUTHORIZED",
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "runner_id": RUNNER_ID,
        "runner_version": RUNNER_VERSION,
        "split": PILOT_SPLIT,
        "confirmatory_execution": "BLOCKED",
    }
    for key, expected in required.items():
        if authorization.get(key) != expected:
            raise ProtocolIntegrityError(f"execution authorization mismatch: {key}")
    for key in ("execution_id", "execution_utc"):
        if not isinstance(authorization.get(key), str) or not authorization[key]:
            raise ProtocolIntegrityError(f"execution authorization lacks {key}")

    runner_commit = str(authorization.get("runner_source_commit", ""))
    if _HEX_40.fullmatch(runner_commit) is None:
        raise ProtocolIntegrityError("execution authorization lacks runner_source_commit")
    if _HEX_40.fullmatch(source_commit) is None:
        raise ProtocolIntegrityError("execution source commit is invalid")
    present = _run_git(root, "cat-file", "-e", f"{runner_commit}^{{commit}}")
    if present.returncode != 0:
        raise ProtocolIntegrityError("authorized runner commit is unavailable")
    ancestor = _run_git(root, "merge-base", "--is-ancestor", runner_commit, source_commit)
    if ancestor.returncode != 0:
        raise ProtocolIntegrityError("authorized runner commit is not an ancestor of execution")

    protected_paths = (
        "src/apophatic_geometry/model.py",
        "src/apophatic_geometry/models.py",
        "src/apophatic_geometry/protocol.py",
        "src/apophatic_geometry/attestation.py",
        "src/apophatic_geometry/pilot_types.py",
        "src/apophatic_geometry/pilot_manifest.py",
        "src/apophatic_geometry/pilot_mechanisms.py",
        "src/apophatic_geometry/pilot_integrators.py",
        "src/apophatic_geometry/pilot_gates.py",
        "src/apophatic_geometry/pilot_integrate.py",
        "src/apophatic_geometry/pilot_archive.py",
        "src/apophatic_geometry/pilot.py",
        "src/apophatic_geometry/pilot_cli.py",
        "protocol/phase5_v1",
        str(INTEGRITY_BASELINE_PATH),
        str(EXECUTION_ENVIRONMENT_PATH),
    )
    changed = _run_git(
        root,
        "diff",
        "--quiet",
        runner_commit,
        source_commit,
        "--",
        *protected_paths,
    )
    if changed.returncode != 0:
        raise ProtocolIntegrityError(
            "runner, integrity baseline, environment policy, or frozen protocol changed after authorization"
        )
    tracked = _run_git(
        root,
        "ls-files",
        "--error-unmatch",
        str(EXECUTION_AUTHORIZATION_PATH),
    )
    if tracked.returncode != 0:
        raise ProtocolIntegrityError("execution authorization must be committed")
    return authorization


def validate_execution_environment_policy(
    repo_root: str | Path,
    runtime: Mapping[str, Any],
    *,
    require_execution_clearance: bool,
) -> Mapping[str, Any]:
    """Validate exact execution versions and the explicit external-clearance state."""

    root = Path(repo_root).resolve()
    policy = _strict_json(root / EXECUTION_ENVIRONMENT_PATH)
    required = {
        "environment_id": "ARG-P6-EXEC-ENV-v1",
        "protocol_id": PROTOCOL_ID,
        "runner_id": RUNNER_ID,
        "confirmatory_execution": "BLOCKED",
    }
    for key, expected in required.items():
        if policy.get(key) != expected:
            raise ProtocolIntegrityError(f"execution environment policy mismatch: {key}")

    python_policy = policy.get("execution_python")
    distributions_policy = policy.get("runtime_distributions")
    distributions_runtime = runtime.get("distributions")
    if not isinstance(python_policy, Mapping):
        raise ProtocolIntegrityError("execution Python policy is missing")
    if not isinstance(distributions_policy, Mapping):
        raise ProtocolIntegrityError("execution distribution policy is missing")
    if not isinstance(distributions_runtime, Mapping):
        raise ProtocolIntegrityError("runtime distribution attestation is missing")

    if runtime.get("python_implementation") != python_policy.get("implementation"):
        raise ProtocolIntegrityError("Python implementation differs from execution policy")
    if runtime.get("python_version") != python_policy.get("version"):
        raise ProtocolIntegrityError("Python version differs from execution policy")
    for name, expected_version in distributions_policy.items():
        entry = distributions_runtime.get(name)
        if not isinstance(entry, Mapping) or entry.get("version") != expected_version:
            raise ProtocolIntegrityError(
                f"runtime distribution differs from execution policy: {name}"
            )
        digest = entry.get("installed_tree_sha256")
        if not isinstance(digest, str) or _HEX_64.fullmatch(digest) is None:
            raise ProtocolIntegrityError(
                f"runtime distribution lacks an installed-byte fingerprint: {name}"
            )

    if require_execution_clearance:
        if policy.get("status") != "CLEARED_AFTER_PHASE6A1_EXTERNAL_AUDIT":
            raise ProtocolIntegrityError("Phase 6A.1 external audit clearance is absent")
        if policy.get("pilot_execution") != "AUTHORIZED_ONLY_WITH_EXECUTION_RECORD":
            raise ProtocolIntegrityError("pilot execution remains blocked by environment policy")
    return policy
