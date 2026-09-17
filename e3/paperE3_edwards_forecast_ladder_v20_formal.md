# Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17

## Abstract

This paper tests whether a one-pool water-balance model outperforms naive
persistence in forecasting next year's water level at the J-17 index well of
the San Antonio Pool, Edwards Aquifer, on 90 years of records (1934–2023).
The water-balance candidate advances the level by the year's recharge minus
pumping through a linear map fitted to history; the benchmark is
persistence ("next year equals this year"). The scoring protocol was fixed
and dated before any error table was computed; departures from the fixed
protocol are recorded in the Methods section.

At one year, exactly one model passes its test: a first-order
autoregression, by 0.39 ft over persistence on 75 rolling origins. That
margin has a bootstrap interval covering zero, ties on mean absolute error,
and reverses at the five-year horizon; under the paper's point-retention
rule it qualifies as a provisional retention, whereas under the framework's
banded rule it would not — a difference of rule definition, not of data. A
water-balance model driven at climatological fluxes forecasts better still
(one-year RMSE 12.28 ft against 13.23 ft for persistence; five-year 17.44
ft against 21.11 ft), but at constant fluxes its equation reduces exactly
to the autoregression; it adds no distinct structure and is excluded from
the ladder on class grounds. All remaining candidates fail or lose to
climatology: live water balance with supplied fluxes, correlated errors,
delayed information, and the climate-covariate variants using lagged
rainfall or Niño-3.4, whose one-year advantages (at most 0.13 ft) lie
within noise and whose five-year scores run 3–6 ft worse than persistence.

Recharge is near-white across years (serial correlation 0.17), while
increments of the level track recharge (correlation 0.74). A stock-flow
model is therefore bounded by what is known about the flow, and at forecast
origin the year's flow is not observable beyond its climatology: persisting
last year's recharge scores 702 against 556 for climatology on the recharge
target itself. An oracle given the true future fluxes reduces pooled error
by 43–49%. The oracle is not a forecast; it is a nowcasting bound, and it
quantifies the value of measuring current recharge rather than elaborating
model structure.

**Keywords:** groundwater; water balance; autoregression; recharge; forecast
evaluation; Edwards Aquifer; rolling origin.

## 1. Introduction

Drought-stage declarations in the San Antonio Pool are triggered by the J-17
level crossing fixed thresholds, so the one-year level forecast is an
operational quantity. Two model families offer to produce it: physical
accounting (recharge raises the level, pumping lowers it) and statistical
learning (the level's dynamics are estimated directly). The aquifer's budget
is dominated by recharge and spring discharge; the question this paper
scores is narrower — whether the accounting predicts next year's level
better than persistence when next year's recharge is not yet observable.

## 2. Design

### 2.1 Protocol

The scoring protocol was fixed and dated (2026-08-25) before any RMSE table
was computed: pooled rolling-origin RMSE is primary at the one-year horizon,
and retention follows the paper's point rule. Departures from the fixed
protocol are recorded in the Methods section.

### 2.2 Models

Persistence; the training mean; a first-order autoregression (M1); water
balance with realized or climatological fluxes (M2; M2m in its
constant-flux form); water balance with correlated errors (M3); delayed
information (M4); and four climate-covariate variants. An oracle supplied
with the true future fluxes is evaluated as a diagnostic and kept out of
the ladder. For horizons beyond one year, all models reuse the one-step
forecast held constant, because no multi-year recharge or pumpage forecast
exists at the origin.

## 3. Results

### 3.1 One-year horizon

Persistence 13.23 ft; M1 12.84 ft; M2m 12.28 ft; M2 14.70 ft; oracle 7.55
ft. The M1 retention under the point rule rests on a 0.39-ft margin with a
bootstrap interval covering zero and tied mean absolute error (10.72 ft
against 10.73 ft).

### 3.2 Five-year horizon

Persistence 21.11 ft; training mean 16.80 ft; M2m 17.44 ft; M1 21.25 ft.
Only climatological structures beat persistence at this horizon, and the one
that reduces to the retained autoregression is excluded as a distinct rung.

### 3.3 Climate covariates

Lagged rainfall and Niño-3.4 tilt recharge forecasts by at most ~10% on
annual axes and move head scores by at most 0.13 ft at one year — within
noise — and by 3–6 ft worse than persistence at five years. For example,
the La Niña episode of September–November 1956 (Niño-3.4 index −0.92) is
followed by 1957 recharge of 1,143 × 10³ acre-ft; the climate signal does
not operate at the scale the recharge target requires.

### 3.4 Fixed windows

The M2 failure is a timing effect: persisting the dry 1956 flux
(43.7 × 10³ acre-ft) drives the projection into the faulted range at the
[610, 710] ft bound (RMSE 55.32 ft; recovery-window persistence 43.62 ft).

## 4. Discussion

The stock-flow family does not fail because the aquifer's physics is
misrepresented; it fails because the informative quantity — the current
year's recharge — is not observable at forecast origin. The one-pool map at
climatological fluxes is the best one-step forecaster tested, and at those
fluxes it coincides with the autoregression. The oracle bound of −43% to
−49% quantifies the value of measuring the current flux. The estimated
withdrawal identification Q = −2876 + 4.77H, implying zero extraction near
603 ft, provides the basis for counterfactual policy analysis. Under the
paper's one-year point rule M1 qualifies provisionally; under the
framework's banded rule it does not; the difference is definitional and
involves no new data.

## 5. Conclusions

(1) At one year, only the autoregression passes its stated rule, and only
provisionally, on a margin within noise; its best physical form is the
climatological-flux water-balance model, which is the same model. (2) At
five years, structure without a flux forecast loses to persistence; the
failure is one of timing rather than physics. (3) The investment the record
supports is measurement of current recharge, not model elaboration; a
3,207-well machine-learning benchmark in the broader literature reaches the
same conclusion for groundwater forecasting.
