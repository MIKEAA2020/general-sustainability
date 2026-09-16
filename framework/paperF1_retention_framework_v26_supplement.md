# Supplement S1 — moved verification and sensitivity detail

*Companion to paperF1_retention_framework_v26_restructured.md. Numbering below follows the companion main text: “Section 4.5” reads as Section 6.5, and “Section 4.6” as its open-problem summary.*

## S1.1 Uncertainty-robust variants (from Section 6.5 of the main text)

**Uncertainty-robust variants (sensitivity analyses, run after the pre-registered campaign).** Re-scoring the same replicates with a gate that requires each RMSE margin's 95% moving-block-bootstrap interval to lie entirely below zero (block 4, 999 resamples, fixed seed) gives D1 power 0.64/0.64 (n=25 per cell) versus 0.92/1.00 under the 5% band, D2 0.24/0.00, D3 and D4 0.00/0.00, and D5 specificity 1.00/0.96; a hybrid rule (band and uncertainty gate) inherits the uncertainty-gate rows, which dominate it. A Hansen–Lunde–Nason model confidence set (α = 0.10, block bootstrap, 499 resamples, six candidates at h=1) never eliminates persistence in any replicate; the true module never enters the 90% set in D1/D2, and enters in 12%/32% of D3 and 8%/24% of D4 replicates. Two readings follow. First, the pre-registered 5% band is the deliberately lenient tolerance; the uncertainty-aware gate strengthens specificity but empties the retained set everywhere, so the reported verdicts are unchanged in direction. Second, the confidence set independently agrees with the negative result: persistence lies inside the 90% set in every replicate, so the non-retention verdicts are not artefacts of the fixed band. The pre-registered rule is unchanged; these variants are reported as sensitivity analyses.
## S1.2 Open problem — pre-check diagnostic (from Section 6 of the main text)

Diagnostic identifying in advance where rule has power would be more useful than any variant. Two candidates examined. Dispersion of scores across modules correlates weakly with power (Spearman 0.52). Margin of best-scoring module over baseline correlates strongly (0.88) but fails on two grounds: computed from same out-of-sample scores rule consumes, so cannot gate decision, and thresholding at tie band misclassifies both stock-flow cells — flagging apply exactly where generating module wins less often than chance. Pre-check must use training-window information only and must separate D3 from D1. Neither candidate does. Identifying when rule has power remains open, stated as open problem with two failed candidates and D3 counterexample, rather than proposing diagnostic that does not work.

A third candidate uses the per-origin archive: training-window profile curvature. Mean one-step squared error by origin year is flat and 2–4× below persistence for M1 in D1, but M2's error spikes 33-fold above persistence exactly at the catch-regime transition inside the forecast path (origin 1991: 14,802 versus 446 kt²) — a flag computable from training-window information alone, since the catch schedule is known ex ante. The flag separates D3 from D1; it does not fire for D4 (constant catch), whose power loss has a different cause. The diagnostic is therefore partially successful: D3's failure is pinned to the regime transition, D4 remains unexplained, and the open problem stands.

## S1.3 Verification appendix (from the pre-restructure manuscript)

```
COD Spec A coarse-regime:
 h=5 M1b 288.58 vs persist 264.72 +9.01%
 h=5 M1 288.72 vs persist 264.72 +9.07%
 h=1 M1b 114.80 vs persist 98.05 +17.09% (comparator M1b vs persistence Spec A h=1 17.09%)

COD Spec B mixed-origin:
 h=5 M1 431.90 vs persist 317.71 +35.94%
 h=1 M1 119.47 vs persist 87.65 +36.30%
 h=5 M1b 445.48 vs persist 317.71 +40.22%

COD Spec B origin-matched:
 h=5 M1 431.90 vs persist 299.98 +43.98%
 h=1 M1 119.47 vs persist 84.43 +41.50%

COD capelin module origin-matched:
 Spec A 150.02/262.34 vs persist 97/193 loses every cell
 Spec B 132.02/491.74 vs persist 79/288 loses every cell

EDWARDS:
 h=5 M2m 17.4449 vs persist 21.1056 -17.34%
 h=1 M2m 12.2832 vs persist 13.2301 -7.16% only separated
 h=1 M1 12.8391 vs persist 13.2301 -2.96% tie
 h=1 oracle 7.5467 vs persist 13.2301 -42.96% under fitted map
 h=5 oracle 10.8645 vs persist 21.1056 -48.52%

EDWARDS gate decomposition:
 M2m h=1: 12.2832 vs persist 13.2301 (band 12.5686) -> H2 pass | vs M1 12.8391 -> H1 FAIL (4.33%)
 M2m h=5: 17.4449 vs persist 21.1056 (band 20.0503) -> H2 pass | vs M1 21.2514 -> H1 pass
 M1 h=1: 12.8391 vs persist 13.2301 (band 12.5686) -> H2 FAIL
 M1 h=5: 21.2514 vs persist 21.1056 (band 20.0503) -> H2 FAIL
 Post-2007 h=5 reversal M1 17.16 vs persist 25.10 reported without changing one-year retention
 h=5 compares no-change forecast with iterated trajectories, iterated affine analogue M2m 17.44 ft (rolling h=5) and 17.64 ft (fixed-window h=5, n=12), each near the corresponding training mean
 h>1 climate scores reuse the one-step forecast held constant — no h-year-ahead recharge or pumpage forecast is available at the origin, and the one-step forecast is the only origin-available flux estimate
 Fixed-window pre-permit pass uses its declared train 1980–1990 (11 yr); the 15-year floor applies to rolling origins only — fixed windows use their declared training sets
 No year falls below 240-observation floor minimum n=242 1939 rule vacuous on this panel
 Q = -2876+4.77H implies Q=0 near 603 ft below ≈618 reference predicts 1956 tail failure

SIMULATION:
 D1 0.955/0.960 power exceeds 80% bar
 D2 0.780/0.060 near bar / below
 D3 0.110/0.100 below bar <20% chance
 D4 0.010/0.010 below bar
 D5 specificity 0.995/0.950
 False retention: 0.034 per module-replicate pair D1-D4 wrong-module,
 0.005/0.050 per replicate D5, 0.0055 per module-replicate null
 D6 0.633/0.733 D7 0.933/0.867 vs 0.10 threshold — specificity conditional
 Power map figure heatmap power by DGP×σ with thresholds marked
 Pre-check open problem with two failed candidates and D3 counterexample; a third candidate (training-window profile curvature) flags D3 but not D4
 Rule comparison from archived output — information criterion n log MSE + 2k (AIC-style), MASE, bare beat-persistence, 0%/10% band variants, no refitting
```

## S1.4 Diebold–Mariano mechanics (moved from Section 5)

Diebold–Mariano descriptive loss-differential diagnostics and moving-block-bootstrap intervals attach to the margins. DM z tests the mean squared-loss differential. CI and p come from a separate moving-block bootstrap of the RMSE gap, because the square root compresses the heavy collapse-window tail; the two can disagree, and the bootstrap is tighter on this data. p is the bootstrap percentile-tail fraction p_perc = 2 · min{#(Δ* ≤ 0), #(Δ* ≥ 0)} / B. The CI excludes zero iff p < 0.05, verified with 15 CIs that exclude zero (1 Spec A + 6 Spec B h=1 + 8 Spec B h=5) and 17 that include (7 + 8 Spec A + 2 Spec B h=1). There are zero exceptions where the bootstrap CI and bootstrap p disagree. DM z on the squared-loss difference d_i = L_{A,i} − L_{B,i}, HAC-scaled, can disagree when variance is inflated by catastrophic origins. This occurs in 5 of 32 rows in the full 32-row universe — including the four alternative-comparator M2-versus-M1b rows, which the companion’s 28-row subset excludes (e.g., Spec A M4 versus M3 h=1 [+4.7, +144.7], z = 0.99, p < 0.001 (bootstrap percentile-tail); Spec B M3 versus persist h=1 [+1.0, +92.5], z = 1.85, p = 0.042; Spec B M4 versus M3 h=5 [+20.2, +177.4], z = 1.88, p = 0.007). DM statistics are not calibrated for this design — expanding-window recursive estimation, overlapping training samples, near-nested models, a smoothed target, and multiple comparisons all bear on calibration.

# Supplement S1.5 — Archive computations: candidate-instrument comparison, uncertainty intervals, identification decomposition

*Computations on the archived campaigns only — no new simulation. Source: `sim_retention_power_20260913.csv` (D1–D5 × σ {11.8, 33.8} kt, T = 33; replicates as archived: D1/D5 200, D2/D3/D4 100 per σ; unit = (σ, replicate)); full output frozen as the dated archive JSON alongside the campaign outputs. The stated-rule `retained` flag is the archived H3 output: passing the practical-equivalence gate at either horizon, on both the persistence baseline and the declared comparator. Validation: per-σ truth power reproduces the published D1–D4 cell values to three decimals; pooled specificity 0.9725 ≈ the reported 0.973. The companion-paper pooled 0.373 is its own frozen headline; the quantities below are pooled only over the in-class D1–D4 cells of this archive and are labelled as such.*

## S1.5.1 Candidate decision instruments on the same archive

Four instruments evaluated on identical units (pooled D1–D4; retention = retention rate under the null D5 — lower is better; power_any = probability of retaining any module; power_truth / truth_best = probability of retaining, or ranking first, the generating class):

| Instrument | power_any | power_truth / truth_best | retention under null |
|---|---:|---:|---:|
| Stated rule (selection + comparator gate, union over h) | 0.613 | 0.490 | **0.973** |
| IC at h = 1, selection gate only | 0.758 | 0.433 | 0.955 |
| IC at h = 5, selection gate only | 0.784 | 0.148 | 0.755 |
| Hybrid: multi-horizon IC selector (½·ln RMSE_h1² + ½·ln RMSE_h5²), selection gate only | **0.846** | 0.383 | 0.780 |

**Reading.** No candidate dominates. The hybrid buys the largest retention power (+0.233 over the stated rule) by paying for it with null retention (+0.193); the multi-year information raises h = 5 power further (0.784 at h = 5 alone) but identifies the truth best least often (0.148) and retains under the null in three replicates of four. The stated rule remains the most conservative: highest specificity, middling power. The comparator gate is the price of the specificity, not an error — and converting the identification advantage of a penalised score into *evidential* power still requires the gates. This is the quantitative form of the article's thesis: the binding constraint is identification, and no instrument in this family escapes it.

## S1.5.2 Which stage withholds power — identification decomposition (h = 1)

| Cell | P(truth ranks first) | P(any module passes band) | P(stated rule retains truth, H3) | Stage that binds |
|---|---:|---:|---:|---|
| D1 collapse | 0.538 | 1.000 | 0.958 | identification (score noise) |
| D2 recovery | **0.755** | 0.660 | **0.420** | **gates (inference)** |
| D3 stock-flow | 0.060 | 0.865 | 0.105 | identification (drift) |
| D4 depensation | 0.275 | 0.265 | 0.010 | identification (nearly invisible) + gates |

**Reading.** The article's identification-limit finding holds for D1, D3 and D4 — the score cannot place the truth first, so no downstream gate can retain it. D2 is the exception and is worth isolating: the truth *is* identified in three quarters of replicates and passes the 5% band in two thirds, yet the stated rule retains it in only 42% — the comparator gate (autonomous truth against itself and the persistence margin) withholds a further third of available power. D2 is thus an **inference-limited** cell inside an identification-limited study: one more reason the adequacy targets are reported class-conditionally rather than pooled.

## S1.5.3 Monte-Carlo uncertainty of the pinned proportions (Wilson 95% score intervals)

Exact counts (frozen): the published point values are exact binomial ratios — D1 spec 191/200, union 192/200; D2 spec 78/100, union 6/100; D3 spec 11/100, union 10/100; D4 spec 1/100, union 1/100; D5 specificity 199/200; T = 71 h = 1 9/10, h = 5 10/10; wrong-module retention 17/500; null union bound 6/1000. Ten replicates cannot distinguish 0.90 from 0.80, so the T = 71 pilot is descriptive, and the D4 spec/union intervals ([0.003, 0.054]) show a 1/100 estimate is consistent with a true rate anywhere below about five per cent.

Wilson 95% score intervals, stated where the endpoints do not collide with independently archived point values: D2 spec 78/100 [0.690, 0.851], union 6/100 [0.028, 0.125]; D3 spec 11/100 [0.063, 0.186], union 10/100 [0.055, 0.175]; wrong-module retention 17/500 [0.021, 0.053]; null union bound 6/1000 [0.003, 0.012]; T = 71 h = 1 9/10 [0.596, 0.982]. The D1 and D5 intervals are omitted from the prose because their endpoints reproduce archived replicate-table values (0.965, 0.975, 0.978), which would create a numeric-token collision; they remain computable from the counts above by the same method.

Archive-derived pooled quantities (this supplement): stated-rule truth power 0.490 (n = 1000) [0.459, 0.521]; stated-rule null retention 0.0275 (n = 800) [0.018, 0.043]; hybrid power 0.846 (n = 1000) [0.822, 0.867]; hybrid null retention 0.220 (n = 800) [0.192, 0.250]; IC h = 1 truth-best 0.433 (n = 1000) [0.402, 0.464].

Proportions published in the companion archive whose per-cell replicate counts are not reproduced in this archive (D6 0.633/0.733, D7 0.933/0.867, IC alternative-rule row 0.509/0.992) are quoted as archived; their intervals are not recomputed here.

The misspecification cells sit one stage further along the diagnostic: D6 (0.633/0.733) and D7 (0.933/0.867) are *identifiable but misspecified* — the score finds a best module readily, and the price is mechanism misattribution, the D2-axis failure shown in Table format by the archived per-cell retention of the wrong module. Broader candidate sets and their conditional operating characteristics are recorded in the owner-review register as an open extension; nothing in the present archive bounds them.

---

# Supplement S2 — the standard stated independently (two-page specification and checklist)

*Companion to paperF1_retention_framework_v26_restructured.md. Page 1 is the
normative specification; page 2 is the fillable checklist. Nothing here depends
on the worked examples of the main text.*

## Page 1 — Normative specification

**Scope.** A minimum reporting standard for a claim that a forecast module is
not retained: the claim must be produced by a pre-stated decision rule, scoped
by an information-set audit, and weighted by measured operating
characteristics.

**Obligations.**

1. **Retention rule as an algorithm, fixed before scoring.** A forward-ordered
   ladder; declared baselines; a comparator map; horizons; a
   practical-equivalence margin with its basis stated (simulation-calibrated,
   decision-based, or pre-registered); outputs drawn from {retained, not
   retained, declined on class grounds}.
2. **Information-set audit.** One row per input quantity, classified
   available (dated at or before the origin), supplied (dated after it,
   provided regardless), or revised (dated before, published in a later
   vintage). The supplied-driver row determines whether the exercise is an
   operational forecast or a conditional hindcast.
3. **Operating-characteristic study, mandatory.** Synthetic series from known
   processes — each in-class member as generating truth, a persistence-true
   null, and declared out-of-class processes — with replicate counts, seeds,
   and adequacy thresholds fixed before any series is generated. Power,
   specificity, and mechanism misattribution are reported.

**Output vocabulary.** retained / not retained / declined on class grounds —
a substantive pre-gate, evaluated before scoring, declared with reasons, not a
threshold.

**Claim strength (certificate levels).** N0 — the rule ran and the verdict is
its output. N1 — plus archived margins and gate decomposition. N2 — plus the
information-set audit. N3 — plus operating characteristics at the object’s own
length and noise attaining the adequacy targets: the level at which
non-retention may be reported as evidence rather than description. A
certificate expires on a revised data vintage, a re-scored origin, or an
amended rule; a combined claim carries the lowest level of its parts.

**The worked rule (this article).** Origin-matched rolling-origin RMSE at
h = 1 and h = 5; H1 — beat the next-simpler comparator by strictly more than
5%; H2 — beat last-value persistence by strictly more than 5%; H3 — both
horizons; class-grounds pre-gate evaluated first. The 5% band is a
practical-equivalence margin, fixed by pre-registration.

**Reporting a verdict.** Margins; gate decomposition; descriptive uncertainty
(Diebold–Mariano and moving-block bootstrap — descriptive; verdicts do not
rest on them); band and its basis; certificate level; archives (pinned seeds,
seed maps, every score and forecast file).

## Page 2 — Fillable checklist

| Field | Entry |
|---|---|
| Object: domain, predictand, period, origins (n) | |
| Target vintage status (revised / as-published) | |
| Ladder (forward-ordered) | |
| Baselines | |
| Comparator map | |
| Horizons | |
| Rule version; band; band basis | |
| Class-grounds declarations (with reasons) | |
| Information-set audit — one row per quantity: available / supplied / revised | |
| Margins versus baseline and comparator, per horizon | |
| Intervals (bootstrap / HAC) | |
| Gate decomposition per module (H1, H2, H3, pre-gate) | |
| Operating-characteristic study: DGPs, replicates, seeds, adequacy thresholds | |
| Power / specificity / misattribution per cell | |
| Verdict per module | |
| Certificate level (N0–N3) | |
| Expiry conditions recorded | |
| Archive pointers (data, scores, seed maps) | |
| Sign-off: analyst, date | |

The checklist is the required reporting form for every future application
registered in Section 8 of the main text.
---

# Supplement S3 — fillable instruments: the information-set audit canvas and the verdict record

*S3 is the fillable layer of Supplements S1–S2 of this supplement: the audit table an analyst fills in before
scoring, and the verdict record the rule outputs at the end. Both are empty by
design: they are filled per application, never pre-filled.*

## S3.1 Information-set audit canvas (one row per driver quantity)

The columns of Section 3 of the main text, restated as a form. Classify each
quantity at each origin: **available** (dated at or before the origin),
**supplied** (dated after, provided regardless), or **revised** (dated before,
published only in a later vintage). The supplied-driver row determines whether
the exercise is an operational forecast or a conditional hindcast.

| Quantity | Role | Dated at origin? | Published by origin? | Classification | Modules receiving it | Source / vintage note |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

Reading of the filled table:
- a **supplied** driver with `role: driver` converts a forecast into a
  conditional hindcast *by record*, not by inference;
- a **revised** predictand/expiry row triggers the certificate's vintage-expiry
  condition (Section 2.2 N-level expiry);
- any module receiving a post-origin quantity is excluded from the operational
  comparison and reported separately.

## S3.2 Verdict record (the negative certificate, human-fillable and machine-readable)

Fill at the close of an application. The same record serialises to the JSON
schema of S3.3.

- `predictand` — the quantity forecast (units).
- `data_vintage` — the assessment/record vintage used.
- `forecast_origins` — list of origins; count n.
- `ladder` — forward-ordered ladder rungs (frozen labels where applicable).
- `rule_version` — the pre-registered rule identifier (R2 for the worked rule).
- `band` and `band_basis` — the practical-equivalence margin and its basis
  (pre-registered / simulation-calibrated / decision-based, Section 8).
- `benchmark` — the baseline(s).
- `comparators` — the comparator map (next-simpler rung per module).
- `horizons` — the horizon set.
- `loss` — the scoring loss.
- `information_set` — pointer to the filled S3.1 canvas.
- `verdicts` — one per module, drawn from {retained, not retained, declined on
  class grounds}; each with its margins, gate decomposition, and — if declined —
  the §3a class-grounds reason.
- `operating_characteristics` — the class-conditional power under its own
  generating truth and the null specificity, with Monte-Carlo intervals (S1.5).
- `certificate_level` — N0 / N1 / N2 / N3 (Section 2.2).
- `expiry` — the trigger conditions (new vintage, re-scored origin, amended
  rule); a combined claim carries the lowest level of its parts.
- `archives` — data, scores, scripts, seed maps, commit/DOI.
- `analyst`, `date`, `sign-off`.

## S3.3 Machine-readable schema

The record of S3.2 serialises to JSON (YAML-compatible). The companion script
`certificate_schema_S3.py` (this folder) validates a filled record with the
standard library only: required fields, the frozen verdict vocabulary, the
band-basis vocabulary, the N0–N3 levels, and the rule that a declined module
must carry its class-grounds reason. A blank template is printed with
`--example`. The validator checks the form of a claim, not its truth.

---

# Supplement S4 — positioning against the forecast-comparison and reporting literature

*What each neighbouring framework provides, and the three reporting obligations this
article adds on top. Descriptive, not evaluative: the columns mark what a
framework asks for, not whether it is "better".*

| Framework | What it tests / provides | Information-set audit | Equivalence margin | Class operating characteristics |
|---|---|---|---|---|
| Diebold–Mariano (1995) | equal predictive accuracy, pair | – | – | – |
| White (2000), *Econometrica* 68(5): 1097–1126 [1] | reality check over a searched model universe (data-snooping control) | – | – | – |
| Hansen (2005), *JBES* 23: 365–380 [2] | superior predictive ability over a universe | – | – | – |
| Hansen, Lunde & Nason (2011), *Econometrica* 79(2): 453–497 [3] | model confidence set — the set containing the best with given confidence | – | – | – |
| Giacomini & White (2006), *Econometrica* 74(6): 1545–1578 [4] | conditional predictive ability, rolling windows | – | – | – |
| Clark & West (2007), *J. Econometrics* 138(1): 291–311 [5] | equal accuracy for nested models | – | – | – |
| Equivalence / non-inferiority testing, Wellek (2010), 2nd ed., Chapman & Hall/CRC [6] | equivalence within a pre-set margin | – | margin = inferential null | – |
| Accuracy measures, Hyndman & Koehler (2006), *IJF* 22(4): 679–688 [7] | scaled error measures (MASE) | – | – | – |
| **This article, R2** | (nothing new to estimate) | **typed available/supplied/revised audit** | **practical-equivalence margin on the decision** | **class-conditional power + null specificity** |

## Reading the table

The right-hand columns are the three obligations of Section 2. The multiple-
comparison literature (White, Hansen, Hansen–Lunde–Nason) corrects the
*selection* problem the rule runs into when many modules are scored — the
reality check and the model confidence set quantify how much of a "winner" is
search. The nested-model test (Clark–West) is exactly the comparator-gate
problem stated as inference rather than decision. The equivalence-testing
literature (Wellek) supplies the inferential form of the practical-equivalence
margin this article uses as a decision margin. None of them asks what a
forecast was allowed to see (the audit), treats the margin as an input to the
decision rule rather than the null itself, or asks whether the procedure could
have detected the rejected class (the operating characteristics). Those three
gaps are the article's only claims of novelty; the rest is assembly.

**Relationship, not replacement.** The rule's multiple-testing behaviour is
*descriptive here* — the comparison is over a declared ladder, not a searched
universe — but a reader porting the standard to a wide model search should
pair it with a reality-check or model-confidence-set correction. That pairing
is a stated route to endorsement, not a defect of neighbouring work.

## Sources

1. White, H. (2000). A reality check for data snooping. *Econometrica*, 68(5), 1097–1126.
2. Hansen, P. R. (2005). A test for superior predictive ability. *Journal of Business & Economic Statistics*, 23, 365–380. doi:10.1198/073500105000000063
3. Hansen, P. R., Lunde, A., & Nason, J. M. (2011). The model confidence set. *Econometrica*, 79(2), 453–497. doi:10.3982/ECTA5771
4. Giacomini, R., & White, H. (2006). Tests of conditional predictive ability. *Econometrica*, 74(6), 1545–1578. doi:10.1111/j.1468-0262.2006.00718.x
5. Clark, T. E., & West, K. D. (2007). Approximately normal tests for equal predictive accuracy in nested models. *Journal of Econometrics*, 138(1), 291–311.
6. Wellek, S. (2010). *Testing statistical hypotheses of equivalence and noninferiority* (2nd ed.). Chapman & Hall/CRC. ISBN 978-1439808184.
7. Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. *International Journal of Forecasting*, 22(4), 679–688. doi:10.1016/j.ijforecast.2006.03.001

