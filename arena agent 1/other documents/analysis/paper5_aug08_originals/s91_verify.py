#!/usr/bin/env python3
"""Battery open item 1 (chile_reported_only) resolution.

Findings (see A6 decision record):
 1. The deposited "Chile" SAU series (chile_sau_annual.csv) is the GLOBAL
    taxon-600004 aggregate (Peru+Chile+Ecuador+...), verified against today's
    public SAU API (taxa/tonnage/reporting-status, region 600004) to max
    relative difference 5.1e-08 (aggregation float dust).
 2. The reported-only sensitivity (supp v7 S4: r=+0.39, p=0.024) reproduces
    EXACTLY from the API's global-reported component through the author's
    raw-SOI pipeline (1950 SOI=-99.99 included): r=+0.3870, p=0.0237.
 3. With artifact-free SOI (1950 dropped) the same cell is r=+0.2519,
    p=0.1573 (n.s.): the printed number verifies but inherits the SOI
    missing-value artifact, so v30 drops the sensitivity with the SOI block.

Inputs: _a6work/taxa_rep.json (SAU API 2026-09-11), deposited chile CSV,
frozen raw SOI. Run: python3 s91_verify.py
"""
import math, json
import numpy as np
from scipy import stats

import os
# Repo layout: run from analysis/paper5_aug08_originals/ (inputs in sibling dirs).
# Workspace layout: /home/user paths.
if os.path.isdir("/home/user/verify_battery/deposited"):
    BASE = "/home/user/verify_battery/deposited"
    TAXA = "/home/user/_a6work/taxa_rep.json"
    SOIF = "/home/user/verify_battery/frozen_inputs/soi.data"
else:
    BASE = "../anchoveta_enso"
    TAXA = "sau_taxa600004_reporting.json"
    SOIF = "../anchoveta_enso/verify/frozen_inputs/soi.data"

def load(fn):
    d = {}
    for line in open(fn):
        line = line.strip()
        if not line or line.startswith("year"):
            continue
        p = line.split(",")
        d[int(p[0])] = float(p[1])
    return d

SC = load(f"{BASE}/chile_sau_annual.csv")
R = json.load(open(TAXA))["data"]
rep = dict((y, v) for y, v in R[0]["values"] if v is not None)
unr = dict((y, v) for y, v in R[1]["values"] if v is not None)
G = {y: rep.get(y, 0) + unr.get(y, 0) for y in set(rep) | set(unr)}
mx = max(abs(SC[y] - G[y]) / abs(SC[y]) for y in SC if y in G)
print(f"deposited-chile vs API-global-taxon max rel diff: {mx:.3e} (expect ~5e-08)")

soi = {}
for line in open(SOIF):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    p = line.split()
    if len(p) != 13:
        continue
    soi[int(p[0])] = [float(v) for v in p[1:]]
Sraw = {y: float(np.mean(soi[y])) for y in soi if 1950 <= y <= 2019}
Scl = {y: float(np.mean([v for v in soi[y] if v > -90])) for y in soi
       if 1950 <= y <= 2019 and any(v > -90 for v in soi[y])}

for stag, S in (("RAW-soi", Sraw), ("CLEAN-soi", Scl)):
    yrs = sorted(set(rep) & set(S))
    x = np.array([math.log(rep[y]) for y in yrs]); x = x - x.mean()
    z = np.array([S[y] for y in yrs]); z = z - z.mean()
    eh = [i for i, y in enumerate(yrs) if y <= 1984]
    r, p = stats.pearsonr(x[eh][1:], z[eh][:-1])
    print(f"global-reported early-half lag1 [{stag}]: r={r:+.4f} p={p:.4f} n={len(eh)-1}")
print("expect: RAW r=+0.3870 p=0.0237 (= printed 0.387/0.0237); CLEAN n.s.")
