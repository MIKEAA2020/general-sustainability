# Stage-structured (maturation-delay) r-window decomposition — results (2026-08-08)

**Formulation (delayed-recruitment / stage-lumped; the Gurney-Blythe-Nisbet
class already cited in the manuscript for its laboratory evidence):**

    dN/dt = r N(t-g) (1 - N(t-g)/K) - q E N
    deficit d = q E N - r N(t-g)(1 - N(t-g)/K)     (perceived extraction minus
                                                     current maturing regeneration)
    dZ/dt = (max(0, softplus(d) - ln2/k + delta) - Z)/tau_m
    dE/dt = (1 - E/Emax) [ eta E (Z(t-tau)/Dref - E/Emax)
                           + delta0 Z(t-tau)/(Zref + Z(t-tau)) ]

Equilibrium is IDENTICAL to the base core (N* = K(1-qE*/r), Z* = delta, E* from
the same quadratic) — a clean comparison, as in the Droop test. Files:
`stage_r_window.py` (two-delay Hopf criterion, validated at g=0 against the base
windows), `stage_decomp2.py` (validated integrators + nonlinear tau=0 classifier).

## Verified results

### 1. Validation
- g=0 reproduces the base windows: (0.00796, 0.0219) at eta=0.914; (0.00676,
  0.0603) at eta=3.0  [base: (0.0080,0.0223)/(0.0068,0.0612)].
- tau=0 classification is NONLINEAR (ground truth): 1%-perturbation runs with a
  single-delay RK4 integrator using the validated droop_test pattern; two-delay
  integrator used only when min(g,tau) > 8*dt; dt-convergence confirmed
  (r=0.3,g=5,tau=10: P=17.00/16.95/16.96, amp=8.648/8.655/8.657 at
  dt=0.1/0.05/0.02).

### 2. Three-part result (the "negative" is not uniform; CORRECTED after fine mapping)

**(a) Late-maturing stocks (g >= 5 yr): fast-r institutional mechanism
absent.** No tau=0-stable points with crossings at r >= 0.6 for g in {5,10} at
either eta (the g=5 institutional window tops out at r ~ 0.33). The fast-r
decadal oscillations are the BIOLOGICAL delayed-recruitment (cohort) mechanism:
at r=0.5, g=5 the tau=0 system already oscillates with period ~20 yr, matching
the cohort-resonance periods (10-15 yr) identified as the cod confound.

**CORRECTION — short maturation delays RELOCATE the window into fish range.**
An earlier coarse grid (r in {0.7, 1.0}) missed this. Fine mapping (0.005-0.03
in r) shows continuous bands on the locus r*g ~ 1.5-1.6:

| g (yr) | r-band (eta=0.914) | r-band (eta=3.0) | tau-window at band centre | period | nonlinear verify |
|---|---|---|---|---|---|
| 1 | 1.565-1.585 | 1.54-1.61 | (1.6, 3.5) yr | ~4 yr | r=1.57, tau=2.5 (eta=3): P=4.0, amp=3.5; tau=2.76 (eta=.914): P=4.02, amp=2.38; dt-converged |
| 2 | 0.77-0.81 | 0.71-0.86 | (2.6, 7.8) yr | ~8 yr | r=0.8, tau=5.5 (eta=3): P=8.04, amp=12.4; tau=5.14 (eta=.914): P=7.98, amp=6.66; dt-converged |
| 3 | 0.50-0.55 | 0.40-0.55 | — | — | — |
| 5 | 0.28-0.33 | none | (9.9, 20.3) yr | ~17 yr | r=0.3, tau=10: P=16.96, amp=8.66 (dt-converged); tau=21 stable |

The g=2 band's tau-window (2.6, 7.8 yr) is INSIDE the documented governance-lag
distribution (2-13 yr), and its period (~8 yr) is decadal. The g=1 band
(r ~ 1.54-1.61) is at the top of the real fish range (anchovy-class). Band
widths grow with eta (g=2: width 0.04 at eta=0.914 vs 0.15 at eta=3.0) and are
parameter-sensitive; the g=7,10 bands deviate from the r*g ~ 1.5-1.6 regularity
(rg = 1.26, 0.8). Not collocation-classified; mapped at finite resolution.

**(b) Slow r (r=0.02): any maturation delay g >= 1 yr destroys the "quiet"
equilibrium.** The tau=0 system is already oscillatory (biological cohort cycle,
P ~ 250-360 yr; e.g. g=5: P=358.8 yr, N swinging 28.5-95.4, physically bounded,
E saturating at Emax). This REINFORCES the centuries-long-period untestability
conclusion: the slow-r system is not even quietly stable once recruitment is
lagged — the institutional-delay question becomes moot at slow r.

**(c) Middle band: maturation delay CREATES genuine institutional-delay windows
at decadal periods for slow-growing, late-maturing stocks (r*g ~ 1.2-1.5).**
For tau=0-stable points with crossings (eta=0.914, sampled r grid 0.03-0.6):
g=3 -> r in (0.50,0.55); g=5 -> (0.28,0.33); g=7 -> (0.15,0.20); g=10 -> r~0.08.
At eta=3.0: g=3 -> r in (0.40,0.55).
Examples verified nonlinearly (two-delay RK4):
- r=0.3, g=5, eta=0.914: tau=0 stable; crossings at tau~9.9 yr (P~19) and
  tau~20.3 yr (P~22); tau=10 -> sustained cycle P=16.96 yr, amp=8.66
  (dt-converged); tau=21 -> stable.
- r=0.1, g=10, eta=0.914: crossings at tau~27.5 yr (P~39) and tau~73 yr (P~73);
  tau=3 and tau=25 stable.

This band includes cod-class stocks (r~0.2-0.3, g~5-8): the model's predicted
institutional-cycle period there (~17-30 yr) is the same order as the observed
Iceland-cod 10-15-yr cycles — resolving the 15-25x period mismatch of the
four-state core — but the cohort mechanism predicts overlapping periods, so the
field discrimination between institutional and biological delay-oscillation
remains confounded. The band is NOT claimed as a closed result: characterised at
sampled (r,g) points only; no collocation-grade Floquet tracking; no dt-converged
Hopf-locus mapping.

### 3. Discrepancy with the earlier session scan (honest note)
The prior-session stage scan (reported as "window remained at low a~0.01-0.02",
no extension) is not on file; it used a maturation-RATE (ODE) stage formulation.
The delayed-recruitment (maturation-DELAY) form reconstructed here — the class
consistent with the manuscript's cited Gurney-blowfly laboratory mechanism and
with cohort resonance — shows the three-part structure above. The fast-r and
slow-r conclusions agree between formulations; the middle band is formulation-
dependent and must be stated as such.

## Recommendation for the manuscript (final, after the 2026-08-08 correction)
- CLAIM: (a) Droop coupling does not move the r-window (clean negative);
  (b) stage structure: fast-r institutional stability survives for
  LATE-MATURING stocks (g >= 5 yr); the slow-r centuries-long barrier is
  reinforced (slow-r system is biologically oscillatory at tau=0 once
  recruitment is lagged); (c) NEW — short maturation delays (g = 1-2 yr)
  RELOCATE the window into fish range on the locus r*g ~ 1.5-1.6, with
  tau-windows inside documented governance lags (2-8 yr) and decadal periods
  (~8 yr at r=0.8/g=2; ~4 yr at r=1.6/g=1): the sharpest new, falsifiable
  empirical avenue (fast-maturing small pelagics with continuous HCRs).
- DO NOT CLAIM: that "no structural extension can fix the window" in general
  (false); nor that the short-delay bands / middle band are closed (finite
  parameter resolution, no collocation classification, parameter-sensitive
  widths, cohort/institutional overlap must be discriminated).
- Status: merged into corrected_manuscript.tex (Patches A/B/C2) and
  deep_research_report.md (D5.1 correction, D7) on 2026-08-08.
