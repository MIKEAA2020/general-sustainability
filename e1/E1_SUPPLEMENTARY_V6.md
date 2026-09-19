# Supplementary Information

## Forecast skill of structural models for Northern cod: a scored ladder

This supplement supports the main article (`paperE1_cod_forecast_ladder`, v62 series). Section numbers are cited in the main text
as SI-1, SI-2, and so on. All content here is derived from the analysis code and result
files archived with this study; no result appears in this supplement that is not
reproducible from that code.

---

## SI-1 Order in which the passes were run

The main text (Section 4) states that the study is a fixed computational protocol rather
than a prospective registration, that no dated pre-scoring protocol file exists, and that
the additional passes were declared in the text as they were added. This section records
the order of execution, documenting which choices were fixed before scoring and
which were not.

The order below is established from the analysis code and its recorded metadata, not from
recollection. Passes 1 and 2 are labelled as such in the driver script `run_ladder.py`
and are distinguished in the archived `results/meta.json` by the keys `catch_pass1` and
`catch_pass2`. Passes 3 and 4 are separate scripts that import from the pass-1/2 driver
`run_ladder.py`, which fixes their order after it: `run_xte.py` imports the model
definitions (`SPECS`) themselves, while the capelin scripts import the shared machinery
(`DATA`, `OUT`, `EPS`, `step`, `naive_baselines`) and add one further model of their own,
`M_cap_index`.

| # | Pass | Catch / data treatment | Produced by | Archived output |
|---|---|---|---|---|
| 1 | Regime catch | Regime constants 240/120/5 kt, read from the SAR prose | `run_ladder.py` (`# Pass 1 (regime C)`) | `fixed_window_scores.csv`, `rolling_summary.csv` (rows `catch = regime`) |
| 2 | Annual landings | Annual series, Schijns et al. (2021) Table 1, tonnes/1000 | `run_ladder.py` (`# Pass 2: annual catch`) | same files, rows `catch = annual` |
| 2b | Survey start | Forecast initiated at the survey state, annual catch | `run_survey_start()`, called within the pass-2 block of `run_ladder.py` | `survey_start_forecasts.csv` |
| 3 | Capelin | Continuous capelin-W ablation, observed acoustic years only | `run_capelin_index.py`, `run_capelin_regime.py` | `capelin_index_summary.csv`, `capelin_regime_summary.csv` |
| 4 | Specification B | The ladder on the xteNCAM domain alone, **not pooled** with NCAM 2016 | `run_xte.py` | `xte_rolling_summary.csv`, `xte_fixed_window_scores.csv` |

Three points follow from this order and bear on how the scores should be read.

**The five ladder models were fixed before any pass was scored.** The `SPECS` list in
`run_ladder.py` defines M1, M1b, M2, M3 and M4 once, and Specification B (pass 4) imports
that same list rather than redefining it. None of M1--M4 was altered after a score was
seen. The capelin pass is the one place where a model was added after scoring began: it
introduces `M_cap_index`, a prey-informed variant, which is reported in the main text as
its own ablation and is not part of the five-rung ladder.

**Two elements of Definition 2.4 were formalised after the Section 3 scores had been
computed:** the 5% tie band, and the comparator declarations for the non-nested rungs.
This is the substantive qualification on the protocol, stated in the main
text. Neither element changes any retention outcome: the tie band
never decides a retention result, the smallest deficit being 17%.

**Specification B was run last and was never pooled with the NCAM 2016 domain.** The
constraint is recorded in the code itself, whose module docstring reads "Wave E ladder on
Ω_xte alone. Do not pool with NCAM 2016.", and in `meta.json`, which records that the full xteNCAM SSB
table was not extracted and was not pooled. The two specifications are therefore scored
separately throughout, and no claim in the main text transfers a result from one to the
other.

---

## SI-2 Schaefer is not the \(\mathfrak s \to 0\) limit of the depensation family

**Statement.** In the family of Definition 2.1, the Schaefer law corresponds to the choice
\(a \equiv 1\). The limit \(\mathfrak s \to 0\) in the depensation branch yields
\(a(S_t) = S_t/K\), hence a cubic modification of the logistic surplus, and not the
Schaefer law.

**Proof.** Substituting \(\mathfrak s = 0\) in \(a(S_t) = (S_t - \mathfrak s)/(K - \mathfrak s)\)
gives \(a(S_t) = S_t/K\), so \(g(S_t) = r S_t (1 - S_t/K)\cdot(S_t/K)\), a cubic surplus
term. The Schaefer law requires \(a \equiv 1\), which is the separate branch in which the
depensation factor is replaced, not obtained by a limiting value of \(\mathfrak s\). ∎

The distinction matters because it fixes what M1b adds to M1: a separate branch of the
family, not a limiting case of it. Abaee (2026b) makes the same distinction.

---

## SI-3 Uncertainty layer: bandwidth grids, disagreement rows, and provenance

### Bandwidth and block-length sensitivity

The M1-against-persistence margin was recomputed over a grid of HAC truncation lags and
moving-block bootstrap block lengths, because the automatic \(h-1\) truncation and the
\(\max(h,3)\) block length are not neutral choices when origins overlap at \(h=5\), the
estimation window expands, the predictand is a smoothed reconstruction, and the sample
straddles a structural break.

| Quantity | Specification A | Specification B |
|---|---|---|
| DM \(z\), \(h=1\), lag 0 → lag 3 | 1.14 → 2.30 | 2.81 → 1.70 |
| Bootstrap \(p\), \(h=1\), block 3–9 | 0.17–0.19 | 0.036–0.049 |
| Bootstrap \(p\), \(h=5\), block 3–9 | 0.26–0.28 | 0.008–0.026 |

The DM statistic crosses the conventional 1.96 threshold within the range of defensible
bandwidths on both specifications — upward on A, downward on B — so no verdict rests on
it. The bootstrap is markedly more stable. The qualitative reading in the main text
(Specification A within noise, Specification B separating) is therefore a bootstrap
result rather than a DM result. The grid was run for the M1-against-persistence margin;
robustness across block lengths is established for that comparison and is not asserted
for every module.

### The four disagreement rows

Four of the twenty-eight rows of Table 9 have a bootstrap interval excluding zero while
\(|z| < 1.96\):

| Spec | \(h\) | Module | Comparator | DM \(z\) | 95% CI (kt) |
|---|---|---|---|---|---|
| A | 1 | M4 | M3 | 0.99 | [+4.7, +144.7] |
| B | 1 | M3 | persist | 1.85 | [+1.0, +92.5] |
| B | 5 | M1b | persist | 1.80 | [+18.2, +250.9] |
| B | 5 | M4 | M3 | 1.88 | [+20.2, +177.4] |

Both summaries are reported side by side and no verdict rests on either where they
disagree.

### Provenance

The layer is produced by `campaign_e1_dm_uncertainty.py`, deterministic under
seed 0, with output archived at `results/e1_dm_uncertainty.csv`.

---

## SI-4 Log-floor binding counts

The log-RMSE scores of Table 4 use \(\log\max(\hat S, \varepsilon_{\mathrm{log}})\) with
\(\varepsilon_{\mathrm{log}} = 10^{-3}\) kt, the trajectory code clipping the state to
\([\varepsilon_{\mathrm{log}}, 10^{6}]\) kt. The floor binds on the following counts of
origins, taken from the archived per-origin records (Specification A: the annual-landings
rolling pass of Section 3.2).

| Spec | \(h\) | origins | M1 | M1b | M2, M3, M4 |
|---|---|---|---|---|---|
| A | 1 | 25 | 15 | 17 | M3 at 3; M2 and M4 at most once per horizon |
| A | 5 | 21 | 19 | 19 | M3 at 3; M2 and M4 at most once per horizon |
| B | 1 | 59 | 22 | 24 | between 0 and 11 |
| B | 5 | 55 | 36 | 46 | between 0 and 11 |

The raw-RMSE column, not the log column, is the retention score, so these counts qualify
a reported diagnostic rather than the verdict.

---

## SI-5 Retention-rule operating characteristics: full decomposition

Design and results are archived in full as `E1_SIMULATION_RESULTS.md`, with the
pre-registration at `wave_e_cod/SPECIFICATION_v4.md` (locked before execution) and the
per-replicate output at `wave_e_cod/results/sim_retention_power.csv` (10,000 rows). This
section records the detail condensed out of Section 3.7.

### SI-5.1 Where the power is lost

H2 alone is "beats persistence by more than the 5% band at both horizons", ignoring the
comparator gate.

| DGP | truth | passes H2 alone | passes full rule | gates, absolute | gates, conditional on H2 |
|---|---|---|---|---|---|
| D1 | M1 | 0.975 | 0.975 | 0.000 | 0% removed |
| D2 | M1 | 0.420 | 0.420 | 0.000 | 0% |
| D3 | M2 | 0.328 | 0.100 | 0.228 | 69% |
| D4 | M1b | 0.180 | 0.010 | 0.170 | 94% |

The absolute cost of the comparator gates is therefore 0.17–0.23 of the shortfall on the
two cells where they bind.

Both framings hold. In absolute terms the dominant failure is H2 — the true module often
does not out-predict persistence on data it generated. Conditional on clearing H2, the
comparator requirement is a dominant further filter.

### SI-5.2 The chance baseline

With five structural modules, random assignment would place the generating module first
20% of the time.

| DGP | true module has lowest h=1 RMSE | versus chance |
|---|---|---|
| D1 (M1 true) | 0.627 (62.7%) | far better |
| D2 (M1 true) | 0.645 (64.5%) | far better |
| **D3 (M2 true)** | **0.0375** | **worse than chance** |
| D4 (M1b true) | 0.258 (25.8%) | barely better |

On D3 the stock-flow module's mean one-year error (85.7 kt) exceeds that of the residual
(77.9 kt) and Allee (79.9 kt) modules. Estimation noise actively disadvantages the correct
structure relative to its siblings at this sample size.

### SI-5.3 Alternative decision rules

Computed on the same archived replicates, no refitting.

| Decision rule | mean power | specificity |
|---|---|---|
| Retention rule as adopted (H1–H3, 5% band) | 0.376 | 0.978 |
| Without the comparator gate (H2, H3 only) | 0.476 | 0.972 |
| Persistence only, h=1, 5% band | 0.562 | 0.955 |
| Persistence only, any margin | 0.542 | 0.765 |
| Full rule, no tie band | 0.436 | 0.772 |
| Full rule, 10% band | 0.337 | 0.998 |
| MASE < 1 against the naive benchmark | 0.651 | 0.675 |
| Information criterion, `n·log MSE + 2k` | 0.509 | 0.992 |

False-retention across the four structural DGPs is 0.044 per module-replicate pair, or
0.176 falsely retained modules per replicate; under the persistence-true null the
per-module rate is 0.005.

### SI-5.4 Two failed pre-check candidates

A diagnostic that told an analyst in advance whether the rule has power on a given series
would be more valuable than any rule variant. Two were examined and neither works.

1. **Dispersion of scores across modules.** Median coefficient of variation against
   true-module power: Spearman ρ = 0.52. Too weak to license a protocol.
2. **Margin of the best-scoring module over persistence.** Spearman ρ = 0.88, Pearson
   r = 0.94 — strongly predictive, but it fails on two grounds. It is computed from the
   same out-of-sample scores the retention rule consumes, so it cannot gate the decision;
   and thresholding it at the tie band misclassifies both D3 cells, flagging "apply" where
   the generating module wins less often than chance.

Identifying when the rule has power therefore remains an open problem.

---

## SI-6 Reproducibility package

Everything in the main text and in this supplement recomputes from the registered scripts and result files archived at https://github.com/MIKEAA2020/general-sustainability. The inventory below is the complete computational surface of the cod paper; checksums (md5, first 8 hex) pin the exact file states scored at release, and every entry is deterministic — re-execution in a fresh environment regenerates the archived outputs byte for byte.

A self-contained zip (`E1_REPRODUCIBILITY_PACKAGE_v62_20260918.zip`, distributed alongside this supplement) mirrors the directory layout so that every script below runs unmodified out-of-go-tree on numpy/pandas/scipy, includes the frozen reference outputs for byte-level diffing, and ships a `verify_package.py` that re-executes the survey-target campaign and the DM layer in a scratch directory and compares md5s against the archived files.

| Script (repo path) | Role in the paper | md5 | |
|---|---|---|---|
| `wave_e_cod/src/run_ladder.py` | Passes 1 (regime catch) and 2 (annual landings); model ladder scoring; writes meta.json keys catch_pass1 / catch_pass2 | `db6b4ae6` | results fixed_window_scores.csv, rolling_summary.csv, meta.json |
| `wave_e_cod/src/run_xte.py` | Pass 3: xteNCAM extended-series scoring (imports SPECS from run_ladder.py) | `5a5229fd` | results xte_* scores |
| `wave_e_cod/src/run_capelin_index.py` | Capelin-index intervention module (scored against origin-matched persistence) | `fa648aab` | capelin index scores |
| `wave_e_cod/src/run_capelin_regime.py` | Capelin wind-era variant | `4fda8885` | capelin regime scores |
| `arena_agent_1/other documents/rerun_campaigns/campaign_e1_baselines.py` | Recomputed naive baselines, origin-matched, asserted against frozen values | `0159acd0` | verified baseline printouts |
| `arena_agent_1/other documents/rerun_campaigns/campaign_e1_m1_reconciliation.py` | M1 fit reconciliation audit | `a97aed57` | reconciliation output |
| `batch 7 (audits of agent arena 1 paper rewrites)/campaign_e1_dm_uncertainty.py` | Post-freeze DM + moving-block bootstrap layer (Spec A/B), seed 0, 20,000 replications, deterministic | `81c559b8` | results/e1_dm_uncertainty.csv |
| `batch 7 (audits of agent arena 1 paper rewrites)/campaign_e1_dm_uncertainty_regime.py` | Regime-stratified DM layer | `6ced3555` | results/e1_dm_uncertainty_regime.csv |

*Execution order.* `run_ladder.py` (Pass 1 then Pass 2) → `run_xte.py` (Pass 3) → `run_capelin_index.py` / `run_capelin_regime.py` (Pass 4) → `campaign_e1_dm_uncertainty.py` and `campaign_e1_dm_uncertainty_regime.py` (post-freeze audit layers, read-only on scores). `campaign_e1_baselines.py` and `campaign_e1_m1_reconciliation.py` are audit reruns: they reassert the frozen values, they never re-decide them.

*Dependency claim.* No script requires external credentials; the only non-redistributable raw input is the DFO assessment table itself, whose registered transcription is archived as `wave_e_cod/data/ncam_2016_table_a2.csv` and `wave_e_cod/data/xtencam_table17_ssb.csv`.

---

## SI-7 Autumn survey index as forecast target (companion to §3.8)

**Object.** The DFO autumn research-vessel trawl survey abundance index for 2J3KL cod, transcribed from Table 3 of Schijns et al. (2021), which sources the series from the Autumn DFO research-vessel survey results table: 33 consecutive annual values 1983–2015, no missing years (verified by a continuity assertion inside the campaign script). The index is converted to kt-equivalents by the deterministic, declared unit-reconciliation constant \(q^{\#}=\operatorname{median}_{1983\dots2015}(\mathrm{SSB}_t/I_t)=5.702\times10^{-4}\) kt per index unit, computed once from the full overlapping sample and never refitted per forecast origin; the resulting target spans 12.4–1,427.0 kt-equivalents. **Correction to v4 (flagged sensitivity):** margin magnitudes are *not* invariant to \(q^{\#}\) — the optimizer \(K\)-bounds \([\max_{\text{train}}+10,\,5000]\) kt track the rescaled state, so fitted paths shift slightly. What *is* invariant is every verdict: re-scoring the whole ladder (annual-landings treatment) at the interquartile bounds of \(\mathrm{SSB}_t/I_t\) (\(q\) = p25/p50/p75) leaves all H1/H2/H3 verdicts and the empty retained set identical. Sensitivity table (closest-structural margin vs persistence, % of RMSE):

| q level | h = 1: closest deficit | h = 5: closest deficit | Any model retained? |
| :--- | :---: | :---: | :---: |
| p25 | +22.6% | +27.8% | No |
| p50 (= 5.702×10⁻⁴) | +29.8% | +42.7% | No |
| p75 | +32.8% | +46.8% | No |

Script `campaign_e1_survey_qsensitivity.py`; output archived as `results/e1_survey_qsensitivity.csv` in the reproducibility package.

**Pre-registration.** The design was frozen before any score was read (`SPEC_E1_SURVEY_TARGET_20260918.md`): object, origin sets, uncertainty-layer conventions (DM with Newey–West HAC lag h−1, moving-block bootstrap block max(h,3), 20,000 replications, seed 0), declared departures (no Brier score — the index carries no normative threshold; no survey-start variant; no capelin modules, which are not part of the frozen ladder), and a pre-registered hypothesis (smoother-injected autocorrelation favours persistence, predicting a shrunken or inverted persistence advantage on a noisier target).

**Machinery reuse and fidelity proof.** The campaign imports `run_ladder.py` unmodified and executes its rolling engine on the survey target for both catch treatments. Before any survey number is written, the engine is re-run on the Spec A series and must reproduce the frozen values (naive persistence 98.05 kt at h = 1; stock-flow regime-catch 144.09 kt at h = 1); assertions enforce this. Two consecutive campaign executions produce byte-identical output files. Computed origin lists equal [1990..2014] (h = 1, n = 25) and [1990..2010] (h = 5, n = 21) — origin-for-origin identical to Spec A.

**Artifacts (archived in the reproducibility package).** `results/e1_survey_target_rolling_forecasts.csv` (per-origin folds, both treatments), `results/e1_survey_target_rolling_summary.csv`, `results/e1_survey_target_fixed_window_scores.csv`, `results/e1_survey_dm_uncertainty.csv` (gap, DM z, bootstrap CI and p), plus the campaign script `campaign_e1_survey_target.py`.

**Full survey-target table (annual-catch treatment; kt-equivalents).**

| Model | h = 1 RMSE | h = 5 RMSE | h = 1 MAE | h = 5 MAE |
| :--- | ---: | ---: | ---: | ---: |
| naive persist | **120.5** | **249.2** | 52.9 | 118.6 |
| naive train mean | 482.4 | 553.0 | 429.9 | 490.2 |
| M1_autonomous_Schaefer | 184.2 | 386.6 | 90.4 | 188.2 |
| M1b_autonomous_Allee | 156.3 | 355.5 | 92.2 | 176.9 |
| M2_stockflow_regimeC | 224.9 | 671.4 | 98.4 | 562.8 |
| M3_AR_residual | 290.3 | 716.7 | 129.5 | 608.6 |
| M4_delayed_info | 371.3 | 880.5 | 203.0 | 803.1 |

Under the coarse-regime catch treatment the ladder spans 156.7–357.1 kt-equivalents at h = 1 and 355.5–913.5 at h = 5 against the same origin-matched persistence baselines (120.5/249.2). Uncertainty layer: every structural deficit vs persistence separates from zero at both horizons except the stock-flow module at h = 1 (annual treatment gap +36,090 kt², 95% CI [−78, +80,933], p = 0.0615; the sign is a deficit either way). Fixed windows: collapse (train 1983–1990, score 1991–1995) structural RMSE 1,102–1,274 vs 791.6 persist / 863.8 mean; recovery (train 1995–2007, score 2008–2015) structural RMSE 41.9–120.1 annual / 33.1–93.2 regime (the upper end is the Allee module, which misses persistence's 109.4 under the annual treatment but beats it under the coarse regime), vs 109.4 persist / 243.1 mean — both windows mirror the reconstruction's ordering (§3.8).

**Information-set declaration.** The survey value for year \(t\) is assigned as available at origin \(t\). The index is compiled after season close; the residual timing conservatism (an analyst scoring in January of year \(t+1\) may not yet hold the released table) is declared in the frozen design and is immaterial to the verdicts, which lose to persistence by large margins, not by timing shifts.
