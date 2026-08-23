# Internal Provisional Answer — A001 Restricted Composition Theorem

## Status

Internal answer for later joint adjudication with external audits. **No manuscript implementation is authorized.**

## 1. Verdict

The submitted A001 Theorem 16.1 is **repairable but invalid as proved**. Its interface-bound premise is useful, but “each local safe-control set is nonempty” does not imply that local controls can be selected jointly, implemented causally, or used in a well-posed closed loop. The proof also omits the hypotheses needed by a strong-invariance theorem.

The narrow repaired result below is sufficient for the first programme composition theorem.

## 2. Minimal shared-control counterexample

Let two scalar subsystems share one control `u∈[-1,1]` and have safe sets `Q_1=Q_2=[0,∞)`. At the joint boundary `(x_1,x_2)=(0,0)`, let

\[
\dot x_1=u-\tfrac12,
\qquad
\dot x_2=-u-\tfrac12.
\]

Subsystem 1 is locally viable by choosing `u≥1/2`; subsystem 2 is locally viable by choosing `u≤-1/2`. Each local safe-control set is nonempty, but their intersection is empty. No shared control prevents immediate exit from the product set. Therefore separate local feasibility does not imply product viability.

## 3. Repaired continuous-time theorem

### Data

For `i=1,…,n`, let `X_i=R^{m_i}` and let `Q_i⊂X_i` be closed. Put

\[
X=\prod_iX_i,
\qquad Q=\prod_iQ_i.
\]

Consider

\[
\dot x_i=f_i(x_i,u_i,C_i(x_{-i}),d_i),
\]

or the joint field `dot x=f(x,u,d)`. Assume:

1. `Q` is locally prox-regular, or belongs to another class for which the selected strong-invariance theorem applies.
2. The joint action correspondence `U(x)` and disturbance correspondence `D(x)` are nonempty compact-valued with the regularity required below.
3. `f` is continuous in `(x,u,d)` and locally Lipschitz in `x` uniformly on compact `(u,d)` sets.
4. Every declared interface is bounded on `Q`:
   \[
   C_i(x_{-i})\in Z_i^{safe}\quad\forall x\in Q.
   \]
5. Define the joint robust safe-control correspondence
   \[
   R_Q(x)=\{u\in U(x):f(x,u,d)\in T_Q(x)\ \forall d\in D(x)\}.
   \]
   It is nonempty for every `x∈Q`.
6. `R_Q` admits a continuous selector `k:Q→U`, or another selector for which the closed-loop solution concept and strong-invariance theorem are explicitly valid.
7. For every measurable disturbance `d(t)∈D(x(t))`, the closed loop
   \[
   \dot x=f(x,k(x),d)
   \]
   has complete forward solutions from `Q` and every such solution is covered by the selected invariance theorem.

### Theorem

Under assumptions 1–7, `Q` is robustly controlled invariant under `k`: every declared closed-loop solution beginning in `Q` remains in `Q` for all forward time.

### Proof

For every `x∈Q`, selector membership gives

\[
f(x,k(x),d)\in T_Q(x)
\qquad\forall d\in D(x).
\]

The regularity, solution, and completeness assumptions match the selected robust strong-invariance theorem. Applying that theorem to the closed-loop disturbance inclusion gives forward invariance of `Q` for every declared disturbance and every admitted solution. ∎

This proof is intentionally short because the substantive content is in the joint feasibility and theorem-matching hypotheses. Pointwise nonemptiness alone is not enough.

## 4. Smooth barrier version

Suppose each

\[
Q_i=\{x_i:b_{i\ell}(x_i)\ge0,\ \ell=1,\dots,r_i\}
\]

has `C1` constraints satisfying a constraint qualification that makes the tangent cone equal to the simultaneous active-gradient halfspaces. Then joint feasibility is

\[
R_Q(x)=\left\{u\in U(x):
\nabla b_{i\ell}(x_i)^Tf_i(x_i,u_i,C_i(x_{-i}),d_i)\ge0
\right.
\]

\[
\left.
\forall d\in D(x),\ \forall(i,\ell)\text{ active at }x
\right\}\ne\varnothing.
\]

With a valid selector and closed-loop theorem, the preceding result applies. Every active constraint is checked simultaneously.

## 5. Independent-control corollary

If

\[
U(x)=\prod_iU_i(x_i)
\]

and controls, budgets, algebraic constraints, and implementation branches are genuinely independent, define

\[
R_i(x)=\{u_i\in U_i(x_i):
 f_i(x_i,u_i,C_i(x_{-i}),d_i)\in T_{Q_i}(x_i)
 \ \forall d_i\in D_i(x)\}.
\]

If every `R_i(x)` is nonempty and the product correspondence admits a selector with the required regularity, then

\[
R_Q(x)=\prod_iR_i(x)
e\varnothing
\]

because `T_Q(x)=product_i T_{Q_i}(x_i)` for the declared product geometry. The repaired theorem yields robust product invariance.

The Cartesian conclusion is unavailable if any actuator, budget, allocation constraint, information channel, or implementation branch is shared.

## 6. Shared-control version

Let one joint control `v∈V(x)` induce local actions `u_i=H_i(x,v)`. Define

\[
R_i^{shared}(x)=\{v∈V(x):
 f_i(x_i,H_i(x,v),C_i(x_{-i}),d_i)∈T_{Q_i}(x_i)
 \ \forall d_i\}.
\]

The necessary composition premise is

\[
\bigcap_iR_i^{shared}(x)\ne\varnothing
\qquad\forall x∈Q,
\]

plus selector and well-posedness hypotheses. Separate nonemptiness of the factors is insufficient, as the counterexample shows.

## 7. Coupling destruction and rescue

Let `Q_i=[0,M]`, `u_i∈[0,U]`, and

\[
\dot x_i=-a x_i+u_i-cx_j,
\qquad i\ne j.
\]

At the lower face `x_i=0`, safety requires `u_i≥cx_j`; the worst interface is `cx_j≤cM`. If `U<cM`, the point `(0,M)` has no safe `u_1`, so coupling destroys product invariance.

If `U≥cM`, controls are independent, and upper-face feasibility is also imposed—for example `U≤aM`, making `dot x_i≤0` at `x_i=M`—then each boundary admits a safe local action and the product safe-control correspondence is nonempty. Under a regular selector, bounded coupling is rescued and `Q` is invariant.

This example shows that the interface bound is a quantitative feasibility condition, not decorative terminology.

## 8. Hybrid extension

Do not include a hybrid corollary without separately requiring:

- flow tangency in each mode;
- reset images contained in the destination safe set;
- joint control feasibility at flow and jump decisions;
- event nonblocking;
- a declared treatment of Zeno solutions;
- a hybrid strong-invariance theorem matched clause by clause.

## 9. Limitations

The repaired theorem does not by itself cover:

- partial observation or information-state policies;
- discontinuous feedback without a solution convention;
- nonconvex relaxation gaps;
- strategic equilibrium controls;
- stochastic chance constraints;
- variable-event RFDE systems;
- general nonlinear small-gain composition.

## 10. Publication disposition

- The submitted theorem must not be published as currently proved.
- The repaired joint-feasibility theorem is suitable for **Paper 2** as the first restricted composition theorem.
- Paper 1 may state the architectural lesson and cite the proved theorem only after stable publication/preprint closure; it should not claim this theorem as its own independent result.
- The counterexample and bounded-coupling rescue example should accompany the theorem.
- A nonlinear cyclic small-gain extension remains a later theorem, not a requirement for the first paper.

## 11. Remaining obligations

1. Choose and cite the exact robust strong-invariance theorem.
2. Decide between continuous-selector assumptions and a differential-inclusion/feedback solution concept.
3. State the joint action/implementation correspondence used by each application.
4. Verify global interface bounds on the proposed `Q`.
5. Add a separate hybrid theorem only if reset/non-Zeno hypotheses are proved.