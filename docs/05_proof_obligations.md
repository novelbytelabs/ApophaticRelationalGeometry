# Proof Obligations

Strong claims are blocked until the applicable obligations are met for the specific model being discussed.

The canonical model family is

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}.
$$

Current status:

$$
M_F\ \text{implemented and unit-tested};
\qquad
M_P,\ M_{FP},\ M_F\equiv M_P\ \text{unverified}.
$$

## Obligations shared by all implemented models

### P1. Positivity of edge lengths

Prove

$$
\ell_e(Z)>0
$$

for every finite state in the declared domain.

### P2. Metric validity

On each connected component, prove that shortest-path distance is nonnegative, symmetric, zero only on the diagonal, and satisfies the triangle inequality.

### P3. Existence and uniqueness

State regularity conditions under which each finite-dimensional initial-value problem has a unique local solution.

### P4. Boundedness or blow-up classification

Determine parameter regimes yielding bounded trajectories, finite-time blow-up, stiffness, or loss of connectivity.

### P5. Equivariance

Prove permutation equivariance and invariant observables under node relabeling for each model separately.

### P6. Numerical convergence

Demonstrate that conclusions survive decreasing time step, alternative integrators, and independent reference implementations.

## Obligations specific to $M_F$

### F1. Substrate-path completeness

Identify every dependency path

$$
x\to c(x)\to(\dot x,\dot s,\dot q)
$$

and prove that no undeclared collective path exists.

### F2. $M_0$ reduction

Show that removing all declared $c(x)$ feedback terms recovers $M_0$ exactly.

### F3. Feedback identifiability

Show through controlled interventions that the effects of $c(x)$ feedback can be separated from local coupling, adaptive topology, and metric deformation.

### F4. Downward-claim ceiling

Use only the label “implemented prototype-level downward feedback/constraint” until organization dependence, counterfactual adequacy, invariance, transport, and alternative-model defeat are tested.

## Obligations specific to $M_P$

### P7. Explicit admissible set

Define

$$
\mathcal M=\{Z:\Gamma(Z)=0,\ H(Z)\geq0\}
$$

with complete domains and regularity assumptions.

### P8. Projection existence and uniqueness

Prove that the tangent-space or normal-space projection exists and is unique on the declared operating domain.

### P9. Constraint preservation

For the continuous-time projected vector field, prove

$$
\frac{d}{dt}\Gamma(Z(t))=0
$$

and state the active-set rule for $H(Z)\geq0$.

### P10. Numerical preservation

Show that the chosen integration and retraction method preserves constraints to declared tolerances under refinement.

### P11. Code-equation parity

Independently verify that the implementation computes the documented projection operator, including rank-deficient and singular cases.

### P12. Projection substrate path

Identify how the global constraint is computed and how the resulting correction reaches each constituent transition.

## Obligations specific to $M_{FP}$

### FP1. Exact reductions

Prove that:

- removing feedback recovers $M_P$;
- removing projection recovers $M_F$;
- removing both recovers $M_0$.

### FP2. Mechanism separation

Retain separately measurable vectors for local proposal, feedback, and projection correction.

### FP3. Ordering and interaction

Declare whether feedback is applied before projection, after projection, or through a coupled solve, and test any noncommuting alternatives.

### FP4. No double counting

Show that the same collective influence is not encoded once as feedback and again as projection without explicit justification.

## Equivalence obligation

### E1. $M_F\equiv M_P$

No equivalence may be claimed from visually similar trajectories.

A valid equivalence claim requires at least one of:

- exact conjugacy;
- exact reparameterization;
- a proved approximation with error bounds;
- a precisely scoped observational equivalence under a declared observation map.

If equivalence is obtained only by defining $\Gamma$ from the already chosen feedback vector field, the construction must be examined for circularity.

## Barrier obligation

### B1. Non-collapse

Under an explicit conserved or bounded energy, show that finite-energy trajectories cannot reach

$$
\ell_e=0.
$$

A divergent formula alone is not yet a noncollision theorem.

## Novelty obligation

### N1. Falsifiable novelty

Identify at least one theorem, invariant, reduction, or prediction that cannot be reproduced by a simpler or established model with matched information and parameter access.

Failure to meet N1 leaves ARG as a candidate synthesis rather than a new mathematical framework.
