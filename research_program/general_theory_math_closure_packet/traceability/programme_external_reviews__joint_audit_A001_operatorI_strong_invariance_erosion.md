# Joint Audit — A001 Operator I Strong Invariance and Erosion

## Inputs

Internal Operator I audit; filtered surviving Part B audit from both GLM raw-reasoning files; directly supplied Part A; and all five direct external responses supplied in the conversation. Raw GLM reasoning is not independent evidence.

## Final decisions

### Part A

The A001 proof is invalid: weak viability gives one viable inclusion trajectory, not one feedback safe for every disturbance and every admitted solution. Replace it with the locally Hausdorff-Lipschitz strong-invariance theorem in `A001_operatorI_strong_invariance_erosion_corrected.md`.

Required structure: one disturbance-independent feedback; compact-convex closed-loop envelope; proximal-normal Hamiltonian inequality; explicit solution concept; and linear growth or another completeness argument. Measurable selection alone is insufficient.

### Part B

Remove the arbitrary-closed-set erosion proposition. Retain only a conditional metric-erosion lemma on a two-sided tubular neighborhood with explicit geometry, field sensitivity, error envelope, nonemptiness, strong-invariance regularity, and completeness.

The controlling condition is

\[
L_G r+\Delta_\varepsilon\le\alpha,
\qquad 0<r<\rho,
\qquad K_{-r}\ne\varnothing.
\]

For `Delta_epsilon=C epsilon` and `r=c epsilon`,

\[
(L_Gc+C)\varepsilon\le\alpha.
\]

Metric erosion and arbitrary barrier superlevels remain distinct.

## Corrections to weaker responses

- Reject Marchaud-only claims unless an exact separate Clarke-cone all-solutions theorem is verified.
- Use proximal normals for the adopted CLSW route.
- Correct the Filippov counterexample by putting the switching surface on `x_1=x_2`.
- Do not claim equality between fixed-disturbance Filippov regularization and convexification across all disturbances.
- Do not infer Lipschitz dynamics from measurable selection.
- Do not claim a universal switching-rate error.
- Reject incomplete cusp/dumbbell/sign-error counterexamples.
- Retain the disjoint-interval erosion counterexample, which proves the need for a uniform tubular field-sensitivity bound.

## Publication

- Paper 2 main foundations: corrected Part A theorem.
- Paper 2 appendix: Part B only after `alpha,L_G,C,rho`, nonemptiness, regularity, and completeness are verified.
- Paper 1: architecture-level quantifier and implementation consequence only.
- Hybrid, stochastic, delayed, discontinuous-feedback, and arbitrary-closed-set extensions remain open.

## Implementation

Authorized in the corrected controlling record and canonical schema. Immutable A001 remains unchanged.
