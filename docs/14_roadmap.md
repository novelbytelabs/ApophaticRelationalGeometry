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
\text{Phase 6B.1 pilot attempt stopped fail closed};
\quad
\text{Phase 6B.2 H6 conditioning remediation active};
\quad
\text{no completed pilot result};
\quad
\text{confirmatory execution blocked}.
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
| Phase 6A — Implement pilot-only runner | COMPLETE | Runner and archive machinery implemented. |
| Phase 6A.1/6A.2 — Integrity remediation and defensive hardening | COMPLETE / CONDITIONAL PASS | External report: 85/100 conditional pass; numerical core strong, five guardrail failures identified. |
| Phase 6B.0 — Conditional-audit closure and authorization freeze | COMPLETE | Five demonstrated guardrail failures remediated; supplied tripwire 19/0/0; exact authorization boundary frozen. |
| Phase 6B.1 — Execute development pilot | STOPPED / NO RESULT | Authorized run `30763372785` stopped after six H6 validity failures exceeded the frozen 10% pause rule. Partial archive preserved; no summaries or completion marker. |
| Phase 6B.2 — H6 conditioning diagnosis and remediation | ACTIVE | Exact identity intact to machine precision; legacy forward-relative metric ill-conditioned near projected equilibrium. Runner v1.1.0 validity-gate revision under audit. |
| Phase 7 onward | BLOCKED | Confirmatory execution remains unauthorized. |

Software tests verify declared code and protocol contracts. They do not validate the scientific hypothesis, and they do not supersede an unresolved independent audit.

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

# Phase 6A.1/6A.2 — Integrity remediation and defensive hardening

## Result

The external report assigned an 85/100 conditional pass and identified five narrow guardrail failures rather than pervasive mathematical defects. Those failures were remediated without changing scientific equations, thresholds, configurations, pilot/confirmatory membership, or outcome rules. The exact supplied tripwire now reports 19 PASS / 0 FAIL / 0 INCONCLUSIVE.

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
- the supplied external tripwire reports no failed or inconclusive integrity property.

# Phase 6B.0 — Clearance integration and authorization freeze

Complete. The report, tripwire, runner tree, frozen scope, and archive destination were bound in one authorization-only commit.

# Phase 6B.1 — First development-pilot attempt

Stopped fail closed. Run `30763372785` created a partial failure archive and no summaries. Six H6 failures exceeded the frozen 10% pause rule. The authorization is consumed and cannot be reused.

# Phase 6B.2 — H6 conditioning diagnosis and remediation

Active. Blinded analysis shows the exact same-state node identity is preserved to binary64 precision, while the legacy forward-relative ratio becomes singular as both projected derivatives approach zero. The remediation keeps the existing `1e-12` forward-relative gate in well-conditioned states and adds a machine-precision backward-error gate only in cancellation-dominated states. Genuine non-radial perturbations must still fail.

Exit requires all 50 frozen pilot MP trajectories to pass the data-blind H6 diagnostic, adversarial mismatch tests, ordinary suites, hardened tripwire, full-horizon verification, and external audit. No primary hypothesis effect may be inspected during this slice.

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

Complete Phase 6B.2 verification and external audit on runner v1.1.0. Preserve the failed run unchanged, inspect no primary effect, and do not reauthorize until the condition-aware H6 gate and all-50 blinded diagnostic are independently cleared.
