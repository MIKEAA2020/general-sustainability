# Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17

**Reader-oriented restructuring draft (v17_reader_draft, 2026-09-17).**
Plain-prose re-expression of the frozen v16 paper
(`paperE3_edwards_forecast_ladder_v16.tex`), following the conventions of the
groundwater literature it cites (water-budget accounting as in the USGS
Edwards conceptual models; recharge-estimation reviews; plus the
forecast-scoring conventions of Hyndman & Koehler 2006). **No number changes
from v16.** Sections marked `[carried]` transplant verbatim at typesetting.

---

## Abstract (plain rewrite)

Groundwater managers watch one number: the water level in an index well. Can a
water-balance model — the bank account of an aquifer — forecast that number
better than the trivial rule "next year like this year"? We test this on 90
years of the J-17 well in the San Antonio Pool of the Edwards Aquifer
(1934–2023), using official recharge, pumping, and level records. A fixed
scoring protocol was frozen and dated before any error table was computed;
that protocol is a computational design, and we do not call it a clinical-style
pre-registration. Under it, exactly one model survives its own one-year test:
a simple autoregression, by 0.39 ft on n = 75 origins — a margin inside noise,
tied on mean absolute error, and reversed at the five-year horizon. A
physically identified water-balance model with climatological recharge and
pumpage forecasts better still at one year (−7.2%) and much better at five
(−17.3%), but under constant fluxes its equation collapses to that same
autoregression, so it adds no new structure and is declined as a rung.
Everything more ambitious — live water balance with supplied fluxes,
correlated errors, delayed information, and climate-covariate variants using
lagged rainfall or Niño-3.4 — fails at one horizon or loses to climatology at
five years. The reason is visible in the data: aquifer recharge is nearly
white noise (serial correlation 0.17), while the level's increments correlate
with recharge at 0.74. A stock-flow model is only as good as what it can know
about the flow, and this flow is, at forecast time, unknowable beyond its
average. Where the anticlimax ends: an oracle given the true future fluxes
cuts the error by 43–49% — a nowcasting bound showing what the aquifer's
physics could deliver if recharge were ever forecastable.

**Keywords:** groundwater; water balance; autoregression; recharge; forecast
evaluation; Edwards Aquifer; rolling origin.

---

## 1. Introduction (plain rewrite)

The Edwards Aquifer supplies San Antonio and sustains endangered-spring
species; drought-stage triggers hang on the J-17 level against fixed stage
thresholds. Two model philosophies compete for such forecasting: physical
accounting (track recharge in, pumpage out, and the change in storage) and
pure statistics (learn how the level series moves). Decades of USGS work on
the Edwards water budget — recharge near 94% of sources in the steady state,
springflow near 74% of sinks — shows the accounting is real. The question this
paper asks is not whether the accounting is true but whether it *predicts*:
given that recharge in any year is dominated by storm events that no annual
forecast contains, does knowing the accounting move next year's level forecast
off the naive benchmark? The test is run in the same courteous style as the
cod companion paper and the shared framework: many origins, refit each time,
score only the future, against persistence.

[carried: §2 data — J-17 series, recharge reconstruction, pumpage; §3 ladder,
six models plus oracle; §4 the frozen protocol and its three recorded
deviations]

## 2. Design and rules in plain words

As in the cod evaluation: origins from 1980 onward, training refit at each,
one- and five-year pooled RMSE, persistence benchmark; the comparator chain
and tie band enter through the shared framework rule while this paper's own
frozen rule is the one-year point rule — the difference between the two
readings is recorded, not smoothed over [carried §5.3; ledger row
CL-RULE-EDW-M1-DIFF]. Fluxes beyond the origin are unavailable in practice;
the design holds them at their training climatology, and one oracle model gets
the true values purely as a diagnostic ceiling.

## 3. Results in plain words

[carried: Tables 4–7 verbatim]

At one year: persistence 13.23 ft, autoregression 12.84 ft, water balance
(climatological) 12.28 ft. At five: persistence 21.11 ft, training mean 16.80
ft. The point rule keeps the autoregression provisionally — a coin flip,
stated as such. The stock-flow family fails not because aquifer physics is
wrong but because the informative direction of the physics is the recharge,
and recharge is near-white: persisting last year's recharge as a forecast
scores 702 against climatology's 556 (10³ acre-ft) on the recharge target
itself [carried §5.4]. Climate covariates shift the one-year score by at most
0.13 ft, inside noise, and lose badly at five years. The oracle rows
(−43% / −49%) mark the size of the prize that a genuine recharge forecast
would represent.

[carried: origin-2024 first scoring (certificate N2, M1 not retained at h=1),
band-calibration companion results, uncertainty layer]

## 4. What this licenses

Plainly: manage with the point-rule autoregression if a one-year statistical
forecast is needed at all; do not promise multi-year drought-stage skill from
structure the record cannot feed; invest instead in the one quantity shown to
pay — same-year recharge estimation (measurement/tracing/nowcasting), where
the oracle bound says the value lies. This separation of "model truth" from
"forecast skill at decision scale" is the paper's intended reading.

## References (unchanged from v16) [carried]
