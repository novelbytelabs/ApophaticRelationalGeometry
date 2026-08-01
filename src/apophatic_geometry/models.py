"""Contract-v1.0 implementations for the current ARG roadmap gate.

M0 and MF retain the verified Phase 2 equations. Phase 3 adds the explicit
constant-amplitude projected-admissibility sandbox MP. MFP remains fail-closed
until its separate roadmap gate.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final

import numpy as np
from numpy.typing import NDArray

from .model import (
    EDGES,
    Parameters,
    State,
    collective_mode,
    conductances,
    derivatives as mf_derivatives,
)

FloatArray = NDArray[np.float64]
CONTRACT_VERSION: Final[str] = "1.0"
PROJECTOR_TOLERANCE: Final[float] = 1.0e-12
MINIMUM_C0: Final[float] = 1.0e-6


class ModelId(str, Enum):
    """Canonical identifiers from the frozen four-model contract."""

    M0 = "m0"
    MF = "mf"
    MP = "mp"
    MFP = "mfp"


@dataclass(frozen=True)
class ProjectionTarget:
    """Run-level constant defining the MP manifold ``c(x) = c0``."""

    c0: float

    def __post_init__(self) -> None:
        c0 = float(self.c0)
        if not np.isfinite(c0) or c0 < MINIMUM_C0:
            raise ValueError(f"c0 must be finite and >= {MINIMUM_C0}")
        object.__setattr__(self, "c0", c0)

    @classmethod
    def from_state(cls, state: State) -> "ProjectionTarget":
        """Derive the non-fitted target from the shared initial state."""

        return cls(c0=collective_mode(state.x))

    @property
    def radius(self) -> float:
        """Sphere radius ``sqrt(3 c0)``."""

        return float(np.sqrt(3.0 * self.c0))

    @property
    def minimum_norm(self) -> float:
        """Frozen fail-closed threshold from contract v1.0."""

        return max(1.0e-12, 1.0e-8 * self.radius)


@dataclass(frozen=True)
class ProjectionDiagnostics:
    """Inspectable decomposition of one MP derivative evaluation."""

    proposal: State
    correction: State
    projected: State
    constraint_residual: float
    normalized_tangency_residual: float
    denominator: float

    @property
    def correction_norm(self) -> float:
        return float(np.linalg.norm(self.correction.x))


@dataclass(frozen=True)
class RetractionResult:
    """Result and diagnostics from one mandatory radial retraction."""

    state: State
    raw_constraint_residual: float
    post_constraint_residual: float
    magnitude: float


@dataclass(frozen=True)
class ProjectedStepResult:
    """One projected RK4 step with all four stage diagnostics."""

    state: State
    raw_state: State
    stage_diagnostics: tuple[
        ProjectionDiagnostics,
        ProjectionDiagnostics,
        ProjectionDiagnostics,
        ProjectionDiagnostics,
    ]
    raw_constraint_residual: float
    post_constraint_residual: float
    retraction_magnitude: float


def parse_model_id(model: ModelId | str) -> ModelId:
    """Normalize a model identifier and reject unknown values."""

    if isinstance(model, ModelId):
        return model
    try:
        return ModelId(str(model).lower())
    except ValueError as exc:
        allowed = ", ".join(member.value for member in ModelId)
        raise ValueError(f"unknown model {model!r}; expected one of: {allowed}") from exc


def _validate_finite_parameters(params: Parameters) -> None:
    nonfinite = [name for name, value in vars(params).items() if not np.isfinite(value)]
    if nonfinite:
        raise ValueError(f"Parameters must be finite: {', '.join(nonfinite)}")


def local_adaptive_derivatives(state: State, params: Parameters) -> State:
    """Evaluate M0 without computing or consuming ``c(x)``."""

    _validate_finite_parameters(params)
    params.validate()
    x, s, q = state.x, state.s, state.q
    weights = conductances(state)

    dx = params.alpha * x - params.beta * x**3
    ds = np.empty(3, dtype=np.float64)
    dq = np.empty(3, dtype=np.float64)

    for edge_index, (i, j) in enumerate(EDGES):
        difference = x[i] - x[j]
        coupling = weights[edge_index] * difference
        dx[i] -= coupling
        dx[j] += coupling

        ds[edge_index] = (
            params.eta_0
            - params.eta_1 * difference**2
            - s[edge_index]
        ) / params.tau_s

        dq[edge_index] = (
            -params.gamma * q[edge_index]
            + params.kappa * difference**2
        ) / params.tau_q

    derivative = State(x=dx, s=ds, q=dq)
    if not np.all(np.isfinite(derivative.pack())):
        raise FloatingPointError("non-finite M0 derivative encountered")
    return derivative


def feedback_vector(state: State, params: Parameters) -> State:
    """Return the explicit MF feedback contribution ``F_F``."""

    _validate_finite_parameters(params)
    params.validate()
    c = collective_mode(state.x)
    return State(
        x=-params.chi * c * state.x,
        s=np.full(3, params.eta_2 * c / params.tau_s, dtype=np.float64),
        q=np.full(3, -params.rho * c / params.tau_q, dtype=np.float64),
    )


def _require_projection_target(target: ProjectionTarget | None) -> ProjectionTarget:
    if target is None:
        raise ValueError("MP requires an explicit ProjectionTarget")
    if not isinstance(target, ProjectionTarget):
        raise TypeError("target must be a ProjectionTarget")
    return target


def _regular_projection_state(x: FloatArray, target: ProjectionTarget) -> tuple[float, float]:
    vector = np.asarray(x, dtype=np.float64)
    if vector.shape != (3,):
        raise ValueError(f"x must have shape (3,), received {vector.shape}")
    if not np.all(np.isfinite(vector)):
        raise FloatingPointError("non-finite projected node state")

    norm = float(np.linalg.norm(vector))
    if norm <= target.minimum_norm:
        raise FloatingPointError(
            "projected node-state norm is at or below the fail-closed threshold"
        )

    denominator = float(np.dot(vector, vector))
    if not np.isfinite(denominator):
        raise FloatingPointError("non-finite projection denominator")
    return denominator, norm


def constraint_residual(state: State, target: ProjectionTarget) -> float:
    """Return ``Gamma(Z) = c(x) - c0``."""

    residual = collective_mode(state.x) - target.c0
    if not np.isfinite(residual):
        raise FloatingPointError("non-finite constraint residual")
    return float(residual)


def tangent_projector(x: FloatArray, target: ProjectionTarget) -> FloatArray:
    """Return the Euclidean tangent projector ``I - xx^T/(x^T x)``."""

    denominator, _ = _regular_projection_state(x, target)
    vector = np.asarray(x, dtype=np.float64)
    projector = np.eye(3, dtype=np.float64) - np.outer(vector, vector) / denominator
    if not np.all(np.isfinite(projector)):
        raise FloatingPointError("non-finite tangent projector")
    return projector


def project_node_derivative(
    x: FloatArray,
    proposal_x: FloatArray,
    target: ProjectionTarget,
) -> tuple[FloatArray, FloatArray, float, float]:
    """Project a proposed node derivative and expose its normal correction."""

    denominator, norm_x = _regular_projection_state(x, target)
    vector = np.asarray(x, dtype=np.float64)
    proposal = np.asarray(proposal_x, dtype=np.float64)
    if proposal.shape != (3,):
        raise ValueError(f"proposal_x must have shape (3,), received {proposal.shape}")
    if not np.all(np.isfinite(proposal)):
        raise FloatingPointError("non-finite proposed node derivative")

    correction = -vector * (float(np.dot(vector, proposal)) / denominator)
    projected = proposal + correction
    norm_projected = float(np.linalg.norm(projected))
    tangency_residual = abs(float(np.dot(vector, projected))) / (
        norm_x * norm_projected + 1.0e-30
    )

    if not np.all(np.isfinite(correction)) or not np.all(np.isfinite(projected)):
        raise FloatingPointError("non-finite projection result")
    if not np.isfinite(tangency_residual):
        raise FloatingPointError("non-finite tangency residual")
    if tangency_residual > PROJECTOR_TOLERANCE:
        raise FloatingPointError(
            "normalized tangency residual exceeds the contract tolerance: "
            f"{tangency_residual}"
        )

    return projected, correction, float(tangency_residual), denominator


def projected_derivative(
    state: State,
    params: Parameters,
    target: ProjectionTarget,
) -> ProjectionDiagnostics:
    """Evaluate MP as M0 proposal followed by node-state projection."""

    proposal = local_adaptive_derivatives(state, params)
    projected_x, correction_x, tangency_residual, denominator = (
        project_node_derivative(state.x, proposal.x, target)
    )
    correction = State(
        x=correction_x,
        s=np.zeros(3, dtype=np.float64),
        q=np.zeros(3, dtype=np.float64),
    )
    projected = State(
        x=projected_x,
        s=proposal.s.copy(),
        q=proposal.q.copy(),
    )
    return ProjectionDiagnostics(
        proposal=proposal,
        correction=correction,
        projected=projected,
        constraint_residual=constraint_residual(state, target),
        normalized_tangency_residual=tangency_residual,
        denominator=denominator,
    )


def derivatives_for_model(
    state: State,
    params: Parameters,
    model: ModelId | str,
    target: ProjectionTarget | None = None,
) -> State:
    """Dispatch implemented models and fail closed for MFP."""

    model_id = parse_model_id(model)
    if model_id is ModelId.M0:
        return local_adaptive_derivatives(state, params)
    if model_id is ModelId.MF:
        _validate_finite_parameters(params)
        return mf_derivatives(state, params)
    if model_id is ModelId.MP:
        return projected_derivative(
            state,
            params,
            _require_projection_target(target),
        ).projected
    raise NotImplementedError(
        f"{model_id.value} is defined by contract v{CONTRACT_VERSION} "
        "but is not implemented at the current roadmap gate"
    )


def retract_to_constraint(state: State, target: ProjectionTarget) -> RetractionResult:
    """Apply the mandatory radial retraction to ``c(x) = c0``."""

    _, norm = _regular_projection_state(state.x, target)
    retracted_x = target.radius * state.x / norm
    retracted_state = State(
        x=retracted_x,
        s=state.s.copy(),
        q=state.q.copy(),
    )

    raw_residual = constraint_residual(state, target)
    post_residual = constraint_residual(retracted_state, target)
    magnitude = float(np.linalg.norm(retracted_x - state.x))
    tolerance = PROJECTOR_TOLERANCE * max(1.0, target.c0)

    if not np.isfinite(magnitude):
        raise FloatingPointError("non-finite retraction magnitude")
    if abs(post_residual) > tolerance:
        raise FloatingPointError(
            "post-retraction constraint residual exceeds the contract tolerance: "
            f"{post_residual}"
        )

    return RetractionResult(
        state=retracted_state,
        raw_constraint_residual=raw_residual,
        post_constraint_residual=post_residual,
        magnitude=magnitude,
    )


def _validate_dt(dt: float) -> None:
    if not np.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be finite and positive")


def projected_rk4_step(
    state: State,
    params: Parameters,
    dt: float,
    target: ProjectionTarget,
) -> ProjectedStepResult:
    """Advance MP with projected RK4 stages and mandatory retraction."""

    _validate_dt(dt)
    target = _require_projection_target(target)
    initial_residual = constraint_residual(state, target)
    initial_tolerance = PROJECTOR_TOLERANCE * max(1.0, target.c0)
    if abs(initial_residual) > initial_tolerance:
        raise ValueError(
            "initial state does not lie on the declared MP constraint manifold"
        )

    y0 = state.pack()
    diagnostics: list[ProjectionDiagnostics] = []

    def rhs(vector: FloatArray) -> FloatArray:
        stage = State.unpack(vector)
        stage_diagnostics = projected_derivative(stage, params, target)
        diagnostics.append(stage_diagnostics)
        return stage_diagnostics.projected.pack()

    k1 = rhs(y0)
    k2 = rhs(y0 + 0.5 * dt * k1)
    k3 = rhs(y0 + 0.5 * dt * k2)
    k4 = rhs(y0 + dt * k3)
    raw_vector = y0 + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    if not np.all(np.isfinite(raw_vector)):
        raise FloatingPointError("non-finite projected RK4 state")

    raw_state = State.unpack(raw_vector)
    retraction = retract_to_constraint(raw_state, target)
    if len(diagnostics) != 4:
        raise RuntimeError("projected RK4 did not produce exactly four stage diagnostics")

    return ProjectedStepResult(
        state=retraction.state,
        raw_state=raw_state,
        stage_diagnostics=(
            diagnostics[0],
            diagnostics[1],
            diagnostics[2],
            diagnostics[3],
        ),
        raw_constraint_residual=retraction.raw_constraint_residual,
        post_constraint_residual=retraction.post_constraint_residual,
        retraction_magnitude=retraction.magnitude,
    )


def rk4_step(
    state: State,
    params: Parameters,
    dt: float,
    model: ModelId | str = ModelId.MF,
    target: ProjectionTarget | None = None,
) -> State:
    """Advance one classical fixed-step RK4 step for an implemented model."""

    _validate_dt(dt)
    model_id = parse_model_id(model)

    if model_id is ModelId.MP:
        return projected_rk4_step(
            state,
            params,
            dt,
            _require_projection_target(target),
        ).state
    if model_id is ModelId.MFP:
        raise NotImplementedError(
            f"{model_id.value} is defined by contract v{CONTRACT_VERSION} "
            "but is not implemented at the current roadmap gate"
        )

    y0 = state.pack()

    def rhs(vector: FloatArray) -> FloatArray:
        return derivatives_for_model(State.unpack(vector), params, model_id).pack()

    k1 = rhs(y0)
    k2 = rhs(y0 + 0.5 * dt * k1)
    k3 = rhs(y0 + 0.5 * dt * k2)
    k4 = rhs(y0 + dt * k3)
    result = y0 + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
    if not np.all(np.isfinite(result)):
        raise FloatingPointError("non-finite RK4 state encountered")
    return State.unpack(result)
