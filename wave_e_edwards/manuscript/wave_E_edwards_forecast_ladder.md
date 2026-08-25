# Does a one-pool water-balance ladder improve forecasts? A scored test on the Edwards Aquifer (J-17)

**Wave E empirical paper — working manuscript**
**Series lock:** J-17 annual-mean elevation, TWDB 6837203 / EAA AY-68-37-203, 1934–2023
**Status:** one scored specification \(\Omega_{\mathrm{SA}}\). Causal stock-flow is *not* earned. Causal recharge forecasts are *not* earned. Oracle water-balance is a certificate, not a retain.

---

## Abstract

The general theory of sustainability states that extra structure is justified only if it improves early warning, out-of-sample prediction, or intervention selection. This paper runs that test (Wave E) on a named groundwater basin: the Edwards Aquifer, San Antonio Pool.

The predictand \(z\) is the calendar-year mean of daily-high water elevation at the J-17 index well (ft AMSL). It is a measured well, not a MODFLOW inversion and not GRACE. Nested models issue fixed-window and rolling-origin forecasts. Recharge (USGS/Puente) and well pumpage (EAA Table 1) enter as drivers. Comal Springs discharge is an out-of-assessment fibre and is scored only after retain/reject is frozen.

**Result.** Persistence is the one-year beating target at 13.23 ft RMSE. Autonomous AR(1) (M1) is 12.84 ft: a 0.39 ft edge, recorded under the frozen point-RMSE rule and not a structural win. The honest causal stock-flow model — last year’s recharge and pumpage persisted — is **worse** than persistence (14.70 ft). Delay and AR residuals do not repair it. Recharge is nearly white noise (lag-1 \(r=0.17\)); persisting it is the wrong information pattern.

When the same map is given *realized* future recharge and pumpage (M2_oracle), one-year RMSE falls to 7.55 ft. Pass 2 asks whether that missing recharge can be forecast from information known at \(t\): AR(1) on \(R\), SON Niño 3.4, lagged climate-division rain, and the three together. Contemporaneous rain tracks \(R\) (\(r=0.78\)) and a rain-oracle head RMSE is 10.56 ft. Every *lagged* climate module is within 0.13 ft of M1 at \(h=1\) and **worse** than persist at \(h=5\). Next year’s rain is not known at \(t\). ENSO and last year’s rain are not substitutes.

No two-pool, solute, or institutional-kernel claim is made. A005 remains conditionally admissible. This object is an R04.Cor2 `APPROXIMATION`.

**Keywords:** viability; forecast ladder; Edwards Aquifer; J-17; model ablation; persistence baseline; Wave E

---

## 1. Why this paper exists

Section 15 of the general theory requires a comparative model ladder. Complexity is kept only if it improves a preregistered score. Closure Wave E is that gate. R04 prefers groundwater unless the readiness matrix fails. Edwards San Antonio Pool passes: named basin, measured \(z\), independent recharge, dated implementable \(U\), declared \(K^*\), and a measured service fibre.

Northern cod (\(\Omega_{2016}\), \(\Omega_{\mathrm{xte}}\)) already returned a negative certificate. This is a second \(\Omega\), not a pooled series. Phosphorus is not opened.

The question is one scored sentence:

> On locked J-17 annual mean head, do M2–M4 reduce forecast error relative to M1 and relative to last-value persistence?

---

## 2. Specification \(\Omega_{\mathrm{SA}}\) **[D]**

| Field | Contents | Type |
|---|---|---|
| \(S\) | Edwards Aquifer, San Antonio Pool, indexed by J-17 | D |
| \(z_t\) | Calendar-year mean of daily-high J-17 elevation, ft AMSL | D |
| Well | TWDB 6837203 / EAA AY-68-37-203 | D |
| \(B\) | San Antonio Pool; calendar years 1934–2023 | D |
| \(K^*_{\mathrm{phys}}\) | Head high enough that Comal does not cease (\(\approx 618\) ft; 1956 daily min \(612.51\)) | N / E |
| \(K^*_{\mathrm{inst}}\) | EAA Stage I, 10-day mean J-17 \(< 660\) ft (post-2007) | N |
| \(W\) | Recharge pulses; unmodeled karst; Uvalde–SA exchange | M |
| \(U_{\mathrm{implementable}}\) | Pre-EAA pumping; post-1996/2007 permits + CPM | E |
| Fibre \(Y\) | USGS 08168710 Comal Springs annual mean, cfs | D |

**Not \(z\).** GRACE/G3P, MODFLOW/GWSIM, EAA reconstructed storage, J-27 (Uvalde Pool), San Marcos Springs, total spring discharge.

**Two thresholds, not one. [N]** Stage I at 660 ft is a 2007 institutional rule. It is not applied as if it existed in 1956. Comal cessation near 618 ft is a physical service bound. Annual-mean \(\mathbf{1}\{H<660\}\) is a coarse Brier proxy, not the 10-day CPM declaration.

**Coverage. [E]** Annual mean uses all available daily highs. Years with \(n<240\) are dropped. 1935 (\(n=258\)) and 1939 (\(n=242\)) are incomplete-coverage means. Missing days are not interpolated. The published pre-continuous composite (Beverly Lodges extension) is used as official and is not re-spliced.

**2023+ J-17 status `R`** is provisional in the TWDB pull. The complete panel ends 2023.

---

## 3. Models

Discrete H0 map **[M]**, head clipped to \([610,710]\):

\[
H_{t+1}=\bigl[H_t+\alpha+\beta\tilde R_{t+1}+\gamma\tilde P_{t+1}+\delta H_t\bigr]_{\mathrm{clip}}
\]

Issued at the end of year \(t\). Known: \((H,R,P)\) through \(t\).

| ID | Rung | Fluxes used at \(t+k\) | Role |
|---|---|---|---|
| naive_persist | baseline | — | \(\hat H_{t+h}=H_t\) |
| naive_mean | baseline | — | training mean |
| M1 | output / autonomous | — | \(H_{t+1}=a+\varphi H_t\) |
| M2 | stock-flow, **causal** | last \((R_t,P_t)\) persisted | the retain candidate |
| M2m | stock-flow, climatology | training-mean \((R,P)\) | collapses to AR(1) |
| M3 | disturbance | as M2 | AR(1) residual on \(\Delta H\) |
| M4 | delay | as M2 | start from \(H_{t-1}\) |
| M2_oracle | diagnostic | realized future \(R,P\) | **cannot retain** |

\(R\) is USGS total San Antonio-area recharge (\(10^3\) acre-ft yr\(^{-1}\)), Puente (1978) stream-loss, independent of J-17. \(P\) is EAA Table 1 well discharge. Total spring discharge is stored and is **not** a driver.

M2m with constant fluxes is

\[
H_{t+1}=(1+\delta)H_t+\text{const},
\]

the same affine class as M1. A numerical edge for M2m is not extra structure.

---

## 4. Scores (frozen in `protocol.md`)

**Primary:** RMSE of annual-mean J-17, feet.

**Secondary:** MAE; Brier for \(\mathbf{1}\{\hat H<660\}\) (interpreted only for origins \(\ge 2007\)); sign-hit of \(\Delta H\) on fixed windows.

**Fixed windows**

1. DOR drawdown: train 1934–1950, test 1951–1956.
2. DOR recovery: train 1934–1956, test 1957–1961.
3. Pre-permit wet: train 1980–1990, test 1991–1995.
4. CPM era: train 1997–2014, test 2015–2023.

**Rolling:** minimum 15 training years; \(h=1,5\); \(n=75\) (\(h=1\)), \(71\) (\(h=5\)).

**Retention.** Causal module retained only if primary RMSE \(<\) persist **and** \(<\) next-simpler causal model. Oracle cannot promote. Fibre cannot promote.

---

## 5. Results

### 5.1 Locked series

![Figure 1](fig1_series.png)

**Figure 1.** J-17 annual mean and daily-high range. 1956 mean \(623.2\) ft, daily min \(612.51\) ft. 1992 mean \(692.0\) ft, daily max \(703.31\) ft. 2023 mean \(635.7\) ft. Annual mean is below 660 ft in 31 of 90 years. Daily min is below 618 ft in **one** year (1956).

### 5.2 Fixed windows

![Figure 2](fig2_windows.png)

**Figure 2.** Multi-step forecasts from the end of each training window. Oracle (dashed) is a diagnostic.

**Table 1.** Fixed-window RMSE (ft).

| Window | persist | M1 | M2 | M2m | oracle |
|---|---:|---:|---:|---:|---:|
| DOR drawdown 1951–56 | 23.75 | 30.94 | **18.11** | 27.44 | 19.69 |
| DOR recovery 1957–61 | 43.62 | 56.24 | 55.32 | 37.74 | **12.26** |
| Pre-permit wet 1991–95 | 30.13 | 20.02 | 16.67 | 23.47 | **7.18** |
| CPM era 2015–23 | 27.41 | 15.62 | 23.37 | 14.79 | **8.70** |

The 1950s drawdown is a continuing low-recharge path: last observed \(R\) is already low, so causal M2 beats persist (18 vs 24) and even beats the oracle. The linear map trained on 1934–1950 has the **wrong sign** on pumpage (\(\gamma=+0.021\)); pumping rose as the drought deepened, so the short window cannot identify a supply response.

The 1957–61 recovery is a recharge pulse (\(R_{1956}=43.7\), \(R_{1957}=1142.6\)). Persist stays at the 1956 floor (RMSE 44). Causal M2 persists the drought recharge and **falls further** (RMSE 55). Oracle, given the 1957 flood year, tracks the rise (RMSE 12). That is the mechanism result: recoveries on this \(\Omega\) are weather events, not autonomous mean reversion and not a pumping-regime event.

The 1992 peak and the 2015–23 CPM window repeat the same split. Oracle follows the recharge year. Persist cannot. Causal persist-\(R\) cannot.

### 5.3 Rolling origin

![Figure 3](fig3_rmse.png)

**Figure 3.** Rolling-origin RMSE. Oracle is excluded from retention.

**Table 2.** Rolling-origin summary (ft).

| Model | \(h=1\) RMSE | \(h=1\) MAE | \(h=5\) RMSE |
|---|---:|---:|---:|
| naive persist | 13.23 | 10.73 | 21.11 |
| naive mean | 16.17 | 13.17 | **16.80** |
| M1 AR(1) | 12.84 | 10.72 | 21.25 |
| M2 persist-\((R,P)\) | 14.70 | 11.45 | 33.49 |
| M2m mean-\((R,P)\) | 12.28 | 10.22 | 17.44 |
| M3 AR residual | 14.46 | 11.12 | 33.46 |
| M4 delayed | 14.30 | 11.17 | 33.39 |
| M2_oracle | 7.55 | 5.79 | 10.87 |

Full-sample facts that explain the ranking **[E]**:

- \(\mathrm{corr}(H_t,H_{t-1})=0.64\). Heads persist, with mean reversion (\(\hat\varphi=0.66\)).
- \(\mathrm{corr}(R_t,R_{t-1})=0.17\). Recharge is a shock. Persisting it injects noise.
- \(\mathrm{corr}(\Delta H_t,R_t)=0.74\). The water-balance class is not empty.
- Full-sample \((\hat\beta,\hat\gamma)=(0.017,-0.026)\): correct signs when the sample is long.

**Retention (primary = rolling \(h=1\) RMSE).**

| Model | vs persist | Distinct structure? | Decision |
|---|---|---|---|
| M1 | \(12.84<13.23\) | output-only | **thin retain** (0.39 ft) |
| M2 | \(14.70>13.23\) | yes (causal fluxes) | reject |
| M2m | \(12.28<13.23\) | no — affine AR(1) | numerical list only; **not extra structure** |
| M3, M4 | worse than persist | yes | reject |
| M2_oracle | \(7.55\) | uses future \(R,P\) | excluded |

M1 is retained by the frozen point-RMSE rule. The margin is 0.39 ft on \(n=75\). That is not a theory confirmation. It is a slightly mean-reverting head.

M2m is listed by the same rule and then demoted on class grounds that were already in the protocol (constant fluxes \(\Rightarrow\) AR(1)). Promoting M2m as “stock-flow earned” would be inflation.

No stock-flow, residual, or delay module is retained as a forecast improvement.

On \(h=5\), training-mean (16.80) beats persist (21.11). Five-year head forecasts on this basin are climatology, not last value and not persist-\(R\).

Post-2007 origins only (\(n=16\), \(h=1\)): persist 13.09, M1 12.16, M2 13.31, oracle 8.03. Same ranking. 660-Brier is 0.31 (persist) vs 0.25 (M1) vs 0.19 (oracle). The annual-mean proxy is not the 10-day rule.

---

## 6. Fibre, after freeze

![Figure 4](fig4_fibre.png)

**Figure 4.** Comal annual mean vs J-17. Contemporaneous \(r=0.986\). The fibre is a measured service, not an independent information source.

The observation map \(Q=c_0+c_1 H\) was fit on 1934–1950 only (\(c_0=-2876\), \(c_1=4.77\)) and applied to already-issued \(\hat H\). One-year Comal RMSE: persist 71.9 cfs, M1 69.0, M2m 68.7, M2 74.8, oracle 45.3.

The fibre does not change retain/reject. It also cannot, because it is almost a linear transform of \(z\). Calling Comal “out-of-assessment” is correct as a *measurement* (USGS spring gage, not used to construct J-17). It is not a strong *informational* robustness check. A genuine second fibre would be GRACE or J-27, and those are different \(\Omega\) or \(Y\) classes, to be run only after this freeze if at all.

Eastern-basin recharge was stored and not used.

---

## 7. What the ladder proved

These are certificates, not basin verdicts.

1. **H0 water balance is not empty [E].** \(\Delta H\) tracks recharge (\(r=0.74\)). Oracle RMSE is about half of persist at \(h=1\) and half at \(h=5\). The one-pool map has content when the year’s water is known.

2. **Causal stock-flow fails as a forecast [E].** Recharge is the dominant increment and is not persistent. M2, M3, and M4 lose to last-value head. This is the groundwater analogue of the cod result that a more accurate \(C_t\) did not rescue surplus production: the identified driver is the wrong *timing* object for a one-year forecast.

3. **Recoveries are recharge pulses [E].** 1957 and 1992 are missed by every causal model and caught by the oracle. They are not autonomous AR paths and not pumping-regime events.

4. **The 1950s crash is not a Stage I event [N/L].** 660 ft is a 2007 rule. 1956 is a physical near-cessation at Comal (annual mean springflow 32 cfs; daily J-17 min 612.51). Slack to 660 is the wrong leading indicator for 1951–56, just as the 2016 cod LRP was the wrong leading indicator for 1983–90.

5. **Two-pool, solute, and \(B_k\) are not identified.** They were not fitted. They cannot be retained. A005’s blocking list is not closed by this paper.

6. **Implementable \(U\) is visible, not scored.** Post-1997 pumpage no longer spikes with drought the way 1956 did (321 kaf wells). That is in \(P_t\). Making CPM a separate M4 switch does not add a degree of freedom beyond the pumpage series.

---

## 8. Limitations (typed)

- **[M]** One-pool annual affine map is not a karst model. Conduits, the Uvalde–SA divide, and unconfined recharge-zone storage are in the residual.
- **[E]** Total-area \(R\) and \(P\) mix San Antonio and Uvalde pools. That is a declared APPROXIMATION defect, not a hidden one.
- **[E]** Recharge is a Puente estimate. Pumpage includes unreported domestic/livestock/federal use. Neither is \(z\).
- **[M]** M4 is a one-year information delay, not an R02 conservative filter.
- **[N]** Brier on annual-mean 660 is not EAA’s 10-day CPM classifier.
- **[E]** \(n=90\) years, four short test windows. The 0.39 ft M1 edge is not a significance claim.
- **[E]** 2023 J-17 values include provisional `R` status.
- This pass was executed after `protocol.md` was written. It is a computational protocol, not a locked clinical preregistration.

---

## 9. Relation to the programme

**Wave E support rule.** No gate is treated as closed for Wave E without
spec matching and independent verification. \(\Omega_{\mathrm{SA}}\) is
an R04.Cor2 `APPROXIMATION` of A005 H0. It does not confirm E5
interval-verified admission, E7 sandwiches, Stackelberg, or a frozen
TCS-1.1. See `https://github.com/MIKEAA2020/general-sustainability`
(`PROOF_MANIFEST.md`, `HONEST_DISCLOSURE.md`) and
`batch 2/04_open_problems/D_TIER_EMPIRICAL_AGENDA.md`.
E5 is not this \(\Omega\).

| Programme object | Role here |
|---|---|
| §15 / Wave E | The test that was run |
| R04 / E1 | Groundwater preferred; Edwards passes readiness; phosphorus not opened |
| R04.Cor2 | This map is `APPROXIMATION` of A005 H0. Two-pool A005 stays conditional |
| A005 | \(q_{\mathrm{rel}}\) removed; leakage N/A; no \(B_k\); \(\chi\) removed |
| R03 | Extra modules stay descriptive without a certificate |
| R02 | Closed-loop filter not fitted |
| A014 / \(\Omega_{2016}\), \(\Omega_{\mathrm{xte}}\) | Previous Wave E object. Not pooled |
| A004 | Not this paper |

The honest reading of “incorporate all the pieces for accurate forecasts” on this case: **the pieces that are not identified, or that arrive too late to be causal, do not go in.** Persistence (plus a thin AR(1)) is the present forecast. The water-balance map is a certificate about a year whose recharge is already known.

---

## 10. What not to do next

- Do not open a phosphorus paper in parallel.
- Do not promote GRACE, J-27, or Comal into co-primary predictands.
- Do not close A005’s two-pool blocking list with this affine map.
- Do not write an aggregator / extinction / species-intelligence companion.
- Pass 2 ran the causal recharge module. It is not retained as structure. Do not reopen it with more indices (PDO, AMO) on this annual origin.
- A mid-year nowcast (different origin) or a true seasonal rainfall forecast product would be a new protocol, not a silent add-on.

---

## 11. Conclusion

Wave E on Edwards San Antonio Pool does not award the general theory a stock-flow forecast win. Last-value persistence is more accurate than a causal one-pool balance that persists last year’s recharge. Autonomous AR(1) is a 0.39 ft trim, not a new architecture. The same balance, given realized recharge, cuts error nearly in half. That is the threshold. It is not the side: the paper does not say the aquifer is unsustainable, and it does not say the theory is empirically confirmed.

The next article is not a second \(\Omega\), not phosphorus, and not a longer climate kitchen-sink on this annual origin. Pass 2 closed the only stock-flow addition that could have changed the primary score without future rain. What remains is either a different origin (seasonal nowcast) under a new protocol, or nothing.

---

## 12. Pass 2 — causal recharge, same \(z\)

Protocol: `protocol_pass2.md`, written after Pass 1 retention and before these RMSE numbers.

Information known at 31 December of year \(t\): \(R_t\), Sep–Nov Niño 3.4 anomaly of year \(t\) (HadISST, 1991–2020 base), and calendar-year precipitation in Texas climate divisions 06 and 07. DJF that includes January of \(t+1\) is not used. For \(h>1\), \(\hat R\) is held at the one-step value.

![Figure 5](fig5_pass2.png)

**Figure 5.** Pass 2 rolling RMSE on J-17. The rain oracle uses year \(t+h\) precipitation and cannot retain.

**Table 3.** Rolling RMSE, Pass 2.

| Model | \(H\) \(h=1\) | \(H\) \(h=5\) | \(R\) \(h=1\) (kaf) |
|---|---:|---:|---:|
| persist \(H\) / persist \(R\) | 13.23 | **21.11** | 702 |
| M1 | 12.84 | 21.25 | — |
| M2_Rar | 13.25 | 25.38 | 561 |
| M2_enso | 12.82 | 24.42 | 528 |
| M2_precip | 12.80 | 25.38 | 545 |
| M2_combo | 12.71 | 26.88 | 538 |
| rain climatology | — | — | 556 |
| rain oracle | 10.56 | 16.91 | **354** |

Same-year \(\mathrm{corr}(R,\bar P)=0.78\). That is why the rain oracle has content (H RMSE 10.56; still worse than the full \(R,P\) oracle 7.55, because the linear rain map misses 1957-scale extremes).

Lagged rain and SON have a little skill on \(R\) versus climatology (528–545 vs 556 kaf). They do not have skill as *forecast structure* on \(z\):

- Frozen point-RMSE rule lists ENSO, lagged rain, and combo (each \(<\) persist and \(<\) M1).
- Margins vs M1 are **0.02, 0.04, and 0.13 ft**.
- At \(h=5\) all three lose to persist by 3–6 ft.
- They are M2m with a weakly adjusted intercept. Promoting them is inflation.

M2_Rar loses at \(h=1\) (13.25). AR on a nearly white \(R\) is not a recharge forecast.

Fixed windows: no causal Pass 2 module beats persist on the 1957–61 recovery (persist 43.6; best causal ~48.8; rain oracle 33.7). SON in 1956 is La Niña (\(-0.92\)). It does not announce \(R_{1957}=1143\).

**Retention, Pass 2:** no causal recharge module is retained as extra structure. The rain oracle is excluded by protocol.

Pass 1’s diagnosis stands: the missing object is next year’s water, and it is not available at the annual origin.

---

## Data and code

```
wave_e_edwards/
  protocol.md
  protocol_pass2.md
  src/build_panel.py
  src/build_climate.py
  src/run_ladder.py
  src/run_recharge.py
  src/make_figures.py
  results/pass2_H_summary.csv
  manuscript/fig5_pass2.{png,svg}
```

Reproduce:

```
python3 src/build_panel.py && python3 src/build_climate.py
python3 src/run_ladder.py && python3 src/run_recharge.py
python3 src/make_figures.py
```

---

## References

Edwards Aquifer Authority. 2024/25. *2023 Groundwater Discharge and Usage*. Table 1, after USGS letter report 5 April 2024. https://www.edwardsaquifer.org/wp-content/uploads/2025/05/2023-Groundwater-Discharge-and-Usage.pdf

Edwards Aquifer Authority. Critical Period / Drought Management. https://www.edwardsaquifer.org/groundwater-users/critical-period-drought-management/

Puente, C. 1978. *Method of estimating natural recharge to the Edwards Aquifer in the San Antonio area, Texas.* USGS.

Texas Water Development Board. Water Data for Texas, well 6837203 (J-17). https://waterdatafortexas.org/groundwater/well/6837203

Umphres, G. D., and Choi, N. J. 2025. Estimated Annual Recharge to the Edwards Aquifer in the San Antonio Area, by Stream Basin or Ungaged Area, 1934–2024. USGS data release. https://doi.org/10.5066/P1BI62NY

USGS. National Water Information System, site 08168710, Comal Springs at New Braunfels, TX.

Internal programme documents cited by ID: general theory §15; R03; R04; A005 revised; closure review Wave E; `wave_e_cod` \(\Omega_{2016}\) / \(\Omega_{\mathrm{xte}}\).
