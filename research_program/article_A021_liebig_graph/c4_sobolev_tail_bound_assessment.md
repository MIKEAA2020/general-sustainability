# C4 Sobolev/Pointwise Tail Bound Assessment

## Objective

Avoid the dependency and analytic-tail difficulties of the weighted Fourier `l1` route by bounding the periodic linearized multiplication/delay operator directly in a pointwise matrix norm on a tight orbit box. In periodic `L2`/Sobolev norms, delay shift is an isometry, so the high-mode derivative diagonal can dominate this pointwise operator bound.

## Tight validated box

A subdivided outward interval computation was performed on

\[
N\in[45.5,95.1],
\quad
A\in[834,944],
\quad
E\in[0.34,20.1],
\quad
Z_{\rm del}\in[0.001,0.68].
\]

This box contains the numerical orbit with visible margin.

The row-sum bounds for the current-plus-delayed linearization are:

\[
(0.13352,\ 0.05384,\ 0.22671,\ 7.60895).
\]

Hence

\[
\|L(t)\|_{\infty}\le7.60895
\]

uniformly on the entire box. The softplus derivative was bounded structurally by `0<=sp'<=1`, avoiding interval dependency inflation.

## High-mode diagonal dominance

For the normalized periodic equation, the high Fourier derivative diagonal is `2 pi i k`. In a periodic L2/Sobolev setting, multiplication by the linearized coefficient and the delay phase shift have operator norm bounded by the pointwise matrix bound. Therefore the high-mode tail factor satisfies

\[
\eta_K
\le
\frac{P\,7.60895}{2\pi(K+1)}.
\]

With

\[
P=370.9311778394~\mathrm{yr},
\]

one obtains:

| K | tail factor bound |
|---:|---:|
| 240 | 1.864 |
| 400 | 1.120 |
| 540 | 0.830 |
| 600 | 0.747 |

The analytic threshold is

\[
K\ge449.
\]

Thus the structured K600 block has a rigorous pointwise-interval high-mode contraction margin of approximately

\[
1-\eta_{600}\ge0.2526.
\]

## Significance

This is stronger than the numerical Fourier-coefficient convolution estimate:

- it uses outward interval state-box derivatives;
- it does not assume an analytic coefficient tail;
- it naturally supports a Sobolev/collocation validation;
- it proves that modes above K600 are contractive for the periodic linearization, provided the validated orbit remains in the stated box.

## Remaining block coupling

The full inverse proof must combine:

1. finite/structured K240-to-K600 preconditioned defect `1.595e-6`;
2. high-mode tail factor at most `0.7475`;
3. finite inverse and interval residual bounds;
4. the norm conversion between the finite collocation block and the Sobolev tail.

A block-Neumann/Schur-complement argument is still required. The large tail margin and tiny structured defect make that closure plausible.

## Status

`OUTWARD_INTERVAL_POINTWISE_LINEARIZATION_BOUND_7P609`

`SOBOLEV_HIGH_MODE_TAIL_CONTRACTION_VERIFIED_ABOVE_K600`

`BLOCK_NORM_COUPLING_PROOF_PENDING`