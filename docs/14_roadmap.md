# ARG Roadmap

## Operating rule

ARG advances by passed gates, not by calendar optimism. A phase is complete only when its exit criteria pass and the claim ledger is aligned.

The governing research order is:

$$
\boxed{
\text{research first}
\;\longrightarrow\;
\text{synthesize second}
\;\longrightarrow\;
\text{formalize third}
\;\longrightarrow\;
\text{experiment only on the unresolved remainder}.
}
$$

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
\text{Phase 6A.1 integrity remediation STOP-SHIP};
\quad
\text{development pilot not authorized for execution};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

The consensus-synthesis track does not change this execution state.

## Current position

### Four-model implementation and experiment track

| Phase | Status | Result |
|---|---|---|
| Phase 0 — Alignment and claim control | COMPLETE | Public and internal descriptions aligned. |
| Phase 1 — Four-model design contract | COMPLETE | Contract v1.0 frozen. |
| Phase 2 — Implement and verify $M_0$ | COMPLETE | No-feedback baseline merged and independently parity-tested. |
| Phase 3 — Implement and verify $M_P$ | COMPLETE | Projection sandbox merged and hosted-tested. |
| Phase 4 — Implement and verify $M_{FP}$ | COMPLETE | Combined model merged; 51 tests passed in each configured Python environment. |
| Phase 5 — Freeze comparative experiment protocol | COMPLETE | Data-free protocol and executable decision rules frozen; 65 tests passed in each configured environment. |
| Phase 6A — Implement pilot-only runner | COMPLETE WITH AUDIT REMEDIATION REQUIRED | Runner gate passed, but an independent audit found integrity defects outside and around the nominal equations. |
| Phase 6A.1 — Integrity remediation | STOP-SHIP / ACTIVE | Provenance, numerical-domain, immutability, atomic-output, lock-containment, strict-JSON, environment-lock, and bundle-assembly defects must be closed and externally re-audited. |
| Phase 6B — Execute development pilot | BLOCKED | No execution authorization may be created until Phase 6A.1 passes external audit. |
| Phase 7 onward | BLOCKED | Confirmatory execution remains unauthorized. |

Software tests verify declared code and protocol contracts. They do not validate the scientific hypothesis, and they do not supersede an unresolved independent audit.

### Consensus synthesis track

| Phase | Status | Result or required output |
|---|---|---|
| CS0 — Governance and schemas | REVIEW PENDING | Consensus method, evidence grades, integration rules, workspace, and source-note schema added on an isolated branch. |
| CS1 — State, structure, representation, and persistence | ACTIVE / LITERATURE AUDIT ONLY | Determine the established mathematical, scientific, and philosophical core before revising formalism or proposing experiments. |
| CS2 — Change, transport, and identity | BLOCKED BY CS1 | Separate standard transport machinery from identity criteria and unresolved representation choices. |
| CS3 — Constraint and causation | BLOCKED | Separate dynamical constraint, intervention, counterfactual, and causal interpretation. |
| CS4 — Parts, wholes, and emergence | BLOCKED | Synthesize composition, closure, multiscale organization, and emergence without forcing one interpretation. |
| CS5 — Scale and effective description | BLOCKED | Audit coarse-graining, model reduction, renormalization, and higher-level autonomy. |
| CS6 — Space, time, and geometry | BLOCKED | Separate mathematical structures, physical evidence, and metaphysical readings. |
| CS7 — Information and measurement | BLOCKED | Disambiguate physical, statistical, computational, semantic, and epistemic information. |
| CS8 — Perspective and observer | BLOCKED | Distinguish reference-frame, gauge, model, and measurement dependence from subjectivism. |
| CS9 — Minimal ARG Core | BLOCKED | Publish only C3–C4 bridge propositions that survive all completed audits. |
| CS10 — Formal revision | BLOCKED | Align notation, papers, claim ledger, novelty matrix, and public language with the consensus core. |

The consensus track is governed by `docs/22_consensus_synthesis_program.md`. Its working material lives under `research/consensus/`.

---

# Consensus synthesis gates

## Objective

Determine what ARG can responsibly synthesize from established cross-disciplinary results before treating familiar principles as discoveries or spending compute on questions already answered by consensus.

## Required artifacts

- Consensus Atlas;
- Concept Translation Dictionary;
- Minimal ARG Core;
- Disagreement and Boundary Map;
- Residual Research Agenda.

## Core operating constraints

- organize research around phenomena, not disciplinary silos;
- decompose prose into atomic claims;
- classify each claim by type and consensus grade;
- map claims into established field terminology before assessing novelty;
- distinguish identity, translation, specialization, approximation, analogy, and loose resemblance;
- preserve interpretive disagreement where shared evidence does not select one ontology;
- test representation robustness before calling a relation invariant;
- import established results rather than recreating them;
- propose experiments only for a precise unresolved residual;
- treat a no-novelty result as a successful research outcome.

## CS1 exit criteria

CS1 passes only when:

- every load-bearing state–structure and persistence claim has traceable source notes;
- consensus statements are graded and scoped;
- state, structure, rule, parameter, environment, compatibility, transport, and persistence have cross-field dictionary entries;
- representation-dependent claims are labeled as such;
- accepted evidence is separated from philosophical interpretation;
- the novelty matrix records direct equation or concept comparisons;
- the claim ledger is narrowed, promoted, rejected, or quarantined as required;
- any proposed experiment addresses a demonstrably unresolved remainder.

CS1 may conclude that the general state–structure principle is standard and that ARG's contribution is synthesis, application, or nothing further. That is an acceptable result.

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

The runner implementation and its original software gate passed, but that result is now subordinate to the independent audit and does not authorize execution.

Original verification: PR `#11`, merge `b0b5acc1f2db77b7b0fab43eefafd15f3ee2f728`, 100 tests in each configured Python environment.

---

# Phase 6A.1 — Integrity remediation

## Objective

Remediate the audit findings without changing scientific equations, thresholds, configurations, pilot/confirmatory membership, or outcome rules.

## Mandatory remediation

- make `State` arrays copied and read-only;
- fail closed on exponential underflow, overflow, zero, or nonfinite geometry values;
- reject lock traversal and symlink escape outside repository root;
- reject non-standard JSON constants including NaN and Infinity;
- remove environment-controlled source provenance and bind run identity to attested source, protocol, runner, integrator, dependency, and environment fingerprints;
- make standalone simulator output atomic and completion-attested;
- pin and fingerprint the execution environment;
- assemble future audit bundles only after clean extraction, lock verification, and advertised-test success;
- quarantine or remove stale Euler output from current evidence;
- add adversarial tests derived from the independent audit, without using expected scientific trajectories as oracles.

## Exit criteria

- all audit-derived adversarial tests pass;
- all pre-existing tests remain passing;
- no pilot or confirmatory data is generated;
- a fresh audit package validates its own lock and test attestation from a clean extraction;
- an external Auditor AI reports no remaining STOP-SHIP finding.

# Phase 6B — Execute the development pilot

Blocked until Phase 6A.1 is externally cleared. A prior execution issue or authorization template does not override this block.

The consensus track may independently narrow or eliminate the scientific motivation for execution. Clearing software integrity is necessary but not sufficient to justify a pilot.

# Phase 7 — Confirmatory four-model experiment

Blocked. Only a separately authorized held-out execution may support scoped comparative claims.

# Phase 8 — Relational projection v2

A constraint involving mismatch, $s$, $q$, intrinsic distance, or compatibility requires a new versioned model contract.

No v2 contract should be drafted until the applicable consensus and novelty audits identify a precise unresolved contribution.

# Phase 9 — Physical anchors

Initial order:

1. constrained mechanics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

## Immediate next actions

Two independent tracks may proceed without weakening either gate:

1. **Integrity track:** complete Phase 6A.1 remediation on its isolated branch, run hosted adversarial verification, assemble a fresh self-validating audit bundle, and submit it to an external Auditor AI. Do not create execution authorization or run the pilot.
2. **Consensus track:** execute CS1 as a primary-source literature and translation audit. Populate source notes, consensus grades, dictionary entries, disagreement boundaries, and the residual agenda before revising ARG's formal ontology or proposing a new persistence experiment.

No development-pilot or confirmatory execution is authorized by this roadmap revision.
