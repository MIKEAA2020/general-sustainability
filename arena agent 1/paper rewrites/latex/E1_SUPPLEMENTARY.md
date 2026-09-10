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
