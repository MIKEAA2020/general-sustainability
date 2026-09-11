#!/usr/bin/env python3
"""Provenance of the v29 |r|~0.31 anchoveta--ENSO figure (A6 decision record input).

Scans {Sep,Aug} SAU Peru vintage x {logged,unlogged,detrended} x NINO1/3/34/4
x lags 1-12 for Pearson |r| in [0.28,0.34]. Result: the unique standard-
pipeline match is September-vintage detrended-log Peru x NINO1 lag1
(r=-0.3119, p=0.0091); the August vintage gives -0.2917 under the same
pipeline. Implausible lag-10 cells are the only other hits.

Inputs (read-only): deposited SAU CSVs + indices_annual.json + Aug-08 CSV.
"""
import math, json
import numpy as np
from scipy import stats

import os
# Repo layout: run from analysis/paper5_aug08_originals/ (inputs in sibling dirs).
# Workspace layout: /home/user/verify_battery/deposited + /home/user/_a6work.
if os.path.isdir("/home/user/verify_battery/deposited"):
    BASE = "/home/user/verify_battery/deposited"
    AUG = "/home/user/_a6work/peru_aug08.csv"
else:
    BASE = "../anchoveta_enso"
    AUG = "peru_anchoveta_catch_sau.csv"

def load(fn):
    d = {}
    for line in open(fn):
        line = line.strip()
        if not line or line.startswith("year"):
            continue
        p = line.split(",")
        d[int(p[0])] = float(p[1])
    return d

SEP = {y: v for y, v in load(f"{BASE}/peru_sau_annual.csv").items() if 1950 <= y <= 2019}
AUG = {y: v for y, v in load(AUG).items() if 1950 <= y <= 2019}
dep = json.load(open(f"{BASE}/indices_annual.json"))
NINO = {n: {int(k): v for k, v in dep[n].items()} for n in ("NINO1", "NINO3", "NINO34", "NINO4")}

def prep(S, mode):
    yrs = sorted(S)
    t = np.arange(len(yrs))
    x = np.array([(math.log(S[y]) if mode != "unlogged" else S[y]) for y in yrs])
    if mode == "detrended":
        b1, b0 = np.polyfit(t, x, 1)
        x = x - (b0 + b1 * t)
    return yrs, x - x.mean()

print("scan: {Sep,Aug} x {logged,unlogged,detrended} x NINOs x lags1-12; want 0.28<=|r|<=0.34")
hits = 0
for sname, S in (("Sep", SEP), ("Aug", AUG)):
    for mode in ("logged", "unlogged", "detrended"):
        yrs, x = prep(S, mode)
        for nm, iv in NINO.items():
            z = np.array([iv[y] for y in yrs])
            z = z - z.mean()
            for lag in range(1, 13):
                r, p = stats.pearsonr(x[lag:], z[:-lag])
                if 0.28 <= abs(r) <= 0.34:
                    hits += 1
                    print(f"  HIT {sname} {mode} {nm} lag{lag}: r={r:+.4f} p={p:.4f}")
print("total hits:", hits)
