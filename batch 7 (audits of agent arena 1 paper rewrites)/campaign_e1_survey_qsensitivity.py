#!/usr/bin/env python3
"""
campaign_e1_survey_qsensitivity.py
----------------------------------
Q-flag sensitivity for Spec C: is every verdict invariant to the deterministic
kt-E conversion q# = median(SSB_t/I_t)? Rescale the target by the interquartile
bounds of the SSB/I ratio (p25, median, p75) and re-score the full ladder
(annual-landings treatment). Note: exact scale equivariance is NOT guaranteed -
the optimizer K-bounds move with q - so margins are checked empirically.
Output: results/e1_survey_qsensitivity.csv  (deterministic: no randomness)
"""
import os, sys
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(WS, "wave_e_cod", "src"))
import run_ladder as RL

DATA = RL.DATA
target = pd.read_csv(DATA / "rv_fall_abundance_schijns_table3.csv")
years = target["year"].to_numpy()
ssb_tab = pd.read_csv(DATA / "ncam_2016_table_a2.csv")
merged = target.merge(ssb_tab[["year", "ssb_kt"]], on="year")
ratio = merged["ssb_kt"] / merged["rv_abundance_index"]
qs = {"p25": float(np.quantile(ratio, 0.25)),
      "p50_med": float(np.median(ratio)),
      "p75": float(np.quantile(ratio, 0.75))}
cat = pd.read_csv(DATA / "catch_schijns_2021.csv")
c_ann = cat.set_index("year").loc[years, "catch_kt"].to_numpy(dtype=float)

rows = []
I = target["rv_abundance_index"].to_numpy(dtype=float)
for tag, q in qs.items():
    T = q * I
    df_s, _ = RL.run_rolling(years, T, c_ann, np.nan)
    df_n, _ = RL.naive_baselines(years, T, np.nan)
    base = df_n[(df_n.model == "naive_persist")]
    for mod in sorted(set(df_s.model)):
        for h in (1, 5):
            a = df_s[(df_s.model == mod) & (df_s.horizon == h)]
            b = base[base.horizon == h]
            comp = a.merge(b, on="origin", suffixes=("_m", "_p"))
            rmse_m = float(np.sqrt(comp.sqerr_m.mean()))
            rmse_p = float(np.sqrt(comp.sqerr_p.mean()))
            rows.append(dict(q=tag, qval=q, model=mod, horizon=h,
                             rmse_module=rmse_m, rmse_persist=rmse_p,
                             margin_pct=100 * (rmse_m / rmse_p - 1)))
out = pd.DataFrame(rows)
out.to_csv(os.path.join(HERE, "results", "e1_survey_qsensitivity.csv"), index=False)
piv = out[out.horizon == 1].pivot(index="model", columns="q", values="margin_pct")
print(piv.round(3).to_string())
piv5 = out[out.horizon == 5].pivot(index="model", columns="q", values="margin_pct")
print(piv5.round(3).to_string())
print("verdict sets:", out.groupby(["q","horizon"]).apply(lambda d: (d.margin_pct<=5).sum(), include_groups=False).to_dict())
