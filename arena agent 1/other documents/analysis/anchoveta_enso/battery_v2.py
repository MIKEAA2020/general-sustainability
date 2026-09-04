#!/usr/bin/env python3
"""Anchoveta-ENSO battery v2 — on the owner-supplied Sea Around Us series.
Peru: shortened.txt (entity 604, taxon 87, Q_tlw), 1950-2024, paper window 1950-2019.
Chile: SAU Taxa 600004 v50-1.csv (Engraulis ringens, all sectors/reporting), 1950-2019.
Indices: NOAA PSL ERSSTv5 NINO1/NINO3/NINO3.4/NINO4, PSL SOI, annual means.
"""
import re, math, json
import numpy as np
import pandas as pd
from scipy import stats
from scipy.signal import lombscargle
from statsmodels.tsa.stattools import grangercausalitytests
import pyEDM

def parse_psl(fn):
    rows = {}; cur_year = None
    for line in open(fn):
        line = line.strip()
        if not line: continue
        toks = line.split()
        if len(toks) == 2 and re.fullmatch(r"\d{4}", toks[0]) and re.fullmatch(r"\d{4}", toks[1]): continue
        if re.fullmatch(r"\d{4}", toks[0]) and len(toks) > 1:
            cur_year = int(toks[0]); toks = toks[1:]
        if cur_year is None: continue
        vals = [float(t) for t in toks if re.match(r"-?\d+(\.\d+)?$", t)]
        rows.setdefault(cur_year, []).extend(vals)
    return {y: sum(v)/len(v) for y, v in rows.items() if v}

def load_peru(fn):
    """shortened.txt: entity<TAB>flag<TAB>taxon<TAB>unit<TAB>year<TAB>value<TAB>status"""
    out = {}
    for line in open(fn):
        t = line.strip().split("\t")
        if len(t) < 6: continue
        try:
            y = int(t[4]); v = float(t[5])
        except ValueError: continue
        out[y] = out.get(y, 0.0) + v
    return out

def load_chile(fn):
    import csv
    out = {}
    for r in csv.DictReader(open(fn)):
        y = int(r["year"]); v = float(r["tonnes"])
        out[y] = out.get(y, 0.0) + v
    return out

def clamp(series, lo, hi):
    return {y: v for y, v in series.items() if lo <= y <= hi}

def spec(series, name):
    yrs = sorted(series); x = np.array(yrs); y = np.log(np.array([series[y] for y in yrs]))
    y = y - y.mean()
    f = np.linspace(1/10, 1/1.5, 4000)
    pg = lombscargle(x, y, 2*np.pi*f, normalize=True)
    return dict(name=name, period=float(1/f[np.argmax(pg)]), power=float(pg.max()), n=len(yrs))

def xcorr(series, index, lag):
    yrs = sorted(set(series) & set(index))
    x = np.array([math.log(series[y]) for y in yrs]); x = x - x.mean()
    z = np.array([index[y] for y in yrs]); z = z - z.mean()
    if lag >= 0: xa, za = x[lag:], z[:-lag] if lag else z
    else: xa, za = x[:lag], z[-lag:]
    r, p = stats.pearsonr(xa, za)
    return float(r), float(p), len(xa)

def granger(series, index, maxlag=3):
    yrs = sorted(set(series) & set(index))
    df = pd.DataFrame({"catch": [math.log(series[y]) for y in yrs], "enso": [index[y] for y in yrs]})
    out = {}
    for direction, cols in [("ENSO->catch", ["catch", "enso"]), ("catch->ENSO", ["enso", "catch"])]:
        g = grangercausalitytests(df[cols], maxlag=maxlag)
        out[direction] = {str(lag): round(float(v[0]["ssr_ftest"][1]), 5) for lag, v in g.items()}
    return out

def ccm_run(series, index, name, libs=("30 35 2", "40 45 2", "50 55 2", "60 65 2")):
    yrs = sorted(set(series) & set(index))
    df = pd.DataFrame({"year": yrs, "logcatch": [math.log(series[y]) for y in yrs], "enso": [index[y] for y in yrs]})
    out = []
    for E in (2, 3):
        for lib in libs:
            try:
                r1 = pyEDM.CCM(dataFrame=df, E=E, columns="logcatch", target="enso", libSizes=lib, sample=50, showPlot=False)
                c1 = float(r1.iloc[-1]["logcatch:enso"])
                r2 = pyEDM.CCM(dataFrame=df, E=E, columns="enso", target="logcatch", libSizes=lib, sample=50, showPlot=False)
                c2 = float(r2.iloc[-1]["enso:logcatch"])
                out.append(dict(E=E, lib=lib, catch_to_enso=round(c1,3), enso_to_catch=round(c2,3)))
            except Exception as ex:
                out.append(dict(E=E, lib=lib, error=f"{type(ex).__name__}"))
    return out

def main():
    idx = {n.upper().replace("NINA","NINO"): parse_psl(f"{n}.anom.data") for n in ["nina1","nina3","nina34","nina4"]}
    idx["SOI"] = parse_psl("soi_ok.data")
    peru_all = load_peru("/home/user/uploads/shortened.txt")
    chile_all = load_chile("/home/user/uploads/SAU Taxa 600004 v50-1.csv")
    peru = clamp(peru_all, 1950, 2019)
    chile = clamp(chile_all, 1950, 2019)
    peru25 = clamp(peru_all, 1950, 2024)
    res = {"peru": {"years": [min(peru), max(peru)], "n": len(peru)},
           "chile": {"years": [min(chile), max(chile)], "n": len(chile)}}

    # spectra
    for nm, s in [("Peru", peru), ("Chile", chile), ("Peru_ext", peru25)]:
        sp = spec(s, nm); res[f"spec_{nm}"] = sp
        print(f"SPEC {nm}: dominant period {sp['period']:.2f} yr, norm power {sp['power']:.3f}, n={sp['n']}")

    # cross-correlation sweep + BH-FDR (90 cells)
    cells = []
    for nm, s in [("Peru", peru), ("Chile", chile)]:
        for iname, iv in idx.items():
            for lag in range(-4, 5):
                r, p, n = xcorr(s, iv, lag)
                cells.append(dict(series=nm, index=iname, lag=lag, r=r, p=p, n=n))
    cells.sort(key=lambda c: c["p"])
    m = len(cells)
    for i, c in enumerate(cells):
        c["bh"] = 0.05*(i+1)/m; c["sig"] = c["p"] <= c["bh"]
    nsig = sum(c["sig"] for c in cells)
    print(f"\nXCC: {m} cells; BH-FDR 0.05 significant: {nsig}")
    for c in cells[:8]:
        print(f"  {c['series']:5s} {c['index']:6s} lag={c['lag']:+d} r={c['r']:+.3f} p={c['p']:.4f} n={c['n']} BH={'Y' if c['sig'] else 'n'}")
    res["xcorr"] = cells

    # pre-committed cells (from v1 battery): NINO1 lag+1, SOI lag+2 — on both series
    for nm, s in [("Peru", peru), ("Chile", chile)]:
        for iname, lag in [("NINO1", 1), ("SOI", 2)]:
            r, p, n = xcorr(s, idx[iname], lag)
            print(f"PRECOMMITTED {nm} {iname} lag={lag:+d}: r={r:+.3f} p={p:.4f} n={n}")

    # Granger (bivariate, maxlag 3)
    for nm, s in [("Peru", peru), ("Chile", chile)]:
        g = granger(s, idx["NINO1"])
        res[f"granger_{nm}"] = g
        print(f"\nGRANGER {nm}: ENSO->catch {g['ENSO->catch']} | catch->ENSO {g['catch->ENSO']}")

    # CCM (now properly powered, n=70)
    for nm, s in [("Peru", peru), ("Chile", chile)]:
        cc = ccm_run(s, idx["NINO1"], nm)
        res[f"ccm_{nm}"] = cc
        print(f"\nCCM {nm} (NINO1):")
        for c in cc:
            print("  ", c)

    # split-half Peru (cut 1985: 1950-1984 vs 1985-2019)
    for nm, s, cut, label in [("Peru", peru, 1985, "1950-84/1985-2019")]:
        for half, lo, hi in [("early", 1950, cut-1), ("late", cut, 2019)]:
            hs = clamp(s, lo, hi)
            r, p, n = xcorr(hs, idx["NINO1"], 1)
            print(f"SPLIT {nm} {half} ({lo}-{hi}, n={n}): NINO1 lag+1 r={r:+.3f} p={p:.4f}")
            res[f"split_{nm}_{half}"] = dict(r=r, p=p, n=n)

    json.dump(res, open("battery_v2_results.json", "w"), indent=1, default=str)
    print("\nSaved battery_v2_results.json")

if __name__ == "__main__":
    main()
