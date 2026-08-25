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
