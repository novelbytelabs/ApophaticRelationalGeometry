# Consensus Source Note — Alphonse, Elliott, and Stinner on Evolving Spaces

## Citation

Amal Alphonse, Charles M. Elliott, and Björn Stinner. “An Abstract Framework for Parabolic PDEs on Evolving Spaces.” *Portugaliae Mathematica* 72, no. 1 (2015): 1–46. arXiv:1403.4500. DOI: 10.4171/PM/1953.

## Source classification

- **Field:** mathematics
- **Subfield:** functional analysis, partial differential equations, evolving Hilbert spaces
- **Source type:** original framework and theorem paper
- **Publication status:** peer reviewed; preprint available
- **Primary or secondary:** primary

## Exact contribution used

The paper formulates parabolic evolution equations on families of changing Hilbert spaces $X(t)$. It assumes pushforward maps

$$
\phi_t:X(0)\rightarrow X(t)
$$

that are linear homeomorphisms under stated compatibility conditions. It defines pullbacks by their inverses and constructs cross-time operators

$$
U(t,s)=\phi_t\phi_{-s}:X(s)\rightarrow X(t).
$$

The paper explicitly shows the composition law

$$
U(t,r)U(r,s)=U(t,s).
$$

It also defines strong and weak material derivatives on the evolving spaces and proves well-posedness for a class of parabolic PDEs under assumptions on the operators and data.

## Claim type

- mathematical definition;
- mathematical framework;
- existence, uniqueness, and regularity results under stated assumptions.

## Assumptions and domain

The source assumes, among other conditions:

- a time-indexed family of real separable Hilbert spaces;
- a fixed reference space $X(0)$;
- bounded linear homeomorphisms $\phi_t$ with inverses;
- uniform norm bounds and continuity/measurability conditions;
- parabolic-operator assumptions for the well-posedness results.

The framework addresses smoothly or compatibly evolving spaces connected to a reference space. It does not establish a canonical transport for arbitrary node creation, deletion, splitting, merging, or unknown correspondence.

## Evidence and verification status

- **Derivation or protocol:** formal definitions and proofs in the paper.
- **Data or code available:** not required for the abstract results.
- **Independent replication or reproduction:** not assessed in this initial note.
- **Authoritative review or field uptake:** the paper develops an established evolving-space analysis program; citation audit pending.
- **Known counterexamples or exceptions:** arbitrary changing spaces without admissible homeomorphisms fall outside this setup.

## Established terminology

- evolving Hilbert spaces;
- pushforward and pullback maps;
- compatibility of an evolving family and its maps;
- two-parameter semigroup;
- material derivative;
- weak material derivative;
- well-posedness.

## Mapping into ARG

### ARG claim IDs affected

- `CS1-C09`
- `CS1-C10`
- future state-transport and persistence claims involving $Q_t=(B_t,x_t)$.

### Proposed mapping

| Source object | ARG object | Mapping type | What is preserved | What is not preserved |
|---|---|---|---|---|
| $X(t)$ | $X_{B_t}$ | specialization/translation | state space depends on changing structure or domain | arbitrary relational semantics |
| $\phi_t$ | reference-to-current transport | exact translation within assumptions | state identification through a reference space | canonical identity outside the chosen maps |
| $U(t,s)$ | $T_{B_s\to B_t}$ | exact translation within assumptions | cross-time transport and composition | abrupt or noninvertible structural change |
| material derivative | derivative after accounting for space evolution | exact translation in applicable models | separates change of carrier from field evolution | universal identity criterion |

## Equation or theorem mapping

### Source form

$$
U(t,s)=\phi_t\phi_{-s},
\qquad
U(t,r)U(r,s)=U(t,s).
$$

### ARG form

$$
T_{B_s\to B_t}:X_{B_s}\rightarrow X_{B_t},
\qquad
T_{B_r\to B_t}\circ T_{B_s\to B_r}=T_{B_s\to B_t}.
$$

### Mapping conditions

The ARG structures must generate a compatible family of state spaces connected by the required invertible maps. The mapping does not cover every graph rewrite, dimension change, or ambiguous identity relation.

## Cross-field implications

The source establishes that changing state spaces and composition-consistent transport are standard mathematical machinery. It does not decide which transport is physically, biologically, or philosophically appropriate. Those criteria must come from the modeled system and preserved observables.

## Consensus assessment

- **Proposed grade:** C4 for the scoped mathematical statement.
- **Scoped consensus statement:** When state spaces evolve through a specified compatible family of maps, states can be transported through a reference space, cross-time transport composes consistently, and derivatives can be defined relative to that evolution.
- **Reason for grade:** explicit definitions and formal results in a mature mathematical framework.
- **What remains disputed or open:** selection or uniqueness of transport outside the assumed family; identity under noninvertible and semantically ambiguous changes.

## Novelty implication for ARG

- standard established ingredient;
- direct precedent for ARG’s proposed transport map;
- general transport machinery is not an ARG novelty;
- a possible residual would require a precisely different class of structural change or an invariant persistence result not already covered.

## Experiment decision

- **Is a new experiment needed?** no for the general claim that changing state spaces require explicit transport and composition rules.
- **Exact unresolved question:** whether a particular ARG transport is appropriate and predictive for a specified relational system.
- **Why existing results do not already answer it:** the answer depends on the concrete structural morphisms, observables, and scientific semantics.

## Required project updates

- [x] consensus table
- [x] translation dictionary
- [x] novelty matrix
- [x] formalism
- [ ] immediate experimental protocol

## Reviewer check

- [x] Source supports the scoped claim.
- [x] Claim type is correct.
- [x] Mapping does not erase the invertibility and compatibility assumptions.
- [x] Proposed experiment is limited to a genuine system-specific residual.
