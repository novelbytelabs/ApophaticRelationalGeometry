# Phase 6B Claim-Ledger Addendum

## Authority and preservation rule

This file is the controlling claim-status addendum after the Phase 6A.2 external conditional audit and its surgical remediation. `08_claim_ledger.md` remains the immutable historical ledger through the STOP-SHIP remediation period. This addendum supersedes only its time-dependent execution and audit statuses; it does not erase or rewrite the historical findings.

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
\text{Phase 6A.2 conditional findings remediated};
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
| ARG-C064 — self-validating clean-extraction bundle | Verified for the audited Phase 6A.2 packet | Candidate `17a17398808cae1befe85e795d371012fe999f03`; packet SHA-256 `5d524253f24f31893ce44e1be4a0de1fa3ab9ae2f87812ee2d35416ac5ca84fd`; external verdict remained conditional. |
| ARG-C065 — Phase 6A.1 authorizes pilot execution | Rejected and still rejected | The conditional audit did not itself authorize execution. `EXECUTION_AUTHORIZATION.json` remains absent until the remediated final tree and exact scope are frozen. |

## New Phase 6B claims

| ID | Claim | Status | Evidence required | Current scope |
|---|---|---|---|---|
| ARG-C066 | Phase 6A.2 received unconditional external clearance. | Rejected | The report explicitly assigns 85/100 and a conditional pass. | Numerical core strong; five guardrails required remediation. |
| ARG-C067 | External clearance itself constitutes pilot authorization. | Rejected | A separate tracked authorization must bind the accepted external report, packet, tripwire, runner source, frozen scope, and archive destination. | Pilot not executed. |
| ARG-C068 | Phase 6B.0 changes a scientific equation, model parameter, initial condition, split, metric, threshold, exclusion, or decision rule. | Rejected | Diff and integrity-baseline verification. | Clearance-policy and documentation slice only. |
| ARG-C069 | The Phase 6B remediated candidate closes the report's five demonstrated guardrail failures. | Locally verified; hosted verification required before merge | Exact supplied tripwire: 19 PASS / 0 FAIL / 0 INCONCLUSIVE, plus compatibility suites and full-horizon gate. | Software and numerical-integrity verification only. |
| ARG-C070 | Phase 6B.0 produced scientific evidence for or against ARG. | Rejected | No execution authorization, pilot archive, trajectory, or result exists. | No scientific result. |

## Phase 6B.0 verification record

Core clearance-policy candidate verified before this append-only claim-control addendum:

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

That workflow artifact is verification material, not an execution authorization or scientific result. Subsequent claim-control-only commits remain subject to the permanent repository workflows and do not change protected equations or runner logic.

## Authorization boundary

The exact external report and tripwire SHA-256 values are now recorded. Authorization remains prohibited until the remediated runner is merged and a single authorization-only commit binds that exact final tree, frozen scope, and new archive destination.

Confirmatory access remains blocked at every runner boundary.

## Claim-promotion rule

No Phase 6B claim may become **numerically supported** until an authorized pilot actually executes and its immutable archive passes the frozen decision and contamination gates. A pilot observation cannot become a confirmatory claim without separately authorized held-out execution.
