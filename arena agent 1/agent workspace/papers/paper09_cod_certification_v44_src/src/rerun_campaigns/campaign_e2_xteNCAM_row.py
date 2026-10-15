"""E2 cod intervention: xteNCAM second-specification row (wave 7, labelled, no pooling).

The row mirrors the committed NCAM object's machinery on the second, unpooled
specification: the xteNCAM SSB series (Regular et al. 2025, Table 17; DFO 2025
Table 1 landings; 2024 catch persisted from 2023), train 1954-2007 (the same
train end as the committed fit), LRP = 276 kt, Schaefer one-step least squares
in the committed fit_params convention (transition t->t+1 uses catch at t,
mean squared error objective), the same K-box rule as the committed fit
[train_max + 10, 5000], the safe set [276, 2K], and the same policy family
{0, 5, 60, 120} kt.

The floor classes are NOT transferred from the NCAM fit (different series
scale): the row declares its own classes from its own training residuals and
is reported as a labelled different-safe-set row; no pooling, no verdict
transfer between the two specifications.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path("/home/user/repo")
COD = REPO / "wave_e_cod" / "src"
HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(COD))

def _import(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(sp)
    sys.modules[name] = mod
    sp.loader.exec_module(mod)
    return mod


run_xte = _import("run_xte", COD / "run_xte.py")
rl = _import("run_ladder", COD / "run_ladder.py")

LRP = 276.0
GRID = 0.05


def schaefer(S, r, K):
    return r * S * (1 - S / K)


def chain_ok(S0, c, e_floor, T, r, K):
    S = S0
    for _ in range(T):
        S = S + schaefer(S, r, K) - c + e_floor
        if S < LRP:
            return False
    return True


def grid_boundary(c, e_floor, T, r, K, S_hi):
    for S0 in np.arange(LRP, S_hi + GRID, GRID):
        if chain_ok(S0, c, e_floor, T, r, K):
            return float(S0)
    return None


def main():
    years, ssb, cat = run_xte.load_xte()
    m_tr = years <= 2007
    p = rl.fit_params(ssb[m_tr], cat[m_tr], allee=False)
    r_, K_ = float(p["r"]), float(p["K"])
    pinned = bool(K_ >= 5000.0 - 1e-9)
    S_hi = 2 * K_
    print(f"xteNCAM Schaefer fit: r = {r_:.4f}, K = {K_:.2f} (pinned={pinned}), "
          f"MSE = {p['sse']:.1f} kt^2, n = {p.get('n', '') or int(m_tr.sum()) - 1}")

    # own residual classes (intervention convention: catch at t+1)
    res = np.array([
        float(ssb[j + 1] - (ssb[j] + schaefer(ssb[j], r_, K_) - cat[j + 1]))
        for j in range(len(years) - 1) if years[j + 1] <= 2007
    ])
    e_min, e_q05, e_q10 = float(res.min()), float(np.percentile(res, 5)), float(np.percentile(res, 10))
    print(f"own classes: e_min = {e_min:.1f}, e_q05 = {e_q05:.1f}, e_q10 = {e_q10:.1f} "
          f"(sd {res.std(ddof=1):.1f}, lag-1 {np.corrcoef(res[1:], res[:-1])[0,1]:.3f})")

    g_max = r_ * K_ / 4
    g_lrp = schaefer(LRP, r_, K_)
    Fp = 1 + r_ * (1 - 2 * LRP / K_)
    cstar = g_lrp - abs(e_q10)
    print(f"g_max = {g_max:.1f}; g(LRP) = {g_lrp:.2f}; F'(LRP) = {Fp:.4f}; "
          f"constructive (own q10) = {cstar:.2f} kt")
    print("vacuity: |e_min| vs g_max:", abs(e_min) > g_max, "| |e_q05| vs g_max:", abs(e_q05) > g_max)

    print("\nkernels vs LRP = 276 (own classes, same policy family):")
    rows = []
    for ucid, e in (("own_min", e_min), ("own_q05", e_q05), ("own_q10", e_q10)):
        for pid, c in (("flat_0", 0.0), ("BAU", 5.0), ("flat_25", 60.0), ("flat_50", 120.0)):
            b1 = grid_boundary(c, e, 1, r_, K_, S_hi)
            b5 = grid_boundary(c, e, 5, r_, K_, S_hi)
            binf = grid_boundary(c, e, 5000, r_, K_, S_hi)
            rows.append(dict(spec="xteNCAM", class_=ucid, policy=pid, T1=b1, T5=b5, Tinf=binf))
            print(f"  {ucid:8} {pid:8} T=1 {b1} T=5 {b5} T=inf {binf}")
    pd.DataFrame(rows).to_csv(OUT / "e2_xteNCAM_row.csv", index=False)

    summary = pd.DataFrame([dict(
        spec="xteNCAM", train="1954-2007", LRP=LRP, r=round(r_, 4), K=round(K_, 2),
        pinned=pinned, MSE_kt2=round(float(p["sse"]), 1), g_max=round(g_max, 1),
        g_lrp=round(g_lrp, 2), Fp_lrp=round(Fp, 4), constructive_own_q10=round(cstar, 2),
        e_min=round(e_min, 1), e_q05=round(e_q05, 1), e_q10=round(e_q10, 1),
    )])
    summary.to_csv(OUT / "e2_xteNCAM_summary.csv", index=False)
    print("\nsummary:\n", summary.to_string(index=False))


if __name__ == "__main__":
    main()
