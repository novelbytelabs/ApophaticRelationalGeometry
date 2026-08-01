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
- **Protocol-frozen** — hypotheses, configurations, metrics, decision rules, and exclusions were fixed before execution.
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
| $M_P$ | Implemented and unit-tested | Contract-v1.0 constant-amplitude projected-admissibility sandbox. |
| $M_{FP}$ | Implemented and unit-tested | Feedback proposal followed by node projection and retraction, with retained $s/q$ feedback and separate diagnostics. |
| $M_F\equiv M_P$ | Unverified | No exact, approximate, or observational equivalence has been established. |

Current ceiling:

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

Current execution state:

$$
\boxed{
\text{pilot-only runner verified};
\quad
\text{development pilot not executed};
\quad
\text{confirmatory execution and scientific claims blocked}.
}
$$

## Current claims

| ID | Claim | Status | Evidence required | Current scope |
|---|---|---|---|---|
| ARG-C001 | A general provisional state may be represented as $Z=(x,s,q,\theta,c)$. | Definition | Internal consistency and per-model specialization. | Target model family. |
| ARG-C002 | Intrinsic edge length may depend on local mismatch, edge activation, and metric deformation. | Definition | Concrete metric properties require analysis. | Model family. |
| ARG-C003 | Shortest-path distance over strictly positive edge lengths defines a metric on each connected component. | Proof obligation | Formal proof with all hypotheses stated. | Fixed state and connected component. |
| ARG-C004 | $M_F$ computes $c(x)=\frac13\sum_i x_i^2$. | Implemented and unit-tested | Code-equation parity and regression tests. | $M_F$. |
| ARG-C005 | The path $x\to c(x)\to(\dot x,\dot s,\dot q)$ is explicit. | Implemented | Dependency audit and equation mapping. | $M_F$ and feedback component of $M_{FP}$. |
| ARG-C006 | The present $M_F$ result is implemented prototype-level downward feedback/constraint. | Implemented | Explicit substrate path; no stronger causal inference. | $M_F$ only. |
| ARG-C007 | $M_F$ establishes macro-level causal autonomy. | Unverified | Organization dependence, counterfactual adequacy, invariance, transport, and alternative-model defeat. | Not licensed. |
| ARG-C008 | Local neighborhoods provide the direct proposal dynamics. | Definition and implemented | Dependency graph and equation audit. | All four models. |
| ARG-C009 | State and intrinsic geometry coevolve nonlinearly in the implemented prototypes. | Implemented | Code-equation parity and trajectory diagnostics. | All four models. |
| ARG-C010 | Contract v1.0 defines projected models by $\Gamma(Z)=c(x)-c_0=0$, $c_0\ge10^{-6}$, with $H=\varnothing$. | Definition and implemented | Contract, target validation, and code mapping. | $M_P,M_{FP}$. |
| ARG-C011 | For regular states, $f_P=f_0-x(x^Tf_0)/(x^Tx)$ satisfies $x^Tf_P=0$. | Proved under stated assumptions and unit-tested | Algebra and tangency tests. | Continuous-time $M_P$ v1.0. |
| ARG-C012 | ARG implements tangent-space projection. | Implemented and unit-tested | Explicit projector, identities, and independent parity. | $M_P,M_{FP}$ v1.0. |
| ARG-C013 | $M_P$ removes the normal component of the $M_0$ node proposal. | Implemented and unit-tested | Proposal/correction/projected decomposition. | $M_P$ v1.0. |
| ARG-C014 | $M_F$ and $M_P$ are dynamically equivalent. | Unverified | Exact conjugacy, reparameterization, bounded approximation, or scoped observational equivalence. | No current evidence. |
| ARG-C015 | $M_{FP}$ recovers declared simpler mechanisms when feedback and/or projection are removed. | Implemented and unit-tested | Reduction tests. | $M_{FP}$ v1.0. |
| ARG-C016 | Local influence normally dominates away from coherence boundaries. | Conjectured | Frozen regimes and matched comparisons. | Not established. |
| ARG-C017 | Projection correction grows near admissibility boundaries. | Conjectured | Boundary definition and confirmatory comparison. | Not established. |
| ARG-C018 | Feedback magnitude grows near organization-dependent transitions. | Conjectured | $M_0/M_F$ comparisons and interventions. | Not established. |
| ARG-C019 | Coevolving geometry produces behavior not reducible to adaptive edge weights alone. | Conjectured | Identifiability proof or discriminating experiment. | Candidate contribution. |
| ARG-C020 | The full family is not observationally equivalent to an established constrained adaptive network. | Conjectured | Primary-source mapping and reparameterization audit. | Candidate novelty. |
| ARG-C021 | The framework unifies fixed-network, adaptive-network, feedback, and constrained-dynamics limits. | Proof obligation | Explicit reductions and limiting derivations. | Target family. |
| ARG-C022 | A non-collapse barrier creates an unreachable finite-energy boundary. | Proof obligation | Coercive energy inequality and continuation assumptions. | Barrier-enabled variants. |
| ARG-C023 | The implemented dynamics are equivariant under node relabeling. | Unit-tested locally | Per-model proof and complete tripwires. | All four models; general theorem open. |
| ARG-C024 | The graph, metric, statistic, and constraint manifold are provisional presentations rather than absolute reality. | Philosophical | Not a mathematical theorem. | Interpretive layer. |
| ARG-C025 | Mathematical success does not entail ontological ultimacy. | Philosophical | Meta-level argument only. | Apophatic schema. |
| ARG-C026 | Objective reality has a pluralistic-monist organization. | Philosophical | No direct evidence. | Ontological conjecture. |
| ARG-C027 | Reality is computational in the specific sense represented by ARG. | Philosophical and unverified | Operational definition and empirical bridge. | Not established. |
| ARG-C028 | A prime-generated substrate underlies the computational fabric. | Conjectured and quarantined | Formal object, lawful dynamics, observable, and unique prediction. | Separate branch. |
| ARG-C029 | $M_0$ contains no collective-statistic transition dependency. | Implemented and unit-tested | Dependency tripwire and independent parity. | $M_0$. |
| ARG-C030 | $M_F(\chi=\eta_2=\rho=0)=M_0$. | Implemented and unit-tested | Exact reduction. | $M_0/M_F$. |
| ARG-C031 | Production $M_0/M_F$ derivatives and RK4 agree with an independent path at tested cases. | Unit-tested | Reference parity. | Software verification only. |
| ARG-C032 | Any ARG model has superior scientific explanatory power. | Unverified | Frozen comparison, matched alternatives, uncertainty, and held-out confirmation. | No scientific result. |
| ARG-C033 | $P_T=I-xx^T/(x^Tx)$ is symmetric, idempotent, and annihilates $x$. | Proved under stated assumptions and unit-tested | Algebra and identity tests. | Projected v1.0 models. |
| ARG-C034 | Projected RK4 plus radial retraction preserves $c(x)=c_0$ within frozen tolerance at tested cases. | Implemented and unit-tested | Residual tripwires and refinement. | $M_P,M_{FP}$ v1.0. |
| ARG-C035 | Production and independent $M_P$ derivatives and projected steps agree at tested cases. | Unit-tested | Independent parity. | Software verification only. |
| ARG-C036 | Raw constraint drift and retraction magnitude decrease in the frozen one-step refinement test. | Unit-tested numerical property | Multi-step study required for scientific use. | Tested cases. |
| ARG-C037 | $M_P$ is ARG's completed relational geometry or a validated physical model. | Unverified | Relational justification, comparison, anchors, and external validation. | Not licensed. |
| ARG-C038 | $M_{FP}$ implements $F_0+F_F$ followed by node-state projection. | Implemented and unit-tested | Explicit decomposition and parity. | $M_{FP}$ v1.0. |
| ARG-C039 | At the same regular full state, radial node feedback is annihilated and $f_{FP}=f_P$. | Proved under stated assumptions and unit-tested | $P_Tx=0$ and identity tests. | Node derivative only. |
| ARG-C040 | $M_{FP}$ retains collective-feedback terms in $s$ and $q$. | Implemented and unit-tested | Equation mapping and tests. | $M_{FP}$ v1.0. |
| ARG-C041 | Production and independent $M_{FP}$ derivatives and projected steps agree at tested cases. | Unit-tested | Independent parity. | Software verification only. |
| ARG-C042 | Same-state equality $f_{FP}=f_P$ implies identical $M_P$ and $M_{FP}$ trajectories. | Rejected as a general inference | $s/q$ dynamics differ and may alter later proposals. | Not licensed. |
| ARG-C043 | All four prototypes are executable through canonical dispatch and labeled output. | Implemented and unit-tested | Dispatch, CLI, schema, and regression tests. | Software capability. |
| ARG-C044 | The four-model comparative experiment establishes a mechanism result. | Unverified | Frozen protocol, pilot, held-out confirmation, and claim review. | No experiment executed. |
| ARG-C045 | Protocol `ARG-P5-COMP-v1` was frozen before trajectory generation. | Protocol-frozen and unit-tested | Human/machine agreement, lock, split, executable metrics, and hosted verification. | Phase 5. |
| ARG-C046 | The Phase 5 primary decision rule is executable and fail closed. | Implemented and unit-tested | Known-answer positive, equivalence, inconclusive, invalid-input, and deterministic-bootstrap tests. | Decision software only. |
| ARG-C047 | The 10-direction pilot and 14-direction confirmatory sets are deterministically separated at direction level. | Protocol-frozen and unit-tested | Hash-rule reconstruction, count checks, and no-overlap tests. | Frozen initial-condition domain. |
| ARG-C048 | Phase 5 produced a numerical or scientific mechanism result. | Rejected | Phase 5 generated no trajectory data. | Not licensed. |
| ARG-C049 | A development pilot is authorized in principle. | Definition of current authorization | Phase 5 exit gate and lock remain intact. | Execution permission only. |
| ARG-C050 | The development pilot has been executed. | Unverified | Separate execution authorization and completed pilot archive. | Not executed. |
| ARG-C051 | The Phase 6 runner reconstructs exactly the 50 frozen pilot configurations and rejects confirmatory/mixed input. | Implemented and unit-tested | Independent membership/hash reconstruction and split tripwires. | Runner software only. |
| ARG-C052 | The runner implements the frozen RK4/DOP853, H5/H6, control, relabeling, and numerical-floor policies. | Implemented and unit-tested | Smoke/reference parity, known-answer gates, and hosted verification. | Runner software only. |
| ARG-C053 | The runner produces a write-once, checksummed archive and independently verifiable hashes. | Implemented and unit-tested | Deterministic archive tests and independent checksum reconstruction. | Archive software only. |
| ARG-C054 | Phase 6 runner verification produced pilot evidence. | Rejected | The execution authorization and pilot archive are absent. | No pilot data. |
| ARG-C055 | The verified runner may access the confirmatory set. | Rejected | Planner, integrator, archive, authorization, and contamination tripwires prohibit access. | Confirmatory execution blocked. |

## Verification records

### Phases 2–4

- Phase 2: 20 local software tests for $M_0/M_F$; no hosted check attached at merge.
- Phase 3: PR `#5`, merge `97a9f6b7222b4543ee8184fb8e42b47b53ddf92c`, Actions `30717582276`, 35 tests in each configured Python environment.
- Phase 4: PR `#7`, merge `205fb8c5bf1b832e241af230612e3d7056be05f5`, Actions `30718821666`, 51 tests in each configured environment.

### Phase 5

Protocol `ARG-P5-COMP-v1`, its manifests, split, numerical policy, exclusions, stop rules, archive provenance, executable metrics, bootstrap, lock verification, and decisions were frozen before data. PR `#9`, merge `d60bb3e618c590e0c994188cebf060bd4b347903`, Actions `30720596773`, 65 tests in each configured environment.

### Phase 6A

The pilot-only runner adds lock-first loading, exact pilot reconstruction, direct confirmatory rejection, all-model RK4/DOP853 paths, H5/H6 and numerical gates, frozen controls, all six relabelings, immutable archives, independent membership/trajectory/checksum references, and a separate execution-authorization boundary.

PR `#11`, Actions `30722763003`, 100 tests on Python 3.10 and 100 on Python 3.12. No execution authorization, pilot trajectory, result, archive, or confirmatory artifact was introduced.

See `20_phase6_runner_design.md` and `21_phase6_runner_verification.md`.

## Claim promotion rules

A claim may move to **numerically supported** only when its contract, protocol, baselines, configurations, solver policy, raw outputs, and exploratory/confirmatory separation are frozen and the applicable execution has actually occurred.

A development-pilot observation cannot be promoted to a confirmatory mechanism claim.

A claim may move to **empirically supported** only with external data or a physical experiment, fair alternatives, uncertainty reporting, and independent reproduction.

A claim may move to **proved under stated assumptions** only when assumptions, domain, singular cases, and proof are explicit and independently checked.

## Non-claims

The repository does not currently establish that:

- feedback and projection are equivalent;
- same-state node equality implies trajectory equality;
- any model defeats scientific alternatives;
- projection or feedback improves predictive performance;
- the constant-amplitude constraint is physically fundamental;
- a pilot or confirmatory experiment has been executed;
- ARG demonstrates macro-level causal autonomy or strong emergence;
- ARG is a fundamental theory of physics;
- primes are the ontological foundation of reality.

## Maintenance rule

Every theorem, implementation, protocol amendment, experiment, or conceptual extension must update this ledger. No claim may exceed `13_alignment_and_claim_ceiling.md`.
