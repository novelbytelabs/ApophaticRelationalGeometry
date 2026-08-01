# Claim Ledger

## Purpose

This ledger prevents definitions, software implementation, numerical observations, scientific evidence, and philosophical interpretations from being presented at the same evidential level.

Every substantive project claim must appear here before it is used in a paper, README, release, issue, presentation, or experimental conclusion.

## Allowed statuses

- **Definition** — fixed by the formalism.
- **Assumption** — adopted but not derived.
- **Proposed** — specified conceptually but not implemented or proved.
- **Implemented** — present in executable code.
- **Unit-tested** — implementation contracts or local mathematical properties have passing software tests.
- **Proof obligation** — intended theorem not yet proved.
- **Proved under stated assumptions** — supported by a checked derivation on an explicit domain.
- **Numerically supported** — observed in controlled simulations.
- **Empirically supported** — supported by external physical or observational data.
- **Conjectured** — precise but unproved.
- **Philosophical** — interpretive and not directly established by mathematics or experiment.
- **Unverified** — required evidence is absent or incomplete.
- **Rejected** — disproved, contradicted, or withdrawn.

## Canonical model status

| Model or relation | Status | Licensed statement |
|---|---|---|
| $M_0$ | Implemented and unit-tested | No-collective local/adaptive baseline with no $c(x)$ transition path. |
| $M_F$ | Implemented and unit-tested | Prototype-level endogenous downward feedback/constraint with adaptive relational geometry. |
| $M_P$ | Implemented and unit-tested | Contract-v1.0 constant-amplitude projected-admissibility sandbox with projected RK4 stages, retraction, fail-closed singular handling, diagnostics, and independent reference parity. |
| $M_{FP}$ | Implemented and unit-tested | Contract-v1.0 feedback proposal followed by node projection and retraction, with retained $s/q$ feedback and separate mechanism diagnostics. |
| $M_F\equiv M_P$ | Unverified | No exact, approximate, or observational equivalence has been established. |

Current ceiling:

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

## Current claims

| ID | Claim | Status | Evidence required | Current scope |
|---|---|---|---|---|
| ARG-C001 | A general provisional state may be represented as $Z=(x,s,q,\theta,c)$. | Definition | Internal consistency and per-model specialization. | Target model family. |
| ARG-C002 | Intrinsic edge length may depend on local mismatch, edge activation, and metric deformation. | Definition | Concrete metric properties require analysis. | Model family. |
| ARG-C003 | Shortest-path distance over strictly positive edge lengths defines a metric on each connected component. | Proof obligation | Formal proof with all hypotheses stated. | Fixed state and connected component. |
| ARG-C004 | $M_F$ computes $c(x)=\frac13\sum_i x_i^2$. | Implemented and unit-tested | Code-equation parity and regression tests. | $M_F$. |
| ARG-C005 | The substrate path $x\to c(x)\to(\dot x,\dot s,\dot q)$ is explicit. | Implemented | Dependency audit and exact equation mapping. | $M_F$ and feedback component of $M_{FP}$. |
| ARG-C006 | The present $M_F$ result is implemented prototype-level downward feedback/constraint. | Implemented | Explicit substrate path; no stronger causal inference. | $M_F$ only. |
| ARG-C007 | $M_F$ establishes macro-level causal autonomy. | Unverified | Organization dependence, counterfactual adequacy, invariance, transport, and alternative-model defeat. | Not licensed. |
| ARG-C008 | Local neighborhoods provide the direct proposal dynamics. | Definition and implemented | Dependency graph and equation audit. | $M_0,M_F,M_P,M_{FP}$. |
| ARG-C009 | State and intrinsic geometry coevolve nonlinearly in the implemented prototypes. | Implemented | Code-equation parity and trajectory diagnostics. | All four models. |
| ARG-C010 | Contract v1.0 defines projected models by $\Gamma(Z)=c(x)-c_0=0$, $c_0\ge10^{-6}$, with $H=\varnothing$. | Definition and implemented | Frozen contract, target validation, and code mapping. | $M_P,M_{FP}$. |
| ARG-C011 | For regular states with $x^Tx>0$, $f_P=f_0-x(x^Tf_0)/(x^Tx)$ satisfies $x^Tf_P=0$ and therefore $d\Gamma/dt=0$. | Proved under stated assumptions and unit-tested | Algebraic derivation, tangency tests, singular-domain declaration. | Continuous-time $M_P$ v1.0. |
| ARG-C012 | ARG implements tangent-space projection. | Implemented and unit-tested | Explicit projector, known-answer test, projector identities, and independent parity. | $M_P,M_{FP}$ v1.0. |
| ARG-C013 | $M_P$ removes the normal component of the $M_0$ node proposal relative to the constant-amplitude manifold. | Implemented and unit-tested | Proposal/correction/projected decomposition and parity tests. | $M_P$ v1.0. |
| ARG-C014 | $M_F$ and $M_P$ are dynamically equivalent. | Unverified | Exact conjugacy, reparameterization, bounded approximation, or scoped observational equivalence. | No current evidence. |
| ARG-C015 | Contract-v1.0 $M_{FP}$ recovers the declared simpler mechanisms when feedback and/or projection are removed. | Implemented and unit-tested | Unprojected proposal parity with $M_F$, exact zero-feedback reduction to $M_P$, and no-feedback/no-projection recovery of $M_0$. | $M_{FP}$ v1.0. |
| ARG-C016 | Local influence normally dominates away from coherence boundaries. | Conjectured | Preregistered regime definitions and matched comparisons. | Not established. |
| ARG-C017 | Projection correction grows near admissibility boundaries. | Conjectured | Boundary definition and confirmatory model comparison. | Not established by unit tests. |
| ARG-C018 | Feedback magnitude grows near organization-dependent transitions. | Conjectured | $M_0/M_F$ comparisons and counterfactual interventions. | Not established. |
| ARG-C019 | Coevolving geometry produces behavior not reducible to adaptive edge weights alone. | Conjectured | Identifiability proof or discriminating experiment. | Candidate contribution. |
| ARG-C020 | The full family is not observationally equivalent to an established constrained adaptive network. | Conjectured | Primary-source mapping and reparameterization audit. | Candidate novelty. |
| ARG-C021 | The framework unifies fixed-network, adaptive-network, feedback, and constrained-dynamics limits. | Proof obligation | Explicit reduction maps and limiting derivations. | Target family. |
| ARG-C022 | A non-collapse barrier creates an unreachable finite-energy boundary. | Proof obligation | Coercive energy inequality and continuation assumptions. | Barrier-enabled variants. |
| ARG-C023 | The implemented dynamics are equivariant under node relabeling. | Unit-tested locally | Per-model derivation and broader permutation coverage. | Tested for all four models; general theorem remains open. |
| ARG-C024 | The graph, metric, feedback statistic, and constraint manifold are provisional presentations rather than absolute reality. | Philosophical | Not a mathematical theorem. | Interpretive layer. |
| ARG-C025 | Mathematical success does not entail ontological ultimacy. | Philosophical | Meta-level argument only. | Apophatic schema. |
| ARG-C026 | Objective reality has a pluralistic-monist organization. | Philosophical | No current direct evidence. | Ontological conjecture. |
| ARG-C027 | Reality is computational in the specific sense represented by ARG. | Philosophical and unverified | Operational definition and empirical bridge. | Not established. |
| ARG-C028 | A prime-generated substrate underlies the computational fabric. | Conjectured and quarantined | Formal definition, derived observables, and discriminating tests. | Separate research branch. |
| ARG-C029 | $M_0$ contains no collective-statistic transition dependency. | Implemented and unit-tested | Dependency tripwire, equation audit, and independent parity. | $M_0$. |
| ARG-C030 | $M_F(\chi=\eta_2=\rho=0)=M_0$ for the frozen equations. | Implemented and unit-tested | Exact reduction test. | $M_0/M_F$. |
| ARG-C031 | Production $M_0/M_F$ derivatives and RK4 agree with an independently written reference path at tested cases. | Unit-tested | Independent reference boundary and parity tests. | Software verification only. |
| ARG-C032 | Any implemented ARG model has superior scientific explanatory power. | Unverified | Frozen comparative experiment, matched alternatives, uncertainty, and held-out confirmation. | No scientific result yet. |
| ARG-C033 | $P_T=I-xx^T/(x^Tx)$ is symmetric, idempotent, and annihilates $x$ on the declared regular domain. | Proved under stated assumptions and unit-tested | Algebraic derivation and projector identity tests. | Projected v1.0 models. |
| ARG-C034 | Projected RK4 stages followed by radial retraction preserve $c(x)=c_0$ within the frozen discrete tolerance at tested cases. | Implemented and unit-tested | Stage projection, post-step retraction, residual tripwires, and refinement tests. | $M_P,M_{FP}$ v1.0. |
| ARG-C035 | Production and independently written $M_P$ derivatives and projected RK4/retraction agree at tested cases. | Unit-tested | Independent reference module and parity tests. | Software verification only. |
| ARG-C036 | Raw constraint drift and retraction magnitude decrease under the frozen one-step refinement test. | Unit-tested numerical property | Preregistered multi-step study remains required before scientific use. | $M_P,M_{FP}$ reference state and tested step sizes. |
| ARG-C037 | $M_P$ is ARG's completed relational-admissibility geometry or a validated physical model. | Unverified | Relational constraint justification, comparative experiment, physical anchors, and external validation. | Not licensed. |
| ARG-C038 | $M_{FP}$ implements $F_0+F_F$ followed by node-state tangent projection. | Implemented and unit-tested | Explicit decomposition, dispatch, stage diagnostics, and independent parity. | $M_{FP}$ v1.0. |
| ARG-C039 | At the same regular full state, the radial node-feedback term is annihilated and $f_{FP}=f_P$. | Proved under stated assumptions and unit-tested | $P_Tx=0$, direct cancellation derivation, and same-state identity tests. | Node derivative only, contract v1.0. |
| ARG-C040 | $M_{FP}$ retains the declared collective-feedback terms in $s$ and $q$. | Implemented and unit-tested | Direct equation mapping and retained-substrate tests. | $M_{FP}$ v1.0. |
| ARG-C041 | Production and independently written $M_{FP}$ derivatives and projected RK4/retraction agree at tested cases. | Unit-tested | Independent reference path and parity tests. | Software verification only. |
| ARG-C042 | Same-state equality $f_{FP}=f_P$ implies identical $M_P$ and $M_{FP}$ trajectories. | Rejected as a general inference | $s/q$ dynamics differ and can alter later conductances and proposals. | Not licensed. |
| ARG-C043 | All four contract-v1.0 prototypes are executable through canonical model dispatch and labeled simulation output. | Implemented and unit-tested | Dispatch, CLI, output-schema, and regression tests. | Software capability. |
| ARG-C044 | The four-model comparative experiment establishes a mechanism result. | Unverified | Frozen Phase 5 protocol, development pilot, held-out confirmation, and claim review. | No experiment executed. |

## Phase 2 verification record

Phase 2 merged exact $M_0$ equations, the unchanged legacy $M_F$ right-hand side, shared RK4, model labels, independent $M_0/M_F$ references, and 20 passing local tests. No hosted check was attached at that merge.

## Phase 3 verification record

Identifiers:

- pull request: `#5`;
- squash merge: `97a9f6b7222b4543ee8184fb8e42b47b53ddf92c`;
- GitHub Actions run: `30717582276`;
- Python 3.10: **35 passed**;
- Python 3.12: **35 passed**.

See `16_phase3_mp_verification.md`.

## Phase 4 verification record

Phase 4 merged:

- explicit $F_0$, $F_F$, and $F_0+F_F$ decomposition;
- feedback-followed-by-projection derivative dispatch;
- projected RK4 stages and mandatory retraction;
- retained $s/q$ feedback;
- separate feedback and projection diagnostics;
- fail-closed target and singular handling;
- independent $M_{FP}$ derivative and projected-step path;
- identity, reduction, equivariance, parity, preservation, refinement, and output tests.

Identifiers:

- pull request: `#7`;
- squash merge: `205fb8c5bf1b832e241af230612e3d7056be05f5`;
- GitHub Actions run: `30718821666`;
- Python 3.10: **51 passed**;
- Python 3.12: **51 passed**.

These are 51 unique software tests executed in two environments, not 102 independent scientific observations.

See `17_phase4_mfp_verification.md`.

## Implementation-claim separation

The specific software claims pass:

$$
\operatorname{MP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS},
$$

$$
\operatorname{MFP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

The scientific comparison remains:

$$
\operatorname{ARG\_COMPARATIVE\_SCIENTIFIC\_CLAIM}=\text{UNVERIFIED}.
$$

## Claim promotion rules

A claim may move to **numerically supported** only when the relevant contract, baselines, configurations, solver policy, ablations, raw outputs, and exploratory/confirmatory separation are frozen.

A claim may move to **empirically supported** only with external data or a physical experiment, fair alternatives, uncertainty reporting, and independent reproduction.

A claim may move to **proved under stated assumptions** only when assumptions, domain, singular cases, and the proof are explicit and independently checked.

A claim may move to **implemented** only when code paths are identified, equations and code agree, undeclared fallbacks are absent, and mechanism-breaking tests fail as expected.

## Non-claims

The repository does not currently establish that:

- feedback and projection are equivalent;
- same-state node equality implies trajectory equality;
- any implemented model defeats scientific alternatives;
- projection or feedback improves predictive performance;
- the constant-amplitude constraint is physically fundamental;
- ARG demonstrates macro-level causal autonomy or strong emergence;
- ARG is a fundamental theory of physics;
- the universe literally computes through this formalism;
- primes are the ontological foundation of reality.

## Maintenance rule

Every new theorem, implementation, experiment, or conceptual extension must update this ledger or explicitly state that it makes no new claim. No claim may exceed the ceiling in `13_alignment_and_claim_ceiling.md`.