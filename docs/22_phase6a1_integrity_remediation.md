# Phase 6A.1 Integrity Remediation

## Status

**STOP-SHIP. Pilot authorization and execution are blocked.**

This gate responds to the independent audit of the delivered ARG bundle. Findings are resolved only by current-repository reproduction, surgical remediation, adversarial regression tests, hosted verification, and a fresh external audit. Narrative rebuttal does not close a finding.

## Binding rules

- No pilot or confirmatory trajectories may be generated.
- No expected scientific outputs may be encoded in production or test logic.
- No oracle, golden trajectory, hidden fixture, test-mode branch, environment bypass, or post-hoc threshold change is permitted.
- Tests must target invariants, independent references, metamorphic properties, failure behavior, and provenance integrity.
- Failed runs must remain failures; no imputation or silent repair.
- Every audit finding remains open until a direct adversarial test passes.

## Current-repository reproduction

The following defects were reproduced on current `main` before remediation:

- `State` retained caller array aliases and exposed writable arrays;
- finite extreme `q` values could produce zero or infinite conductances and lengths;
- `load_json()` accepted non-standard `NaN` and infinity constants;
- `verify_lock()` joined untrusted paths without root-containment checks;
- the standalone simulator accepted `ARG_SOURCE_COMMIT` as provenance;
- the standalone simulator wrote directly to the final CSV path and had no completion attestation;
- standalone run identity did not bind source-tree, protocol-lock, integrator, or runtime fingerprints.

The delivered-bundle lock omission and stale Euler `run.csv` are historical packaging and evidence defects. They require a fresh self-validating bundle and explicit rejection of the stale output; source patches alone cannot close them.

## Remediation register

| Finding | Current disposition | Required closure evidence |
|---|---|---|
| Delivered lock omitted a required file | Historical bundle defect; OPEN | clean extracted bundle, complete lock, advertised test command passes after final assembly |
| Bundled `run.csv` used obsolete Euler integration | Rejected as current evidence; OPEN packaging action | remove or quarantine legacy output; current artifacts declare and attest integrator |
| Source provenance caller-controlled | PATCH IN PROGRESS | source commit derived from Git; source tree, runner, protocol lock, environment, and configuration bound into execution identity |
| Extreme finite geometry breaks positivity/finite invariants | PATCH IN PROGRESS | fail-closed exponential-domain checks and adversarial finite-extreme tests |
| `State` arrays mutable through aliasing/write access | PATCH IN PROGRESS | copied, read-only arrays and mutation tests |
| Failed simulator leaves plausible partial output | PATCH IN PROGRESS | atomic temporary write, completion record, checksum, and failure cleanup tests |
| Lock paths can escape repository root | PATCH IN PROGRESS | resolved containment checks and traversal/symlink adversarial tests |
| JSON accepts NaN/Infinity | PATCH IN PROGRESS | strict parser and malformed-constant tests |
| Exact execution environment not locked | OPEN | versioned execution policy plus archived installed-byte fingerprints |
| Predictable split chronology unavailable in old bundle | OPEN provenance concern | preserve Git chronology and external audit record; no split changes after pilot effects |

## Exit gate

This phase passes only when:

1. all current defects above are patched;
2. adversarial tests fail against the old behavior and pass against the remediation;
3. all pre-existing tests remain passing;
4. hosted Python 3.10 and 3.12 verification passes under the declared environment policy;
5. no execution authorization or pilot data is present;
6. a fresh audit package is assembled only after final tests and validates itself from a clean extraction;
7. an external Auditor AI reviews the remediated artifact and no STOP-SHIP finding remains.

Until then:

\[
\boxed{
\text{Phase 6A.1 STOP-SHIP};\quad
\text{pilot execution blocked};\quad
\text{scientific claims unchanged}.
}
\]
