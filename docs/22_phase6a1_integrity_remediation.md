# Phase 6A.1 Integrity Remediation

## Status

**STOP-SHIP remains active. Pilot authorization and execution are blocked.**

The code-level remediation and clean-extraction bundle machinery are implemented on the remediation branch. Internal and hosted checks are necessary but not sufficient. This gate remains open until the final branch artifact passes an external Auditor AI review with no STOP-SHIP finding.

Narrative rebuttal does not close a finding.

## Binding rules

- No pilot or confirmatory trajectories may be generated.
- No expected scientific outputs may be encoded in production or test logic.
- No oracle, golden trajectory, hidden fixture, test-mode branch, environment bypass, or post-hoc threshold change is permitted.
- Tests target invariants, independently written equations, generated-state differential comparisons, metamorphic properties, failure behavior, and provenance integrity.
- Failed runs remain failures; no imputation or silent repair.
- No remediation is considered externally cleared merely because its internal tests pass.

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
- the environment policy remains `FROZEN_NO_EXECUTION` pending external audit;
- an integrity baseline freezes canonical equations, remediated execution code, protocol lock, environment policy, independent references, adversarial tests, CI workflow, build metadata, and audit-bundle builder;
- the canonical four-model equation file must remain byte-identical to the Phase 4 model commit.

### Independent and adversarial checks

- 300 generated moderate states are evaluated across all four models;
- production derivatives and RK4 steps are compared against a separately written reference implementation;
- no stored expected scientific trajectory is used;
- immutability, finite extremes, strict JSON, lock escape, environment spoofing, incomplete attestation, atomic failure cleanup, output completion, archive identity, and confirmatory contamination are tested directly.

### Delivered-artifact remediation

- the legacy Euler `run.csv` is explicitly rejected as current evidence;
- the audit-bundle builder accepts only a clean Git checkout;
- execution authorization, pilot artifacts, confirmatory artifacts, and unclassified `run.csv` files are forbidden;
- source is exported from Git and full history is included as a Git bundle;
- a fresh clone reruns the complete test suite and data-free pilot validation/plan;
- the wheel is rebuilt after those checks;
- the audit manifest is created only after successful assembly;
- the final archive is re-extracted, all hashes are verified, the repository is recloned from the included history, and the tests are rerun before atomic publication.

## Remediation register

| Finding | Branch status | External closure requirement |
|---|---|---|
| Delivered lock omitted a required file | Remediated by complete self-validating bundle assembly | External extraction must reproduce every locked file and advertised test result. |
| Bundled `run.csv` used obsolete Euler integration | Rejected and quarantined by policy | External audit must confirm no stale or unclassified output is included. |
| Source provenance caller-controlled | Patched and adversarially tested | External review of attestation and execution-identity binding. |
| Extreme finite geometry breaks positivity/finite invariants | Patched and adversarially tested | External finite-domain and nominal-regression verification. |
| `State` arrays mutable through aliasing/write access | Patched and adversarially tested | External alias/write mutation verification. |
| Failed simulator leaves plausible partial output | Patched and adversarially tested | External fault-injection and artifact-cleanup verification. |
| Lock paths can escape repository root | Patched and adversarially tested | External traversal and symlink testing. |
| JSON accepts NaN/Infinity | Patched and adversarially tested | External malformed-JSON testing. |
| Exact execution environment not locked | Frozen and fingerprinted; still no execution clearance | External review of version and installed-byte attestation. |
| Predictable split chronology unavailable in old bundle | Full Git history included; no pilot trajectory exists | External chronology review must confirm split preceded all pilot output. |

## Current hosted state

The remediation suite has passed in exact compatibility environments during development, and the clean-extraction audit builder has completed successfully on a pre-final branch commit. Because documentation and integrity-baseline alignment continued afterward, only the latest final-branch run may be cited as the external-audit candidate.

No execution authorization, pilot trajectory, pilot result, confirmatory trajectory, or scientific observation has been generated.

## Exit gate

This phase passes only when:

1. the final branch state passes all pre-existing and audit-derived adversarial tests;
2. exact Python 3.10 and Python 3.12 hosted compatibility checks pass;
3. the final clean-extraction audit bundle validates itself and is published for review;
4. the final bundle contains no execution authorization or trajectory data;
5. an external Auditor AI reviews that exact artifact and reports no remaining STOP-SHIP finding;
6. any external findings are remediated through another reviewed baseline, not explained away;
7. the claim ledger and roadmap are aligned fail closed.

Until then:

\[
\boxed{
\text{Phase 6A.1 STOP-SHIP};\quad
\text{pilot execution blocked};\quad
\text{scientific claims unchanged}.
}
\]
