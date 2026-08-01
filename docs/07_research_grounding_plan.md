# Research Grounding Plan

## Purpose

This document defines the path from software-verified prototypes to a research-grounded and falsifiable program.

ARG must not move directly from philosophical motivation or software tests to scientific or ontological claims.

## Evidence levels

Work proceeds through four distinct levels:

1. **Interpretive principle** — the apophatic non-reification schema.
2. **Mathematical hypothesis** — a coherent family of local, feedback, projected, and combined relational dynamics.
3. **Scientific hypothesis** — one or more ARG mechanisms explain or predict selected systems better than simpler alternatives.
4. **Ontological conjecture** — objective reality has a pluralistic-monist organization.

The interpretive principle is formulated. Contract v1.0 now supplies software-verified prototypes for the second level. The third and fourth levels remain unverified.

## Canonical current status

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

No comparative scientific experiment has been executed.

## Canonical model family

- $M_0$: local/adaptive substrate without collective feedback or projection.
- $M_F$: endogenous collective feedback.
- $M_P$: constant-amplitude tangent projection of the $M_0$ node proposal.
- $M_{FP}$: explicit feedback proposal followed by node projection, with retained $s/q$ feedback.

At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

but this does not imply trajectory equivalence because the adaptive-substrate dynamics differ.

The detailed model and claim boundaries are fixed in `13_alignment_and_claim_ceiling.md`. Execution phases are fixed in `14_roadmap.md`.

## Research principles

### Falsification first

Every strong claim must be paired with a result that would weaken or reject it.

### Separate mechanisms before comparison

Collective feedback, tangent projection, and their combination remain separately measurable. Similar behavior must not erase their mechanistic distinction.

### Baselines before novelty

Every extended model must be compared against simpler systems with matched information, parameter budgets, initial conditions, observation access, and tuning effort.

### Recover known limits

A credible framework should reproduce established special cases when mechanisms are removed or frozen.

### Separate evidence levels

Every statement must be labeled as one of:

- definition;
- assumption;
- implemented;
- unit-tested;
- proof obligation;
- proved under stated assumptions;
- numerically supported;
- empirically supported;
- conjectured;
- philosophical;
- rejected.

### No ontological promotion

Mathematical or empirical success does not by itself establish that the model is absolute reality.

---

# Workstream 1: claim control and contracts

## Completed

- canonical $M_0/M_F/M_P/M_{FP}$ definitions;
- exact claim ceiling;
- frozen contract-v1.0 equations;
- explicit feedback and projection substrate paths;
- declared reduction relationships;
- fail-closed singular and nonfinite behavior;
- Phase 3 and Phase 4 verification records.

## Remaining

- maintain alignment as experiment protocols and results are added;
- prohibit scientific promotion from software evidence alone.

---

# Workstream 2: novelty audit

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

- primary-source novelty matrix;
- the closest existing feedback, projection, and combined frameworks;
- exact equation mappings;
- reparameterization and equivalence analysis;
- precise remaining candidate novelty;
- a no-novelty conclusion where appropriate.

Implementation is not evidence of novelty.

---

# Workstream 3: mathematical foundation

## Shared obligations

- positivity and metric validity of intrinsic distance;
- local existence and uniqueness;
- boundedness or blow-up classification;
- permutation-equivariance theorem;
- numerical convergence beyond reference cases;
- mechanism identifiability.

## Projection obligations

- rank and regularity conditions;
- projection existence and uniqueness;
- continuous-time preservation;
- future inequality active-set treatment;
- numerical preservation and retraction analysis;
- code-equation parity;
- fail-closed singular behavior.

## Combined-model obligations

- exact same-state cancellation analysis;
- trajectory consequences of retained $s/q$ feedback;
- no-double-counting analysis;
- ordering sensitivity;
- reduction maps.

Failed proofs and counterexamples are preserved as research results.

---

# Workstream 4: literature landscape

Primary tracks:

1. collective-variable and mean-field feedback;
2. constrained nonlinear dynamics and DAEs;
3. projected dynamical systems and tangent-cone dynamics;
4. feedback under constraints;
5. adaptive and state-dependent networks;
6. cellular sheaves and local-to-global consistency;
7. discrete curvature and evolving metric graphs;
8. equivariance and quotient descriptions;
9. singular barriers and noncollision;
10. physical anchors such as constrained mechanics, incompressible flow, synchronization, and flocking.

Each source note records:

- exact theorem, equation, algorithm, or experiment used;
- assumptions;
- mapping into ARG notation;
- overlap and difference;
- novelty implications;
- code or dataset availability;
- reproduction status;
- unresolved questions.

---

# Workstream 5: benchmark ladder

## Stage A: software and equation verification — complete

All four prototypes have canonical dispatch, regression tests, fail-closed behavior, and independently written reference paths at tested cases.

## Stage B: comparative protocol freeze — active

Phase 5 must freeze:

- primary and secondary hypotheses;
- observation maps and equivalence tolerances;
- parameter and initial-condition manifests;
- development and confirmatory partitions;
- inferential units;
- interventions and ablations;
- numerical refinement and alternate-integrator policy;
- exclusions and stop rules;
- raw-output provenance and checksums.

No pilot may run before this gate passes.

## Stage C: development pilot — blocked

Purpose:

- expose numerical failures;
- test whether observables identify the mechanisms;
- locate degeneracies;
- determine whether the constant-amplitude sandbox is informative enough.

Pilot results remain developmental.

## Stage D: confirmatory comparison — blocked

Compare

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}
$$

on held-out configurations under the frozen protocol.

## Stage E: established physical anchors — blocked

Initial targets:

1. constrained mechanical dynamics;
2. incompressible-flow projection;
3. adaptive synchronization or flocking.

ARG must reproduce established behavior before claiming an extension.

---

# Workstream 6: measurements

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
{\|F_{\mathrm{proposal},i}(t)\|+\epsilon}.
$$

Constraint error:

$$
\epsilon_\Gamma(t)=|\Gamma(Z(t))|.
$$

Additional outputs:

- full-state and observation-map trajectory discrepancy;
- adaptive-substrate divergence;
- intrinsic-distance evolution;
- perturbation recovery;
- stability and bifurcation measures;
- condition and singularity diagnostics;
- computational cost;
- parameter sensitivity;
- structural-intervention response;
- partial-observation identifiability.

Every metric requires executable, frozen aggregation and tolerance rules.

---

# Workstream 7: controls and tripwires

Required controls:

- graph intervention with state fixed;
- state intervention with graph fixed;
- collective-statistic replacement with a matched exogenous signal;
- node relabeling and inverse recovery;
- independent equation implementation;
- solver and tolerance replication;
- matched-parameter baselines;
- deterministic seeds and frozen configurations;
- raw-output hashes;
- explicit singular-projection tests;
- frozen-$s$, frozen-$q$, and static-geometry ablations.

No result is accepted if it depends on one solver, one seed family, hidden configuration, or undeclared model difference.

---

# Workstream 8: prime-substrate quarantine

The prime-substrate conjecture remains separate until it has:

- a precise mathematical definition;
- a lawful map into states, relations, or metric variables;
- a derived observable;
- a prediction not inserted through parameter selection;
- comparison against non-prime alternatives.

It must not function as an unexplained foundational stopping point.

---

# Current phase sequence

1. alignment and claim control — complete;
2. four-model design contract — complete;
3. $M_0/M_F$ implementation — complete;
4. $M_P$ implementation — complete;
5. $M_{FP}$ implementation — complete;
6. comparative experiment protocol — active;
7. development pilot — blocked;
8. confirmatory comparison — blocked;
9. relational projection v2 and physical anchors — blocked.

See `14_roadmap.md` for deliverables, exit gates, and stop conditions.

## Decision gate

Continue toward stronger scientific claims only if at least one of the following is established:

- a new theorem;
- a strict generalization of established models;
- a robust preregistered dynamical signature unavailable to matched alternatives;
- improved performance on a constrained physical problem;
- a useful invariant, curvature, or mechanism decomposition.

Otherwise, narrow ARG to a documented candidate synthesis.

## Immediate next action

Freeze the Phase 5 comparative experiment protocol tracked by GitHub Issue `#8`. No pilot execution is authorized before the protocol passes.

## Research maxim

> Establish what is known. Separate what differs. Prove what can be proved. Test the alternatives. Reify nothing.
