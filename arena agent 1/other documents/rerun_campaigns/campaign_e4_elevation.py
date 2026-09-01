"""E4 Edwards intervention: finite-duration recharge floors + floor-class supply (wave 7).

Two declared post-freeze layers on the committed affine map (a = 0.746094,
alpha = 163.49, beta = 0.01983, gamma = -0.02844; UC_min = 43.7, UC_q05 = 166.5,
UC_q10 = 179.1 x10^3 acre-ft; P_bar = 282.16):

  A. Finite-duration floors: the recharge floor R_lo holds for n years, then
     recharge returns to its training mean R_bar (the zero-residual analogue of
     the cod paper's finite floors). The infinite-horizon lower boundary at the
     618-ft physical threshold is computed by exact backward recursion: start
     from the infinite kernel of the nominal (R_bar) map, then pull back n
     floor-map preimages. n = 5/10/15, each UC class, each policy.

  B. Floor-class supply: the closed loop is simulated from the observed 1934
     head (659.5 ft) with recharge held at the class floor, for 57 transitions
     (1934->1991, the training span) and 90 transitions (1934->2024, the full
     panel), and the mean prescribed pumping is reported per policy — the
     declared-scoring half the historical replay does not supply. Domain exits
     (head leaving [610, 710] ft) are flagged.

Validation gate: the committed fit and class values must reproduce from the
committed results file before any new number is reported.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path("/home/user/repo")
EDW = REPO / "wave_e_edwards" / "src"
HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(EDW))

spec = importlib.util.spec_from_file_location("e4_intervention", EDW / "run_intervention.py")
ri = importlib.util.module_from_spec(spec)
sys.modules["e4_intervention"] = ri
spec.loader.exec_module(ri)

K_PHYS = 618.0
H_LO, H_HI = 610.0, 710.0


def preimage_floor(S_prev, policy, a, alpha, beta, gamma, R_lo, K):
    """Pull S_prev back one step under the floor map, clipped to [K, H_HI]."""
    fn, th = policy["fn"], policy["thresholds"]
    out = []
    for (plo, phi) in ri._pieces(th):
        c = alpha + beta * R_lo + gamma * fn(0.5 * (plo + min(phi, plo + 1e-9)))
        for (ulo, uhi) in S_prev:
            lo = max((ulo - c) / a, plo, K)
            hi = min((uhi - c) / a, phi, H_HI)
            if hi > lo:
                out.append((lo, hi))
    return ri._normalize(out)


def main():
    panel = ri.load_panel()
    fit = ri.fit_affine(panel)
    committed = json.loads((REPO / "wave_e_edwards" / "results" / "intervention_results.json").read_text())
    cf = committed["fit"]
    assert abs(fit["a"] - cf["a"]) < 1e-9 and abs(fit["alpha"] - cf["alpha"]) < 1e-9
    assert abs(fit["gamma"] - cf["gamma"]) < 1e-9
    UC = committed["declared"]["uncertainty_classes"]
    P_bar = committed["declared"]["P_bar_train"]
    assert abs(P_bar - 282.16) < 0.01
    print("validation gate: committed fit (a=0.746094, alpha=163.49, gamma=-0.02844), "
          f"UC classes {UC}, P_bar = {P_bar} reproduced")

    yr = panel["year"].to_numpy()
    R = panel["R_total"].to_numpy(float)
    H = panel["H_mean"].to_numpy(float)
    m_tr = yr <= ri.TRAIN_END
    R_bar = float(np.mean(R[m_tr]))
    H_1934 = float(H[yr == 1934][0])
    print(f"R_bar (train mean) = {R_bar:.1f}; H(1934) = {H_1934:.2f}")

    pols = ri.make_policies(P_bar)

    # ---------- A. finite-duration floors ----------
    print("\n=== A. finite-duration floors: n years at R_lo, then R_bar; T=inf boundary at 618 ft ===")
    rows = []
    a, alpha, beta, gamma = fit["a"], fit["alpha"], fit["beta"], fit["gamma"]
    for ucid, R_lo in UC.items():
        for pid, pol in pols.items():
            S_cur = ri.kernel_inf_stable(pol, fit, R_bar, K_PHYS)
            if S_cur is None:
                # nominal map already empty at infinity: pull-backs stay empty
                for n in (5, 10, 15):
                    rows.append(dict(class_=ucid, policy=pid, n=n, boundary=None))
                print(f"  {ucid:7} {pid:8} nominal T=inf kernel EMPTY under R_bar")
                continue
            for n in (5, 10, 15):
                S_cur_n = S_cur
                for _ in range(n):
                    S_cur_n = preimage_floor(S_cur_n, pol, a, alpha, beta, gamma, R_lo, K_PHYS)
                    if not S_cur_n:
                        break
                b = round(min(iv[0] for iv in S_cur_n), 1) if S_cur_n else None
                rows.append(dict(class_=ucid, policy=pid, n=n, boundary=b))
                print(f"  {ucid:7} {pid:8} n={n:2} boundary={b}")
    pd.DataFrame(rows).to_csv(OUT / "e4_finite_floors.csv", index=False)

    # ---------- B. floor-class supply ----------
    print("\n=== B. floor-class supply: closed loop from H(1934), recharge held at the floor ===")
    rows2 = []
    for ucid, R_lo in UC.items():
        for pid, pol in pols.items():
            fn = pol["fn"]
            for horizon, label in ((57, "1934-1990"), (90, "1934-2023")):
                h = H_1934
                Ps = []
                hmin = h
                exit_step = None
                for k in range(horizon):
                    P = fn(h)
                    Ps.append(P)
                    h = a * h + alpha + beta * R_lo + gamma * P
                    hmin = min(hmin, h)
                    if exit_step is None and not (H_LO <= h <= H_HI):
                        exit_step = k + 1
                rows2.append(dict(class_=ucid, policy=pid, horizon=label,
                                  mean_P=round(float(np.mean(Ps)), 2),
                                  min_head=round(float(hmin), 2),
                                  end_head=round(float(h), 2),
                                  domain_exit_step=exit_step))
                print(f"  {ucid:7} {pid:8} {label:9} mean_P={np.mean(Ps):7.2f} "
                      f"end_head={h:6.1f} exit={exit_step}")
    # reference: actual-recharge model replay (no floor)
    n_avail = len(R) - 1  # 89 transitions available (1934->2023)
    for pid, pol in pols.items():
        fn = pol["fn"]
        for horizon, label in ((57, "1934-1990"), (n_avail, "1934-2023")):
            h = H_1934
            Ps = []
            for k in range(horizon):
                P = fn(h)
                Ps.append(P)
                h = a * h + alpha + beta * R[1 + k] + gamma * P
            rows2.append(dict(class_="actual_R", policy=pid, horizon=label,
                              mean_P=round(float(np.mean(Ps)), 2),
                              min_head=None, end_head=round(float(h), 2),
                              domain_exit_step=None))
    df2 = pd.DataFrame(rows2)
    df2.to_csv(OUT / "e4_floor_supply.csv", index=False)
    print("saved:", OUT)


if __name__ == "__main__":
    main()
