# CS1 Preliminary Translation Dictionary

## Status

> **PRELIMINARY — based on the first three source baskets.**

This dictionary records established meanings before ARG synthesis. Entries are not declarations that the terms are identical across fields.

## Mapping labels

- **Identity:** the same formal object under a declared mapping.
- **Exact translation:** equivalent formulations preserving the relevant structure.
- **Specialization:** one term is a restricted case of another.
- **Generalization:** one term covers a broader class.
- **Analogy:** structurally useful resemblance without identity.
- **Loose resemblance:** insufficient for a scientific bridge.

---

# State

## Dynamical systems

A point $x$ in a state space whose value, together with the evolution law and required inputs, determines future evolution.

## Control theory

An internal realization variable. State coordinates and even state dimension may vary across realizations; minimal realization removes input/output-inaccessible redundancy under stated linear assumptions.

## Adaptive networks

Usually includes node variables and may be augmented to include edge or topology variables.

## ARG implication

`State` is a role in a model, not automatically an invariant ontological category.

---

# Structure

## Linear dynamics

May refer to the operator $A$, invariant subspaces, spectral or singular-vector geometry, or the algebraic form of the system.

## Control theory

The scientific system description usually includes more than $A$:

$$
(A,B,C,D),
$$

where $B$ defines inputs and $C$ defines outputs.

## Adaptive networks

Topology, edge weights, or coupling rules may evolve and can be represented as additional state variables.

## ARG implication

Bare `structure` is under-typed. A claim must specify transition, input, output, constraint, metric, or relational structure.

---

# Transition law

A rule such as

$$
x_{t+1}=F(x_t)
$$

or

$$
\dot x=f(x,u)
$$

that determines admissible evolution.

It is not interchangeable with graph topology, causal structure, a conservation law, or an observed trajectory.

---

# Input or control map

## Linear control

The matrix $B$ in

$$
\dot x=Ax+Bu
$$

specifies how external control enters the state dynamics.

## Nonlinear control

Control vector fields $f_i(x)$ specify available intervention directions and may generate additional accessible directions through Lie brackets.

## ARG implication

Reachability cannot generally be inferred from $(A,x)$ or $(B_t,x_t)$ alone. The admissible input structure is part of the question.

---

# Output or observation map

## Linear control

The matrix $C$ in

$$
y=Cx+Du
$$

specifies which state distinctions affect measured outputs.

## Nonlinear control

An output function $h(x)$ and its Lie derivatives determine locally distinguishable state directions under scoped rank conditions.

## ARG implication

Recoverability and observational persistence require an observation map. They are not intrinsic properties of state coordinates alone.

---

# Controllability and reachability

## Linear systems

Controllability asks whether available inputs can move the system through the relevant state directions over a declared horizon.

## Nonlinear systems

Accessibility and controllability require local or global geometric definitions; Lie-generated distributions provide scoped criteria.

## Not equivalent to

- stability;
- persistence;
- observability;
- identity;
- causal importance without a declared intervention model.

---

# Observability

Whether distinct internal states can be distinguished from output histories under the declared dynamics and measurements.

## Not equivalent to

- visibility at one instant;
- controllability;
- ontological existence;
- semantic information;
- full recoverability under noise and finite data.

---

# Gramian

A matrix encoding a scoped energy geometry for a linear system.

- The controllability Gramian measures input-relative accessibility.
- The observability Gramian measures output-relative sensitivity.

A Gramian is not a universal compatibility tensor. It depends on the system, horizon or stability assumptions, coordinates, and input/output maps.

---

# Balanced realization

A linear coordinate representation in which controllability and observability Gramians are equal and diagonal.

The diagonal Hankel singular values rank directions by joint input/output importance.

## ARG implication

Balanced realization is an established precedent for a representation-aware state–system relation. It does not establish one universal state–structure compatibility measure.

---

# Constraint set

A declared subset $K$ of states or occurrences that are allowed, safe, feasible, or scientifically relevant.

A constraint set may represent physical exclusion, engineering safety, a model convention, or a target definition. These meanings must not be conflated.

---

# Viability

A state is viable relative to dynamics $F$ and constraint set $K$ when at least one admissible continuation remains in $K$.

$$
x_0\in\operatorname{Viab}_F(K)
$$

is an existential continuation statement. It is not the same as attraction or autonomous stability.

---

# Positive invariance

A set is positively invariant when all trajectories of the declared closed-loop or autonomous dynamics that start in it remain in it.

# Controlled invariance

A set is controlled invariant when an admissible control can be chosen to keep trajectories in it.

## Critical distinction

Autonomous preservation and preservation requiring ongoing correction are different mechanisms.

---

# Transport

A map or relation identifying states across changing spaces or structures.

Established forms include pushforward/pullback maps for smoothly evolving spaces. Reset maps, projections, remeshing, correspondences, and couplings cover other cases.

Transport is not automatically determined by source and destination spaces.

---

# Persistence

No unqualified cross-field definition is licensed.

Current typed forms include:

$$
P_{\mathrm{norm}},
P_{\mathrm{basin}},
P_{\mathrm{manifold}},
P_{\mathrm{retain}},
P_{\mathrm{structural}},
P_{\mathrm{viable}},
P_{\mathrm{invariant}},
P_{\mathrm{controlled}}.
$$

These are not assumed commensurable.

---

# Compatibility

## Current ARG status

A provisional umbrella term for a relation among a state, dynamics, structure, observables, controls, constraints, and horizon.

## Established neighboring quantities

- modal projection;
- finite-time propagator gain;
- singular-vector alignment;
- basin membership;
- invariant-manifold normal hyperbolicity;
- transfer-operator retention;
- accessibility distribution;
- observability codistribution;
- controllability and observability Gramians;
- Hankel singular values;
- viability-kernel membership;
- invariant-set membership.

## Current restriction

No evidence yet supports one universal compatibility scalar or invariant across these frameworks.

---

# Representation equivalence

Possible criteria include:

- equal input/output behavior;
- minimal realization equivalence;
- linear similarity;
- balanced representation;
- topological conjugacy;
- definitional equivalence;
- categorical equivalence;
- interpretational equivalence.

Each preserves different structure. None may be silently substituted for another.

---

# Preliminary context schema

A scientific claim may require a typed context such as

$$
\mathcal S=
(\mathcal X,F,B_{\mathrm{in}},C_{\mathrm{out}},K,\mathcal U,\mathcal W,\Phi,T).
$$

This records:

- state space $\mathcal X$;
- dynamics $F$;
- input map $B_{\mathrm{in}}$;
- output map $C_{\mathrm{out}}$;
- constraint set $K$;
- admissible controls $\mathcal U$;
- disturbances $\mathcal W$;
- measured functional $\Phi$;
- time horizon $T$.

It is a methodological typing aid, not a final ontology.

## Next dictionary expansion

The next baskets must add:

- connection and parallel transport;
- reset maps and hybrid state;
- gauge, quotient, and surplus structure;
- information, sufficient statistics, and causal states;
- biological function, homeostasis, lineage, and organizational closure;
- philosophical identity and persistence.
