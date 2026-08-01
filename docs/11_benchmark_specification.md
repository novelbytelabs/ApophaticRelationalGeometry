# Benchmark Specification

## Purpose

This document fixes the comparison structure before ARG generates scientific results.

The goal is to determine whether collective feedback, admissibility projection, and their combination are identifiable, numerically stable, scientifically useful, and distinguishable from simpler alternatives.

## Current authorization

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

Equation and software verification is complete for the four contract-v1.0 prototypes. Comparative execution remains blocked until the Phase 5 protocol freezes hypotheses, manifests, metrics, inferential units, numerical policies, stop rules, and provenance.

## Canonical model family

All comparisons must use matched state dimensions where possible, comparable parameter budgets, identical initial-condition families, equal observation access, and the same numerical-accuracy targets.

### $M_0$: local/adaptive substrate baseline

- local nonlinear node dynamics;
- neighborhood coupling;
- adaptive edge and metric variables;
- no collective statistic in constituent transition equations;
- no tangent-space projection.

### $M_F$: collective-feedback prototype

- $M_0$ substrate;
- endogenous statistic $c(x)$;
- declared feedback paths into $\dot x$, $\dot s$, and $\dot q$;
- no admissibility projection.

### $M_P$: projected-admissibility prototype

- $M_0$ proposal;
- explicit equality constraint

  $$
  \Gamma(Z)=\frac13x^Tx-c_0=0;
  $$

- node tangent projection;
- projected RK4 stages;
- mandatory radial retraction;
- no collective feedback in proposal equations.

### $M_{FP}$: feedback plus projection

- explicit proposal $F_0+F_F$;
- node tangent projection after feedback;
- retained feedback in $s$ and $q$;
- separately measurable local, feedback, combined-proposal, projection, and retraction terms.

At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

but trajectory identity is not implied because the adaptive-substrate derivatives differ.

### Secondary control: $M_\lambda$

A matched soft-penalty model may be introduced to test whether exact projection adds value beyond penalty enforcement. It is not part of the frozen four-model family and requires a separate preregistered amendment.

---

# Stage A: equation and software verification

## Status

**Complete for contract v1.0.**

Verified elements include:

- independent $M_0/M_F$ derivative and RK4 parity;
- no-$c(x)$ dependency in $M_0$;
- exact $M_F(\chi=\eta_2=\rho=0)=M_0$ reduction;
- $M_P$ projector identities, tangency, retraction, singular handling, and independent parity;
- explicit $M_{FP}$ decomposition into $F_0$, $F_F$, $F_0+F_F$, correction, and projected derivative;
- same-state identity $f_{FP}=f_P$;
- retained $s/q$ feedback;
- zero-feedback $M_{FP}=M_P$ reduction;
- permutation-equivariance tripwires for all four models;
- labeled outputs and configuration hashes.

These are software results only.

---

# Stage B: Phase 5 protocol freeze

## Status

**In progress. No pilot is authorized.**

The protocol must freeze:

- primary and secondary hypotheses;
- parameter and initial-condition manifests;
- development and confirmatory partitions;
- observation maps and tolerances;
- structural inferential units;
- intervention and ablation schedule;
- metrics and uncertainty treatment;
- refinement and alternate-integrator policy;
- exclusions, failures, and stop rules;
- raw-output schema and checksum policy;
- claim-promotion and falsification rules.

---

# Stage C: four-model mechanism comparison

Run

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}
$$

under matched conditions.

## C1. $M_0$ versus $M_F$

Question: does endogenous collective feedback produce behavior not reproduced by the no-feedback adaptive substrate?

Feedback contribution:

$$
\chi_i^F(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

## C2. $M_0$ versus $M_P$

Question: what behavior is attributable to constant-amplitude projection rather than the unprojected substrate?

Projection contribution:

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

## C3. $M_P$ versus $M_{FP}$

Question: when does retained feedback in $s$ and $q$ make $M_{FP}$ distinguishable from $M_P$ despite the same-state node identity?

Required distinction:

$$
f_{FP}(Z)=f_P(Z)
$$

at the same regular state does not imply

$$
\Phi_t^{FP}(Z_0)=\Phi_t^P(Z_0).
$$

The protocol must measure when adaptive-substrate divergence propagates back into node dynamics and intrinsic geometry.

## C4. $M_F$ versus $M_P$

Question: are collective feedback and tangent projection dynamically distinct under the declared domain and observation maps?

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

An equivalence claim requires exact mathematics, a bounded approximation, or declared observational equivalence.

## C5. Combined interaction

Using a preregistered trajectory or observable distance $\Delta$, define

$$
R_{FP}
=
\Delta(M_{FP},M_0)
-
\Delta(M_F,M_0)
-
\Delta(M_P,M_0).
$$

Interpretation requires care because nonlinear effects need not add linearly.

---

# Stage D: dynamic-geometry ablation

Within each applicable model compare:

1. dynamic $q$ and $s$;
2. frozen $q$;
3. frozen $s$;
4. frozen $q$ and $s$;
5. static graph with parameter-matched node dynamics.

This tests whether intrinsic geometry contributes beyond extra adaptive state variables or ordinary weighted-network dynamics.

---

# Stage E: established-system anchors

## E1. Constrained pendulum or linkage

- verify exact constraint behavior;
- compare projection, multiplier, and penalty methods;
- measure energy drift.

## E2. Divergence-free lattice flow

- reproduce a known local-proposal/global-correction structure;
- evaluate whether an ARG extension adds value without violating incompressibility.

## E3. Adaptive synchronization network

- compare local, feedback, projection, and combined variants;
- test whether intrinsic metric dynamics add information beyond adaptive weights.

## E4. Compatibility or consensus network

- compare graph-Laplacian dynamics with compatibility-aware variants;
- test local mismatch and global consistency measures.

No physical-anchor claim is authorized until the synthetic four-model protocol is stable.

---

# Required interventions

1. alter graph structure while state is fixed;
2. alter state while graph structure is fixed;
3. replace $c(x)$ with a matched exogenous signal;
4. relabel the entire system and invert the permutation;
5. remove feedback only;
6. remove projection only;
7. remove both;
8. replace projection with a matched penalty under a separate amendment;
9. freeze geometry variables;
10. test singular and near-singular projection cases.

An intervention is informative only if the affected mechanism had an opportunity to act.

---

# Observation maps

Every conclusion must name its observation map.

## Full state

$$
O_{\mathrm{full}}(Z)=(x,s,q).
$$

## Node state

$$
O_x(Z)=x.
$$

## Adaptive substrate

$$
O_{sq}(Z)=(s,q).
$$

## Intrinsic geometry

$$
O_d(Z)=(d_{01},d_{02},d_{12}).
$$

## Mechanism map

Include local proposal, feedback, combined proposal, projection correction, constraint residual, tangency residual, denominator, and retraction magnitude.

A model may be equivalent under one observation map and distinguishable under another. Unqualified equivalence language is prohibited.

---

# Primary metrics

## Constraint error

$$
\epsilon_\Gamma(t)=|\Gamma(Z(t))|.
$$

Applicable to $M_P$, $M_{FP}$, and constraint controls.

## Feedback magnitude

$$
\chi_i^F(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

Applicable to $M_F$ and $M_{FP}$.

## Projection magnitude

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{\mathrm{proposal},i}(t)\|+\epsilon}.
$$

Applicable to $M_P$ and $M_{FP}$.

## Trajectory discrepancy

For declared observation map $O$,

$$
D_O(A,B)
=
\sup_{t\in[0,T]}
\|O(Z_A(t))-O(Z_B(t))\|.
$$

The protocol must specify normalization, aggregation, and tolerance.

## Metric evolution

$$
\Delta_{\mathrm{metric}}(t)
=
\|d(t+\Delta t)-d(t)\|.
$$

## Predictive and dynamical performance

Use task-appropriate measures such as:

- trajectory error;
- event-time error;
- held-out likelihood;
- perturbation-response error;
- synchronization-time error;
- structural-transition prediction;
- attractor or fixed-point recovery.

## Complexity and cost

Report:

- fitted parameter count;
- state dimension;
- solver evaluations;
- wall-clock time;
- memory usage;
- failed and singular runs.

---

# Fairness requirements

- Tune each model using the same validation budget.
- Match observation access.
- Do not give projected or combined models privileged state information without an explicit control.
- Report failed runs and singular cases.
- Use the same data divisions and structural intervention families.
- Freeze evaluation code before final test execution.
- Distinguish exploratory from confirmatory runs.
- Do not count nested seeds or solver steps as independent structural evidence.
- Report parameter-count and mechanism-access differences.

---

# Numerical protocol

Each reported result must include:

- exact source commit;
- dependency manifest;
- solver and version;
- absolute and relative tolerances;
- step controls;
- seed manifest;
- initial-condition manifest;
- parameter file;
- raw-output checksum;
- model contract version.

Require runs at

$$
\Delta t,\quad \Delta t/2,\quad \Delta t/4,
$$

and a second appropriate integration method before strong scientific conclusions.

At least one independent implementation must agree within declared tolerances on the minimal systems.

---

# Acceptance criteria

A mechanism earns further study only when it:

1. passes equation, numerical, and invariance tripwires;
2. preserves applicable constraints;
3. remains stable across reasonable solver changes;
4. differs from or improves upon simpler alternatives under matched conditions;
5. survives structural and exogenous controls;
6. produces a preregistered discriminating signature;
7. does not require post hoc changes to its defining contract.

Failure is an admissible outcome and must narrow or stop the affected claim.

---

# Reporting template

Every benchmark report must contain:

1. question;
2. authorized claim ceiling;
3. preregistered hypothesis;
4. compared models;
5. system or data definition;
6. fixed observation maps and metrics;
7. numerical protocol;
8. raw and summarized results;
9. interventions and ablations;
10. failure analysis;
11. claim-ledger updates;
12. explicit non-claims.
