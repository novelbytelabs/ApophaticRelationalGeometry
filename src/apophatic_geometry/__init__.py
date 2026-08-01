"""Executable reference implementation of the ARG M_F feedback prototype.

This package does not yet implement the M_P admissibility projection or the
combined M_FP model.
"""

from .model import Parameters, State, derivatives, intrinsic_distance_matrix, intrinsic_edge_lengths

__all__ = [
    "Parameters",
    "State",
    "derivatives",
    "intrinsic_distance_matrix",
    "intrinsic_edge_lengths",
]
