# C4 Sixth-Derivative Coefficient Assessment

## Objective

Replace point-sampled sixth-derivative maxima by a Fourier coefficient-sum bound, which is the natural quantity for a rigorous periodic derivative estimate.

## Coefficient bound

For the periodic linearization coefficient matrices `A(t),D(t)`, the trigonometric inequality gives

\[
\|L^{(6)}\|_\infty
\le
\sum_{k\in\mathbb Z}
\left(\frac{2\pi|k|}{P}\right)^6
\left(\|A_k\|_\infty+\|D_k\|_\infty\right).
\]

Evaluating the coefficient sum from the K=120 corrected orbit gives convergence:

| coefficient cutoff | sixth-derivative coefficient sum |
|---:|---:|
| 40 | `8.0725e-5` |
| 60 | `9.0925e-5` |
| 80 | `9.2031e-5` |
| 100 | `9.2125e-5` |
| 120 | `9.21323e-5` |
| 160 | `9.21328e-5` |
| 240 | `9.21328e-5` |
| 500 | `9.21335e-5` |

The signal-dominated coefficient sum stabilizes near

\[
9.214\times10^{-5}.
\]

This is below the earlier pointwise spectral-differentiation estimate `1.50e-4`; the latter includes amplified numerical high-frequency noise.

## Validation budget

A factor-two outward allowance gives the target

\[
\|L^{(6)}\|_\infty
<1.843\times10^{-4},
\]

still below the sufficient block-Neumann target

\[
2.0\times10^{-4}.
\]

Thus the sixth-derivative validation has a numerical margin of roughly eight percent even under a twofold coefficient allowance.

## What remains rigorous

The coefficient sum is computed from the approximate orbit. A proof must include:

1. outward interval enclosures of the retained `A_k,D_k` coefficients;
2. a tail bound beyond the retained coefficient cutoff;
3. sensitivity of `L^(6)` over the validated periodic-orbit ball.

Independent node intervals would destroy Fourier correlation and overestimate the sixth derivative. The correct approach is coefficient-space interval arithmetic or a radii-ball Lipschitz estimate in a sufficiently strong Sobolev norm.

## Consequence

The block-Neumann precursor remains viable:

- required sixth-derivative bound: `<2.0e-4`;
- approximate coefficient bound: `9.214e-5`;
- factor-two validation target: `1.843e-4`.

## Status

`SIXTH_DERIVATIVE_COEFFICIENT_BOUND_NUMERICALLY_BELOW_HALF_TARGET`

`INTERVAL_COEFFICIENT_AND_ORBIT_BALL_SENSITIVITY_PENDING`