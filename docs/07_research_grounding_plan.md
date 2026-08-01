# Research Grounding Plan

## Purpose

This document defines the path from an executable prototype to a research-grounded and falsifiable program.

ARG must not move directly from philosophical motivation or software tests to scientific or ontological claims.

## Evidence levels

Work proceeds through four distinct levels:

1. **Interpretive principle** — the apophatic non-reification schema.
2. **Mathematical hypothesis** — a coherent family of local, feedback, and projected relational dynamics.
3. **Scientific hypothesis** — one or more ARG mechanisms explain or predict selected systems better than simpler alternatives.
4. **Ontological conjecture** — objective reality has a pluralistic-monist organization.

The first level is formulated. The current executable supports only a narrow part of the second.

## Canonical current status

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

The current implementation is a prototype of endogenous collective feedback, not yet a projected-admissibility model.

## Canonical model family

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}.
$$

- $M_0$: local/adaptive substrate without collective feedback or projection.
- $M_F$: endogenous collective feedback; current executable.
- $M_P$: explicit $\Gamma/H$ admissibility projection; unimplemented.
- $M_{FP}$: separately measurable feedback and projection; unimplemented.

The detailed model and gate definitions are fixed in `13_alignment_and_claim_ceiling.md`. Execution phases are fixed in `14_roadmap.md`.

## Research principles

### Falsification first

Every strong claim must be paired with a result that would weaken or reject it.

### Separate mechanisms before comparison

Collective feedback and tangent-space projection must be implemented and measured separately before any equivalence or combined-mechanism claim.

### Baselines before novelty

The full model must be compared against simpler systems with matched information, parameter budgets, initial conditions, and tuning effort.

### Recover known limits

A credible framework should reproduce established special cases when mechanisms are removed or frozen.

### Separate evidence levels

Every statement must be labeled as one of:

- definition;
- assumption;
- implemented;
- unit-tested;
- proof obligation;
- proved;
- numerically supported;
- empirically supported;
- conjectured;
- philosophical;
- rejected.

### No ontological promotion

Mathematical or empirical success does not by itself establish that the model is absolute reality.

## Workstream 1: Alignment and design contracts

Required outputs:

- canonical model definitions;
- exact current claim ceiling;
- frozen equations for $M_0,M_F,M_P,M_{FP}$;
- complete substrate dependency paths;
- exact reduction relationships;
- declared singular and failure behavior.

No comparative experiment begins until these contracts are frozen.

## Workstream 2: Novelty audit

Determine whether the proposed synthesis already exists in substantially equivalent form.

The comparison target is the conjunction

$$
\begin{aligned}
&\text{state-dependent metric}\\
+{}&\text{adaptive relational topology}\\
+{}&\text{collective feedback and/or projection}\\
+{}&\text{local-to-global compatibility}\\
+{}&\text{non-collapse barrier}\\
+{}&\text{presentation invariance}.
\end{aligned}
$$

Required outputs:

- a novelty matrix;
- the three closest existing frameworks;
- a list of standard ingredients;
- an explicit equivalence analysis;
- a precise statement of any remaining candidate novelty;
- a no-novelty conclusion if appropriate.

## Workstream 3: Mathematical foundation

### Shared obligations

- positivity and validity of intrinsic distance;
- local existence and uniqueness;
- boundedness or blow-up classification;
- permutation equivariance;
- numerical convergence;
- mechanism identifiability.

### Projection-specific obligations

- explicit $\Gamma/H$ definitions;
- rank and regularity conditions;
- projection existence and uniqueness;
- continuous-time constraint preservation;
- active inequality handling;
- numerical preservation or retraction;
- code-equation parity;
- fail-closed singular behavior.

Failed proofs and counterexamples are preserved as research results.

## Workstream 4: Literature landscape

Primary research tracks:

1. constrained nonlinear dynamics and differential-algebraic systems;
2. projected dynamical systems and tangent-cone dynamics;
3. adaptive and state-dependent networks;
4. collective-variable and mean-field feedback;
5. cellular sheaves and local-to-global consistency;
6. discrete curvature and evolving metric graphs;
7. gauge invariance, equivariance, and quotient descriptions;
8. singular barriers and noncollision;
9. physical anchor systems such as incompressible flow, constrained mechanics, synchronization, and flocking.

Each paper note records:

- exact result used;
- assumptions;
- mapping into ARG notation;
- overlap and difference;
- novelty implications;
- code or dataset availability;
- reproduction status;
- unresolved questions.

## Workstream 5: Benchmark ladder

### Stage A: Software and equation verification

- current three-node $M_F$;
- true no-feedback $M_0$;
- independent right-hand sides;
- exact reductions;
- permutation and numerical tripwires.

### Stage B: Projection verification

- mathematically specified $M_P$;
- constraint preservation;
- singularity handling;
- code-equation parity;
- comparison with penalty and multiplier controls.

### Stage C: Mechanism comparison

Compare

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}.
$$

Determine whether feedback and projection are distinct, approximately equivalent in a restricted regime, complementary, or redundant.

### Stage D: Established physical anchors

Initial targets:

1. constrained mechanical dynamics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

ARG must first reproduce established behavior before claiming additional value.

## Workstream 6: Measurements

Feedback contribution:

$$
\chi_i^F(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

Projection contribution:

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{0,i}(t)+F_{F,i}(t)\|+\epsilon}.
$$

Constraint error:

$$
\epsilon_\Gamma(t)=\|\Gamma(Z(t))\|.
$$

Metric evolution:

$$
\Delta_{\mathrm{metric}}(t)
=
\|g(t+\Delta t)-g(t)\|.
$$

Additional outputs:

- predictive and trajectory error;
- perturbation recovery;
- stability margins;
- topology changes;
- curvature measures;
- condition numbers;
- computational cost;
- parameter sensitivity;
- structural-intervention response;
- partial-observation identifiability.

## Workstream 7: Controls and tripwires

Required controls:

- graph-structure intervention with state fixed;
- state intervention with graph fixed;
- collective-statistic replacement with a matched exogenous signal;
- node relabeling and inverse recovery;
- independent equation implementation;
- solver and tolerance replication;
- matched-parameter baselines;
- deterministic seeds and frozen configurations;
- raw-output hashes;
- explicit singular-projection tests.

No result is accepted if it depends on one solver, one seed family, hidden configuration, or an undeclared model difference.

## Workstream 8: Prime-substrate quarantine

The prime-substrate conjecture remains separate until it has:

- a precise mathematical definition;
- a lawful map into states, relations, or metric variables;
- a derived observable;
- a prediction not inserted through parameter selection;
- comparison against non-prime alternatives.

It must not function as an unexplained foundational stopping point.

## Phase sequence

The binding execution sequence is:

1. alignment and claim control;
2. four-model design contract;
3. $M_0$ implementation and $M_F$ freeze;
4. $M_P$ mathematics;
5. $M_P$ implementation and preservation tests;
6. $M_{FP}$ implementation;
7. comparative mechanism experiment;
8. research grounding and physical anchors;
9. narrow scientific evaluation.

See `14_roadmap.md` for phase deliverables, exit gates, and stop conditions.

## Decision gate

Continue toward stronger scientific claims only if at least one of the following is established:

- a new theorem;
- a strict generalization of established models;
- a robust dynamical signature unavailable to matched alternatives;
- improved performance on a constrained physical problem;
- a useful invariant, curvature, or mechanism decomposition.

Otherwise, narrow ARG to a documented candidate synthesis.

## Immediate next actions

1. Finish Phase 0 documentation alignment.
2. Rerun and record the current software test suite.
3. Freeze the Phase 1 design contract.
4. Implement $M_0$ without hidden collective paths.
5. Design $M_P$ mathematically before implementation.

## Research maxim

> Establish what is known. Separate what differs. Prove what can be proved. Test the alternatives. Reify nothing.
