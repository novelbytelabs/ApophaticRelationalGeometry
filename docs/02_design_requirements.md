# Design Requirements

## Status

These are requirements for the **target ARG model family**, not a claim that every requirement is already implemented by the current three-node executable.

Current status:

$$
M_F\ \text{implemented and unit-tested};
\qquad
M_P,\ M_{FP},\ M_F\equiv M_P\ \text{unverified}.
$$

The current $M_F$ prototype satisfies only the requirements applicable to collective feedback and adaptive relational geometry. Projection-specific requirements remain target obligations.

## R1. Relationality

No node label, coordinate chart, or embedding is physically privileged.

## R2. Locality

Direct local proposals depend on the current node and its active neighborhood.

## R3. Mechanism separation

Collective feedback and global admissibility projection must be explicitly distinguished in equations, code, diagnostics, and claims.

No equivalence

$$
M_F\equiv M_P
$$

is assumed.

## R4. Endogenous feedback path

For feedback variants, every collective statistic must be computed from declared substrate variables and every path back into constituent transitions must be explicit.

## R5. Global admissibility

For projected variants, the complete configuration restricts proposed velocity through an explicitly defined admissible set

$$
\mathcal M=\{Z:\Gamma(Z)=0,H(Z)\geq0\}
$$

and an implemented projection or mathematically equivalent constrained solve.

This requirement is not yet implemented in the current executable.

## R6. One-many inseparability

Any collective statistic, compatibility condition, or admissibility constraint must be computed from or jointly defined with local and relational variables. It may not be an unexplained external controller.

## R7. Dynamic geometry

States, edge activations, metric deformations, and collective observables may evolve.

## R8. Nonlinearity

The family must permit state-dependent coupling, feedback, saturation, bifurcation, and non-superposable responses.

## R9. Persistence

The current state must carry information from prior evolution.

## R10. Non-collapse

For barrier-enabled variants, finite-energy trajectories should not attain zero intrinsic edge length. This remains a theorem obligation under explicit energy assumptions.

## R11. Presentation invariance

Observable predictions must be invariant or appropriately equivariant under declared relabelings and coordinate transformations.

## R12. Exact reductions

The canonical models must satisfy declared reductions:

- removing feedback from $M_{FP}$ recovers $M_P$;
- removing projection from $M_{FP}$ recovers $M_F$;
- removing both recovers $M_0$;
- removing all feedback paths from $M_F$ recovers $M_0$.

## R13. Fail-closed projection

A projected-geometry claim requires explicit constraints, projection implementation, preservation tests, code-equation parity, and substrate-path identification.

Missing evidence yields

$$
\operatorname{PROJECTED\_CLAIM}=\text{UNVERIFIED}.
$$

## R14. Falsifiability

The model family must make measurable, preregistered comparisons among

$$
M_0,\quad M_F,\quad M_P,\quad M_{FP},
$$

and against established alternatives with matched information and parameter access.

## R15. Claim discipline

Software implementation and unit tests may establish code-level properties. They do not by themselves establish scientific validity, causal autonomy, strong emergence, novelty, or physical fundamentality.
