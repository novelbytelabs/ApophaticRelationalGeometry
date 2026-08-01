# Falsification Criteria

## Purpose

This document defines in advance what would weaken, narrow, or reject ARG's mathematical and scientific hypotheses.

The project must not reinterpret every possible outcome as support.

## Current claim ceiling

$$
\boxed{
M_0,M_F,M_P,M_{FP}\ \text{implemented and unit-tested};
\quad
M_F\equiv M_P\ \text{unverified}.
}
$$

Implementation claims have passed their current software gates. No comparative scientific result has been established.

## Hypothesis classes

### Feedback hypothesis

An endogenous system statistic changes constituent transitions through an explicit substrate path.

This is implemented at prototype level in $M_F$ and $M_{FP}$.

### Projection hypothesis

An explicitly defined admissible geometry removes the inadmissible component of proposed motion while preserving declared constraints.

The equality-only constant-amplitude version is implemented in $M_P$ and $M_{FP}$. Its scientific relevance remains unverified.

### Combined-mechanism hypothesis

Feedback retained in the adaptive substrate can make $M_{FP}$ dynamically distinguishable from $M_P$ even though

$$
f_{FP}(Z)=f_P(Z)
$$

at the same regular full state.

This trajectory-level hypothesis has not been tested scientifically.

### Equivalence hypothesis

Collective feedback and admissibility projection are mathematically or observationally equivalent on a declared domain.

No such equivalence is currently established.

### Scientific hypothesis

For at least one established or empirical system, one or more ARG mechanisms provide robust explanatory or predictive value beyond simpler alternatives.

### Ontological conjecture

Objective reality has a pluralistic-monist organization represented usefully by local processes under relational whole-system organization.

The ontological conjecture is not validated by a small benchmark.

---

# Implementation rejection conditions

## $M_0$

Correct or withdraw the $M_0$ implementation claim if:

1. any value computed from $c(x)$ enters its transition equations;
2. its documented right-hand side differs from code;
3. permutation equivariance fails in a claimed regime;
4. independent-reference parity fails;
5. invalid or nonfinite inputs continue silently.

## $M_F$

Correct or withdraw the $M_F$ implementation claim if:

1. code does not compute the documented $c(x)$;
2. any declared path $x\to c(x)\to(\dot x,\dot s,\dot q)$ is absent;
3. undeclared collective paths exist;
4. removing feedback coefficients does not recover $M_0$;
5. independent parity or regression tests fail;
6. mechanism tests still pass after deliberate path mutation.

## $M_P$

Correct or withdraw the $M_P$ implementation claim if:

1. $\Gamma/H$ are not explicit;
2. the code contains no declared projector;
3. the documented projector differs from the executable;
4. tangency or post-retraction preservation fails beyond tolerance;
5. singular systems continue silently;
6. proposal and correction cannot be decomposed;
7. an independent reference implementation disagrees beyond tolerance;
8. refinement does not reduce raw constraint drift in the declared test.

## $M_{FP}$

Correct or withdraw the $M_{FP}$ implementation claim if:

1. the unprojected proposal does not agree with $M_F$;
2. setting $\chi=\eta_2=\rho=0$ does not recover $M_P$;
3. removing feedback and projection does not recover $M_0$;
4. local proposal, feedback, combined proposal, projection correction, and retraction cannot be measured separately;
5. the radial node-feedback term is not annihilated as declared;
6. $s/q$ feedback is absent or incorrectly signed;
7. ordering choices are hidden or changed after results are observed;
8. independent derivative or projected-step parity fails.

Passing these gates licenses only implementation-level claims.

---

# Prototype-level downward claim limits

The label “implemented prototype-level downward feedback/constraint” must not be promoted to macro-level causal autonomy unless all of the following are separately supported:

- organization dependence;
- substrate-level counterfactual adequacy;
- invariance under admissible presentation changes;
- transport across systems, scales, or realizations;
- defeat of simpler alternative models;
- evidence that the collective variable is not merely a convenient reparameterization.

Failure of any required gate keeps the stronger claim unverified.

---

# Mathematical rejection conditions

## Projected formalism

Revise, narrow, or reject the projected formalism if:

1. no nontrivial admissible set can be defined without circularly encoding the desired correction;
2. projection is nonunique in ordinary operating regimes;
3. the constraint Jacobian loses rank without declared fail-closed behavior;
4. the projected vector field is not locally well posed on its claimed domain;
5. continuous-time preservation fails under the documented equations;
6. future inequality active-set behavior is undefined or inconsistent;
7. equivariance fails under the declared transformation class;
8. projection is merely a relabeled feedback or penalty term without an independent geometric definition.

A restricted theorem may rescue a narrower model, not the unrestricted claim.

## Same-state identity

The contract-v1.0 identity

$$
\boxed{f_{FP}=f_P}
$$

must be restricted to the same regular full state and node derivative.

Reject any inference that it establishes identical trajectories if $s/q$ trajectories differ or later node proposals diverge.

---

# Equivalence rejection conditions

Reject a global claim

$$
M_F\equiv M_P
$$

if any admissible initial state, parameter set, perturbation, or declared observation distinguishes the models.

Do not infer equivalence from:

- similar plots;
- matching aggregate statistics alone;
- one parameter regime;
- one finite time window;
- poor observation resolution;
- underpowered tests;
- the identity $f_{FP}=f_P$, which concerns a different comparison and only a same-state node derivative.

Permitted narrower outcomes include:

- local equivalence near a fixed point;
- asymptotic equivalence;
- approximation with an error bound;
- observational equivalence under a stated map;
- parameter-specific equivalence.

Each must be labeled with its exact scope.

---

# Novelty rejection conditions

Withdraw mathematical novelty if:

1. the family is a reparameterization of an existing constrained adaptive-network model;
2. dynamic metric variables are observationally equivalent to ordinary dynamic edge weights;
3. projection adds nothing beyond a standard multiplier or penalty method;
4. the feedback-projection combination already appears in prior work with substantially the same equations and scope;
5. differences are terminological or philosophical rather than mathematical.

A valid implementation, synthesis, diagnostic, or interpretive contribution may remain.

---

# Scientific weakening conditions

The scientific hypothesis is weakened if:

1. $M_F$ performs no better than $M_0$ under matched conditions;
2. $M_P$ performs no better than $M_0$ or a standard constraint method;
3. $M_{FP}$ adds no distinguishable value beyond $M_P$ and $M_F$;
4. improvements disappear after fair tuning of alternatives;
5. improvements occur only on exploratory cases;
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

---

# Signature tests

## Feedback signature

For

$$
\chi_i^F(t)
=
\frac{\|F_{F,i}(t)\|}
{\|F_{0,i}(t)\|+\epsilon},
$$

predefine:

- the intervention that changes collective organization;
- expected response direction and minimum size;
- aggregation across nodes and time;
- independent inferential units;
- comparison with $M_0$ and exogenous-statistic controls.

A large feedback ratio does not by itself establish causal autonomy.

## Projection signature

For

$$
\chi_i^P(t)
=
\frac{\|F_{P,i}(t)\|}
{\|F_{\mathrm{proposal},i}(t)\|+\epsilon},
$$

predefine:

- the admissibility surface;
- expected correction direction;
- constraint-residual behavior;
- comparison with multiplier and penalty methods;
- singular and near-singular regimes.

## Combined signature

Predefine when retained $s/q$ feedback should make $M_{FP}$ distinguishable from $M_P$ under

$$
O_{\mathrm{full}},\quad O_x,\quad O_{sq},\quad O_d.
$$

A difference under one map must not be reported as an unqualified difference under all maps.

---

# Barrier test

The barrier claim requires both mathematical and numerical evidence.

## Mathematical requirement

Derive conditions under which finite energy $E_0$ implies

$$
\ell_e(t)\geq\ell_{\min}(E_0)>0.
$$

## Numerical tripwires

Reject a run if:

- an edge crosses the derived lower bound beyond declared tolerance;
- crossing is caused by time-step size;
- energy or constraint errors diverge first;
- the result changes qualitatively under tighter tolerance.

---

# Equivariance and intervention tests

For each admissible permutation $P$, require

$$
\Phi_t(PZ_0)=P\Phi_t(Z_0)
$$

within declared numerical tolerance.

Keep distinct:

1. graph intervention with state fixed;
2. state intervention with graph fixed;
3. collective-statistic intervention;
4. projection-constraint intervention;
5. pure relabeling without physical change.

These controls are not interchangeable.

---

# Phase 5 stop rules

Pause protocol expansion when:

- a foundational proof obligation fails;
- hypotheses or metrics cannot be frozen;
- two supposedly distinct mechanisms collapse under exact analysis;
- benchmark failures are answered only by unplanned complexity;
- no unique prediction remains after fair alternatives;
- numerical instability prevents reproducibility;
- exploratory and confirmatory cases cannot be separated;
- the claim ledger cannot state the current hypothesis precisely.

At a stop rule, diagnose and reduce the claim rather than enlarging the experiment.

---

# Evidence that justifies continuation

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
