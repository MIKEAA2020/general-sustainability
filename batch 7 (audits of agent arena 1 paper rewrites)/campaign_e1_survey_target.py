#!/usr/bin/env python3
"""
campaign_e1_survey_target.py
----------------------------
Second empirical object (Spec C) for paper E1: the frozen five-module ladder
scored against the RV fall survey abundance index (monitoring series) instead
of the assessment reconstruction.

Design frozen in SPEC_E1_SURVEY_TARGET_20260918.md before any score was read.

Inputs  : wave_e_cod/data/rv_fall_abundance_schijns_table3.csv (1983-2015)
          wave_e_cod/data/catch_schijns_2021.csv (annual landings)
          wave_e_cod/src/run_ladder.py          (engine, imported unmodified)
Outputs : results/e1_survey_target_rolling_forecasts.csv
          results/e1_survey_target_rolling_summary.csv
          results/e1_survey_target_fixed_window_scores.csv
          results/e1_survey_dm_uncertainty.csv

Deterministic (seed 0, 20,000 replications - same DM/bootstrap conventions as
the registered E1/E3 layers). Engine fidelity is asserted against the frozen
Spec A values before any survey value is written.
"""
import os, sys, json
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
SRC = os.path.join(WS, "wave_e_cod", "src")
sys.path.insert(0, SRC)
import run_ladder as RL  # engine reused unmodified

OUT = os.path.join(HERE, "results")
os.makedirs(OUT, exist_ok=True)

DATA = RL.DATA
target = pd.read_csv(DATA / "rv_fall_abundance_schijns_table3.csv")
years = target["year"].to_numpy()
assert list(years) == list(range(1983, 2016)), "series must be continuous 1983-2015"

ssb_tab = pd.read_csv(DATA / "ncam_2016_table_a2.csv")
merged = target.merge(ssb_tab[["year", "ssb_kt"]], on="year")
Q = float(np.median(merged["ssb_kt"] / merged["rv_abundance_index"]))
T = Q * target["rv_abundance_index"].to_numpy(dtype=float)

# Spec A catch series on the same year grid
c_reg = np.where(years <= 1991, 240.0, np.where(years == 1992, 120.0, 5.0)).astype(float)
cat = pd.read_csv(DATA / "catch_schijns_2021.csv")
c_ann = cat.set_index("year").loc[years, "catch_kt"].to_numpy(dtype=float)

NOLRP = np.nan  # C.3.1: no normative threshold; brier column not computed/used

# ---------- C.5.1 engine fidelity proof against frozen Spec A values ----------
ssb = ssb_tab["ssb_kt"].to_numpy(dtype=float)
lrp = float(np.mean(ssb[(ssb_tab["year"].to_numpy() >= 1983) & (ssb_tab["year"].to_numpy() <= 1989)]))
df_a, sum_a = RL.run_rolling(ssb_tab["year"].to_numpy(), ssb, c_reg, lrp)
frozen = {("M2_stockflow_regimeC", 1): 144.09, ("naive_persist", 1): 98.05}
naive_a, _ = RL.naive_baselines(ssb_tab["year"].to_numpy(), ssb, lrp)
guard = []
for (mod, h), exp in frozen.items():
    got = None
    if mod.startswith("naive"):
        got = naive_a[(naive_a.model == mod) & (naive_a.horizon == h)]
    else:
        got = df_a[(df_a.model == mod) & (df_a.horizon == h)]
    got = float(np.sqrt(got.sqerr.mean()))
    guard.append((mod, h, exp, round(got, 2)))
    assert abs(got - exp) < 0.05, f"ENGINE FIDELITY FAIL {mod} h={h}: {got} vs frozen {exp}"

# ---------- C.2 survey scoring, both catch treatments ----------
frames, sums = [], []
for name, C in (("regime", c_reg), ("annual", c_ann)):
    df_c, sum_c = RL.run_rolling(years, T, C, lrp)
    df_c.insert(0, "catch", name); sum_c.insert(0, "catch", name)
    frames.append(df_c); sums.append(sum_c)
df_n, sum_n = RL.naive_baselines(years, T, lrp)
sum_n.insert(0, "catch", "naive")

roll = pd.concat(frames, ignore_index=True)
roll.to_csv(os.path.join(OUT, "e1_survey_target_rolling_forecasts.csv"), index=False)
summ = pd.concat(sums + [sum_n], ignore_index=True)
summ = summ.drop(columns=["brier"], errors="ignore")
summ.to_csv(os.path.join(OUT, "e1_survey_target_rolling_summary.csv"), index=False)

fw_a, _ = RL.run_fixed_windows(years, T, c_reg, lrp)
fw_b, _ = RL.run_fixed_windows(years, T, c_ann, lrp)
fw_a.insert(0, "catch", "regime"); fw_b.insert(0, "catch", "annual")
pd.concat([fw_a, fw_b], ignore_index=True).to_csv(
    os.path.join(OUT, "e1_survey_target_fixed_window_scores.csv"), index=False)

# ---------- C.5.3 origin-set equality ----------
org1 = sorted(set(roll[roll.horizon == 1].origin))
org5 = sorted(set(roll[roll.horizon == 5].origin))
assert org1 == list(range(1990, 2015)) and org5 == list(range(1990, 2011)), (org1[:3], org1[-3:])

# ---------- DM + moving-block bootstrap (frozen conventions) ----------
NB, SEED = 20000, 0

def dm_hac(lossdiff, horizon):
    d = lossdiff.values
    n = len(d)
    lag = max(horizon - 1, 0)
    x = d - d.mean()
    g0 = float((x @ x) / n)
    gam = np.array([float((x[:-k] @ x[k:]) / n) for k in range(1, lag + 1)]) if lag > 0 else np.array([])
    s2 = g0 + 2 * gam.sum()
    dm = d.mean() / np.sqrt(s2 / n)
    return float(dm)

def block_boot(gap, block, nboot=NB, seed=SEED):
    rng = np.random.default_rng(seed)
    n = len(gap)
    means, obs = [], float(gap.mean())
    for b in range(nboot):
        starts = rng.integers(0, n - block + 1, size=(n + block - 1) // block)
        samp = np.concatenate([gap[s:s + block] for s in starts])[:n]
        means.append(samp.mean())
    means = np.sort(means)
    lo, hi = np.percentile(means, [2.5, 97.5])
    p = float(np.mean(np.sign(means) != np.sign(obs))) if obs != 0 else 0.0
    # one-sided empirical tail vs zero
    p_one = float(np.mean(np.array(means) >= 0)) if obs < 0 else float(np.mean(np.array(means) <= 0))
    return float(lo), float(hi), min(2 * p_one, 1.0)

rows = []
base = df_n[(df_n.model == "naive_persist")]
for name in ("regime", "annual"):
    c = roll[roll["catch"] == name]
    for mod in sorted(set(c.model)):
        for h in (1, 5):
            a = c[(c.model == mod) & (c.horizon == h)]
            b = base[base.horizon == h]
            comp = a.merge(b, on="origin", suffixes=("_m", "_p"))
            lm = np.log(np.maximum(comp.pred_m, 1e-3)) - np.log(np.maximum(comp.obs_m, 1e-3))
            # squared error loss differential on raw scale (frozen convention: sq error)
            ldiff = comp.sqerr_m - comp.sqerr_p
            z = dm_hac(ldiff, h)
            lo_, hi_, p_ = block_boot(ldiff.to_numpy(), max(h, 3))
            rows.append(dict(catch=name, model=mod, horizon=h, n=len(comp),
                             rmse_module=float(np.sqrt(comp.sqerr_m.mean())),
                             rmse_persist=float(np.sqrt(comp.sqerr_p.mean())),
                             gap=float(ldiff.mean()), DM_z=z,
                             block=max(h, 3), ci95_lo=lo_, ci95_hi=hi_, p_bootstrap=p_))
dm = pd.DataFrame(rows)
dm.to_csv(os.path.join(OUT, "e1_survey_dm_uncertainty.csv"), index=False)
print(dm.to_string(index=False))
print("guard:", guard, "| q#:", round(Q, 6), "| origins h1/h5 n =", len(org1), "/", len(org5))
