# Wave E — Edwards San Antonio Pool. Frozen protocol

**Locked 2026-08-25.** Retention is decided only after this file exists.
This is not a clinical preregistration. It is a computational protocol written
before scores were generated.

## Protocol sentence (frozen)

Model retention is decided solely by held-out scores on the declared basin
state \(z\). Any out-of-assessment \(Y\) is a post-selection robustness check
and cannot promote a module.

## One object

| Field | Contents | Type |
|---|---|---|
| \(S\) | Edwards Aquifer, San Antonio Pool, as indexed by well J-17 | D |
| \(z_t\) | Calendar-year mean of daily-high J-17 elevation, ft AMSL | D |
| Well | TWDB 6837203 / EAA AY-68-37-203 / J-17, Bexar County | D |
| \(B\) | San Antonio Pool management region; calendar years 1934–2023 | D |
| \(I\) | Continuity of a confined-head index that can occupy the safe side of a declared \(K^*\) | N |
| \(K^*_{\mathrm{phys}}\) | Head high enough that Comal Springs do not cease (\(\approx 618\) ft AMSL; 1956 observed daily min \(612.51\)) | N / E |
| \(K^*_{\mathrm{inst}}\) | EAA San Antonio Pool Stage I: 10-day mean J-17 \(< 660\) ft AMSL (post-2007 rule) | N |
| \(W\) | Recharge (estimated), unmodeled karst/conduit, Uvalde–SA pool exchange | M |
| \(U_{\mathrm{theoretical}}\) | Any nonnegative pumping schedule | M |
| \(U_{\mathrm{implementable}}\) | Pre-EAA unregulated pumping; post-1996/2007 permit + CPM reductions | E |
| \(T\) | Hindcast 1934–2023; four fixed windows + rolling origin | D |
| Fibre \(Y\) | USGS 08168710 Comal Springs annual mean discharge (cfs) | D |
| Not \(z\) | GRACE/G3P, MODFLOW/GWSIM heads, EAA reconstructed storage, J-27, San Marcos | D |

J-17 is a **measured well**, not an assessment inversion. TWDB transcribes EAA
feet AMSL to feet below land surface with land-surface elevation 731 ft; the
AMSL column in the TWDB file is the management unit and is the predictand.

Annual mean uses all available daily highs that year. Years with fewer than
240 daily values are dropped. 1935 (\(n=258\)) and 1939 (\(n=242\)) are
retained as incomplete-coverage means. Missing days are **not** interpolated.

The published J-17 record before continuous on-site logging (literature:
Beverly Lodges well used to extend J-17 to 1932) is used as the official
composite. It is not re-spliced here. **[E]**

## What is not the primary

- Phosphorus is not this \(\Omega\). Two \(\Omega\), two papers.
- J-27 (Uvalde Pool) is a different pool.
- Comal Springs is \(Q_{\mathrm{eco}}\), an A005 service, not \(z\).
- Total spring discharge from EAA Table 1 is **not** a driver (endogenous).
- USGS recharge is a Puente (1978) stream-loss **estimate**. It is a driver,
  not \(z\). It is independent of J-17 (gaged losing streams + NEXRAD rainfall).
- Well pumpage is reported + estimated unreported use. Driver, not \(z\).

## Ladder (causal)

Issued at the end of year \(t\). Known: \(H_s, R_s, P_s\) for \(s\le t\).
Unknown: \(R_{t+1},\ldots\) and \(P_{t+1},\ldots\).

Discrete one-pool map **[M]**, H0 of A005:

\[
H_{t+1}=\bigl[H_t+\alpha+\beta \tilde R_{t+1}+\gamma \tilde P_{t+1}+\delta H_t\bigr]_{[H_{\mathrm{dry}},H_{\mathrm{cap}}]}
\]

with \(H_{\mathrm{dry}}=610\), \(H_{\mathrm{cap}}=710\) ft AMSL.

| ID | Rung | \(\tilde R,\tilde P\) | Notes |
|---|---|---|---|
| naive_persist | baseline | — | \(\hat H_{t+h}=H_t\) |
| naive_mean | baseline | — | training mean |
| M1 | output / autonomous | — | \(H_{t+1}=a+\varphi H_t\) |
| M2 | stock-flow, causal | last observed \((R_t,P_t)\) persisted | one-pool water balance |
| M2m | stock-flow, causal | training-mean \((R,P)\) | climatological fluxes |
| M3 | disturbance | as M2 | M2 + AR(1) residual on \(\Delta H\) |
| M4 | delay | as M2 | start from \(H_{t-1}\) |
| M2_oracle | **diagnostic only** | realized future \(R,P\) | cannot retain |

Oracle M2 is the analogue of “known catch” in the cod paper. Recharge is
weather, not a control, so oracle skill is a **certificate** about the
balance class, not a forecast win.

## Scores (frozen)

**Primary:** RMSE of annual-mean J-17, feet AMSL.

**Secondary:** MAE; Brier for \(\mathbf{1}\{\hat H<660\}\) (annual-mean proxy
for Stage I, **not** the 10-day rule); sign-hit of \(\Delta H\) on fixed
windows. Brier on 660 is interpreted only for origins \(\ge 2007\).

**Fixed windows**

1. DOR drawdown: train 1934–1950, test 1951–1956.
2. DOR recovery: train 1934–1956, test 1957–1961.
3. Pre-permit wet: train 1980–1990, test 1991–1995.
4. CPM era: train 1997–2014, test 2015–2023.

**Rolling:** minimum 15 training years; horizons \(h=1\) and \(h=5\);
complete panel 1934–2023 only.

**Retention.** A causal module is retained only if it reduces **primary**
RMSE relative to the next-simpler causal model **and** relative to
`naive_persist`. Oracle results cannot promote a module. Fibre results
cannot promote a module.

## Fibre (after freeze)

Fit \(Q^{\mathrm{Comal}}=c_0+c_1 H\) once on 1934–1950.
Push frozen \(\hat H\) forecasts through that map.
Report Comal RMSE. Do not change retain/reject.

Eastern-basin recharge \(R_{\mathrm{east}}=\) basins 5+6+7+9 is stored and
not used for selection.

## R04 status for this object

The full A005 two-pool module remains **conditionally admissible**
(V-A005-04…11). This paper uses an H0 one-pool discrete map as an
`APPROXIMATION` (R04.Cor2). See `admission/R04_Cor2_edwards_H0.md`.

No kernel, no set-valued \(B_k\), no claim that two-pool leakage is
identified.
