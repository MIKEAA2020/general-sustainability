# Does a dependency-closed viability ladder improve forecasts? A scored test on Northern cod (NAFO 2J3KL)

**Wave E empirical paper — working manuscript**  
**Series lock:** NCAM M-shift SSB, DFO SAR 2016/026 Table A2 (1983–2015)  
**Status:** two scored specifications (\(\Omega_{2016}\), \(\Omega_{\mathrm{xte}}\)). Complexity is *not* earned on either.

---

## Abstract

The general theory of sustainability states that extra structure—stocks and flows, disturbances, delays, implementable control, observation—is justified only if it improves early warning, out-of-sample prediction, or intervention selection. This paper runs that test (Wave E) on an R04-admitted fisheries object: Northern cod in NAFO 2J3KL.

The observation is the NCAM M-shift spawning-stock biomass (SSB) series of DFO (2016, Table A2). The 2016 limit reference point (LRP) is the 1983–1989 mean SSB, 884.6 kt **[N]**. Four nested models plus two naive baselines issue fixed-window and rolling-origin forecasts. Catch enters first as a coarse SAR regime (240 / 120 / 5 kt) and then as Schijns et al. (2021) year-by-year landings. NCAM \(F\) and \(M\) are not drivers—using them would reconstruct the assessment, not forecast a stock.

**Result.** No structural model beats persistence on the primary score. One-year rolling RMSE is 98 kt for last-value persistence versus 115–206 kt for the surplus-production ladder. Replacing the catch regime with Schijns year-by-year landings does not change the ranking (M2 annual RMSE 160). Five-year RMSE is 265 kt versus 289–488 kt. The collapse window (train 1983–1990, test 1991–1995) is missed by every model (RMSE 694–819 kt): a constant-productivity surplus model with a 1992 catch drop cannot produce the observed crash. Adding an AR residual and an assessment delay does not repair it; delay **raises** error. On the recovery window the autonomous Allee fit has the lowest structural RMSE (90 kt) but is unidentified (\(s\to 0\), \(K\) pinned) and still does not beat a simple reading of the rising series.

The theory therefore earns a **negative certificate** on this \(\Omega\), not a forecast gain: (i) the exact autonomous scalar class is incompatible with the path (A014); (ii) catch-regime stock-flow is not sufficient for collapse; (iii) extra modules that are not identified on the training window increase error. The same retention rule holds on a second, unpooled specification (\(\Omega_{\mathrm{xte}}\), 1954–2024, LRP = 276 kt): persist 1-year RMSE 88 vs M1 120. The series are not mixed.

**Keywords:** viability; forecast ladder; Northern cod; model ablation; persistence baseline; Wave E

---

## 1. Why this paper exists

Section 15 of the general theory requires a comparative model ladder:

1. output-only  
2. stock-and-flow  
3. disturbance / residual  
4. delay, implementable control, observation  

Complexity is kept only if it improves a preregistered score. Wave E of the closure review is that empirical gate. R04 admits the A001 fisheries resource–sink module fully and admits A014 at corrected scalar-autonomous status. Groundwater (A005) and phosphorus (A004) remain **conditionally** admissible (blocking lists V-A005-04…, V-A004-03…). They are not used.

This paper does **not** estimate an Allee threshold, identify the cause of collapse, or evaluate whether the 1992 moratorium was adequate (A014-L4, L5, L6). It asks one scored question:

> On this locked series, do M2–M4 reduce forecast error relative to M1 and relative to naive persistence?

---

## 2. Specification \(\Omega\) **[D]**

| Field | Contents | Type |
|---|---|---|
| \(S\) | Northern cod, NAFO 2J3KL, as represented by NCAM M-shift SSB | D |
| \(I\) | Continuity of a spawning stock that can occupy the 2016 PA “cautious/healthy” side of the 2016 LRP | N |
| \(B\) | Stock area in DFO (2016) Fig. 1; 1983–2015 calendar years | D |
| \(K^*\) | \(S_t \ge \mathrm{LRP} = 884.6\) kt (1983–1989 mean of Table A2) | N |
| \(W\) | Unspecified productivity shocks; not a fitted \(M(t)\) | M |
| \(U_{\mathrm{theoretical}}\) | Any \(C_t\ge 0\) | M |
| \(U_{\mathrm{implementable}}\) | Pre-1992 directed fishery; post-2 July 1992 moratorium / low inshore removals | E |
| \(T\) | Hindcast 1983–2015; two fixed test windows plus rolling origin | D |
| \(\mathcal D\) | Food-web (capelin) **excluded** from this pass | M |
| \(\mathcal N\) | 2010/2016 DFO PA LRP (1980s mean SSB), not the 2023 40% \(B_{\mathrm{MSY}}\) LRP | N |

**Non-pooling rule.** Regular et al. (2025) / DFO (2024) xteNCAM extends the model to 1954, revises the LRP downward by about 40%, and estimates 2024 SSB at 342 kt (1.2× the new LRP). That is a different \(\Omega\). Mixing the two SSB columns is a rejected mapping (R04 necessity: safe-set and dynamics correspondence both fail).

**Observation vs driver.** Table A2 also reports \(F\) and \(M\). They are joint outputs with SSB. They are stored and not used as exogenous inputs.

---

## 3. Models

Discrete surplus, \(S\) in kt, \(C\) in kt yr\(^{-1}\):

\[
S_{t+1}=\bigl[S_t+rS_t\bigl(1-S_t/K\bigr)\tfrac{S_t-\mathfrak s}{K-\mathfrak s}-C_t+\varepsilon_t\bigr]_+
\]

with \(\mathfrak s=0\) unless an Allee term is on. **[M]**

| ID | Ladder rung | What is free on the training window | What is frozen into the test window |
|---|---|---|---|
| Naive-P | baseline | nothing | \( \hat S_{t+h}=S_t \) |
| Naive-μ | baseline | train mean | \( \hat S_{t+h}=\bar S_{\mathrm{train}} \) |
| M1 | output / autonomous | \(r,K,C\) constant | same \(C\) |
| M1b | autonomous + Allee | \(r,K,\mathfrak s,C\) | same |
| M2 | stock-flow | \(r,K\); \(C_t\) is the regime series | regime \(C_t\) |
| M3 | disturbance | M2 + AR(1) residual \(\varepsilon_t=\phi\varepsilon_{t-1}\) | \(\phi\) persisted |
| M4 | delay / information | M3 | forecast starts from \(S_{t-\tau}\), \(\tau=1\) yr |

**Catch regime [E, approximate].** From DFO (2016) prose, not STATLANT:

\[
C_t=\begin{cases}
240 & t\le 1991\\
120 & t=1992\\
5 & t\ge 1993.
\end{cases}
\]

Sensitivity of this coarseness is a limitation, not a hidden degree of freedom.

Parameters are fit by one-step least squares on the training window only (`src/run_ladder.py`). Bounds: \(r\in(0.001,2]\), \(K\) above training max.

---

## 4. Scores (frozen)

**Fixed windows**

- Collapse: train 1983–1990, test 1991–1995.  
- Recovery: train 1995–2007, test 2008–2015.

**Rolling origin:** minimum 8 training years; horizons \(h=1\) and \(h=5\).

**Primary score:** RMSE on SSB (kt).  
**Secondary:** MAE; RMSE on \(\log S\); Brier score for the hard forecast \(\mathbf{1}\{\hat S<\mathrm{LRP}\}\); sign-hit rate of \(\Delta S\) on fixed windows.

A module is **retained** only if it reduces primary RMSE relative to the next-simpler model **and** relative to Naive-P. **[D]**

---

## 5. Results

### 5.1 Locked series

![Figure 1](fig1_series.png)

**Figure 1.** NCAM M-shift SSB (DFO 2016, Table A2). Dashed line: 2016 LRP \(=884.6\) kt. 2015 SSB is 33.8% of that LRP, matching the SAR statement of 34%.

### 5.2 Fixed windows

![Figure 2](fig2_windows.png)

**Figure 2.** Multi-step forecasts from the end of each training window. Collapse is missed by every model. Recovery is under-predicted once an AR residual fitted on a slow early-recovery train is persisted.

**Table 1.** Fixed-window scores (RMSE in kt).

| Window | Model | RMSE | MAE | log-RMSE | Brier | Direction |
|---|---|---:|---:|---:|---:|---:|
| Collapse | M1 | 694 | 638 | 2.73 | 1.00 | 0.50 |
| | M1b | 694 | 636 | 2.73 | 0.80 | 0.00 |
| | M2 | 819 | 751 | 2.85 | 1.00 | 0.25 |
| | M3 | 819 | 751 | 2.85 | 1.00 | 0.25 |
| | M4 | 819 | 750 | 2.85 | 1.00 | 0.25 |
| Recovery | M1 = M2 | 120 | 105 | 0.61 | 0.00 | 0.57 |
| | M1b | **90** | 55 | 0.52 | 0.00 | 0.57 |
| | M3 | 220 | 200 | 0.92 | 0.00 | 0.57 |
| | M4 | 214 | 195 | 0.91 | 0.00 | 0.57 |

On collapse, fitted \(r\) saturates at the upper bound (\(\approx 2\)). The 1983–1990 window is a high, weakly trending stock: surplus production cannot see the 1992–94 mortality pulse, and dropping \(C\) from 240 to 5 **raises** forecast SSB, which is the wrong sign. M2 is therefore *worse* than M1 on collapse. That is a result, not a bug: if the crash were a catch-regime event in this accounting, M2 would win. It does not.

On recovery, M1 and M2 coincide because \(C_t\equiv 5\) on both train and test. M1b reports a lower RMSE but \(\mathfrak s\to 0\) and \(K\) collapses to the training range—an unidentified Allee, not a biological threshold (A014 Proposition 2, conditional form). M3’s \(\phi=0.95\) persists a negative residual and **hurts**.

### 5.3 Rolling origin

![Figure 3](fig3_rmse.png)

**Figure 3.** Rolling-origin RMSE. Persistence is the best 1-year and 5-year point forecast.

**Table 2.** Rolling-origin summary.

| Model | \(h=1\) RMSE | \(h=1\) MAE | \(h=1\) log-RMSE | \(h=5\) RMSE |
|---|---:|---:|---:|---:|
| **Naive persist** | **98** | **48** | **0.52** | **265** |
| M1 Schaefer | 121 | 80 | 8.02 | 289 |
| M1b Allee | 115 | 80 | 8.70 | 289 |
| M2 regime \(C\) | 144 | 61 | 0.59 | 398 |
| M3 AR | 135 | 53 | 3.39 | 366 |
| M4 delayed | 196 | 82 | 0.76 | 488 |
| Naive train-mean | 424 | 375 | 2.35 | 507 |

M1/M1b log-RMSE explodes because some origins produce trajectories that hit the numerical floor. M2 stabilizes the log score (catch keeps the state off zero) but loses on raw RMSE. M4, which is the only model that respects an assessment delay, is the **worst** structural model on raw RMSE. That is the information cost of \(\tau=1\), not a coding error.

**Retention decision.** No module M2–M4 is retained as a forecast improvement on this \(\Omega\). Naive-P is the scoring winner. **[E]**

---

## 6. What the ladder did prove

These are certificates, not forecasts.

1. **A014 phase-line (reconfirmed).** The observed path is non-monotone. An exact fixed autonomous scalar trajectory cannot do that. M1’s collapse failure is the finite-sample face of that theorem.

2. **Catch-regime insufficiency [E].** Under the SAR catch story, lowering \(C\) in 1992 cannot generate the crash. Collapse on this \(\Omega\) is a productivity / unobserved-mortality / observation event, not a surplus-production response to the declared catch drop. That is compatible with DFO’s own caution that NCAM \(M\) can absorb unreported deaths (A014-L4).

3. **Unidentified extra structure increases error [E].** AR residuals fitted on short, regime-changing windows persist the wrong sign. An Allee parameter goes to the boundary. Delay removes information. This is R03’s “descriptive unless the certificate hypotheses hold”: M3–M4 are not inner certificates here.

4. **LRP slack cannot lead the 1980s crash [L given N].** The 2016 LRP *is* the 1980s mean. Slack to that bound is near zero by construction throughout the training window that precedes collapse. A leading-indicator claim that uses this \(K^*\) is circular for 1983–1990.

5. **Implementable \(U\) is visible, not scored.** The moratorium is a hard change in \(U_{\mathrm{implementable}}\). It is already in the catch regime. Making it a separate M4 switch does not add a degree of freedom beyond M2. H8 (empty kernel under current architecture) is a **viability** statement about 1992, not a 1-year RMSE statement.

---

## 7. Limitations (typed)

- **[E]** Year-by-year landings are now locked (Schijns = DFO Table 1 on 1983–1993). They still cannot create the 1992–94 pulse. Recreational catch remains incompletely measured.
- **[M]** One-dimensional surplus is not NCAM. Age structure, migration, and survey catchability are omitted. The test is whether *this ladder* earns its keep, not whether DFO’s assessment is a good filter.
- **[M]** Observation error is not a full state-space likelihood. M4 is a delay, not a Kalman filter (R02 conservative-filter theorem is not instantiated).
- **[N]** \(K^*\) is the 2016 LRP. Repeating the ladder under the 2023 40% \(B_{\mathrm{MSY}}\) LRP requires the xteNCAM series and a new admission row.
- **[E]** \(n=33\) years, two short test windows. Rolling \(n=25\) (\(h=1\)) and \(21\) (\(h=5\)) is enough to rank models, not enough to certify a small skill difference.
- This pass was executed after the windows and scores were written into `run_ladder.py`. It is a computational protocol, not a locked clinical-style preregistration.

---

## 8. Relation to the programme

**Wave E support rule.** No gate is treated as closed for Wave E without
spec matching and independent verification. This manuscript’s scores are
a computational protocol on a locked \(\Omega\). They do not confirm
unmatched session IDs (E5, E7, B10, interval Hopf, TCS-1.1-as-frozen).
See `https://github.com/MIKEAA2020/general-sustainability` (`PROOF_MANIFEST.md`, “Reproducibility status” — the
consolidated disclosure content) and
`batch 2/04_open_problems/D_TIER_EMPIRICAL_AGENDA.md`.
E5_NUMBERS.json is a linear \((S,K)\) template, not this SSB series.

| Programme object | Role here |
|---|---|
| General theory §15, Wave E | The test that was run |
| R04 | Case selection: fisheries admitted; A004/A005 not used |
| A014 | Phase-line obstruction; defect list respected |
| R03 | Extra modules stay descriptive without a certificate |
| R02 | Closed-loop filter **not** fitted; listed as the next typed addition |
| A012 | Delay is instantiated only as \(\tau=1\) information delay, not as an RFDE |
| A016 | Community margins not used (unarchived CSD extract) |
| xteNCAM 1954–2024 | Scored alone in §13; not pooled |

The honest reading of “incorporate all the pieces for accurate forecasts” on this case: **the pieces that are not identified do not go in.** Persistence plus a typed impossibility certificate is the present forecast.

---

## 9. What to do next (still Wave E, not a new vision)

1. ~~Year-by-year landings.~~ Done (Pass 2–3). Identity with DFO Table 1 on 1983–1993.  
2. ~~Digitise Table 17 and score \(\Omega_{\mathrm{xte}}\) alone.~~ Done (Pass 4). Same retention outcome.  
3. ~~Observed capelin acoustic column.~~ Done (Pass 6). Not retained.  
4. Groundwater / phosphorus only after R04 blocking lists close **and** a basin series exists.

---

## 10. Conclusion

Wave E, run as specified, does not award the general theory a forecast win on Northern cod 1983–2015. Persistence is more accurate than surplus production, catch-regime stock-flow, AR residuals, and delayed information. The crash is not a catch-drop event in this accounting. Extra modules that fail identification increase error.

That is not a failure of the research programme. It is the programme’s own retention rule. The next article is a better series or a closed blocking list, not another aggregator, not an extinction theorem, and not a kitchen-sink planetary ODE.

---

## Data and code

```
wave_e_cod/
  data/SOURCES.md
  data/ncam_2016_table_a2.csv
  src/run_ladder.py
  src/make_figures.py
  results/fixed_window_scores.csv
  results/rolling_summary.csv
  results/rolling_forecasts.csv
  results/meta.json
  manuscript/fig1_series.{png,svg}
  manuscript/fig2_windows.{png,svg}
  manuscript/fig3_rmse.{png,svg}
```

Reproduce: `python3 src/run_ladder.py && python3 src/make_figures.py`

---

## 11. Pass 2 — annual catch and survey start

Pass 1 used a three-level catch regime. Pass 2 replaces it with Schijns et al. (2021) Table 1, year by year, and adds one information ablation: start the surplus step from \(\hat q \times I_t\) where \(I_t\) is the fall RV abundance index and \(\hat q\) is the training-window median of \(\mathrm{SSB}/I\). The RV index is an NCAM *input*. This is not an independent stock; it is a delayed/noisy start state.

xteNCAM SSB is still **not** in the file. Regular et al. (2025) give 2024 SSB = 342 kt under a different LRP. That remains a separate \(\Omega\).

### 11.1 Annual catch does not rescue M2

2015 Schijns catch = 4.436 kt, matching DFO reported landings. Pre-collapse catches are 172–269 kt, not a flat 240. The 1992 drop is to 41 kt, then 11 kt, then ~0.4–1.3 kt — sharper than the regime series.

**Table 3.** Rolling-origin RMSE, annual catch (kt SSB).

| Model | \(h=1\) | \(h=5\) |
|---|---:|---:|
| Naive persist | **98** | **265** |
| M1 | 121 | 289 |
| M1b | 115 | 289 |
| M2 annual catch | 160 | 394 |
| M3 | 154 | 352 |
| M4 delayed | 206 | 486 |
| M2 survey start | 128 | 331 |

Annual landings make M2 **worse** than the coarse regime on 1-year RMSE (160 vs 144). Collapse-window RMSE stays ~821 kt. A more accurate \(C_t\) cannot produce the 1992–94 crash in a constant-\(r\) surplus model, because the observed \(\Delta S\) is far larger than \(C_t\). Apparent net production \(S_{t+1}-S_t+C_t\) is strongly negative in 1991–93 even after subtracting the reconstructed catch.

**Retention:** M2 still not retained. The pass-1 conclusion is robust to the catch lock.

### 11.2 Survey start (R02-lite)

Starting from \(\hat q I_t\) instead of SSB:

- 1-year RMSE 128 kt — better than M2/M4, still worse than persist (98).
- 1-year log-RMSE 0.49 — **slightly better** than persist (0.52).
- 5-year RMSE 331 vs persist 265.

On the **primary** score (RMSE of SSB) the module is not retained. The log-score hint is recorded, not promoted. A full R02 conservative filter (set-valued compatible states, all-branches implementation) is not instantiated: there is no independent observation fibre that is outside NCAM.

### 11.3 What pass 2 changes in the argument

Nothing about the retention rule. One thing about mechanism: the crash remains a productivity / unallocated-mortality / observation event after the best public catch reconstruction we could lock. That tightens A014-L4 rather than relaxing it.

---

## 12. Pass 3 — official landings identity and xteNCAM specification (not a second ladder)

### 12.1 Schijns = DFO Table 1 on the forecast window

Regular et al. (2025) Table 1 2J3KL totals for 1983–1993 match Schijns et al. (2021) **exactly** (11 years, max |diff| = 0 t). See `results/catch_overlap_audit.csv`.

The STATLANT-versus-Schijns sensitivity is closed for the collapse window: they are the same column. A 1956 discrepancy (DFO 236,210 t vs Schijns 263,210 t) sits outside 1983–2015 and is unused. Pass 2 does not need a third catch file.

### 12.2 xteNCAM is a different \(\Omega\)

Table 17 is now extracted (`data/xtencam_table17_ssb.csv`). Earlier locked prose points remain as checkpoints. The specification card:

| Year | Quantity | Value | 95% CI | Role |
|---|---|---:|---|---|
| 2005 | SSB | 26 kt | 22–31 | checkpoint vs NCAM 2016: 25.18 kt |
| 2017 | SSB | 451 kt | 381–534 | stall begins |
| 2021 | SSB | ~400 kt | — | NCAM and xteNCAM said to agree |
| 2024 | SSB | 342 kt | 246–475 | 1.2 × new LRP |
| — | LRP | 276 kt | 180–423 | 40% \(B_{\mathrm{MSY}}\) **[N]** |

\(\Omega_{\mathrm{xte}}\) differs from \(\Omega_{\mathrm{2016}}\) in four typed fields:

1. **Dynamics [M]:** xteNCAM vs NCAM M-shift; start year 1954 vs 1983; capelin/cod ratio as a predictor of \(M\).
2. **Safe set [N]:** \(K^*=276\) kt vs \(884.6\) kt. The same late-period biomass is 34% of the old LRP and above the new one after 2016.
3. **Catch [E]:** estimated inside bounds, not treated as known \(C_t\).
4. **Horizon [D]:** 1954–2024 vs 1983–2015.

R04 necessity: if the safe-set map or the dynamics map fails, judgment transfer is forbidden. Both fail. **No kernel, no RMSE, no pooling.**

The 2005 checkpoint (26 vs 25.18 kt) shows the two assessments can agree on a low year without sharing an LRP. That is not a licence to splice columns.

### 12.3 What the prose adds to the Wave E argument

Regular et al. assign the 1992–94 disappearance primarily to \(M\) (peak \(\approx 2.5\)), informed by tagging and a capelin/cod predictor, and they state that some of that \(M\) *could* still be unreported \(F\). That is the same split obtained from the surplus residual after subtracting official \(C_t\): constant-\(r\) stock-flow cannot produce the crash.

Capelin is a candidate disturbance class \(W\), not a parameter we fitted. Instantiating it needs the capelin acoustic index and the xteNCAM SSB column. Both remain outside the lock.

### 12.4 Executed in §13

`src/run_xte.py` scores \(\Omega_{\mathrm{xte}}\) alone. No mixed rows.

---

## 13. Pass 4 — \(\Omega_{\mathrm{xte}}\) scored alone

Tables 17 and 1 were extracted from the official PDF (Regular et al. 2025). Checkpoints match the prose: 2005 SSB = 26, 2017 = 451, 2024 = 342, 2024/LRP = 1.24. The series is 1954–2024. Catch is Table 1 landings (2024 persist-2023). **No row is taken from NCAM 2016.**

![Figure 4](fig4_xtencam.png)

**Figure 4.** Two specifications. Overlap 1983–2015 RMSE = 126 kt (2015: NCAM 299 vs xte 273). Different \(K^*\). Not pooled.

**Table 4.** Rolling-origin RMSE on \(\Omega_{\mathrm{xte}}\) (kt).

| Model | \(h=1\) | \(h=5\) |
|---|---:|---:|
| Naive persist | **88** | **318** |
| M1 | 120 | 432 |
| M1b | 152 | 446 |
| M2 landings | 166 | 1059 |
| M3 | 127 | 930 |
| M4 delayed | 206 | 1031 |
| Naive train-mean | 449 | 506 |

Collapse window (train 1954–89, test 1990–95): M1 RMSE 817; M2 1898. Again, feeding official landings **worsens** the crash forecast.

**Retention on \(\Omega_{\mathrm{xte}}\):** none. Persistence wins. The longer series and the new LRP do not earn the extra modules.

That is the second independent negative certificate. Same rule, different \(\Omega\).

---

## 14. Pass 5 — capelin as \(W\), without digitizing a figure

Murphy et al. (2025) / DFO (2024/050) state a 1991 acoustic collapse (1985–90 median 3704 kt vs 1991–2022 median 174 kt). The year-by-year index is Figure 15, not a table. It was **not** digitized.

**M_cap** is a two-regime \(r\) with break 1991. Forecasts issued before 1991 use \(r_{\mathrm{hi}}\) only (no peeking). After 1991 the low-capelin regime is treated as observed.

**Table 5.** Rolling RMSE vs persist.

| \(\Omega\) | Model | \(h=1\) | \(h=5\) |
|---|---|---:|---:|
| 2016 | Persist | **98** | **265** |
| 2016 | M_cap | 154 | 334 |
| xte | Persist | **88** | **318** |
| xte | M_cap | 147 | 894 |

Post-break origins only (xte, \(h=1\)): M_cap 107 vs persist 88. Still not retained.

A published step in prey does not earn a surplus-production module on these scores.

---

## 15. Pass 6 — observed acoustic column (no interpolation)

The year-by-year 3L spring acoustic biomass is tabulated in Zenodo 17515115 (NAFC / Steele et al. 2025), plus 2023 = 331.3 kt from Murphy et al. (2025). Missing survey years are **not** GP-filled. \(I_{\mathrm{known}}(t)\) is last observation at or before \(t\), and pre-1991 values are not carried across the collapse. Forecasts persist \(I_{\mathrm{known}}(\mathrm{origin})\) only.

\[
g_t=rS_t\bigl(1-S_t/K\bigr)\bigl(I_{\mathrm{known}}/I_{\mathrm{ref}}\bigr)^{b}
\]

**Table 6.** Rolling RMSE, observed-\(I\) module.

| \(\Omega\) | Model | \(h=1\) | \(h=5\) |
|---|---|---:|---:|
| 2016 | Persist | **98** | 265 |
| 2016 | M_cap_index | 150 | 262 |
| xte | Persist | **88** | **318** |
| xte | M_cap_index | 132 | 492 |

On \(\Omega_{2016}\), five-year RMSE is a near-tie (262 vs 265). One-year RMSE is worse. Not retained.

The continuous prey index, used causally, still does not earn the module on the primary score.

---

## References

Cadigan, N. G. 2016. A state-space stock assessment model for Northern cod, including underreported catches and variable natural mortality rates. *Canadian Journal of Fisheries and Aquatic Sciences*.

DFO. 2009. A fishery decision-making framework incorporating the Precautionary Approach.

DFO. 2010. Proceedings of the Newfoundland and Labrador Regional Atlantic Cod Framework Meeting. CSAS Proceedings 2010/053.

DFO. 2016. Stock Assessment of Northern Cod (NAFO Divs. 2J3KL) in 2016. CSAS SAR 2016/026.

DFO. 2024. NAFO Divisions 2J3KL Northern Cod stock assessment to 2024. CSAS SAR 2024/049.

Regular, P. M., et al. 2025. Assessment of the Northern Cod stock in NAFO Divisions 2J3KL in 2024. CSAS Research Document 2025/048.

Murphy, H. M., Adamack, A. T., Lewis, R. S., and Bourne, C. M. 2025. Assessment of Capelin in NAFO Divisions 2J+3KL to 2023. CSAS Res. Doc. 2025/022.

Northwest Atlantic Fisheries Centre. 2025. 2J3KL Cod and Capelin Biomass Indices. Zenodo. https://doi.org/10.5281/zenodo.17515115

Schijns, R., et al. 2021. Five centuries of cod catches in Eastern Canada. *ICES Journal of Marine Science* 78: 2675–.

Internal programme documents cited by ID: general theory manuscript §15; R03; R04; A014 revised; closure review Wave E.
