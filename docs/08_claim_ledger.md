# Claim Ledger

## Purpose

This ledger prevents definitions, assumptions, numerical observations, and philosophical interpretations from being presented at the same evidential level.

Every substantive project claim must appear here before it is used in a paper, README, presentation, or experimental conclusion.

## Allowed statuses

- **Definition** — fixed by the formalism.
- **Assumption** — adopted but not derived.
- **Proof obligation** — intended theorem not yet proved.
- **Proved** — supported by a checked proof under explicit assumptions.
- **Numerically supported** — observed in controlled simulations.
- **Empirically supported** — supported by external physical or observational data.
- **Conjectured** — precise but unproved.
- **Philosophical** — interpretive and not directly established by mathematics or experiment.
- **Rejected** — disproved, contradicted, or withdrawn.

## Current claims

| ID | Claim | Status | Evidence required | Current scope |
|---|---|---|---|---|
| ARG-C001 | A provisional state may be represented as $Z=(x,s,q,\theta,c)$. | Definition | None beyond consistency of notation. | Minimal formalism. |
| ARG-C002 | Intrinsic edge length may depend on local mismatch, edge activation, and metric deformation. | Definition | None; specific functional choices require analysis. | Model family. |
| ARG-C003 | Shortest-path distance over strictly positive edge lengths defines a metric on each connected component. | Proof obligation | Formal proof with all hypotheses stated. | Fixed admissible state $Z$. |
| ARG-C004 | The projected vector field preserves equality constraints. | Proof obligation | Derivation and numerical verification under rank and regularity conditions. | Smooth constraint regime. |
| ARG-C005 | Finite structural energy prevents intrinsic edge collapse. | Proof obligation | Coercive energy bound and continuation assumptions. | Barrier-enabled models. |
| ARG-C006 | The dynamics are equivariant under node relabeling. | Proof obligation | Symbolic proof plus permutation tripwire tests. | Symmetric parameter regime. |
| ARG-C007 | Local neighborhoods provide the direct proposed motion. | Definition | Inspection of dependency graph and Jacobian sparsity. | Current implementation. |
| ARG-C008 | Collective coherence removes locally proposed motion that violates admissibility. | Definition | Exact projection formula and implementation parity. | Constraint-projection formulation. |
| ARG-C009 | Local influence normally dominates away from coherence boundaries. | Conjectured | Distribution of $\chi_i$ across regimes, systems, and seeds. | Not yet established. |
| ARG-C010 | Collective correction grows near structural or coherence boundaries. | Conjectured | Preregistered perturbation experiments and baseline comparison. | Not yet established. |
| ARG-C011 | State and geometry can coevolve nonlinearly. | Definition | Explicit coupled equations. | Model family. |
| ARG-C012 | Coevolving geometry produces behavior not reducible to adaptive edge weights alone. | Conjectured | Identifiability proof or discriminating experiment. | Candidate novelty. |
| ARG-C013 | The full model is not observationally equivalent to an ordinary constrained adaptive network. | Conjectured | Reparameterization audit and benchmark evidence. | Candidate novelty. |
| ARG-C014 | The framework unifies fixed-network, adaptive-network, and constrained-dynamics limits. | Proof obligation | Explicit reduction maps and limiting derivations. | Mathematical claim. |
| ARG-C015 | A non-collapse barrier creates an unreachable finite-energy boundary. | Proof obligation | Energy inequality and numerical tripwires. | Barrier-enabled models. |
| ARG-C016 | The graph, metric, and constraint manifold are provisional presentations rather than ontologically privileged objects. | Philosophical | Not a mathematical theorem. | Interpretive layer. |
| ARG-C017 | Mathematical success does not entail ontological ultimacy. | Philosophical | Meta-level argument only. | Apophatic schema. |
| ARG-C018 | Objective reality has a pluralistic-monist organization. | Philosophical | No current direct evidence. | Ontological conjecture. |
| ARG-C019 | Reality is computational in the specific sense represented by this geometry. | Philosophical | Requires an operational definition and empirical bridge. | Not established. |
| ARG-C020 | A prime-generated substrate underlies the computational fabric. | Conjectured | Formal definition, derived observables, and discriminating tests. | Quarantined research branch. |

## Claim promotion rules

A claim may move from **conjectured** to **numerically supported** only when:

1. the metric is frozen as executable code;
2. the baseline family is implemented;
3. seeds and configurations are recorded;
4. solver sensitivity has been checked;
5. relevant ablations and structural controls have passed;
6. raw outputs are retained.

A claim may move to **empirically supported** only when:

1. the dataset or physical experiment is external to the model;
2. evaluation criteria were fixed before final analysis;
3. simpler baselines were tested fairly;
4. uncertainty is reported;
5. the result survives independent reproduction.

A claim may move to **proved** only when:

1. all assumptions are explicit;
2. edge cases and singular regimes are addressed;
3. the proof has been checked independently;
4. numerical evidence is not substituted for proof.

## Non-claims

The repository currently does not establish that:

- the geometry is a fundamental theory of physics;
- the universe literally computes through this exact formalism;
- the global constraint is a separate causal entity;
- the apophatic schema is a theorem of mathematics;
- primes are the ontological foundation of reality;
- the minimal model has empirical validity.

## Maintenance rule

Every new experiment, theorem, or conceptual extension must either:

- update an existing claim row;
- add a new claim row;
- or explicitly state that it makes no new claim.
