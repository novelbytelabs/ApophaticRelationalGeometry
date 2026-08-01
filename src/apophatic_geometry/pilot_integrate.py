"""Integration facade retained for stable Phase 6 imports."""

from .pilot_gates import (
    assess_numerics, inverse_permute_state, inverse_permute_state_trajectory,
    permute_state, require_constraint_gate, require_same_state_identity_gate,
    run_permutation_tripwires, same_state_identity_error,
)
from .pilot_integrators import exogenous_replay_control, integrate_dop853, integrate_rk4
from .pilot_mechanisms import all_permutations

__all__ = [
    "all_permutations", "assess_numerics", "exogenous_replay_control",
    "integrate_dop853", "integrate_rk4", "inverse_permute_state",
    "inverse_permute_state_trajectory", "permute_state",
    "require_constraint_gate", "require_same_state_identity_gate",
    "run_permutation_tripwires", "same_state_identity_error",
]
