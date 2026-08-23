# Corrected Restricted Composition Theorem

## Status

Controlling corrected theorem record superseding A001 Theorem 16.1. Jointly adjudicated from the internal answer and ER044–ER047. Immutable A001 remains the source of record and is not edited.

## 1. Failure of the submitted theorem

Separate nonempty local safe-control sets do not imply one jointly feasible control. For shared `u in [-1,1]`,

\[
\dot x_1=u-\tfrac12,\qquad \dot x_2=-u-\tfrac12,
\qquad Q_1=Q_2=[0,\infty),
\]

local safety requires respectively `u>=1/2` and `u<=-1/2`; their intersection is empty at the origin. Hence the source proof is invalid.

## 2. Abstract robust theorem via proximal normals

Let `Q_i subset R^{n_i}` be nonempty closed sets and `Q=product_i Q_i`. Consider

\[
\dot x=f(x,u,C(x),d),
\]

with true joint control set `U`, compact disturbance set `D`, and interface map `C`.

For each `x in Q`, define the robust joint regulation map

\[
R(x)=\left\{u\in U:
\langle\zeta_i,f_i(x,u,C(x),d)\rangle\le0
\quad
\forall i,\ \forall\zeta_i\in N^P_{Q_i}(x_i),\ \forall d\in D
\right\}.
\]

Assume:

1. `R(x)` is nonempty for every `x in Q`.
2. `R` has nonempty compact values and a measurable graph.
3. The convexified robust velocity envelope
   \[
   G(x)=\operatorname{clco}\{f(x,u,C(x),d):u\in R(x),\ d\in D\}
   \]
   is nonempty compact convex-valued and locally Hausdorff-Lipschitz on a neighborhood of `Q`.
4. `G` has linear growth on `Q`, or another hypothesis guarantees forward completeness. Bounded `Q` with a bounded neighborhood field is sufficient.
5. The solution concept is the absolutely continuous solution of `dot x in G(x)` and the standard proximal-normal strong-invariance lemma applies:
   \[
   \sup_{v\in G(x)}\langle\zeta,v\rangle\le0
   \quad\forall x\in Q,\ \forall\zeta\in N^P_Q(x)
   \Longrightarrow Q\text{ is strongly invariant.}
   \]

### Theorem

Under assumptions 1–5, `Q` is strongly invariant for `dot x in G(x)`. Consequently, for every measurable selector `kappa(x) in R(x)`, every measurable unobserved disturbance `d(t) in D`, and every forward-complete Carathéodory trajectory satisfying

\[
\dot x(t)=f(x(t),\kappa(x(t)),C(x(t)),d(t)),
\]

the implication

\[
x(0)\in Q\Longrightarrow x(t)\in Q\quad\forall t\ge0
\]

holds.

### Proof

For finite products,

\[
N^P_Q(x)=\prod_iN^P_{Q_i}(x_i).
\]

Take `zeta=(zeta_1,...,zeta_n) in N^P_Q(x)`. Every raw velocity used to construct `G(x)` satisfies

\[
\langle\zeta,f(x,u,C(x),d)\rangle
=\sum_i\langle\zeta_i,f_i(x,u,C(x),d)\rangle\le0
\]

by the definition of `R(x)`. The inequality is preserved by closure and convexification, so it holds for every `v in G(x)`. The proximal-normal strong-invariance lemma yields strong invariance of `Q`. Every realized closed-loop velocity belongs to `G(x)` almost everywhere, so every such trajectory is a solution of the invariant inclusion. The growth/completeness assumption extends the conclusion for all forward time. ∎

## 3. Smooth single-valued corollary

If each `Q_i` is convex or finitely represented by `C1` inequalities satisfying a constraint qualification, all active gradient inequalities give the appropriate regular tangent/normal condition. If a locally Lipschitz selector `kappa:Q->U` exists, `f` is jointly locally Lipschitz in `(x,u,z)` uniformly in `d`, `C` is locally Lipschitz, and the closed loop is forward complete, then one obtains the same robust conclusion for the Carathéodory system with one state-feedback policy independent of unmeasured disturbance.

A measured-disturbance feedback `kappa(x,d)` is a separate, weaker-information corollary and is not the main robust theorem.

## 4. Independent-control corollary

If `U=product_i U_i`, disturbances factor, and there are no shared actuators, budgets, allocations, algebraic constraints, or implementation branches, define each local robust regulation map uniformly over the interface tolerance ball. If every local map is nonempty and the resulting selectors/envelope satisfy the preceding regularity assumptions, the joint map factors and the product set is robustly invariant.

The word “independent” includes implementation feasibility, not merely a rectangular symbol in the equations.

## 5. Shared-control rule

For shared resources, the theorem requires direct nonemptiness of `R(x)` in the true joint control set. Nonempty projections or local factors are neither necessary nor sufficient.

## 6. Coupling destruction and rescue

For `dot x_1=u_1-x_2`, `Q_1=[0,infinity)`, and `u_1 in [-1,1]`, the state `(0,2)` cannot be protected: coupling exceeds control authority. Replacing `x_2` by a bounded interface `tanh(x_2)` permits the boundary feedback `u_1=1`; with the analogous second subsystem and valid regularity, the product orthant is rescued.

## 7. Limitations

This theorem does not establish:

- selector/envelope regularity for a particular model;
- physical implementability of convexified velocities;
- partial-observation safety;
- hybrid reset preservation or non-Zeno continuation;
- stochastic viability;
- nonconvex relaxation exactness;
- nonlinear small-gain composition.

Each application must verify interface bounds, graph measurability, joint feasibility, selector or envelope regularity, solution existence, and forward completeness.

## 8. Publication routing

- Paper 2: abstract theorem, smooth corollary, counterexample, and exact limitations.
- Paper 1: architecture-level independent-control lesson only, with citation closure.
- Monograph/conditional docket: hybrid, stochastic, partial-observation, and nonlinear small-gain extensions.