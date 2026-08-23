# C4 Collocation and Inverse Convergence Assessment

## Objective

Test whether the phase-fixed finite Jacobian inverse and corrected periodic solution stabilize as Fourier truncation increases. This is the numerical precursor to a continuum inverse-transfer theorem.

## Results

| K | dimension | corrected period | inverse infinity norm | off-grid residual |
|---:|---:|---:|---:|---:|
| 40 | 325 | 370.9311774696 | 1847.8333 | `2.71e-5` |
| 60 | 485 | 370.9311778385 | 1847.8959 | `8.04e-7` |
| 80 | 645 | 370.9311778395 | 1847.8638 | `7.85e-9` |
| 100 | 805 | 370.9311778396 | 1847.7928 | `2.67e-10` |

The period stabilizes to approximately eleven decimal places by K=60. The inverse norm remains within `0.11` across all four levels, a relative spread below `6e-5`. The off-grid residual falls by roughly five orders of magnitude between K=40 and K=100.

## Interpretation

The phase-fixed inverse is not growing with truncation. Numerically,

\[
\|J_K^{-1}\|_\infty<1848
\]

for all tested K. This strongly supports a bounded continuum inverse rather than an impending tail singularity.

The K=100 off-grid residual

\[
2.67\times10^{-10}
\]

combined with the inverse norm gives a correction scale below

\[
5.0\times10^{-7},
\]

far below the floor margin.

## What this closes

- numerical convergence of the phase-fixed period;
- numerical stability of the inverse norm under K refinement;
- spectral decay of the off-grid residual;
- feasibility of an inverse-transfer theorem with target continuum bound near 1850.

## What remains

A rigorous inverse-transfer result still requires:

1. a normed injection/projection between the K and continuum spaces;
2. a bound `delta_L` on the difference between the continuum linearization and the lifted finite linearization;
3. proof that

\[
(1850)\,\delta_L<1;
\]

4. the resulting Neumann estimate

\[
\|L^{-1}\|
\le\frac{1850}{1-1850\delta_L}.
\]

The numerical data indicate that `delta_L` is small, but off-grid residual convergence is not itself an operator-norm consistency bound.

## Status

`PHASE_FIXED_INVERSE_NORM_CONVERGED_NUMERICALLY`

`CONTINUUM_INVERSE_TRANSFER_BOUND_PENDING`