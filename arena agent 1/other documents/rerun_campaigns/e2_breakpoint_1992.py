"""E2 cod intervention: formal breakpoint test at the 1991->1992 transition.

Computed on the committed fit (r = 0.2369, K = 5000 kt, one-step least squares,
window 1983-2007) with the committed residual convention (catch at t+1):
residual of year t is e_t = S_t - (S_{t-1} + surplus(S_{t-1}) - C_t), t = 1984..2007.
Break candidate: the 1992 residual (the 1991->1992 transition), i.e. the first
transition of the "after" group {1992..2007} versus {1984..1991}.

Statistics:
  - group means and their difference (Welch t reported with the residual
    autocorrelation caveat: it is indicative, not a hypothesis test),
  - Chow F at the fixed break position,
  - permutation p-value on the mean difference (10^5 draws, seed fixed):
    the residual values are permuted among the 24 positions, so the null is
    exchangeable residuals at fixed positions (order-free, not autocorrelation-free).

Protocol status: this is a declared post-freeze analysis on the frozen machinery;
it changes no committed number and modifies no frozen table.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np

REPO = Path("/home/user/repo")
COD = REPO / "wave_e_cod" / "src"
HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(COD))

SEED = 20260831
RNG = np.random.default_rng(SEED)
N_PERM = 100_000


def _import(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


rl = _import("run_ladder", COD / "run_ladder.py")
ri = _import("run_intervention", COD / "run_intervention.py")


def main() -> None:
    years, ssb, c_reg, c_ann, idx, lrp = rl.load()
    fit = ri.fit_surplus()
    r0, K0 = float(fit["r"]), float(fit["K"])
    assert abs(r0 - 0.2369) < 5e-5 and abs(K0 - 5000.0) < 1e-9

    res_by_year = {
        int(years[j + 1]): float(ssb[j + 1] - (ssb[j] + rl.surplus(ssb[j], r0, K0) - c_ann[j + 1]))
        for j in range(len(years) - 1)
    }
    res_tr = np.array([res_by_year[y] for y in sorted(res_by_year) if y <= 2007])
    yr_tr = np.array([y for y in sorted(res_by_year) if y <= 2007])
    assert len(res_tr) == 24 and abs(res_tr.min() + 460.03) < 0.1

    before = res_tr[yr_tr < 1992]   # 1984..1991, n = 8
    after = res_tr[yr_tr >= 1992]   # 1992..2007, n = 16
    assert len(before) == 8 and len(after) == 16

    mb, ma = before.mean(), after.mean()
    diff = ma - mb
    n1, n2 = len(before), len(after)
    v1, v2 = before.var(ddof=1), after.var(ddof=1)
    welch_t = diff / np.sqrt(v1 / n1 + v2 / n2)

    # Chow F at the fixed 1992 position (common mean vs break dummy)
    d = (yr_tr >= 1992).astype(float)
    y = res_tr
    Xr = np.ones((len(y), 1))
    Xu = np.column_stack([np.ones(len(y)), d])
    ssr = ((y - Xr @ np.linalg.lstsq(Xr, y, rcond=None)[0]) ** 2).sum()
    ssu = ((y - Xu @ np.linalg.lstsq(Xu, y, rcond=None)[0]) ** 2).sum()
    chow_F = ((ssr - ssu) / 1) / (ssu / (len(y) - 2))

    # permutation p-value on the mean difference (10^5 draws, seed fixed)
    n = len(y)
    idx = np.tile(np.arange(n), (N_PERM, 1))
    idx = RNG.permuted(idx, axis=1)
    grp = idx[:, :n1].astype(np.intp)
    vals = y[grp]
    # direct computation: mean of the first n1 draws minus mean of the rest
    perm_mean_before = vals.mean(axis=1)
    perm_mean_after = (y.sum() - vals.sum(axis=1)) / n2
    perm_diffs = perm_mean_after - perm_mean_before
    p_perm = float((np.abs(perm_diffs) >= np.abs(diff)).mean())

    print("=== 1992 breakpoint test (committed fit, n = 24, seed %d) ===" % SEED)
    print(f"mean 1984-1991 : {mb:9.2f} kt   (n = {n1})")
    print(f"mean 1992-2007 : {ma:9.2f} kt   (n = {n2})")
    print(f"difference     : {diff:9.2f} kt")
    print(f"Welch t        : {welch_t:9.3f}   (indicative; residuals autocorrelated, lag-1 = 0.65)")
    print(f"Chow F(1,22)   : {chow_F:9.3f}")
    print(f"permutation p  : {p_perm:.4f}   ({N_PERM} draws)")

    out = OUT / "e2_breakpoint_1992.csv"
    import pandas as pd
    pd.DataFrame([{
        "n": n, "n_before": n1, "n_after": n2,
        "mean_before": round(mb, 2), "mean_after": round(ma, 2),
        "mean_difference": round(diff, 2),
        "welch_t": round(welch_t, 3),
        "chow_F": round(chow_F, 3),
        "perm_p": round(p_perm, 4),
        "seed": SEED, "n_perm": N_PERM,
    }]).to_csv(out, index=False)
    print("saved:", out)


if __name__ == "__main__":
    main()
