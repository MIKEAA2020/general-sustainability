# C4 K=80 Newton–Kantorovich Precursor

## Objective

Estimate the finite-dimensional Newton–Kantorovich margin before replacing every quantity by outward-rounded interval bounds. This is a diagnostic for feasibility, not a validated radii-polynomial proof.

## Finite system

- dimension: `645` unknowns;
- four states at `161` periodic Fourier-collocation phases plus period;
- phase-fixed K=80 solution;
- induced infinity norm.

## Numerical bounds

Approximate inverse norm:

\[
B=\|J^{-1}\|_\infty
\approx1847.8638.
\]

Newton-preconditioned residual:

\[
Y_{\rm num}=\|J^{-1}F(\bar u)\|_\infty
\approx1.2941\times10^{-11}.
\]

Approximate inverse defect:

\[
Z_{0,\rm num}
=\|I-J^{-1}J\|_\infty
\approx2.8330\times10^{-9}.
\]

Directional finite-difference sampling of the Jacobian derivative (80 random infinity-normalized directions, 32 representative state coordinates, and the period direction) gives

\[
L_{\rm dir,max}\approx852.51,
\]

with median approximately `741.48`.

The numerical Kantorovich precursor is

\[
h_{\rm num}=B L_{\rm dir,max}Y_{\rm num}
\approx2.04\times10^{-5}\ll\frac12.
\]

Thus the finite collocation root has a very large numerical Newton–Kantorovich margin despite the ill-conditioned phase-fixed Jacobian.

## Interpretation

This result strongly suggests that an outward-rounded finite-dimensional interval Newton step should succeed. It does **not** bound:

- unsampled Hessian directions;
- rounding error;
- Fourier convolution tails;
- the infinite-dimensional periodic-orbit operator;
- true-orbit floor clearance.

The rigorous interval implementation must replace `L_dir,max` by an analytic or interval Hessian bound and include the coefficient tail.

## Next interval target

A conservative finite-dimensional interval attempt can tolerate an interval Hessian bound as large as roughly

\[
L_{\max}<\frac{1}{2BY_{\rm num}}
\approx2.09\times10^7
\]

before the elementary Kantorovich half-condition fails. This wide budget indicates that interval overestimation in the finite block is unlikely to be the primary obstacle; the analytic tail and nonlinear convolution bounds are more likely to control success.

## Status

`FINITE_K80_KANTOROVICH_MARGIN_STRONGLY_POSITIVE_NUMERICALLY`

Outward-rounded finite block and infinite tail remain pending.