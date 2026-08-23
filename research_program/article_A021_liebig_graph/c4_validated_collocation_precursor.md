# C4 Validated-Collocation Precursor

## Objective

Evaluate the corrected K=80 Fourier solution away from its 161 collocation nodes and determine whether a continuous-function-space a posteriori correction is feasible.

## Off-grid residual convergence

The corrected K=80 trigonometric polynomial was evaluated on independent uniform grids:

| check grid | residual infinity norm |
|---:|---:|
| 1024 | `7.84854e-9` |
| 2048 | `7.84854e-9` |
| 4096 | `7.85014e-9` |
| 8192 | `7.86436e-9` |
| 16384 | `7.86436e-9` |

The stable limit is

\[
\|u'-F(u,u_{\rm del})\|_\infty
\approx7.87\times10^{-9}.
\]

Statewise maxima are approximately

\[
(1.77\times10^{-10},
3.11\times10^{-12},
2.25\times10^{-9},
7.87\times10^{-9}).
\]

This is nearly three orders of magnitude smaller than the earlier raw Fourier-seed residual and confirms that the Newton-corrected polynomial solves the continuous periodic equation accurately between collocation nodes.

## A posteriori correction scale

Using the finite phase-fixed inverse norm

\[
\|J^{-1}\|_\infty\approx1847.86,
\]

the naive inverse-times-defect scale is

\[
1847.86(7.87\times10^{-9})
\approx1.45\times10^{-5}.
\]

This is about one percent of the numerical floor margin

\[
1.4755\times10^{-3}.
\]

Therefore a continuum correction of the expected size would remain safely inside the smooth-floor region.

## Consequence for validation route

The collocation/Sobolev route is numerically viable:

1. finite Newton root residual is `1.54e-10` at nodes;
2. off-grid continuous residual is below `7.9e-9`;
3. finite inverse-times-defect is about `1.45e-5`;
4. interval derivative bounds give a large Kantorovich margin;
5. the correction scale is far below the floor margin.

The remaining proof issue is no longer whether the approximate orbit is accurate. It is proving that the finite inverse controls the phase-fixed continuum linear operator, including interpolation/tail error.

## Next mathematical target

Establish an a posteriori inverse-transfer inequality

\[
\|L^{-1}\|_{C^0\to C^1}
\le
\frac{\|J_K^{-1}\|+\delta_{\rm inv}}
{1-(\|J_K^{-1}\|+\delta_{\rm inv})\delta_L},
\]

where `L` is the continuum phase-fixed linearization, `J_K` the K=80 collocation Jacobian, `delta_L` the finite-to-continuum consistency bound, and the denominator is positive.

Once this is available, Newton–Kantorovich can validate the orbit directly in a collocation/Sobolev space without a K=80 analytic diagonal-tail contraction.

## Status

`OFF_GRID_CONTINUOUS_RESIDUAL_BELOW_8E_MINUS_9`

`VALIDATED_COLLOCATION_ROUTE_NUMERICALLY_FEASIBLE`

`CONTINUUM_INVERSE_TRANSFER_PENDING`