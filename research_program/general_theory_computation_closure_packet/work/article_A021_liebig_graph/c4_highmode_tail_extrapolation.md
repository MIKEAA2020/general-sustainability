# C4 High-Mode Tail-Transfer Extrapolation

## Extended truncations

The phase-fixed Fourier system was extended without forming the fine inverse to:

- K=200 (1605 unknowns);
- K=240 (1925 unknowns).

The period and off-grid residual remain stable:

| K | period | off-grid residual |
|---:|---:|---:|
| 160 | 370.9311778394262 | `2.35e-12` |
| 200 | 370.9311778394397 | `2.81e-12` |
| 240 | 370.9311778394484 | `3.07e-12` |

The small increase at the finest levels is consistent with floating-point resolution, not loss of spectral convergence.

## Preconditioned transfer sequence

| transfer | preconditioned defect |
|---|---:|
| 100→120 | `5.936e-3` |
| 120→160 | `4.577e-5` |
| 160→200 | `3.118e-5` |
| 200→240 | `2.182e-5` |

The final two ratios are approximately `0.68` and `0.70`. If that geometric behavior continues, the sum of unresolved finite increments beyond K=240 is approximately bounded numerically by

\[
\frac{2.182\times10^{-5}\times0.70}{1-0.70}
\approx5.1\times10^{-5}.
\]

A conservative empirical high-mode transfer allowance is therefore

\[
\delta_{240,\infty}^{\rm emp}=10^{-4}.
\]

Combined with the stable inverse norm near 1848, this would imply an empirical continuum inverse target

\[
\|L^{-1}\|
\lesssim
\frac{1848}{1-10^{-4}}
<1848.2.
\]

## Status and limitation

This is strong truncation-convergence evidence, not a proof of geometric decay for all higher modes. A rigorous tail requires an analytic recurrence, complex-strip bound, Sobolev interpolation theorem, or validated collocation consistency estimate.

The extended computations show that a target continuum preconditioned tail defect below `10^-3` is extremely conservative relative to the observed sequence.

## Status

`EMPIRICAL_HIGH_MODE_TRANSFER_TAIL_BELOW_1E_MINUS_4`

`RIGOROUS_CONTINUUM_TAIL_BOUND_PENDING`