# C4 Finite Linear-Algebra and Shift-Bound Assessment

## Objective

Bound floating-point matrix-product error in the K=80 approximate inverse and define conservative finite Fourier-shift norm targets over a period interval. These bounds still exclude interval evaluation of the nonlinear residual and the infinite Fourier tail.

## IEEE rounding bounds

For the `645 x 645` finite Jacobian, with unit roundoff

\[
u=2^{-53}=1.1102230\times10^{-16},
\]

the standard matrix-product factor is

\[
\gamma_{645}=\frac{645u}{1-645u}
=7.16094\times10^{-14}.
\]

Using `gamma_n |A||J|` gives a product-rounding allowance

\[
2.4080\times10^{-7}.
\]

Combined with the observed inverse defect,

\[
\|I-AJ\|_\infty=2.8330\times10^{-9},
\]

the finite-double bound is

\[
Z_{0,\rm dbl}\le2.4364\times10^{-7}.
\]

For the preconditioned residual,

\[
\|AF\|_\infty=1.2941410\times10^{-11},
\]

and the matrix-vector rounding allowance is below `5e-23`, so

\[
Y_{\rm dbl}\le1.294142\times10^{-11}
\]

for the stored double `J,F`.

These are rigorous IEEE product-error formulas applied to double matrices. They do not bound the difference between those matrices and an outward interval evaluation of the exact collocation map.

## Fourier delay-shift targets

At

\[
P_0=370.9311778394287~\mathrm{yr},
\]

the K=80 finite shift matrices have numerical induced infinity norms

\[
\|S(P_0)\|_\infty=1.48234749,
\]

\[
\|S_P(P_0)\|_\infty=0.05513701,
\qquad
\|S_{PP}(P_0)\|_\infty=0.00053158.
\]

For a provisional period interval

\[
|P-P_0|\le10^{-3}~\mathrm{yr},
\]

Taylor sensitivity gives conservative finite-matrix targets

\[
\|S(P)\|_\infty\le1.483,
\]

\[
\|S_P(P)\|_\infty\le0.0552,
\qquad
\|S_{PP}(P)\|_\infty\le0.0006.
\]

The period seed/Newton correction is many orders of magnitude smaller than this interval. Outward-rounded trigonometric evaluation must still confirm these bounds.

## Combined finite-block precursor

With

\[
B\approx1847.86,
\quad
Y_{\rm dbl}\le1.294142\times10^{-11},
\quad
Z_{0,\rm dbl}\le2.4364\times10^{-7},
\quad
L_{\rm coll}\le2000,
\]

the finite block has ample contraction margin. The dominant unclosed terms are no longer ordinary floating-point multiplication or finite nonlinear conditioning; they are:

1. outward interval evaluation of exact coefficients;
2. analytic Fourier tail;
3. conversion from finite collocation to the infinite coefficient-space operator.

## Status

`FINITE_DOUBLE_ROUNDING_BOUNDS_CLOSED`

`OUTWARD_COEFFICIENT_INTERVAL_AND_INFINITE_TAIL_PENDING`