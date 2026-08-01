# ARG Roadmap

## Operating rule

ARG advances by passed gates, not by calendar optimism. A phase is complete only when its exit criteria pass and the claim ledger is updated.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P\ \text{implemented and unit-tested};
\quad
M_{FP}\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Current position

| Phase | Status | Result |
|---|---|---|
| Phase 0 — Alignment and claim control | COMPLETE | Public and internal descriptions aligned. |
| Phase 1 — Four-model design contract | COMPLETE | Contract v1.0 frozen. |
| Phase 2 — Implement and verify $M_0$ | COMPLETE | No-feedback baseline merged and independently parity-tested. |
| Phase 3 — Implement and verify $M_P$ | COMPLETE | Projection sandbox merged; 35 hosted tests passed on Python 3.10 and 3.12. |
| Phase 4 — Implement and verify $M_{FP}$ | IN PROGRESS | Combined-mechanism gate opened. |
| Phase 5 onward | BLOCKED | Await $M_{FP}$ exit gate. |

Software tests verify declared code contracts. They do not validate the scientific hypothesis.

---

# Completed phases

## Phase 0 — Alignment

**PASS.**

The repository uses the canonical $M_0/M_F/M_P/M_{FP}$ split and distinguishes feedback from projection.

## Phase 1 — Frozen contract

**PASS.**

`15_four_model_design_contract.md` freezes:

- the common nine-dimensional substrate;
- exact equations for all four models;
- the constant-amplitude $M_P$ sandbox;
- project-after-feedback ordering for $M_{FP}$;
- shared RK4;
- mandatory retraction for projected models;
- singular fail-closed behavior;
- diagnostics, observation maps, and independent-reference rules.

## Phase 2 — $M_0$

**PASS.**

Implemented and unit-tested:

- exact no-feedback $F_0$;
- no $c(x)$ transition dependency;
- unchanged $M_F$ regression behavior;
- exact zero-feedback reduction $M_F=M_0$;
- independent derivative and RK4 parity.

## Phase 3 — $M_P$

**PASS.**

Implemented:

$$
\Gamma(Z)=c(x)-c_0=\frac13x^Tx-c_0=0,
$$

$$
f_P=f_0-x\frac{x^Tf_0}{x^Tx}.
$$

The implementation includes:

- explicit target and tangent projector;
- separate proposal, correction, and projected derivative;
- projection at all four RK4 stages;
- mandatory radial retraction;
- constraint, tangency, denominator, correction, and retraction diagnostics;
- fail-closed singular handling;
- independent derivative and step parity;
- permutation equivariance;
- step-refinement tripwires.

Verification record:

- PR `#5`;
- merge `97a9f6b7222b4543ee8184fb8e42b47b53ddf92c`;
- GitHub Actions run `30717582276`;
- Python 3.10: 35 passed;
- Python 3.12: 35 passed.

See `16_phase3_mp_verification.md`.

No physical-adequacy, novelty, equivalence, or scientific-performance claim was promoted.

---

# Phase 4 — Implement and verify $M_{FP}$

## Objective

Implement feedback followed by projection while keeping the two mechanisms separately observable.

The proposal is

$$
F_{\mathrm{proposal}}=F_0+F_F.
$$

The node derivative is

$$
f_{FP}=P_T\left(f_0-\chi c(x)x\right).
$$

Because

$$
P_Tx=0,
$$

contract v1.0 predicts

$$
\boxed{f_{FP}=f_P}
$$

for node derivatives.

The $s$ and $q$ derivatives retain $M_F$ feedback:

$$
\dot s^{(FP)}\ne\dot s^{(P)},
\qquad
\dot q^{(FP)}\ne\dot q^{(P)}
$$

when $\eta_2$ or $\rho$ is nonzero.

## Required implementation

- feedback proposal followed by the existing projection path;
- retained $s/q$ feedback;
- separate feedback and projection diagnostics;
- projected RK4 stages and mandatory retraction;
- fail-closed singular behavior identical to $M_P$;
- model-labeled raw output;
- independent reference implementation.

## Required identities and reductions

- exact node identity $f_{FP}=f_P$ within frozen tolerance;
- $M_{FP}$ with projection disabled equals $M_F$;
- $M_{FP}$ with $\chi=\eta_2=\rho=0$ equals $M_P$;
- disabling both mechanisms recovers $M_0$;
- $s/q$ feedback remains present when declared;
- permutation equivariance;
- production/reference derivative and RK4 parity;
- all 35 existing tests remain passing.

## Exit ceiling

At most:

$$
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
$$

Completing $M_{FP}$ will not establish that feedback and projection are scientifically equivalent.

---

# Phase 5 — Freeze comparative experiment protocol

Blocked until all four models pass software verification.

The protocol must freeze:

- hypotheses and observation maps;
- parameter and initial-condition manifests;
- structural inferential units;
- metrics and uncertainty treatment;
- refinement and solver policies;
- exclusions and stop rules;
- raw-output, source-commit, and checksum policy.

# Phase 6 — Development pilot

Use the frozen protocol to expose numerical failures, degeneracies, and insufficient observables. Pilot results remain developmental.

# Phase 7 — Confirmatory four-model experiment

Only a held-out run may support comparative mechanism claims.

# Phase 8 — Relational projection v2

A later constraint involving mismatch, $s$, $q$, distance, or compatibility requires a new versioned contract.

# Phase 9 — Physical anchors

Initial order:

1. constrained mechanics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

## Immediate next action

Implement and independently verify $M_{FP}$ under contract v1.0.
