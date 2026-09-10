# Supplementary Information

## Forecast skill of structural models for Northern cod: a scored ladder

This supplement supports the main article. Section numbers are cited in the main text
as SI-1, SI-2, and so on. All content here is derived from the analysis code and result
files archived with this study; no result appears in this supplement that is not
reproducible from that code.

---

## SI-1 Order in which the passes were run

The main text (Section 4) states that the study is a fixed computational protocol rather
than a prospective registration, that no dated pre-scoring protocol file exists, and that
the additional passes were declared in the text as they were added. This section records
the order of execution, so that a reader can judge for themselves which choices were
fixed before scoring and which were not.

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
This is stated in the main text and is repeated here because it is the substantive
qualification on the protocol. Neither element changes any retention outcome: the tie band
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

The layer is produced by `campaign_e1_dm_uncertainty.py` (batch-7 audit directory of the
repository), deterministic under seed 0, with output archived at
`results/e1_dm_uncertainty.csv`.

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
