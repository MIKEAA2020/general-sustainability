# C4 K80 Storage-Hull Interval Assessment

## Objective

Use the exported one-ULP Fourier coefficient/period hulls to perform an actual outward interval evaluation of the finite K=80 collocation residual and bound storage-induced Jacobian uncertainty.

## Coefficient and period hulls

The maximum reconstructed physical-node radii from one-ULP coefficient hulls are:

\[
(2.12\times10^{-14},
1.27\times10^{-13},
1.33\times10^{-16},
4.32\times10^{-15})
\]

for `(N,A,Z,E)`. The delayed-Z radius is

\[
1.50\times10^{-16},
\]

and the period radius is one ULP,

\[
5.68\times10^{-14}~\mathrm{yr}.
\]

## Outward interval residual

Interval evaluation of the smooth C4 vector field at all K=80 collocation phases gives physical-time residual interval radius at most

\[
3.03\times10^{-15}.
\]

After conversion to the normalized periodic collocation equation, the residual radius is

\[
1.88\times10^{-12}.
\]

Combining this with the finite approximate inverse gives

\[
Y_{\rm storage}
\le3.49\times10^{-9}.
\]

## Storage-induced Jacobian uncertainty

Using the interval state radii, the outward vector-field Hessian bound, period radius, and padded delay-shift sensitivities gives

\[
\delta J_{\rm storage}
\le2.30\times10^{-8}.
\]

Together with IEEE matrix-product rounding,

\[
Z_{0,\rm storage}
\le4.27\times10^{-5}.
\]

These values cover coefficient/period storage hulls and finite arithmetic. They do not cover the true orbit ball or infinite tail.

## Finite storage-hull radii polynomial

With

\[
B=1847.864,
\qquad L=2000,
\]

use

\[
p_{\rm storage}(r)
=Y_{\rm storage}+Z_{0,\rm storage}r+BLr^2-r.
\]

It is negative, for example:

| `r` | `p_storage(r)` |
|---:|---:|
| `1e-8` | `-6.15e-9` |
| `2e-8` | `-1.50e-8` |
| `5e-8` | `-3.73e-8` |
| `1e-7` | `-5.96e-8` |
| `2e-7` | `-4.87e-8` |

Thus the finite K=80 system remains interval-closeable after incorporating the portable one-ULP coefficient data.

## Scope

This closes the raw coefficient/storage-rounding objection for the finite block. It does not validate:

- the continuum Fourier tail;
- the true periodic-orbit ball;
- continuum Floquet multipliers;
- the product NAIM theorem.

## Status

`K80_STORAGE_HULL_INTERVAL_RESIDUAL_CLOSED`

`FINITE_STORAGE_HULL_RADII_POLYNOMIAL_NEGATIVE`

`INFINITE_TAIL_AND_TRUE_ORBIT_BALL_PENDING`