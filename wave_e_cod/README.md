# Wave E — scored forecast ladder (Northern cod 2J3KL)

First empirical gate of the general theory (§15 / closure Wave E).

**Pass 2:** Schijns 2021 annual catch + RV-index start state.  
Persistence still wins RMSE. Annual \(C_t\) does not rescue M2.  
Survey start helps log-RMSE slightly; not retained on primary score.  
xteNCAM SSB not pooled (table not extracted).

**Pass 6:** observed acoustic column (Zenodo 17515115), causal carry-forward.  
Still not retained (150/132 vs persist 98/88). Near-tie on 2016 five-year RMSE only.

```
python3 src/run_ladder.py
python3 src/make_figures.py
```

Do not pool this SSB column with xteNCAM (DFO 2024/25).

**Intervention leg** (§15 intervention selection; `protocol_intervention.md`, frozen before scores; `python3 src/run_intervention.py`): robust viability kernels of the LRP (884.6 kt) for a declared catch-policy family (BAU moratorium-level 5 kt / flat caps / the DFO-2009 critical-zone rule / a cascade) under persistent productivity-shock floors (UC-min/q05/q10), with the Cor2 erosion conversion in the **expansive** form (the map is expansive at the LRP: F′ = 1.153 > 1; the contraction form is inapplicable). Verdicts: **productivity negative certificate** (under UC-min/q05 no catch policy — zero included — holds the LRP: no positive fixed point exists; protected by good years, not catch management); **no policy retained** (S1/cpm are strictly less protective than BAU at the boundary — the mirror image of the Edwards positive result); maximal robust flat catch **57.6 kt** at UC-q10 (24% of the historical 240 kt); certified kernels empty beyond T = 5 yr (expansion-bound). Kernel-level Cor2 admission row `admission/R04_Cor2_cod_kernel.md` (APPROXIMATION). First run; rerun NONE.
