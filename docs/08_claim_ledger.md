# Claim Ledger

## Purpose

This ledger prevents definitions, software implementation, numerical observations, scientific evidence, and philosophical interpretations from being presented at the same evidential level.

Every substantive project claim must appear here before it is used in a paper, README, release, issue, presentation, or experiment conclusion.

## Allowed statuses

- **Definition** — fixed by the formalism.
- **Assumption** — adopted but not derived.
- **Proposed** — specified conceptually but not implemented or proved.
- **Implemented** — present in executable code.
- **Unit-tested** — implementation contracts or local properties have passing software tests.
- **Proof obligation** — intended theorem not yet proved.
- **Proved** — supported by a checked proof under explicit assumptions.
- **Numerically supported** — observed in controlled simulations.
- **Empirically supported** — supported by external physical or observational data.
- **Conjectured** — precise but unproved.
- **Philosophical** — interpretive and not directly established by mathematics or experiment.
- **Unverified** — required evidence is absent or incomplete.
- **Rejected** — disproved, contradicted, or withdrawn.

## Canonical model status

| Model or relation | Status | Licensed statement |
|---|---|---|
| $M_0$ | Proposed | No-collective local/adaptive baseline; design not yet frozen. |
| $M_F$ | Implemented and unit-tested | Prototype-level endogenous downward feedback/constraint with adaptive relational geometry. |
| $M_P$ | Unverified | Target projected-admissibility prototype; not yet implemented. |
| $M_{FP}$ | Unverified | Target combined feedback-plus-projection model; not yet implemented. |
| $M_F\equiv M_P$ | Unverified | No mathematical, approximate, or observational equivalence established. |

Current ceiling:

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

## Current claims

| ID | Claim | Status | Evidence required | Current scope |
|---|---|---|---|---|
| ARG-C001 | A general provisional state may be represented as $Z=(x,s,q,\theta,c)$. | Definition | Internal consistency and per-model specialization. | Target model family. |
| ARG-C002 | Intrinsic edge length may depend on local mismatch, edge activation, and metric deformation. | Definition | None for the family; concrete properties require analysis. | Model family. |
| ARG-C003 | Shortest-path distance over strictly positive edge lengths defines a metric on each connected component. | Proof obligation | Formal proof with all hypotheses stated. | Fixed state and connected component. |
| ARG-C004 | The current executable computes $c(x)=\frac13\sum_i x_i^2$. | Implemented and unit-tested | Code-equation parity and regression tests. | $M_F$. |
| ARG-C005 | The substrate path $x\to c(x)\to(\dot x,\dot s,\dot q)$ is explicit. | Implemented | Dependency audit and exact equation mapping. | $M_F$. |
| ARG-C006 | The present result is implemented prototype-level downward feedback/constraint. | Implemented | Explicit substrate path; no stronger causal inference. | $M_F$ only. |
| ARG-C007 | $M_F$ establishes macro-level causal autonomy. | Unverified | Organization dependence, counterfactual adequacy, invariance, transport, and alternative-model defeat. | Not licensed. |
| ARG-C008 | Local neighborhoods provide direct proposed motion. | Definition and implemented | Dependency graph and Jacobian sparsity. | Current $M_F$ implementation. |
| ARG-C009 | State and intrinsic geometry coevolve nonlinearly in the current prototype. | Implemented | Code-equation parity and trajectory diagnostics. | $M_F$. |
| ARG-C010 | An admissible set may be defined by $\Gamma(Z)=0$ and $H(Z)\geq0$. | Proposed definition | Complete domain, regularity, and active-set specification. | Target $M_P/M_{FP}$. |
| ARG-C011 | The projected vector field preserves equality constraints. | Proof obligation | Derivation under explicit rank and regularity assumptions. | Target $M_P/M_{FP}$. |
| ARG-C012 | ARG currently implements tangent-space projection. | Unverified | Explicit projection code and fail-closed gate. | Not licensed. |
| ARG-C013 | Collective coherence removes inadmissible motion in the executable. | Unverified | Projection implementation and code-equation parity. | The current executable uses feedback instead. |
| ARG-C014 | $M_F$ and $M_P$ are dynamically equivalent. | Unverified | Exact conjugacy, reparameterization, bounded approximation, or scoped observational equivalence. | No current evidence. |
| ARG-C015 | $M_{FP}$ reduces exactly to $M_F$, $M_P$, and $M_0$ when mechanisms are removed. | Proof obligation | Frozen contracts, implementation, and reduction tests. | Target combined model. |
| ARG-C016 | Local influence normally dominates away from coherence boundaries. | Conjectured | Preregistered regime definitions and matched comparisons. | Not yet established. |
| ARG-C017 | Projection correction grows near admissibility boundaries. | Conjectured | Implemented $M_P$, boundary definitions, and confirmatory tests. | Blocked. |
| ARG-C018 | Feedback magnitude grows near organization-dependent transitions. | Conjectured | $M_0/M_F$ comparison and counterfactual interventions. | Not yet established. |
| ARG-C019 | Coevolving geometry produces behavior not reducible to adaptive edge weights alone. | Conjectured | Identifiability proof or discriminating experiment. | Candidate contribution. |
| ARG-C020 | The full family is not observationally equivalent to an established constrained adaptive network. | Conjectured | Primary-source mapping and reparameterization audit. | Candidate novelty. |
| ARG-C021 | The framework unifies fixed-network, adaptive-network, feedback, and constrained-dynamics limits. | Proof obligation | Explicit reduction maps and limiting derivations. | Target family. |
| ARG-C022 | A non-collapse barrier creates an unreachable finite-energy boundary. | Proof obligation | Coercive energy inequality and continuation assumptions. | Barrier-enabled target variants. |
| ARG-C023 | The dynamics are equivariant under node relabeling. | Mixed | Per-model proof plus permutation tripwires. | Unit-tested locally for current code; general claim unproved. |
| ARG-C024 | The graph, metric, feedback statistic, and constraint manifold are provisional presentations rather than absolute reality. | Philosophical | Not a mathematical theorem. | Interpretive layer. |
| ARG-C025 | Mathematical success does not entail ontological ultimacy. | Philosophical | Meta-level argument only. | Apophatic schema. |
| ARG-C026 | Objective reality has a pluralistic-monist organization. | Philosophical | No current direct evidence. | Ontological conjecture. |
| ARG-C027 | Reality is computational in the specific sense represented by ARG. | Philosophical and unverified | Operational definition and empirical bridge. | Not established. |
| ARG-C028 | A prime-generated substrate underlies the computational fabric. | Conjectured and quarantined | Formal definition, derived observables, and discriminating tests. | Separate research branch. |

## Projected-claim gate

A projected-geometry claim requires

$$
\operatorname{PROJECTED\_CLAIM}
=
D_{\Gamma,H}
\land_{FC}
I_{\Pi}
\land_{FC}
T_{\mathrm{preserve}}
\land_{FC}
E_{\mathrm{code}}
\land_{FC}
S_{\mathrm{path}}.
$$

Current status:

| Gate | Status |
|---|---|
| Explicit $\Gamma/H$ definition | UNVERIFIED |
| Projection implementation | UNVERIFIED |
| Constraint-preservation tests | UNVERIFIED |
| Code-equation equivalence | UNVERIFIED |
| Projection substrate path | UNVERIFIED |

Therefore:

$$
\operatorname{PROJECTED\_CLAIM}=\text{UNVERIFIED}.
$$

## Claim promotion rules

A claim may move from **conjectured** to **numerically supported** only when:

1. the relevant model contract is frozen;
2. all required baselines are implemented;
3. seeds and configurations are recorded;
4. solver sensitivity has been checked;
5. ablations and structural controls have passed;
6. raw outputs and checksums are retained;
7. exploratory and confirmatory analyses are separated.

A claim may move to **empirically supported** only when:

1. the dataset or physical experiment is external to the model;
2. evaluation criteria were fixed before final analysis;
3. simpler alternatives were tested fairly;
4. uncertainty is reported;
5. the result survives independent reproduction.

A claim may move to **proved** only when:

1. all assumptions and domains are explicit;
2. singular and edge cases are addressed;
3. the proof has been checked independently;
4. numerical evidence is not substituted for proof.

A claim may move to **implemented** only when:

1. code paths are identified;
2. equations and code agree;
3. undeclared fallbacks are absent;
4. tests fail when the mechanism is deliberately broken.

## Non-claims

The repository currently does not establish that:

- the current executable is projected geometry;
- feedback and projection are equivalent;
- ARG demonstrates macro-level causal autonomy or strong emergence;
- the geometry is a fundamental theory of physics;
- the universe literally computes through this exact formalism;
- the global constraint is a separate causal entity;
- the apophatic schema is a theorem of mathematics;
- primes are the ontological foundation of reality;
- the minimal model has empirical validity.

## Maintenance rule

Every new experiment, theorem, implementation, or conceptual extension must:

- update an existing claim row;
- add a new claim row;
- or explicitly state that it makes no new claim.

No claim may exceed the ceiling in `13_alignment_and_claim_ceiling.md`.
