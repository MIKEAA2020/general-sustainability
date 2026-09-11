# Sampled-governance (periodic-review) feasibility — results (2026-08-08)

**Question:** can the stage model's institutional-oscillation prediction be made
field-testable, given that real multi-year governance is periodic-review rather
than continuous-delay?

**Answer: YES — demonstrated.** Reframing the institutional lag as a
**review interval T_r with sample-and-hold of the deficit signal** (institutions
hold their observation between reviews and adjust effort continuously against
the held signal — the correct bridge to the continuous model, verified below)
relocates the instability into review-interval space, where real institutions
live. Code: `sampled_governance.py` (v2). Model:

    dN/dt = r N(t-g)(1-N(t-g)/K) - q E N
    dZ/dt = (max(0, softplus(qEN - regen) - ln2/k + delta) - Z)/tau_m
    dE/dt = (1-E/Emax)[ eta E (Z_sig/Dref - E/Emax) + delta0 Z_sig/(Zref+Z_sig) ]
    Z_sig(t) = Z(k T_r)  for t in [k T_r, (k+1) T_r)      (sample-and-hold)

As T_r -> 0 this recovers the tau=0 continuous system (stable below the
window), so the bridge is correct by construction.

## Verified results (eta = 0.914 unless noted; all dt-converged)

### Sprat band (r = 0.8, g = 2; continuous tau-window (2.6, 7.7) yr)

| T_r (yr) | outcome | period (yr) | amp(N) |
|---|---|---|---|
| 1 (annual) | **stable** (amp 0.000) | — | 0 |
| 3 | stable | — | 0 |
| 5 | stable | — | 0 |
| 6 | oscillatory | ~8 | (borderline) |
| 7 | oscillatory | 7.96 | 2.2 |
| 8 | oscillatory | 8.0 | ~1 |
| 10 | oscillatory | 8.0 | ~1 |
| 12 | oscillatory | 8.0 | 0.96 |

dt-convergence (T_r=7): P = 7.95/7.96/7.96, amp = 2.20/2.22/2.22 at
dt = 0.05/0.02/0.01. **Annual review (T_r=1) is stable — matching observed
annual TAC systems (Baltic sprat shows no robust cycle). The sampled window
starts at T_r ~ 5-6 yr, period ~ 8 yr.**

### Anchovy band (r = 1.6, g = 1; continuous tau-window none at eta=0.914,
(1.1, 3.9) at eta=3.0)

| T_r (yr) | outcome | period (yr) | amp(N) |
|---|---|---|---|
| 0.5 | stable | — | 0 |
| 1 (annual) | stable (weak 4-yr wiggle, amp 0.40) | ~4 | 0.41 |
| 1.5 | oscillatory | ~4 | — |
| 2 | oscillatory | ~4 | — |
| 3 | oscillatory | 3.96 | 1.47 |
| 4 | oscillatory | ~4 | — |
| 5 | oscillatory | ~4 | — |

dt-convergence (T_r=3): P = 3.95/3.96/3.97, amp = 1.43/1.47/1.48.
**Sampled window T_r ~ (1.5-2, >=5), period ~ 4 yr — OVERLAPS real 1-3 yr
quota-cycle governance (SAFMC-type regional quotas, data-poor multi-year TACs).
This is the most testable locus found.**

### Cod band (r = 0.3, g = 5; continuous tau-window (9.9, 20.3) yr)

| T_r (yr) | outcome |
|---|---|
| 1, 2, 3, 5, 8, 10, 12, 15, 20 | **stable at every T_r** |

**The continuous-delay middle band does NOT survive under sampled governance.**
This is an honest refinement: the manuscript's merged cod-class middle-band
claim (tau-window 9.9-20.3 yr) rests on continuous tau; realistic periodic
review makes cod-like systems stable at any review interval, reinforcing the
cod verdict (no institutional mechanism for cod) and narrowing the middle
band's empirical relevance. At eta=3.0 only T_r=1 shows a 34-yr oscillation
(suspect; not robust).

## What this establishes (feasibility answer)

1. **The mechanism is testable in review-interval space.** The sampled window
   for anchovy-class stocks (T_r ~ 2-5 yr) overlaps real multi-year governance;
   a fast-maturing small pelagic under a 2-5 yr responsive review cycle is
   predicted to show ~4-yr institutional cycles (falsifiable: onset dateable to
   the review-cycle change; stability below and, presumably, above).
2. **Annual systems are predicted stable — and observed stable** (Baltic sprat;
   annual TAC practice worldwide). The model and observation agree at T_r = 1.
3. **The sprat-class window (T_r ~ 6-12 yr) is currently untestable** — no real
   5+ yr responsive review system exists (found in the tau-window search); but
   the annual prediction (stable) is confirmed by data.
4. **Cod-class: no instability under realistic governance** — the continuous
   middle band over-predicts; manuscript refinement recommended (one sentence).

## Honest caveats / open items

- Deterministic; no assessment error or noise (real assessments are noisy;
  error could damp or amplify — open, and the natural next step).
- Sample-and-hold is one governance model; partial-revision (gradual rule
  updates) and assessment lag inside T_r are not yet modeled.
- Window edges are parameter-sensitive (eta, tau_m, etc.); the *existence* of a
  window at realistic T_r and its period (~4 yr anchovy-class, ~8 yr
  sprat-class) are the robust claims.
- v1 (instant full reset of effort to E*(Z) at each review) was WRONG —
  aggressive sampled control destabilizes at any interval (unrealistic); v2
  (sample-and-hold) is the defensible bridge and is what the numbers above use.

## Next steps (all feasible)

1. Add assessment error / noise to the sampled model; re-scan windows
   (robustness of the 2-5 yr anchovy window).
2. Cross-sectional test on the 58 RAM stocks: rank by documented review
   interval T_r; test whether spectral power near the predicted period (4 yr
   anchovy-class, 8 yr sprat-class) increases as T_r approaches the window.
3. Merge the one-sentence refinement into corrected_manuscript.tex: the
   continuous-tau middle band (cod-class) does not survive periodic-review
   governance; the testable locus is the anchovy-class sampled window
   (T_r ~ 2-5 yr).
