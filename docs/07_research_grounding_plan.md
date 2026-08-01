# Research Grounding Plan

## Purpose

This document defines the path from a coherent mathematical proposal to a research-grounded and falsifiable program.

The project must not move directly from philosophical motivation to claims about physical reality. Work proceeds through four distinct levels:

1. **Interpretive principle** — the apophatic non-reification schema.
2. **Mathematical hypothesis** — a well-posed nonlinear dynamic relational constraint geometry.
3. **Scientific hypothesis** — the full geometry explains or predicts selected systems better than simpler alternatives.
4. **Ontological conjecture** — objective reality has a pluralistic-monist organization.

Only the first level is currently formulated. The second is partially implemented. The third and fourth remain unestablished.

## Core mathematical hypothesis

The working dynamical form is

$$
\dot Z
=
\Pi_{T_Z\mathcal M(Z)}F_{\mathrm{local}}(Z),
$$

or equivalently,

$$
\dot Z
=
F_{\mathrm{local}}(Z)
-
\Pi_{N_Z\mathcal M(Z)}F_{\mathrm{local}}(Z).
$$

The intended interpretation is:

- local states and local relations propose change;
- the admissible geometry excludes incoherent motion;
- state, topology, metric, rule parameters, and collective modes may coevolve;
- no presentation is granted ontological privilege.

## Research principles

### Falsification first

Every strong claim must be paired with a result that would weaken or reject it.

### Baselines before novelty

The full model must be compared against simpler systems with matched parameter budgets.

### Recover known limits

A credible framework should reproduce established special cases when components are frozen or removed.

### Separate evidence levels

Every statement must be labeled as one of:

- definition;
- assumption;
- proved;
- numerically supported;
- empirically supported;
- conjectured;
- philosophical.

### No ontological promotion

Mathematical success does not by itself establish that the model is reality.

## Workstream 1: Novelty audit

Determine whether the proposed synthesis already exists in substantially equivalent form.

The comparison target is not any single ingredient. It is the conjunction

$$
\begin{aligned}
&\text{state-dependent metric}\\
+{}&\text{adaptive relational topology}\\
+{}&\text{local-to-global compatibility}\\
+{}&\text{constraint projection}\\
+{}&\text{non-collapse barrier}\\
+{}&\text{presentation invariance}.
\end{aligned}
$$

Required outputs:

- a novelty matrix;
- the three closest existing frameworks;
- a list of components that are standard;
- a precise statement of any remaining candidate novelty;
- an explicit no-novelty conclusion if the system is equivalent to known methods.

## Workstream 2: Mathematical foundation

The following obligations must be discharged before strong scientific claims:

1. **Metric validity** — positivity, symmetry, path finiteness, and the triangle inequality.
2. **Well-posedness** — local existence, uniqueness, and continuation conditions.
3. **Constraint preservation** — admissible initial states remain admissible.
4. **Projection regularity** — the tangent or normal projection exists and is sufficiently regular.
5. **Equivariance** — relabeling or coordinate changes do not alter observables.
6. **Non-collapse** — finite energy prevents intrinsic edge length from reaching zero.
7. **Reduction limits** — fixed-graph, fixed-metric, unconstrained, and linear compatibility limits are recovered.
8. **Identifiability** — the proposed mechanisms are distinguishable from one another.

Failed proofs and counterexamples must be preserved as research results.

## Workstream 3: Literature landscape

Primary research tracks:

1. constrained nonlinear dynamics and differential-algebraic systems;
2. projected dynamical systems and tangent-cone dynamics;
3. adaptive and state-dependent networks;
4. cellular sheaves and local-to-global consistency;
5. discrete curvature and evolving metric graphs;
6. gauge invariance, equivariance, and quotient descriptions;
7. relational mechanics and relational physical theories;
8. physical anchor systems such as incompressible flow, constrained mechanics, synchronization, and flocking.

Each paper note must record:

- exact result used;
- assumptions;
- mathematical overlap;
- differences from this project;
- implications for novelty;
- code or dataset availability;
- unresolved questions.

## Workstream 4: Benchmark ladder

### Stage A: Exact synthetic systems

Use small systems where correctness can be independently checked:

- three-node scalar model;
- constrained pendulum or linkage;
- divergence-free lattice flow;
- adaptive synchronization network;
- compatibility or consensus network.

### Stage B: Mechanism isolation

Compare:

$$
\begin{aligned}
M_0&:\text{ fixed graph with local dynamics},\\
M_1&:\text{ adaptive graph without global projection},\\
M_2&:\text{ fixed geometry with global projection},\\
M_3&:\text{ dynamic geometry with soft penalties},\\
M_4&:\text{ complete proposed geometry}.
\end{aligned}
$$

### Stage C: Established physical anchors

Initial targets:

1. incompressible-flow projection;
2. constrained mechanical dynamics;
3. adaptive synchronization or flocking.

The full model must first reproduce established behavior before it is evaluated for additional explanatory value.

## Workstream 5: Measurements

Core quantities include

$$
\epsilon_{\Gamma}(t)=\|\Gamma(Z(t))\|,
$$

$$
\chi_i(t)
=
\frac{\|F_i^{\mathrm{collective}}(t)\|}
{\|F_i^{\mathrm{local}}(t)\|+\epsilon},
$$

$$
\Delta_{\mathrm{metric}}(t)
=
\|g(t+\Delta t)-g(t)\|,
$$

and

$$
\Delta E(t)=E(t)-E(0).
$$

Additional outputs:

- predictive error;
- perturbation recovery;
- stability margins;
- topology changes;
- curvature measures;
- computational cost;
- parameter sensitivity;
- structural-intervention response.

A central testable signature is:

> Local dynamics dominate ordinary evolution, while the collective correction becomes large near coherence boundaries, topological transitions, or collapse barriers.

## Workstream 6: Controls and tripwires

Required controls:

- graph-structure permutation with states and parameters fixed;
- state permutation with graph and parameters fixed;
- collective-mode replacement with a matched exogenous signal;
- node relabeling with trajectory recovery after inverse permutation;
- independent reference implementation of the right-hand side;
- solver and tolerance replication;
- matched-parameter baselines;
- deterministic seeds and frozen configuration manifests.

No result is accepted if it depends on one solver, one seed family, hidden caching, or an unrecorded configuration.

## Workstream 7: Prime-substrate quarantine

The prime-substrate conjecture remains separate from the core geometry until it has:

- a precise mathematical definition;
- a lawful map into states, relations, or metric variables;
- at least one derived observable;
- a prediction not inserted through parameter selection;
- a comparison against non-prime alternatives.

It must not function as an unexplained foundational stopping point.

## Schedule

### Sprint 1 — Research map and claims

- complete the claim ledger;
- collect the first primary-source set;
- build the novelty matrix;
- identify the closest existing frameworks;
- rewrite the formalism in standard constrained-dynamics notation.

### Sprint 2 — Proofs and numerical correctness

- address metric, constraint-preservation, and equivariance obligations;
- document counterexamples;
- implement the baseline family $M_0$ through $M_4$;
- freeze numerical protocols and tripwires.

### Sprint 3 — Synthetic mechanism tests

- run exact and synthetic benchmarks;
- complete structural ablations;
- measure local-versus-collective influence;
- determine whether the full model has behavior not reproduced by simpler baselines.

### Sprint 4 — Physical anchors

- reproduce one constrained-flow experiment;
- reproduce one constrained-mechanics experiment;
- reproduce one adaptive-network experiment;
- compare accuracy, stability, interpretability, and cost.

## Decision gate

Continue toward stronger scientific claims only if at least one of the following is established:

- a new theorem;
- a demonstrably broader unification of established models;
- a robust dynamical signature unique to the full model;
- improved performance on a constrained physical problem;
- a useful new invariant or curvature quantity.

Otherwise, narrow the project claim to a formal synthesis or modeling framework.

## Immediate next actions

1. Populate `08_claim_ledger.md` with every current project claim.
2. Begin primary-source intake using `10_literature_landscape.md`.
3. Complete the comparison rows in `09_novelty_matrix.md`.
4. Freeze the first benchmark protocol in `11_benchmark_specification.md`.
5. Treat `12_falsification_criteria.md` as binding before results are generated.

## Research maxim

> Establish what is known. Prove what can be proved. Isolate what is new. Try to break it. Reify nothing.
