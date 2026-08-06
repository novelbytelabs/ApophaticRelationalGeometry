# Falsification and Experiment Program

## 1. Scientific posture

The philosophy proposes a hypothesis. The mathematics must earn it.

The experimental program is designed to discover whether the proposed mechanisms add explanatory value beyond ordinary nonlinear adaptive-network dynamics.

## 2. Primary hypotheses

### H1: Structure–state compatibility

$$
\boxed{
\text{Persistence depends on compatibility between relational structure
and state placement.}
}
$$

### H2: Dynamic geometry

State-dependent topology or metric feedback produces robust behavior not reproduced by fixed geometry with matched parameters.

### H3: Global admissibility

A global constraint correction changes trajectories in ways not reducible to the local update rule alone.

### H4: Local dominance with boundary amplification

Local terms usually dominate, while global correction grows near coherence or viability boundaries.

### H5: Prime-derived substrate

Prime-derived structure produces reproducible effects that survive graph-matched controls.

## 3. Experimental units

Use ensembles of:

- graph structures;
- state assignments;
- parameter settings;
- perturbations;
- initial conditions.

Do not treat timepoints from one trajectory as independent experimental units.

## 4. Frozen primary endpoints

Candidate primary endpoints:

- persistence duration;
- probability of remaining in a viability set;
- recovery time after perturbation;
- coherence loss;
- constraint correction magnitude;
- change in path geometry;
- prediction error against held-out trajectories.

Choose and freeze one primary endpoint per experiment.

## 5. Structure–state alignment experiment

Construct a graph $B$ and state vector $x$.

Compare:

1. observed or designed alignment $(B,x)$;
2. state-permuted $(B,Px)$;
3. graph-relabeled with states held fixed;
4. degree-preserving edge rewiring;
5. jointly permuted control preserving pure relabeling equivalence.

The pure relabeling control must produce identical results. The destructive permutations should change only the targeted alignment.

## 6. Ablations

Run:

- local-only;
- global-only;
- no dynamic edges;
- no metric dynamics;
- no collective variable;
- no barrier;
- no SHADOW memory;
- no KEEPER correction;
- fixed random graph;
- prime-derived graph;
- matched random graph.

A component earns explanatory status only if its removal causes a robust, preregistered degradation.

## 7. Null models

Nulls must preserve relevant confounds.

Examples:

- degree sequence;
- weight distribution;
- connectedness;
- spectral density where feasible;
- state marginal distribution;
- energy;
- timescale distribution;
- parameter count.

A random graph is not a valid null if it is substantially different in degree or connectivity.

## 8. Structural permutations

The conversation rejected weak sign-flip controls where structural permutations are required.

Use separate permutation families for:

- graph topology;
- arithmetic operator or prime-derived labels;
- initial state;
- structure-state alignment;
- forcing schedule if present.

## 9. Tripwires

Tripwires are deliberately invalid or corrupted inputs that must fail.

Examples:

- broken constraint Jacobian;
- permuted output labels;
- non-symmetric edge lengths in a symmetric model;
- invalid negative activation;
- incorrect projection sign;
- leaked target information;
- constant state where the metric should not change;
- relabeling that incorrectly changes observables.

A pipeline that passes the target experiment while failing tripwires is untrustworthy.

## 10. Independent parity

Implement critical formulas twice:

- vectorized and loop form;
- symbolic and numerical derivative;
- projection matrix and Lagrange-multiplier solve;
- shortest path using two independent libraries or one library plus brute force for tiny graphs.

Parity failures block interpretation.

## 11. Seeds and blinding

Use deterministic seeds, but do not let a public date or chosen result determine the seed.

Freeze:

- seeds;
- metrics;
- parameter ranges;
- exclusions;
- permutation counts;
- stopping rules.

Where practical, blind condition labels during analysis.

## 12. Permutation count

Use enough structural permutations to estimate the target tail probability.

For exploratory work, hundreds may be acceptable.

For stronger inference, use approximately $999$ or more when computationally feasible.

## 13. Multiple comparisons

Distinguish:

- one primary endpoint;
- prespecified secondary endpoints;
- exploratory diagnostics.

Do not select the most favorable metric after seeing results.

## 14. Robustness

Require:

- multiple graph sizes;
- multiple parameter regions;
- multiple initial-condition families;
- alternative solvers;
- alternative viability thresholds;
- out-of-sample confirmation.

## 15. Falsification conditions

### H1 fails if
alignment effects disappear under matched controls or reduce to simple graph/state statistics.

### H2 fails if
fixed-geometry models reproduce the effect after matching effective couplings.

### H3 fails if
the projection correction is zero, redundant, or empirically irrelevant.

### H4 fails if
global influence is not generally local-small/boundary-large, or the ratio is coordinate artifact.

### H5 fails if
prime-derived effects disappear under degree-, spectrum-, and arithmetic-matched controls.

## 16. Interpretation discipline

A positive simulation result establishes behavior of the model.

It does not establish:

- objective reality is pluralistic monism;
- the universe is a graph;
- primes underlie physics;
- the apeiron is mathematically discovered;
- global constraints explain quantum entanglement.

Those require separate evidence.

## 17. Reporting template

For each experiment record:

1. hypothesis;
2. mathematical model;
3. endpoint;
4. null;
5. tripwires;
6. permutation scheme;
7. seed;
8. environment;
9. result;
10. sensitivity;
11. failure modes;
12. claim status update.

## 18. Immediate first experiment

The first experiment should test H1 on the minimal three-node model and a small graph ensemble:

$$
\boxed{
\text{Does preserving structure–state alignment increase persistence
relative to matched destructive permutations?}
}
$$
