# ARG Mechanism Sandbox V1

## Purpose

This sandbox isolates the smallest mechanisms needed to test the candidate synthesis. It is not a universe simulation and not a proof of ontology.

## Model family

### Model A: local fixed graph

State:

$$
x_i(t)\in\mathbb R.
$$

Dynamics:

$$
\dot x_i
=
f_i(x_i)
+
\sum_jw_{ij}(x_j-x_i).
$$

Purpose: ordinary local-network baseline.

### Model B: global constraint only

Use a fixed graph and project the local vector field onto:

$$
\Gamma(x)=0.
$$

Purpose: isolate the effect of global admissibility.

### Model C: dynamic relations

Let:

$$
\dot s_{ij}
=
g(s_{ij},x_i,x_j).
$$

Purpose: test whether adaptive topology changes persistence.

### Model D: dynamic metric

Let:

$$
\dot q_{ij}
=
h(q_{ij},x_i,x_j),
$$

with:

$$
\ell_{ij}
=
\frac{\exp(q_{ij})}{\sigma(s_{ij})}
\sqrt{\epsilon^2+(x_i-x_j)^2}.
$$

Purpose: isolate state–geometry feedback.

### Model E: full local–global fabric

Combine:

- nonlinear local dynamics;
- dynamic relations;
- dynamic metric;
- collective state;
- hard or soft global coherence;
- optional non-collapse barrier.

Purpose: test the complete mechanism.

### Model F: prime-derived support

Replace an arbitrary graph with a prime- or arithmetic-derived relational graph while keeping the same dynamics.

Purpose: test whether prime structure adds anything beyond generic graph properties.

## Common measurements

- persistence duration;
- escape or dissolution time;
- coherence energy;
- path distance;
- connectivity;
- local/global influence ratio;
- residual correction magnitude;
- sensitivity to state placement;
- sensitivity to structure permutation;
- Lyapunov or perturbation growth where appropriate;
- computational cost.

## Core comparisons

$$
\text{full model}
\quad\text{versus}\quad
\text{fixed geometry},
$$

$$
\text{aligned state–structure}
\quad\text{versus}\quad
\text{permuted alignment},
$$

$$
\text{global correction}
\quad\text{versus}\quad
\text{local-only},
$$

$$
\text{prime-derived graph}
\quad\text{versus}\quad
\text{degree-matched controls}.
$$

## Non-negotiable scientific constraints

The conversation established a strict experimental doctrine:

- no oracle labels;
- no synthetic confirmation disguised as evidence;
- no selective metric changes after seeing results;
- use tripwires;
- use independent parity checks;
- replace weak sign-flip controls with structural permutations;
- separate graph, operator, and initial-state permutations;
- freeze metrics in code;
- use many permutations when feasible;
- lock the environment;
- separate exploration from confirmatory analysis.

## Minimal sequence

1. Prove that each model is well-defined.
2. Implement deterministic small systems.
3. Verify numerical parity against independent formulas.
4. Run nulls and tripwires.
5. Test structure-state compatibility.
6. Add dynamic geometry only if earlier stages are sound.
7. Add prime-derived support last.

## What would count as progress

Progress is not visually complex dynamics.

Progress is one of:

- a proved property;
- a falsified hypothesis;
- a robust effect surviving controls;
- a reduction to known mathematics;
- a clearer boundary on the claim.

## What would not count

- attractive plots without nulls;
- one chosen initial condition;
- post hoc metrics;
- a prime graph outperforming a poorly matched random graph;
- metaphysical interpretation of generic nonlinear behavior;
- claiming “emergence” because a pattern appears.

## Sandbox status

The sandbox is a controlled test environment for the candidate geometry. It should remain small until the mechanism survives falsification attempts.
