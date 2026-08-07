# Canonical Alignment and Claim Ceiling

## Purpose

This document fixes the relationship between the ARG formalism, implemented prototypes, frozen experiment protocol, runner software, independent audit, remediation state, and strongest currently licensed claims. It is binding on documentation, code, experiments, releases, and external descriptions.

## Mechanism distinction

### Collective feedback

A substrate-computed statistic enters constituent transition equations:

$$
x\longrightarrow c(x)\longrightarrow(\dot x,\dot s,\dot q).
$$

This is implemented by $M_F$ and retained within $M_{FP}$.

### Global admissibility projection

A proposed vector field is projected onto the tangent space of an explicit admissible manifold:

$$
\dot Z=\Pi_{T_Z\mathcal M}F(Z).
$$

Contract v1.0 implements

$$
\Gamma(Z)=c(x)-c_0=\frac13x^Tx-c_0=0,
\qquad
P_T=I-\frac{xx^T}{x^Tx}.
$$

This is implemented by $M_P$ and $M_{FP}$.

The mechanisms are not assumed equivalent:

$$
M_F\not\equiv M_P
$$

unless a scoped mathematical or observational equivalence is independently established.

## Canonical model family

| Model | Software status | Licensed description |
|---|---|---|
| $M_0$ | Implemented and unit-tested | Local/adaptive baseline with no collective-statistic transition path and no projection. |
| $M_F$ | Implemented and unit-tested | Endogenous collective-feedback prototype; implemented prototype-level downward feedback/constraint. |
| $M_P$ | Implemented and unit-tested | Constant-amplitude projected-admissibility sandbox with projected RK4, retraction, fail-closed singular handling, and separate diagnostics. |
| $M_{FP}$ | Implemented and unit-tested | Feedback proposal followed by node projection and retraction, with retained $s/q$ feedback and separate mechanism diagnostics. |

For the same regular full state,

$$
\boxed{f_{FP}=f_P}
$$

because the node-feedback term is radial and $P_Tx=0$. This identity is local to the same-state node derivative and does not imply trajectory identity.

## Current scientific claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Binding integrity and execution status

The independent audit found that the delivered bundle could not reproduce its advertised test result, contained obsolete Euler output, and exposed current or historical defects in provenance, state immutability, finite geometry, atomic output, lock containment, strict JSON, and environment locking.

Several defects reproduced against current `main`; therefore previous runner test counts do not authorize execution.

Current binding state:

$$
\boxed{
\text{Phase 6A.1 STOP-SHIP remediation active};
\quad
\text{development pilot not authorized for execution};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

Issue #12, the former Phase 6B authorization path, is closed as superseded. A fresh authorization gate may be created only from an externally cleared remediation commit.

## Passed historical implementation gates

### $M_P$ version 1.0

Explicit equality constraint, projection, constraint-preservation tests, independent code-equation parity, diagnostics, and fail-closed singular handling: **PASS at software/mechanism level**.

$$
\operatorname{MP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

### $M_{FP}$ version 1.0

Feedback proposal, projection ordering, same-state identity, retained $s/q$ feedback, reduction paths, independent parity, and constraint handling: **PASS at software/mechanism level**.

$$
\operatorname{MFP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

### Phase 5 protocol version 1.0

The scientific design—hypotheses, parameters, initial conditions, split, metrics, thresholds, numerical policy, exclusions, stop rules, and decisions—was frozen before trajectory generation. Phase 6A.1 changes only integrity and execution controls; `ARG-P5-LOCK-v1.1-INTEGRITY` records that no scientific design field changed.

$$
\operatorname{PHASE5\_SCIENTIFIC\_DESIGN\_FREEZE}=\text{PASS}.
$$

### Phase 6A runner version 1.0

The original runner implemented exact pilot reconstruction, confirmatory rejection, all-model RK4/DOP853 paths, H5/H6 and numerical gates, frozen controls, all six relabelings, archive construction, and independent software references. That remains a historical software result.

It does not license execution while Phase 6A.1 is STOP-SHIP.

## Phase 6A.1 remediation gate

The remediation branch currently implements:

- copied read-only state arrays;
- fail-closed finite-positive exponential, conductance, length, distance, and derivative domains;
- strict rejection of non-standard JSON constants;
- root-confined regular-file lock targets with traversal and symlink-escape rejection;
- Git-derived source commit and tracked-tree attestation;
- installed-distribution, Python executable, protocol-lock, implementation-file, and runtime fingerprints;
- atomic standalone output, explicit completion manifest, row counts, and output checksum;
- source-bound execution identity distinct from the scientific configuration hash;
- pilot archive run identity bound to authorization, attestation, environment policy, configuration hashes, and integrator suite;
- exact future scientific execution environment, still marked `FROZEN_NO_EXECUTION`;
- an integrity baseline over canonical equations, remediated code, independent references, adversarial tests, CI workflow, build metadata, and audit-bundle builder;
- 300 generated-state all-model derivative and RK4 comparisons against a separately written reference path;
- a clean-extraction audit-bundle builder that reruns tests, reconstructs the data-free pilot plan, rebuilds the wheel, verifies all file hashes, and republishes nothing until final re-extraction passes.

Internal and hosted checks do not close this gate by themselves.

### Mandatory remaining gate

$$
\boxed{
\operatorname{PHASE6A1\_CLEARANCE}
=
\text{hosted checks}
\land
\text{self-validating final bundle}
\land
\text{external Auditor AI clearance}.
}
$$

Until all terms pass:

$$
\operatorname{PHASE6A1\_CLEARANCE}=\text{BLOCKED}.
$$

## Comparative scientific claim

No trajectory experiment has run. Therefore:

$$
\operatorname{ARG\_COMPARATIVE\_SCIENTIFIC\_CLAIM}=\text{UNVERIFIED}.
$$

## Current non-claims

ARG has not established:

- that $M_F$ and $M_P$ are dynamically or observationally equivalent;
- that same-state node identity implies trajectory identity;
- any pilot effect size or numerical mechanism result;
- that any mechanism defeats simpler scientific alternatives;
- that projection or feedback improves prediction;
- that constant amplitude is a law of nature;
- that the version-1.0 sandbox is the final relational geometry;
- that the development pilot has been executed;
- that Phase 6A.1 has passed external audit;
- that the confirmatory experiment is authorized;
- that macro-level causal autonomy or strong emergence has been demonstrated;
- that ARG is a fundamental physical theory.

## Verification references

- `16_phase3_mp_verification.md`
- `17_phase4_mfp_verification.md`
- `18_phase5_comparative_protocol.md`
- `19_phase5_protocol_verification.md`
- `20_phase6_runner_design.md`
- `21_phase6_runner_verification.md`
- `22_phase6a1_integrity_remediation.md`
- `protocol/phase5_v1/`
- `protocol/phase6_runner_v1/`
- `history/legacy_euler_run_rejected.md`

## NeoEmergenics relationship

NeoEmergenics remains an independent fail-closed harness and claim evaluator. It may enforce this ceiling but supplies no scientific evidence for ARG.

## Change-control rule

Every claim must name the model, evidence level, observation map, domain, and protocol version where applicable. “Projected geometry” must be qualified as **constant-amplitude**, **prototype**, and **software-verified** when scientific or ontological interpretation could otherwise be inferred.

No narrative explanation, internal test count, or prior authorization can override an unresolved independent integrity finding. Any substantive scientific-design change requires a new protocol version and a fresh unexecuted confirmatory set. Any integrity-file change requires a new baseline and external re-review.
