# C4 Finite-Block Interval Derivative Assessment

## Objective

Replace directional Hessian sampling by an outward interval bound for the smooth C4 vector field on a rectangular box containing the selected orbit, then propagate that bound to a conservative finite-collocation Jacobian-Lipschitz budget.

## Validated state/delay box

\[
N\in[45,96],\quad
A\in[830,950],\quad
Z\in[0,0.7],\quad
E\in[0.3,21],\quad
Z_{\rm del}\in[0,0.7].
\]

This box contains the reproduced periodic orbit with margin.

## Outward interval vector-field bounds

Using `mpmath.iv` and structural softplus derivative bounds

\[
0\le \operatorname{sp}'_k\le1,
\qquad
0\le \operatorname{sp}''_k\le k/4=2.5,
\]

the induced infinity bounds are:

\[
\|F\|_\infty\le13.30145,
\]

\[
\|DF\|_\infty\le20.72046,
\]

\[
\|D^2F\|_{\infty,\mathrm{bilinear}}\le1.91308.
\]

The output-component Hessian bounds are approximately

\[
(0.002520,\ 0.000562,\ 0.010258,\ 1.913074).
\]

The full floor argument has interval lower bound

\[
6.54\times10^{-7}>0
\]

on the entire broad box. For Candidate A, `delta=ln(2)/k`, so the floor argument is the strictly positive softplus itself. Thus the outer `max` is inactive throughout this bounded box, not merely at the collocation nodes.

## Fourier shift norms

For the K=80, 161-node finite collocation system at the corrected period, numerical induced infinity norms are

\[
\|S(P)\|_\infty\approx1.48235,
\]

\[
\|S_P(P)\|_\infty\approx0.05514,
\qquad
\|S_{PP}(P)\|_\infty\approx0.000532.
\]

For the finite-block interval implementation, the padded bounds

\[
\|S\|_\infty\le1.5,
\quad
\|S_P\|_\infty\le0.06,
\quad
\|S_{PP}\|_\infty\le0.001,
\quad
P\in[370,372]
\]

are proposed. They still require outward-rounded verification of the finite matrices.

## Conservative collocation Hessian budget

The state-state contribution is bounded by

\[
P\|D^2F\|\max(1,\|S\|)^2
\le372(1.91308)(1.5)^2
<1602.
\]

Mixed state-period and period-period terms are bounded using `F`, `DF`, `D2F`, `S_P`, `S_PP`, and the state box. A conservative aggregate target is

\[
L_{\rm coll}\le2000.
\]

With the previously computed

\[
B\approx1847.86,
\qquad
Y_{\rm num}\approx1.2941\times10^{-11},
\]

the finite-block Kantorovich precursor becomes

\[
B L_{\rm coll}Y_{\rm num}
<4.8\times10^{-5}\ll\frac12.
\]

Therefore the finite interval Newton block has a very large margin even under this conservative derivative budget.

## What is closed

- outward interval bounds for `F`, `DF`, and `D2F` on a broad orbit box;
- a broad-box proof that the memory floor is inactive;
- a conservative finite-collocation Hessian target well inside the numerical Kantorovich budget.

## What remains

- outward-rounded verification of the Fourier shift matrix norms;
- interval inverse/preconditioner and residual;
- weighted sequence-space convolution tail;
- rigorous radii polynomial on the infinite coefficient space.

## Status

`FINITE_BLOCK_INTERVAL_DERIVATIVE_BOUNDS_CLOSED`

`INFINITE_FOURIER_TAIL_AND_OUTWARD_LINEAR_ALGEBRA_PENDING`