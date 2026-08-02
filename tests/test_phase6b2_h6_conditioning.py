from __future__ import annotations

from dataclasses import replace
import math

import numpy as np
import pytest

from apophatic_geometry.model import Parameters, State
from apophatic_geometry.models import ProjectionTarget
from apophatic_geometry import pilot_gates


def _state_near_projected_equilibrium(magnitude: float) -> tuple[State, float]:
    c0 = 0.5
    radial = np.array([-1.0, -1.0, -1.0], dtype=np.float64)
    radial /= np.linalg.norm(radial)
    tangent = np.array([1.0, -1.0, 0.0], dtype=np.float64)
    tangent /= np.linalg.norm(tangent)
    direction = radial + magnitude * tangent
    direction /= np.linalg.norm(direction)
    x = math.sqrt(3.0 * c0) * direction
    return (
        State(
            x=x,
            s=np.array([0.2, -0.1, 0.05], dtype=np.float64),
            q=np.array([0.1, -0.2, 0.05], dtype=np.float64),
        ),
        c0,
    )


def _tangent_unit(x: np.ndarray) -> np.ndarray:
    candidate = np.array([1.0, -1.0, 0.0], dtype=np.float64)
    candidate -= x * (float(np.dot(x, candidate)) / float(np.dot(x, x)))
    return candidate / np.linalg.norm(candidate)


def test_h6_near_equilibrium_uses_backward_error_not_singular_ratio() -> None:
    state, c0 = _state_near_projected_equilibrium(1.0e-10)
    assessment = pilot_gates.same_state_identity_assessment(
        state, Parameters(), c0
    )

    assert assessment.regime == "cancellation_dominated"
    assert assessment.forward_relative_error > 1.0e-12
    assert assessment.backward_error <= pilot_gates._H6_BACKWARD_TOLERANCE
    assert assessment.radiality_pass
    assert assessment.passed


def test_h6_well_conditioned_case_retains_frozen_relative_tolerance(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state, c0 = _state_near_projected_equilibrium(0.1)
    params = Parameters()
    baseline = pilot_gates.same_state_identity_assessment(state, params, c0)
    assert baseline.regime == "well_conditioned"
    assert baseline.passed

    original = pilot_gates.combined_projected_derivative

    def perturbed(state_arg: State, params_arg: Parameters, target: ProjectionTarget):
        diagnostics = original(state_arg, params_arg, target)
        tangent = _tangent_unit(state_arg.x)
        delta = 4.0e-12 * np.linalg.norm(diagnostics.projected.x) * tangent
        projected = State(
            x=diagnostics.projected.x + delta,
            s=diagnostics.projected.s,
            q=diagnostics.projected.q,
        )
        return replace(diagnostics, projected=projected)

    monkeypatch.setattr(pilot_gates, "combined_projected_derivative", perturbed)
    assessment = pilot_gates.same_state_identity_assessment(state, params, c0)
    assert assessment.regime == "well_conditioned"
    assert assessment.forward_relative_error > 1.0e-12
    assert not assessment.identity_pass
    assert not assessment.passed


def test_h6_cancellation_regime_rejects_real_projected_mismatch(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state, c0 = _state_near_projected_equilibrium(1.0e-10)
    params = Parameters()
    original = pilot_gates.combined_projected_derivative

    def perturbed(state_arg: State, params_arg: Parameters, target: ProjectionTarget):
        diagnostics = original(state_arg, params_arg, target)
        tangent = _tangent_unit(state_arg.x)
        input_scale = max(
            np.linalg.norm(diagnostics.local_proposal.x),
            np.linalg.norm(diagnostics.proposal.x),
            np.linalg.norm(diagnostics.feedback.x),
        )
        projected = State(
            x=diagnostics.projected.x + 1.0e-10 * input_scale * tangent,
            s=diagnostics.projected.s,
            q=diagnostics.projected.q,
        )
        return replace(diagnostics, projected=projected)

    monkeypatch.setattr(pilot_gates, "combined_projected_derivative", perturbed)
    assessment = pilot_gates.same_state_identity_assessment(state, params, c0)
    assert assessment.regime == "cancellation_dominated"
    assert assessment.backward_error > pilot_gates._H6_BACKWARD_TOLERANCE
    assert not assessment.identity_pass
    assert not assessment.passed


def test_h6_rejects_nonradial_feedback_even_when_outputs_match(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state, c0 = _state_near_projected_equilibrium(0.1)
    params = Parameters()
    original = pilot_gates.combined_projected_derivative

    def nonradial(state_arg: State, params_arg: Parameters, target: ProjectionTarget):
        diagnostics = original(state_arg, params_arg, target)
        tangent = _tangent_unit(state_arg.x)
        feedback = State(
            x=diagnostics.feedback.x
            + 1.0e-10 * np.linalg.norm(diagnostics.feedback.x) * tangent,
            s=diagnostics.feedback.s,
            q=diagnostics.feedback.q,
        )
        return replace(diagnostics, feedback=feedback)

    monkeypatch.setattr(pilot_gates, "combined_projected_derivative", nonradial)
    assessment = pilot_gates.same_state_identity_assessment(state, params, c0)
    assert assessment.radiality_error > pilot_gates._H6_BACKWARD_TOLERANCE
    assert not assessment.radiality_pass
    assert not assessment.passed
