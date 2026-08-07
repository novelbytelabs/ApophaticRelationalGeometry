"""Frozen-manifest loading, pilot reconstruction, and execution authorization."""

from __future__ import annotations

import ast
from dataclasses import asdict
import hashlib
import importlib
import platform
from pathlib import Path
import re
import subprocess
from typing import Any, Mapping, Sequence

import numpy as np

from .attestation import distribution_tree_sha256
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


def require_frozen_configuration(
    bundle: FrozenProtocolBundle,
    configuration: PilotConfiguration,
) -> PilotConfiguration:
    """Require exact frozen pilot or smoke membership before integration."""

    if configuration.split == SMOKE_SPLIT:
        expected = smoke_configuration(bundle)
    elif configuration.split == PILOT_SPLIT:
        expected_by_id = {
            item.config_id: item for item in build_pilot_configurations(bundle)
        }
        expected = expected_by_id.get(configuration.config_id)
        if expected is None:
            raise ConfirmatoryAccessError(
                "configuration is not a frozen pilot member"
            )
    else:
        raise ConfirmatoryAccessError(
            "only exact frozen pilot or smoke configurations may be integrated"
        )

    if configuration.direction_id != expected.direction_id:
        raise ConfirmatoryAccessError("configuration direction differs from frozen membership")
    if configuration.split != expected.split:
        raise ConfirmatoryAccessError("configuration split differs from frozen membership")
    if configuration.configuration_hash != expected.configuration_hash:
        raise ConfirmatoryAccessError("configuration hash differs from frozen membership")
    if configuration.c0 != expected.c0:
        raise ConfirmatoryAccessError("configuration c0 differs from frozen membership")
    if not np.array_equal(
        configuration.initial_state.pack(), expected.initial_state.pack()
    ):
        raise ConfirmatoryAccessError(
            "configuration initial state differs from frozen membership"
        )
    return expected


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


def _models_ast_outside_projector_cleanup(source: str) -> str:
    tree = ast.parse(source)
    retained: list[ast.stmt] = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            aliases = [alias for alias in node.names if alias.name != "math"]
            if not aliases:
                continue
            node = ast.Import(names=aliases)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "project_node_derivative":
            continue
        retained.append(node)
    tree.body = retained
    return ast.dump(tree, annotate_fields=True, include_attributes=False)


def _verify_authorized_projector_remediation(root: Path, phase4_commit: str) -> None:
    historical = _run_git(
        root,
        "show",
        f"{phase4_commit}:src/apophatic_geometry/models.py",
    )
    if historical.returncode != 0 or not historical.stdout:
        raise ProtocolIntegrityError("unable to read the frozen Phase 4 model source")
    current_path = root / "src/apophatic_geometry/models.py"
    current = current_path.read_text(encoding="utf-8")
    if _models_ast_outside_projector_cleanup(historical.stdout) != _models_ast_outside_projector_cleanup(current):
        raise ProtocolIntegrityError(
            "model equations differ outside the authorized projector roundoff remediation"
        )


def _verify_integrity_baseline(root: Path, phase4_commit: str) -> Mapping[str, Any]:
    path = root / INTEGRITY_BASELINE_PATH
    if not path.is_file():
        raise ProtocolIntegrityError("remediated integrity baseline is missing")
    baseline = _strict_json(path)
    required = {
        "baseline_id": "ARG-P6-INTEGRITY-BASELINE-v4",
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
    remediation = baseline.get("numerical_remediation")
    expected_remediation = {
        "remediation_id": "ARG-P6A2-PROJECTOR-ROUNDOFF-v1",
        "trigger": "full-horizon normalized tangency residual 1.0166487685339358e-12 exceeded 1e-12",
        "scope": "binary64 orthogonality cleanup inside project_node_derivative only",
        "scientific_equation_changed": False,
        "protocol_threshold_changed": False,
        "pilot_data_generated": False,
        "confirmatory_execution": "BLOCKED",
    }
    if not isinstance(remediation, Mapping):
        raise ProtocolIntegrityError("projector remediation record is missing")
    for key, expected in expected_remediation.items():
        if remediation.get(key) != expected:
            raise ProtocolIntegrityError(f"projector remediation mismatch: {key}")
    policy = baseline.get("verification_policy")
    if not isinstance(policy, Mapping):
        raise ProtocolIntegrityError("integrity verification policy is missing")
    if policy.get("canonical_equation_file_must_match_phase4") is not False:
        raise ProtocolIntegrityError("projector remediation policy must disable byte identity")
    if policy.get("phase4_equation_scope_ast_must_match_except_project_node_derivative") is not True:
        raise ProtocolIntegrityError("projector remediation scope guard is missing")
    if policy.get("projector_tolerance_unchanged") is not True:
        raise ProtocolIntegrityError("projector tolerance preservation is not recorded")

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

    baseline = _verify_integrity_baseline(root, phase4_commit)
    policy = baseline.get("verification_policy")
    if not isinstance(policy, Mapping):
        raise ProtocolIntegrityError("integrity verification policy is missing")
    if policy.get("canonical_equation_file_must_match_phase4") is True:
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
    elif policy.get("phase4_equation_scope_ast_must_match_except_project_node_derivative") is True:
        _verify_authorized_projector_remediation(root, phase4_commit)
    else:
        raise ProtocolIntegrityError("no valid model-source comparison policy is frozen")

    dirty = _run_git(root, "status", "--porcelain", "--untracked-files=all")
    if dirty.returncode != 0 or dirty.stdout.strip():
        raise ProtocolIntegrityError("pilot execution requires a clean tracked working tree")
    head = _run_git(root, "rev-parse", "HEAD")
    source_commit = head.stdout.strip()
    if head.returncode != 0 or _HEX_40.fullmatch(source_commit) is None:
        raise ProtocolIntegrityError("unable to resolve source commit")
    return source_commit


def _git_tree_hash(root: Path, commit: str) -> str:
    result = _run_git(root, "rev-parse", f"{commit}^{{tree}}")
    value = result.stdout.strip()
    if result.returncode != 0 or _HEX_40.fullmatch(value) is None:
        raise ProtocolIntegrityError("unable to resolve authorized Git tree")
    return value


def _tracked_commit_sha256(root: Path, commit: str) -> str:
    listed = _run_git(root, "ls-tree", "-r", commit)
    if listed.returncode != 0:
        raise ProtocolIntegrityError("unable to enumerate authorized source tree")
    entries = [line for line in listed.stdout.splitlines() if line]
    if not entries:
        raise ProtocolIntegrityError("authorized source tree is empty")
    digest = hashlib.sha256()
    for entry in sorted(entries):
        encoded = entry.encode("utf-8")
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
    return digest.hexdigest()


def validate_execution_authorization(
    repo_root: str | Path,
    source_commit: str,
    *,
    expected_scope: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Require one authorization-only commit on the exact audited Git tree.

    Complete-tree binding includes every tracked byte, including
    ``"src/apophatic_geometry/__init__.py"``; the quoted path is documentary,
    not a hand-maintained authorization allowlist.
    """

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

    # The complete Git tree includes src/apophatic_geometry/__init__.py and
    # every other tracked byte; no hand-maintained executable-file allowlist is used.
    computed_scope = dict(expected_scope) | {
        "runner_source_commit": runner_commit,
        "runner_git_tree": _git_tree_hash(root, runner_commit),
        "runner_source_tree_sha256": _tracked_commit_sha256(
            root, runner_commit
        ),
        "authorization_only_commit_count": 1,
    }
    scope = authorization.get("scope")
    if not isinstance(scope, Mapping):
        raise ProtocolIntegrityError("execution authorization lacks exact scope")
    if dict(scope) != computed_scope:
        raise ProtocolIntegrityError(
            "execution authorization scope differs from exact executable tree"
        )
    scope_sha256 = authorization.get("scope_sha256")
    if scope_sha256 != canonical_json_sha256(computed_scope):
        raise ProtocolIntegrityError("execution authorization scope hash is invalid")

    external_audit = authorization.get("external_audit")
    if not isinstance(external_audit, Mapping):
        raise ProtocolIntegrityError("execution authorization lacks external audit clearance")
    if external_audit.get("verdict") != "CONDITIONAL_PASS":
        raise ProtocolIntegrityError("external audit verdict is not the accepted conditional pass")
    if external_audit.get("clearance") != "USER_AUTHORIZED_EXPLORATORY_PILOT_AFTER_REMEDIATION":
        raise ProtocolIntegrityError(
            "exploratory pilot has not been authorized after audit remediation"
        )
    for key in ("bundle_sha256", "report_sha256", "tripwire_sha256"):
        value = external_audit.get(key)
        if not isinstance(value, str) or _HEX_64.fullmatch(value) is None:
            raise ProtocolIntegrityError(f"external audit clearance lacks {key}")

    parent = _run_git(root, "rev-parse", f"{source_commit}^")
    if parent.returncode != 0 or parent.stdout.strip() != runner_commit:
        raise ProtocolIntegrityError(
            "execution must occur from one authorization-only commit on the audited runner"
        )
    count = _run_git(root, "rev-list", "--count", f"{runner_commit}..{source_commit}")
    if count.returncode != 0 or count.stdout.strip() != "1":
        raise ProtocolIntegrityError(
            "execution source must be exactly one commit after the audited runner"
        )
    changed_names = _run_git(
        root,
        "diff",
        "--name-only",
        runner_commit,
        source_commit,
    )
    changed = {line for line in changed_names.stdout.splitlines() if line}
    if changed_names.returncode != 0 or changed != {str(EXECUTION_AUTHORIZATION_PATH)}:
        raise ProtocolIntegrityError(
            "post-audit execution commit must change only EXECUTION_AUTHORIZATION.json"
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
    """Validate exact platform, imported modules, and execution versions."""

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
    platform_policy = policy.get("platform_policy")
    distributions_policy = policy.get("runtime_distributions")
    distributions_runtime = runtime.get("distributions")
    if not isinstance(python_policy, Mapping):
        raise ProtocolIntegrityError("execution Python policy is missing")
    if not isinstance(platform_policy, Mapping):
        raise ProtocolIntegrityError("execution platform policy is missing")
    if not isinstance(distributions_policy, Mapping):
        raise ProtocolIntegrityError("execution distribution policy is missing")
    if not isinstance(distributions_runtime, Mapping):
        raise ProtocolIntegrityError("runtime distribution attestation is missing")

    if runtime.get("python_implementation") != python_policy.get("implementation"):
        raise ProtocolIntegrityError("Python implementation differs from execution policy")
    if runtime.get("python_version") != python_policy.get("version"):
        raise ProtocolIntegrityError("Python version differs from execution policy")

    actual_system = platform.system()
    actual_machine = platform.machine()
    if runtime.get("operating_system") != actual_system:
        raise ProtocolIntegrityError("runtime operating-system attestation is false")
    if runtime.get("machine") != actual_machine:
        raise ProtocolIntegrityError("runtime machine attestation is false")
    if actual_system != platform_policy.get("operating_system"):
        raise ProtocolIntegrityError("operating system differs from execution policy")
    if actual_machine != platform_policy.get("machine"):
        raise ProtocolIntegrityError("machine architecture differs from execution policy")

    numpy_configuration = runtime.get("numpy_configuration")
    numpy_configuration_sha256 = runtime.get("numpy_configuration_sha256")
    if not isinstance(numpy_configuration, str) or not numpy_configuration.strip():
        raise ProtocolIntegrityError("NumPy/BLAS configuration is missing")
    if hashlib.sha256(numpy_configuration.encode("utf-8")).hexdigest() != numpy_configuration_sha256:
        raise ProtocolIntegrityError("NumPy/BLAS configuration hash is invalid")

    module_names = {
        "numpy": "numpy",
        "scipy": "scipy",
        "apophatic-relational-geometry": "apophatic_geometry",
    }
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
        if digest != distribution_tree_sha256(name):
            raise ProtocolIntegrityError(
                f"runtime distribution bytes differ from attestation: {name}"
            )
        expected_module_name = module_names[name]
        if entry.get("module_name") != expected_module_name:
            raise ProtocolIntegrityError(f"runtime module identity differs: {name}")
        module = importlib.import_module(expected_module_name)
        raw_module_file = getattr(module, "__file__", None)
        if not raw_module_file:
            raise ProtocolIntegrityError(f"runtime module has no file identity: {name}")
        actual_module_file = Path(raw_module_file).resolve(strict=True)
        if entry.get("module_file") != str(actual_module_file):
            raise ProtocolIntegrityError(f"runtime module origin differs: {name}")
        raw_root = entry.get("distribution_root")
        if not isinstance(raw_root, str) or not raw_root:
            raise ProtocolIntegrityError(f"runtime distribution root is missing: {name}")
        distribution_root = Path(raw_root).resolve(strict=True)
        if name in {"numpy", "scipy"}:
            try:
                actual_module_file.relative_to(distribution_root)
            except ValueError as exc:
                raise ProtocolIntegrityError(
                    f"runtime module is outside its hashed distribution: {name}"
                ) from exc
        else:
            try:
                actual_module_file.relative_to(root)
            except ValueError as exc:
                raise ProtocolIntegrityError(
                    "ARG runtime module is outside the attested repository"
                ) from exc

    if require_execution_clearance:
        if policy.get("status") != "CLEARED_FOR_EXPLORATORY_PILOT_AFTER_REMEDIATION":
            raise ProtocolIntegrityError("post-audit remediation clearance is absent")
        if policy.get("pilot_execution") != "AUTHORIZED_ONLY_WITH_EXECUTION_RECORD":
            raise ProtocolIntegrityError("pilot execution remains blocked by environment policy")
    return policy
