#!/usr/bin/env python3
"""Anchoveta-ENSO battery: spectral, cross-correlation+FDR, CCM, Granger, split-half, replication.
Series: RAM Legacy v4.66 TC (Peru PANCHNCHSP 1986-2019; Chile PANCHCCH 1985-2020).
Indices: PSL NINO1/NINO3/NINO3.4/NINO4 (ERSSTv5), SOI (PSL soi.data), annual means.
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

def load_csv(fn):
    out = {}
    for line in open(fn):
        line = line.strip()
        if not line or line.startswith('"'): continue
        p = line.split(",")
        try: out[int(p[0])] = float(p[1])
        except: pass
    return out

def main():
    idx = {n.upper().replace("NINA","NINO"): parse_psl(f"{n}.anom.data") for n in ["nina1","nina3","nina34","nina4"]}
    idx["SOI"] = parse_psl("soi_ok.data")
    peru = load_csv("PANCHNCHSP_catch.csv")
    chile = load_csv("PANCHCCH_catch.csv")
    res = {}

    # 0. spectra
    def spec(series):
        yrs = sorted(series); x = np.array(yrs); y = np.log(np.array([series[y] for y in yrs]))
        y = y - y.mean()
        f = np.linspace(1/10, 1/1.5, 2000)
        pg = lombscargle(x, y, 2*np.pi*f, normalize=True)
        return float(1/f[np.argmax(pg)]), float(pg.max())
    for nm, s in [("Peru", peru), ("Chile", chile)]:
        p, pw = spec(s); res[f"spec_{nm}"] = (p, pw)
        print(f"SPEC {nm}: dominant period {p:.2f} yr, normalized power {pw:.3f}")

    # 1. cross-correlations + BH-FDR
    def xcorr(series, index, lag):
        yrs = sorted(set(series) & set(index))
        x = np.array([math.log(series[y]) for y in yrs]); x = x - x.mean()
        z = np.array([index[y] for y in yrs]); z = z - z.mean()
        if lag >= 0: xa, za = x[lag:], z[:-lag] if lag else z
        else: xa, za = x[:lag], z[-lag:]
        return stats.pearsonr(xa, za)
    cells = []
    for nm, s in [("Peru", peru), ("Chile", chile)]:
        for iname, iv in idx.items():
            for lag in range(-4, 5):
                r, p = xcorr(s, iv, lag)
                cells.append(dict(series=nm, index=iname, lag=lag, r=float(r), p=float(p)))
    cells.sort(key=lambda c: c["p"])
    m = len(cells)
    for i, c in enumerate(cells):
        c["bh"] = 0.05*(i+1)/m
        c["sig"] = c["p"] <= c["bh"]
    nsig = sum(c["sig"] for c in cells)
    print(f"\nXCC: {m} cells; BH-FDR 0.05 significant: {nsig}")
    for c in cells[:6]:
        print(f"  {c['series']:5s} {c['index']:6s} lag={c['lag']:+d} r={c['r']:+.3f} p={c['p']:.4f}")
    for nm in ["Peru","Chile"]:
        b = sorted([c for c in cells if c["series"]==nm], key=lambda c: c["p"])[0]
        print(f"  BEST {nm}: {b['index']} lag={b['lag']:+d} r={b['r']:+.3f} p={b['p']:.4f}")
    res["xcorr"] = cells

    # 2. CCM (pyEDM) — direction test, honest about small n
    def ccm_run(series, iname, nm):
        yrs = sorted(set(series) & set(idx[iname]))
        df = pd.DataFrame({"year": yrs, "logcatch": [math.log(series[y]) for y in yrs], "enso": [idx[iname][y] for y in yrs]})
        out = []
        for E in [2, 3]:
            for lib in ["20 25 2", "25 30 2"]:
                try:
                    r1 = pyEDM.CCM(dataFrame=df, E=E, columns="logcatch", target="enso", libSizes=lib, sample=50, showPlot=False)
                    c1 = float(r1.iloc[-1]["logcatch:enso"])
                    r2 = pyEDM.CCM(dataFrame=df, E=E, columns="enso", target="logcatch", libSizes=lib, sample=50, showPlot=False)
                    c2 = float(r2.iloc[-1]["enso:logcatch"])
                    out.append(dict(E=E, lib=lib, catch_to_enso=c1, enso_to_catch=c2))
                    print(f"CCM {nm} {iname} E={E} lib={lib}: catch->ENSO {c1:+.3f} | ENSO->catch {c2:+.3f}")
                except Exception as ex:
                    out.append(dict(E=E, lib=lib, error=f"{type(ex).__name__}: {ex}"))
                    print(f"CCM {nm} {iname} E={E} lib={lib}: FAILED {type(ex).__name__}")
        return out
    res["ccm_peru"] = ccm_run(peru, "NINO1", "Peru")
    res["ccm_chile"] = ccm_run(chile, "NINO1", "Chile")

    # 3. Granger (linear, bivariate) — annual data, maxlag 3
    def granger(series, iname, nm):
        yrs = sorted(set(series) & set(idx[iname]))
        df = pd.DataFrame({"catch": [math.log(series[y]) for y in yrs], "enso": [idx[iname][y] for y in yrs]})
        out = {}
        for direction, cols in [("ENSO->catch", ["catch", "enso"]), ("catch->ENSO", ["enso", "catch"])]:
            try:
                g = grangercausalitytests(df[cols], maxlag=3, verbose=False)
                out[direction] = {lag: (float(v[0]["ssr_ftest"][1]),) for lag, v in g.items()}
                for lag, v in g.items():
                    p = v[0]["ssr_ftest"][1]
                    print(f"GR {nm} {direction} lag={lag}: F-test p={p:.4f}")
            except Exception as ex:
                out[direction] = {"error": str(ex)}
        return out
    res["granger_peru"] = granger(peru, "NINO1", "Peru")
    res["granger_chile"] = granger(chile, "NINO1", "Chile")

    # 4. split-half (Peru: 1986-2002 vs 2003-2019) on the best cell (NINO1 lag+1)
    def split_half(series, iname, lag, cut=2003):
        yrs = sorted(set(series) & set(idx[iname]))
        halves = {"early": [y for y in yrs if y < cut], "late": [y for y in yrs if y >= cut]}
        out = {}
        for hn, hy in halves.items():
            if len(hy) < 8: out[hn] = None; continue
            x = np.array([math.log(series[y]) for y in hy]); x = x - x.mean()
            z = np.array([idx[iname][y] for y in hy]); z = z - z.mean()
            if lag >= 0: xa, za = x[lag:], z[:-lag] if lag else z
            else: xa, za = x[:lag], z[-lag:]
            r, p = stats.pearsonr(xa, za)
            out[hn] = (float(r), float(p), len(hy))
            print(f"SPLIT Peru {hn} (n={len(hy)}): {iname} lag={lag:+d} r={r:+.3f} p={p:.4f}")
        return out
    res["split_peru"] = split_half(peru, "NINO1", 1)

    json.dump(res, open("battery_results.json", "w"), indent=1, default=str)
    print("\nSaved battery_results.json")

if __name__ == "__main__":
    main()
