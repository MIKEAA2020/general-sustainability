# Pre-registered design — E1 second empirical object: RV fall survey index target (Spec C)

**Frozen 2026-09-18, before any score was computed on the survey target.** Owner directive: run the RV-survey campaign properly as a second empirical object (per the attached recommendation "Is the RV survey-index campaign merited?"): two-target paper preferred if the design holds.

## C.1 Object and series

- **Target.** The autumn research-vessel trawl survey abundance index for Northern cod (NAFO 2J3KL), Schijns et al. (2021) Table 3 citing DFO 2021b Table 2: 33 consecutive annual values, **1983–2015**, no missing years (verified at freeze). Archived fixture: `wave_e_cod/data/rv_fall_abundance_schijns_table3.csv`.
- **Unit reconciliation.** Models close the stock-flow map in kt. The index is converted to kt-equivalents by a deterministic scale factor $q^{\#} = \operatorname{median}_{1983..2015}(SSB_t / I_t)$, where $SSB$ is the registered Spec-A series. Retention verdicts are proportional margins and are therefore scale-invariant; $q^{\#}$ affects only reported absolute RMSE.
- **Scope.** The object evaluates forecast skill *on a monitoring series*, a different target from the assessment reconstruction — it reuses the frozen ladder and scoring machinery unchanged, it does not re-fit or substitute any E1 setting.

## C.2 Machinery reuse and pairing

- Models M1, M1b, M2, M3, M4 and naive baselines are executed by the registered `wave_e_cod/src/run_ladder.py` engine (imported, unmodified): one-step least-squares fits on expanding windows (min 8 year training), bounds $r\in(0.001,2.0]$, $K\in[\max_{\text{train}}+10, 5000]$ kt on the target's own units, multi-start $K=500$ kt, the frozen $\hat\phi$ rule, fewer-than-four-transitions fallback, deterministic plug-in projections, floors/ceilings (10⁻³/10⁶).
- Both Spec-A catch treatments (coarse regime; annual landings) are scored.
- **Origin pairing.** With years 1983–2015 and min_train=8, structural origins are exactly 1990–2014 at h=1 (n=25) and 1990–2010 at h=5 (n=21) — origin-for-origin identical to Spec A. Naive baselines use the engine's own rule (1983+7→1990, n=25/21), and all readings are origin-matched.
- Fixed windows (collapse train 1983–1990 → 1991–1995; recovery train 1995–2007 → 2008–2015) are scored by the same engine.
- Uncertainty layer: Diebold–Mariano, HAC lag h−1, moving-block bootstrap block h, **20,000 replications, seed 0**, deterministic (identical conventions to the registered E1/E3 layers).

## C.3 Declared departures (complete list)

1. **No normative threshold.** The survey index carries no limit reference point; secondary Brier scores are **not computed** for Spec C. Everything else follows Spec A metrics (RMSE, MAE, log-RMSE, sign-hit where defined).
2. **No survey-start variant.** Initial-state rescaling is meaningless when the index is itself the target; M2_survey_start is dropped from Spec C.
3. **No capelin-prey modules and no delay-fix variants:** Spec C scores the frozen five-module ladder plus two naive baselines only.
4. **Target timing.** The fall survey for year *t* is treated as available at origin *t*; the survey-vs-origin timing caveat (index compiled after season close) is declared here and reported in the information-set audit.

## C.4 Pre-registered hypothesis and decision consequences

- **Hypothesis (from the framework paper's simulation layer):** assessment-like smoothing injects autocorrelation that favours persistence; on the less-smoothed monitoring series the persistence advantage should shrink or invert.
- **Scorecard.** Verdicts are computed identically to Spec A (H1/H2/H3, δ = 0.05 tie band). A retention on the survey target with persistence margins outside bootstrap intervals at either horizon counts as a contrary result and is reported as such, without narrative smoothing.
- **Paper consequence (frozen choice):** regardless of outcome, the survey object becomes a numbered part of the E1 paper's Results (two-target presentation), with a target-contrast subsection; the headline claim is rewritten only if the verdict changes.

## C.5 Verification battery (defined at freeze)

1. **Engine fidelity proof.** Re-run of the same engine on the SSB Spec A series must reproduce the archived rolling values (persistence 98.05 kt / 264.72 kt; M1 120.51/288.72; M1b 114.80/288.58; M2 144.09/398.18 regime-filtered etc.) before any survey number is read.
2. **Determinism.** Two consecutive campaign executions produce byte-identical outputs.
3. **Origin-set equality.** Computed origin lists equal [1990..2014] and [1990..2010].
4. **DM replication.** The 20,000-replication layer reproduces identically on re-execution.
