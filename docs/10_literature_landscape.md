# Literature Landscape

## Purpose

This document defines how the project will ground its mathematical and scientific claims in primary research.

It is a search and evidence plan. It does not yet claim that the listed neighboring fields validate the proposed geometry.

## Source standards

Priority order:

1. original papers containing the relevant theorem, model, or experiment;
2. authoritative monographs or review articles for field structure;
3. official code and datasets linked by the authors;
4. independent reproductions;
5. secondary explanations only for orientation.

For technical claims, summaries, social posts, and promotional pages are not sufficient evidence.

## Research track 1: Constrained nonlinear dynamics

### Questions

- When does projection onto a constraint manifold define a unique vector field?
- How are rank changes and nonsmooth boundaries handled?
- When is a projected ordinary differential equation equivalent to a differential-algebraic equation?
- What stabilization methods are needed under numerical integration?
- How are constraint forces separated from unconstrained motion?

### Search vocabulary

- projected dynamical systems;
- tangent-cone dynamics;
- differential-algebraic equations;
- constrained Hamiltonian systems;
- Lagrange multipliers;
- SHAKE and RATTLE methods;
- viability theory;
- incompressible-flow projection.

### Project relevance

This track tests whether

$$
\dot Z=\Pi_{T_Z\mathcal M}F(Z)
$$

is standard constrained dynamics, a state-dependent extension, or mathematically ill-posed in the proposed regime.

## Research track 2: Adaptive and coevolving networks

### Questions

- Which systems jointly evolve node state and edge structure?
- When can adaptive weights be interpreted as geometry?
- What continuum, mean-field, or graph-limit results exist?
- Which adaptive-network behaviors require topology change rather than state change alone?
- How is causality separated when state and topology update one another?

### Search vocabulary

- adaptive networks;
- coevolving networks;
- state-dependent graphs;
- temporal graphs;
- adaptive synchronization;
- dynamic graph Laplacians;
- network rewiring;
- graph limits for adaptive systems.

### Project relevance

This track tests whether the variables $s_e$ and $q_e$ add anything beyond ordinary dynamic edge weights.

## Research track 3: Local-to-global compatibility

### Questions

- How are local states glued into globally consistent assignments?
- Which sheaf or bundle structures allow nonlinear restriction maps?
- How are inconsistency and global sections quantified?
- Can the restriction maps themselves evolve?
- How do sheaf Laplacians compare with the proposed coherence energy?

### Search vocabulary

- cellular sheaves;
- sheaf Laplacians;
- global sections;
- nonlinear sheaves;
- vector bundles on graphs;
- distributed consensus;
- compatibility complexes;
- local-to-global obstruction.

### Project relevance

This track determines whether the mismatch maps

$$
\delta_e
=
\rho_{ie}(x_i,\theta_i,c)
-
\rho_{je}(x_j,\theta_j,c)
$$

should be formalized as a sheaf, bundle, groupoid, or more general compatibility system.

## Research track 4: Dynamic discrete geometry

### Questions

- When does a weighted graph define a meaningful intrinsic metric?
- Which discrete curvature notions remain stable under changing topology?
- How do graph Ricci flows and metric adaptation interact with node dynamics?
- What continuity results exist for time-dependent metric graphs?
- Which geometric quantities are invariant under graph presentation changes?

### Search vocabulary

- metric graphs;
- dynamic metric spaces;
- Forman curvature;
- Ollivier curvature;
- graph Ricci flow;
- weighted shortest-path geometry;
- evolving metric-measure spaces;
- discrete differential geometry.

### Project relevance

This track tests whether the proposed edge lengths define genuine geometry and whether curvature supplies useful observables.

## Research track 5: Invariance and relational descriptions

### Questions

- What is the correct class of admissible presentation changes?
- Should the symmetry structure be a group, group action, or groupoid?
- Which observables descend to quotient descriptions?
- How should topology-changing systems be compared under relabeling?
- What distinguishes gauge redundancy from physical symmetry?

### Search vocabulary

- equivariant dynamical systems;
- gauge invariance;
- quotient configuration spaces;
- groupoid symmetry;
- graph isomorphism invariance;
- relational mechanics;
- coordinate-free dynamics.

### Project relevance

This track makes the phrase “no privileged presentation” mathematically operational.

## Research track 6: Singular barriers and non-collision

### Questions

- Under what conditions do singular potentials prevent collision?
- What bounds follow from finite conserved or dissipative energy?
- How do singularities affect existence and continuation?
- Can barrier forces be defined on intrinsic graph distances?
- When do numerical methods falsely cross a singular barrier?

### Search vocabulary

- singular interaction potentials;
- hard-core repulsion;
- collision avoidance;
- non-collision theorems;
- inverse-power potentials;
- barrier methods;
- singular ordinary differential equations.

### Project relevance

This track grounds the claim that

$$
U_{\mathrm{barrier}}
=
\sum_e\frac{B_e}{\ell_e^{p_e}}
$$

creates an unreachable finite-energy boundary.

## Research track 7: Physical anchor systems

Initial anchor families:

### Incompressible flow

Reason: a local provisional update followed by a global compatibility correction is already physically meaningful and mathematically developed.

### Constrained mechanics

Reason: constraint manifolds, multiplier forces, and energy behavior can be checked exactly.

### Adaptive synchronization and flocking

Reason: local state, neighborhood structure, and effective geometry genuinely interact.

For each anchor, the project must first reproduce a standard result before testing an extension.

## Research track 8: Philosophical and interpretive neighbors

This track is kept separate from mathematical validation.

Topics include:

- pluralistic monism;
- process ontology;
- relationalism;
- dependent origination;
- apophatic non-reification;
- limits of formal representation.

These sources may clarify interpretation. They cannot establish the equations or physical validity of the model.

## Paper intake template

Each source note must use the following structure.

### Citation

Full bibliographic citation and persistent identifier.

### Source type

Original paper, review, monograph, code repository, dataset, or reproduction.

### Exact contribution

State the theorem, equation, algorithm, or result actually used.

### Assumptions

List mathematical, numerical, and physical assumptions.

### Mapping to project notation

Map source variables and equations into the project formalism where possible.

### Overlap

Identify what the source already contains.

### Difference

Identify what remains different without relying on terminology alone.

### Novelty implication

Record whether the source strengthens, narrows, or eliminates a candidate novelty claim.

### Reproducibility

Record code, data, parameter settings, and whether reproduction has been attempted.

### Open questions

List unresolved issues that affect this project.

## Initial collection target

The first evidence set should contain at least:

- five primary sources on constrained or projected dynamics;
- five on adaptive networks;
- five on local-to-global or sheaf-based systems;
- five on discrete evolving geometry;
- three on singular non-collision mechanisms;
- three physical anchor papers with reproducible equations or code.

The count is an intake target, not a quality substitute.

## Completion criterion

This landscape is complete enough for the first novelty decision when:

1. every row in `09_novelty_matrix.md` has primary-source support;
2. the three closest frameworks have been reproduced in common notation;
3. equivalence and reparameterization have been actively tested;
4. unsupported novelty language has been removed;
5. the remaining candidate contribution can be stated in one precise paragraph.
