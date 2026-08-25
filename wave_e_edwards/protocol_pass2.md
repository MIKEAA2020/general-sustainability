# Wave E Edwards — Pass 2 protocol (frozen before scores)

**Locked 2026-08-25, after Pass 1 retention, before Pass 2 RMSE.**
Pass 1 decisions are frozen: causal persist-\((R,P)\) rejected; M1 thin retain;
M2_oracle is a certificate; fibre cannot promote.

## Question

Does a **causal** forecast of next year’s recharge, using only information
known at the end of year \(t\), reduce primary RMSE on J-17 relative to
persistence **and** relative to M1?

If it only improves the \(R\) score, it is not retained.

## Predictors (all known at origin \(t\))

| Symbol | Definition | Source |
|---|---|---|
| \(R_t\) | USGS total recharge, year \(t\) | already locked |
| \(\mathrm{SON}_t\) | Sep–Nov mean Niño 3.4 anomaly, year \(t\), minus 1991–2020 monthly climatology | PSL HadISST `nino34.long.data` |
| \(\bar P_t\) | Mean of Texas nClimDiv CD 06 (Edwards Plateau) and CD 07 (South Central) annual precipitation, inches | NCEI climdiv-pcpndv |

The 1991–2020 SST climatology is a declared NOAA-style base period, not
re-estimated on each training window. It is a function of SST only.

Sep–Nov of year \(t\) is complete on 30 November, hence at the 31 December
origin. DJF spanning January of \(t+1\) is **not** used.

## \(R\) maps (fit on the training window only)

\[
\begin{aligned}
\hat R^{\mathrm{AR}}_{t+1} &= a+\varphi R_t \\
\hat R^{\mathrm{ENSO}}_{t+1} &= a+b\,\mathrm{SON}_t \\
\hat R^{\mathrm{P}}_{t+1} &= a+c\,\bar P_t \\
\hat R^{\mathrm{X}}_{t+1} &= a+\varphi R_t+b\,\mathrm{SON}_t+c\,\bar P_t
\end{aligned}
\]

For \(h>1\), \(\hat R\) is held at the one-step value (no future SON or
precip). Pumpage remains last-value persist, as in Pass 1 M2.

Head map is the Pass 1 M2 affine law, refit on the training window, then
stepped with \(\hat R\) and persisted \(P\).

| ID | Role |
|---|---|
| M2_Rar | causal AR(1) recharge |
| M2_enso | causal SON Niño 3.4 |
| M2_precip | causal lagged climate-division rain |
| M2_combo | causal AR + SON + lagged rain |
| M2_precip_oracle | \(\tilde R_{t+k}=a+c\bar P_{t+k}\), contemporaneous rain | **cannot retain** |

M2_precip_oracle asks whether recharge is essentially rain. It is the
weather-oracle analogue of M2_oracle, not a forecast.

## Scores

Unchanged. Primary: rolling \(h=1\) RMSE of annual-mean J-17.
Secondary: \(R\)-forecast RMSE (reported, cannot retain); fibre after freeze.

Fixed windows unchanged.

## Retention

A Pass 2 module is retained only if primary RMSE \(<\) persist **and** \(<\) M1.
Oracle excluded. Fibre excluded. Improving the \(R\) score is not enough.

## What this pass is not

- Not a two-pool model.
- Not GRACE as \(z\).
- Not phosphorus.
- Not mid-year nowcast (different origin).
- Not PDO/AMO kitchen-sink.
