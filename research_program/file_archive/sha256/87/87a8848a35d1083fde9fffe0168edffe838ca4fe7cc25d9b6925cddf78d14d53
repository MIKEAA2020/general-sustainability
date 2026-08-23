# C4 Block-Neumann Precursor from Sixth-Derivative Tail

## Objective

Estimate the low-to-tail and tail-to-low coupling needed to combine:

- K240 finite inverse;
- structured K240-to-K600 transfer;
- diagonal tail above K600.

## Fourier tail by integration by parts

For a periodic matrix coefficient `L(t)=A(t)+D(t)shift`, repeated integration by parts gives

\[
\sum_{|k|>K_0}\|L_k\|
\le
2C_p\sum_{k>K_0}k^{-p},
\]

where

\[
C_p=\frac{P^p\|L^{(p)}\|_\infty}{(2\pi)^p}.
\]

Numerical spectral differentiation of the periodic linearization gives the best stable estimate at `p=6`:

\[
\|L^{(6)}\|_\infty
\approx1.5021\times10^{-4}
\]

in physical time. For the cross-mode gap

\[
K_0=600-240=360,
\]

the resulting two-sided coefficient-tail estimate is

\[
\varepsilon_{\rm coeff}^{(6)}
\approx4.18\times10^{-7}.
\]

This uses a rigorous Fourier integration-by-parts inequality with a numerical, not interval-enclosed, derivative supremum.

## Block estimates

### Low-row coupling

With

\[
\|J_{240}^{-1}\|_\infty\approx1848,
\]

the low-row cross estimate is

\[
b_{LT}
\lesssim
1848\,P\,\varepsilon_{\rm coeff}^{(6)}
\approx0.286.
\]

### Tail-row coupling

The diagonal inverse above K600 satisfies

\[
\|D_{\rm tail}^{-1}\|
\le\frac{1}{2\pi(601)}.
\]

Thus

\[
b_{TL}
\lesssim
\frac{P\varepsilon_{\rm coeff}^{(6)}}{2\pi(601)}
\approx4.1\times10^{-8}.
\]

### Diagonal blocks

- finite/structured preconditioned defect: `1.595e-6`;
- tail-tail contraction: at most `0.7475`.

A block maximum-row estimate therefore gives approximately

\[
\max\{1.6\times10^{-6}+0.286,
\ 0.7475+4.1\times10^{-8}\}
<0.748<1.
\]

## Significance

The hybrid block-Neumann architecture is numerically closeable even after including a conservative sixth-derivative cross-tail estimate. The tail-tail diagonal block, not cross coupling, controls the margin.

## Required rigorous replacement

Validate an outward interval bound on

\[
\|L^{(6)}\|_\infty
\]

over the enclosed periodic-orbit ball. A sufficient target is approximately

\[
\|L^{(6)}\|_\infty<2.0\times10^{-4},
\]

which retains the low-row coupling comfortably below one and leaves the tail row controlled by `0.7475`.

## Status

`BLOCK_NEUMANN_CONTRACTION_NUMERICALLY_CLOSES_BELOW_0P75`

`INTERVAL_SIXTH_DERIVATIVE_BOUND_PENDING`