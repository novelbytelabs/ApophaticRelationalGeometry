# Consensus Source Note — Moore on Balanced Realization and Model Reduction

## Citation

B. C. Moore. “Principal Component Analysis in Linear Systems: Controllability, Observability, and Model Reduction.” *IEEE Transactions on Automatic Control* 26(1), 17–32 (1981). DOI: 10.1109/TAC.1981.1102568.

Accessible copy: https://algos.inesc-id.pt/projectos/mor4less/Moore_81.pdf

## Source classification

- **Field:** control theory and numerical systems analysis
- **Subfield:** balanced realization, controllability and observability Gramians, model reduction
- **Source type:** original method paper
- **Publication status:** peer reviewed
- **Primary or secondary:** primary

## Exact contribution used

Moore recasts minimal realization and state importance through responses to injected signals and measured outputs. The controllability and observability Gramians are transformed into a balanced coordinate system in which they are equal and diagonal. The resulting diagonal values rank state directions by their joint controllability and observability, supporting model reduction by truncating directions that are simultaneously difficult to excite and difficult to observe.

The load-bearing result for CS1 is that no coordinate component is intrinsically important merely because it appears as a state variable. Its input-output relevance is relational: it depends jointly on system dynamics, actuation, observation, and the chosen performance norm.

## Claim type

- mathematical construction;
- model-reduction method;
- representation-invariant input/output ranking under stated linear assumptions.

## Assumptions and domain

The classical balanced-realization construction assumes a finite-dimensional, stable linear time-invariant system and usually a minimal realization. The interpretation of Gramian eigenvalues and Hankel singular values depends on system class, norm, horizon, and stability assumptions.

Balanced truncation does not rank metaphysical significance, biological function, or unconstrained nonlinear persistence.

## Evidence and verification status

- **Derivation or protocol:** analytic linear-systems and singular-value analysis.
- **Data or code available:** not required for the theorem-level construction.
- **Independent replication or reproduction:** mature and widely used model-reduction framework.
- **Known limitations:** direct nonlinear, unstable, switched, stochastic, and structure-changing generalizations are not automatic.

## Established terminology

- controllability Gramian;
- observability Gramian;
- internally balanced realization;
- Hankel singular values;
- model reduction;
- truncation;
- minimal realization.

## Mapping into ARG

### ARG claim IDs affected

- `CS1-C03`
- `CS1-C05`
- `CS1-C06`
- `CS1-C08`
- `CS1-C11`
- `CS1-C12`
- `CS1-C13`
- `CS1-C14`

### Proposed mapping

| Source object | ARG object | Mapping type | What is preserved | What is not preserved |
|---|---|---|---|---|
| controllability Gramian | input-relative state accessibility | exact translation in LTI systems | control-energy geometry | autonomous persistence |
| observability Gramian | output-relative state recoverability | exact translation in LTI systems | output-energy geometry | intrinsic identity |
| balanced coordinate | joint state-system representation | specialization | simultaneous actuation/measurement importance | universal structure-state gauge |
| Hankel singular value | joint controllability-observability importance | exact translation | input/output significance invariant under similarity | all notions of compatibility |
| truncated state direction | reduced representation | specialization | approximate input/output behavior | physical deletion of a component |

## Equation or theorem mapping

For a stable minimal LTI system, the infinite-horizon Gramians solve

$$
AW_c+W_cA^T+BB^T=0,
$$

$$
A^TW_o+W_oA+C^TC=0.
$$

A balancing transformation produces coordinates with

$$
W_c=W_o=\Sigma,
\qquad
\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_n),
$$

where the $\sigma_i$ are Hankel singular values.

The mapped ARG lesson is not that $\sigma_i$ measure universal persistence. It is that a rigorous joint state-structure relevance measure already exists for a specific input/output question.

## Cross-field implications

Balanced realization is a direct precedent for the intuition that behavior depends on how state directions align with system structure. But it also shows why the intuition must be typed: relevance changes when actuation or observation changes, and a coordinate transformation can redistribute state components while preserving the input/output system.

## Consensus assessment

- **Proposed grade:** C4 within stable finite-dimensional LTI model reduction.
- **Scoped consensus statement:** State directions can be ranked by joint controllability and observability, and this ranking supports representation-aware model reduction.
- **Reason for grade:** foundational method with extensive theoretical and practical uptake.
- **What remains disputed or open:** principled generalization to broad nonlinear, hybrid, adaptive, and evolving-space systems.

## Novelty implication for ARG

- a joint state-system importance measure is not novel in general;
- any ARG compatibility scalar must be compared directly with Gramian and Hankel-based quantities where they apply;
- the likely ARG residual, if any, is a broader synthesis across changing structures or multiple persistence predicates, not the discovery that state relevance is relational.

## Experiment decision

- **Is a new experiment needed?** no to establish joint controllability-observability relevance in LTI systems.
- **Exact unresolved question:** whether an ARG quantity supplies robust predictive value beyond balanced or finite-horizon Gramian measures in systems where the operator, state space, or observation map changes.
- **Minimum discriminating test:** held-out comparison against balanced, Gramian, singular-vector, and reduced-order baselines under matched observables.

## Required project updates

- [x] consensus table
- [x] translation dictionary
- [x] representation audit
- [x] novelty matrix
- [ ] residual agenda after full CS1

## Reviewer check

- [x] Scope is restricted to the classical linear setting.
- [x] Coordinate importance is not confused with ontology.
- [x] Similarity invariance is distinguished from arbitrary re-encoding.
- [x] Novelty implication is direct.
