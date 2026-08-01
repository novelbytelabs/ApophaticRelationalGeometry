# Literature Landscape

## Purpose

This document defines how ARG will ground its mathematical and scientific claims in primary research.

It is a search and evidence plan. It does not claim that the neighboring fields validate ARG.

## Current mechanism boundary

The current executable is $M_F$, the collective-feedback prototype. $M_P$ and $M_{FP}$ remain unimplemented.

Literature review must therefore distinguish:

- endogenous collective feedback;
- explicit projected admissibility;
- feedback under constraints;
- penalties and multiplier forces;
- adaptive geometry;
- claims of equivalence among these mechanisms.

## Source standards

Priority order:

1. original papers containing the relevant theorem, model, or experiment;
2. authoritative monographs or review articles for field structure;
3. official code and datasets linked by the authors;
4. independent reproductions;
5. secondary explanations only for orientation.

Technical claims cannot rest on summaries, social posts, or promotional pages.

## Research track 1: Collective variables and endogenous feedback

### Questions

- Which systems compute an order parameter, mean field, collective coordinate, or macrovariable and feed it back into constituent dynamics?
- When is that feedback merely a reparameterization of local interactions?
- How are organization dependence and counterfactual influence tested?
- Which models combine mean-field feedback with adaptive topology or metric variables?
- What mathematical conditions make the macrovariable dynamically informative rather than redundant?

### Search vocabulary

- mean-field feedback;
- order-parameter feedback;
- collective-coordinate dynamics;
- adaptive mean-field systems;
- macro-to-micro feedback;
- causal coarse-graining;
- slaving principle;
- synergetics;
- feedback through global observables.

### Project relevance

This track is the closest literature base for the current $M_F$ path

$$
x\to c(x)\to(\dot x,\dot s,\dot q).
$$

It tests whether the implemented mechanism is standard, reducible, or distinctive only through its coupling to adaptive relational geometry.

## Research track 2: Constrained nonlinear dynamics

### Questions

- When does projection onto a constraint manifold define a unique vector field?
- How are rank changes and nonsmooth boundaries handled?
- When is a projected ordinary differential equation equivalent to a differential-algebraic equation?
- What stabilization or retraction methods are needed numerically?
- How are constraint forces separated from unconstrained motion?

### Search vocabulary

- projected dynamical systems;
- tangent-cone dynamics;
- differential-algebraic equations;
- constrained Hamiltonian systems;
- Lagrange multipliers;
- SHAKE and RATTLE;
- viability theory;
- incompressible-flow projection.

### Project relevance

This track tests whether target $M_P$

$$
\dot Z=\Pi_{T_Z\mathcal M}F(Z)
$$

is standard constrained dynamics, a state-dependent extension, or ill-posed in the proposed regime.

## Research track 3: Feedback under constraints

### Questions

- Which models combine global feedback with holonomic, algebraic, or viability constraints?
- Does projection act on a proposal that already contains feedback?
- When do feedback and projection commute?
- What exact reductions recover feedback-only and projection-only models?
- Are there existing frameworks equivalent to target $M_{FP}$?

### Search vocabulary

- constrained feedback systems;
- projected control systems;
- mean-field differential-algebraic equations;
- feedback on manifolds;
- constrained adaptive control;
- projected gradient systems with global coupling.

### Project relevance

This track assesses whether $M_{FP}$ is already known and whether $M_F\equiv M_P$ can hold in any nontrivial domain.

## Research track 4: Adaptive and coevolving networks

### Questions

- Which systems jointly evolve node state and edge structure?
- When can adaptive weights be interpreted as geometry?
- What continuum, mean-field, or graph-limit results exist?
- Which behaviors require topology change rather than state change alone?
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

This track tests whether $s_e$ and $q_e$ add anything beyond ordinary dynamic edge weights.

## Research track 5: Local-to-global compatibility

### Questions

- How are local states glued into globally consistent assignments?
- Which sheaf or bundle structures allow nonlinear restriction maps?
- How are inconsistency and global sections quantified?
- Can restriction maps themselves evolve?
- How do sheaf Laplacians compare with ARG mismatch energies?

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

This track determines whether

$$
\delta_e
=
\rho_{ie}(x_i,\theta_i,c)
-
\rho_{je}(x_j,\theta_j,c)
$$

should be formalized as a sheaf, bundle, groupoid, or more general compatibility system.

## Research track 6: Dynamic discrete geometry

### Questions

- When does a weighted graph define a meaningful intrinsic metric?
- Which curvature notions remain stable under changing topology?
- How do graph Ricci flows and metric adaptation interact with node dynamics?
- What continuity results exist for time-dependent metric graphs?
- Which geometric quantities are invariant under presentation changes?

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

This track tests whether the implemented and target edge lengths define useful geometry rather than merely dynamic weights.

## Research track 7: Invariance and relational descriptions

### Questions

- What is the correct class of admissible presentation changes?
- Should the symmetry structure be a group, action, or groupoid?
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

This track makes “no privileged presentation” operational for each of $M_0,M_F,M_P,M_{FP}$.

## Research track 8: Singular barriers and noncollision

### Questions

- Under what conditions do singular potentials prevent collision?
- What bounds follow from conserved or dissipative energy?
- How do singularities affect existence and continuation?
- Can barrier forces be defined on intrinsic graph distances?
- When do numerical methods falsely cross a singular barrier?

### Search vocabulary

- singular interaction potentials;
- hard-core repulsion;
- collision avoidance;
- noncollision theorems;
- inverse-power potentials;
- barrier methods;
- singular ordinary differential equations.

### Project relevance

This track grounds any claim that

$$
U_{\mathrm{barrier}}
=
\sum_e\frac{B_e}{\ell_e^{p_e}}
$$

creates an unreachable finite-energy boundary.

## Research track 9: Physical anchor systems

### Constrained mechanics

Reason: constraint manifolds, multiplier forces, projection, and energy behavior can be checked against established solutions.

### Incompressible flow

Reason: a provisional local update followed by a global compatibility correction is mathematically and physically developed.

### Adaptive synchronization and flocking

Reason: local state, neighborhood structure, collective observables, and effective geometry interact.

For each anchor, reproduce a standard result before testing an ARG extension.

## Research track 10: Philosophical and interpretive neighbors

This track remains separate from mathematical validation.

Topics include:

- pluralistic monism;
- process ontology;
- relationalism;
- dependent origination;
- apophatic non-reification;
- limits of formal representation.

These sources may clarify interpretation. They cannot establish equations, implementation, novelty, or physical validity.

## Paper intake template

### Citation

Full bibliographic citation and persistent identifier.

### Source type

Original paper, review, monograph, code repository, dataset, or reproduction.

### Exact contribution

State the theorem, equation, algorithm, or result actually used.

### Assumptions

List mathematical, numerical, and physical assumptions.

### Mapping to ARG models

Map the source into one or more of:

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}.
$$

### Mechanism classification

Label each relevant term as:

- local dynamics;
- adaptive relation or metric;
- collective feedback;
- explicit projection;
- multiplier force;
- penalty;
- compatibility condition.

### Overlap

Identify what the source already contains.

### Difference

Identify what remains different without relying on terminology alone.

### Novelty implication

Record whether the source strengthens, narrows, or eliminates a candidate novelty claim.

### Reproducibility

Record code, data, parameters, and reproduction status.

### Open questions

List unresolved issues affecting ARG.

## Initial collection target

The first evidence set should contain at least:

- five primary sources on collective-variable or mean-field feedback;
- five on constrained or projected dynamics;
- three on systems combining feedback and constraints;
- five on adaptive networks;
- five on local-to-global or sheaf-based systems;
- five on dynamic discrete geometry;
- three on singular noncollision mechanisms;
- three physical anchor papers with reproducible equations or code.

The count is an intake target, not a substitute for quality.

## Completion criterion

This landscape is sufficient for the first novelty decision when:

1. every row in `09_novelty_matrix.md` has primary-source support;
2. the closest feedback, projection, and combined frameworks are reproduced in common notation;
3. equivalence and reparameterization have been actively tested;
4. unsupported novelty language has been removed;
5. the remaining candidate contribution can be stated precisely;
6. the current $M_F$ result is not used as evidence for unimplemented $M_P$ or $M_{FP}$.
