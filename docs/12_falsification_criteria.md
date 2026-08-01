# Falsification Criteria

## Purpose

This document defines in advance what would weaken, narrow, or reject the project's mathematical and scientific hypotheses.

The project must not reinterpret every possible outcome as support.

## Hypothesis classes

### Mathematical hypothesis

A coherent nonlinear dynamic relational constraint geometry can be defined with:

- a valid intrinsic metric;
- well-posed projected dynamics;
- preserved admissibility constraints;
- presentation equivariance;
- controlled non-collapse behavior;
- identifiable local, geometric, and collective mechanisms.

### Scientific hypothesis

For at least some real or established physical systems, the full geometry provides a robust explanatory or predictive advantage over simpler alternatives.

### Ontological conjecture

Objective reality has a pluralistic-monist organization represented usefully by local dynamics under global relational constraints.

The ontological conjecture is not directly validated by success on a small benchmark.

## Mathematical rejection conditions

The current formalism must be revised or rejected if any essential result holds:

1. the proposed shortest-path construction fails to define a metric under the intended assumptions;
2. the projection is nonunique in ordinary operating regimes;
3. the vector field is not locally well posed without ad hoc regularization;
4. constraint preservation fails even with exact arithmetic under the stated equations;
5. the barrier does not imply a positive finite-energy separation bound;
6. equivariance fails under admissible relabelings or coordinate changes;
7. topology changes make the state space or dynamics undefined without replacing the formalism;
8. the local, geometric, and collective terms are structurally unidentifiable.

A restricted theorem on a smaller domain may rescue a narrower model, but not the original unrestricted claim.

## Novelty rejection conditions

The mathematical novelty claim must be withdrawn if:

1. the full model is a reparameterization of an existing constrained adaptive-network model;
2. dynamic metric variables are observationally equivalent to ordinary dynamic edge weights;
3. collective projection is equivalent to a standard penalty or multiplier method in every tested and derived regime;
4. the purported synthesis already appears in prior work with substantially the same equations and scope;
5. differences are terminological or philosophical rather than mathematical.

A valid implementation, synthesis, or interpretive contribution may remain after novelty is rejected.

## Scientific weakening conditions

The scientific hypothesis is weakened if:

1. the full model performs no better than $M_0$ through $M_3$ under matched budgets;
2. improvements disappear after tuning baselines fairly;
3. improvements occur only on training or exploratory cases;
4. results are not stable across seeds, solvers, or tolerances;
5. global correction magnitude does not track coherence boundaries as predicted;
6. dynamic geometry provides no measurable contribution beyond topology adaptation;
7. performance gains arise solely from additional parameters or privileged inputs;
8. structural interventions produce no response distinct from null models;
9. the model fails to reproduce established limiting systems.

## Scientific rejection conditions

For a selected application domain, reject the strong scientific claim if:

1. no preregistered discriminating prediction survives confirmatory testing;
2. simpler models match or exceed predictive performance and stability;
3. the full model cannot be fit or simulated without unstable singular behavior;
4. independent reproduction fails under the published protocol;
5. claimed effects disappear under structural permutation or matched exogenous-control tests.

Rejection in one domain does not automatically reject the mathematical framework in every domain.

## Central signature test

The current central signature is:

> Local dynamics dominate ordinary evolution, while collective correction becomes large near coherence boundaries, topological transitions, or collapse barriers.

Operationally, for

$$
\chi_i(t)
=
\frac{\|F_i^{\mathrm{collective}}(t)\|}
{\|F_i^{\mathrm{local}}(t)\|+\epsilon},
$$

the confirmatory test must specify in advance:

- what counts as an ordinary regime;
- what counts as a coherence boundary;
- the expected direction and size of change in $\chi_i$;
- the aggregation across nodes and time;
- the independent inferential units;
- the comparison baselines.

The signature is not supported merely because $\chi_i$ occasionally becomes large.

## Barrier test

The barrier claim requires both mathematical and numerical evidence.

### Mathematical requirement

Derive conditions under which finite energy $E_0$ implies

$$
\ell_e(t)\geq\ell_{\min}(E_0)>0.
$$

### Numerical tripwires

Reject a numerical run if:

- an edge crosses the derived lower bound beyond declared tolerance;
- the barrier is crossed only because of time-step size;
- energy or constraint errors diverge before the event;
- the result changes qualitatively under a tighter solver tolerance.

## Equivariance test

For each admissible permutation $P$, require

$$
\Phi_t(PZ_0)=P\Phi_t(Z_0)
$$

within declared numerical tolerance.

Failure indicates that node labels or implementation order affect the purported physical result.

## Structural intervention tests

The following interventions must remain distinct:

1. permute graph structure while holding state and parameters fixed;
2. permute state while holding graph and parameters fixed;
3. alter collective variables while holding local structure fixed;
4. relabel the entire system without changing physical structure.

These interventions must not be treated as interchangeable controls.

## Stop rules

Pause expansion of the framework when any condition holds:

- a foundational proof obligation fails;
- two supposedly different mechanisms are shown equivalent;
- benchmark failures are repeatedly explained only by adding unplanned complexity;
- no unique prediction remains after fair baseline comparison;
- numerical instability prevents reproducible evaluation;
- the claim ledger cannot state the current hypothesis precisely.

At a stop rule, the next action is diagnosis and claim reduction, not a larger experiment.

## Evidence that would justify continuation

Proceed toward stronger claims only after at least one result is established:

- a new theorem with independently checked proof;
- a strict generalization of established model families;
- a robust and preregistered dynamical signature;
- improved prediction or stability on a physical anchor;
- a useful invariant, curvature, or decomposition unavailable to the baselines.

## Ontological restraint

Even complete success on the mathematical and scientific program would establish only that the framework is useful and empirically adequate within tested domains.

It would not prove

$$
\text{model}=\text{absolute reality}.
$$

The apophatic principle remains a restriction on interpretation, not a device for immunizing the hypothesis against failure.
