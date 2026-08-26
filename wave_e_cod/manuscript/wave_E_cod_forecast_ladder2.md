# Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL

## Abstract

The general theory of sustainability admits additional model structure only when that structure improves early warning, out-of-sample prediction, or intervention selection. This paper applies that test to Northern cod in NAFO divisions 2J3KL.

The primary predictand is the NCAM $M$-shift spawning-stock biomass (SSB) series of DFO (2016, Table A2), 1983--2015. The 2016 limit reference point (LRP) is the 1983--1989 mean SSB, 884.6 kt. Nested surplus-production models and two naive baselines issue fixed-window and rolling-origin forecasts. Catch enters first as a coarse regime (240 / 120 / 5 kt) and then as year-by-year landings (Schijns et al. 2021). NCAM fishing mortality and natural mortality are joint assessment outputs and are not used as exogenous drivers.

No structural model has lower primary RMSE than last-value persistence. One-year rolling RMSE is 98 kt for persistence and 115--206 kt for the surplus-production ladder. Year-by-year landings do not change the ranking (stock-flow RMSE 160 kt). Five-year RMSE is 265 kt versus 289--488 kt. The collapse window (train 1983--1990, test 1991--1995) is missed by every model (RMSE 694--819 kt): a constant-productivity surplus model with a 1992 catch drop cannot produce the observed crash. An AR residual and a one-year information delay do not reduce that error; the delay raises it. On the recovery window the autonomous Allee fit has the lowest structural RMSE (90 kt) but is unidentified ($s\to 0$, $K$ pinned).

The same retention rule holds on a second, unpooled specification (xteNCAM, 1954--2024, LRP 276 kt): persist one-year RMSE 88 kt versus 120 kt for the autonomous Schaefer model. Capelin-informed productivity, using a 1991 regime break or the tabulated acoustic index without interpolation across 1991, is not retained on the primary score.

**Keywords:** viability; forecast evaluation; Northern cod; surplus production; model ablation; persistence

---

## 1. Introduction

Comparative model evaluation is required before additional structure is retained for prediction or control (general theory §15). The ladder is output-only, stock-and-flow, residual, then delay and observation. A module is kept only if it improves a preregistered score.

Northern cod in 2J3KL is an R04-admitted fisheries object. Module A014 is admitted at corrected scalar-autonomous status. This paper does not estimate an Allee threshold, identify the cause of the 1990s collapse, or evaluate whether the 1992 moratorium was adequate. It asks whether stock-flow, residual, delay, or prey-informed modules reduce SSB forecast error relative to last-value persistence and to an autonomous surplus-production model.

A groundwater evaluation on Edwards J-17 is reported separately. The series are not pooled.

---

## 2. Data and specifications

Claim types in the specification tables follow the programme taxonomy: D, data; E, empirical construct; M, model; N, normative threshold.

**Table 1.** Primary specification $\Omega_{2016}$.

| Field | Contents | Type |
|---|---|---|
| System | Northern cod, NAFO 2J3KL, as represented by NCAM $M$-shift SSB | D |
| Interest | Continuity of a spawning stock on the 2016 precautionary-approach cautious or healthy side of the 2016 LRP | N |
| Domain | Stock area in DFO (2016) Figure 1; calendar years 1983--2015 | D |
| $K^*$ | $S_t\ge\mathrm{LRP}=884.6$ kt (1983--1989 mean of Table A2) | N |
| Disturbance | Unspecified productivity shocks; not a fitted $M(t)$ | M |
| Theoretical catch | Any $C_t\ge 0$ | M |
| Implementable catch | Pre-1992 directed fishery; post-2 July 1992 moratorium and low inshore removals | E |
| Horizon | Hindcast 1983--2015; two fixed test windows and rolling origin | D |

Table A2 also reports $F$ and $M$. They are joint outputs with SSB and are not used as exogenous inputs.

Regular et al. (2025) extend the assessment to 1954, revise the LRP to 276 kt (40% of $B_{\mathrm{MSY}}$), and estimate 2024 SSB at 342 kt. That is a second specification, $\Omega_{\mathrm{xte}}$ (Section 5.3). The two objects differ in four typed fields: the dynamics map (xteNCAM versus NCAM $M$-shift; start year 1954 versus 1983), the safe-set map (276 kt versus 884.6 kt), the treatment of catch, and the horizon. The two SSB columns are not mixed. If either the safe-set map or the dynamics map fails, R04 forbids judgment transfer. Both fail.

---

## 3. Forecast models

Discrete surplus production, $S$ in kt and $C$ in kt yr$^{-1}$:

\[
S_{t+1}=\bigl[S_t+rS_t\bigl(1-S_t/K\bigr)\tfrac{S_t-\mathfrak s}{K-\mathfrak s}-C_t+\varepsilon_t\bigr]_+
\]

with $\mathfrak s=0$ unless an Allee term is active.

**Table 2.** Model ladder.

| ID | Class | Free on the training window | Frozen into the test window |
|---|---|---|---|
| persist | baseline | --- | $\hat S_{t+h}=S_t$ |
| mean | baseline | training mean | $\hat S_{t+h}=\bar S_{\mathrm{train}}$ |
| M1 | autonomous | $r,K,C$ constant | same $C$ |
| M1b | autonomous with Allee | $r,K,\mathfrak s,C$ | same |
| M2 | stock-flow | $r,K$; $C_t$ prescribed | prescribed $C_t$ |
| M3 | residual | M2 + AR(1) residual | $\phi$ persisted |
| M4 | delay | M3 | forecast starts from $S_{t-1}$ |

The coarse catch regime, taken from DFO (2016) prose, is $C_t=240$ for $t\le 1991$, $C_t=120$ for $t=1992$, and $C_t=5$ for $t\ge 1993$. Year-by-year landings (Schijns et al. 2021, Table 1) replace that regime in Section 5.2. Regular et al. (2025) Table 1 matches Schijns exactly on 1983--1993 (11 years, maximum absolute difference 0 t). A 1956 discrepancy between those sources (236,210 t versus 263,210 t) lies outside 1983--2015 and is unused.

Parameters are estimated by one-step least squares on the training window only. Bounds: $r\in(0.001,2]$, $K$ above the training maximum.

A survey-start variant replaces the surplus initial condition by $\hat q\,I_t$, where $I_t$ is the autumn research-vessel abundance index and $\hat q$ is the training-window median of $\mathrm{SSB}/I$. The index is an NCAM input, not an independent stock.

Prey-informed variants (Section 5.4) scale surplus production by a 1991 capelin regime or by the tabulated 3L spring acoustic index. Pre-1991 acoustic values are not carried across 1991. Missing survey years are not interpolated.

---

## 4. Evaluation

Fixed windows on $\Omega_{2016}$: collapse, train 1983--1990, test 1991--1995; recovery, train 1995--2007, test 2008--2015. Rolling origin: minimum eight training years; horizons $h=1$ and $h=5$.

The primary score is RMSE of SSB (kt). Secondary scores are mean absolute error, RMSE on $\log S$, Brier score for $\mathbf{1}\{\hat S<\mathrm{LRP}\}$, and the sign-hit rate of $\Delta S$ on fixed windows.

A module is retained only if it reduces primary RMSE relative to the next-simpler model and relative to persistence. Retention is decided separately on each specification.

On $\Omega_{\mathrm{xte}}$ the collapse window is train 1954--1989, test 1990--1995. Catch is Table 1 landings (2024 persisted from 2023). No row is taken from NCAM 2016.

---

## 5. Results

### 5.1 Primary specification

![Figure 1](fig1_series.png)

**Figure 1.** NCAM $M$-shift SSB (DFO 2016, Table A2). Dashed line: 2016 LRP $=884.6$ kt. 2015 SSB is 33.8% of that LRP, matching the advisory report statement of 34%.

![Figure 2](fig2_windows.png)

**Figure 2.** Multi-step forecasts from the end of each training window.

**Table 3.** Fixed-window scores (RMSE in kt).

| Window | Model | RMSE | MAE | log-RMSE | Brier | Direction |
|---|---|---:|---:|---:|---:|---:|
| Collapse | M1 | 694 | 638 | 2.73 | 1.00 | 0.50 |
| | M1b | 694 | 636 | 2.73 | 0.80 | 0.00 |
| | M2 | 819 | 751 | 2.85 | 1.00 | 0.25 |
| | M3 | 819 | 751 | 2.85 | 1.00 | 0.25 |
| | M4 | 819 | 750 | 2.85 | 1.00 | 0.25 |
| Recovery | M1 $=$ M2 | 120 | 105 | 0.61 | 0.00 | 0.57 |
| | M1b | **90** | 55 | 0.52 | 0.00 | 0.57 |
| | M3 | 220 | 200 | 0.92 | 0.00 | 0.57 |
| | M4 | 214 | 195 | 0.91 | 0.00 | 0.57 |

On collapse, fitted $r$ saturates at the upper bound ($\approx 2$). The 1983--1990 window is a high, weakly trending stock. Surplus production does not identify the 1992--94 mortality pulse, and dropping $C$ from 240 to 5 raises forecast SSB. If the crash were a catch-regime event in this accounting, M2 would improve on M1. It does not.

On recovery, M1 and M2 coincide because $C_t\equiv 5$ on both train and test. M1b reports a lower RMSE, but $\mathfrak s\to 0$ and $K$ collapses to the training range: an unidentified Allee parameter, not a biological threshold. M3's $\phi=0.95$ persists a negative residual and increases error.

![Figure 3](fig3_rmse.png)

**Figure 3.** Rolling-origin RMSE. Persistence is the best one-year and five-year point forecast.

**Table 4.** Rolling-origin summary, $\Omega_{2016}$, coarse catch regime.

| Model | $h=1$ RMSE | $h=1$ MAE | $h=1$ log-RMSE | $h=5$ RMSE |
|---|---:|---:|---:|---:|
| persist | **98** | **48** | **0.52** | **265** |
| M1 | 121 | 80 | 8.02 | 289 |
| M1b | 115 | 80 | 8.70 | 289 |
| M2 | 144 | 61 | 0.59 | 398 |
| M3 | 135 | 53 | 3.39 | 366 |
| M4 | 196 | 82 | 0.76 | 488 |
| mean | 424 | 375 | 2.35 | 507 |

Log-RMSE for M1 and M1b is large because some origins produce trajectories that hit the numerical floor. M2 keeps the state off zero and stabilizes the log score, but loses on raw RMSE. M4, the only model that imposes a one-year assessment delay, is the worst structural model on raw RMSE.

No module M2--M4 is retained on $\Omega_{2016}$. Persistence is the lowest-RMSE forecast.

### 5.2 Annual landings and survey start

Year-by-year landings for 2015 are 4.436 kt. Pre-collapse catches are 172--269 kt, not a flat 240. The 1992 drop is to 41 kt, then 11 kt, then about 0.4--1.3 kt.

**Table 5.** Rolling-origin RMSE (kt) with annual landings.

| Model | $h=1$ | $h=5$ |
|---|---:|---:|
| persist | **98** | **265** |
| M1 | 121 | 289 |
| M1b | 115 | 289 |
| M2 | 160 | 394 |
| M3 | 154 | 352 |
| M4 | 206 | 486 |
| M2, survey start | 128 | 331 |

Annual landings make M2 worse than the coarse regime on one-year RMSE (160 versus 144 kt). Collapse-window RMSE remains about 821 kt. Apparent net production $S_{t+1}-S_t+C_t$ is strongly negative in 1991--93 even after subtracting reconstructed catch. A more accurate $C_t$ cannot produce the crash in a constant-$r$ surplus model.

Starting from $\hat q I_t$ instead of SSB: one-year RMSE 128 kt (still worse than persist 98); one-year log-RMSE 0.49 versus persist 0.52; five-year RMSE 331 versus persist 265. On the primary score the variant is not retained. The log-score difference is recorded and not used for selection. A set-valued conservative filter is not instantiated: there is no observation fibre outside NCAM.

### 5.3 Alternative assessment specification

![Figure 4](fig4_xtencam.png)

**Figure 4.** The two specifications. Overlap 1983--2015 RMSE $=126$ kt (2015: NCAM 299 kt, xteNCAM 273 kt). Different $K^*$. Not pooled.

Checkpoints from Regular et al. (2025) Table 17: 2005 SSB $=26$ kt, 2017 $=451$ kt, 2024 $=342$ kt, 2024/LRP $=1.24$. The 2005 values (26 kt versus NCAM 25.18 kt) can agree on a low year without sharing an LRP.

**Table 6.** Rolling-origin RMSE on $\Omega_{\mathrm{xte}}$ (kt).

| Model | $h=1$ | $h=5$ |
|---|---:|---:|
| persist | **88** | **318** |
| M1 | 120 | 432 |
| M1b | 152 | 446 |
| M2 | 166 | 1059 |
| M3 | 127 | 930 |
| M4 | 206 | 1031 |
| mean | 449 | 506 |

Collapse window (train 1954--89, test 1990--95): M1 RMSE 817 kt; M2 1898 kt. Official landings worsen the crash forecast. No module is retained. Persistence remains the lowest-RMSE forecast. The longer series and the revised LRP do not justify retaining the additional modules.

Regular et al. assign the 1992--94 disappearance primarily to $M$ (peak $\approx 2.5$), informed by tagging and a capelin/cod predictor, and note that some of that $M$ could still be unreported $F$. That split is the same as the surplus residual after subtracting official $C_t$.

### 5.4 Prey-informed productivity

Murphy et al. (2025) report a 1991 acoustic collapse (1985--90 median 3704 kt versus 1991--2022 median 174 kt). A two-regime $r$ with break 1991 uses the high regime only for forecasts issued before 1991.

**Table 7.** Rolling RMSE, two-regime $r$.

| Specification | Model | $h=1$ | $h=5$ |
|---|---|---:|---:|
| $\Omega_{2016}$ | persist | **98** | **265** |
| $\Omega_{2016}$ | M\_cap | 154 | 334 |
| $\Omega_{\mathrm{xte}}$ | persist | **88** | **318** |
| $\Omega_{\mathrm{xte}}$ | M\_cap | 147 | 894 |

On post-break origins only ($\Omega_{\mathrm{xte}}$, $h=1$): M\_cap 107 versus persist 88. Not retained.

The year-by-year 3L spring acoustic biomass is tabulated in Zenodo 10.5281/zenodo.17515115, with 2023 $=331.3$ kt from Murphy et al. (2025). Surplus is scaled by $(I_{\mathrm{known}}/I_{\mathrm{ref}})^{b}$, where $I_{\mathrm{known}}(t)$ is the last observation at or before $t$.

**Table 8.** Rolling RMSE, observed acoustic index.

| Specification | Model | $h=1$ | $h=5$ |
|---|---|---:|---:|
| $\Omega_{2016}$ | persist | **98** | 265 |
| $\Omega_{2016}$ | M\_cap\_index | 150 | 262 |
| $\Omega_{\mathrm{xte}}$ | persist | **88** | **318** |
| $\Omega_{\mathrm{xte}}$ | M\_cap\_index | 132 | 492 |

On $\Omega_{2016}$, five-year RMSE is a near-tie (262 versus 265 kt). One-year RMSE is worse. The module is not retained.

---

## 6. Discussion

The observed path is non-monotone. An exact fixed autonomous scalar trajectory cannot reproduce it; M1's collapse failure is the finite-sample face of that obstruction (A014).

Under both the coarse catch regime and official landings, lowering $C$ in 1992 cannot generate the crash. Collapse on these specifications is a productivity, unallocated-mortality, or observation event, not a surplus-production response to the declared catch drop. That is compatible with DFO's caution that NCAM $M$ can absorb unreported deaths.

Unidentified extra structure increases error. Autoregressive residuals fitted on short, regime-changing windows persist the wrong sign. An Allee parameter goes to the boundary. A one-year delay removes information.

The 2016 LRP is the 1980s mean SSB. Slack to that bound is near zero by construction throughout the training window that precedes collapse. A leading-indicator claim that uses this $K^*$ is circular for 1983--1990.

The moratorium is a change in implementable catch and is already in $C_t$. A separate delay switch does not add a degree of freedom beyond stock-flow. Whether the 1992 architecture has an empty viability kernel is a viability statement, not a one-year RMSE statement.

One-dimensional surplus production is not NCAM: age structure, migration, and survey catchability are omitted. The test is whether this ladder earns retention, not whether the assessment is a good filter. M4 is a delay, not a Kalman filter. Recreational catch remains incompletely measured. Sample sizes are small ($n=33$ years on $\Omega_{2016}$; rolling $n=25$ at $h=1$). They suffice to rank models and do not suffice to certify a small skill difference.

The scores do not transfer an interval-verified linear toy, do not instantiate a closed-loop information filter, and do not mix the two assessment specifications.

---

## 7. Conclusions

On locked NCAM $M$-shift SSB for 1983--2015, last-value persistence is more accurate than surplus production, catch-driven stock-flow, autoregressive residuals, delayed information, and prey-informed productivity. The crash is not a catch-drop event in this accounting. Extra modules that fail identification increase error. The same retention outcome holds on the unpooled xteNCAM series.

The paper reports a forecast comparison. It does not conclude that the stock is unsustainable, and it does not conclude that the general theory is empirically confirmed on this stock.

---

## Data and code availability

Locked inputs, scoring scripts, and result files are in `wave_e_cod/` of <https://github.com/MIKEAA2020/general-sustainability>. Primary SSB: DFO (2016) Table A2. Alternative SSB and landings: Regular et al. (2025) Tables 17 and 1. Historical landings: Schijns et al. (2021). Capelin acoustic index: Zenodo 10.5281/zenodo.17515115 and Murphy et al. (2025). An independent execution of the scoring scripts reproduced the committed result files (`batch 4/WAVE_E_RERUN.md`). That reproduction does not close a Wave E specification-matching gate.

```
python3 src/run_ladder.py && python3 src/run_xte.py
python3 src/run_capelin_regime.py && python3 src/run_capelin_index.py
python3 src/compare_catch.py && python3 src/make_figures.py
```

---

## References

Cadigan, N. G. 2016. A state-space stock assessment model for Northern cod, including underreported catches and variable natural mortality rates. *Canadian Journal of Fisheries and Aquatic Sciences*.

DFO. 2009. A fishery decision-making framework incorporating the Precautionary Approach.

DFO. 2010. Proceedings of the Newfoundland and Labrador Regional Atlantic Cod Framework Meeting. CSAS Proceedings 2010/053.

DFO. 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in 2016. CSAS Science Advisory Report 2016/026.

DFO. 2024. NAFO Divisions 2J3KL Northern cod stock assessment to 2024. CSAS Science Advisory Report 2024/049.

Murphy, H. M., Adamack, A. T., Lewis, R. S., and Bourne, C. M. 2025. Assessment of capelin in NAFO Divisions 2J+3KL to 2023. CSAS Research Document 2025/022.

Northwest Atlantic Fisheries Centre. 2025. 2J3KL cod and capelin biomass indices. Zenodo. <https://doi.org/10.5281/zenodo.17515115>

Regular, P. M., et al. 2025. Assessment of the Northern cod stock in NAFO Divisions 2J3KL in 2024. CSAS Research Document 2025/048.

Schijns, R., et al. 2021. Five centuries of cod catches in Eastern Canada. *ICES Journal of Marine Science* 78: 2675--.

DFO. 2024. Assessment of capelin in NAFO Divisions 2J3KL. CSAS Science Advisory Report 2024/050.
