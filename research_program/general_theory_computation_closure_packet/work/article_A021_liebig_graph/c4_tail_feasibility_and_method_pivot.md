# C4 Infinite-Tail Feasibility and Validation-Method Pivot

## Objective

Test whether the simplest weighted-Fourier radii proof—K=80 finite inverse plus diagonal `2 pi i k` tail—can close with the available derivative bounds.

## Diagonal tail criterion

For Fourier modes `|k|>K`, the differential diagonal has magnitude `2 pi |k|`. A crude tail inverse gives

\[
\|D_{\rm tail}^{-1}\|
\le\frac{P}{2\pi(K+1)}.
\]

A contraction based only on diagonal dominance requires approximately

\[
\frac{P L_F}{2\pi(K+1)}<1,
\]

where `L_F` bounds the vector-field derivative in the coefficient algebra.

With

\[
P\approx370.9312,
\]

and the broad outward box bound

\[
L_F\le20.7205,
\]

the factor is:

| K | diagonal-tail factor |
|---:|---:|
| 80 | 15.10 |
| 512 | 2.38 |
| 1024 | 1.19 |
| 1224 | 0.999 |
| 1600 | 0.764 |

Thus a **simple diagonal tail cannot close at K=80**, regardless of the excellent finite Newton residual.

## Tighter local derivative information

On the corrected K=80 orbit samples, the current-plus-delayed Jacobian infinity norm ranges from approximately `0.34` to `7.09`. Structural optimization of the delayed effort derivative gives an orbit-box row bound near `8.6`, much lower than the dependency-inflated broad-box value.

Even with `L_F=8.6`, diagonal dominance needs approximately

\[
K\gtrsim507.
\]

Hence a K=512 tail threshold is plausible but marginal. The finite numerical seed contains modes through 512, but coefficients beyond about 80 are at the numerical-noise floor; they are useful as zero/near-zero initial guesses, not as validated tail data.

## Empirical forcing tail

For the K=80 seed, the nonlinear vector-field coefficients beyond K are numerically tiny. With weight `nu=1.01`, the weighted residual tail over `80<|k|<=160` is of order

\[
(10^{-10},10^{-12},4.5\times10^{-9},1.3\times10^{-8})
\]

before diagonal inversion. This explains why the numerical Newton solution succeeds despite the failure of the crude global derivative tail criterion.

The obstacle is not the residual tail; it is proving contraction of all possible tail perturbations.

## Method decision

Do not attempt to certify the infinite problem with a K=80 diagonal tail. Choose one of:

1. **Structured extended tail:** retain the K=80 dense inverse, add a finite structured block through at least K=512, and use diagonal dominance only beyond that block;
2. **Validated collocation/Sobolev method:** enclose the periodic boundary-value problem directly with interpolation-error estimates, avoiding analytic weighted-tail contraction;
3. **Sharper tail linearization:** invert the dominant periodic linearized tail operator rather than only `2 pi i k`.

The most feasible route is option 2 because the phase-corrected collocation root already has residual `1.54e-10`, a strong finite Kantorovich margin, and explicit interval derivative bounds. A validated trigonometric-collocation interpolation-error theorem would avoid a 4000-plus-dimensional interval inverse.

## Revised status

- K=80 finite Newton block: excellent and ready.
- K=80 simple diagonal analytic tail: **fails**.
- K about 512 structured tail: plausible but computationally heavier.
- validated collocation/Sobolev enclosure: recommended next route.

## Status labels

`K80_DIAGONAL_TAIL_REJECTED`

`VALIDATED_COLLOCATION_ROUTE_RECOMMENDED`

No theorem promotion follows.