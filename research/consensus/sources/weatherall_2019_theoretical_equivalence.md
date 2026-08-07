# Consensus Source Note — Weatherall on Theoretical Equivalence

## Citation

James Owen Weatherall. “Theoretical Equivalence in Physics.” *Philosophy Compass* 14, nos. 5–6 (2019), Parts 1 and 2. DOI: 10.1111/phc3.12592 and 10.1111/phc3.12591. arXiv:1810.08192.

## Source classification

- **Field:** philosophy of physics and philosophy of science
- **Subfield:** theoretical equivalence, representation, duality, categorical and definitional equivalence
- **Source type:** authoritative review
- **Publication status:** peer reviewed
- **Primary or secondary:** authoritative synthesis of the equivalence literature

## Exact contribution used

The review distinguishes several questions that are often conflated when two formulations are said to represent the same theory:

- empirical equivalence;
- interpretational equivalence;
- definitional and generalized definitional equivalence;
- categorical equivalence;
- duality.

It explains that agreement in empirical predictions is important but does not automatically settle whether two formulations have the same interpretation or theoretical structure. Different formal criteria preserve different information and may support different judgments of equivalence.

For CS1, the source establishes that representation equivalence is not captured by one automatic test. A proposed state–structure factorization cannot be declared physically meaningful merely because it is mathematically convenient, and two empirically equivalent state–structure decompositions may still differ interpretively or structurally.

## Claim type

- philosophical and formal-methodological analysis;
- authoritative review of theory-equivalence criteria.

## Assumptions and domain

The source analyzes relationships between theories and formulations, especially in physics. Application to a concrete ARG model requires specifying:

- the formal objects and morphisms;
- the empirical content or observables;
- the interpretation assigned to modeled quantities;
- the structure a proposed equivalence is required to preserve.

No one equivalence criterion is assumed to settle every scientific or metaphysical question.

## Evidence and verification status

- **Derivation or protocol:** conceptual and formal comparison of established criteria.
- **Data or code available:** not applicable.
- **Independent replication or reproduction:** not applicable in the experimental sense; the review surveys an active literature.
- **Known counterexamples or exceptions:** examples in the literature show that categorical or empirical equivalence alone may fail to capture all intended theoretical structure.

## Established terminology

- empirical equivalence;
- theoretical equivalence;
- interpretational equivalence;
- definitional equivalence;
- generalized definitional or Morita equivalence;
- categorical equivalence;
- duality;
- surplus structure.

## Mapping into ARG

### ARG claim IDs affected

- `CS1-C06`
- `CS1-C07`
- `CS1-C08`
- presentation-invariance claims in `docs/09_novelty_matrix.md`;
- philosophical claims about structure, state, and representation.

### Proposed mapping

| Source object | ARG object | Mapping type | What is preserved | What is not preserved |
|---|---|---|---|---|
| alternative theoretical formulation | alternative state–structure–rule factorization | specialization | comparison of descriptions of a process | automatic physical identity |
| empirical equivalence | equality of selected observable predictions | exact translation | scoped observational content | interpretation and all structure |
| definitional equivalence | mutual translation between vocabularies | potential formal criterion | definitional content under translations | every model-theoretic or physical relation |
| categorical equivalence | equivalence of model categories | potential formal criterion | specified categorical structure | necessarily all interpretation or physical content |
| interpretational equivalence | same intended physical meaning | philosophical criterion | semantic content | formal equivalence by itself |

## Formal mapping obligation

For an ARG re-representation

$$
g:(B,x,F)\longrightarrow(B',x',F'),
$$

it is insufficient merely to assert that trajectories look similar. The project must specify whether it claims:

$$
\mathcal O(F^t(B,x))
=
\mathcal O'(F'^t(B',x'))
$$

for selected observables, a conjugacy of dynamical systems, a definitional translation, an equivalence between categories of models, or an interpretive identity.

These are different claims.

## Cross-field implications

This literature supplies a mature framework for the ARG gauge problem. It supports the need to define admissible re-representations and the exact content they preserve. It does not imply that all equivalent formulations are merely subjective or that structure is unreal.

## Consensus assessment

- **Proposed grade:** C3–C4 for the methodological claim that equivalence has multiple non-identical formal and interpretive criteria.
- **Scoped consensus statement:** Empirical, formal, categorical, and interpretational equivalence are distinct; a claim that two representations describe the same theory must state the criterion and preserved content.
- **Reason for grade:** authoritative review of a developed formal and philosophical literature.
- **What remains disputed or open:** which equivalence criterion is appropriate for a particular scientific purpose and how interpretation should enter the judgment.

## Novelty implication for ARG

- the general representation or gauge problem is established;
- ARG should import equivalence machinery rather than present representation dependence as a new discovery;
- a possible residual would be a rigorously specified equivalence or invariance result for ARG’s concrete dynamical family.

## Experiment decision

- **Is a new experiment needed?** no to establish that multiple equivalence criteria exist or that empirical equivalence does not automatically imply interpretational identity.
- **Exact unresolved question:** which admissible re-representations are scientifically appropriate for ARG, and which observables or structures must they preserve?
- **Minimum discriminating work:** formal definitions and proofs before experiment; empirical tests become relevant only when two non-equivalent formulations make different observable predictions.

## Required project updates

- [x] consensus table
- [x] translation dictionary
- [x] disagreement map
- [x] presentation-invariance workstream
- [ ] formalism after additional gauge and dynamical-systems sources

## Reviewer check

- [x] Source supports the scoped methodological claim.
- [x] Formal and interpretive equivalence are not conflated.
- [x] Mapping does not claim Weatherall directly analyzes ARG.
- [x] Experiment is deferred until a prediction-level residual exists.
