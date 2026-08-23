# Final Joint Audit — A001 Composition Theorem

## Inputs

- internal provisional composition answer;
- ER044 strong-invariance repair;
- ER045 smooth Carathéodory/Nagumo repair;
- ER046 robust single/set-valued repair;
- ER047 product-cone, selector, growth, and proximal-normal correction.

## Final verdict

The submitted A001 Theorem 16.1 is **false/invalid as proved** and is superseded. All inputs converge on the shared-control counterexample and the need for a single jointly feasible causal control policy. ER047 closes the most important remaining technical gaps.

## Joint corrections to weaker suggestions

1. **Product geometry:** do not use `T_Q=product T_Qi` for arbitrary Bouligand/contingent cones. Use proximal-normal inequalities for the abstract theorem. A smooth/convex tangentially regular corollary may use Clarke/product tangent geometry.
2. **Robust quantifiers:** the main policy is independent of unmeasured disturbance: `exists policy, forall disturbances, forall admitted solutions`. ER045's `kappa(x,d)` is retained only as a measured-disturbance corollary.
3. **Selector regularity:** nonempty pointwise controls and measurable selection do not imply Lipschitz closed-loop dynamics. The abstract theorem assumes a regular convexified velocity envelope; a single-valued corollary separately assumes a locally Lipschitz selector.
4. **Filippov caution:** convexifying neighboring tangent velocities can exit a nonconvex contingent cone. The final abstract theorem uses proximal-normal strong invariance of a Lipschitz compact-convex envelope instead.
5. **Growth:** compact `U,D` do not imply linear growth in `x`. Forward completeness is guaranteed only by bounded `Q`, an explicit growth bound, or another continuation/Lyapunov hypothesis.
6. **Multiple constraints:** all active constraints are simultaneous. A scalar barrier is allowed only when exactness is proved.
7. **Interface scope:** local feasibility must hold uniformly over the declared interface tolerance set; actual interface bounds must hold over the proposed joint set.
8. **Convexification:** the convex hull is a proof envelope. It does not prove relaxed controls are physically implementable.
9. **Publication:** the rigorous joint theorem and counterexample belong in Paper 2. Paper 1 may state the independent-control architecture lesson, subject to citation closure. Hybrid, stochastic, partial-observation, and nonlinear small-gain results remain open.

## Adopted theorem architecture

1. Abstract proximal-normal robust strong-invariance theorem for a regular convexified velocity envelope.
2. Locally Lipschitz single-valued feedback corollary for smooth/regular constraints.
3. Cartesian independent-control corollary.
4. Shared-budget counterexample.
5. Bounded-interface destruction/rescue example.
6. Explicit limitations and application obligations.

## Rejected claims

- local nonemptiness automatically yields joint feasibility;
- arbitrary contingent cones factor over products;
- measurable selection automatically yields a Lipschitz or Filippov-safe closed loop;
- compact inputs imply forward completeness;
- the continuous theorem automatically extends to hybrid, stochastic, or partial-observation systems;
- the bare product argument is a novel general composition theorem.

## Implementation decision

Authorize conservative implementation in a separate corrected theorem record and the canonical schema. Do not rewrite immutable A001. Do not promote broader composition or small-gain claims.