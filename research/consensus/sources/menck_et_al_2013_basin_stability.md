# Consensus Source Note — Menck et al. on Basin Stability

## Citation

Peter J. Menck, Jobst Heitzig, Norbert Marwan, and Jürgen Kurths. “How Basin Stability Complements the Linear-Stability Paradigm.” *Nature Physics* 9 (2013): 89–92. DOI: 10.1038/nphys2516.

## Source classification

- **Field:** physics and nonlinear dynamics
- **Subfield:** multistability, resilience, basins of attraction, complex systems
- **Source type:** original methodological and numerical paper
- **Publication status:** peer reviewed
- **Primary or secondary:** primary

## Exact contribution used

The paper argues that local linearization is insufficient for assessing stability against large perturbations in multistable systems. It introduces **basin stability**, a nonlocal and nonlinear measure related to the volume of an attractor’s basin of attraction, and applies it to model systems and network ensembles.

The load-bearing result for CS1 is that whether a perturbed state returns to a chosen attractor depends on where that state lies in the global basin geometry, not merely on local eigenvalues at the attractor. Thus two states in the same dynamical system can have different long-term outcomes because they occupy different regions of state space.

## Claim type

- mathematical definition;
- numerical method;
- empirical/modeling result within specified dynamical systems.

## Assumptions and domain

- a specified deterministic dynamical system;
- one or more attractors and their basins of attraction;
- a declared region or probability distribution from which perturbations are sampled;
- convergence or classification criteria for assigning trajectories to attractors;
- a finite numerical sampling procedure in practical applications.

Basin stability depends on the sampling measure and region. It is not an intrinsic scalar of an attractor independent of how perturbations are distributed.

## Evidence and verification status

- **Derivation or protocol:** basin membership is estimated by sampling perturbed initial conditions and integrating their trajectories.
- **Data or code available:** not assessed in this initial note.
- **Independent replication or reproduction:** the measure has become a standard method in nonlinear and network stability research; direct reproduction is not performed here.
- **Known counterexamples or exceptions:** local linear stability can be adequate for sufficiently small perturbations; basin stability does not by itself describe transient time, internal basin geometry, or noise-driven escape.

## Established terminology

- multistability;
- attractor;
- basin of attraction;
- local linear stability;
- basin stability;
- large perturbation;
- resilience.

## Mapping into ARG

### ARG claim IDs affected

- `CS1-C01`
- `CS1-C02`
- `CS1-C04`
- `CS1-C11`
- `CS1-C13`
- ARG language concerning persistence as state–structure compatibility.

### Proposed mapping

| Source object | ARG object | Mapping type | What is preserved | What is not preserved |
|---|---|---|---|---|
| dynamical system and attractor landscape | relational transition structure | specialization | global possibilities and basins | arbitrary changing structure or ontology |
| perturbed initial condition | state | exact translation within the model | phase-space location | semantic identity or organization |
| basin membership | successful persistence/return criterion | specialization | whether the state reaches the selected attractor | pattern continuity during the transient |
| basin stability | population-level robustness measure | partial translation | probability or volume of successful return | universal compatibility or individual identity |

## Equation or theorem mapping

For an attractor $A$ with basin $\mathcal B(A)$ and a declared perturbation density $\rho(x)$, basin stability can be represented as

$$
S_{\mathcal B}(A;\rho)
=
\int \mathbf 1_{\mathcal B(A)}(x)\,\rho(x)\,dx.
$$

A Monte Carlo estimator is

$$
\widehat S_{\mathcal B}
=
\frac{1}{N}\sum_{k=1}^{N}
\mathbf 1_{\mathcal B(A)}(x_k),
\qquad x_k\sim\rho.
$$

In ARG notation, for fixed structure $B$ and target persistent regime $\mathcal A_B$,

$$
P_{\mathrm{basin}}(B;\rho)
=
\Pr_{x\sim\rho}
\bigl[\Phi_B^t(x)\rightarrow\mathcal A_B\bigr].
$$

### Mapping conditions

The target regime, sampling measure, observation horizon, convergence criterion, and fixed dynamical law must all be declared. This is a measure of basin robustness, not a universal measure of persistence.

## Cross-field implications

Basin stability supplies a nonlinear geometric counterpart to linear modal and nonmodal analysis. It shows that state location relative to basin boundaries is an established predictor of long-term outcome. In biology or philosophy, analogous language about “remaining the same” is only an analogy unless attractors, perturbation distributions, and observables are operationally defined.

## Consensus assessment

- **Proposed grade:** C4 for the scoped claim that large-perturbation outcomes in multistable systems depend on global basin geometry and initial-state location.
- **Scoped consensus statement:** In a multistable dynamical system, persistence in or return to a selected attractor is a joint property of the dynamics, the initial condition, and the basin geometry; local linear stability alone need not determine robustness to large perturbations.
- **Reason for grade:** direct definition and numerical demonstration in a primary paper, followed by broad field uptake.
- **What remains disputed:** the appropriate sampling measure, perturbation region, target attractor, and interpretation in each application.

## Novelty implication for ARG

- nonlinear state–structure dependence through basin location is established;
- “the same structure preserves some states and destroys others” is not novel in multistable dynamics;
- an ARG contribution would need to exceed basin membership, basin-volume, transient, and transfer-operator measures.

## Experiment decision

- **Is a new experiment needed?** no to establish that state location within a basin landscape controls large-perturbation persistence.
- **Exact unresolved question:** whether a representation-robust ARG quantity predicts persistence across changing relational structures beyond basin-based predictors.
- **Why existing results do not already answer it:** basin stability normally assumes a specified dynamical representation and target attractor; it does not provide a universal cross-representation invariant.
- **Minimum discriminating experiment or proof:** show held-out predictive improvement over basin membership, distance-to-boundary, and basin-stability baselines under explicitly equivalent representations.

## Required project updates

- [x] consensus table
- [x] translation dictionary
- [x] novelty matrix
- [x] disagreement map
- [ ] formalism after broader audit

## Reviewer check

- [x] Source supports the scoped claim.
- [x] Claim type is correct.
- [x] Mapping preserves dependence on the perturbation measure.
- [x] Novelty implication follows from direct comparison.
- [x] Proposed experiment is genuinely residual.
