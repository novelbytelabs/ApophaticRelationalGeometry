# Consensus Source Note — Smale on Structural Stability

## Citation

Stephen Smale. “Differentiable Dynamical Systems.” *Bulletin of the American Mathematical Society* 73, no. 6 (1967): 747–817. DOI: 10.1090/S0002-9904-1967-11798-1.

## Source classification

- **Field:** mathematics
- **Subfield:** global analysis, differentiable dynamical systems, hyperbolicity, structural stability
- **Source type:** foundational survey and theorem synthesis containing primary results and research program
- **Publication status:** peer reviewed
- **Primary or secondary:** primary foundational source

## Exact contribution used

Smale formulates qualitative equivalence of dynamical systems through topological conjugacy and identifies the associated robustness notion as **structural stability**. In the same work he develops the hyperbolic framework, including Axiom A, stable and unstable manifolds, spectral decomposition, and the structural stability of Anosov systems.

The paper also records a crucial limitation: structurally stable diffeomorphisms are not dense in the full space of diffeomorphisms. Structural stability is therefore an important conditional property, not a universal fact about dynamical systems.

The load-bearing result for CS1 is that “persistence of behavior when the governing structure changes slightly” already has a rigorous meaning: a perturbed system may remain topologically conjugate to the original, preserving its qualitative orbit structure even though coordinates and individual trajectories change.

## Claim type

- mathematical definition;
- theorem and theorem synthesis;
- foundational research framework.

## Assumptions and domain

- differentiable maps or flows on manifolds;
- a declared topology on the space of systems, commonly a $C^r$ topology;
- equivalence by topological conjugacy or, for flows, an explicitly stated orbit equivalence;
- hyperbolicity and related hypotheses for the strongest stability results.

Structural stability does not mean numerical closeness of every trajectory, identity of state variables, or preservation under arbitrary large or discontinuous changes.

## Evidence and verification status

- **Derivation or protocol:** definitions, propositions, theorems, and synthesis of the hyperbolic program.
- **Data or code available:** not applicable.
- **Independent replication or reproduction:** foundational results in a mature mathematical field.
- **Known counterexamples or exceptions:** Smale explicitly notes that structurally stable systems are not dense; nonhyperbolic systems can change qualitative behavior under arbitrarily small perturbations.

## Established terminology

- topological conjugacy;
- structural stability;
- hyperbolic set;
- Axiom A;
- nonwandering set;
- stable and unstable manifolds;
- spectral decomposition;
- Anosov diffeomorphism.

## Mapping into ARG

### ARG claim IDs affected

- `CS1-C06`
- `CS1-C07`
- `CS1-C08`
- `CS1-C11`
- `CS1-C12`
- ARG language concerning persistence under structural change and representation invariance.

### Proposed mapping

| Source object | ARG object | Mapping type | What is preserved | What is not preserved |
|---|---|---|---|---|
| dynamical system $f$ | structured transition law | specialization | orbit-generating rule | complete ontology or environment |
| nearby system $g$ | changed structure/rule | specialization | perturbation in a declared topology | arbitrary structural mutation |
| conjugacy $h$ | representation/continuation map | exact mathematical neighbor | qualitative orbit structure | metric distances and state labels |
| structural stability | persistence of qualitative dynamics | specialization | equivalence class under perturbation | persistence of one state or material object |

## Equation or theorem mapping

Two maps $f,g:M\rightarrow M$ are topologically conjugate when there is a homeomorphism $h:M\rightarrow M$ such that

$$
h\circ f = g\circ h.
$$

A system $f$ is structurally stable in a declared function-space topology when every sufficiently nearby system $g$ is topologically conjugate to $f$.

In ARG notation, the relevant persistence claim is not

$$
Q_t \approx Q_{t+1},
$$

but rather the existence of an equivalence map between two transition systems:

$$
h\circ F_B = F_{B'}\circ h.
$$

### Mapping conditions

The state spaces, topology of perturbations, regularity class, and equivalence criterion must be specified. A conjugacy preserves orbit structure, not every metric, observable, causal interpretation, or state–structure decomposition.

## Cross-field implications

Structural stability provides a precise bridge between mathematics and philosophy of representation: two systems may count as qualitatively the same because their dynamical organization is conjugate, even when their coordinates differ. Physics may demand preservation of additional observables, measures, symplectic structure, or causal interpretation; topological conjugacy alone need not be sufficient.

## Consensus assessment

- **Proposed grade:** C4 for the scoped mathematical definitions and hyperbolic stability results.
- **Scoped consensus statement:** Qualitative dynamical behavior can persist under small perturbations when the original and perturbed systems are related by an appropriate conjugacy; such structural stability requires explicit hypotheses and is not universal.
- **Reason for grade:** foundational primary source and mature subsequent theory.
- **What remains disputed:** which equivalence relation and preserved observables are scientifically appropriate for a given ARG application.

## Novelty implication for ARG

- persistence of qualitative behavior under changes to the governing dynamics is established;
- ARG’s gauge problem is a specialization of the broader problem of equivalence and conjugacy between dynamical representations;
- ARG must state what additional relational, metric, probabilistic, or causal structure its admissible maps preserve.

## Experiment decision

- **Is a new experiment needed?** no to establish structural stability or conjugacy as a general concept.
- **Exact unresolved question:** which ARG models are conjugate, orbit-equivalent, observationally equivalent, or inequivalent under admissible re-representations.
- **Why existing results do not already answer it:** ARG has not defined the relevant transformation class or proved model-specific conjugacies.
- **Minimum discriminating experiment or proof:** define the admissible category and prove a commuting relation or construct a counterexample; numerical trajectory similarity alone is insufficient.

## Required project updates

- [x] consensus table
- [x] translation dictionary
- [x] novelty matrix
- [x] disagreement map
- [ ] formalism after the equivalence basket

## Reviewer check

- [x] Source supports the scoped claim.
- [x] Claim type is correct.
- [x] Mapping does not conflate conjugacy with identity.
- [x] Consensus grade is justified.
- [x] Proposed work is genuinely residual and model-specific.
