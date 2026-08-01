# Benchmark Specification

## Purpose

This document freezes the benchmark structure before the project generates confirmatory results.

The goal is not merely to show that the full model can produce interesting behavior. The goal is to determine whether its proposed mechanisms are necessary, identifiable, numerically stable, and empirically useful.

## Model family

All comparisons must use matched state dimensions, comparable parameter budgets, identical initial-condition families, and the same numerical accuracy targets.

### $M_0$: Fixed graph, local dynamics

- Fixed topology.
- Fixed edge weights.
- No metric deformation.
- No collective projection.

This is the minimal local baseline.

### $M_1$: Adaptive graph without collective projection

- Dynamic edge activation.
- Optional dynamic edge weights.
- No tangent-space or normal-space projection.

This tests whether adaptive topology alone explains the observed behavior.

### $M_2$: Fixed geometry with collective projection

- Fixed graph and metric.
- Dynamic local states.
- Global admissibility projection enabled.

This isolates the contribution of the collective constraint.

### $M_3$: Dynamic geometry with soft penalties

- Dynamic graph and metric.
- Coherence enforced through penalty terms rather than exact projection.

This tests whether exact projection is necessary.

### $M_4$: Full proposed geometry

- Dynamic local states.
- Dynamic edge activation.
- Dynamic metric deformation.
- Dynamic compatibility structure where implemented.
- Collective admissibility projection.
- Non-collapse barrier where relevant.
- Presentation-equivariance requirements.

## Benchmark stage A: Exact synthetic systems

### A1. Three-node scalar model

Purpose:

- verify implementation consistency;
- measure $\chi_i$;
- test permutation equivariance;
- exercise dynamic edge and metric variables.

Required checks:

- reference right-hand-side parity;
- convergence under decreasing time step;
- inverse-permutation trajectory agreement;
- deterministic replay;
- finite-value tripwire;
- constraint-error trace.

### A2. Constrained pendulum or linkage

Purpose:

- verify exact constraint preservation;
- compare projection with multiplier and penalty methods;
- measure energy drift.

Required outputs:

- geometric constraint error;
- velocity constraint error;
- energy error;
- projection magnitude;
- solver cost.

### A3. Divergence-free lattice flow

Purpose:

- test a known local-proposal/global-correction structure;
- determine whether the implementation reproduces a standard projection result.

Required outputs:

- divergence norm before and after correction;
- kinetic-energy change;
- projection residual;
- grid-refinement behavior.

### A4. Adaptive synchronization network

Purpose:

- compare fixed, adaptive, and geometry-coupled networks;
- test whether metric deformation contributes beyond edge adaptation.

Required outputs:

- order parameter;
- convergence time;
- topology trajectory;
- intrinsic-distance trajectory;
- perturbation recovery.

### A5. Compatibility or consensus network

Purpose:

- test local-to-global agreement;
- compare ordinary graph Laplacian dynamics with compatibility-aware dynamics.

Required outputs:

- local mismatch energy;
- global consistency residual;
- convergence rate;
- failure under incompatible local assignments.

## Benchmark stage B: Mechanism isolation

Each benchmark must run all applicable models $M_0$ through $M_4$.

Required ablations:

1. freeze $q$;
2. freeze $s$;
3. freeze both $q$ and $s$;
4. remove collective projection;
5. replace projection with a matched penalty;
6. replace endogenous collective state with a matched exogenous signal;
7. remove the barrier;
8. randomize graph structure while preserving basic graph statistics;
9. permute initial states while holding structure fixed;
10. relabel nodes and invert the permutation at evaluation.

An ablation is informative only if the removed mechanism had an opportunity to act in the selected regime.

## Benchmark stage C: Physical anchors

### C1. Incompressible-flow anchor

Minimum requirement:

- reproduce a standard projection-based incompressible-flow result before adding dynamic geometry.

Comparison question:

> Does the proposed relational geometry improve prediction, stability, adaptivity, or interpretation without violating incompressibility?

### C2. Constrained-mechanics anchor

Minimum requirement:

- reproduce a standard constrained trajectory with known invariants or reference solution.

Comparison question:

> Does the evolving metric or compatibility structure capture behavior not represented by ordinary constrained mechanics?

### C3. Adaptive synchronization or flocking anchor

Minimum requirement:

- reproduce a standard adaptive-network result.

Comparison question:

> Does intrinsic geometry provide a measurable contribution beyond adaptive weights and topology?

## Primary metrics

### Constraint error

$$
\epsilon_{\Gamma}(t)=\|\Gamma(Z(t))\|.
$$

Report maximum, mean, final, and integrated error.

### Local-versus-collective influence

$$
\chi_i(t)
=
\frac{\|F_i^{\mathrm{collective}}(t)\|}
{\|F_i^{\mathrm{local}}(t)\|+\epsilon}.
$$

Report distributions across nodes, time, regimes, and seeds.

### Metric evolution

$$
\Delta_{\mathrm{metric}}(t)
=
\|g(t+\Delta t)-g(t)\|.
$$

Report alongside state change so that geometric motion is not mistaken for state motion.

### Energy behavior

$$
\Delta E(t)=E(t)-E(0).
$$

Use only when the modeled system has a defined conserved or dissipative energy law.

### Predictive performance

Use task-appropriate measures such as:

- trajectory error;
- event-time error;
- held-out likelihood;
- perturbation-response error;
- synchronization-time error;
- structural-transition prediction.

### Complexity and cost

Report:

- trainable or fitted parameter count;
- solver evaluations;
- wall-clock time;
- memory usage;
- projection-system condition number where applicable.

## Fairness requirements

- Tune each baseline using the same validation budget.
- Match observation access across models.
- Do not give the full model privileged state information.
- Report failed runs and singular cases.
- Use the same train, validation, and test divisions.
- Freeze evaluation code before final test execution.
- Distinguish exploratory from confirmatory runs.

## Numerical protocol

Each reported result must include:

- exact source commit;
- environment lockfile or dependency manifest;
- solver name and version;
- absolute and relative tolerances;
- time step or adaptive-step controls;
- seed manifest;
- initial-condition manifest;
- complete parameter file;
- raw output checksum.

At least one independently written reference implementation must agree within declared tolerances on the minimal systems.

## Statistical protocol

Structural interventions, not nested solver seeds or repeated probes, are the primary inferential units when the scientific question concerns structure.

Report:

- effect sizes;
- uncertainty intervals;
- the number and type of independent structural units;
- all exclusions;
- multiplicity treatment where multiple hypotheses are tested.

## Acceptance criteria for the full model

The full model earns further study only when it satisfies all applicable conditions:

1. passes numerical and invariance tripwires;
2. preserves constraints at the declared tolerance;
3. remains stable across reasonable solver changes;
4. outperforms or explains behavior not captured by simpler models;
5. retains the effect under matched parameter budgets;
6. survives relevant structural controls;
7. produces at least one preregistered discriminating signature.

## Reporting template

Every benchmark report must contain:

1. question;
2. preregistered hypothesis;
3. compared models;
4. data or system definition;
5. fixed metrics;
6. numerical protocol;
7. raw and summarized results;
8. ablations;
9. failure analysis;
10. claim-ledger updates;
11. explicit non-claims.
