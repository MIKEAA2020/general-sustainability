# C4 Finite Radii Polynomial and Fourier-Tail Precursor

## Finite K=80 radii polynomial

Use the conservative finite-block quantities

\[
Y=1.294142\times10^{-11},
\qquad
Z_0=2.4364\times10^{-7},
\]

\[
B=1847.8638,
\qquad
L=2000.
\]

The numerical finite-block radii polynomial

\[
p_{\rm fin}(r)=Y+Z_0r+BLr^2-r
\]

is negative over a wide test range:

| `r` | `p_fin(r)` |
|---:|---:|
| `1e-10` | `-8.70e-11` |
| `1e-9` | `-9.83e-10` |
| `1e-8` | `-9.62e-9` |
| `1e-7` | `-6.30e-8` |
| `2e-7` | `-5.22e-8` |

Thus the finite K=80 Newton system has a robust numerical radii margin. This is not yet an interval theorem because `Y,Z0,L` do not include exact coefficient intervals and the infinite tail.

## Empirical geometric coefficient tail

Over signal-dominated modes `20<=k<=70`, all four state coefficients are bounded empirically by

\[
|a_{k,j}|\le C_j q^k,
\qquad q=0.85,
\]

with

\[
(C_N,C_A,C_Z,C_E)
=(0.003479,0.000547,0.001942,0.027818).
\]

If this geometric envelope were validated for all `k>=20`, the two-sided unweighted coefficient tail beyond `K=80` would satisfy approximately

\[
(8.90\times10^{-8},
1.40\times10^{-8},
4.97\times10^{-8},
7.12\times10^{-7}).
\]

This envelope is fitted evidence, not a proof for uncomputed modes.

## Revised initial analytic weight

The weighted tail magnifies geometric tails by replacing `q` with `q nu`. The implied E-component tail is approximately:

| `nu` | empirical weighted E-tail beyond K=80 |
|---:|---:|
| 1.01 | `1.69e-6` |
| 1.02 | `3.99e-6` |
| 1.03 | `9.40e-6` |
| 1.05 | `5.17e-5` |

Therefore the first interval execution should use

\[
\boxed{K=80,\qquad \nu=1.01}
\]

rather than `nu=1.05`. The smaller weight substantially reduces tail amplification while retaining a weighted convolution algebra.

## What must make the tail rigorous

One of the following is required:

1. an interval recurrence/majorant proving `|a_k|<=Cq^k` for every `k>K`;
2. a Cauchy estimate from a validated complex strip;
3. a Sobolev/polynomial-tail radii proof avoiding analytic geometric weights;
4. a posteriori Fourier tail bounds derived from the diagonal `2 pi i k` dominance of the RFDE coefficient equations.

The fourth route is most compatible with the present Fourier Newton system: invert the diagonal derivative on `|k|>K` and bound nonlinear convolutions in the chosen weighted algebra.

## Status

`FINITE_K80_RADII_POLYNOMIAL_NEGATIVE_NUMERICALLY`

`EMPIRICAL_TAIL_ENVELOPE_AVAILABLE`

`RIGOROUS_INFINITE_TAIL_PENDING`