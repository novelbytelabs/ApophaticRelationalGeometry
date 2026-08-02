# Phase 6B Claim-Ledger Addendum

## Authority and preservation rule

This file is the controlling claim-status addendum after the Phase 6A.2 external re-audit. `08_claim_ledger.md` remains the immutable historical ledger through the STOP-SHIP remediation period. This addendum supersedes only its time-dependent execution and audit statuses; it does not erase or rewrite the historical findings.

All model, equation, protocol, and scientific claim ceilings in the historical ledger remain binding unless explicitly changed here.

## Current scientific ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

No pilot or confirmatory mechanism result exists.

## Current integrity and execution state

$$
\boxed{
\text{Phase 6A.2 externally cleared};
\quad
\text{Phase 6B.0 authorization preparation verified};
\quad
\text{execution authorization absent};
\quad
\text{pilot not executed};
\quad
\text{confirmatory execution blocked}.
}
$$

## Superseded time-dependent statuses

| Historical claim | Current status | Evidence and boundary |
|---|---|---|
| ARG-C063 — no stored expected scientific trajectory oracle | Externally reviewed and retained | Generated-state differential tests, independent equations, hardened tripwire, and accepted external re-audit. This does not prove the test system infallible. |
| ARG-C064 — self-validating clean-extraction bundle | Externally cleared for the accepted Phase 6A.2 packet | Candidate `17a17398808cae1befe85e795d371012fe999f03`; packet SHA-256 `5d524253f24f31893ce44e1be4a0de1fa3ab9ae2f87812ee2d35416ac5ca84fd`. |
| ARG-C065 — Phase 6A.1 authorizes pilot execution | Rejected and still rejected | External clearance applies to the frozen runner substrate. `EXECUTION_AUTHORIZATION.json` is absent, and the exact accepted audit-report SHA-256 has not been bound. |

## New Phase 6B claims

| ID | Claim | Status | Evidence required | Current scope |
|---|---|---|---|---|
| ARG-C066 | Phase 6A.2 passed external re-audit. | User-confirmed external clearance with fixed repository evidence | Exact candidate, accepted packet digest, remediation history, and merge record. | Runner-integrity clearance only. |
| ARG-C067 | External clearance itself constitutes pilot authorization. | Rejected | A separate tracked authorization must bind the accepted external report, packet, tripwire, runner source, frozen scope, and archive destination. | Pilot not executed. |
| ARG-C068 | Phase 6B.0 changes a scientific equation, model parameter, initial condition, split, metric, threshold, exclusion, or decision rule. | Rejected | Diff and integrity-baseline verification. | Clearance-policy and documentation slice only. |
| ARG-C069 | The Phase 6B.0 candidate passes its declared software gates. | Hosted-verified | Python 3.10 and 3.12 suites, hardened tripwire, clean-extraction bundle build, and full-horizon numerical gate on the exact candidate. | Software and numerical-integrity verification only. |
| ARG-C070 | Phase 6B.0 produced scientific evidence for or against ARG. | Rejected | No execution authorization, pilot archive, trajectory, or result exists. | No scientific result. |

## Phase 6B.0 verification record

Exact candidate head:

```text
d554e057f357f463d48cc43f9f580310cc2eb535
```

Hosted evidence:

- ordinary compatibility suite, Python 3.10.20 / NumPy 2.2.6 / SciPy 1.15.3: **PASS**;
- ordinary compatibility suite, Python 3.12.13 / NumPy 2.5.1 / SciPy 1.18.0: **PASS**;
- hardened tripwire: **PASS**;
- clean-extraction bundle assembly: **PASS**;
- full 10-unit-horizon numerical gate: **PASS**;
- execution authorization: **ABSENT**;
- pilot artifact directory: **ABSENT**.

Relevant workflow runs:

- standard suite and bundle: `30760146292`;
- hardened tripwire CI: `30760212631`;
- permanent full-horizon gate: `30760146160`.

The standard workflow artifact digest was:

```text
sha256:dadeccbc8ee18af8673927d28cec70d918507a1adb8a42d9eb1900a969defe20
```

That workflow artifact is verification material, not an execution authorization or scientific result.

## Authorization boundary

The next authorization commit is prohibited until the exact accepted external audit-report SHA-256 is available. A user statement, packet digest, narrative summary, placeholder digest, or report authored by the implementation agent is not a substitute.

Confirmatory access remains blocked at every runner boundary.

## Claim-promotion rule

No Phase 6B claim may become **numerically supported** until an authorized pilot actually executes and its immutable archive passes the frozen decision and contamination gates. A pilot observation cannot become a confirmatory claim without separately authorized held-out execution.
