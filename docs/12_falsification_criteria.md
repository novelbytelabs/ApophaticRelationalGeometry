# Falsification Criteria

## Purpose

This document defines in advance what would weaken, narrow, or reject ARG's mathematical and scientific hypotheses.

The project must not reinterpret every possible outcome as support.

## Current claim ceiling

$$
\boxed{
M_F\ \text{implemented and unit-tested};
\quad
M_P,\ M_{FP},\ \text{and }M_F\equiv M_P\ \text{unverified}.
}
$$

Therefore current falsification work may address $M_F$ implementation integrity and $M_0/M_F$ mechanism design. Projected scientific claims remain blocked.

## Hypothesis classes

### Feedback hypothesis

An endogenous system statistic changes constituent transitions through an explicit substrate path.

The current executable implements this at prototype level.

### Projection hypothesis

An explicitly defined admissible geometry removes the inadmissible component of proposed motion while preserving declared constraints.

This remains unimplemented and unverified.

### Equivalence hypothesis

Collective feedback and admissibility projection are mathematically or observationally equivalent on a declared domain.

No such equivalence is currently established.

### Scientific hypothesis

For at least one established or empirical system, one or more ARG mechanisms provide robust explanatory or predictive value beyond simpler alternatives.

### Ontological conjecture

Objective reality has a pluralistic-monist organization represented usefully by local processes under relational whole-system organization.

The ontological conjecture is not validated by a small benchmark.

## $M_F$ implementation rejection conditions

The current feedback implementation must be corrected or its claim withdrawn if:

1. code does not compute the documented $c(x)$;
2. any declared path $x\to c(x)\to(\dot x,\dot s,\dot q)$ is absent;
3. undeclared collective paths exist;
4. removing feedback coefficients does not recover the frozen $M_0$ equations;
5. permutation equivariance fails in a regime where it is claimed;
6. numerical conclusions disappear under reasonable solver refinement;
7. unit tests pass after deliberate mutation of the mechanism they are intended to guard.

## Prototype-level downward claim limits

The label “implemented prototype-level downward feedback/constraint” must not be promoted to macro-level causal autonomy unless all of the following are separately supported:

- organization dependence;
- substrate-level counterfactual adequacy;
- invariance under admissible presentation changes;
- transport across systems, scales, or realizations;
- defeat of simpler alternative models;
- evidence that the collective variable is not merely a convenient reparameterization.

Failure of any required gate keeps the stronger claim unverified.

## $M_P$ mathematical rejection conditions

The projected formalism must be revised, narrowed, or rejected if:

1. no nontrivial admissible set can be defined without circularly encoding the desired correction;
2. the projection is nonunique in ordinary operating regimes;
3. the constraint Jacobian loses rank without a declared fail-closed behavior;
4. the projected vector field is not locally well posed on its claimed domain;
5. continuous-time constraint preservation fails under the documented equations;
6. inequality active-set behavior is undefined or inconsistent;
7. equivariance fails under the declared transformation class;
8. the proposed projection is merely a relabeled feedback or penalty term without an independent geometric definition.

A restricted theorem may rescue a narrower model, not the unrestricted claim.

## Projected-implementation rejection conditions

An implementation may not be called $M_P$ or projected geometry unless:

$$
D_{\Gamma,H}
\land_{FC}
I_{\Pi}
\land_{FC}
T_{\mathrm{preserve}}
\land_{FC}
E_{\mathrm{code}}
\land_{FC}
S_{\mathrm{path}}
$$

passes.

Reject the implementation claim if:

- $\Gamma/H$ are not explicit;
- the code contains no projector;
- the documented projector differs from the executable;
- constraint error does not converge under refinement;
- singular systems continue silently;
- the correction cannot be decomposed from the local proposal;
- an independent reference implementation disagrees beyond tolerance.

## $M_{FP}$ rejection conditions

Reject the combined-mechanism implementation if:

1. removing feedback does not recover $M_P$;
2. removing projection does not recover $M_F$;
3. removing both does not recover $M_0$;
4. feedback and projection contributions cannot be separately measured;
5. the same collective term is counted twice without explicit justification;
6. ordering choices are hidden or changed after results are observed.

## Equivalence rejection conditions

Reject a global claim

$$
M_F\equiv M_P
$$

if any admissible initial state, parameter set, perturbation, or observation distinguishes the models.

Do not infer equivalence from:

- similar plots;
- matching aggregate statistics alone;
- one parameter regime;
- one finite time window;
- poor observation resolution;
- underpowered tests.

Permitted narrower outcomes include:

- local equivalence near a fixed point;
- asymptotic equivalence;
- approximation with an error bound;
- observational equivalence under a stated map;
- parameter-specific equivalence.

Each must be labeled with its exact scope.

## Novelty rejection conditions

Withdraw mathematical novelty if:

1. the full family is a reparameterization of an existing constrained adaptive-network model;
2. dynamic metric variables are observationally equivalent to ordinary dynamic edge weights;
3. projection adds nothing beyond a standard multiplier or penalty method;
4. the synthesis already appears in prior work with substantially the same equations and scope;
5. differences are terminological or philosophical rather than mathematical.

A valid implementation, synthesis, or interpretive contribution may remain.

## Scientific weakening conditions

The scientific hypothesis is weakened if:

1. $M_F$ performs no better than $M_0$ under matched conditions;
2. $M_P$ performs no better than $M_0$ or a standard constraint method;
3. $M_{FP}$ adds no value beyond its simpler components;
4. improvements disappear after fair tuning of alternatives;
5. improvements occur only on exploratory or training cases;
6. results are unstable across seeds, solvers, tolerances, or structural units;
7. dynamic geometry adds no measurable contribution beyond adaptive weights;
8. gains arise solely from extra parameters or privileged inputs;
9. structural interventions produce no response distinct from null models;
10. ARG fails to reproduce established limiting systems.

## Scientific rejection conditions

For a selected domain, reject the strong claim if:

1. no preregistered discriminating prediction survives confirmatory testing;
2. simpler models match or exceed predictive performance and stability;
3. the relevant ARG model cannot be simulated without unstable singular behavior;
4. independent reproduction fails;
5. claimed effects disappear under structural permutation, exogenous-statistic, or matched-penalty controls.

Rejection in one domain does not automatically reject the mathematical family in every domain.

## Separate signature tests

### Feedback signature

For

$$
\chi_i^F(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon},
$$

predefine:

- the intervention that changes collective organization;
- the expected direction and size of response;
- aggregation across nodes and time;
- independent inferential units;
- comparison with $M_0$ and exogenous-statistic controls.

A large feedback coefficient or ratio does not by itself establish causal autonomy.

### Projection signature

For

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{0,i}(t)+F_{F,i}(t)\|+\epsilon},
$$

predefine:

- the admissibility boundary;
- expected correction direction;
- constraint residual behavior;
- comparison with multiplier and penalty methods;
- singular and near-singular regimes.

This test is blocked until $M_P$ exists.

## Barrier test

The barrier claim requires both mathematical and numerical evidence.

### Mathematical requirement

Derive conditions under which finite energy $E_0$ implies

$$
\ell_e(t)\geq\ell_{\min}(E_0)>0.
$$

### Numerical tripwires

Reject a run if:

- an edge crosses the derived lower bound beyond declared tolerance;
- crossing is caused by time-step size;
- energy or constraint errors diverge first;
- the result changes qualitatively under tighter tolerance.

## Equivariance test

For each admissible permutation $P$, require

$$
\Phi_t(PZ_0)=P\Phi_t(Z_0)
$$

within declared numerical tolerance.

Run this separately for every implemented model.

## Structural intervention tests

Keep distinct:

1. graph intervention with state fixed;
2. state intervention with graph fixed;
3. collective-statistic intervention;
4. projection-constraint intervention;
5. pure relabeling without physical change.

These controls are not interchangeable.

## Stop rules

Pause expansion when:

- a foundational proof obligation fails;
- model definitions cannot be frozen;
- two supposedly different mechanisms are equivalent and the distinction collapses;
- benchmark failures are answered only by unplanned complexity;
- no unique prediction remains after fair alternatives;
- numerical instability prevents reproducibility;
- the claim ledger cannot state the current hypothesis precisely.

At a stop rule, diagnose and reduce the claim rather than enlarging the experiment.

## Evidence that justifies continuation

Proceed toward stronger claims only after at least one result is established:

- a new theorem with independent checking;
- a strict generalization of an established family;
- a robust preregistered dynamical signature;
- improved prediction or stability on a physical anchor;
- a useful invariant, curvature, or mechanism decomposition unavailable to alternatives.

## Ontological restraint

Even complete mathematical and scientific success would establish only usefulness and empirical adequacy within tested domains.

It would not prove

$$
\text{model}=\text{absolute reality}.
$$

The apophatic principle is a restriction on interpretation, not a device for immunizing ARG against failure.
