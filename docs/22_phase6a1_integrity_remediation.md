# Phase 6A.1 Integrity Remediation

## Status

**CLOSED WITH CONDITIONAL-AUDIT FOLLOW-UP:** The external report scored Phase 6A.2 85/100 with a conditional pass. Its five demonstrated guardrail failures have now been remediated and pass the supplied external tripwire. Pilot execution remains unexecuted and requires a separate hash-bound authorization record.

The remediation and defensive-hardening candidate passed the ordinary suite and full-horizon gate. The external report then identified five narrow guardrail failures; the follow-up remediation passes the exact supplied tripwire at 19 PASS / 0 FAIL / 0 INCONCLUSIVE. Candidate `17a17398808cae1befe85e795d371012fe999f03` merged as `4fb987b34220927466812f0276e10bb0776c28fd`.

## Binding rules

- No pilot or confirmatory trajectories may be generated during remediation.
- No expected scientific outputs may be encoded in production or test logic.
- No oracle, golden trajectory, hidden fixture, test-mode branch, environment bypass, or post-hoc threshold change is permitted.
- Tests target invariants, independently written equations, generated-state differential comparisons, metamorphic properties, failure behavior, and provenance integrity.
- Failed runs remain failures; no imputation or silent repair.
- Internal tests alone never constituted external clearance.

## Current-repository reproduction

The following defects were reproduced on pre-remediation `main`:

- `State` retained caller array aliases and exposed writable arrays;
- finite extreme `q` values could produce zero or infinite conductances and lengths;
- `load_json()` accepted non-standard `NaN` and infinity constants;
- `verify_lock()` joined untrusted paths without root-containment checks;
- the standalone simulator accepted `ARG_SOURCE_COMMIT` as provenance;
- the standalone simulator wrote directly to the final CSV path and had no completion attestation;
- standalone run identity did not bind source-tree, protocol-lock, integrator, or runtime fingerprints.

The delivered-bundle lock omission and stale Euler `run.csv` were also accepted as genuine historical packaging/evidence defects.

## Implemented remediation

### State and numerical domain

- arrays are copied at `State` construction and marked read-only;
- finite exponential underflow, overflow, zero, and nonfinite values fail closed;
- conductances and intrinsic lengths must remain finite and strictly positive;
- intrinsic distance and derivative arithmetic fail closed outside the executable FP64 domain;
- adversarial tests exercise extreme finite $s$ and $q$ values.

### Protocol and lock integrity

- strict JSON rejects `NaN`, `Infinity`, and `-Infinity`;
- lock targets must be relative, root-contained regular files;
- traversal, absolute-path, and symlink-escape cases are adversarially tested;
- `ARG-P5-LOCK-v1.1-INTEGRITY` records that no parameter, initial condition, split, metric, threshold, decision rule, or trajectory status changed.

### Provenance and output integrity

- source commit is derived from a clean Git checkout rather than an environment variable;
- tracked source bytes, protocol lock, implementation files, Python executable, installed distributions, NumPy/BLAS configuration, integrator, and environment are fingerprinted;
- scientific configuration hash is separated from source-bound execution identity;
- standalone output is written to temporary files, flushed, row-count checked, checksummed, and atomically published with a separate `COMPLETE` manifest;
- any failed standalone run removes temporary and final artifacts;
- pilot run identity binds authorization, attestation, environment policy, all configuration hashes, and the integrator suite;
- archive configuration, raw data, summaries, failures, and final completion marker all carry the run identity.

### Environment and post-authorization integrity

- intended Phase 6B execution is frozen to CPython 3.12.13, NumPy 2.5.1, SciPy 1.18.0, and ARG 0.6.0;
- installed-byte and interpreter fingerprints are recorded at execution;
- external clearance now applies to the frozen execution substrate only;
- pilot execution still requires a separately committed authorization binding the accepted external audit-report SHA-256, exact runner source, scope, and archive destination;
- the integrity baseline freezes canonical equations, authorized projector roundoff remediation, execution code, protocol lock, environment policy, independent references, adversarial tests, CI workflow, build metadata, and audit tooling;
- AST-based comparison rejects equation-source changes outside the explicitly authorized `project_node_derivative` roundoff cleanup, and the projector tolerance remains unchanged.

### Independent and adversarial checks

- 300 generated moderate states are evaluated across all four models;
- production derivatives and RK4 steps are compared against a separately written reference implementation;
- no stored expected scientific trajectory is used;
- immutability, finite extremes, strict JSON, lock escape, environment spoofing, incomplete attestation, atomic failure cleanup, output completion, archive identity, and confirmatory contamination are tested directly.

### Delivered-artifact remediation

- the legacy Euler `run.csv` is explicitly rejected as current evidence;
- the audit-bundle builder accepts only a clean Git checkout;
- execution authorization, pilot artifacts, confirmatory artifacts, and unclassified `run.csv` files are forbidden from remediation bundles;
- source is exported from Git and full history is included as a Git bundle;
- a fresh clone reruns the complete test suite and data-free pilot validation/plan;
- the wheel is rebuilt after those checks;
- the audit manifest is created only after successful assembly;
- the final archive is re-extracted, all hashes are verified, the repository is recloned from the included history, and the tests are rerun before atomic publication.

## Remediation register

| Finding | Final status | Closure evidence |
|---|---|---|
| Delivered lock omitted a required file | Closed | Complete self-validating bundle and external re-audit. |
| Bundled `run.csv` used obsolete Euler integration | Closed | Rejected and quarantined by policy; absent from accepted evidence. |
| Source provenance caller-controlled | Closed | Git-derived attestation and adversarial verification. |
| Extreme finite geometry breaks positivity/finite invariants | Closed | Fail-closed finite-domain checks and external review. |
| `State` arrays mutable through aliasing/write access | Closed | Copied read-only arrays and mutation tests. |
| Failed simulator leaves plausible partial output | Closed | Atomic publication, cleanup, and fault-injection tests. |
| Lock paths can escape repository root | Closed | Root confinement plus traversal and symlink tests. |
| JSON accepts NaN/Infinity | Closed | Strict JSON parser and malformed-input tests. |
| Exact execution environment not locked | Closed for substrate; authorization still separate | Frozen versions, execution-time fingerprints, and external clearance. |
| Predictable split chronology unavailable in old bundle | Closed | Full Git history and confirmation that no pilot trajectory predated the split. |
| Full-horizon projected tangency exceeded the frozen tolerance by 1.7% | Closed | Compensated three-term dot products and residual radial cleanup; same equation and tolerance; permanent full-horizon workflow passed. |

## Final verification record

- exact candidate: `17a17398808cae1befe85e795d371012fe999f03`;
- accepted packet SHA-256: `5d524253f24f31893ce44e1be4a0de1fa3ab9ae2f87812ee2d35416ac5ca84fd`;
- ordinary suite: **PASS**;
- hardened tripwire: **PASS**;
- full-horizon numerical gate: **PASS**;
- external report: **85/100 CONDITIONAL PASS**; supplied post-remediation tripwire: **19/0/0**;
- merge commit: `4fb987b34220927466812f0276e10bb0776c28fd`;
- execution authorization: absent;
- pilot trajectory data: absent;
- confirmatory execution: blocked.

## Closure boundary

Phase 6A.1/6A.2 plus the Phase 6B audit-closure patch establishes a strongly defended computational runner substrate suitable for an authorized exploratory pilot, not formal certification. It does not establish a pilot result, scientific mechanism effect, physical adequacy, novelty, or ontology.

The next gate is `23_phase6b_clearance_and_authorization.md`.
