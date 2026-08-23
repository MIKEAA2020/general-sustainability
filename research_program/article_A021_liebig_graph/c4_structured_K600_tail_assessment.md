# C4 Structured K600 and Diagonal-Tail Assessment

## Objective

Implement the hybrid architecture selected by the tail-feasibility study:

1. retain the converged K=240 phase-fixed inverse;
2. apply the K=600 structured Jacobian to prolonged K=240 modes without forming/inverting the full K=600 matrix;
3. restrict back to K=240 and measure the preconditioned consistency defect;
4. use diagonal dominance only above K=600.

## Structured K240 to K600 transfer

The fine structured state dimension is `4804`; the coarse phase-fixed dimension is `1925`. Batched FFT interpolation and exact local Jacobian application give

\[
\left\|
J_{240}^{-1}
\left(J_{240}-R_{600\to240}J_{600}E_{240\to600}\right)
\right\|_\infty
=1.5950\times10^{-6}.
\]

The raw restricted Jacobian difference is only

\[
2.3859\times10^{-4}.
\]

Despite interpolation/restriction infinity norms near `4.89` and `5.48`, the preconditioned low-mode defect is negligible.

## Diagonal tail above K600

For weight `nu=1.01`, the numerical periodic-linearization convolution norm is

\[
L_\nu\approx9.15522.
\]

The diagonal-tail factor beyond K=600 is

\[
\eta_{\rm tail}
=
\frac{P L_\nu}{2\pi(601)}
\approx0.899<1.
\]

Thus K=600 is beyond the numerically identified diagonal-tail threshold. A padded interval coefficient target such as

\[
L_\nu^{\rm int}<9.2
\]

would retain a tail factor below approximately `0.904`, leaving a positive Neumann margin.

## Combined architecture

The numerical structured defect and diagonal tail have very different roles:

- structured low/medium-mode defect: `1.6e-6`;
- diagonal infinite-tail contraction: about `0.899`.

The infinite tail is therefore the limiting validation factor, but it is finally below one at a computationally feasible cutoff.

## What would complete the inverse proof

1. outward interval enclosure of `L_nu` below the permitted threshold;
2. rigorous weighted convolution-tail bound for the periodic coefficients;
3. interval verification of the finite K240 inverse/residual;
4. block-Neumann estimate combining finite, coupling, and tail blocks.

The observed structured transfer is already far below any plausible interval budget. The proof now hinges on certifying the diagonal tail factor rather than extending finite truncations further.

## Status

`STRUCTURED_K240_TO_K600_DEFECT_1P6E_MINUS_6`

`DIAGONAL_TAIL_FACTOR_ABOVE_K600_APPROX_0P899`

`OUTWARD_INTERVAL_LINEARIZATION_NORM_PENDING`