# Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL

## Abstract

This paper asks a narrow question and answers it negatively: does adding
structure to a forecasting model of the Northern cod stock (NAFO Divisions
2J3KL) improve its forecasts? Five surplus-production models and two naive
baselines are compared under a scoring rule fixed before the scores were
read. Three elements of that rule condition the interpretation of the
results. (1) The benchmark is persistence: next year's spawning biomass
equals this year's. (2) Retention requires a model to beat persistence and
the next-simpler model by more than a 5% margin at both the one-year and
five-year horizons, on error pooled over rolling forecast origins. (3) Information availability at the forecast
origin is documented for every quantity each model uses. The
target series is a modern assessment reconstruction whose earlier values
embed information produced after the nominal forecast dates, and three
models receive realized catches over the forecast horizon. Both features
favour the structural models.

A scope element is relevant to the collapse years. The ladder's
one-dimensional maps cannot generate a collapse followed by recovery, so
collapse-window scores measure the misspecification penalty of a class that
cannot generate the event, rather than relative forecast skill between
persistence and structure.

On both estimated biomass series, evaluated separately throughout, no model
is retained. On the 2016-assessment series (1983–2015), pooled one-year RMSE
is 98 kt for persistence against 115–196 kt for the structural models; at
five years, 265 kt against 289–488 kt. On the extended series (1954–2024),
the origin-matched one-year figures are 84 kt for persistence against
120 kt for the best structural model; the corresponding mixed-origin
persistence figure is 88 kt, a difference attributable to the training
window. From a fixed pre-collapse origin, every model misses the 1991–1995
collapse (694–819 kt, against 670 and 688 kt for the baselines). A
prey-index module loses in every cell. The claim is scoped to this ladder,
this estimator, and this scoring design; it is not a statement about the
sustainability of the stock or about surplus production in nature.

**Keywords:** forecast evaluation; surplus-production models; northern cod;
rolling-origin; hindcasting; persistence benchmark; time series.

## 1. Introduction

Whether better models fit better is well studied; whether they forecast
better is the question that matters for advice. Two features of the cod
record make it a demanding test. First, the stock collapsed in the early
1990s and partly recovered, so a forecaster refit year by year confronts two
regimes (Hutchings & Myers 1994). Second, two independently estimated series
describe the same stock: the spawning-biomass series of the 2016 assessment
(1983–2015) and the extended 1954–2024 reconstruction. The design evaluates
both series separately and reports the informational advantages on each side
of the comparison: persistence inherits the smoothness of the
reconstruction; the structural models receive realized catches over the
forecast horizon.

## 2. Design

### 2.1 Models

The candidate set: persistence; the training mean; logistic growth with a
training-mean catch (M1); logistic growth with a low-abundance penalty
(M1b); a stock-flow model with realized catches (M2); M2 with correlated
errors (M3); and M3 started one year late (M4). The order of the ladder was
fixed before scoring.

### 2.2 Scoring rule

Pooled rolling-origin RMSE at the one-year and five-year horizons. Retention
requires both the persistence margin and the next-simpler-comparator margin
to exceed 5% at both horizons. Scores that are undefined for persistence by
construction (the 0/1 direction and Brier-type scores at the one-year
horizon on the short series) are assigned 0.00 by convention.

### 2.3 Information availability at the forecast origin

For every quantity entering each model, availability at the forecast origin
is documented. One case requires emphasis: in the collapse
window, supplying the 1992 catch reduction to a constant-productivity map
renders the run a policy-as-exogenous counterfactual, not a retention
candidate on that window.

### 2.4 Protocol timing

The scoring core was fixed before the first primary pass. The subsequent
passes — annual landings, survey start, capelin covariate, and
Specification B — were each fixed and dated before their own scoring.

## 3. Results

### 3.1 Pooled margins and regime composition

Pooling conceals regime composition. Persistence wins the quiescent bands
and loses the collapse band on five origins, a window too small to score. On
a fixed recovery window, M1b attains 90 kt against 104 kt for persistence;
this is a fixed-window structural margin that the rolling-origin protocol
does not score.

### 3.2 Decomposition of the delay experiment

At one year on the 2016-assessment series, the cost of the one-year delay is
approximately 86 kt (stale persistence 184 kt, fresh persistence 98 kt);
the further cost of the structural model under the delay is approximately
12 kt (stale M4, 196 kt; stale persistence, 184 kt). At five years on the
extended series, the model cost under the delay dominates: 1,030.7 kt for
stale M4 against 337.4 kt for stale persistence and 300.0 kt for fresh
persistence. The staleness penalty compounds through the iterated dynamics
rather than through information loss alone. Constructively, a timely
persistence forecast added more value at one year than any structure tested.

### 3.3 Uncertainty

Uncertainty statements are descriptive. No short-series margin against
persistence has an interval excluding zero; several long-series margins
against structure do.

## 4. Discussion

Simulation evidence bearing on interpretation is reported in the companion
framework paper: at collapse-window parameters the scoring rule recovers a
true autonomous module in approximately 97% of replicates and is weak
against stock-flow and depensation alternatives. Rose (2026) provides
reconstruction-level corroboration of the extended series.

## 5. Conclusions

(1) On rolling-origin RMSE for these two series, under the stated rule, no
tested structure is retained. (2) The collapse-window outcome measures a
class misspecification penalty; it is not evidence about whether structure
forecasts better in regimes the structural class can represent. (3) No
conclusion follows about the sustainability of the stock, and no tested
model is shown to be the best available. (4) The informativeness of the
negative result depends on the operating characteristics of the scoring rule
against known truths; those characteristics are measured in the companion
framework paper.
