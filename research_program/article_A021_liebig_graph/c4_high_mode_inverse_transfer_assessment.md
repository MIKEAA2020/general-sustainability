# C4 High-Mode Inverse-Transfer Assessment

## K=160 refinement

The phase-fixed Fourier system was extended to

\[
K=160,
\qquad
1285\ \text{unknowns}.
\]

Results:

\[
P_{160}=370.9311778394262~\mathrm{yr},
\]

\[
\|J_{160}^{-1}\|_\infty=1847.71102,
\]

\[
\|F_{160}\|_{\rm nodes,\infty}=4.67\times10^{-10},
\]

\[
\|F_{160}\|_{\rm offgrid,\infty}=2.35\times10^{-12}.
\]

The inverse remains stable and the off-grid defect is at the numerical floor.

## K=120 to K=160 transfer

Under explicit Fourier prolongation and restriction, the preconditioned consistency defect is

\[
\left\|J_{120}^{-1}
\left(J_{120}-R_{160\to120}J_{160}E_{120\to160}\right)
\right\|_\infty
=4.58\times10^{-5}.
\]

This is more than two orders of magnitude smaller than the K=100 to K=120 value `0.00594`.

The raw Jacobian difference is only `0.02075`, despite the interpolation maps having infinity norms above four.

## Numerical inverse-transfer implication

Taking the observed defect literally, a Neumann transfer gives

\[
\|L^{-1}\|\lesssim
\frac{1847.711}{1-4.58\times10^{-5}}
\approx1847.80.
\]

Even a tenfold safety multiplier on the observed high-mode defect gives a transfer denominator above `0.9995` and an inverse bound below about `1848.6`.

This is not a rigorous continuum estimate, but it sharply localizes the remaining task: prove that the unrepresented modes beyond K=160 contribute a preconditioned defect below a modest threshold, for example `10^-3`.

## Updated consistency sequence

| pair | preconditioned defect |
|---|---:|
| 40→60 | 1.75747 |
| 60→80 | 0.016480 |
| 80→100 | 0.012943 |
| 100→120 | 0.005936 |
| 120→160 | 0.0000458 |

The abrupt final decrease indicates that K=160 resolves the important structured linearized couplings missed by the crude diagonal-tail estimate.

## Status

`HIGH_MODE_FINITE_INVERSE_TRANSFER_DEFECT_BELOW_5E_MINUS_5`

`CONTINUUM_TAIL_PROOF_PENDING`

The next proof step is an analytic bound on modes above 160, not further low-mode Newton correction.