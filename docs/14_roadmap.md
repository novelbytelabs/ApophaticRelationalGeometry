# ARG Roadmap

## Operating rule

ARG advances by passed gates, not by calendar optimism. A phase is complete only when its exit criteria pass and the claim ledger is updated.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Current position

| Phase | Status | Result |
|---|---|---|
| Phase 0 — Alignment and claim control | COMPLETE | Public and internal descriptions aligned. |
| Phase 1 — Four-model design contract | COMPLETE | Contract v1.0 frozen. |
| Phase 2 — Implement and verify $M_0$ | COMPLETE | No-feedback baseline merged and independently parity-tested. |
| Phase 3 — Implement and verify $M_P$ | COMPLETE | Projection sandbox merged and hosted-tested. |
| Phase 4 — Implement and verify $M_{FP}$ | COMPLETE | Combined feedback-plus-projection model merged; 51 hosted tests passed on Python 3.10 and 3.12. |
| Phase 5 — Freeze comparative experiment protocol | IN PROGRESS | Scientific protocol gate opened. |
| Phase 6 onward | BLOCKED | Await the frozen Phase 5 protocol. |

Software tests verify declared code contracts. They do not validate the scientific hypothesis.

---

# Completed implementation phases

## Phase 0 — Alignment

**PASS.**

The repository uses the canonical $M_0/M_F/M_P/M_{FP}$ split and distinguishes collective feedback from global-admissibility projection.

## Phase 1 — Frozen contract

**PASS.**

`15_four_model_design_contract.md` freezes the shared substrate, equations, model ordering, RK4 and retraction policies, singular behavior, diagnostics, observation maps, and independent-reference boundary.

## Phase 2 — $M_0$

**PASS.**

Implemented and unit-tested:

- exact no-feedback $F_0$;
- no $c(x)$ transition dependency;
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

Verification record:

- PR `#5`;
- merge `97a9f6b7222b4543ee8184fb8e42b47b53ddf92c`;
- GitHub Actions run `30717582276`;
- Python 3.10: 35 passed;
- Python 3.12: 35 passed.

See `16_phase3_mp_verification.md`.

## Phase 4 — $M_{FP}$

**PASS.**

Implemented the frozen ordering

$$
F_{\mathrm{proposal}}=F_0+F_F,
$$

followed by node-state projection and mandatory retraction.

The same-state structural identity is verified:

$$
\boxed{f_{FP}=f_P},
$$

because the node-feedback term is radial and $P_Tx=0$.

The identity does not imply trajectory equivalence. $M_{FP}$ retains feedback in $s$ and $q$, so its adaptive substrate can diverge from $M_P$ and alter later node proposals.

Verification record:

- PR `#7`;
- merge `205fb8c5bf1b832e241af230612e3d7056be05f5`;
- GitHub Actions run `30718821666`;
- Python 3.10: 51 passed;
- Python 3.12: 51 passed.

See `17_phase4_mfp_verification.md`.

No physical-adequacy, novelty, equivalence, causal-autonomy, or scientific-performance claim was promoted.

---

# Phase 5 — Freeze comparative experiment protocol

## Objective

Freeze a falsification-oriented protocol that can distinguish the four mechanisms without using exploratory results to choose the final test.

## Required model comparisons

$$
M_0\leftrightarrow M_F,
\qquad
M_0\leftrightarrow M_P,
\qquad
M_P\leftrightarrow M_{FP},
\qquad
M_F\leftrightarrow M_P.
$$

The protocol must explicitly separate:

- feedback effects;
- projection effects;
- adaptive-substrate effects;
- state-dependent geometry;
- numerical artifacts;
- observation-map dependence.

## Required frozen elements

- primary and secondary hypotheses;
- exact observation maps;
- parameter manifest;
- initial-condition manifest;
- structural inferential units;
- intervention and ablation schedule;
- trajectory-distance and mechanism metrics;
- numerical refinement and alternate-integrator policy;
- uncertainty treatment;
- exclusion and stop rules;
- exploratory versus confirmatory separation;
- raw-output schema, source commit, configuration hashes, and checksums;
- claim-promotion and failure rules.

## Central predictions to test

1. $M_F$ and $M_P$ are not assumed dynamically equivalent.
2. At the same full state under contract v1.0,

   $$
   f_{FP}=f_P.
   $$

3. $M_P$ and $M_{FP}$ may nevertheless develop different trajectories because $M_{FP}$ retains $s/q$ feedback.
4. Any claim of equivalence must specify the observation map, domain, and tolerance.
5. Projection may add no useful explanatory or predictive value; that remains an admissible outcome.

## Exit criteria

- protocol document is complete and versioned;
- all hypotheses and metrics are executable;
- manifests and seeds are frozen;
- no unresolved implementation ambiguity remains;
- development-pilot and confirmatory datasets/configurations are separated before execution;
- claim ledger and falsification criteria agree with the protocol.

---

# Phase 6 — Development pilot

Blocked until Phase 5 passes.

Purpose:

- expose numerical failures;
- test whether observables identify the mechanisms;
- identify degeneracies;
- determine whether the sphere projection is informative enough.

Pilot results remain developmental and cannot support confirmatory claims.

# Phase 7 — Confirmatory four-model experiment

Only a frozen held-out run may support comparative mechanism claims.

Permitted outcomes include:

- $M_F\ne M_P$;
- restricted observational equivalence;
- same-state node identity without trajectory identity;
- no useful value from projection beyond simpler controls.

# Phase 8 — Relational projection v2

A later constraint involving mismatch, $s$, $q$, intrinsic distance, or compatibility requires a new versioned contract.

# Phase 9 — Physical anchors

Initial order:

1. constrained mechanics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

## Immediate next action

Create and freeze the Phase 5 comparative experiment protocol before executing any pilot runs.