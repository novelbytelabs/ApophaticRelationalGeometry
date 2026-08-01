# Proof Obligations

Strong claims remain blocked until the applicable obligations are met for the specific model and evidence level under discussion.

## Current status

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
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

### FP1. Declared reductions — software level passed

The implementation verifies:

- the unprojected $F_0+F_F$ proposal agrees with $M_F$;
- setting $\chi=\eta_2=\rho=0$ recovers $M_P$;
- removing feedback and projection recovers $M_0$.

These are implementation reductions, not evidence of scientific adequacy.

### FP2. Mechanism separation — software level passed

The implementation retains separate local proposal, feedback, combined proposal, projection-correction, projected derivative, and retraction diagnostics.

Whether these mechanisms are empirically identifiable remains open.

### FP3. Ordering — passed for version 1.0

Version 1.0 implements feedback first and projection second at every RK4 derivative stage.

Alternative orderings or coupled solves remain separate future models.

### FP4. Same-state node identity — passed on the regular domain

Because the node feedback is radial,

$$
P_T[-\chi c(x)x]=0,
$$

and therefore

$$
\boxed{f_{FP}=f_P}
$$

at the same regular full state.

This identity is algebraic and unit-tested. It does not imply equal trajectories because the $s$ and $q$ dynamics differ.

### FP5. Retained substrate feedback — passed

$M_{FP}$ retains the $\eta_2c(x)$ and $-\rho c(x)$ terms in the $s$ and $q$ equations.

### FP6. No double counting — software decomposition passed; scientific interpretation open

The code represents feedback and projection as separately inspectable vectors. A scientific argument that both are necessary, nonredundant mechanisms remains open and belongs to the comparative experiment.

### FP7. Trajectory interaction — open

Determine when retained $s/q$ feedback causes $M_{FP}$ trajectories to diverge from $M_P$, under which observation maps, and whether the difference is distinguishable from simpler adaptive-network alternatives.

## Equivalence obligation

### E1. $M_F\equiv M_P$ — unverified

Visual trajectory similarity is insufficient. A valid claim requires at least one of:

- exact conjugacy;
- exact reparameterization;
- a proved approximation with error bounds;
- scoped observational equivalence under a declared observation map and tolerance.

The verified identity $f_{FP}=f_P$ at the same state does not discharge this obligation.

## Comparative-experiment obligation

### C1. Frozen protocol — open

Before any development pilot, freeze:

- primary and secondary hypotheses;
- observation maps and tolerances;
- parameter and initial-condition manifests;
- interventions and ablations;
- structural inferential units;
- numerical refinement and alternate-integrator policies;
- exclusions and stop rules;
- exploratory/confirmatory separation;
- raw-output provenance and checksums.

### C2. Alternative-model defeat — open

No whole-part, projection, geometry, or emergence claim may exceed prototype status until simpler alternatives with matched information and parameter access are tested fairly.

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
