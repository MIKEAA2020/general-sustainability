# Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17

**Prepared in the format of Groundwater (Wiley/NGWA)**

## Abstract
Index-well head forecasting is a recurring operational problem of groundwater management. This evaluation follows a stated retention rule, fixed in the analysis scripts before execution: structure is retained only when it improves the declared out-of-sample score against persistence and the next-simpler causal model, under the class veto fixed in the protocol (constant-flux reductions of the causal map are declined on class grounds). The predictand is the calendar-year mean of daily-high elevation at the J-17 index well, 1934–2023, in feet. One-year rolling RMSE is 13.23 ft for last-value persistence and 12.84 ft for a univariate AR(1), retained as an output-only model by a margin of 0.39 ft at the one-year horizon (MAE is a tie; at five years the AR(1) does not beat persistence, so retention is a one-year statement). The causal stock-flow specification has RMSE 14.70 ft and is rejected; a climatological variant reaches 12.28 ft but shares the AR(1)'s forecast equation and is declined on the class grounds fixed in the protocol. At five years, training-mean climatology (16.80 ft) beats persistence (21.11 ft). Given realized future recharge and pumpage, the same map reaches 7.55 ft through estimated coefficients, not an aquifer oracle — an error reduction of 43% of the persistence error that no signal available at the annual origin recovers. Three of the four climate-informed recharge forecasts lie within 0.13 ft of AR(1) at one year; the R-AR variant is 0.41 ft worse; none is retained. Contemporaneous Comal Springs discharge tracks J-17 (r = 0.986) but is a measured service of the same state, not an independent information source.--

## 1. Introduction

Forecasting aquifer heads at index wells is a recurring operational problem of groundwater management: drought-stage declarations, springflow protection, and permit adjustments all key on forecasted water levels. The methodological literature has responded with an increasingly rich inventory of groundwater-level forecasting models, from conceptual water balances to data-driven regressions and, prominently, artificial-neural-network and wavelet–neural-network conjunction models trained on measured heads (Daliakopoulos, Coulibaly, and Tsanis 2005; Adamowski and Chan 2011). The field has also begun to institutionalize benchmark culture: GEMS-GER, the first machine-learning benchmark dataset for long-term groundwater levels, standardizes 32 years of weekly observations from 3,207 German wells together with three benchmark models of increasing complexity (Ohmer et al. 2026), and systematic comparisons of nine machine-learning and deep-learning architectures on a karst catchment now anchor the karst groundwater forecasting literature (Zhu et al. 2026).

The term "water balance" is used throughout in its increment-structure sense: head change equals weighted fluxes plus a linear drain, with the spring-discharge series stored but deliberately excluded from the forecasting equation and a [610, 710] clip standing in for a physical storage floor — the map is not a closed mass balance, and the qualification travels with every use of the term. Whether added structure improves out-of-sample forecasts — as opposed to in-sample fit — is a separate, testable question, and the general forecasting literature has made the benchmark discipline explicit: across the M4 competition's 100,000 series, sophisticated methods did not uniformly beat simple statistical baselines (Makridakis, Spiliotis, and Assimakopoulos 2020). The minimal bar for any proposed module is therefore the forecast that nothing changes — last-value persistence — together with the training mean. Yet the groundwater benchmark studies above compare model families against one another; they do not subject each module to a retention gate against the naive baselines, and none subjects a deliberately simple process-based water balance to a scored ablation against those baselines. This paper supplies that missing test: a scored model-ablation design, in which a ladder of incrementally structured one-pool models is evaluated against the two naive baselines, and complexity is kept only if it improves the stated score, decided on out-of-sample error on the predictand itself.

The San Antonio Pool of the Edwards (Balcones Fault Zone) Aquifer, Texas, indexed by the J-17 well, is the natural test bed. Its 1934–2023 daily head record is among the longest managed groundwater series in North America; its institutional thresholds (the 660-ft Stage I line of the Edwards Aquifer Authority) and its physical threshold (the ≈618-ft level at which Comal Springs approaches cessation) are explicit and dated; and recharge and pumpage series exist that are constructed independently of the head series. The aquifer is also a karst system in which regional flow has long been represented — and debated — through equivalent porous media and lumped approaches (Scanlon et al. 2003, for the Barton Springs segment; the lumped-versus-EPM question is inherited by the San Antonio Pool, not settled by that citation), which makes the fate of a deliberately simple one-pool water-balance map a live hydrogeologic question rather than a straw man.

The question is whether stock-flow, residual, delay, or climate-informed recharge modules reduce forecast error of J-17 annual-mean head relative to last-value persistence and to a univariate AR(1). The climate modules enter because El Niño/Southern Oscillation (ENSO) phases shift North American precipitation patterns (Ropelewski and Halpert 1986): September–November Niño 3.4 and lagged climate-division precipitation are precisely the signals observable at an annual forecast origin.

A companion study under separate review applies the same scored design to a marine fishery stock (Northern cod, NAFO 2J3KL); the two systems' scores are never pooled, and no retention verdict is transferred between them. This paper does not assess whether the aquifer is sustainable, does not close the two-pool exchange module's blocking list, and does not treat springflow or reconstructed storage as co-primary predictands. No solute or water-quality module is opened.

## 2. Data and Specification

**Table 1.** The San Antonio Pool specification: J-17 annual-mean elevation, 1934–2023.

| Field | Contents | Type |
|---|---|---|
| System | Edwards Aquifer, San Antonio Pool, indexed by J-17 | D |
| $z_t$ | Calendar-year mean of daily-high J-17 elevation (ft AMSL) | D |
| Well | TWDB 6837203 / EAA AY-68-37-203 | D |
| Domain | San Antonio Pool; calendar years 1934–2023 | D |
| Physical threshold | Head high enough that Comal Springs does not cease (≈618 ft; 1956 daily minimum 612.51 ft) | N / E |
| Institutional threshold | EAA Stage I, 10-day mean J-17 < 660 ft (in force after 2007) | N |
| Disturbance | Recharge pulses; unmodeled karst; Uvalde–San Antonio exchange | M |
| Implementable use | Pre-EAA pumping; post-1996/2007 permits and critical-period management | E |
| Service series | USGS 08168710 Comal Springs annual mean discharge (cfs) | D |

Field types: D = data, E = empirical construct, M = model, N = normative threshold. The predictand is a measured well series. It is not a GRACE or G3P storage reconstruction, a MODFLOW or GWSIM inversion, EAA reconstructed storage, the J-27 Uvalde index, San Marcos Springs, or total spring discharge.

Stage I at 660 ft is a 2007 institutional rule and is not applied as if it existed in 1956. Cessation of Comal Springs near 618 ft is a physical service bound. The indicator 1{H < 660} on the annual mean is a coarse proxy for the Authority's 10-day declaration, not the declaration itself.

Annual means use all available daily highs. Years with fewer than 240 observations are dropped; no year falls below the floor (minimum n = 242, 1939), so the rule is vacuous on this panel; 1935 (n = 258) and 1939 (n = 242) satisfy the 240-observation rule and are retained as incomplete-coverage means (they are not exceptions — they are the incomplete years that still qualify); missing days are not interpolated. The published pre-continuous composite (Beverly Lodges extension) is used as issued. The complete estimation panel ends in 2023, whose values carry provisional TWDB status.

Recharge R is USGS total San Antonio-area recharge (10³ acre-ft yr⁻¹), estimated by the Puente (1978) stream-loss method and constructed independently of J-17 (Umphres and Choi 2025). Pumpage P is well discharge from Edwards Aquifer Authority Table 1. Total spring discharge is stored and is not used as a driver. Climate predictors, used only in Section 5.4, are September–November Niño 3.4 (HadISST, anomaly relative to 1991–2020) and calendar-year precipitation in Texas climate divisions 06 and 07 (NCEI nClimDiv).

## 3. Forecast Models

The one-pool map, with head clipped to [610, 710] ft, is

$$H_{t+1}=\bigl[H_t+\alpha+\beta\tilde R_{t+1}+\gamma\tilde P_{t+1}+\delta H_t\bigr]_{\mathrm{clip}},$$

where $\tilde R$ and $\tilde P$ are the flux values a forecast substitutes for the (unknown) year $t+1$ fluxes. Forecasts are issued at the end of year $t$ from (H, R, P) through $t$.

**Table 2.** Model ladder.

| ID | Class | Fluxes at $t+k$ | Role |
|---|---|---|---|
| persist | baseline | — | $\hat H_{t+h}=H_t$ |
| mean | baseline | — | training-window mean |
| M1 | autonomous | — | $H_{t+1}=a+\varphi H_t$ |
| M2 | causal stock-flow | last $(R_t,P_t)$ persisted | candidate for retention |
| M2m | climatological stock-flow | training-mean $(R,P)$ | affine AR(1) |
| M3 | residual | as M2 | AR(1) residual on $\Delta H$ |
| M4 | delay | as M2 | starts from $H_{t-1}$ |
| M2_oracle | diagnostic | realized future $R,P$ | excluded from retention |

With constant fluxes, M2m reduces to $H_{t+1}=(1+\delta)H_t+\mathrm{const}$ and therefore shares M1's forecast function class — but not its estimator: M2m pins its intercept and persistence from the in-sample mean fluxes, an additional identifying use of the recharge and pumpage records in training. The protocol declines it because the retained object is forecast-time structure, not estimator refinement; the estimator distinction is recorded so that the decline is not misread as numerical equivalence of the two fits.

Climate-informed variants (Section 5.4) replace persisted R by a one-step forecast of R from information known at t: AR(1) on R, lagged Niño 3.4, lagged climate-division precipitation, or all three. A precipitation-oracle variant uses year $t+h$ precipitation and is excluded from retention. For horizons $h>1$, the one-step recharge forecast is held constant.

The scoring protocols for the primary pass and the climate pass were frozen and dated (2026-08-25) before the corresponding RMSE tables were computed; the frozen protocol documents are archived with the analysis code. The design is a fixed computational protocol rather than a prospective clinical-style registration.

## 4. Evaluation Design

The primary score is RMSE of annual-mean J-17, in feet. Secondary scores are mean absolute error and the Brier score for $\mathbf{1}\{\hat H < 660\}$, interpreted only for origins at or after 2007. A sign-hit rate of $\Delta H$ was listed in an earlier design iteration and is struck: no value is reported for it, and it is not part of any retention decision.

Fixed windows: (1) drought-of-record drawdown, train 1934–1950, test 1951–1956; (2) drought-of-record recovery, train 1934–1956, test 1957–1961; (3) pre-permit wet interval, train 1980–1990, test 1991–1995; (4) critical-period era, train 1997–2014, test 2015–2023.

Rolling origin: minimum 15 training years; horizons h = 1 and h = 5; n = 75 and n = 71 origins respectively (the 15-year floor is the rolling rule; the fixed windows use their declared trains).

A causal module is retained only if its primary RMSE is strictly less than that of persistence and strictly less than that of the next-simpler causal model. Diagnostic oracles are excluded from retention; the Comal series is excluded from retention. Retention is decided on the head series only; the service series is scored after that decision is frozen.

## 5. Results

### 5.1 The series

![Figure 1](figs_e3/fig1_series.png)

**Figure 1.** J-17 annual mean and daily-high range. 1956 mean 623.15 ft, daily minimum 612.51 ft. 1992 mean 691.96 ft, daily maximum 703.31 ft. 2023 mean 635.68 ft. The annual mean is below 660 ft in 31 of 90 years; the daily minimum is below 618 ft in one year (1956).

### 5.2 Fixed windows

![Figure 2](figs_e3/fig2_windows.png)

**Figure 2.** Multi-step forecasts from the end of each training window. The oracle (dashed) is diagnostic.

**Table 3.** Fixed-window RMSE (ft).

| Window | persist | mean | M1 | M2 | M2m | M3 | M4 | oracle |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Drawdown 1951–56 | 23.75 | 35.19 | 30.94 | **18.11** | 27.44 | 18.12 | 18.23 | 19.69 |
| Recovery 1957–61 | 43.62 | 14.07 | 56.24 | 55.32 | 37.74 | 55.28 | 55.12 | **12.26** |
| Pre-permit wet 1991–95 | 30.13 | 18.24 | 20.02 | 16.67 | 23.47 | 16.41 | 15.26 | **7.18** |
| Critical-period era 2015–23 | 27.41 | 14.77 | 15.62 | 23.37 | 14.79 | 22.84 | 22.17 | **8.70** |

Bold marks the best model of the window; on the drawdown window the best causal model, M2, also beats the oracle. The train-mean baseline is the best non-oracle forecast on the recovery window (14.07 ft) and on the critical-period era (14.77 ft), consistent with its rolling five-year win; the residual-persistence rungs M3/M4 track M2 on the drawdown (18.12/18.23 versus 18.11 ft); M4 is the best causal model on the pre-permit wet window (15.26 ft); and both fail with the causal family on the recovery and critical-period windows.

The 1950s drawdown is a continuing low-recharge path: the last observed R is already low, so causal M2 has lower RMSE than persistence (18 versus 24 ft) and also lower RMSE than the oracle. The linear map trained on 1934–1950 has the wrong sign on pumpage (γ = +0.021): pumping rose as the drought deepened, so pumpage is behaviorally coupled to recharge and the least-squares coefficient aliases the human response into the physical state transition — simultaneity bias; the short training window compounds the identification failure.

The 1957–61 recovery is a recharge pulse (R₁₉₅₆ = 43.7, R₁₉₅₇ = 1142.6 × 10³ acre-ft). Persistence stays at the 1956 floor (RMSE 44 ft). Causal M2 persists drought recharge and falls further (RMSE 55 ft). The oracle, given the 1957 flood year, tracks the rise (RMSE 12 ft). Recoveries on this specification are recharge events, not autonomous mean reversion and not a change in the pumping regime. The 1992 peak and the 2015–23 window repeat the same split: the oracle follows the recharge year; persistence and persisted recharge do not.

### 5.3 Rolling origin

![Figure 3](figs_e3/fig3_rmse.png)

**Figure 3.** Rolling-origin RMSE. The oracle is excluded from retention.

**Table 4.** Rolling-origin summary (ft).

| Model | h=1 RMSE | h=1 MAE | h=5 RMSE |
|---|---:|---:|---:|
| persist | 13.23 | 10.73 | 21.11 |
| mean | 16.17 | 13.17 | **16.80** |
| M1 | 12.84 | 10.72 | 21.25 |
| M2 | 14.70 | 11.45 | 33.49 |
| M2m | 12.28 | 10.22 | 17.44 |
| M3 | 14.46 | 11.12 | 33.46 |
| M4 | 14.30 | 11.17 | 33.39 |
| M2_oracle | 7.55 | 5.79 | 10.87 |

**Table 5.** Retention on rolling h = 1 RMSE.

| Model | Versus persist | Distinct structure | Decision |
|---|---|---|---|
| M1 | 12.84 < 13.23 | output only | retained (margin 0.39 ft) |
| M2 | 14.70 > 13.23 | causal fluxes | reject |
| M2m | 12.28 < 13.23 | no (affine AR(1)) | list only; not extra structure |
| M3, M4 | worse than persist | yes | reject |
| M2_oracle | 7.55 | uses future R, P | excluded |

M1 is retained by the point-RMSE rule at the one-year horizon. The margin is 0.39 ft on n = 75 and is not a significance claim — mean absolute error is a tie (M1 10.72 versus persist 10.73 ft), and at h = 5 M1 (21.25 ft) does not beat persistence (21.11 ft) while the training mean (16.80 ft) beats both, so the retention is explicitly a one-year, RMSE-level statement: it records a slightly mean-reverting head series, not a confirmation of stock-flow structure, and at the decision scale of annual drought-stage declarations the difference is operationally nil. M2m is listed by the same rule and then declined on the class grounds fixed in the protocol (constant fluxes reduce the forecast equation to the affine AR(1)); its numerical advantage is estimator-level, as stated. The climate modules are the same story nested one level up: the combination (12.71 ft) loses to its own nested comparator M2m (12.28 ft) — the declined M2m still serving as the declared nested comparator for the climate rung (a protocol kink, acknowledged) — which is the clean rejection, and the point-RMSE listing alone would not decide it. No stock-flow, residual, or delay module is retained.

At h = 5 the training mean (16.80 ft) has lower RMSE than persistence (21.11 ft): five-year forecasts on this basin are climatology, not last value and not persisted recharge.

Full-sample correlations: corr(H_t, H_{t−1}) = 0.64 with AR(1) coefficient φ̂ = 0.66; corr(R_t, R_{t−1}) = 0.17; corr(ΔH_t, R_t) = 0.74. Full-sample (β̂, γ̂) = (0.017, −0.026) have the expected signs when the sample is long. The water-balance class is not empty, but recharge is not persistent.

On post-2007 origins only (n = 16, h = 1): persist 13.09, M1 12.16, M2 13.31, oracle 8.03 ft. The ranking is unchanged. The 660-ft Brier scores are 0.31 (persist), 0.25 (M1), and 0.19 (oracle). At h = 5 (n = 12): persist 25.10, M1 17.16, M2m 17.64, mean 16.41, M2/M3/M4 34.9–35.0, oracle 8.69 ft — the post-2007 h = 5 reversal of the M1–persistence ordering is reported without changing the one-year retention statement. The declared scoring choice at h = 5 compares a no-change persistence forecast with iterated model trajectories; the iterated affine analogue M2m (17.64 ft) sits with the mean. The annual-mean proxy is not the 10-day rule.

### 5.4 Climate-informed recharge

Information known at 31 December of year t comprises R_t, the September–November Niño 3.4 anomaly of year t, and calendar-year precipitation in Texas climate divisions 06 and 07. December–February precipitation that includes January of t+1 is not used.

![Figure 4](figs_e3/fig4_pass2.png)

**Figure 4.** Rolling RMSE on J-17 for climate-informed recharge. The precipitation oracle uses year t+h precipitation and cannot be retained.

**Table 6.** Rolling RMSE, climate-informed recharge.

| Model | H, h=1 (ft) | H, h=5 (ft) | R, h=1 (10³ acre-ft) |
|---|---:|---:|---:|
| persist H / persist R | 13.23 | **21.11** | 702 |
| M1 | 12.84 | 21.25 | — |
| M2_Rar | 13.25 | 25.38 | 561 |
| M2_Renso | 12.82 | 24.42 | 528 |
| M2_Rprecip | 12.80 | 25.38 | 545 |
| M2_combo | 12.71 | 26.88 | 538 |
| rain climatology | — | — | 556 |
| rain oracle | 10.56 | 16.91 | **354** |

Same-year corr(R, precipitation) = 0.78, which is why the precipitation oracle reduces head RMSE to 10.56 ft; it remains worse than the full (R, P) oracle (7.55 ft) because the linear rain map misses 1957-scale extremes.

Lagged precipitation and September–November Niño 3.4 have modest skill on R relative to climatology (528–545 versus 556 × 10³ acre-ft), and they do not constitute forecast structure on head: the point-RMSE rule lists ENSO, lagged precipitation, and the combination (each less than persist and less than M1), but the margins versus M1 are 0.02, 0.04, and 0.13 ft; at h = 5 all three have RMSE 3–6 ft higher than persistence (the h > 1 climate scores reuse the one-step recharge forecast, held constant over the horizon); and they are M2m with a weakly adjusted intercept. M2_Rar loses at h = 1 (13.25 ft; 0.41 ft worse than M1) — autoregression on nearly white recharge is not a recharge forecast.

On the 1957–61 recovery, no causal climate-informed module has lower RMSE than persistence (persist 43.6 ft; best causal about 48.8 ft; precipitation oracle 33.7 ft). September–November 1956 is La Niña (−0.92) and does not announce R₁₉₅₇ = 1143.

The remaining fixed windows complete the same record: drawdown 1951–56, M2_Renso 24.30, M2_Rprecip 28.67, M2_combo 24.70, precipitation oracle 18.16 ft; pre-permit wet 1991–95, M2_Rprecip 22.03, M2_Renso 23.03, M2_Rar 23.94, M2_combo 25.71, oracle 10.98 ft; critical-period era 2015–23, M2_Rprecip 14.52, M2_Rar 14.67, M2_Renso 16.01, M2_combo 16.57, oracle 9.75 ft — on this one window the two climate-informed modules M2_Rprecip and M2_Rar edge past M1 by about one foot (14.52 and 14.67 versus 15.62 ft). On the recharge target itself the fixed-window scores are an order of magnitude coarser on every window (climate modules 199–937; precipitation oracle 80.7–487, against the 556 × 10³ acre-ft climatology scale of the rolling record), so the marginal head advantage is a window-specific result, not a recharge forecast.

No climate-informed recharge module is retained. Closing the gap between persistence and the oracle would require next year's recharge, which is not available at the annual forecast origin.

### 5.5 The service series after the retention freeze

![Figure 5](figs_e3/fig5_fibre.png)

**Figure 5.** Comal annual mean versus J-17. Contemporaneous r = 0.986. The service series is a measured channel of the same state — a measured service, not an independent information source.

The map Q = c₀ + c₁H was fitted on 1934–1950 only (c₀ = −2876, c₁ = 4.77) and applied to already-issued Ĥ; the r = 0.986 figure is the full-sample contemporaneous correlation, not the 1934–1950 fit. The fitted map does not track the drought-of-record: at the 1956 annual mean (623.15 ft) it reads ≈97 cfs against an observed ≈32 cfs annual mean, so the Comal score is informative about information redundancy at ordinary heads, not about the drought tail. The fitted intercept implies zero discharge near 603 ft (2876/4.77 ≈ 602.9), below the ≈618 ft reference — the linear map itself predicts the 1956 tail failure, a consequence of the intercept not noted elsewhere. One-year Comal RMSE (cfs): persist 71.9, M1 69.0, M2m 68.7, M2 74.8, M3 73.8, M4 73.4, train-mean 89.7, oracle 45.3.

The service series does not change retention, and it cannot: it is nearly a linear transform of head. Comal is an independent measurement (a USGS spring gauge, not used to construct J-17), but it is not an independent information source. Gravimetric storage or the J-27 Uvalde index would be different objects, not a second fibre of this specification. Eastern-basin recharge was stored and not used.

## 6. Discussion

The one-pool increment ΔH tracks recharge (r = 0.74), and the oracle's RMSE is 43% below persistence at h = 1 and 49% below at h = 5: the map accounts for contemporaneous increments when the year's water is known. As a one-year forecast, causal stock-flow fails because the dominant increment is not persistent; residual and delayed variants inherit that timing error. Recoveries in 1957 and 1992 are missed by every causal model and captured by the oracle. The identified driver has the wrong timing for an annual origin — the same pattern a companion evaluation finds on Northern cod, where a more accurate catch series does not rescue constant-productivity surplus production. The two score tables are not pooled.

Two features distinguish this design from the groundwater benchmark literature it engages. First, the retention gate: GEMS-GER ships three benchmark models and reports the fraction of wells for which the best one reaches NSE > 0.5 (Ohmer et al. 2026), and the karst benchmark of Zhu et al. (2026) ranks nine architectures by RMSE and R² — both compare model families against one another, while here every module must beat persistence and the next-simpler causal model under a rule frozen before scoring, and on that rule the entire causal ladder is rejected at the one-year horizon. Second, the horizon contrast: no benchmark study of this basin reports that a training mean beats persistence at a longer horizon. The five-year climatology result (16.80 versus 21.11 ft) is the specification's most directly transferable finding for management planning that keys on multi-year outlooks.

Two specification points carry over to the interpretation. First, next-year pumpage is partially an institutional scenario — permits and critical-period rules respond to head — rather than a purely exogenous flux like rainfall; persisting last year's pumpage is a declared simplification, and the oracle pumpage is in no information set. Second, the karst setting matters. The annual affine one-pool specification is not a karst model: conduits, the Uvalde–San Antonio divide, unconfined recharge-zone storage, and the confined-zone pressure response remain in the residual, and the long-standing question whether lumped or equivalent-porous-media representations can carry regional flow (Scanlon et al. 2003) is inherited, not resolved, by this design. What the design shows is that at the annual origin, the information carried by such a map is timing-bound: the same structure that cannot forecast next year certifies this year — the water-balance map is a certificate for a year whose recharge is already known, not a forecast. The five-year climatology win is setting-specific in the same way: the San Antonio Pool is a rapidly recharged, institutionally bounded system — karst recharge and EAA critical-period limits hold the head within a band — so the training mean is informative at long horizons, and a non-stationary fossil aquifer under sustained depletion would not sustain a mean-reverting baseline; the climatology result is not claimed for such settings. The retained AR(1) admits a complementary reading: to first order, spring discharge obeys Darcy proportionality to head above the spring level, and the autonomous solution of that drainage law is an affine autoregression $H_{t+1} \approx (1-k)H_t + k H_s$; the fitted $\hat\varphi = 0.66$ is consistent with a drainage-decay coefficient $\hat k \approx 0.34$ yr⁻¹. The module is output-only in the protocol's sense — no flux data enter the forecast — but the shape it fits carries the aquifer's own free-drainage momentum.

The wrong leading indicator is worth recording. The 1950s decline is not a Stage I event: the 660-ft line is a 2007 rule, and slack to 660 ft is the wrong leading indicator for 1951–56, just as the 2016 Northern cod limit reference point was the wrong leading indicator for 1983–90 in the companion study. 1956 is a physical near-cessation at Comal (annual mean springflow 32 cfs; daily J-17 minimum 612.51 ft).

Two-pool exchange, solute, and barrier bookkeeping were not fitted and cannot be retained. In the two-pool parameterization the relative-exchange term is removed, leakage is not applicable, and no barrier or exchange term is fitted; the blocking list is not closed by this paper. Post-1997 pumpage no longer spikes with drought as in 1956 (321 kaf from wells); that change is already in P_t, and a separate critical-period switch adds no degree of freedom beyond the pumpage series.

Limitations follow the data and the map. Total-area R and P mix the San Antonio and Uvalde pools; recharge is a Puente estimate; pumpage includes unreported domestic, livestock, and federal use. Neither series is head. M4 is a one-year information delay, not a conservative filter; J-17 is a telemetered gauge whose head is recorded daily, so the module is kept in the ladder for symmetry with the companion fisheries evaluation and prices a theoretical information lag rather than a constraint of this system's monitoring. The sample is 90 years with four short test windows, and the 0.39-ft AR(1) margin is not a significance claim. Reopening the climate module with additional indices (PDO, AMO) on this annual origin would re-instantiate the rejected structure; a mid-year nowcast would require a new evaluation protocol.

## 7. Conclusions

On locked J-17 annual-mean head, last-value persistence is more accurate than a causal one-pool balance that persists last year's recharge. Univariate AR(1) improves one-year RMSE by 0.39 ft and is retained as an output-only model. The same balance, given realized recharge and pumpage, cuts error nearly in half; climate variables known at the annual origin do not recover that gap; and at five years, climatology wins.

The paper reports a forecast comparison. It does not conclude that the aquifer is unsustainable, and it does not conclude that the evaluation framework is empirically confirmed on this basin.

## Data Availability Statement

All input data, analysis scripts, and result files are archived in the public repository at https://github.com/MIKEAA2020/general-sustainability, together with the frozen scoring protocols (dated 2026-08-25, locked before any score was generated). J-17 daily highs: Texas Water Development Board well 6837203. Recharge: Umphres and Choi (2025), USGS data release, https://doi.org/10.5066/P1BI62NY. Pumpage: Edwards Aquifer Authority Table 1. Comal Springs: USGS 08168710. Niño 3.4: NOAA PSL HadISST (raw file committed with the repository). Precipitation: NCEI nClimDiv — the raw file is not distributed with the repository (provenance URL archived in the sources index), so the three precipitation columns of the fixed panel are not reproducible from the committed code alone, while the two Niño columns rebuild from the committed file to machine precision; scoring from the committed analysis panel does not require the nClimDiv file. The committed twenty-column analysis panel is the dataset of record for all scored analyses. All computations are deterministic: re-executing the committed scripts in a fresh environment regenerated every archived result file byte for byte, and all scored rows recompute from the per-observation forecast files and the committed series.

## References

Adamowski, J., and Chan, H.F. 2011. A wavelet neural network conjunction model for groundwater level forecasting. *Journal of Hydrology* 407: 28–40. https://doi.org/10.1016/j.jhydrol.2011.06.013

Daliakopoulos, I.N., Coulibaly, P., and Tsanis, I.K. 2005. Groundwater level forecasting using artificial neural networks. *Journal of Hydrology* 309: 229–240. https://doi.org/10.1016/j.jhydrol.2004.12.001

Edwards Aquifer Authority. 2024/25. *2023 Groundwater Discharge and Usage*, Table 1 (after USGS letter report, 5 April 2024). https://www.edwardsaquifer.org/wp-content/uploads/2025/05/2023-Groundwater-Discharge-and-Usage.pdf

Edwards Aquifer Authority. Critical Period / Drought Management. https://www.edwardsaquifer.org/groundwater-users/critical-period-drought-management/

Makridakis, S., Spiliotis, E., and Assimakopoulos, V. 2020. The M4 Competition: 100,000 time series and 61 forecasting methods. *International Journal of Forecasting* 36: 54–74.

NOAA National Centers for Environmental Information. nClimDiv precipitation (climdiv-pcpndv-v1.0.0). https://www.ncei.noaa.gov/pub/data/cirs/climdiv/

NOAA Physical Sciences Laboratory. Niño 3.4 monthly SST (HadISST). https://psl.noaa.gov/data/timeseries/month/data/nino34.long.data

Ohmer, M., Liesch, T., Habbel, B., Heudorfer, B., Gomez, M., Clos, P., Nölscher, M., and Broda, S. 2026. GEMS-GER: A machine learning benchmark dataset of long-term groundwater levels in Germany with meteorological forcings and site-specific environmental features. *Earth System Science Data* 18, 77.

Puente, C. 1978. *Method of estimating natural recharge to the Edwards Aquifer in the San Antonio area, Texas.* U.S. Geological Survey, Austin, Texas.

Ropelewski, C.F., and Halpert, M.S. 1986. North American precipitation and temperature patterns associated with the El Niño/Southern Oscillation (ENSO). *Monthly Weather Review* 114: 2352–2362.

Scanlon, B.R., Mace, R.E., Barrett, M.E., and Smith, B. 2003. Can we simulate regional groundwater flow in a karst system using equivalent porous media models? Case study, Barton Springs Edwards aquifer, USA. *Journal of Hydrology* 276: 137–158.

Texas Water Development Board. Water Data for Texas, well 6837203 (J-17). https://waterdatafortexas.org/groundwater/well/6837203

Umphres, G.D., and Choi, N.J. 2025. Estimated Annual Recharge to the Edwards Aquifer in the San Antonio Area, by Stream Basin or Ungaged Area, 1934–2024. U.S. Geological Survey data release. https://doi.org/10.5066/P1BI62NY

U.S. Geological Survey. National Water Information System, site 08168710, Comal Springs at New Braunfels, Texas.

Zhu, Q., Zhu, Y., Niu, J., Huang, J., Huang, F., Zhou, X., Liu, D., and Hu, B.X. 2026. Benchmarking machine learning and deep learning models for groundwater level prediction in karst aquifers: The dominant role of hydrogeological complexity. *Water* 18, no. 8: 939.
