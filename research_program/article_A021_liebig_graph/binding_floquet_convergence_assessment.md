# Binding C4 Floquet Convergence Assessment

## Result

Three independent history-grid levels for the selected gated Candidate-A C4 cycle at `tau=4.5` give:

| `dt` | history dimension | phase multiplier | dominant nontrivial multiplier |
|---:|---:|---:|---:|
| 0.25 | 76 | 0.98687854 | 0.68774849 |
| 0.10 | 184 | 0.99774865 | 0.68770289 |
| 0.05 | 364 | 1.00136091 | 0.68768669 |

A linear-in-step extrapolation gives

\[
\mu_s(0)\approx0.68767164.
\]

Using twice the finest two-level difference as a conservative empirical discretization allowance gives

\[
\mu_s\in[0.68763924,0.68770405].
\]

The entire empirical interval lies strictly inside the unit circle. The corresponding normal exponent is approximately

\[
\beta_x\approx1.0094\times10^{-3}\ {\rm yr}^{-1}.
\]

## Interpretation

This is strong convergence evidence for a simple phase direction and a stable leading nontrivial multiplier. It is not an interval enclosure of the continuum RFDE monodromy operator. The phase multiplier's deviation from one reflects orbit/period/discretization error and decreases to the `10^-3` level on the finest grid.

The finite-history matrices at each level include all multipliers of that discretization. Their stable spectra agree in the leading modes, while the remaining multipliers cluster near zero, consistent with eventual compactness.

## Remaining rigorous step

A formal proof still requires one of:

1. an outward-rounded collocation/monodromy enclosure with an a posteriori operator-error bound;
2. a validated periodic-orbit and Floquet package from a theorem-capable DDE continuation tool;
3. an exact source-attested complete C4 Floquet computation accepted at theorem-verification status.

The present result supports numerical NAIM status but not manuscript theorem promotion.