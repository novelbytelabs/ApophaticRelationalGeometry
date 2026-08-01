# Design Requirements

## Status

These requirements govern both the implemented contract-v1.0 prototypes and broader ARG variants.

Current status:

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

Implementation of the four prototypes does not establish that every broader relational, invariance, physical, or scientific requirement has been satisfied.

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

This is implemented for $M_F$ and the feedback component of $M_{FP}$.

## R5. Global admissibility

For projected variants, the complete configuration restricts proposed velocity through an explicitly defined admissible set

$$
\mathcal M=\{Z:\Gamma(Z)=0,H(Z)\geq0\}
$$

and an implemented projection or mathematically equivalent constrained solve.

Contract v1.0 implements the equality-only constant-amplitude case

$$
\Gamma(Z)=\frac13x^Tx-c_0=0,
\qquad H=\varnothing,
$$

for $M_P$ and $M_{FP}$. Broader relational and inequality-constrained admissibility remains a target obligation.

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

Permutation equivariance is unit-tested for all four prototypes. General presentation invariance remains open.

## R12. Exact reductions

The canonical implementation must satisfy declared reductions:

- the unprojected $M_{FP}$ proposal agrees with $M_F$;
- setting $\chi=\eta_2=\rho=0$ in $M_{FP}$ recovers $M_P$;
- removing feedback and projection recovers $M_0$;
- removing all feedback paths from $M_F$ recovers $M_0$.

These reductions are unit-tested at the software level.

## R13. Fail-closed projection

A projected-implementation claim requires explicit constraints, projection implementation, preservation tests, code-equation parity, and substrate-path identification.

The contract-v1.0 implementation gate passes for $M_P$ and $M_{FP}$. The broader scientific claim remains

$$
\operatorname{ARG\_COMPARATIVE\_SCIENTIFIC\_CLAIM}
=
\text{UNVERIFIED}.
$$

## R14. Falsifiability

The model family must make measurable, preregistered comparisons among

$$
M_0,\quad M_F,\quad M_P,\quad M_{FP},
$$

and against established alternatives with matched information and parameter access.

## R15. Claim discipline

Software implementation and unit tests may establish code-level properties. They do not by themselves establish scientific validity, causal autonomy, strong emergence, novelty, equivalence, or physical fundamentality.
