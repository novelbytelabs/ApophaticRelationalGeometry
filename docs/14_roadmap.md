# ARG Roadmap

## Operating rule

ARG advances by passed gates, not by calendar optimism.

A phase is complete only when its exit criteria are satisfied and the claim ledger is updated. Failed results narrow or stop the program; they do not automatically trigger a more complicated model.

## Binding claim ceiling

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Current position

| Phase | Status | Result |
|---|---|---|
| Phase 0 — Alignment and claim control | COMPLETE | Public and internal descriptions now match the executable evidence. |
| Phase 1 — Four-model design contract | COMPLETE | `15_four_model_design_contract.md` frozen as version 1.0. |
| Phase 2 — Implement and verify $M_0$ | IN PROGRESS | First code gate opened. |
| Phase 3 onward | BLOCKED | Await $M_0$ exit gate. |

Software-test results validate code contracts only. They do not validate the scientific hypothesis.

---

# Phase 0 — Alignment and claim control

## Exit decision

**PASS.**

Completed:

- canonical $M_0/M_F/M_P/M_{FP}$ split;
- explicit claim ceiling;
- feedback/projection documentation separation;
- package and citation metadata alignment;
- claim-ledger and falsification alignment;
- existing software tests retained.

---

# Phase 1 — Freeze the four-model contract

## Exit decision

**PASS.**

The frozen contract now specifies:

- exact equations for $M_0,M_F,M_P,M_{FP}$;
- fixed nine-dimensional substrate;
- constant-amplitude projection sandbox for $M_P$;
- project-after-feedback ordering for $M_{FP}$;
- exact radial-feedback annihilation prediction;
- shared RK4 integrator;
- mandatory retraction for projected models;
- fail-closed singular behavior;
- fixed reference parameters and development initial conditions;
- observation maps and equivalence language;
- independent-reference boundary;
- fairness and safety tripwires.

The sphere constraint is accepted only as a minimal projection-mechanism testbed. It is not the completed relational geometry.

---

# Phase 2 — Implement and verify $M_0$

## Objective

Create a true no-feedback local/adaptive baseline without altering the current $M_F$ behavior.

## Required implementation

- expose a model identifier or dispatch mechanism;
- implement $F_0$ directly from the frozen contract;
- keep $c(x)$ diagnostic-only in $M_0$;
- preserve the current state representation and intrinsic geometry;
- add shared fixed-step RK4 integration without changing the legacy equations;
- retain explicit Euler only as a transparent low-level test helper if needed;
- label every output with model ID and contract version.

## Required tests

- hand-computed $M_0$ derivative;
- no-feedback dependency audit;
- $M_F(\chi=\eta_2=\rho=0)=M_0$ exactly;
- permutation equivariance;
- finite-state and parameter validation;
- independent-reference derivative parity;
- independent-reference RK4 one-step parity;
- regression test proving unchanged $M_F$ derivatives at the reference state.

## Exit criteria

- all existing tests pass;
- all new $M_0$ tests pass;
- no hidden $c(x)$ transition path exists in $M_0$;
- current $M_F$ behavior remains unchanged;
- source and raw outputs identify the selected model;
- implementation and reference paths agree within frozen tolerances;
- claim ledger updated to mark $M_0$ implemented and unit-tested.

## Claim ceiling after completion

Expected ceiling:

$$
M_0,M_F\ \text{implemented and unit-tested};
\quad
M_P,M_{FP},M_F\equiv M_P\ \text{unverified}.
$$

No scientific mechanism claim is promoted merely by implementing $M_0$.

---

# Phase 3 — Implement and verify $M_P$

Blocked until Phase 2 passes.

Required elements:

- tangent projector;
- projected RK4 stages;
- mandatory radial retraction;
- constraint and tangency diagnostics;
- singular fail-closed path;
- independent implementation parity;
- step-refinement evidence.

---

# Phase 4 — Implement and verify $M_{FP}$

Blocked until Phase 3 passes.

Required elements:

- feedback proposal followed by projection;
- exact $f_{FP}=f_P$ node-derivative identity;
- retained $s/q$ feedback;
- exact reduction tests;
- separate feedback and projection diagnostics.

---

# Phase 5 — Freeze comparative experiment protocol

Blocked until all four models pass software and mathematical verification.

The protocol must freeze:

- hypotheses;
- observation maps;
- parameter and initial-condition manifests;
- structural inferential units;
- metrics and uncertainty treatment;
- solver and refinement policy;
- exclusions and stop rules;
- raw-output and checksum policy.

---

# Phase 6 — Development pilot

Purpose:

- find numerical failures;
- test whether observables identify mechanisms;
- expose degeneracies;
- determine whether the sphere projection is informative enough.

Pilot results remain developmental.

---

# Phase 7 — Confirmatory four-model experiment

Only a frozen held-out run may support comparative mechanism claims.

Permitted outcomes include:

- $M_F\ne M_P$;
- restricted observational equivalence;
- $M_{FP}=M_P$ for node dynamics but not geometry;
- no useful value from projection beyond simpler controls.

Negative results narrow the project.

---

# Phase 8 — Relational projection v2

Only after the projection machinery is verified may ARG introduce constraints involving relational mismatch, $s$, $q$, intrinsic distance, or compatibility structure.

Such a model requires a new design contract and may not silently replace version 1.0.

---

# Phase 9 — Physical anchors

Initial anchor order:

1. constrained mechanics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

ARG must reproduce an established result before claiming an extension.

## Immediate next action

Implement the exact $M_0$ baseline and its independent verification suite under the frozen version 1.0 contract.
