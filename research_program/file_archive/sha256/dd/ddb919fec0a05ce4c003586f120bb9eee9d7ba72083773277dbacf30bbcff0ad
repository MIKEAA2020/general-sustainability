# C4 Periodic Linearization Fourier-Tail Threshold

## Objective

Replace broad state-box derivative bounds by the actual Fourier convolution norm of the periodic linearization, and determine where a simple diagonal tail becomes contractive.

## Periodic linearization

Along the K=120 corrected periodic orbit,

\[
\dot v(t)=A(t)v(t)+D(t)v_Z(t-\tau),
\]

with period

\[
P=370.9311778396~\mathrm{yr}.
\]

The Fourier coefficient matrices of `A(t)` and `D(t)` were computed on a 4096-point check grid. Their weighted convolution norms are:

| weight `nu` | `||A||_{l1_nu}` | `||D||_{l1_nu}` | total `L_nu` | diagonal tail threshold |
|---:|---:|---:|---:|---:|
| 1.000 | 0.41091 | 8.56573 | 8.97665 | K >= 529 |
| 1.001 | 0.41143 | 8.58269 | 8.99413 | K >= 530 |
| 1.005 | 0.41355 | 8.65132 | 9.06487 | K >= 535 |
| 1.010 | 0.41625 | 8.73897 | 9.15522 | K >= 540 |

The threshold solves

\[
\frac{P L_\nu}{2\pi(K+1)}<1.
\]

## Consequence

The earlier broad-box estimate predicted a threshold above 1200. The actual periodic linearization reduces the threshold to approximately

\[
K_{\rm tail}=540
\]

for `nu=1.01`.

Thus a feasible rigorous Fourier architecture is:

1. structured finite/medium block through at least K=540;
2. diagonal analytic inverse for modes above K=540;
3. convolution-tail bounds using `L_nu`;
4. low-mode inverse supplied by the converged phase-fixed collocation system.

For validation margin, use K=600 or larger rather than the barely contractive K=540 threshold.

## Remaining rigor

The reported coefficient norms are high-resolution numerical sums, not outward interval bounds. A proof requires:

- interval enclosure of the orbit coefficients;
- interval convolution norms for `A_k,D_k`;
- a validated tail bound beyond the computed Fourier window;
- a structured finite-block inverse/preconditioner through K about 600.

## Method decision

The simple diagonal-tail approach is not impossible; it was merely impossible at K=80. The corrected route is a **hybrid structured block plus diagonal tail** with K around 600.

This competes with the validated collocation/Sobolev route. The hybrid Fourier route has the advantage that the tail threshold is now explicit and moderate enough for matrix-free sparse computation.

## Status

`PERIODIC_LINEARIZATION_TAIL_THRESHOLD_K540_NUMERICALLY_IDENTIFIED`

`STRUCTURED_K600_PLUS_DIAGONAL_TAIL_RECOMMENDED`

No continuum theorem is claimed.