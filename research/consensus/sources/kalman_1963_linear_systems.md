# Consensus Source Note — Kalman on Linear State, Controllability, Observability, and Minimal Realization

## Citation

R. E. Kalman. “Mathematical Description of Linear Dynamical Systems.” *Journal of the Society for Industrial and Applied Mathematics, Series A: Control* 1(2), 152–192 (1963). DOI: 10.1137/0301010.

Stable source: https://epubs.siam.org/doi/10.1137/0301010

## Source classification

- **Field:** control theory and systems theory
- **Subfield:** linear state-space systems, controllability, observability, realization theory
- **Source type:** original theorem and framework paper
- **Publication status:** peer reviewed
- **Primary or secondary:** primary

## Exact contribution used

Kalman distinguishes state-variable descriptions from input/output descriptions and shows, for linear systems, that input/output behavior determines only the completely controllable and completely observable part of a realization. The paper gives methods for irreducible or minimal realization and discusses the redundancy of reducible state descriptions.

The load-bearing result for CS1 is that internal state coordinates are not all equally connected to intervention and observation. Some directions may be unreachable from available inputs, some may be invisible at the outputs, and state-space realizations with extra inaccessible or invisible variables need not add observable system content.

## Claim type

- mathematical framework;
- linear-systems theorem family;
- representation and realization result.

## Assumptions and domain

The exact results used here apply to linear dynamical systems with specified input and output maps. Controllability and observability are relative to the chosen input channels, output channels, time domain, and realization.

They do not establish metaphysical accessibility, semantic significance, or a universal partition of reality into state and structure.

## Evidence and verification status

- **Derivation or protocol:** analytic linear-systems theory.
- **Data or code available:** not applicable to the theorem-level result.
- **Independent replication or reproduction:** mature foundational theory with broad textbook and engineering uptake.
- **Known limitations:** nonlinear, constrained, stochastic, switching, and time-varying cases require extensions; input/output equivalence is weaker than full physical or ontological equivalence.

## Established terminology

- state-variable description;
- input/output relation;
- controllability;
- observability;
- realization;
- irreducible or minimal realization;
- reducible realization.

## Mapping into ARG

### ARG claim IDs affected

- `CS1-C01`
- `CS1-C05`
- `CS1-C06`
- `CS1-C07`
- `CS1-C08`
- `CS1-C11`
- `CS1-C12`
- `CS1-C13`

### Proposed mapping

| Source object | ARG object | Mapping type | What is preserved | What is not preserved |
|---|---|---|---|---|
| state realization | chosen state representation | exact translation in linear models | internal variables sufficient for evolution | unique ontology of state |
| input map | admissible external intervention | specialization | directions through which a system can be driven | all environmental or endogenous influence |
| output map | declared observable | specialization | distinctions visible to measurement | complete physical identity |
| controllable subspace | reachable state directions | exact translation | intervention-relative accessibility | spontaneous persistence or semantic importance |
| observable subspace | output-distinguishable directions | exact translation | measurement-relative recoverability | intrinsic existence |
| minimal realization | representation stripped of unreachable/unobservable redundancy | exact translation | input/output content | every physically relevant internal distinction |

## Equation or theorem mapping

For a continuous-time linear system,

$$
\dot x=Ax+Bu,
\qquad
y=Cx+Du.
$$

The finite-horizon controllability Gramian is

$$
W_c(T)=\int_0^T e^{At}BB^T e^{A^Tt}\,dt,
$$

and the observability Gramian is

$$
W_o(T)=\int_0^T e^{A^Tt}C^TCe^{At}\,dt.
$$

The exact rank and realization results require the usual linear-system hypotheses. The source paper’s central claim is that input/output behavior identifies the controllable and observable portion, not arbitrary redundant internal coordinates.

## Cross-field implications

This directly sharpens ARG’s representation problem. A state component may exist in a chosen realization yet be irrelevant to available interventions or observations. Conversely, changing the input or output map changes controllability and observability without changing the autonomous matrix $A$.

Therefore “compatibility” cannot be a property of $(A,x)$ alone when the scientific question concerns intervention or recoverability; it must include at least the relevant input or output structure.

## Consensus assessment

- **Proposed grade:** C4 for scoped linear controllability, observability, and minimal realization.
- **Scoped consensus statement:** In linear systems, internal state directions differ in reachability and observability relative to specified input and output maps; input/output behavior determines only the controllable-observable part of a realization.
- **Reason for grade:** foundational theorem-level work with mature field consensus.
- **What remains disputed:** which realization best represents physical ontology, and which variables or measurements are scientifically privileged.

## Novelty implication for ARG

- the claim that a state’s role depends on how it sits within a transition-and-observation structure is established;
- state-only and structure-only summaries are known to be insufficient for intervention and inference;
- ARG must compare any compatibility quantity against controllability, observability, and minimal-realization theory;
- no general ARG novelty is established by rediscovering reachable or observable directions.

## Experiment decision

- **Is a new experiment needed?** no for the scoped linear result.
- **Exact unresolved question:** whether an ARG-specific quantity predicts behavior beyond standard controllability, observability, and realization measures in nonlinear or changing-structure systems.
- **Minimum discriminating experiment or proof:** compare against appropriate Gramians, rank tests, reachable sets, and observation maps on held-out systems.

## Required project updates

- [x] consensus table
- [x] translation dictionary
- [x] representation audit
- [x] novelty implications
- [ ] formalism revision after the full basket

## Reviewer check

- [x] Source supports the scoped claim.
- [x] Input/output relativity is explicit.
- [x] Mathematical results are not promoted into ontology.
- [x] Novelty implication follows from direct overlap.
