# Experimental Plan

## Status

$M_0$, $M_F$, and the contract-v1.0 $M_P$ projection sandbox are implemented and unit-tested. $M_{FP}$ remains unimplemented.

No comparative scientific experiment is authorized until $M_{FP}$ passes its implementation gate and the experiment protocol is frozen.

## Canonical models

### $M_0$

Local/adaptive substrate without collective feedback or projection.

### $M_F$

$M_0$ plus endogenous collective feedback.

### $M_P$

$M_0$ proposal projected onto

$$
\Gamma(Z)=\frac13x^Tx-c_0=0.
$$

It includes projected RK4 stages and mandatory radial retraction.

### $M_{FP}$

Feedback proposal followed by projection, with feedback and projection separately observable. This model remains the active implementation gate.

## Experiment 0: Code-equation alignment

### Completed

- $M_0/M_F$ derivative and RK4 reference parity;
- $M_F(\chi=\eta_2=\rho=0)=M_0$ reduction;
- $M_P$ projector identities;
- $M_P$ tangency, retraction, singular handling, and reference parity;
- model, contract, source, and configuration labels where declared.

### Remaining

- $M_{FP}$ implementation and independent parity;
- exact combined-model reductions;
- full four-model output schema parity;
- final confirmatory configuration manifest.

## Experiment 1: $M_0$ versus $M_F$

### Question

Does endogenous collective feedback produce behavior not reproduced by the no-feedback substrate?

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

A difference supports only a scoped feedback result. It does not establish macro-level causal autonomy.

## Experiment 2: $M_0$ versus $M_P$

### Question

What behavior is produced by constant-amplitude projection relative to the unprojected local/adaptive substrate?

### Projection ratio

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon}.
$$

### Required outputs

- constraint residual;
- tangent and normal components;
- projection denominator;
- retraction magnitude;
- solver-refinement behavior;
- full-state and observation-map trajectory differences.

Implementation tests have passed. The comparative scientific run remains blocked pending the frozen four-model protocol.

## Experiment 3: $M_F$ versus $M_P$

### Question

Are collective feedback and global admissibility projection dynamically distinct?

Required comparisons:

- full-state trajectory distance;
- observation-map distance;
- local Jacobian comparison;
- fixed points and stability;
- perturbation response;
- parameter sensitivity;
- partial-observation identifiability.

Similar trajectories are not evidence of equivalence.

## Experiment 4: $M_{FP}$ mechanism interaction

### Binding structural prediction

For the contract-v1.0 sphere constraint,

$$
P_T[-\chi c(x)x]=0,
$$

hence

$$
\boxed{f_{FP}=f_P}
$$

for node derivatives.

The $s$ and $q$ derivatives retain $M_F$ feedback. The first task is to implement and verify this identity before measuring trajectory interaction.

### Interaction residual

After implementation, define under a preregistered comparison map

$$
R_{FP}
=
\Delta(M_{FP},M_0)
-
\Delta(M_F,M_0)
-
\Delta(M_P,M_0).
$$

The exact $\Delta$ must be frozen before results are generated.

## Experiment 5: Dynamic-geometry ablation

Within each applicable model compare:

1. full dynamic $q$ and $s$;
2. frozen $q$;
3. frozen $s$;
4. frozen $q$ and $s$;
5. static graph with parameter-matched node dynamics.

This tests whether geometry contributes beyond adaptive weights or extra state variables.

## Experiment 6: Structural intervention

Permute graph incidence while holding node states and parameters fixed. Independently sampled structures, not nested solver steps or seeds, are the inferential units for structural claims.

## Experiment 7: State intervention

Permute or perturb initial states while holding graph structure and parameters fixed.

## Experiment 8: Relabeling tripwire

Require

$$
\Phi_t(PZ_0)=P\Phi_t(Z_0)
$$

after undoing the permutation. Software-level permutation tests pass for $M_0$, $M_F$, and $M_P$; $M_{FP}$ remains pending.

## Experiment 9: Numerical tripwires

Require:

- decreasing discrepancy under step refinement;
- agreement with an independently written reference path;
- deterministic replay;
- finite-value checks;
- explicit singular-projection failure;
- configuration and output hashes;
- a second appropriate integrator before strong scientific conclusions.

## Experiment 10: Equivalence test

The claim

$$
M_F\equiv M_P
$$

requires one of:

- exact conjugacy;
- exact reparameterization;
- a proved approximation with an error bound;
- observational equivalence under a specified map, domain, and tolerance.

Numerical resemblance alone is insufficient.

## Primary outputs

- node-state trajectories;
- edge-activation trajectories;
- metric-deformation trajectories;
- intrinsic distance matrices;
- feedback vector;
- projection correction;
- constraint and tangency residuals;
- retraction magnitude;
- perturbation response;
- computational cost;
- singularity and failure logs.

## Execution authorization

Current authorization:

- $M_0/M_F/M_P$ software verification: complete;
- $M_{FP}$ implementation and software verification: authorized;
- exploratory four-model pilot: blocked;
- confirmatory four-model run: blocked;
- scientific feedback-versus-projection claims: blocked;
- $M_F\equiv M_P$ claim: unverified;
- physical or ontological claims: not authorized.
