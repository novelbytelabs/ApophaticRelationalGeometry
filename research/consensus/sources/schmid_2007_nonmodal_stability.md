# Consensus Source Note — Schmid on Nonmodal Stability

## Citation

Peter J. Schmid. “Nonmodal Stability Theory.” *Annual Review of Fluid Mechanics* 39 (2007): 129–162. DOI: 10.1146/annurev.fluid.38.050304.092139.

## Source classification

- **Field:** applied mathematics and fluid mechanics
- **Subfield:** linear stability, non-normal dynamics, transient growth
- **Source type:** authoritative review
- **Publication status:** peer reviewed
- **Primary or secondary:** authoritative synthesis of a mature research program

## Exact contribution used

The review explains why eigenvalues alone do not determine finite-time disturbance behavior for non-normal linear operators. It formulates stability through the linear initial-value problem and surveys transient growth, optimal disturbances, pseudospectra, impulse response, transfer functions, and extensions to time-dependent, stochastic, nonlinear, and spatially complex systems.

The load-bearing result for CS1 is that realized finite-time amplification or decay depends jointly on the propagator and the orientation of the initial disturbance. Stable eigenvalues do not prevent substantial transient growth when eigenvectors are non-orthogonal, and different initial disturbances under the same operator may evolve very differently.

## Claim type

- established mathematical mechanism;
- authoritative field synthesis;
- application to hydrodynamic transition.

## Assumptions and domain

The basic nonmodal analysis concerns linearized initial-value problems and chosen norms or energy measures. Extensions and physical interpretations require additional assumptions specific to the flow, forcing, nonlinear terms, and observation horizon.

Nonmodal growth is not identical to long-term persistence, identity, biological function, or general metaphysical continuation.

## Evidence and verification status

- **Derivation or protocol:** operator and propagator analysis reviewed from the established literature.
- **Data or code available:** not assessed in this initial note.
- **Independent replication or reproduction:** the review summarizes a broad mathematical and experimental literature.
- **Known counterexamples or exceptions:** normal operators with orthogonal eigenvectors do not exhibit the same nonmodal mechanism under the corresponding norm.

## Established terminology

- linear initial-value problem;
- non-normal operator;
- transient growth;
- optimal disturbance;
- propagator;
- pseudospectrum;
- impulse response;
- transfer function.

## Mapping into ARG

### ARG claim IDs affected

- `CS1-C01`
- `CS1-C02`
- `CS1-C03`
- `CS1-C05`
- recent ERO-derived language concerning state–structure compatibility and destructive cancellation.

### Proposed mapping

| Source object | ARG object | Mapping type | What is preserved | What is not preserved |
|---|---|---|---|---|
| linear operator or propagator | relational transition structure | specialization | available amplification and decay directions | arbitrary nonlinear or ontological structure |
| initial disturbance | state | exact translation in linear models | activated combination of dynamical directions | identity or semantic content |
| optimal growth | persistence/amplification metric | partial translation | finite-time norm growth | all meanings of persistence |
| non-orthogonal modes | structural cancellation/amplification geometry | exact mathematical neighbor | state-dependent transient behavior | unique ARG mechanism |

## Equation or theorem mapping

For a linear initial-value problem,

$$
\dot x=Ax,
\qquad
x(t)=e^{tA}x_0.
$$

Finite-time amplification in a chosen norm is governed by the propagator:

$$
G(t)=\max_{x_0\neq0}
\frac{\|e^{tA}x_0\|^2}{\|x_0\|^2}.
$$

The realized outcome for a particular state is

$$
G(t;x_0)=
\frac{\|e^{tA}x_0\|^2}{\|x_0\|^2},
$$

which depends on the pair $(A,x_0)$.

### Mapping conditions

The exact mapping applies to a linearized system, a specified norm, and a fixed time horizon. It cannot by itself establish a universal persistence ontology.

## Cross-field implications

This literature directly supports the mathematical core of the claim that an operator alone does not determine one realized trajectory and that the same operator can amplify or suppress different states. It also shows that a simple dominant-eigenvector narrative can be inadequate for non-normal systems.

## Consensus assessment

- **Proposed grade:** C4 for the scoped linear-dynamical statement.
- **Scoped consensus statement:** In linear initial-value problems, finite-time behavior is a property of the propagator acting on the initial condition; for non-normal operators, state orientation can produce transient amplification or cancellation not captured by eigenvalues alone.
- **Reason for grade:** mature mathematical theory summarized in an authoritative review.
- **What remains disputed or open:** which norm, observable, time horizon, and nonlinear continuation are appropriate in a particular scientific system.

## Novelty implication for ARG

- the general state–operator interaction principle is established;
- destructive cancellation and mode-dependent persistence are not ARG discoveries;
- ARG may still offer a cross-field synthesis or a system-specific invariant, but that requires comparison beyond ordinary propagator and nonmodal analysis.

## Experiment decision

- **Is a new experiment needed?** no to establish that initial state and operator jointly determine finite-time linear behavior.
- **Exact unresolved question:** whether an ARG-specific compatibility quantity predicts outcomes in nonlinear, changing-structure systems beyond established propagator, basin, or transient-growth measures.
- **Minimum discriminating test:** compare the ARG quantity against standard modal, singular-vector, pseudospectral, and basin-based predictors on held-out systems.

## Required project updates

- [x] consensus table
- [x] translation dictionary
- [x] novelty matrix
- [x] disagreement map
- [ ] formal model revision after broader source audit

## Reviewer check

- [x] Source supports the scoped claim.
- [x] Claim type is correct.
- [x] Mapping is restricted to linear/nonmodal dynamics.
- [x] Novelty implication follows from direct conceptual and equation comparison.
