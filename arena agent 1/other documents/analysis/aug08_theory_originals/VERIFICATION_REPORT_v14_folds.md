# Independent verification of the v14 "canonical folds" (gated four-state core, Candidate A)

Date: 2026-08-17
Method: independent numba-compiled RK4 DDE integrator implementing the v14 equations
  (donor-limited B, shifted/floored softplus, gated effort law), finite-difference
  Jacobians, |P|=|Q| characteristic root search, and carry continuation with
  delay-history carried between steps (the manuscript's own method).
Scripts: verify_gated_fourstate.py, verify_folds*.py, verify_basins.py (workspace).

System:
  dN  = r N (1-N/K) A/(A+A0) - q E N
  dA  = -B + omega_A (Aeq - A),   B = R + kappa_A N A/(A+A0)
  dZ  = (1/tau_m)[ max(0, sp_k(qEN - R) - ln2/k + delta) - Z ]
  dE  = (1 - E/Emax)[ eta E (Z(t-tau)/Dref - E/Emax) + delta0 Z(t-tau)/(Zref+Z(t-tau)) ]
  Aeq = Aeq_intrinsic + kappa_A K / omega_A  (= 5050)
Parameters: r=0.02, K=100, q=0.001, eta=0.914, Emax=30, delta0=0.01, Dref=1,
  tau_m=5, Zref=1, k=10, delta=ln2/10, kappa_A=0.05, omega_A=1e-3, A0=1,
  Aeq_intrinsic=50.

## Results vs v14 claims

| Quantity            | v14 claim                        | Independent result                  | Status |
|---------------------|----------------------------------|-------------------------------------|--------|
| Equilibrium         | N*=89.525622655, Z*=ln2/10,      | identical to all shown digits       | CONFIRMED |
| (N*,Z*,E*,A*)       | E*=2.089623398, A*=397.866535    |                                     |        |
| tau=0 spectrum      | 0.000372 +/- 0.02765i (unstable) | 0.000372 +/- 0.027646i,            | CONFIRMED |
|                     | plus real modes                  | real -0.27812, -0.001032           |        |
| tau_-               | 3.7849 yr                        | 3.784866 yr                        | CONFIRMED |
| tau_+               | 150.12 yr                        | 150.121765 yr                      | CONFIRMED |
| Lower fold SNPO,L   | ~5.62 yr                         | cycle steady at 5.62 (amp 23.3),   | CONFIRMED |
|                     |                                  | collapses by 5.64 => fold ~5.63    | (to ~0.01) |
| Upper fold SNPO,R   | in (64.4, 64.5) yr               | cycle steady at 64.5 (amp 11.0),   | CONFIRMED |
|                     |                                  | collapses by 64.25 => fold ~64.4   | (to ~0.1) |
| Upper-window period | ~158 yr (near tau_+) -> ~73 yr   | 156.4 yr -> 73.2 yr                | CONFIRMED |
|                     | at lower edge                    |                                     |        |
| Lower-window period | ~375 yr (tau=4)                  | 371 yr (tau=4.5), amp ~49          | consistent |
| Upper bistable      | (64.4, 150.12) yr, wide          | cycle coexists with stable eq over  | CONFIRMED |
| window              |                                  | ~(64.4, 150.1); three-state proxy  | (the 64.4 |
|                     |                                  | (148.3) would have been wrong      | value is REAL) |
| Monostable middle   | (5.62, 64.4) quiet from generic  | quiet from all 5 IC classes,       | CONFIRMED |
|                     | histories                        | tau in [6, 60]                     |        |

## Discrepancy found

1. "Reached from generic histories only for tau >~ 143 yr" (abstract/conclusion):
   NOT reproduced. From far-from-equilibrium ICs, high-stock classes
   (N=1.2N* with Z0 in {0.30, delta, 0.01}; N=1.05K) reach the upper-window
   cycle down to tau ~ 75-100. Only the depleted-stock class (N=0.8N*) has a
   threshold near ~135-140. So tau~143 matches the depleted class only; the
   abstract states it as generic, and its own next sentence ("the large cycle
   tends to capture abundant, well-stocked systems") describes exactly the
   class that reaches it ~twice as deep. The two abstract statements are in
   tension on this point.

## File-level finding (supplied CSVs)

2. snpo_lower_fold_{variational,tip,push}.csv record mu_dom_imag = 0.0 at every
   point: the dominant Floquet multiplier is REAL, 0.2396 (tau=4.0) ->
   0.9644 (tau=5.5815). This contradicts the manuscript text's "dominant
   complex Floquet pair ... coalescing at +1" (Data section and limitations
   item) and instead supports the text's other narrative: a real multiplier
   approaching +1 (the SNPO signature). The manuscript contains both
   narratives; only the real-multiplier one is supported by its own data
   files. Also: the collocation orbit is still converged (residual ~1e-12)
   at tau=5.5815, past the claimed stable-branch fold at 5.574-5.575.

## Bottom line

The v14 canonical fold numbers are real and reproducible:
  lower fold ~5.63 yr, upper fold ~64.4 yr (not ~148),
  tau_- = 3.785, tau_+ = 150.12, wide upper bistable window (64.4, 150.1),
  monostable middle confirmed.
The bisection-derived values survive carry-continuation. The remaining
corrections are (a) the abstract's "tau >~ 143" generic-reachability claim is
IC-specific and overstated, and (b) the "complex Floquet pair coalescing at +1"
sentences are contradicted by the supplied collocation CSVs (real multiplier).
