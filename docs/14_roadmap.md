# ARG Roadmap

## Operating rule

ARG advances by passed gates, not by calendar optimism. A phase is complete only when its exit criteria pass and the claim ledger is aligned.

## Binding claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Execution authorization

$$
\boxed{
\text{development pilot authorized};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

No Phase 5 trajectory was generated. Authorization is not execution.

## Current position

| Phase | Status | Result |
|---|---|---|
| Phase 0 — Alignment and claim control | COMPLETE | Public and internal descriptions aligned. |
| Phase 1 — Four-model design contract | COMPLETE | Contract v1.0 frozen. |
| Phase 2 — Implement and verify $M_0$ | COMPLETE | No-feedback baseline merged and independently parity-tested. |
| Phase 3 — Implement and verify $M_P$ | COMPLETE | Projection sandbox merged and hosted-tested. |
| Phase 4 — Implement and verify $M_{FP}$ | COMPLETE | Combined model merged; 51 tests passed on Python 3.10 and 3.12. |
| Phase 5 — Freeze comparative experiment protocol | COMPLETE | Data-free protocol, manifests, executable metrics, decision rules, and lock frozen; 65 tests passed on Python 3.10 and 3.12. |
| Phase 6 — Development pilot | IN PROGRESS | Pilot runner and archival pipeline are the active implementation gate; no pilot has run. |
| Phase 7 onward | BLOCKED | Confirmatory execution remains unauthorized. |

Software tests verify declared code and protocol contracts. They do not validate the scientific hypothesis.

---

# Completed implementation phases

## Phase 0 — Alignment

**PASS.** The repository uses the canonical $M_0/M_F/M_P/M_{FP}$ split and distinguishes collective feedback from global-admissibility projection.

## Phase 1 — Frozen model contract

**PASS.** `15_four_model_design_contract.md` freezes equations, ordering, RK4 and retraction policies, singular behavior, diagnostics, observation maps, and the independent-reference boundary.

## Phase 2 — $M_0$

**PASS.** Exact no-feedback dynamics, no hidden $c(x)$ transition path, zero-feedback reduction from $M_F$, and independent derivative/RK4 parity were established at software level.

## Phase 3 — $M_P$

**PASS.** The constant-amplitude projector

$$
\Gamma(Z)=\frac13x^Tx-c_0=0,
\qquad
f_P=f_0-x\frac{x^Tf_0}{x^Tx}
$$

was implemented with projected RK4 stages, mandatory retraction, fail-closed singular handling, and independent parity.

Verification: PR `#5`, merge `97a9f6b7222b4543ee8184fb8e42b47b53ddf92c`, Actions `30717582276`, 35 tests in each configured Python environment.

## Phase 4 — $M_{FP}$

**PASS.** The frozen ordering

$$
F_{\mathrm{proposal}}=F_0+F_F
$$

followed by projection was implemented. At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

while feedback remains in $s$ and $q$; therefore same-state derivative identity does not imply trajectory identity.

Verification: PR `#7`, merge `205fb8c5bf1b832e241af230612e3d7056be05f5`, Actions `30718821666`, 51 tests in each configured Python environment.

## Phase 5 — Frozen comparative protocol

**PASS.** Protocol `ARG-P5-COMP-v1` was frozen before trajectory generation.

The primary question is whether $M_F$ and $M_P$ are distinguishable under the full-state map. The protocol freezes:

- symmetric normalized RMS trajectory distance;
- detection threshold $0.02$;
- scoped-equivalence margin $0.002$;
- direction-level inferential units;
- a deterministic 24-direction, five-amplitude design;
- 10 pilot directions and 14 held-out confirmatory directions;
- fixed parameters with no fitting;
- RK4 refinement and segmented DOP853 replication;
- numerical floors, exclusions, stop rules, and immutable provenance;
- executable bootstrap and fail-closed decision logic;
- a SHA-256 protocol lock.

Hosted verification reported 65 passing tests on Python 3.10 and 65 on Python 3.12. These are protocol/software tests, not experimental observations.

See `18_phase5_comparative_protocol.md` and `protocol/phase5_v1/`.

---

# Phase 6 — Development pilot

## Objective

Implement and verify a runner that executes **pilot configurations only** and produces a complete immutable archive without allowing confirmatory access.

## Required implementation

- load and verify `LOCK.json` before execution;
- reject every configuration labeled `confirmatory`;
- execute all four models on the 50 frozen pilot configurations;
- run the three RK4 resolutions and alternate DOP853 policy;
- record all observation maps and mechanism diagnostics;
- implement exogenous-replay and frozen-$s/q$ controls exactly as declared;
- run all permutation tripwires;
- retain failures and singular runs without imputation;
- produce `RUN_MANIFEST.json`, environment records, raw outputs, summaries, `failures.jsonl`, and `checksums.sha256`;
- compute developmental summaries without changing thresholds, manifests, or the held-out split.

## Phase 6 claim ceiling

Pilot results may identify numerical defects, degeneracies, uninformative observables, or protocol amendments. They cannot support a confirmatory mechanism claim.

Any substantive amendment creates protocol v1.1 or later and requires a fresh, still-unexecuted confirmatory set.

## Exit criteria

- runner and archive schema pass independent tests;
- confirmatory-access tripwires fail closed;
- deterministic replay and checksums agree;
- pilot numerical gates are applied exactly;
- every failure is retained;
- pilot outcome is labeled developmental;
- no confirmatory trajectory has been generated.

# Phase 7 — Confirmatory four-model experiment

Blocked. Only a separately authorized held-out execution may support scoped comparative claims.

Permitted outcomes include detection, restricted observational equivalence, inconclusive, or invalid. None establishes a fundamental geometry.

# Phase 8 — Relational projection v2

A constraint involving mismatch, $s$, $q$, intrinsic distance, or compatibility requires a new versioned model contract.

# Phase 9 — Physical anchors

Initial order:

1. constrained mechanics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

## Immediate next action

Implement and independently verify the Phase 6 pilot runner without executing confirmatory configurations.
