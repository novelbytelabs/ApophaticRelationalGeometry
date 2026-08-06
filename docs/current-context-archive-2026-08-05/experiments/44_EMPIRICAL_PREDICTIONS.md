# Candidate Empirical Predictions

## Status

These are candidate consequences of the model. None has been established as a physical prediction.

Each item must be paired with a baseline and a failure condition.

## 1. Structure–state compatibility predicts persistence

Prediction:

$$
\kappa(B,x)
$$

predicts persistence duration beyond separate features of $B$ and $x$.

Baseline:

- topology-only model;
- state-only model;
- additive topology-plus-state model without interaction.

Failure:

The interaction or compatibility term adds no out-of-sample predictive value.

## 2. Alignment-sensitive persistence

Destroying state placement while preserving state distribution and graph structure reduces or changes persistence.

Baseline:

- pure node relabeling, which must leave results invariant;
- state permutations;
- graph permutations.

Failure:

Destructive permutations do not differ from aligned conditions after confound matching.

## 3. Boundary amplification of global correction

Prediction:

$$
\chi_i
=
\frac{\|F_i^{\mathrm{whole}}\|}
{\|F_i^{\mathrm{local}}\|+\epsilon}
$$

increases near active global constraints or viability boundaries.

Baseline:

A random correction field with matched norm.

Failure:

$\chi_i$ does not track boundary proximity or is coordinate-dependent.

## 4. Dynamic geometry improves recovery

After perturbation, adaptive $s_e$ and $q_e$ improve recovery or persistence compared with fixed effective couplings.

Baseline:

A fixed graph tuned to match mean conductance.

Failure:

Dynamic geometry provides no robust advantage or only overfits the tested perturbation.

## 5. Hysteresis or path dependence

Because geometry carries memory, two systems with the same current $x$ but different $s,q,\theta,c$ histories may evolve differently.

Baseline:

A Markov model using $x$ alone.

Failure:

History variables add no predictive value once current state is controlled.

## 6. Topological gating

Certain graph-state alignments strongly permit or block persistent dynamics.

Baseline:

Degree-, weight-, and spectrum-matched graphs.

Failure:

The effect reduces to one ordinary graph statistic.

## 7. Global modes without central controller

Collective patterns can constrain local motion without a special central node.

Baseline:

A centralized controller model and a local-only model.

Failure:

The same behavior requires explicit centralized coupling or is reproduced by ordinary local diffusion.

## 8. Non-collapse

With the barrier:

$$
U_{\mathrm{barrier}}
=
\sum_e\frac{B_e}{\ell_e^{p_e}},
$$

finite-energy trajectories maintain:

$$
\ell_e>0.
$$

Baseline:

Steep finite repulsion.

Failure:

The divergent barrier is unnecessary, unstable, or empirically indistinguishable from finite alternatives.

## 9. Geometry–state reciprocity

Perturbing state changes intrinsic distances, which in turn changes subsequent state propagation.

Baseline:

A fixed metric with matched instantaneous coupling.

Failure:

Metric changes do not improve prediction or control.

## 10. Prime-derived effects

A prime-derived relational graph may show distinctive persistence, phase structure, or alignment sensitivity.

Baseline:

- degree-matched random graphs;
- multiplicative but non-prime graphs;
- shuffled arithmetic labels;
- spectral-matched surrogates.

Failure:

The effect disappears under matched controls or is not size-stable.

## 11. Scale-dependent one–many balance

At different coarse-graining levels, local and global influence ratios change but compatible observables remain stable.

Baseline:

Arbitrary coarse-graining.

Failure:

Results depend entirely on chosen scale without invariant structure.

## 12. Distributed memory

Persistent relational variables can store information not contained in node states alone.

Baseline:

State-only reconstruction.

Failure:

Relation variables provide no recoverable or predictive information.

## 13. Constraint versus transmission signature

A global constraint may alter joint admissibility without a propagating local signal.

This is mathematically possible, but a physical claim requires operational timing and no-signaling analysis.

Failure:

The apparent effect is fully explained by hidden direct coupling, numerical projection, or preprocessing.

## 14. Priority

The first three scientifically tractable predictions are:

1. alignment-sensitive persistence;
2. boundary amplification of global correction;
3. dynamic-geometry recovery advantage.

The prime and physics-level predictions must wait.
