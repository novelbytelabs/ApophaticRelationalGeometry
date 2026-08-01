# ARG Roadmap

## Operating rule

ARG advances by passed gates, not by calendar optimism.

A phase is complete only when its exit criteria are satisfied and the claim ledger is updated. Failed results narrow or stop the program; they do not automatically trigger a more complicated model.

## Binding claim ceiling

$$
\boxed{
M_0,M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Current position

| Phase | Status | Result |
|---|---|---|
| Phase 0 — Alignment and claim control | COMPLETE | Public and internal descriptions match the executable evidence. |
| Phase 1 — Four-model design contract | COMPLETE | `15_four_model_design_contract.md` frozen as version 1.0. |
| Phase 2 — Implement and verify $M_0$ | COMPLETE | $M_0$ merged with independent derivative/RK4 parity, reduction, equivariance, and no-feedback tripwires. |
| Phase 3 — Implement and verify $M_P$ | IN PROGRESS | Projection implementation gate opened. |
| Phase 4 onward | BLOCKED | Await $M_P$ exit gate. |

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
- claim-ledger and falsification alignment.

---

# Phase 1 — Freeze the four-model contract

## Exit decision

**PASS.**

The frozen contract specifies:

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

The sphere constraint is only a minimal projection-mechanism testbed. It is not the completed relational geometry.

---

# Phase 2 — Implement and verify $M_0$

## Exit decision

**PASS.**

Merged implementation:

- canonical model dispatch;
- exact no-feedback $F_0$;
- no $c(x)$ transition dependency in $M_0$;
- unchanged legacy $M_F$ right-hand side;
- shared classical fixed-step RK4;
- model ID and contract-version labels in raw outputs;
- fail-closed dispatch for unimplemented $M_P$ and $M_{FP}$;
- independent reference equations and RK4 path;
- hosted pytest workflow for future runs.

Verification completed:

- hand-computed $M_0$ derivative;
- fixed $M_F$ regression vector;
- exact $M_F(\chi=\eta_2=\rho=0)=M_0$ reduction;
- no-feedback dependency tripwire;
- permutation equivariance;
- production/reference derivative parity;
- production/reference RK4 parity;
- invalid-parameter and unimplemented-model fail-closed tests;
- labeled-output test;
- all five original tests retained.

A clean local reconstruction passed **20 software tests**. No hosted check run was attached at merge time; therefore the result is local software verification plus merged code review, not hosted-CI attestation.

## Claim promotion

Only $M_0$ is promoted:

$$
M_0=\text{implemented and unit-tested}.
$$

No projection, equivalence, causal-autonomy, or scientific-performance claim is promoted.

---

# Phase 3 — Implement and verify $M_P$

## Objective

Implement the constant-amplitude projection sandbox exactly as frozen:

$$
\Gamma(Z)=c(x)-c_0=0,
\qquad
c_0=c(x(0))>0,
$$

$$
f_P
=
f_0-x\frac{x^Tf_0}{x^Tx}.
$$

## Required implementation

- projection target object carrying $c_0$;
- tangent projector or algebraically equivalent correction;
- projected derivative with $s,q$ following $M_0$;
- RK4 stage projection;
- mandatory post-step radial retraction;
- constraint residual, tangency residual, correction norm, and retraction magnitude;
- declared near-singular threshold and fail-closed exception;
- model-labeled outputs and configuration capture.

## Required mathematical and software checks

- $P_T^T=P_T$;
- $P_T^2=P_T$;
- $P_Tx=0$;
- $x^Tf_P=0$;
- $\frac{d}{dt}\Gamma=0$ in continuous time;
- hand-computed projection case;
- retraction restores $c(x)=c_0$;
- zero-norm and near-singular paths fail closed;
- permutation equivariance;
- independent derivative and RK4/retraction parity;
- step-refinement evidence for raw drift and retraction magnitude;
- $M_0$ and $M_F$ regression suites remain passing.

## Exit criteria

- explicit projection code matches contract v1.0;
- all projection identities and preservation tests pass;
- production and independent reference paths agree;
- singular behavior is fail-closed;
- all prior tests remain passing;
- claim ledger is updated only after the complete gate passes.

## Claim ceiling after completion

At most:

$$
M_0,M_F,M_P\ \text{implemented and unit-tested};
\quad
M_{FP},\ M_F\equiv M_P\ \text{unverified}.
$$

This would verify a projection implementation, not its physical adequacy.

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

Implement the frozen $M_P$ projection sandbox with independent parity, preservation, singular-path, and step-refinement tests.
