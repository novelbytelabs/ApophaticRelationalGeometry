from __future__ import annotations

import csv

import numpy as np
import pytest

import apophatic_geometry.models as model_module
from apophatic_geometry.model import Parameters, State, derivatives
from apophatic_geometry.models import (
    CONTRACT_VERSION,
    ModelId,
    derivatives_for_model,
    feedback_vector,
    local_adaptive_derivatives,
    rk4_step,
)
from apophatic_geometry.simulate import run
from tests.reference_equations import reference_derivative, reference_rk4_step
from tests.test_model import permute_state, sample_state


M0_EXPECTED = np.array(
    [
        -0.44747451812019629,
        0.72927750937500757,
        0.13069700874518864,
        -1.0525,
        0.22749999999999998,
        -0.33999999999999997,
        0.44100000000000006,
        0.009000000000000008,
        0.23599999999999999,
    ],
    dtype=np.float64,
)

MF_EXPECTED = np.array(
    [
        -0.53194118478686292,
        0.75567334270834086,
        0.083184508745188637,
        -0.99216666666666664,
        0.28783333333333333,
        -0.27966666666666662,
        0.39575000000000005,
        -0.036249999999999998,
        0.19074999999999998,
    ],
    dtype=np.float64,
)


def test_m0_known_answer_derivative() -> None:
    actual = local_adaptive_derivatives(sample_state(), Parameters()).pack()
    assert np.allclose(actual, M0_EXPECTED, rtol=0.0, atol=1.0e-14)


def test_mf_reference_state_regression_is_unchanged() -> None:
    actual = derivatives(sample_state(), Parameters()).pack()
    assert np.allclose(actual, MF_EXPECTED, rtol=0.0, atol=1.0e-14)


def test_m0_does_not_call_collective_mode(monkeypatch: pytest.MonkeyPatch) -> None:
    def forbidden(_: np.ndarray) -> float:
        raise AssertionError("M0 must not compute collective feedback")

    monkeypatch.setattr(model_module, "collective_mode", forbidden)
    result = local_adaptive_derivatives(sample_state(), Parameters())
    assert np.all(np.isfinite(result.pack()))


def test_zero_feedback_mf_reduces_exactly_to_m0() -> None:
    params = Parameters(chi=0.0, eta_2=0.0, rho=0.0)
    state = sample_state()
    m0 = local_adaptive_derivatives(state, params)
    mf = derivatives_for_model(state, params, ModelId.MF)
    assert np.array_equal(mf.pack(), m0.pack())
    assert np.array_equal(feedback_vector(state, params).pack(), np.zeros(9))


def test_m0_is_permutation_equivariant() -> None:
    state = sample_state()
    params = Parameters()
    permutation = (2, 0, 1)
    actual = local_adaptive_derivatives(permute_state(state, permutation), params)
    expected = permute_state(local_adaptive_derivatives(state, params), permutation)
    assert np.allclose(actual.pack(), expected.pack(), rtol=0.0, atol=1.0e-14)


@pytest.mark.parametrize("model_id", [ModelId.M0, ModelId.MF])
def test_production_derivative_matches_independent_reference(model_id: ModelId) -> None:
    state = sample_state()
    params = Parameters()
    actual = derivatives_for_model(state, params, model_id)
    expected = reference_derivative(state, params, model_id.value)
    assert np.allclose(actual.pack(), expected.pack(), rtol=0.0, atol=1.0e-14)


@pytest.mark.parametrize("model_id", [ModelId.M0, ModelId.MF])
def test_rk4_step_matches_independent_reference(model_id: ModelId) -> None:
    state = sample_state()
    params = Parameters()
    dt = 0.005
    actual = rk4_step(state, params, dt, model_id)
    expected = reference_rk4_step(state, params, dt, model_id.value)
    assert np.allclose(actual.pack(), expected.pack(), rtol=0.0, atol=1.0e-14)


def test_mp_dispatch_requires_explicit_target() -> None:
    with pytest.raises(ValueError, match="ProjectionTarget"):
        derivatives_for_model(sample_state(), Parameters(), ModelId.MP)


def test_mfp_dispatch_requires_explicit_target() -> None:
    with pytest.raises(ValueError, match="ProjectionTarget"):
        derivatives_for_model(sample_state(), Parameters(), ModelId.MFP)


@pytest.mark.parametrize(
    "params",
    [
        Parameters(alpha=np.nan),
        Parameters(tau_s=0.0),
        Parameters(epsilon=-1.0),
    ],
)
def test_invalid_parameters_fail_closed(params: Parameters) -> None:
    with pytest.raises(ValueError):
        local_adaptive_derivatives(sample_state(), params)


def test_simulation_output_is_labeled_with_model_and_contract(tmp_path) -> None:
    output = tmp_path / "run.csv"
    run(steps=1, dt=0.005, output=output, model=ModelId.M0)

    with output.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    assert len(rows) == 2
    assert {row["model_id"] for row in rows} == {ModelId.M0.value}
    assert {row["contract_version"] for row in rows} == {CONTRACT_VERSION}
    assert len({row["configuration_hash"] for row in rows}) == 1
