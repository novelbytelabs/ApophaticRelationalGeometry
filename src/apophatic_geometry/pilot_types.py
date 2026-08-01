"""Shared immutable types and constants for the Phase 6 pilot-only runner."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any, Mapping

import numpy as np
from numpy.typing import NDArray

from .model import State, collective_mode
from .models import CONTRACT_VERSION
from .protocol import PROTOCOL_ID, PROTOCOL_VERSION

FloatArray = NDArray[np.float64]

RUNNER_ID = "ARG-P6-PILOT-RUNNER-v1"
RUNNER_VERSION = "1.0.0"
PILOT_SPLIT = "pilot"
CONFIRMATORY_SPLIT = "confirmatory"
SMOKE_SPLIT = "smoke"
EXPECTED_PILOT_DIRECTIONS = 10
EXPECTED_PILOT_CONFIGURATIONS = 50
EXECUTION_AUTHORIZATION_PATH = Path(
    "protocol/phase6_runner_v1/EXECUTION_AUTHORIZATION.json"
)
ALLOWED_ABLATIONS = {None, "freeze_s", "freeze_q", "freeze_sq"}
_SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


class PilotRunnerError(RuntimeError):
    """Base error for a fail-closed runner condition."""


class ProtocolIntegrityError(PilotRunnerError):
    """The frozen protocol, source tree, or execution record is invalid."""


class ConfirmatoryAccessError(PilotRunnerError):
    """A confirmatory or mixed-split execution request was rejected."""


class NumericalGateError(PilotRunnerError):
    """A mandatory numerical or invariance gate failed."""


@dataclass(frozen=True)
class FrozenProtocolBundle:
    """Lock-verified Phase 5 manifests loaded in fail-closed order."""

    repo_root: Path
    protocol: Mapping[str, Any]
    parameters: Mapping[str, Any]
    initial_conditions: Mapping[str, Any]
    interventions: Mapping[str, Any]
    lock: Mapping[str, Any]


@dataclass(frozen=True)
class PilotConfiguration:
    """One deterministic configuration authorized for a declared split."""

    config_id: str
    direction_id: str
    split: str
    c0: float
    initial_state: State
    configuration_hash: str

    def __post_init__(self) -> None:
        if not _SAFE_ID.fullmatch(self.config_id) or not _SAFE_ID.fullmatch(self.direction_id):
            raise ValueError("configuration identifiers must be path-safe")
        if self.split not in {PILOT_SPLIT, CONFIRMATORY_SPLIT, SMOKE_SPLIT}:
            raise ValueError(f"unsupported split: {self.split}")
        c0 = float(self.c0)
        if not np.isfinite(c0) or c0 <= 0.0:
            raise ValueError("c0 must be finite and positive")
        if not isinstance(self.configuration_hash, str) or len(self.configuration_hash) != 64:
            raise ValueError("configuration_hash must be a SHA-256 hexadecimal digest")
        try:
            int(self.configuration_hash, 16)
        except ValueError as exc:
            raise ValueError("configuration_hash is not hexadecimal") from exc
        actual_c0 = collective_mode(self.initial_state.x)
        if not np.isclose(actual_c0, c0, rtol=0.0, atol=1.0e-14):
            raise ValueError("initial state does not realize the declared c0")
        object.__setattr__(self, "c0", c0)

    def canonical_payload(self) -> dict[str, Any]:
        return {
            "protocol_id": PROTOCOL_ID,
            "protocol_version": PROTOCOL_VERSION,
            "contract_version": CONTRACT_VERSION,
            "config_id": self.config_id,
            "direction_id": self.direction_id,
            "split": self.split,
            "c0": self.c0,
            "initial_state": {
                "x": self.initial_state.x.tolist(),
                "s": self.initial_state.s.tolist(),
                "q": self.initial_state.q.tolist(),
            },
        }


@dataclass(frozen=True)
class ControlSpec:
    """A declared developmental control without changing canonical model IDs."""

    ablation: str | None = None
    exogenous_times: FloatArray | None = None
    exogenous_c: FloatArray | None = None

    def __post_init__(self) -> None:
        if self.ablation not in ALLOWED_ABLATIONS:
            raise ValueError(f"unsupported ablation: {self.ablation}")
        one_missing = (self.exogenous_times is None) != (self.exogenous_c is None)
        if one_missing:
            raise ValueError("exogenous_times and exogenous_c must be supplied together")
        if self.exogenous_times is not None and self.exogenous_c is not None:
            times = np.asarray(self.exogenous_times, dtype=np.float64)
            values = np.asarray(self.exogenous_c, dtype=np.float64)
            if times.ndim != 1 or values.ndim != 1 or times.shape != values.shape:
                raise ValueError("exogenous replay arrays must be matching one-dimensional arrays")
            if times.size < 2 or not np.all(np.isfinite(times)) or not np.all(np.isfinite(values)):
                raise ValueError("exogenous replay arrays are incomplete or non-finite")
            if not np.all(np.diff(times) > 0.0):
                raise ValueError("exogenous replay times must be strictly increasing")
            if np.any(values < 0.0):
                raise ValueError("exogenous collective statistic must be nonnegative")
            object.__setattr__(self, "exogenous_times", times)
            object.__setattr__(self, "exogenous_c", values)

    @property
    def id(self) -> str:
        parts: list[str] = []
        if self.exogenous_times is not None:
            parts.append("exogenous_replay")
        if self.ablation is not None:
            parts.append(self.ablation)
        return "+".join(parts) if parts else "canonical"


@dataclass(frozen=True)
class Trajectory:
    """One labeled trajectory and its observation/step diagnostics."""

    config_id: str
    direction_id: str
    split: str
    model_id: str
    integrator: str
    profile: str
    control_id: str
    source_commit: str
    times: FloatArray
    states: FloatArray
    geometry: FloatArray
    local_proposal: FloatArray
    feedback: FloatArray
    combined_proposal: FloatArray
    projection_correction: FloatArray
    constraint_residual: FloatArray
    tangency_residual: FloatArray
    denominator: FloatArray
    step_times: FloatArray
    raw_constraint_residual: FloatArray
    post_constraint_residual: FloatArray
    retraction_magnitude: FloatArray

    def __post_init__(self) -> None:
        times = np.asarray(self.times, dtype=np.float64)
        n = times.size
        if times.ndim != 1 or n < 1 or not np.all(np.isfinite(times)):
            raise ValueError("trajectory times are invalid")
        if n > 1 and not np.all(np.diff(times) > 0.0):
            raise ValueError("trajectory times must be strictly increasing")
        values = {
            "states": np.asarray(self.states, dtype=np.float64),
            "geometry": np.asarray(self.geometry, dtype=np.float64),
            "local_proposal": np.asarray(self.local_proposal, dtype=np.float64),
            "feedback": np.asarray(self.feedback, dtype=np.float64),
            "combined_proposal": np.asarray(self.combined_proposal, dtype=np.float64),
            "projection_correction": np.asarray(self.projection_correction, dtype=np.float64),
            "constraint_residual": np.asarray(self.constraint_residual, dtype=np.float64),
            "tangency_residual": np.asarray(self.tangency_residual, dtype=np.float64),
            "denominator": np.asarray(self.denominator, dtype=np.float64),
        }
        expected_shapes = {
            "states": (n, 9),
            "geometry": (n, 3),
            "local_proposal": (n, 9),
            "feedback": (n, 9),
            "combined_proposal": (n, 9),
            "projection_correction": (n, 9),
            "constraint_residual": (n,),
            "tangency_residual": (n,),
            "denominator": (n,),
        }
        for name, expected in expected_shapes.items():
            value = values[name]
            if value.shape != expected:
                raise ValueError(f"{name} has shape {value.shape}; expected {expected}")
            if not np.all(np.isfinite(value)):
                raise ValueError(f"{name} contains non-finite values")
            object.__setattr__(self, name, value)
        step_values = {
            "step_times": np.asarray(self.step_times, dtype=np.float64),
            "raw_constraint_residual": np.asarray(self.raw_constraint_residual, dtype=np.float64),
            "post_constraint_residual": np.asarray(self.post_constraint_residual, dtype=np.float64),
            "retraction_magnitude": np.asarray(self.retraction_magnitude, dtype=np.float64),
        }
        shape = step_values["step_times"].shape
        if len(shape) != 1:
            raise ValueError("step_times must be one-dimensional")
        for name, value in step_values.items():
            if value.shape != shape:
                raise ValueError("step diagnostics must share the step_times shape")
            if not np.all(np.isfinite(value)):
                raise ValueError(f"{name} contains non-finite values")
            object.__setattr__(self, name, value)
        object.__setattr__(self, "times", times)

    def observation(self, map_id: str) -> FloatArray:
        if map_id == "full":
            return self.states
        if map_id == "x":
            return self.states[:, 0:3]
        if map_id == "sq":
            return self.states[:, 3:9]
        if map_id == "d":
            return self.geometry
        raise ValueError(f"unsupported observation map: {map_id}")

    def raw_arrays(self) -> dict[str, FloatArray]:
        return {
            "times": self.times,
            "states": self.states,
            "geometry": self.geometry,
            "local_proposal": self.local_proposal,
            "feedback": self.feedback,
            "combined_proposal": self.combined_proposal,
            "projection_correction": self.projection_correction,
            "constraint_residual": self.constraint_residual,
            "tangency_residual": self.tangency_residual,
            "denominator": self.denominator,
            "step_times": self.step_times,
            "raw_constraint_residual": self.raw_constraint_residual,
            "post_constraint_residual": self.post_constraint_residual,
            "retraction_magnitude": self.retraction_magnitude,
        }


@dataclass(frozen=True)
class NumericalAssessment:
    """Frozen convergence and alternate-integrator checks."""

    map_id: str
    coarse_medium: float
    medium_fine: float
    fine_alternate: float
    endpoint_error: float
    endpoint_limit: float
    refinement_pass: bool
    endpoint_pass: bool
    alternate_pass: bool

    @property
    def passed(self) -> bool:
        return self.refinement_pass and self.endpoint_pass and self.alternate_pass


@dataclass(frozen=True)
class ArchiveWriteResult:
    """Hashes of all immutable files written for one trajectory."""

    relative_directory: str
    files: Mapping[str, str]
