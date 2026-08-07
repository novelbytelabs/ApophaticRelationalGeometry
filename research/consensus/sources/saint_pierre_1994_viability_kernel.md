# Consensus Source Note — Saint-Pierre on Viability Kernels

## Citation

Patrick Saint-Pierre. “Approximation of the Viability Kernel.” *Applied Mathematics & Optimization* 29, 187–209 (1994). DOI: 10.1007/BF01204182.

Stable source: https://link.springer.com/article/10.1007/BF01204182

## Source classification

- **Field:** viability theory, control, and set-valued dynamics
- **Subfield:** constrained differential inclusions, numerical approximation of viability kernels
- **Source type:** original theorem and algorithm paper
- **Publication status:** peer reviewed
- **Primary or secondary:** primary

## Exact contribution used

Saint-Pierre studies discrete approximations of differential inclusions and proves convergence results for approximating a viability kernel by discrete viability kernels. A viability kernel is the largest subset of a constraint set from which at least one admissible trajectory can remain within the constraint set over the relevant horizon.

The load-bearing result for CS1 is that persistence under constraints is already formalized as an existential, policy- and admissibility-relative property. It is not merely passive state retention: a state is viable when suitable allowable dynamics or controls can keep it inside a declared safe or admissible set.

## Claim type

- mathematical definition;
- approximation theorem;
- numerical set-valued method.

## Assumptions and domain

The paper concerns differential inclusions and their discrete approximations under regularity conditions including Lipschitz-type assumptions. The viability kernel depends on:

- the constraint set;
- the set-valued dynamics or available controls;
- the time horizon;
- discretization and approximation policy.

Viability does not imply attraction, autonomous stability, identity, or optimality.

## Evidence and verification status

- **Derivation or protocol:** set-valued analysis and convergence of discrete viability-kernel approximations.
- **Data or code available:** not required for the theorem-level result.
- **Independent replication or reproduction:** established viability-theory methodology with broad applications.
- **Known limitations:** computational scaling, regularity failure, uncertainty, stochastic dynamics, and hybrid discontinuities require additional methods.

## Established terminology

- viability domain;
- viability kernel;
- differential inclusion;
- admissible trajectory;
- constraint set;
- discrete viability kernel;
- internal approximation.

## Mapping into ARG

### ARG claim IDs affected

- `CS1-C04`
- `CS1-C05`
- `CS1-C09`
- `CS1-C11`
- `CS1-C12`
- `CS1-C13`

### Proposed mapping

| Source object | ARG object | Mapping type | What is preserved | What is not preserved |
|---|---|---|---|---|
| constraint set $K$ | admissible occurrence region | specialization | allowed states or occurrences | universal law or ontology |
| set-valued dynamics $F$ | admissible transition family | specialization | available local evolutions or controls | unique realized trajectory |
| viability kernel $\operatorname{Viab}_F(K)$ | states from which admissible continuation exists | exact translation for constrained persistence | existential continuation under constraints | attraction, identity, or passive retention |
| discrete approximation | computational ARG test | exact methodological neighbor | convergent approximation under assumptions | proof outside those assumptions |

## Equation or theorem mapping

For a differential inclusion

$$
\dot x(t)\in F(x(t)),
\qquad x(t)\in K,
$$

the viability kernel is

$$
\operatorname{Viab}_F(K)
=
\left\{x_0\in K:
\exists x(\cdot),\ x(0)=x_0,
\ \dot x(t)\in F(x(t)),
\ x(t)\in K
\right\}.
$$

Saint-Pierre develops discrete internal approximations using recursive inclusions and proves convergence under scoped assumptions.

## Cross-field implications

This adds another established persistence predicate:

$$
P_{\mathrm{viable}}.
$$

It differs from basin return, metastable retention, invariant-manifold continuation, and norm preservation. Viability is relative to allowed interventions and constraints, making it a direct counterexample to treating persistence as one intrinsic scalar of a state–structure pair.

## Consensus assessment

- **Proposed grade:** C4 for viability kernels and their scoped approximation theory.
- **Scoped consensus statement:** Constrained continuation can be formalized by the viability kernel, the set of states from which at least one admissible trajectory remains within a declared constraint set.
- **Reason for grade:** mature theorem-level framework and numerical methodology.
- **What remains disputed or open:** which constraints and controls are scientifically justified in a particular system and how to scale computation to complex changing structures.

## Novelty implication for ARG

- persistence under admissibility constraints is established control mathematics;
- ARG projection and admissibility language must be compared with viability and controlled-invariance theory;
- a state’s viability depends on dynamics, constraints, and allowed controls, not merely state–operator alignment;
- no new experiment is needed to show that constrained persistence is relational and policy-dependent.

## Experiment decision

- **Is a new experiment needed?** no for the general viability principle.
- **Exact unresolved question:** whether ARG supplies a distinct admissibility set or transition family producing a useful result unavailable through standard viability analysis.
- **Minimum discriminating experiment or proof:** derive the ARG viability kernel or controlled-invariant set and compare it with standard projection, viability, and invariant-set methods under matched constraints.

## Required project updates

- [x] consensus table
- [x] translation dictionary
- [x] persistence type discipline
- [x] novelty implications
- [ ] formalism impact note

## Reviewer check

- [x] Viability is distinguished from stability and identity.
- [x] Existential control dependence is explicit.
- [x] Approximation claims retain their assumptions.
- [x] Novelty implication is scoped.
