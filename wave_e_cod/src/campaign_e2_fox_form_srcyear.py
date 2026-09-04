"""E2 cod intervention: Fox surplus form as the third co-equal model form (wave 7).

The floor classes are declared objects of the committed Schaefer fit and stay
FROZEN (e_min = -328.97, e_q05 = -287.36, e_q10 = -80.87 kt, source-year); the Fox fit
defines no new classes. Objects computed here:

  1. Fox one-step least-squares fit: g(S) = r*S*ln(K/S), residual convention
     e_t = S_t - (S_{t-1} + g(S_{t-1}) - C_t), t = 1984..2007 (catch at t+1),
     box r in (0.001, 2], K in [951, 5000] (the committed box), multi-start
     L-BFGS-B.
  2. Analytic quantities: g_max = rK/e at S = K/e; g(K*); F'(S) = 1 + r(ln(K/S)-1);
     F'(K*); constructive bound c* = g(K*) - |e_q10| under the frozen q10 class.
  3. Kernel lower boundaries by forward-mask grid iteration on [K*, 10^4]
     (the map is monotone on the domain for the fitted r: F' > 0 throughout),
     T = 1/3/5/inf, BAU(5)/flat_0(0)/60/120 kt, under each frozen class.
  4. Side-by-side form comparison rows vs the committed Schaefer fit.

Validation gate: the committed Schaefer numbers must reproduce (r = 0.2369,
K = 5000 pinned, SSE = 306,532, residual percentiles) before the Fox numbers
are reported.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize

REPO = Path("/tmp/liverepo")
COD = REPO / "wave_e_cod" / "src"
HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(COD))


def _import(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


rl = _import("run_ladder", COD / "run_ladder.py")
ri = _import("run_intervention", COD / "run_intervention_srcyear.py")

K_STAR, S_HI = 884.6, 10_000.0
GRID = 0.05


def fox_surplus(S, r, K):
    return r * S * np.log(K / S)


def fox_fit(years, ssb, c_ann, train_end=2007):
    """One-step LS fit of the Fox map in the committed fit_params convention:
    transition t->t+1 uses catch at t; objective = mean squared error per
    transition (the convention under which the committed Schaefer/Allee
    comparison reports 12,772 / 7,690 kt^2). Returns
    (r, K, mse, res, n, box_pinned) with residuals in the same convention."""
    m_tr = years <= train_end
    S_tr = ssb[m_tr]
    C_tr = c_ann[m_tr]
    dS = np.diff(S_tr)
    C_use = C_tr[:-1]
    S0 = S_tr[:-1]
    n = len(dS)

    def mse(p):
        r_, K_ = p
        if r_ <= 0 or K_ <= np.max(S0) * 0.5:
            return 1e12
        pred = np.array([fox_surplus(s0, r_, K_) - c for s0, c in zip(S0, C_use)])
        return float(np.mean((pred - dS) ** 2))

    best = None
    for r0 in (0.1, 0.3, 0.5, 1.0, 1.5):
        for K0 in (2000.0, 3500.0, 5000.0):
            res = minimize(mse, [r0, K0], method="L-BFGS-B",
                           bounds=[(1e-3, 2.0), (np.max(S0) + 10.0, 5000.0)])
            if best is None or res.fun < best.fun:
                best = res
    r_, K_ = float(best.x[0]), float(best.x[1])
    fitted = np.array([fox_surplus(s0, r_, K_) - c for s0, c in zip(S0, C_use)])
    res = dS - fitted
    return r_, K_, float(best.fun), res, n, bool(K_ >= 5000.0 - 1e-9)


def fox_chain(S0, c, e_floor, T, r, K):
    """Forward trajectory under the Fox map with the constant floor.
    c may be a scalar (constant catch) or a callable of S (state rule)."""
    S = S0
    for _ in range(T):
        catch = c(S) if callable(c) else c
        S = S + fox_surplus(S, r, K) - catch + e_floor
        if S < K_STAR:
            return False
    return True


def grid_boundary(c, e_floor, T, r, K, S_hi=S_HI, grid=GRID):
    """Lower boundary of {S: the T-step chain stays >= K*}: first grid point."""
    grid_pts = np.arange(K_STAR, S_hi + grid, grid)
    for S0 in grid_pts:
        if fox_chain(S0, c, e_floor, T, r, K):
            return float(S0)
    return None  # empty on the grid


def main():
    years, ssb, c_reg, c_ann, idx, lrp = rl.load()
    committed = ri.fit_surplus()
    r0, K0 = float(committed["r"]), float(committed["K"])
    assert abs(r0 - 0.2369) < 5e-5 and abs(K0 - 5000.0) < 1e-9
    e_min, e_q05, e_q10 = (float(committed["train_residual_min"]),
                           float(committed["train_residual_q05"]),
                           float(committed["train_residual_q10"]))
    assert abs(e_min + 328.97) < 0.1 and abs(e_q05 + 287.36) < 0.1 and abs(e_q10 + 80.87) < 0.1
    print("validation gate: committed Schaefer numbers reproduced (classes frozen)")

    # convention gate: committed fit_params MSEs must reproduce
    m_tr = years <= 2007
    p_sch = rl.fit_params(ssb[m_tr], c_ann[m_tr], allee=False)
    p_all = rl.fit_params(ssb[m_tr], c_ann[m_tr], allee=True)
    assert abs(p_sch["sse"] - 12772.0) < 100, p_sch["sse"]
    assert abs(p_all["sse"] - 7690.0) < 100, p_all["sse"]
    print(f"convention gate: Schaefer MSE = {p_sch['sse']:.1f} (paper 12,772), "
          f"Allee MSE = {p_all['sse']:.1f} (paper 7,690) OK")

    rF, KF, sseF, resF, nF, pinnedF = fox_fit(years, ssb, c_ann)
    print(f"\nFox fit: r = {rF:.4f}, K = {KF:.2f} (pinned={pinnedF}), MSE = {sseF:,.1f} "
          f"(fit_params convention; Schaefer 12,772, Allee 7,690), n = {nF}")
    print(f"Fox residuals: mean {resF.mean():.1f}, sd {resF.std(ddof=1):.1f}, "
          f"min {resF.min():.1f}, max {resF.max():.1f}, lag-1 {np.corrcoef(resF[1:], resF[:-1])[0,1]:.3f}")

    g_max_F = rF * KF / np.e
    g_K_F = fox_surplus(K_STAR, rF, KF)
    Fp_F = 1 + rF * (np.log(KF / K_STAR) - 1)
    cstar_F = g_K_F - abs(e_q10)
    print(f"\nFox: g_max = {g_max_F:.1f} (Schaefer 296.1); g(K*) = {g_K_F:.2f} (172.48); "
          f"F'(K*) = {Fp_F:.4f} (1.1531); constructive q10 = {cstar_F:.2f} (57.61)")

    # monotonicity check on the kernel grid
    S_test = np.arange(K_STAR, S_HI + 0.05, 0.05)
    Fp = 1 + rF * (np.log(KF / S_test) - 1)
    assert Fp.min() > 0, Fp.min()
    print(f"monotonicity: min F'(S) on [K*, 10^4] = {Fp.min():.4f} > 0")

    print("\nFox kernels (lower boundary, kt; empty = None):")
    rows = []
    for ucid, e in (("UC_min", e_min), ("UC_q05", e_q05), ("UC_q10", e_q10)):
        for pid, c in (("BAU", 5.0), ("flat_0", 0.0), ("flat_25", 60.0), ("flat_50", 120.0)):
            b1 = grid_boundary(c, e, 1, rF, KF)
            b5 = grid_boundary(c, e, 5, rF, KF)
            binf = grid_boundary(c, e, 1000, rF, KF)  # T=inf proxy (stable-equilibrium check below)
            rows.append(dict(form="fox", class_=ucid, policy=pid,
                             T1=b1, T5=b5, Tinf=binf))
            print(f"  {ucid:7} {pid:8} T=1 {b1} T=5 {b5} T=inf {binf}")
    s1_fn = lambda S: 60.0 if S >= K_STAR else 0.0
    for ucid, e in (("UC_min", e_min), ("UC_q05", e_q05), ("UC_q10", e_q10)):
        b1 = grid_boundary(s1_fn, e, 1, rF, KF)
        b5 = grid_boundary(s1_fn, e, 5, rF, KF)
        binf = grid_boundary(s1_fn, e, 1000, rF, KF)
        rows.append(dict(form="fox", class_=ucid, policy="S1",
                         T1=b1, T5=b5, Tinf=binf))
        print(f"  {ucid:7} {'S1':8} T=1 {b1} T=5 {b5} T=inf {binf}")

    # stable-equilibrium verification of the T=inf proxy: for the lowest reported
    # boundary b, iterate 5000 steps and confirm the chain never dips below K*
    # (done inside grid_boundary with T=1000; double-check at T=5000 for q10/BAU)
    b = grid_boundary(5.0, e_q10, 1, rF, KF)
    for T in (5000,):
        ok = fox_chain(b, 5.0, e_q10, T, rF, KF)
        print(f"  T=inf stability spot check (BAU q10 from {b}): {'holds' if ok else 'FAILS'}")

    # side-by-side form table
    comp = pd.DataFrame([
        dict(form="Schaefer (committed)", r=0.2369, K=5000.0, pinned=True,
             MSE_kt2=round(float(p_sch["sse"]), 1), g_max=296.1, g_Kstar=172.48,
             Fp_Kstar=1.1531, constructive_q10=57.61),
        dict(form="Allee (committed refit)", r=round(float(p_all["r"]), 4),
             K=round(float(p_all["K"]), 2), pinned=False,
             MSE_kt2=round(float(p_all["sse"]), 1), g_max="", g_Kstar="",
             Fp_Kstar="", constructive_q10=""),
        dict(form="Fox (this campaign)", r=round(rF, 4), K=round(KF, 2), pinned=pinnedF,
             MSE_kt2=round(sseF, 1), g_max=round(g_max_F, 1), g_Kstar=round(g_K_F, 2),
             Fp_Kstar=round(Fp_F, 4), constructive_q10=round(cstar_F, 2)),
    ])
    comp.to_csv(OUT / "e2_fox_form.csv", index=False)
    pd.DataFrame(rows).to_csv(OUT / "e2_fox_kernels.csv", index=False)
    print("\ncomparison:\n", comp.to_string(index=False))
    print("saved:", OUT)


if __name__ == "__main__":
    main()
