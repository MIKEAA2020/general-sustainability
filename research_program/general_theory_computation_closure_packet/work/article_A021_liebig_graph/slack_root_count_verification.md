# Slack-Equilibrium Rightmost-Root Count

## Objective

Strengthen the provisional identical-C4 slack equilibrium used in the minimal two-block scaffold by checking that the refined pair near `-0.00052673 +/- 0.02208464 i` is globally rightmost, rather than merely the rightmost root returned by a discretization.

## Analytic exterior bound

For

\[
\Delta(\lambda)=\lambda I-J-De^{-\lambda\tau},
\qquad \tau=10,
\]

if `Re(lambda)>=a` and

\[
|\lambda|>\|J\|_2+\|D\|_2e^{-a\tau},
\]

then `Delta(lambda)` is invertible by a Neumann-series estimate. Numerically,

\[
\|J\|_2=0.2002948449,
\qquad
\|D\|_2=1.7850160431.
\]

Thus every root in each tested right half-plane lies inside a finite rectangle of radius approximately `2.0`.

## Argument-principle counts

The winding number of `det Delta(lambda)` was computed at 70-digit precision around the resulting rectangles. Counts were stable under 2,000, 4,000, 8,000, and 16,000 samples per edge.

| left boundary `a` | roots with `Re(lambda)>=a` |
|---:|---:|
| `0` | 0 |
| `-0.0005` | 0 |
| `-0.0006` | 2 |
| `-0.0007` | 2 |
| `-0.0010` | 2 |
| `-0.0011` | 3 |

The first pair is therefore the unique pair in the strip

\[
-0.0006\le\operatorname{Re}\lambda<-0.0005.
\]

Direct determinant Newton refinement gives

\[
\lambda_{1,2}
=-0.00052673009564114
\pm0.0220846350193287i,
\]

with residual below `3e-21`. The next root is the real root

\[
\lambda_3=-0.00103151651411957,
\]

consistent with the root count changing from two to three between left boundaries `-0.0010` and `-0.0011`.

## Status

This combines an analytic exterior exclusion with mesh-converged high-precision winding counts and is substantially stronger than method-of-lines ordering alone. It is not interval arithmetic: the contour image was not enclosed by outward-rounded complex intervals. The result is therefore classified as **high-confidence numerical root-count certification**, not a formal computer-assisted proof.

## Consequence for the scaffold

The slack asymptotic rate is supported as

\[
\beta_y=0.00052673009564114\ {\rm yr}^{-1}
\]

up to the distinction between numerical certification and rigorous enclosure. The slack block remains the rate-limiting factor of the two-block product.