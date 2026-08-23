# C4 Fourier Operator-Consistency Assessment

## Objective

Measure the consistency of phase-fixed Fourier Jacobians under explicit low-mode prolongation and restriction. The relevant quantity is the preconditioned difference

\[
\delta_{K,K'}
=
\left\|J_K^{-1}
\left(J_K-R_{K'\to K}J_{K'}E_{K\to K'}\right)
\right\|_\infty.
\]

If a continuum version of this quantity is below one, a Neumann argument transfers invertibility from the finite Jacobian to the continuum linearization.

## Results

| coarse K | fine K | preconditioned consistency | period difference |
|---:|---:|---:|---:|
| 40 | 60 | 1.75747 | `3.69e-7` |
| 60 | 80 | 0.016480 | `1.00e-9` |
| 80 | 100 | 0.012943 | `2.24e-11` |
| 100 | 120 | 0.005936 | `5.63e-12` |

K=40 is insufficient in this transfer norm. Starting at K=60, the finite low-mode transfer defect is far below one and decreases to about `0.006` by K=100→120.

## K=120 solution

At K=120 (965 unknowns):

- period `370.93117783955665 yr`;
- inverse infinity norm `1847.72899`;
- node residual `3.74e-10`;
- off-grid residual `2.82e-12`;
- correction from seed `3.3827e-4`.

The off-grid residual has fallen by more than seven orders of magnitude relative to K=40.

## Interpretation

The finite inverse and low-mode operator are converging strongly. A K=100 or K=120 finite block is a better base for continuum inverse transfer than K=80, even though K=80 already solved the finite orbit accurately.

If an analytic tail estimate establishes

\[
\delta_{120,\infty}<0.01,
\]

then the continuum inverse would satisfy a bound close to

\[
\|L^{-1}\|
\lesssim
\frac{1848}{1-0.01}
<1867.
\]

This target is consistent with the observed K100→120 defect `0.00594`, but the finite sequence does not prove the continuum tail estimate.

## Remaining proof step

Bound the operator action from modes above K=120 into the retained modes and the tail-to-tail block. The naive diagonal-tail criterion remains too crude at K=120; the consistency data show that the structured periodic linearization is much better behaved than that global bound.

The next feasible validation should use the observed structured transfer defect, not revert to the rejected K=80 diagonal-only tail.

## Status

`FINITE_LOW_MODE_INVERSE_TRANSFER_DEFECT_BELOW_0P006_AT_K100_TO_120`

`CONTINUUM_TAIL_TRANSFER_PENDING`