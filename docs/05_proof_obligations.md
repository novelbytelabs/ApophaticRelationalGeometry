# Proof Obligations

Strong claims remain blocked until the applicable obligations are met for the specific model and evidence level under discussion.

## Current status

$$
\boxed{
M_0,M_F,M_P\ \text{implemented and unit-tested};
\quad
M_{FP}\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

Passing a software obligation does not discharge a scientific or physical-validation obligation.

## Shared obligations

### S1. Positivity of edge lengths

For every finite declared state, establish

$$
\ell_e(Z)>0.
$$

### S2. Metric validity

On every connected component, establish nonnegativity, symmetry, identity of indiscernibles, and the triangle inequality for shortest-path distance.

### S3. Existence and uniqueness

State conditions under which each finite-dimensional initial-value problem has a unique local solution.

### S4. Boundedness and continuation

Classify regimes with bounded trajectories, finite-time blow-up, stiffness, overflow, or loss of numerical validity.

### S5. Equivariance

Prove permutation equivariance and identify invariant observables for each model. Current permutation tests are software evidence, not the complete theorem.

### S6. Numerical convergence

Show that scientific conclusions survive refinement, alternative integrators, and independently written implementations.

## $M_F$ obligations

### F1. Substrate-path completeness — software level passed

The declared path

$$
x\to c(x)\to(\dot x,\dot s,\dot q)
$$

is explicit and unit-tested. A broader dependency audit remains appropriate before scientific use.

### F2. $M_0$ reduction — passed

$$
M_F(\chi=\eta_2=\rho=0)=M_0
$$

is implemented and unit-tested.

### F3. Feedback identifiability — open

Separate feedback effects from local coupling, adaptive edges, and metric deformation through controlled comparisons.

### F4. Downward-claim ceiling — binding

Use only “implemented prototype-level downward feedback/constraint” until organization dependence, counterfactual adequacy, invariance, transport, and alternative-model defeat are tested.

## $M_P$ obligations

### P1. Explicit admissible set — passed for version 1.0

$$
\Gamma(Z)=\frac13x^Tx-c_0=0,
\qquad
c_0\ge10^{-6},
\qquad
H=\varnothing.
$$

### P2. Projection existence and uniqueness — passed on the declared regular domain

For $x^Tx>0$,

$$
P_T=I-\frac{xx^T}{x^Tx}
$$

is uniquely defined. The implementation fails closed near rank loss.

### P3. Continuous-time preservation — passed for version 1.0

$$
f_P=f_0-x\frac{x^Tf_0}{x^Tx}
$$

satisfies

$$
x^Tf_P=0,
$$

hence

$$
\frac{d}{dt}\Gamma(Z(t))=0
$$

on the regular domain.

### P4. Discrete numerical preservation — software level passed

Projected RK4 stages and mandatory radial retraction preserve the frozen constraint tolerance at tested cases. Broader multi-step and regime-level convergence remains open before scientific use.

### P5. Code-equation parity — passed at tested cases

Production derivatives and projected RK4/retraction agree with an independently written reference path.

### P6. Projection substrate path — passed for the implementation

The implementation exposes

$$
F_0\longrightarrow F_{\mathrm{correction}}\longrightarrow F_P
$$

and the post-step numerical retraction separately.

### P7. Physical justification — open

No evidence yet establishes that constant node amplitude is the correct admissibility condition for a real system or the completed ARG relational geometry.

### P8. Predictive utility — open

No comparison yet shows that $M_P$ explains or predicts behavior better than $M_0$, $M_F$, or established alternatives.

## $M_{FP}$ obligations

### FP1. Exact reductions — open

The implementation must verify:

- removing feedback recovers $M_P$;
- removing projection recovers $M_F$;
- removing both recovers $M_0$.

### FP2. Mechanism separation — open

Retain separate local proposal, feedback, projection-correction, and retraction diagnostics.

### FP3. Ordering — frozen, implementation open

Version 1.0 fixes feedback first and projection second.

### FP4. Node identity — open

Because the node feedback is radial,

$$
P_T[-\chi c(x)x]=0,
$$

so the implementation must verify

$$
\boxed{f_{FP}=f_P}
$$

for regular node derivatives.

### FP5. Retained substrate feedback — open

Verify that $M_{FP}$ retains the $\eta_2c(x)$ and $-\rho c(x)$ terms in the $s$ and $q$ equations.

### FP6. No double counting — open

Demonstrate that feedback and projection remain explicitly distinct mechanisms rather than duplicated labels for one effect.

## Equivalence obligation

### E1. $M_F\equiv M_P$ — unverified

Visual trajectory similarity is insufficient. A valid claim requires at least one of:

- exact conjugacy;
- exact reparameterization;
- a proved approximation with error bounds;
- scoped observational equivalence under a declared observation map and tolerance.

## Barrier obligation

### B1. Non-collapse — open

Under an explicit conserved or bounded energy, prove that finite-energy trajectories cannot reach

$$
\ell_e=0.
$$

A divergent barrier formula alone is not a noncollision theorem.

## Novelty obligation

### N1. Falsifiable novelty — open

Identify at least one theorem, invariant, reduction, or prediction not reproduced by a simpler or established model with matched information and parameter access.

Until N1 passes, ARG remains a candidate synthesis.
