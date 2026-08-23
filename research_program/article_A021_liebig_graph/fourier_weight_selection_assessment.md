# Fourier Weight and Truncation Assessment

## Objective

Complete the next executable pre-interval step in Module 1: choose a defensible Fourier truncation and initial analytic weight from the archived C4 seed without inventing a tail theorem.

## Coefficient decay

Log-linear fits over signal-dominated modes `10<=k<=70` give:

| state | decay slope | implied coefficient ratio `exp(-slope)` | `R^2` |
|---|---:|---:|---:|
| `N` | `-0.27437` | 1.3157 | 0.9947 |
| `A` | `-0.24449` | 1.2770 | 0.9206 |
| `Z` | `-0.22990` | 1.2585 | 0.9975 |
| `E` | `-0.24687` | 1.2800 | 0.9968 |

The slowest observed decay is in `Z`, suggesting that weights below about `1.25` are compatible with the signal-dominated coefficients. This is not a validated analyticity radius.

Beyond roughly 80–120 modes, several coefficient sequences reach the numerical noise floor. Those coefficients must not be used to infer analytic tails.

## Truncation comparison

| retained modes `K` | residual infinity norm | RMS residual | floor margin |
|---:|---:|---:|---:|
| 40 | `2.74e-5` | `3.40e-6` | `0.001475556` |
| 60 | `1.68e-6` | `2.18e-7` | `0.001475543` |
| 80 | `1.48e-6` | `2.12e-7` | `0.001475542` |
| 100 | `1.48e-6` | `2.12e-7` | `0.001475542` |

Improvement saturates by `K=80`; higher modes primarily add numerical noise.

## Initial weight choice

Use

\[
K=80,
\qquad
\nu=1.05
\]

for the first outward-rounded radii-polynomial attempt.

At `K=80`, truncated weighted residual sums over `|k|<=2K` are approximately:

\[
(4.14\times10^{-9},
2.70\times10^{-6},
1.35\times10^{-7},
4.07\times10^{-6})
\]

for `nu=1.05`. For `nu=1.10`, the corresponding `A` residual rises to about `5.95e-5`, so `nu=1.05` gives a safer initial inverse/tail budget.

These weighted residual sums are diagnostics only. They are not the Newton-preconditioned residual `Y`, and the residual tail beyond `2K` remains to be enclosed analytically.

## Decision

The interval execution should begin with finite seed `K=80`, weight `nu=1.05`, and outward-rounded convolution/tail bounds. The archived 512-mode seed remains useful for generating coefficients and cross-checking decay, but should not be treated as a 512-mode validated analytic object.

## Status

`FOURIER_TRUNCATION_AND_INITIAL_WEIGHT_SELECTED_NUMERICALLY`

Radii-polynomial constants and a true analytic tail remain pending.