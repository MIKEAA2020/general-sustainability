#!/usr/bin/env python3
"""
EXPLORATORY diagnostics — is the J-27 M2 "win" real, or noise / artifact?

The primary J-27 run returned retained_as_structure = ['M2'] at h=1, which
CONTRADICTS the frozen E3 verdict (structure never beats persistence). Before
that can motivate anything, it must survive:

  D1. Diebold-Mariano (Newey-West HAC, lag h-1) on M2 vs persistence at h=1
  D2. Moving-block bootstrap CI on the RMSE gap (10,000 reps, block 8)
  D3. Origin-level win/loss count
  D4. Sub-period stability (split the origins in half)
  D5. Driver-independence check (the same win under a mismatched driver)
  D6. The candidate mechanism: head autocorrelation across pools

EXPLORATORY ONLY — cannot alter any published conclusion.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_j27_exploratory as R  # noqa: E402

OUT = R.OUT
rng = np.random.default_rng(20260910)


def rmse(e):
    e = np.asarray(e, float)
    return float(np.sqrt(np.mean(e ** 2)))


def dm_test(e1, e2, h=1):
    """Diebold-Mariano with Newey-West HAC. e = forecast errors (same order)."""
    d = e1 ** 2 - e2 ** 2
    n = len(d)
    dbar = d.mean()
    lag = h - 1
    gamma0 = np.mean((d - dbar) ** 2)
    var = gamma0
    for k in range(1, lag + 1):
        gk = np.mean((d[k:] - dbar) * (d[:-k] - dbar))
        var += 2 * (1 - k / (lag + 1)) * gk
    se = np.sqrt(var / n) if var > 0 else np.nan
    z = dbar / se if se and se > 0 else np.nan
    return float(z), float(dbar), float(se)


def block_bootstrap_gap(e1, e2, block=8, reps=10000):
    n = len(e1)
    gaps = np.empty(reps)
    nb = int(np.ceil(n / block))
    for i in range(reps):
        starts = rng.integers(0, n - block + 1, nb)
        idx = np.concatenate([np.arange(s, s + block) for s in starts])[:n]
        gaps[i] = rmse(e1[idx]) - rmse(e2[idx])
    return (float(np.percentile(gaps, 2.5)), float(np.percentile(gaps, 97.5)),
            float(np.mean(gaps < 0)))


def main():
    print("=" * 78)
    print("EXPLORATORY DIAGNOSTICS — J-27 (Uvalde Pool) M2-vs-persistence gap")
    print("=" * 78)

    j27 = R.build_j27_panel()
    rec = R.load_recharge_uv()
    pmp = R.load_pumpage_uv()
    panel = j27.merge(rec, on="year", how="left").merge(pmp, on="year", how="left")
    full = panel[panel["H_mean"].notna() & panel["R_uv_12"].notna()
                 & panel["P_uv"].notna()].reset_index(drop=True)
    lo, hi = 820.0, 890.0

    df, summary = R.run_ladder(full, "R_uv_12", lo, hi)
    print(f"\npanel: {int(full.year.min())}-{int(full.year.max())}, n={len(full)}")

    # ---- D1/D2/D3/D4 on h = 1
    h1 = df[df.horizon == 1]
    piv_e = h1.pivot_table(index="origin", columns="model", values="pred")
    piv_y = h1.groupby("origin")["obs"].first()
    piv_e = piv_e.sub(piv_y, axis=0)  # errors == pred - obs

    e_m2 = piv_e["M2"].to_numpy(float)
    e_pe = piv_e["naive_persist"].to_numpy(float)
    origins = piv_e.index.to_numpy()

    z, dbar, se = dm_test(e_m2, e_pe, h=1)
    lo_ci, hi_ci, p_ge = block_bootstrap_gap(e_m2, e_pe, block=8, reps=10000)

    wins = int(np.sum(np.abs(e_m2) < np.abs(e_pe)))
    print("\n-- D1 Diebold-Mariano (M2 vs persistence, h=1) --")
    print(f"   mean sq-err gap = {dbar:+.3f}  (negative favours M2),  DM z = {z:+.3f}")
    print(f"   => {'M2 significantly better' if z < -1.96 else 'INSIGNIFICANT (|z|<1.96)'}")
    print("\n-- D2 moving-block bootstrap, RMSE gap (10,000 reps, block 8) --")
    print(f"   95% CI = [{lo_ci:+.3f}, {hi_ci:+.3f}] ft ; P(gap<0) = {p_ge:.3f}")
    print(f"   => {'CI excludes 0 (favours M2)' if hi_ci < 0 else 'CI COVERS 0 -> not separated'}")
    print("\n-- D3 origin-level win/loss (h=1) --")
    print(f"   M2 wins on {wins}/{len(origins)} origins")

    print("\n-- D4 sub-period stability (h=1) --")
    half = len(origins) // 2
    for lbl, sl in [("early", slice(0, half)), ("late", slice(half, None))]:
        a, b = e_m2[sl], e_pe[sl]
        print(f"   {lbl:5s} (n={len(a)}): RMSE M2={rmse(a):6.2f} persist={rmse(b):6.2f} "
              f"gap={rmse(a)-rmse(b):+6.2f}")

    # ---- D5 driver independence: does M2 still win under a mismatched driver?
    print("\n-- D5 driver independence (h=1 RMSE) --")
    for label, col in [("Uvalde Basin_1+2", "R_uv_12"), ("Uvalde Basin_1-4", "R_uv_1234"),
                       ("San Antonio Total", "R_sa_total")]:
        d2, s2 = R.run_ladder(full, col, lo, hi)
        hh = s2[s2.horizon == 1].set_index("model")["rmse"]
        print(f"   R={label:18s} persist={hh['naive_persist']:6.2f} "
              f"M1={hh['M1']:6.2f} M2={hh['M2']:6.2f} M2m={hh['M2m']:6.2f}")

    # ---- D6 mechanism: head autocorrelation across pools
    j17 = pd.read_csv(R.DATA / "annual_panel.csv")
    sa = j17[j17.H_mean.notna() & j17.R_total.notna()]
    def ac1(x):
        x = np.asarray(x, float); return float(np.corrcoef(x[1:], x[:-1])[0, 1])
    print("\n-- D6 candidate mechanism: head persistence --")
    print(f"   head AC1  J-17 (San Antonio) = {ac1(sa.H_mean):.3f}")
    print(f"   head AC1  J-27 (Uvalde)      = {ac1(full.H_mean):.3f}")
    print(f"   recharge AC1 J-17 = {ac1(sa.R_total):.3f}   "
          f"J-27 = {ac1(full.R_uv_12):.3f}")

    out = {
        "status": "EXPLORATORY_NOT_FROZEN",
        "h1_dm_z": z, "h1_mean_sqerr_gap": dbar,
        "h1_bootstrap_ci": [lo_ci, hi_ci], "h1_p_gap_lt_0": p_ge,
        "h1_origins_M2_wins": wins, "h1_origins_n": int(len(origins)),
        "head_ac1_j17": ac1(sa.H_mean), "head_ac1_j27": ac1(full.H_mean),
        "recharge_ac1_j17": ac1(sa.R_total), "recharge_ac1_j27": ac1(full.R_uv_12),
    }
    with open(OUT / "j27_diagnostics.json", "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwritten: {OUT/'j27_diagnostics.json'}")


if __name__ == "__main__":
    main()
