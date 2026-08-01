# Experimental Plan

## Status

All four contract-v1.0 models are implemented and unit-tested:

$$
M_0,\qquad M_F,\qquad M_P,\qquad M_{FP}.
$$

No comparative scientific experiment is authorized until the Phase 5 protocol is complete and frozen.

## Canonical models

### $M_0$

Local/adaptive substrate without collective feedback or projection.

### $M_F$

$M_0$ plus endogenous collective feedback.

### $M_P$

$M_0$ proposal projected onto

$$
\Gamma(Z)=\frac13x^Tx-c_0=0,
$$

with projected RK4 stages and mandatory radial retraction.

### $M_{FP}$

The feedback proposal

$$
F_{\mathrm{proposal}}=F_0+F_F
$$

followed by node projection, with feedback and projection separately observable.

At the same regular full state,

$$
\boxed{f_{FP}=f_P},
$$

while feedback remains in $s$ and $q$.

## Experiment 0: Code-equation alignment

### Completed at software level

- independent derivative and RK4 parity for $M_0/M_F$;
- exact $M_F(\chi=\eta_2=\rho=0)=M_0$ reduction;
- $M_P$ projector identities, tangency, retraction, singular handling, and independent parity;
- $M_{FP}$ feedback/projection decomposition and independent parity;
- same-state identity $f_{FP}=f_P$;
- retained $s/q$ feedback in $M_{FP}$;
- exact zero-feedback $M_{FP}=M_P$ reduction;
- permutation tripwires for all four models;
- model, contract, source, configuration, and mechanism output labels.

### Remaining before scientific execution

- frozen comparative hypotheses and metrics;
- final parameter and initial-condition manifests;
- alternate-integrator policy;
- exploratory and confirmatory partition;
- structural inferential units;
- exclusion, stop, and failure rules;
- raw-output checksum and archival manifest.

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

## Experiment 4: $M_P$ versus $M_{FP}$

### Binding structural result

At the same regular full state,

$$
P_T[-\chi c(x)x]=0,
$$

hence

$$
\boxed{f_{FP}=f_P}.
$$

This does not imply trajectory identity because $M_{FP}$ retains feedback in $s$ and $q$, which can change later conductances and node proposals.

### Primary question

Under which parameter regimes and observation maps does retained adaptive-substrate feedback make $M_{FP}$ distinguishable from $M_P$?

### Interaction residual

Under a preregistered comparison map, define

$$
R_{FP}
=
\Delta(M_{FP},M_0)
-
\Delta(M_F,M_0)
-
\Delta(M_P,M_0).
$$

The exact $\Delta$, aggregation, and tolerance must be frozen before results are generated.

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

after undoing the permutation. Software-level permutation tests pass for all four models.

## Experiment 9: Numerical tripwires

Require:

- decreasing discrepancy under step refinement;
- agreement with independently written reference paths;
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
- local proposal, feedback vector, and combined proposal;
- projection correction;
- constraint and tangency residuals;
- retraction magnitude;
- perturbation response;
- computational cost;
- singularity and failure logs.

## Phase 5 protocol requirements

Before a pilot, freeze:

- primary and secondary hypotheses;
- observation maps and equivalence tolerances;
- parameter and initial-condition manifests;
- intervention and ablation schedule;
- structural inferential units;
- metrics and uncertainty treatment;
- refinement and alternate-integrator rules;
- exclusion and stop rules;
- pilot/confirmatory separation;
- source-commit, configuration-hash, output-checksum, and archival policy;
- claim-promotion and falsification rules.

## Execution authorization

Current authorization:

- all four software-verification programs: complete;
- Phase 5 protocol design and review: authorized;
- exploratory four-model pilot: blocked until protocol freeze;
- confirmatory four-model run: blocked;
- scientific feedback-versus-projection claims: blocked;
- $M_F\equiv M_P$ claim: unverified;
- physical or ontological claims: not authorized.
