# Consensus Source Note — Blanchini on Set Invariance in Control

## Citation

Franco Blanchini. “Set Invariance in Control.” *Automatica* 35(11), 1747–1767 (1999). DOI: 10.1016/S0005-1098(99)00113-2.

Stable source: https://www.sciencedirect.com/science/article/pii/S0005109899001132

## Source classification

- **Field:** control theory
- **Subfield:** positive invariance, controlled invariance, constrained control, robustness
- **Source type:** authoritative survey
- **Publication status:** peer reviewed
- **Primary or secondary:** authoritative field synthesis

## Exact contribution used

Blanchini surveys positively invariant, robustly positively invariant, and controlled-invariant sets and their roles in constrained control, robustness analysis, synthesis, and optimization. The framework distinguishes sets preserved by autonomous closed-loop dynamics from sets that can be preserved through an appropriate admissible control law.

The load-bearing result for CS1 is that “remaining within an organization or admissible region” has several established control-theoretic meanings. Whether a set persists depends on the declared dynamics, disturbances, feedback policy, and constraints.

## Claim type

- authoritative synthesis of mathematical definitions and results;
- constrained-control methodology;
- robustness framework.

## Assumptions and domain

Specific invariance results depend on the system class, constraint set, disturbance model, feedback class, regularity, and whether invariance is positive, robust, or controlled.

Set invariance does not by itself imply attraction, recurrence, identity, optimality, or that every point in the set has the same behavior.

## Evidence and verification status

- **Derivation or protocol:** synthesis of established invariant-set theory and control applications.
- **Data or code available:** not required for the conceptual and theorem-level framework.
- **Independent replication or reproduction:** mature control-theory literature.
- **Known limitations:** exact maximal invariant-set computation can be difficult; nonlinear, stochastic, hybrid, and high-dimensional cases require specialized approximations.

## Established terminology

- positively invariant set;
- robust positively invariant set;
- controlled-invariant set;
- constrained control;
- Lyapunov function;
- robustness;
- control synthesis.

## Mapping into ARG

### ARG claim IDs affected

- `CS1-C04`
- `CS1-C05`
- `CS1-C11`
- `CS1-C12`
- `CS1-C13`
- ARG projection and admissibility claims.

### Proposed mapping

| Source object | ARG object | Mapping type | What is preserved | What is not preserved |
|---|---|---|---|---|
| positively invariant set | autonomously preserved admissible region | exact translation | forward set preservation | attraction or identity |
| controlled-invariant set | maintainable region under feedback | exact translation | existence of preserving control | passive persistence |
| robust invariant set | disturbance-tolerant admissible region | specialization | preservation across disturbance class | arbitrary uncertainty |
| constraint set | permitted occurrence region | specialization | declared admissibility | natural or ontological necessity |
| feedback law | KEEPER or corrective policy analogue | analogy/specialization | state-dependent corrective action | ARG-specific architecture or semantics |

## Equation or theorem mapping

For a controlled system

$$
\dot x=f(x,u,w),
$$

a set $K$ is positively invariant under fixed closed-loop dynamics if every trajectory beginning in $K$ remains in $K$. It is controlled invariant if, for every initial state in $K$, there exists an admissible control strategy keeping the trajectory in $K$.

These are distinct predicates and must not be merged.

## Cross-field implications

This literature provides a mature formal home for claims that global constraints restrict allowable local evolution and that corrective control can preserve a viable organization. Those ideas are therefore ingredients for ARG synthesis, not presumptive novelty.

It also clarifies that preservation of a set is weaker than preservation of a pointwise state and stronger than merely returning to the set after departure.

## Consensus assessment

- **Proposed grade:** C4 for the scoped control-theoretic distinctions among positive, robust, and controlled invariance.
- **Scoped consensus statement:** Set persistence under dynamics is relative to the system, feedback policy, disturbance class, and constraints; autonomous invariance and controlled invariance are distinct.
- **Reason for grade:** mature and authoritative survey of established control theory.
- **What remains disputed or open:** which invariant-set concept best models biological, physical, or organizational persistence in any target application.

## Novelty implication for ARG

- global admissibility and corrective preservation are established control concepts;
- a KEEPER-like mechanism must be mapped against feedback and controlled-invariance theory before novelty is discussed;
- ARG must distinguish autonomous persistence from persistence achieved by ongoing correction;
- projection onto a constraint and controlled invariance of a set are not automatically equivalent.

## Experiment decision

- **Is a new experiment needed?** no to establish the general set-invariance concepts.
- **Exact unresolved question:** whether ARG’s feedback, projection, and adaptive geometry produce a distinct invariant-set theorem, improved control policy, or useful decomposition.
- **Minimum discriminating experiment or proof:** direct equation mapping plus matched comparison with standard invariant-set and constrained-control baselines.

## Required project updates

- [x] consensus table
- [x] translation dictionary
- [x] novelty matrix
- [x] formalism impact note candidate
- [ ] ARG mechanism mapping after CS1

## Reviewer check

- [x] Autonomous and controlled invariance are separated.
- [x] Set preservation is not confused with pointwise identity.
- [x] Feedback analogy is labeled as analogy/specialization.
- [x] Novelty implication remains conditional.
