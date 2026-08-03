# CS1 — State, Structure, Representation, and Persistence

## Status

> **ACTIVE — literature and consensus audit only.**

Three source baskets are entered:

1. initial-value dynamics, adaptive structure, evolving spaces, and equivalence;
2. nonlinear persistence;
3. controllability, observability, model reduction, viability, and invariance.

No new state–structure principle, persistence law, transport formalism, or novelty claim is licensed by this document.

## Governing question

> **What is already established across mathematics, physics, dynamical systems, control, computer science, biology, and philosophy about the roles of state, structure, transition rule, representation, and persistence?**

The purpose is to identify the minimal cross-field consensus, preserve genuine disagreement, and isolate only the unresolved remainder.

## Why this slice comes first

Recent ARG discussion used statements such as:

> Persistence depends on compatibility between the relational structure and the state moving through it.

That may be useful umbrella language, but its mathematical core overlaps established ideas including initial-condition dependence, modal projection, invariant subspaces, basin structure, transient growth, controllability, observability, adaptive networks, viability, invariant sets, and representation equivalence.

CS1 must determine exactly what is standard, what is perspective-relative, what is interpretive, and whether any ARG-specific contribution remains.

---

# Atomic claim inventory

Grades below reflect the current provisional evidence and remain subject to full CS1 review.

| ID | Atomic claim to audit | Claim type | Current provisional status |
|---|---|---|---|
| CS1-C01 | A realized trajectory depends jointly on a transition rule and an initial state. | Mathematical | C4 within specified dynamical models |
| CS1-C02 | The same transition structure can preserve, suppress, amplify, or transform different states. | Mathematical/dynamical | C4 in modal and nonmodal dynamics |
| CS1-C03 | Linear finite-time behavior, control energy, and output sensitivity depend on propagator and Gramian geometry relative to declared inputs, outputs, norms, and horizons. | Mathematical | C4 |
| CS1-C04 | In nonlinear systems, persistence and accessibility may depend on basin location, invariant and almost-invariant sets, manifolds, local generated directions, and viability regions. | Mathematical/dynamical | C4 within distinct scoped theories |
| CS1-C05 | State–system interaction is already decomposed into reachability, observability, joint input/output importance, accessibility, viability, and controlled invariance. | Statistical/mechanistic | C4 in scoped control theories |
| CS1-C06 | The boundary between state, structure, parameters, rule, and environment can depend on model representation. | Modeling/philosophical | C4 for linear realization redundancy; C3 more broadly |
| CS1-C07 | Dynamically or observationally equivalent formulations can move or remove internal variables without changing specified behavior. | Mathematical/philosophical | C3–C4, criterion-dependent |
| CS1-C08 | Meaningful compatibility claims require invariance or known covariance under admissible re-representations. | Mathematical/methodological | C3–C4, criterion-dependent |
| CS1-C09 | When structure changes and state spaces differ, cross-time comparison requires transport, projection, reset, or correspondence. | Mathematical | C4 for scoped evolving-space frameworks; broader basket pending |
| CS1-C10 | Source and destination spaces alone may not uniquely determine transport or preservation semantics. | Mathematical/philosophical | C3–C4 within audited frameworks; broader basket pending |
| CS1-C11 | Energy, basin return, manifold continuation, ensemble retention, reachability, observability, viability, invariance, function, recoverability, and identity are inequivalent notions. | Conceptual/scientific | C4 within audited mathematics; other fields pending |
| CS1-C12 | A persistence criterion is relative to specified observables, inputs, outputs, controls, constraints, disturbances, equivalences, and time scales. | Methodological/philosophical | C3–C4 |
| CS1-C13 | ARG's `state–structure compatibility` is a useful unifying diagnostic or schema across multiple established frameworks. | Synthesis claim | C1; only a typed umbrella is presently supported |
| CS1-C14 | ARG's synthesis yields a representation-robust prediction or theorem not already available in neighboring frameworks. | Candidate novelty | C0 and unlicensed |

---

# Current correction to the formal problem

A purely autonomous model may use

$$
Q_t=(B_t,x_t),
\qquad
x_{t+1}=F_{B_t}(x_t).
$$

But the control-theory basket establishes that many scientific questions require more context. A preliminary typed context is

$$
\mathcal S=
(\mathcal X,F,B_{\mathrm{in}},C_{\mathrm{out}},K,\mathcal U,\mathcal W,\Phi,T).
$$

This includes the state space, transition law, input map, output map, constraints, admissible controls, disturbances, measured functional, and horizon.

This is a methodological typing result. It does not establish a new ontology.

---

# Field map

## Linear dynamics and spectral theory

Entered:

- eigenmode and generalized-eigenmode dependence;
- non-normal transient growth;
- propagator and singular-vector analysis;
- destructive interference and cancellation;
- asymptotic versus finite-time behavior.

## Nonlinear dynamical systems

Entered:

- attractors and basins;
- invariant manifolds;
- metastability and almost-invariant sets;
- structural stability.

Still required:

- slow manifolds and singular perturbation;
- bifurcation;
- trajectory-dependent local contraction;
- noise-driven escape.

## Control theory

Entered:

- controllability and observability;
- state-transition operators and Gramians;
- balanced realization and model reduction;
- nonlinear accessibility and observability;
- viability kernels;
- positive, robust, and controlled invariance.

Still required:

- switched and hybrid control;
- stochastic viability;
- practical computational limits in changing structures.

## Evolving spaces and hybrid systems

Entered:

- pushforward and pullback;
- evolving Hilbert/Banach spaces.

Next basket:

- connections and parallel transport;
- reset maps and reset relations;
- remeshing and conservative projection;
- dimension-changing systems.

## Adaptive, temporal, and graph-based systems

Entered:

- coevolving state and topology.

Still required:

- graph signals on time-varying graphs;
- dynamic graph Laplacians;
- sheaves and local-to-global consistency;
- graph matching and optimal transport;
- node-label and quotient invariance.

## Computation, machine learning, and information

Still required:

- hidden state versus parameters;
- recurrent memory and state-space models;
- sufficient statistics and causal states;
- information preservation and recoverability;
- architecture–input interaction.

## Biology and systems science

Still required:

- organizational persistence;
- homeostasis and allostasis;
- developmental and lineage continuity;
- structure–function relationships;
- multiscale organization;
- turnover with maintained identity.

## Philosophy

Entered in part:

- theoretical equivalence criteria.

Still required:

- persistence and identity through change;
- structural realism;
- process ontology;
- scientific perspectivism and pluralism;
- gauge, representation, and underdetermination;
- criteria of objecthood and continuity.

---

# Translation hazards

The following terms must not be treated as automatically equivalent:

- mathematical state / physical state / epistemic state;
- graph structure / transition structure / input structure / output structure / constraint structure;
- invariant mode / reachable direction / observable direction / stable pattern / persistent identity;
- constraint / cause / control / law / boundary condition;
- information / observability / entropy / semantic content / recoverability;
- transport / physical motion / identity continuation;
- representation dependence / observer dependence / subjectivity;
- autonomous invariance / controlled invariance / attraction / viability.

Every proposed bridge must identify the exact relation among the terms.

---

# Required outputs

CS1 is complete only when it produces:

1. **Consensus table** — active and provisional.
2. **Translation dictionary** — active and provisional.
3. **Disagreement map** — pending.
4. **Representation audit** — pending.
5. **Novelty decision** — pending completion of source baskets.
6. **Residual agenda** — pending.
7. **Claim-ledger amendments** — pending independent review.
8. **Formalism impact note** — preliminary typed-context correction entered; final note pending.

---

# Stop rules

Stop a proposed novelty or experiment when:

- the claim is already a standard theorem or repeatedly demonstrated mechanism;
- ARG merely renames an established quantity;
- the proposed experiment reproduces a known qualitative result without testing an extension;
- equivalent representations make the claim arbitrary and no admissible gauge class is specified;
- different fields use the same word for non-equivalent objects;
- the evidence underdetermines interpretation and no discriminating test exists.

In those cases, cite and synthesize the established result.

---

# Exit gate

CS1 passes only when an independent reviewer can trace every consensus statement to its source notes and verify that:

- no C0–C2 statement entered the Minimal ARG Core;
- disagreements were not erased;
- standard results were not relabeled as ARG discoveries;
- experiments are proposed only for a precise unresolved residual;
- the formalism and public language are aligned with the findings.

## Immediate action

Proceed with the transport-and-structural-change basket:

1. connections and parallel transport;
2. hybrid reset maps and reset relations;
3. remeshing and conservative projection;
4. graph correspondence and optimal transport;
5. dimension-changing and noninvertible transitions.

Do not revise the ontology or propose a transport experiment until this basket and the associated representation audit are complete.
