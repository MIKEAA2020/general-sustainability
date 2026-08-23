# Filtered Internal Audit — Surviving Part B Erosion Results

## Status

This record extracts only conclusions that survived mathematical checking from the raw GLM reasoning files. The raw reasoning is not an external review and is not independent evidence. Failed, incomplete, or self-retracted counterexamples are excluded.

## Surviving conclusions

### 1. The original claim is unacceptable

The statement

> full-state invariance plus strict boundary margin and error `epsilon` implies invariance of `K^{-c epsilon}` for some unspecified `c>0`

is not a quantitative theorem. It omits the geometry of inner parallel sets, field/error sensitivity, nonemptiness, solution regularity, and completeness.

### 2. Metric erosion and barrier-superlevel restriction are different

Metric erosion is

\[
K_{-r}=\{x\in K:\operatorname{dist}(x,K^c)\ge r\}.
\]

A barrier restriction is `\{h\ge eta\}` for a chosen defining function. They coincide only for signed distance; otherwise explicit two-sided comparison constants are required. Invariance of one does not automatically prove invariance of the other.

### 3. A viable metric theorem needs tubular geometry

A clean sufficient class is a closed domain with a two-sided tubular radius `rho>0`, so that signed distance is `C^{1,1}` in `|s_K|<rho`, nearest boundary projection is unique, and normals of `K_{-r}` correspond to normals of `K` for `0<r<rho`.

Ordinary closedness alone is insufficient for this normal-transfer argument. The theorem should state the tubular property directly rather than use ambiguous shorthand about reach.

### 4. Quantitative normal-margin transfer

Let the nominal compact-convex envelope `G` be locally Hausdorff-Lipschitz in the inner tube with constant `L_G`. Suppose on the original boundary

\[
\sup_{v\in G(p)}\langle n(p),v\rangle\le-\alpha<0.
\]

Let the implemented envelope satisfy

\[
\widetilde G_\epsilon(x)\subseteq G(x)+\Delta_\epsilon B.
\]

At `x\in\partial K_{-r}` with corresponding boundary point `p` and common outward normal,

\[
\sup_{w\in\widetilde G_\epsilon(x)}\langle n,w\rangle
\le-\alpha+L_G r+\Delta_\epsilon.
\]

Hence the sufficient condition is

\[
\boxed{L_G r+\Delta_\epsilon\le\alpha},
\qquad 0<r<\rho,
\qquad K_{-r}\ne\varnothing.
\]

Under a matched strong-invariance theorem and forward completeness, `K_{-r}` is strongly invariant.

### 5. Observer/implementation error must be converted to velocity error

If

\[
|\hat x-x|\le a_o\epsilon,
\qquad
|u_{impl}-k(\hat x)|\le a_u\epsilon,
\]

`k` is Lipschitz with constant `L_k`, and the plant is Lipschitz in control with constant `L_u`, then one admissible bound is

\[
\Delta_\epsilon=C\epsilon,
\qquad
C=L_u(L_k a_o+a_u),
\]

plus any separately bounded plant or disturbance-model error. Errors with different physical units must not be added before conversion through their sensitivity constants.

### 6. Explicit proportional erosion condition

For `r=c\epsilon`, the condition is

\[
(L_Gc+C)\epsilon\le\alpha,
\qquad
c\epsilon<\rho,
\qquad
K_{-c\epsilon}\ne\varnothing.
\]

If erosion must also guarantee actual-state safety from an estimated state, require `c\ge a_o`. Therefore a feasible `c` must satisfy

\[
a_o\le c\le\frac{\alpha/\epsilon-C}{L_G}
\]

when `L_G>0`. This interval may be empty. No universal unspecified `c` is justified.

### 7. Completeness and solution concepts remain binding

The nominal and implemented envelopes must satisfy the regularity required by the selected strong-invariance theorem, and global-time conclusions need linear growth, bounded invariant state, or another continuation argument. Hybrid resets, delays, stochastic noise, and discontinuous feedback require separate theorems.

## Excluded material

The following raw-reasoning content is not retained:

- tentative cusp, dumbbell, L-shape, and neck counterexamples that were incomplete, sign-inconsistent, or later self-retracted;
- claims that positive reach automatically gives a smooth one-dimensional normal ray at corners;
- unsupported switching-rate error estimates;
- any assertion based solely on internal exploratory calculations.

## Provisional publication disposition

- Remove the arbitrary-closed-set erosion proposition.
- Retain the tubular metric theorem only as a conditional technical lemma until `alpha`, `L_G`, `C`, `rho`, nonemptiness, and completeness are verified in an application.
- Keep barrier-superlevel and metric-erosion statements separately typed.