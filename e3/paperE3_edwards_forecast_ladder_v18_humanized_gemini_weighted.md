# Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17

**Humanized version v18 (2026-09-17).** Merged from the Gemini and Grok
humanized rewrites after joint drift audit and adjudication (see
`audits_E1_E3/e3_audit_2026-09/E3_JOINT_EVAL_GEMINI_GROK_HUMANIZED_20260917.md`).
Prose mechanics follow the Gemini rewrite; every number is a frozen v16 or
archived-results value. Rejected material (recorded in the evaluation):
Gemini's pre-permit map parameters γ̂ = −0.0310 / δ̂ = −0.217 (archived fits
are ≈ −0.0284 / −0.254), its unarchived counterfactual outcomes (76.4; 5.2 ft;
646.8 ft), the over-precise R_1957 = 1,142.6 (archived print: 1,143), and all
ASCII figure mocks. v16 remains the frozen scientific text.

---

## Abstract

This paper asks whether the bank account of an aquifer can out-forecast a
coin flip. The account is a one-pool water-balance map: next year's water
level equals this year's, plus the year's recharge, minus pumping, through a
linear map fitted to history. The coin flip is naive persistence: "next year
equals this year." The test site is the J-17 index well of the San Antonio
Pool, Edwards Aquifer, on 90 years of official records (1934–2023), and the
scoring protocol was frozen and dated before any error table was computed —
a fixed computational protocol, not a clinical-style registration; its
three protocol elements that fall outside the frozen rule are recorded in one
place.

The answer has two honest halves. First half: exactly one model passes its
own one-year test — a plain autoregression, by 0.39 ft over persistence on
75 rolling origins. That margin has a bootstrap interval covering zero, ties
on mean absolute error, and reverses at the five-year horizon; under this
paper's frozen point rule it is a retention, recorded as provisional, and
under the framework's banded rule it would not be one — the difference is a
rule-version difference, not a data difference. Second half: a water-balance
model driven at climatological fluxes forecasts better still (one-year RMSE
12.28 ft against persistence's 13.23 ft; five-year 17.44 against 21.11), but
under constant fluxes it is the same autoregression wearing a gauge — its
equation reduces exactly — so it adds no new structure and is declined as a
ladder rung on class grounds. Everything else fails or loses to climatology:
live water balance with supplied fluxes, correlated errors, delayed
information, and the climate-covariate variants using lagged rainfall or
Niño-3.4, whose one-year edges (at most 0.13 ft) sit inside noise and whose
five-year scores run 3–6 ft worse than persistence.

The mechanism is visible in the data. Recharge is near-white across years
(serial correlation 0.17), while the level's increments track recharge
(t0.74). A stock-flow model can only be as good as what it knows about the
flow, and at forecast time the year's flow is unknowable beyond its
climatology — persisting last year's recharge scores 702 against
climatology's 556 on the recharge target itself. The oracle given the true
future fluxes cuts the pooled error by 43–49%: that is not a forecast, it is
a nowcasting bound, and it prices the one quantity worth buying — same-year
recharge estimation — rather than any model structure on this record.

**Keywords:** groundwater; water balance; autoregression; recharge; forecast
evaluation; Edwards Aquifer; rolling origin.

---

## 1. Introduction (humanized)

Drought-stage declarations in the San Antonio Pool hang on the J-17 level
crossing fixed stage thresholds, so the one-year level forecast is an
operational object, not an academic one. Two model philosophies offer to make
it: physical accounting (recharge in, pumping out, the balance moves the
level) and statistics (learn how the level moves). The accounting is real —
the aquifer's budget is dominated by recharge and spring discharge — but the
question this paper scores is narrower: does the accounting *predict* next
year's level better than persistence, when next year's recharge is not yet
observable?

*(Frozen v16 sections — data, the ladder with equations, the frozen protocol
and its recorded deviations, fixed-windows material — transplant verbatim.)*

## 2. Design, in plain words (adopting Gemini's protocol-record structure)

**Protocol record.** The scoring protocol, frozen and dated (2026-08-25)
before any RMSE table: pooled rolling RMSE is primary at one year; retention
follows this paper's point rule (Definition 4.2 of v16). Three protocol
elements sit outside the frozen rule and are recorded in one place instead
of being called "pre-registered."

**Models.** Persistence; training mean; autoregression (M1); water balance
with realised or climatological fluxes (M2; its constant-flux form M2m);
water balance with correlated errors (M3); delayed information (M4); four
climate-covariate variants; and an oracle given the true future fluxes, kept
out of the ladder as a diagnostic. Forecasts longer than one year reuse the
one-step forecast held constant — no multi-year recharge or pumpage forecast
exists at the origin; this convention is stated here, at first mention, not
buried.

## 3. Results (numbers frozen; narrative humanized)

*(Tables 3–7 transplant verbatim.)*

- **One year.** Persistence 13.23 ft; M1 12.84; M2m 12.28; M2 14.70; oracle
  7.55. The M1 point-rule retention is a 0.39-ft coin flip (interval covering
  zero; MAE tied 10.72 vs 10.73).
- **Five years.** Persistence 21.11; training mean 16.80; M2m 17.44; M1
  21.25. Only climatological structures beat persistence at this horizon, and
  the one that reduces to the retained autoregression is declined as a rung.
- **Climate.** Lagged rainfall and Niño-3.4 tilt recharge forecasts by at
  most ~10% on annual axes and move head scores by at most 0.13 ft at one
  year — inside noise — and 3–6 ft worse than persistence at five. A cleaner
  sentence than hedging: September–November 1956 is La Niña (−0.92) and does
  not announce R_1957 = 1,143 × 10³ acre-ft; the signal does not operate at
  the scale the record needs.
- **Fixed windows.** The M2 failure is a timing artifact: persisting the dry
  1956 flux (43.7 × 10³ acre-ft) rails the projection to faulting at the
  [610, 710] ft clip (RMSE 55.32 ft; recovery-window persistence 43.62).

## 4. Discussion — the timing bottleneck (adopting Gemini's framing)

Forecasting versus nowcasting is the paper's center, stated plainly: the
stock-flow family does not fail because the aquifer's physics is wrong; it
fails because the informative quantity (this year's recharge) is the one the
ladder cannot know at origin. The one-pool map with climatological fluxes is
the best one-step forecaster tested and is, at those fluxes, the
autoregression — a class reduction stated once, not re-litigated. What the
record supports buying is measurement of the current flux (nowcasting), where
the oracle bound (−43% to −49%) prices the value. The rule-version item is
stated once: this paper's frozen h=1 point rule retains M1 provisionally; the
framework's banded rule would not; a recorded rule-version difference, not a
data difference (ledger CL-RULE-EDW-M1-DIFF).

*(Comal Springs service series and pumpage-policy counterfactual sections:
content carried conceptually; any printed scenario outcomes go to W2
registration before they print — see the joint evaluation; the archived
policy-map identification Q = −2876 + 4.77H (implying zero extraction near
603 ft) is quoted from v16 unchanged.)*

## 5. Conclusions

Three sentences within their evidence classes. (1) At one year, only the
autoregression survives its frozen rule — provisionally, by a margin inside
noise — and the best physical form of it is a climatological-flux water
balance that is the same model. (2) At five years, structure without a flux
forecast loses; the failure is timing, not physics. (3) The investment the
data point to is same-year recharge measurement, not model elaboration; a
3,207-well machine-learning benchmark cited in the literature reaches the same
conclusion for groundwater forecasting in general.

## References (frozen strings from v16; verbatim)
