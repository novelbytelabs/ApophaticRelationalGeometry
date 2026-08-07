# Literature Landscape

## Purpose

This document defines how ARG grounds mathematical, scientific, and interpretive claims in primary research.

It is a search and evidence plan. Neighboring fields do not validate ARG merely by resemblance.

## Current mechanism boundary

All four contract-v1.0 prototypes are implemented and unit-tested:

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

Implementation makes direct equation comparison possible. It does not establish novelty or scientific adequacy.

## Current CS1 boundary

Three source baskets are entered:

1. initial-value dynamics, adaptive networks, evolving spaces, and equivalence;
2. nonlinear persistence;
3. controllability, observability, model reduction, viability, and invariance.

Current evidence supports a typed family of state–system relations, not one universal compatibility or persistence scalar.

## Source standards

Priority order:

1. original paper containing the relevant theorem, model, or experiment;
2. authoritative monograph or review for field structure;
3. official code and datasets linked by authors;
4. independent reproductions and critiques;
5. secondary explanations only for orientation.

Technical claims cannot rest on summaries, social posts, promotional pages, or unsupported model paraphrases.

---

# Research track 1: initial-value, modal, and nonmodal dynamics

## Questions

- How do operator, propagator, initial state, norm, and horizon determine finite-time behavior?
- When do eigenvalues fail to predict transient growth or cancellation?
- Which quantities are coordinate invariant?
- How do modal and singular-vector analyses differ?

## Entered sources

- Schmid 2007.

## ARG implication

General state–operator dependence and destructive cancellation are established.

---

# Research track 2: nonlinear persistence

## Questions

- How do basins determine robustness to large perturbations?
- Under what conditions do invariant manifolds persist?
- How are metastability and leakage measured?
- Which dynamics are structurally stable under perturbation?
- How do slow manifolds, bifurcations, and noise alter persistence?

## Entered sources

- Menck et al. 2013;
- Fenichel 1971/72;
- Froyland and Padberg 2009;
- Smale 1967.

## ARG implication

Persistence is not one quantity. Basin return, manifold continuation, ensemble retention, and structural stability are distinct.

---

# Research track 3: controllability, observability, and realization

## Questions

- Which state directions are reachable through declared inputs?
- Which state distinctions are recoverable through declared outputs?
- What does a minimal realization preserve?
- Which state directions are jointly important for input/output behavior?
- How do nonlinear accessibility and observability differ from linear rank conditions?

## Entered sources

- Kalman 1963;
- Moore 1981;
- Hermann and Krener 1977.

## ARG implication

The scientific role of a state depends on dynamics, inputs, outputs, and horizon. A bare pair $(B,x)$ is often insufficient.

---

# Research track 4: viability and set invariance

## Questions

- Which states admit at least one constrained continuation?
- Which sets are preserved autonomously?
- Which sets can be preserved only through feedback?
- How do robustness and disturbance classes change invariance?
- How does projection relate to viability and controlled invariance?

## Entered sources

- Saint-Pierre 1994;
- Blanchini 1999.

## ARG implication

Autonomous persistence, viable continuation, and controlled persistence are distinct established concepts.

---

# Research track 5: transport and structural change — next

## Questions

- When does a connection determine parallel transport?
- Which axioms make path transport equivalent to a connection?
- How are states transferred across discrete mode changes?
- How do reset maps handle dimension changes, merges, and splits?
- How is conservation enforced during remeshing?
- When identity is unknown, what does optimal transport or graph correspondence recover?
- Which transitions are invertible, many-to-one, one-to-many, or relation-valued?

## Search vocabulary

- connection and parallel transport;
- transport functor;
- vector bundle connection;
- hybrid reset map;
- reset relation;
- dimension-varying hybrid systems;
- remeshing projection;
- conservative interpolation;
- arbitrary Lagrangian–Eulerian remap;
- graph matching;
- Gromov–Wasserstein;
- fused Gromov–Wasserstein;
- graph signal transfer;
- topology-changing dynamics.

## Required output

Classify each transport as:

- canonical from supplied physical identity;
- selected modeling structure;
- inferred correspondence;
- nonunique relation;
- impossible without additional semantics.

---

# Research track 6: collective variables and endogenous feedback

## Questions

- Which systems compute a macrovariable and feed it into constituent dynamics?
- When is that feedback reducible to local interactions?
- How are organization dependence and counterfactual influence tested?
- Which models combine feedback with adaptive topology or metric variables?

## ARG relevance

This track audits

$$
x\to c(x)\to(\dot x,\dot s,\dot q)
$$

in $M_F$ and $M_{FP}$.

---

# Research track 7: constrained nonlinear dynamics

## Questions

- When does projection onto a constraint manifold define a unique vector field?
- How are rank changes and nonsmooth boundaries handled?
- When is a projected ODE equivalent to a DAE?
- How do retraction, viability, and controlled invariance differ?

## ARG relevance

This track audits

$$
\dot Z=\Pi_{T_Z\mathcal M}F(Z)
$$

and radial retraction against established constrained dynamics.

---

# Research track 8: feedback under constraints

## Questions

- Which models combine global feedback with algebraic or viability constraints?
- When do feedback and projection commute?
- What reductions recover feedback-only and projection-only models?
- Are existing frameworks equivalent to $M_{FP}$?

---

# Research track 9: adaptive and coevolving networks

## Questions

- Which systems jointly evolve node state and edge structure?
- When can adaptive weights be interpreted as geometry?
- Which behaviors require topology change rather than augmented state dynamics?
- How is causality separated when state and topology update one another?

## Entered source

- Gross and Blasius 2008.

---

# Research track 10: local-to-global compatibility

## Questions

- How are local states glued into globally consistent assignments?
- Which sheaf or bundle structures allow nonlinear restrictions?
- How are inconsistency and global sections quantified?
- Can restriction maps evolve?

## ARG relevance

This track determines whether mismatch terms should be formalized through sheaves, bundles, groupoids, or more general compatibility systems.

---

# Research track 11: dynamic discrete geometry

## Questions

- When does a weighted graph define meaningful intrinsic geometry?
- Which curvature notions remain stable under changing topology?
- How do metric adaptation and node dynamics interact?
- Which geometric quantities survive presentation changes?

---

# Research track 12: invariance, gauge, and relational descriptions

## Questions

- What is the correct class of admissible presentation changes?
- Should the symmetry structure be a group, action, groupoid, or category?
- Which observables descend to quotient descriptions?
- What distinguishes gauge redundancy, coordinate change, physical symmetry, conjugacy, and input/output equivalence?

## Entered sources

- Weatherall 2019;
- Smale 1967;
- Kalman 1963;
- Moore 1981.

---

# Research track 13: information and recoverability

## Questions

- How do observability and information differ?
- What is a sufficient statistic?
- What are causal states and predictive equivalence classes?
- Which information measures are invariant under recoding?
- How are recoverability and semantic function distinguished?

---

# Research track 14: biological organization and persistence

## Questions

- How do organisms maintain organization under material turnover?
- What distinguishes homeostasis, allostasis, development, lineage, repair, and functional persistence?
- Which structural changes preserve biological identity?
- How are multiscale constraints measured experimentally?

---

# Research track 15: singular barriers and noncollision

## Questions

- Under what conditions do singular potentials prevent collision?
- What bounds follow from conserved or dissipative energy?
- Can barriers be defined on intrinsic graph distances?
- When do numerical methods falsely cross singular boundaries?

---

# Research track 16: physical anchors

## Constrained mechanics

Constraint manifolds, multiplier forces, projection, viability, and energy behavior can be checked against established solutions.

## Incompressible flow

A local update followed by a global compatibility correction is mathematically and physically developed.

## Adaptive synchronization and flocking

Local state, neighborhood structure, collective observables, and effective geometry interact.

For each anchor, reproduce a standard result before testing an ARG extension.

---

# Research track 17: philosophical and interpretive neighbors

This track remains separate from mathematical validation.

Topics include:

- identity through change;
- pluralistic monism;
- process ontology;
- structural realism;
- dependent origination;
- scientific perspectivism;
- gauge and underdetermination;
- apophatic non-reification;
- limits of formal representation.

These sources clarify interpretation. They cannot establish equations, implementation, novelty, or physical validity.

---

# Paper intake template

Every note must include:

- full citation and stable identifier;
- source type;
- exact result used;
- assumptions and excluded cases;
- original terminology;
- mapping into ARG;
- equation or theorem mapping;
- consensus grade;
- novelty implication;
- experiment decision;
- required project updates.

Use `research/consensus/source_note_template.md`.

---

# Completion criterion

The landscape is sufficient for a first novelty decision when:

1. every load-bearing claim has primary-source support;
2. the closest feedback, projection, transport, control, and combined frameworks are represented in common notation;
3. equivalence and reparameterization are actively tested;
4. unsupported novelty language is removed;
5. the remaining contribution can be stated precisely;
6. software implementation is not presented as scientific novelty;
7. experiments are proposed only for a residual not answered by consensus.

## Immediate action

Complete research track 5: transport and structural change.
