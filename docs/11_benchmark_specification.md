# Benchmark Specification

## Purpose

This document freezes the comparison structure before ARG generates confirmatory results.

The goal is to determine whether collective feedback, admissibility projection, and their combination are necessary, identifiable, numerically stable, and scientifically useful.

## Current authorization

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

Current software work may verify $M_F$, design and implement $M_0$, and mathematically specify $M_P$. Comparative projected-geometry claims remain blocked.

## Canonical model family

All comparisons must use matched state dimensions where possible, comparable parameter budgets, identical initial-condition families, equal observation access, and the same numerical-accuracy targets.

### $M_0$: Local/adaptive substrate baseline

- local nonlinear node dynamics;
- neighborhood coupling;
- adaptive topology and metric variables where declared;
- no collective statistic in constituent transition equations;
- no tangent-space or normal-space projection.

This is the mechanism-free baseline for the two global mechanisms under study.

### $M_F$: Collective-feedback prototype

- $M_0$ substrate;
- endogenous statistic $c(x)$;
- declared feedback paths into $\dot x$, $\dot s$, or $\dot q$;
- no admissibility projection.

The current executable three-node model is $M_F$.

### $M_P$: Projected-admissibility prototype

- explicit state and proposal field;
- explicit admissible set $\mathcal M=\{Z:\Gamma(Z)=0,H(Z)\geq0\}$;
- implemented tangent-space or normal-space projection;
- tested constraint preservation;
- no collective feedback unless separately declared.

$M_P$ is currently unimplemented.

### $M_{FP}$: Feedback plus projection

- collective feedback as in $M_F$;
- projection as in $M_P$;
- separately measurable feedback and projection vectors;
- exact reductions to $M_0$, $M_F$, and $M_P$.

$M_{FP}$ is currently unimplemented.

### Secondary control: $M_{\lambda}$

A matched soft-penalty model may be included to test whether exact projection adds value beyond penalty enforcement. It is a secondary control and does not replace the canonical four-model comparison.

## Stage A: Equation and software verification

### A1. Current $M_F$ prototype

Purpose:

- verify code-equation parity;
- map all collective substrate paths;
- test permutation equivariance;
- exercise adaptive edge and metric variables.

Required checks:

- independent right-hand-side agreement;
- convergence under decreasing time step;
- inverse-permutation trajectory agreement;
- deterministic replay;
- finite-value tripwire;
- exact parameter manifest;
- intentional mutation test proving feedback tests fail when a path is broken.

### A2. $M_0$ reduction

Purpose:

- create a true no-collective baseline;
- prove that every $c(x)$ transition path is absent;
- verify exact reduction from $M_F$ when feedback coefficients are removed.

Required checks:

- dependency audit;
- exact equation comparison;
- matched initial conditions;
- identical local and adaptive parameters;
- no diagnostic statistic entering transitions.

## Stage B: Projection verification

This stage is blocked until the $M_P$ design contract is frozen.

### B1. Constraint definition

Record:

- complete state vector;
- $\Gamma$ and $H$;
- domains;
- rank conditions;
- active-set rules;
- state-space metric;
- singularity policy.

### B2. Projection implementation

Required outputs:

- local proposal;
- tangent component;
- normal correction;
- constraint Jacobian;
- projection-system condition number;
- retraction or constraint-integrator correction;
- failure state for rank deficiency.

### B3. Preservation tests

Report:

$$
\epsilon_\Gamma(t)=\|\Gamma(Z(t))\|,
$$

including maximum, mean, final, and integrated error under solver refinement.

For inequalities, report active-set transitions and violation margins.

### B4. Reference comparisons

Compare projection against:

- an independently written projector;
- a differential-algebraic or multiplier formulation where applicable;
- the matched soft-penalty control $M_{\lambda}$.

## Stage C: Four-model mechanism comparison

Run

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}
$$

under matched conditions.

### C1. Feedback contribution

$$
\chi_i^F(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

### C2. Projection contribution

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{0,i}(t)+F_{F,i}(t)\|+\epsilon}.
$$

For $M_P$, set $F_F=0$.

### C3. Combined interaction

Use a preregistered trajectory or observable distance $\Delta$ and define

$$
R_{FP}
=
\Delta(M_{FP},M_0)
-
\Delta(M_F,M_0)
-
\Delta(M_P,M_0).
$$

Interpretation requires care because nonlinear model effects need not add linearly.

### C4. Equivalence analysis

Do not infer

$$
M_F\equiv M_P
$$

from similar aggregate plots.

Test:

- vector-field equality or reparameterization;
- local Jacobians;
- fixed points and stability;
- bifurcations;
- perturbation response;
- full-state trajectory distance;
- partial-observation identifiability;
- domain and parameter dependence.

An equivalence claim requires exact mathematics, a bounded approximation, or a declared observational equivalence.

## Stage D: Dynamic-geometry ablation

Within each applicable model compare:

1. dynamic $q$ and $s$;
2. frozen $q$;
3. frozen $s$;
4. frozen $q$ and $s$;
5. static graph with parameter-matched node dynamics.

This tests whether geometry contributes beyond extra adaptive state variables.

## Stage E: Exact or established systems

### E1. Constrained pendulum or linkage

Purpose:

- verify exact constraint behavior;
- compare projection, multiplier, and penalty methods;
- measure energy drift.

### E2. Divergence-free lattice flow

Purpose:

- reproduce a known local-proposal/global-correction structure;
- evaluate whether any ARG extension adds value without violating incompressibility.

### E3. Adaptive synchronization network

Purpose:

- compare local, feedback, projection, and combined variants;
- test whether intrinsic metric dynamics add information beyond adaptive weights.

### E4. Compatibility or consensus network

Purpose:

- compare ordinary graph-Laplacian dynamics with compatibility-aware variants;
- test local mismatch and global consistency measures.

## Required interventions

1. alter graph structure while state is fixed;
2. alter state while graph structure is fixed;
3. replace $c(x)$ with a matched exogenous signal;
4. relabel the entire system and invert the permutation;
5. remove feedback only;
6. remove projection only;
7. remove both;
8. replace projection with a matched penalty;
9. freeze geometry variables;
10. test singular and near-singular projection cases.

An intervention is informative only if the affected mechanism had an opportunity to act.

## Primary metrics

### Constraint error

$$
\epsilon_\Gamma(t)=\|\Gamma(Z(t))\|.
$$

Applicable only to $M_P$, $M_{FP}$, and constraint controls.

### Feedback magnitude

$$
\chi_i^F(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

Applicable to $M_F$ and $M_{FP}$.

### Projection magnitude

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{0,i}(t)+F_{F,i}(t)\|+\epsilon}.
$$

Applicable to $M_P$ and $M_{FP}$.

### Metric evolution

$$
\Delta_{\mathrm{metric}}(t)
=
\|g(t+\Delta t)-g(t)\|.
$$

### Energy behavior

$$
\Delta E(t)=E(t)-E(0).
$$

Use only when the modeled system has a declared conserved or dissipative law.

### Predictive and dynamical performance

Use task-appropriate measures such as:

- trajectory error;
- event-time error;
- held-out likelihood;
- perturbation-response error;
- synchronization-time error;
- structural-transition prediction;
- attractor or fixed-point recovery.

### Complexity and cost

Report:

- fitted parameter count;
- state dimension;
- solver evaluations;
- wall-clock time;
- memory usage;
- projection-system condition number;
- failed and singular runs.

## Fairness requirements

- Tune each model using the same validation budget.
- Match observation access.
- Do not give projected or combined models privileged state information without an explicit control.
- Report failed runs and singular cases.
- Use the same data divisions and structural intervention families.
- Freeze evaluation code before final test execution.
- Distinguish exploratory from confirmatory runs.
- Do not count nested seeds as independent structural evidence.

## Numerical protocol

Each reported result must include:

- exact source commit;
- dependency manifest;
- solver and version;
- absolute and relative tolerances;
- step controls;
- seed manifest;
- initial-condition manifest;
- parameter file;
- raw output checksum;
- model contract version.

At least one independent implementation must agree within declared tolerances on the minimal systems.

## Acceptance criteria

A mechanism earns further study only when it:

1. passes equation, numerical, and invariance tripwires;
2. preserves applicable constraints;
3. remains stable across reasonable solver changes;
4. differs from or improves upon simpler alternatives under matched conditions;
5. survives structural and exogenous controls;
6. produces a preregistered discriminating signature;
7. does not require post hoc changes to its defining contract.

## Reporting template

Every benchmark report must contain:

1. question;
2. authorized claim ceiling;
3. preregistered hypothesis;
4. compared models;
5. system or data definition;
6. fixed metrics;
7. numerical protocol;
8. raw and summarized results;
9. interventions and ablations;
10. failure analysis;
11. claim-ledger updates;
12. explicit non-claims.
