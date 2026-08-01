# Experimental Plan

## Status

The current executable is $M_F$, the collective-feedback prototype. The projected variants $M_P$ and $M_{FP}$ are not yet implemented and cannot yet be experimentally compared.

No projected-geometry result may be reported until the fail-closed projection gate passes.

## Canonical models

### $M_0$ — local/adaptive substrate baseline

- local nonlinear dynamics;
- neighborhood coupling;
- adaptive edge and metric dynamics where declared;
- no collective-feedback terms;
- no admissibility projection.

### $M_F$ — collective feedback

- $M_0$ substrate;
- endogenous statistic $c(x)$;
- explicit feedback into constituent transitions;
- no projection.

### $M_P$ — global admissibility projection

- explicit $\Gamma/H$ admissible set;
- implemented projection of the local proposal;
- no feedback unless separately declared.

### $M_{FP}$ — feedback plus projection

- both mechanisms;
- separate feedback and projection diagnostics.

## Experiment 0: Code-equation alignment

Before mechanism experiments:

- verify each model against a frozen equation contract;
- retain an independently written right-hand side;
- verify exact reduction paths among models;
- fail closed on unrecognized parameters or undeclared dependencies.

## Experiment 1: $M_0$ versus $M_F$

### Question

Does endogenous collective feedback create behavior not reproduced by the no-feedback substrate?

### Feedback ratio

$$
\chi_i^F(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

### Required interventions

- remove all $c(x)$ transition terms;
- replace $c(x)$ with a matched exogenous signal;
- permute initial states while holding structure fixed;
- alter graph structure while holding state fixed;
- perturb $c(x)$ through substrate-consistent state interventions.

### Claim limit

A difference between $M_0$ and $M_F$ supports only a prototype-level feedback result. It does not establish macro-level causal autonomy.

## Experiment 2: $M_0$ versus $M_P$

This experiment is blocked until $M_P$ passes the projected-claim implementation gate.

### Projection ratio

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

### Required outputs

- equality-constraint error;
- inequality active-set trace where applicable;
- tangent and normal components;
- projection-system condition number;
- retraction or integrator correction;
- solver-refinement behavior.

## Experiment 3: $M_F$ versus $M_P$

### Question

Are collective feedback and global admissibility projection dynamically distinct?

Required comparisons:

- full-state trajectory distance;
- observable trajectory distance;
- local linearization and Jacobian comparison;
- fixed points and stability;
- bifurcation structure;
- perturbation response;
- parameter sensitivity;
- partial-observation identifiability.

Similar plots are not evidence of equivalence.

## Experiment 4: $M_{FP}$ interaction

### Question

Do feedback and projection combine additively, redundantly, or nonlinearly?

Define an interaction residual under a declared comparison map:

$$
R_{FP}
=
\Delta(M_{FP},M_0)
-
\Delta(M_F,M_0)
-
\Delta(M_P,M_0).
$$

The exact form of $\Delta$ must be preregistered for each experiment.

## Experiment 5: Dynamic-geometry ablation

Within each applicable model compare:

1. full dynamic $q$ and $s$;
2. frozen $q$;
3. frozen $s$;
4. frozen $q$ and $s$;
5. static graph with parameter-matched node dynamics.

This determines whether “geometry” contributes beyond adaptive weights or extra state variables.

## Experiment 6: Structural intervention

Permute graph incidence while holding node states and parameters fixed. Treat independently sampled structures, not nested solver runs, as the inferential units for structural claims.

## Experiment 7: State intervention

Permute or perturb initial states while holding graph structure and parameters fixed.

## Experiment 8: Relabeling tripwire

Randomly relabel nodes and require identical invariant trajectories after undoing the permutation:

$$
\Phi_t(PZ_0)=P\Phi_t(Z_0).
$$

Run this independently for $M_0$, $M_F$, $M_P$, and $M_{FP}$ as they become available.

## Experiment 9: Numerical tripwires

Require:

- convergence under decreasing step size or tighter tolerance;
- agreement across at least two appropriate integrators;
- independently written reference equations;
- deterministic replay;
- finite-value checks;
- explicit failure on singular projection systems;
- configuration and output hashes.

## Experiment 10: Equivalence test

The claim

$$
M_F\equiv M_P
$$

requires one of:

- exact conjugacy;
- exact reparameterization;
- a proved approximation with an error bound;
- observational equivalence under a specified observation map and domain.

Numerical resemblance alone is insufficient.

## Primary outputs

- node-state trajectories;
- edge-activation trajectories;
- metric-deformation trajectories;
- intrinsic distance matrices;
- coherence or mismatch measures where defined;
- feedback contribution $F_F$;
- projection contribution $F_P$;
- constraint residuals;
- Lyapunov or local stability estimates;
- intervention response;
- computational cost;
- failure and singularity logs.

## Execution authorization

Current authorization:

- $M_F$ software tests: authorized;
- $M_0$ design and implementation: authorized;
- $M_P$ mathematical design: authorized;
- $M_P$ scientific claims: not authorized;
- $M_{FP}$ experiments: blocked pending implementation;
- feedback-projection equivalence claim: unverified.
