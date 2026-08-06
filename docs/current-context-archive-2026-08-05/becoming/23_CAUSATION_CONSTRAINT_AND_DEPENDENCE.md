# Causation, Constraint, and Dependence

## 1. Starting framework

Suppose a condition persists as changing structure and state:

$$
Q_t=(B_t,x_t).
$$

Its next condition is produced by:

$$
(B_t,x_t,\Delta_t,C_t,E_t,M_t)
\longrightarrow
(B_{t+1},x_{t+1}).
$$

The question is what “cause” means in such a framework.

## 2. Candidate definition

$$
\boxed{
\text{Causation is lawful dependence of one relational condition
on another under specified constraints.}
}
$$

A cause need not be a separate object that pushes an effect. It can be a variable, relation, intervention, boundary condition, or state component whose alteration changes the subsequent trajectory.

## 3. Dynamical form

Let:

$$
\dot Q=F(Q,U,C),
$$

where $U$ is an input or candidate cause.

$U$ has causal relevance when changing $U$, while controlling the relevant conditions, changes the trajectory:

$$
F(Q,U,C)
\neq
F(Q,U',C).
$$

A stronger intervention form is:

$$
\operatorname{do}(U=u)
$$

leading to a different distribution or trajectory than:

$$
\operatorname{do}(U=u').
$$

The conversation did not develop a full intervention calculus, so this remains a conceptual criterion.

## 4. Correlation

Correlation means variables vary together.

It does not establish:

- direction;
- mechanism;
- intervention response;
- exclusion of common causes;
- lawful dependence.

Thus:

$$
\text{correlation}
\not\Rightarrow
\text{causation}.
$$

## 5. Temporal sequence

A precedes B does not imply A causes B.

Temporal priority may be required in some causal models, but sequence alone is insufficient.

## 6. Constraint

A constraint removes possibilities:

$$
\Gamma(Q)=0.
$$

It may shape all trajectories without selecting one unique next state.

Therefore a constraint is not automatically a cause. It becomes causally relevant when modifying or removing the constraint changes actual or counterfactual evolution.

## 7. Description of change

An equation can describe a trajectory without explaining which dependency is causal.

For example:

$$
Q_{t+1}=\mathcal T(Q_t)
$$

may reproduce observed change but not identify interventions, mechanism, or explanatory decomposition.

## 8. Local and global causes

Local causes can enter direct update terms:

$$
\dot x_i
=
f_i(x_i,x_{\mathcal N_i},c).
$$

Global constraints can alter admissible motion:

$$
\dot Z
=
\Pi_{T_Z\mathcal M}F(Z).
$$

The global term may be interpreted as a distributed causal condition if changing $\mathcal M$ changes the trajectory. It should not be anthropomorphized as a separate agent.

## 9. Noncausal reality

A reality without separate objects acting on effects is not necessarily noncausal.

Lawful relational dependence can support causation even when:

- relata are mutually dependent;
- causes are distributed;
- constraints are global;
- no external controller exists.

A truly noncausal model would lack stable dependence or intervention-sensitive regularity.

## 10. Strongest weakness

The framework risks defining causation too broadly. If every dependency or constraint counts as causal, the concept loses discrimination.

A valid causal account must specify:

- variables;
- intervention class;
- temporal or structural ordering;
- controlled conditions;
- competing explanations;
- mechanism or invariant dependence.

## 11. Plain-English definition

> A cause is something whose change makes a lawful difference to what happens next, given the relevant conditions.
