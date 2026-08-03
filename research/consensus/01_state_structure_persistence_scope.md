# CS1 — State, Structure, Representation, and Persistence

## Status

> **ACTIVE — literature and consensus audit only.**

No new state–structure principle, persistence law, transport formalism, or novelty claim is licensed by this document.

## Governing question

> **What is already established across mathematics, physics, dynamical systems, control, computer science, biology, and philosophy about the roles of state, structure, transition rule, representation, and persistence?**

The purpose is to identify the minimal cross-field consensus, preserve genuine disagreement, and isolate only the unresolved remainder.

## Why this slice comes first

Recent ARG discussion used statements such as:

> Persistence depends on compatibility between the relational structure and the state moving through it.

That may be useful language, but its mathematical core overlaps established ideas including initial-condition dependence, modal projection, invariant subspaces, basin structure, transient growth, controllability, observability, adaptive networks, and representation equivalence.

CS1 must determine exactly what is standard, what is perspective-relative, what is interpretive, and whether any ARG-specific contribution remains.

---

# Atomic claim inventory

All grades below are **pending** until supported by completed source notes.

| ID | Atomic claim to audit | Claim type | Initial threat of prior establishment |
|---|---|---|---|
| CS1-C01 | A realized trajectory depends jointly on a transition rule and an initial state. | Mathematical | Very high |
| CS1-C02 | The same transition structure can preserve, suppress, amplify, or transform different states. | Mathematical/dynamical | Very high |
| CS1-C03 | Persistence in linear systems depends on a state's projection into persistent invariant or modal subspaces. | Mathematical | Very high |
| CS1-C04 | In nonlinear systems, persistence may depend on basin location, slow manifolds, local contraction, and trajectory-dependent alignment. | Mathematical/dynamical | Very high |
| CS1-C05 | State–structure interaction may predict behavior beyond state-only or structure-only summaries. | Statistical/mechanistic | High; scope-dependent |
| CS1-C06 | The boundary between state, structure, parameters, rule, and environment can depend on model representation. | Modeling/philosophical | High |
| CS1-C07 | Dynamically equivalent formulations can move variables between state and structure without changing observables. | Mathematical/philosophical | High |
| CS1-C08 | Meaningful compatibility claims require invariance or known covariance under admissible re-representations. | Mathematical/methodological | High |
| CS1-C09 | When structure changes and state spaces differ, cross-time comparison requires a transport, projection, reset, or correspondence rule. | Mathematical | Very high |
| CS1-C10 | The source and destination spaces alone may not uniquely determine transport. | Mathematical/philosophical | Very high |
| CS1-C11 | Energy, shape, information, function, recoverability, and identity are inequivalent notions of persistence. | Conceptual/scientific | Very high |
| CS1-C12 | A criterion of persistence is always relative to specified observables, equivalences, and time scales. | Methodological/philosophical | High |
| CS1-C13 | ARG's `structure–state compatibility` is a useful unifying diagnostic across multiple established frameworks. | Synthesis claim | Open |
| CS1-C14 | ARG's synthesis yields a representation-robust prediction or theorem not already available in neighboring frameworks. | Candidate novelty | Open and unlicensed |

---

# Field map

## Linear dynamics and spectral theory

Audit:

- eigenmode and generalized-eigenmode decomposition;
- invariant subspaces;
- non-normal transient growth;
- pseudospectra;
- destructive interference and cancellation;
- asymptotic versus finite-time persistence.

## Nonlinear dynamical systems

Audit:

- attractors and basins;
- invariant and slow manifolds;
- Lyapunov stability;
- local Jacobian directions;
- bifurcation and metastability;
- structural stability.

## Control theory

Audit:

- controllability and observability;
- state-transition operators;
- Gramians;
- model reduction;
- viability and invariant sets;
- state-dependent and switched systems.

## Evolving spaces and hybrid systems

Audit:

- pushforward and pullback;
- connections and parallel transport;
- evolving Hilbert/Banach spaces;
- reset maps and reset relations;
- remeshing and conservative projection;
- dimension-changing systems.

## Adaptive, temporal, and graph-based systems

Audit:

- coevolving state and topology;
- graph signals on time-varying graphs;
- dynamic graph Laplacians;
- sheaves and local-to-global consistency;
- graph matching and optimal transport;
- representation and node-label invariance.

## Computation, machine learning, and information

Audit:

- hidden state versus parameters;
- recurrent memory and state-space models;
- representation equivalence;
- sufficient statistics and causal states;
- information preservation and recoverability;
- architecture–input interaction.

## Biology and systems science

Audit:

- organizational persistence;
- homeostasis and allostasis;
- developmental and lineage continuity;
- structure–function relationships;
- multiscale organization;
- turnover with maintained identity.

## Philosophy

Audit:

- persistence and identity through change;
- structural realism and ontic structural realism;
- process ontology;
- dispositional and powers accounts;
- scientific perspectivism and pluralism;
- gauge, representation, and underdetermination;
- criteria of objecthood and continuity.

---

# Translation hazards

The following terms must not be treated as automatically equivalent:

- mathematical state / physical state / epistemic state;
- graph structure / geometric structure / causal structure / organizational structure;
- invariant mode / stable pattern / persistent identity;
- constraint / cause / law / boundary condition;
- information / entropy / semantic content / recoverability;
- transport / physical motion / identity continuation;
- representation dependence / observer dependence / subjectivity.

Every proposed bridge must identify the exact relation among the terms.

---

# Required outputs

CS1 is complete only when it produces:

1. **Consensus table** — one row per atomic claim with sources, scope, grade, exceptions, and ARG implication.
2. **Translation dictionary** — state, structure, rule, parameter, environment, relation, compatibility, transport, and persistence across fields.
3. **Disagreement map** — accepted formal or empirical core separated from live interpretations.
4. **Representation audit** — the admissible transformations under which each claim is invariant, covariant, or representation-relative.
5. **Novelty decision** — standard result, useful synthesis, open question, candidate residual, or rejected claim.
6. **Residual agenda** — only questions not already answered by consensus.
7. **Claim-ledger amendments** — promotion, narrowing, rejection, or quarantine of affected ARG claims.
8. **Formalism impact note** — whether the current `Q_t=(B_t,x_t)` language should be retained, revised, or treated as one modeling factorization.

---

# Search and source baskets

Initial terminology should include:

- initial condition dependence;
- modal projection and persistence;
- non-normal dynamics and transient growth;
- invariant subspace and slow manifold;
- basin stability;
- state–operator interaction;
- parameter augmentation;
- skew-product dynamical system;
- cocycle and random dynamical system;
- conjugate dynamical systems;
- gauge and representation equivalence;
- evolving state spaces;
- transport on vector bundles;
- reset maps in hybrid systems;
- graph signals on time-varying graphs;
- adaptive and coevolving networks;
- organizational persistence;
- identity through change;
- structural realism;
- process ontology.

Search vocabulary is an orientation aid, not evidence.

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

Begin source intake with authoritative field maps, then trace every load-bearing claim to original mathematical or experimental sources. Do not revise the ontology from abstracts or isolated quotations.
