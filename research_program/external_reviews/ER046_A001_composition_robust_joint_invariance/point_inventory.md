# ER046 Point Inventory — Preliminary, Pending Full Composition-Audit Batch

## Strong points

1. Provides a stronger shared-budget counterexample than a merely identified shared scalar actuator.
2. Preserves the programme's desired robust quantifier order without allowing feedback to observe the disturbance.
3. Separates single-valued prescribed feedback from set-valued authorized controls and all realized selections.
4. Makes the true joint control set—not projected local sets—the feasibility object.
5. Handles all active constraints through tangent-cone exactness and an explicit constraint qualification.
6. States well-posedness and forward completeness rather than inferring them from compact inputs.
7. Gives coherent destruction/rescue examples and aligns rigorous theorem routing with Paper 2.

## Qualifications requiring final theorem care

1. The exact strong-invariance theorem must be cited and matched to the chosen contingent or Clarke tangent cone. The cone cannot be changed casually between R1 and R2.
2. For R2, Hausdorff-Lipschitz compact-convex regularity of the convexified velocity envelope is a substantive assumption; it does not follow from nonempty `Gamma`.
3. If convexification is used only as a proof envelope, the final text must distinguish safety of actual trajectories from physical implementability of relaxed velocities.
4. The statement `Gamma(x) subset S(x)` already gives robust tangency of every prescribed control; the separate robust-tangency clause is clarifying but logically redundant.
5. The independent-control corollary still needs proof that local selectors compose with the coupling maps at the required regularity.
6. Publication routing remains provisional until the composition batch and Paper 2 length decision close.

## Provisional disposition

Strongly retain. ER046 currently gives the most complete robust theorem architecture of the received responses and converges with the internal answer on Paper 2 routing. Do not implement before the remaining announced audits and exact theorem/citation verification.