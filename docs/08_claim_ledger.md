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
| $M_{FP}$ | Unverified | Frozen feedback-plus-projection target; not yet implemented. |
| $M_F\equiv M_P$ | Unverified | No exact, approximate, or observational equivalence has been established. |

Current ceiling:

$$
\boxed{
M_0,M_F,M_P\ \text{implemented and unit-tested};
\quad
M_{FP}\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Current claims

| ID | Claim | Status | Evidence required | Current scope |
|---|---|---|---|---|
| ARG-C001 | A general provisional state may be represented as $Z=(x,s,q,\theta,c)$. | Definition | Internal consistency and per-model specialization. | Target model family. |
| ARG-C002 | Intrinsic edge length may depend on local mismatch, edge activation, and metric deformation. | Definition | Concrete metric properties require analysis. | Model family. |
| ARG-C003 | Shortest-path distance over strictly positive edge lengths defines a metric on each connected component. | Proof obligation | Formal proof with all hypotheses stated. | Fixed state and connected component. |
| ARG-C004 | $M_F$ computes $c(x)=\frac13\sum_i x_i^2$. | Implemented and unit-tested | Code-equation parity and regression tests. | $M_F$. |
| ARG-C005 | The substrate path $x\to c(x)\to(\dot x,\dot s,\dot q)$ is explicit. | Implemented | Dependency audit and exact equation mapping. | $M_F$. |
| ARG-C006 | The present $M_F$ result is implemented prototype-level downward feedback/constraint. | Implemented | Explicit substrate path; no stronger causal inference. | $M_F$ only. |
| ARG-C007 | $M_F$ establishes macro-level causal autonomy. | Unverified | Organization dependence, counterfactual adequacy, invariance, transport, and alternative-model defeat. | Not licensed. |
| ARG-C008 | Local neighborhoods provide the direct proposal dynamics. | Definition and implemented | Dependency graph and equation audit. | $M_0,M_F,M_P$. |
| ARG-C009 | State and intrinsic geometry coevolve nonlinearly in the implemented prototypes. | Implemented | Code-equation parity and trajectory diagnostics. | $M_0,M_F,M_P$. |
| ARG-C010 | Contract v1.0 defines $M_P$ by $\Gamma(Z)=c(x)-c_0=0$, $c_0\ge10^{-6}$, with $H=\varnothing$. | Definition and implemented | Frozen contract, target validation, and code mapping. | $M_P$. |
| ARG-C011 | For regular states with $x^Tx>0$, $f_P=f_0-x(x^Tf_0)/(x^Tx)$ satisfies $x^Tf_P=0$ and therefore $d\Gamma/dt=0$. | Proved under stated assumptions and unit-tested | Algebraic derivation, tangency tests, singular-domain declaration. | Continuous-time $M_P$ v1.0. |
| ARG-C012 | ARG implements tangent-space projection. | Implemented and unit-tested | Explicit projector, known-answer test, projector identities, and independent parity. | $M_P$ v1.0 only. |
| ARG-C013 | $M_P$ removes the normal component of the $M_0$ node proposal relative to the constant-amplitude manifold. | Implemented and unit-tested | Proposal/correction/projected decomposition and parity tests. | $M_P$ v1.0 only. |
| ARG-C014 | $M_F$ and $M_P$ are dynamically equivalent. | Unverified | Exact conjugacy, reparameterization, bounded approximation, or scoped observational equivalence. | No current evidence. |
| ARG-C015 | $M_{FP}$ reduces exactly to $M_F$, $M_P$, and $M_0$ when mechanisms are removed. | Proof obligation | Implementation and exact reduction tests. | Target $M_{FP}$. |
| ARG-C016 | Local influence normally dominates away from coherence boundaries. | Conjectured | Preregistered regime definitions and matched comparisons. | Not established. |
| ARG-C017 | Projection correction grows near admissibility boundaries. | Conjectured | Boundary definition and confirmatory model comparison. | Not established by unit tests. |
| ARG-C018 | Feedback magnitude grows near organization-dependent transitions. | Conjectured | $M_0/M_F$ comparisons and counterfactual interventions. | Not established. |
| ARG-C019 | Coevolving geometry produces behavior not reducible to adaptive edge weights alone. | Conjectured | Identifiability proof or discriminating experiment. | Candidate contribution. |
| ARG-C020 | The full family is not observationally equivalent to an established constrained adaptive network. | Conjectured | Primary-source mapping and reparameterization audit. | Candidate novelty. |
| ARG-C021 | The framework unifies fixed-network, adaptive-network, feedback, and constrained-dynamics limits. | Proof obligation | Explicit reduction maps and limiting derivations. | Target family. |
| ARG-C022 | A non-collapse barrier creates an unreachable finite-energy boundary. | Proof obligation | Coercive energy inequality and continuation assumptions. | Barrier-enabled variants. |
| ARG-C023 | The implemented dynamics are equivariant under node relabeling. | Unit-tested locally | Per-model derivation and broader permutation coverage. | Tested for $M_0,M_F,M_P$; general theorem remains open. |
| ARG-C024 | The graph, metric, feedback statistic, and constraint manifold are provisional presentations rather than absolute reality. | Philosophical | Not a mathematical theorem. | Interpretive layer. |
| ARG-C025 | Mathematical success does not entail ontological ultimacy. | Philosophical | Meta-level argument only. | Apophatic schema. |
| ARG-C026 | Objective reality has a pluralistic-monist organization. | Philosophical | No current direct evidence. | Ontological conjecture. |
| ARG-C027 | Reality is computational in the specific sense represented by ARG. | Philosophical and unverified | Operational definition and empirical bridge. | Not established. |
| ARG-C028 | A prime-generated substrate underlies the computational fabric. | Conjectured and quarantined | Formal definition, derived observables, and discriminating tests. | Separate research branch. |
| ARG-C029 | $M_0$ contains no collective-statistic transition dependency. | Implemented and unit-tested | Dependency tripwire, equation audit, and independent parity. | $M_0$. |
| ARG-C030 | $M_F(\chi=\eta_2=\rho=0)=M_0$ for the frozen equations. | Implemented and unit-tested | Exact reduction test. | $M_0/M_F$. |
| ARG-C031 | Production $M_0/M_F$ derivatives and RK4 agree with an independently written reference path at tested cases. | Unit-tested | Independent reference boundary and parity tests. | Software verification only. |
| ARG-C032 | $M_0$, $M_F$, or $M_P$ has superior scientific explanatory power. | Unverified | Frozen comparative experiment, matched alternatives, uncertainty, and held-out confirmation. | No scientific result yet. |
| ARG-C033 | $P_T=I-xx^T/(x^Tx)$ is symmetric, idempotent, and annihilates $x$ on the declared regular domain. | Proved under stated assumptions and unit-tested | Algebraic derivation and projector identity tests. | $M_P$ v1.0. |
| ARG-C034 | Projected RK4 stages followed by radial retraction preserve $c(x)=c_0$ within the frozen discrete tolerance at tested cases. | Implemented and unit-tested | Stage projection, post-step retraction, residual tripwires, and refinement tests. | $M_P$ v1.0 software result. |
| ARG-C035 | Production and independently written $M_P$ derivatives and projected RK4/retraction agree at tested cases. | Unit-tested | Independent reference module and parity tests. | Software verification only. |
| ARG-C036 | Raw constraint drift and retraction magnitude decrease under the frozen one-step refinement test. | Unit-tested numerical property | Preregistered multi-step study remains required before scientific use. | Reference state and tested step sizes. |
| ARG-C037 | $M_P$ is ARG's completed relational-admissibility geometry or a validated physical model. | Unverified | Relational constraint justification, comparative experiment, physical anchors, and external validation. | Not licensed. |

## Phase 2 verification record

Phase 2 merged:

- exact $M_0$ equations;
- unchanged legacy $M_F$ right-hand side;
- shared RK4;
- model/contract output labels;
- independent $M_0/M_F$ derivative and RK4 paths;
- 20 passing tests in a clean local reconstruction.

No hosted check run was attached at the Phase 2 merge.

## Phase 3 verification record

Phase 3 merged:

- explicit $M_P$ target and projector;
- proposal/correction/projected decomposition;
- projected RK4 stages;
- mandatory radial retraction;
- fail-closed singular handling;
- mechanism diagnostics and labeled outputs;
- independent $M_P$ derivative and projected-step path;
- projector, preservation, equivariance, parity, and refinement tests.

Verification identifiers:

- pull request: `#5`;
- squash merge: `97a9f6b7222b4543ee8184fb8e42b47b53ddf92c`;
- GitHub Actions run: `30717582276`;
- Python 3.10: **35 passed**;
- Python 3.12: **35 passed**.

These are 35 unique software tests executed in two environments, not 70 independent scientific observations.

## Projected-claim separation

For the specific contract-v1.0 implementation:

| Gate | Status |
|---|---|
| Explicit $\Gamma/H$ definition | PASS — $\Gamma=c(x)-c_0$, $H=\varnothing$ |
| Projection implementation | PASS |
| Constraint-preservation tests | PASS at software/mechanism level |
| Code-equation equivalence | PASS at tested cases |
| Projection substrate path | PASS — proposal, correction, projected derivative, and retraction are explicit |

Therefore:

$$
\operatorname{MP\_V1\_IMPLEMENTATION\_CLAIM}=\text{PASS}.
$$

The scientific claim remains:

$$
\operatorname{PROJECTED\_GEOMETRY\_SCIENTIFIC\_CLAIM}=\text{UNVERIFIED}.
$$

## Claim promotion rules

A claim may move to **numerically supported** only when the relevant contract, baselines, configurations, solver policy, ablations, raw outputs, and exploratory/confirmatory separation are frozen.

A claim may move to **empirically supported** only with external data or a physical experiment, fair alternatives, uncertainty reporting, and independent reproduction.

A claim may move to **proved under stated assumptions** only when assumptions, domain, singular cases, and the proof are explicit and independently checked.

A claim may move to **implemented** only when code paths are identified, equations and code agree, undeclared fallbacks are absent, and mechanism-breaking tests fail as expected.

## Non-claims

The repository does not currently establish that:

- feedback and projection are equivalent;
- $M_{FP}$ is implemented;
- any implemented model defeats scientific alternatives;
- projection improves predictive performance;
- the constant-amplitude constraint is physically fundamental;
- ARG demonstrates macro-level causal autonomy or strong emergence;
- ARG is a fundamental theory of physics;
- the universe literally computes through this formalism;
- primes are the ontological foundation of reality.

## Maintenance rule

Every new theorem, implementation, experiment, or conceptual extension must update this ledger or explicitly state that it makes no new claim. No claim may exceed the ceiling in `13_alignment_and_claim_ceiling.md`.
