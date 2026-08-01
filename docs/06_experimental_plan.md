# Experimental Plan

## Experiment 1: Local versus collective influence

Measure

$$
\chi_i(t)
=
\frac{\|F_i^{\mathrm{collective}}\|}
{\|F_i^{\mathrm{local}}\|+\epsilon}.
$$

Test whether local influence dominates away from coherence boundaries while collective correction grows near structural failure.

## Experiment 2: Dynamic-geometry ablation

Compare:

1. Full model.
2. Frozen $q$.
3. Frozen $s$.
4. Frozen $q$ and $s$.
5. No collective feedback.
6. Static graph with parameter-matched node dynamics.

## Experiment 3: Structural intervention

Permute graph incidence while holding node states and parameters fixed. Treat structural permutations as inferential units.

## Experiment 4: State intervention

Permute initial states while holding graph structure and parameters fixed.

## Experiment 5: Collective-mode intervention

Replace $c(x)$ with a matched exogenous signal to determine whether endogenous whole-part closure adds measurable behavior.

## Experiment 6: Relabeling tripwire

Randomly relabel nodes and require identical invariant trajectories after undoing the permutation.

## Experiment 7: Numerical tripwires

Require agreement across time steps and an independently written reference right-hand side.

## Primary outputs

- State trajectories.
- Edge activation trajectories.
- Metric deformation trajectories.
- Intrinsic distance matrices.
- Coherence energy.
- Lyapunov estimates.
- Intervention response.
- Local-versus-global influence ratio.
