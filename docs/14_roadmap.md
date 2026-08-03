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
\text{Phase 6A.1 integrity remediation STOP-SHIP};
\quad
\text{development pilot not authorized for execution};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

## Current position

| Track or phase | Status | Result |
|---|---|---|
| Phase 0 — Alignment and claim control | COMPLETE | Public and internal descriptions aligned. |
| Phase 1 — Four-model design contract | COMPLETE | Contract v1.0 frozen. |
| Phase 2 — Implement and verify $M_0$ | COMPLETE | No-feedback baseline merged and independently parity-tested. |
| Phase 3 — Implement and verify $M_P$ | COMPLETE | Projection sandbox merged and hosted-tested. |
| Phase 4 — Implement and verify $M_{FP}$ | COMPLETE | Combined model merged; 51 tests passed in each configured Python environment. |
| Phase 5 — Freeze comparative experiment protocol | COMPLETE | Data-free protocol and executable decision rules frozen; 65 tests passed in each configured environment. |
| Phase 6A — Implement pilot-only runner | COMPLETE WITH AUDIT REMEDIATION REQUIRED | Runner gate passed, but an independent audit found integrity defects outside and around the nominal equations. |
| Phase 6A.1 — Integrity remediation | STOP-SHIP / ACTIVE | Provenance, numerical-domain, immutability, atomic-output, lock-containment, strict-JSON, environment-lock, and bundle-assembly defects must be closed and externally re-audited. |
| Phase 6B — Execute development pilot | BLOCKED | No execution authorization may be created until Phase 6A.1 passes external audit and the consensus track confirms scientific necessity. |
| Phase 7 onward | BLOCKED | Confirmatory execution remains unauthorized. |
| CS0 — Consensus governance | DRAFT COMPLETE / REVIEW | Consensus method, workspace, source template, grades, and stop rules added on PR #29. |
| CS1 — State, structure, representation, persistence | ACTIVE | Three source baskets entered: initial-value/equivalence, nonlinear persistence, and control theory. |

Software tests verify declared code and protocol contracts. They do not validate the scientific hypothesis, and they do not supersede an unresolved independent audit or a no-novelty consensus result.

---

# Completed software gates

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

Verification: PR `#7`, merge `205fb8c5bf1b832e241af230612e3d7056be05f5`, Actions `30718821666`, 51 tests in each configured environment.

## Phase 5 — Frozen comparative protocol

Protocol `ARG-P5-COMP-v1` froze the primary and secondary hypotheses, observation maps, thresholds, direction-level units, deterministic pilot/confirmatory split, parameters, numerical replication, exclusions, stop rules, archive provenance, executable metrics, fail-closed decisions, and critical-file lock before trajectory generation.

Verification: PR `#9`, merge `d60bb3e618c590e0c994188cebf060bd4b347903`, Actions `30720596773`, 65 tests in each configured environment.

## Phase 6A — Pilot-only runner

The runner implementation and its original software gate passed, but that result is now subordinate to the independent audit and does not authorize execution.

Original verification: PR `#11`, merge `b0b5acc1f2db77b7b0fab43eefafd15f3ee2f728`, 100 tests in each configured environment.

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

Blocked until both conditions hold:

1. Phase 6A.1 is externally cleared;
2. CS1 and the applicable later consensus slices establish a precise unresolved scientific residual that the frozen pilot actually discriminates.

A prior execution issue or authorization template does not override either block.

# Phase 7 — Confirmatory four-model experiment

Blocked. Only a separately authorized held-out execution may support scoped comparative claims, and only if a literature-grounded residual remains.

# Phase 8 — Relational projection v2

A constraint involving mismatch, $s$, $q$, intrinsic distance, or compatibility requires a new versioned model contract and must survive the consensus audit.

# Phase 9 — Physical anchors

Initial order:

1. constrained mechanics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

---

# Consensus synthesis track

## CS0 — Governance

Draft governance and workspace are present on PR `#29`. The program requires research before synthesis, synthesis before formalization, and experiments only on the unresolved remainder.

## CS1 — State, structure, representation, and persistence

### Basket 1 — entered

- nonmodal initial-value dynamics;
- adaptive networks;
- evolving state spaces and transport;
- theoretical equivalence.

### Basket 2 — entered

- basin stability;
- invariant-manifold persistence;
- metastability and almost-invariant sets;
- structural stability.

### Basket 3 — entered

- linear controllability and observability;
- minimal realization;
- balanced realization and model reduction;
- nonlinear accessibility and observability;
- viability kernels;
- positive and controlled invariance.

### Current provisional correction

The evidence supports a typed family of relations rather than one universal compatibility or persistence scalar.

Many scientific questions require a context broader than

$$
Q_t=(B_t,x_t).
$$

A preliminary typed context is

$$
\mathcal S=
(\mathcal X,F,B_{\mathrm{in}},C_{\mathrm{out}},K,\mathcal U,\mathcal W,\Phi,T).
$$

This is a methodological correction, not an ontological promotion.

### Remaining CS1 gates

- transport and structural-change basket;
- gauge, quotient, and representation audit;
- information and recoverability basket;
- biological persistence basket;
- philosophical identity and persistence basket;
- disagreement map;
- residual research agenda;
- formalism impact note;
- claim-ledger and novelty-matrix amendments;
- independent review.

## Immediate next action

Proceed with the CS1 transport-and-structural-change basket:

1. connections and parallel transport;
2. hybrid reset maps and reset relations;
3. remeshing and conservative projection;
4. graph correspondence and optimal transport;
5. dimension-changing and noninvertible transitions.

Do not execute the pilot or revise the ontology before this basket and the associated representation audit are complete.
