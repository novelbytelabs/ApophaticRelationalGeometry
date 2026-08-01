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

## Current execution state

$$
\boxed{
\text{pilot-only runner verified};
\quad
\text{development pilot not executed};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

## Current position

| Phase | Status | Result |
|---|---|---|
| Phase 0 — Alignment and claim control | COMPLETE | Public and internal descriptions aligned. |
| Phase 1 — Four-model design contract | COMPLETE | Contract v1.0 frozen. |
| Phase 2 — Implement and verify $M_0$ | COMPLETE | No-feedback baseline merged and independently parity-tested. |
| Phase 3 — Implement and verify $M_P$ | COMPLETE | Projection sandbox merged and hosted-tested. |
| Phase 4 — Implement and verify $M_{FP}$ | COMPLETE | Combined model merged; 51 tests passed in each configured Python environment. |
| Phase 5 — Freeze comparative experiment protocol | COMPLETE | Data-free protocol and executable decision rules frozen; 65 tests passed in each configured environment. |
| Phase 6A — Implement pilot-only runner | COMPLETE | Fail-closed runner, numerical gates, controls, and immutable archive verified; 100 tests passed in each configured environment. |
| Phase 6B — Execute development pilot | NEXT GATE | Requires a separate committed authorization naming the verified runner commit. No pilot has run. |
| Phase 7 onward | BLOCKED | Confirmatory execution remains unauthorized. |

Software tests verify declared code and protocol contracts. They do not validate the scientific hypothesis.

---

# Completed gates

## Phases 0–2

Alignment, the frozen model contract, and the exact no-feedback $M_0$ baseline passed their declared software gates.

## Phase 3 — $M_P$

The constant-amplitude projector

$$
\Gamma(Z)=\frac13x^Tx-c_0=0,
\qquad
f_P=f_0-x\frac{x^Tf_0}{x^Tx}
$$

was implemented with projected RK4 stages, mandatory retraction, fail-closed singular handling, and independent parity.

Verification: PR `#5`, merge `97a9f6b7222b4543ee8184fb8e42b47b53ddf92c`, Actions `30717582276`, 35 tests in each configured Python environment.

## Phase 4 — $M_{FP}$

The frozen ordering $F_{\mathrm{proposal}}=F_0+F_F$ followed by projection was implemented. At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

while feedback remains in $s$ and $q$.

Verification: PR `#7`, merge `205fb8c5bf1b832e241af230612e3d7056be05f5`, Actions `30718821666`, 51 tests in each configured Python environment.

## Phase 5 — Frozen comparative protocol

Protocol `ARG-P5-COMP-v1` froze the primary and secondary hypotheses, observation maps, thresholds, direction-level units, deterministic pilot/confirmatory split, parameters, numerical replication, exclusions, stop rules, archive provenance, executable metrics, fail-closed decisions, and critical-file lock before trajectory generation.

Verification: PR `#9`, merge `d60bb3e618c590e0c994188cebf060bd4b347903`, Actions `30720596773`, 65 tests in each configured Python environment.

## Phase 6A — Pilot-only runner

**PASS at software and runner-contract level.**

The runner now:

- reconstructs exactly 50 pilot configurations and no confirmatory configurations;
- rejects mixed or confirmatory input before integration;
- independently rejects confirmatory input in RK4, DOP853, and archive paths;
- runs all four models at all frozen RK4 resolutions;
- applies DOP853 to every decision-bearing model/map;
- enforces H5, H6, refinement, endpoint, and alternate-integrator gates;
- implements exogenous replay and frozen-$s/q$ controls;
- executes all six relabeling tripwires;
- writes a checksummed, write-once, read-only-finalized archive;
- independently reconstructs membership, hashes, smoke trajectories, and archive checksums;
- requires a separately committed execution authorization naming the verified runner commit.

Hosted verification: PR `#11`, Actions `30722763003`, 100 tests on Python 3.10 and 100 on Python 3.12.

The verification slice contains no execution authorization, pilot trajectory, result, archive, or confirmatory artifact. See `20_phase6_runner_design.md` and `21_phase6_runner_verification.md`.

---

# Phase 6B — Execute the development pilot

## Objective

Execute exactly the 50 frozen pilot configurations with the already verified runner, preserving the protocol and all failures.

## Preconditions

- commit the fixed execution authorization naming the verified Phase 6A runner commit;
- change no protected model, protocol, runner, metric, threshold, configuration, or split file;
- rerun hosted verification;
- create a new empty archive destination;
- retain confirmatory lockout.

## Execution obligations

- run all canonical models, numerical profiles, controls, and relabeling tripwires;
- stop on lock, split, H5, H6, parity, or permutation failure;
- pause if more than 10% of pilot configurations fail numerical acceptance;
- preserve all failures without imputation;
- hash and retain every raw and summary artifact;
- report developmental observations without changing the held-out protocol.

## Maximum result

The pilot may expose numerical defects, degeneracies, uninformative observables, or developmental mechanism signatures. It cannot establish a confirmatory mechanism result, physical adequacy, causal autonomy, strong emergence, novelty, or ontology.

# Phase 7 — Confirmatory four-model experiment

Blocked. Only a separately authorized held-out execution may support scoped comparative claims.

# Phase 8 — Relational projection v2

A constraint involving mismatch, $s$, $q$, intrinsic distance, or compatibility requires a new versioned model contract.

# Phase 9 — Physical anchors

Initial order:

1. constrained mechanics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

## Immediate next action

Create the separate Phase 6B execution authorization without changing protected runner or protocol files, rerun verification, and then execute only the frozen pilot set.
