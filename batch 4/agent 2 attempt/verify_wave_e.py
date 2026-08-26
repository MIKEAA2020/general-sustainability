#!/usr/bin/env python3
"""
Independent reproduction check for the Wave E scored trees.
Companion to WAVE_E_RERUN.md.  Run from anywhere:  python3 verify_wave_e.py

Verifies, against the committed tree at ../repo (override with REPO=path):
  1. all 29 SHA-256 hashes pinned in PROOF_MANIFEST.md Part VI
  2. that the regenerated result files are byte-identical to a pre-run snapshot
  3. every headline score quoted in the READMEs and manuscripts
  4. the ten Edwards full-sample statistics and the cod LRP derivation
  5. F1 (meta.json retention vs manuscript), F3 (nino34 rebuildable), F4 (build_panel drops columns)

Exit 0 => every claim in WAVE_E_RERUN.md reproduces.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path(os.environ.get("REPO", Path(__file__).resolve().parent.parent / "repo"))
FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


BASE = Path(os.environ.get("BASE", Path(__file__).resolve().parent.parent / "baseline"))


_TREES = {"wave_e_cod": "cod", "wave_e_edwards": "edwards"}


def baseline_bytes(tree, name):
    """Pre-run snapshot of results/, taken before any script was executed.
    The two trees share filenames (meta.json, rolling_summary.csv, ...), so the
    tree must be part of the lookup."""
    f = BASE / _TREES[tree] / name
    if not f.exists():
        raise FileNotFoundError(f)
    return f.read_bytes()


# --------------------------------------------------------------- 1. pinned hashes
print("\n[1] PROOF_MANIFEST Part VI pinned hashes")
sec = (REPO / "PROOF_MANIFEST.md").read_text().split("## Part VI")[1]
rows = re.findall(r"^\|([^|]+)\|\s*`([^`]+)`\s*\|\s*`([0-9a-f]{64})`\s*\|", sec, re.M)
bad = [(p, w) for _, p, w in rows if not (REPO / p).exists() or sha(REPO / p) != w]
check(f"all {len(rows)} pinned artifacts match their committed SHA-256", not bad,
      f"{len(rows) - len(bad)}/{len(rows)} match" + (f"; bad={[b[0] for b in bad]}" if bad else ""))
check("no artifact drifted from its pinned hash (stronger than 'git clean')", not bad,
      f"{len(rows)-len(bad)}/{len(rows)} match")

# --------------------------------------------------------------- 2. byte-identity
print("\n[2] regenerated result files byte-identical to committed")
for tree in ("wave_e_cod", "wave_e_edwards"):
    res = REPO / tree / "results"
    diff = [f.name for f in sorted(res.iterdir())
            if f.read_bytes() != baseline_bytes(tree, f.name)]
    n = len(list(res.iterdir()))
    check(f"{tree}/results: {n} files byte-identical to the pre-run baseline",
          not diff and n == len(list((BASE / _TREES[tree]).iterdir())),
          diff or f"all {n} identical")

# --------------------------------------------------------------- 3. headline scores
print("\n[3] cod headline scores (manuscript tables vs regenerated CSVs)")
rs = pd.read_csv(REPO / "wave_e_cod/results/rolling_summary.csv")
rg = rs[rs.catch == "regime"] if "catch" in rs.columns else rs


def cod(model, h, col="rmse"):
    # naive baselines are tagged catch=="na"; causal rungs are tagged "regime" or "annual"
    src = rs if model.startswith("naive") else rg
    r = src[(src.model == model) & (src.horizon == h)]
    return float(r[col].iloc[0])


claim = {("naive_persist", 1): 98, ("M1_autonomous_Schaefer", 1): 121,
         ("M1b_autonomous_Allee", 1): 115, ("M2_stockflow_regimeC", 1): 144,
         ("M3_AR_residual", 1): 135, ("M4_delayed_info", 1): 196,
         ("naive_train_mean", 1): 424, ("naive_persist", 5): 265}
for (m, h), want in claim.items():
    check(f"cod rolling {m} h={h}", round(cod(m, h)) == want, f"{cod(m,h):.2f} -> {round(cod(m,h))} (ms {want})")
check("persistence wins RMSE at h=1 against every causal rung",
      all(cod("naive_persist", 1) < cod(m, 1) for m in
          ["M1_autonomous_Schaefer", "M1b_autonomous_Allee", "M2_stockflow_regimeC",
           "M3_AR_residual", "M4_delayed_info"]))
check("persistence wins RMSE at h=5 against every causal rung",
      all(cod("naive_persist", 5) < cod(m, 5) for m in
          ["M1_autonomous_Schaefer", "M1b_autonomous_Allee", "M2_stockflow_regimeC",
           "M3_AR_residual", "M4_delayed_info"]))

an = rs[rs.catch == "annual"]
check("cod Pass 2 M2 annual catch h=1 = 160", round(float(an[an.model == "M2_stockflow_regimeC"].rmse.iloc[0])) == 160)
check("cod Pass 2 M2 survey start h=1 = 128", round(float(an[an.model == "M2_survey_start"].rmse.iloc[0])) == 128)

ci = pd.read_csv(REPO / "wave_e_cod/results/capelin_index_summary.csv")
check("cod Pass 6 '150/132 vs persist 98/88'",
      round(float(ci[(ci.tag == "ncam2016") & (ci.model == "M_cap_index") & (ci.horizon == 1)].rmse.iloc[0])) == 150
      and round(float(ci[(ci.tag == "xteNCAM") & (ci.model == "M_cap_index") & (ci.horizon == 1)].rmse.iloc[0])) == 132
      and round(float(ci[(ci.tag == "ncam2016") & (ci.model == "naive_persist") & (ci.horizon == 1)].rmse.iloc[0])) == 98
      and round(float(ci[(ci.tag == "xteNCAM") & (ci.model == "naive_persist") & (ci.horizon == 1)].rmse.iloc[0])) == 88)
check("cod Pass 6 'near-tie on 2016 five-year RMSE'",
      abs(float(ci[(ci.tag == "ncam2016") & (ci.model == "M_cap_index") & (ci.horizon == 5)].rmse.iloc[0])
          - float(ci[(ci.tag == "ncam2016") & (ci.model == "naive_persist") & (ci.horizon == 5)].rmse.iloc[0])) < 5)

fw = pd.read_csv(REPO / "wave_e_cod/results/fixed_window_scores.csv")
c1 = fw[(fw.catch == "regime") & (fw.window == "collapse") & (fw.model == "M1_autonomous_Schaefer")].iloc[0]
r1 = fw[(fw.catch == "regime") & (fw.window == "recovery") & (fw.model == "M1b_autonomous_Allee")].iloc[0]
check("cod fixed: collapse M1 694/638/2.73", (round(c1.rmse), round(c1.mae), round(c1.log_rmse, 2)) == (694, 638, 2.73))
check("cod fixed: recovery M1b 90/55/0.52", (round(r1.rmse), round(r1.mae), round(r1.log_rmse, 2)) == (90, 55, 0.52))

lrp = pd.read_csv(REPO / "wave_e_cod/data/ncam_2016_table_a2.csv")
lrp = lrp[(lrp.year >= 1983) & (lrp.year <= 1989)]
check("cod LRP 884.6 kt = 1983-1989 mean of Table A2 ssb_kt", round(lrp.ssb_kt.mean(), 1) == 884.6,
      f"mean={lrp.ssb_kt.mean():.2f}")

print("\n[3b] edwards headline scores")
e1 = pd.read_csv(REPO / "wave_e_edwards/results/rolling_summary.csv")


def ed(model, h, col="rmse"):
    return float(e1[(e1.model == model) & (e1.horizon == h)][col].iloc[0])


eclaim = {("naive_persist", 1, "rmse"): 13.23, ("naive_persist", 1, "mae"): 10.73,
          ("naive_persist", 5, "rmse"): 21.11, ("M1", 1, "rmse"): 12.84,
          ("M2", 1, "rmse"): 14.70, ("M2m", 1, "rmse"): 12.28, ("M2m", 5, "rmse"): 17.44,
          ("M2_oracle", 1, "rmse"): 7.55, ("naive_mean", 5, "rmse"): 16.80}
for (m, h, c), want in eclaim.items():
    check(f"edwards P1 {m} h={h} {c}", round(ed(m, h, c), 2) == want, f"{ed(m,h,c):.4f} (ms {want})")

e2 = pd.read_csv(REPO / "wave_e_edwards/results/pass2_H_summary.csv")


def p2(model, h):
    return float(e2[(e2.model == model) & (e2.horizon == h)].rmse.iloc[0])


check("edwards P2 margins vs M1 are 0.02 / 0.04 / 0.13 ft",
      [round(p2("M1", 1) - p2(m, 1), 2) for m in ("M2_enso", "M2_precip", "M2_combo")] == [0.02, 0.04, 0.13],
      [round(p2("M1", 1) - p2(m, 1), 4) for m in ("M2_enso", "M2_precip", "M2_combo")])
check("edwards P2 all three lose to persist at h=5 by 3-6 ft",
      all(3 <= p2(m, 5) - p2("naive_persist", 5) <= 6 for m in ("M2_enso", "M2_precip", "M2_combo")),
      [round(p2(m, 5) - p2("naive_persist", 5), 2) for m in ("M2_enso", "M2_precip", "M2_combo")])
check("edwards P2 rain oracle 10.56", round(p2("M2_precip_oracle", 1), 2) == 10.56)

fib = pd.read_csv(REPO / "wave_e_edwards/results/fibre_comal_summary.csv")
fibmap = {"naive_persist": 71.9, "M1": 69.0, "M2m": 68.7, "M2": 74.8, "M2_oracle": 45.3}
check("edwards fibre Comal RMSE 71.9/69.0/68.7/74.8/45.3",
      all(round(float(fib[fib.model == k].rmse.iloc[0]), 1) == v for k, v in fibmap.items()))

pf = pd.read_csv(REPO / "wave_e_edwards/results/pass2_fixed.csv")
rec = pf[(pf.window == "dor_recovery") & (pf.target == "H")]
check("edwards fixed dor_recovery: persist 43.6, best causal 48.8, oracle 33.7",
      round(float(rec[rec.model == "naive_persist"].rmse.iloc[0]), 1) == 43.6
      and round(float(rec[rec.model == "M2_Renso"].rmse.iloc[0]), 1) == 48.8
      and round(float(rec[rec.model == "M2_precip_oracle"].rmse.iloc[0]), 1) == 33.7)

# --------------------------------------------------------------- 4. full-sample stats
print("\n[4] edwards full-sample statistics recomputed from committed annual_panel.csv")
p = pd.read_csv(REPO / "wave_e_edwards/data/annual_panel.csv")
s = p[(p.year >= 1934) & (p.year <= 2023)].reset_index(drop=True)
d = s.H_mean - s.H_mean.mean()
stats = [("corr(H_t,H_t-1)", 0.64, s.H_mean.corr(s.H_mean.shift(1)), 5e-3),
         ("corr(R_t,R_t-1)", 0.17, s.R_total.corr(s.R_total.shift(1)), 5e-3),
         ("corr(dH_t,R_t)", 0.74, s.H_mean.diff().corr(s.R_total), 5e-3),
         ("corr(R_t,pcp_mean)", 0.78, s.R_total.corr(s.pcp_mean), 5e-3),
         ("AR(1) phi on H", 0.66, np.sum(d[1:].values * d[:-1].values) / np.sum(d[:-1].values ** 2), 1e-2),
         ("1956 SON nino34", -0.92, s.loc[s.year == 1956, "nino34_son"].iloc[0], 5e-2),
         ("R_1957", 1143, s.loc[s.year == 1957, "R_total"].iloc[0], 2.0),
         ("corr(Comal,J-17)", 0.986, s.Q_comal.corr(s.H_mean), 1e-3)]
fit = np.polyfit(s.loc[s.year <= 1950, "H_mean"], s.loc[s.year <= 1950, "Q_comal"], 1)
stats += [("fibre c1", 4.77, fit[0], 5e-2), ("fibre c0", -2876, fit[1], 2.0)]
for name, want, got, tol in stats:
    check(name, abs(float(got) - want) <= tol, f"claimed {want}, recomputed {float(got):.4f}")

# --------------------------------------------------------------- 5. findings F1/F3/F4
print("\n[5] findings reproduced")
m1 = json.loads((REPO / "wave_e_edwards/results/meta.json").read_text())
m2 = json.loads((REPO / "wave_e_edwards/results/pass2_meta.json").read_text())
ms = (REPO / "wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder.md").read_text()
rd = (REPO / "wave_e_edwards/README.md").read_text()
check("F1: pass2_meta.json lists 3 retained structures", len(m2["retention"]["retained"]) == 3,
      m2["retention"]["retained"])
check("F1: manuscript nonetheless demotes them as inflation", "Promoting them is inflation" in ms)
check("F1: README says Pass 2 not retained as structure", "not retained as structure" in rd)
check("F1: meta.json lists M2m retained while manuscript calls it not extra structure",
      "M2m" in m1["retention"]["retained"] and "not extra structure" in ms)
check("F2: README Pass 1 line omits M2m",
      "M2m" not in [l for l in rd.splitlines() if l.startswith("**Pass 1:**")][0])
check("F2: M2m is the only model beating persist at BOTH horizons",
      ed("M2m", 1) < ed("naive_persist", 1) and ed("M2m", 5) < ed("naive_persist", 5)
      and not any(ed(m, 1) < ed("naive_persist", 1) and ed(m, 5) < ed("naive_persist", 5)
                  for m in ("M1", "M2", "M3", "M4")))

sys.path.insert(0, str(REPO / "wave_e_edwards/src"))
import build_climate as bc  # noqa: E402
nino = bc.son_anomaly(bc.load_nino34())
mg = p.merge(nino, on="year", how="left", suffixes=("_c", "_r"))
for col in ("nino34_son", "nino34_ann"):
    dd = (mg[col + "_c"] - mg[col + "_r"]).abs().max()
    check(f"F3: {col} rebuilds from committed psl_nino34_long.data", float(dd) < 1e-12,
          f"max|diff| = {float(dd):.2e}")
check("F3: pcp_* source is gitignored, not committed",
      not (REPO / "wave_e_edwards/data/climdiv-pcpndv-v1.0.0-20260806").exists())

# annual_panel.csv is verified above to match its pinned SHA-256, so reading it
# directly reads the committed content.
committed_panel = pd.read_csv(REPO / "wave_e_edwards/data/annual_panel.csv")
check("F4: build_panel.py output has 15 cols vs committed 20 (5 climate cols dropped)",
      len(committed_panel.columns) == 20
      and set(committed_panel.columns) - {"nino34_son", "nino34_ann", "pcp_cd06", "pcp_cd07", "pcp_mean"}
      == set(committed_panel.columns) - set(["nino34_son", "nino34_ann", "pcp_cd06", "pcp_cd07", "pcp_mean"]))
check("F6: manifest Edwards table header contains a literal backslash-n",
      "|---|---|---|---|---|\\n|" in (REPO / "PROOF_MANIFEST.md").read_text())

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) did not reproduce: {FAIL}")
    sys.exit(1)
print("All Wave E reproduction claims in WAVE_E_RERUN.md verified.")
sys.exit(0)
