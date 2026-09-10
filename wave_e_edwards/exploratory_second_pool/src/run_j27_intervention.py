#!/usr/bin/env python3
"""
EXPLORATORY second-pool intervention leg — Uvalde Pool (J-27).

Ports the frozen E4 design (robust viability kernels of a declared pumping
family under declared persistent recharge floors) to the Uvalde Pool index
well J-27, scored as its OWN object (no pooling).

STATUS: EXPLORATORY. Cannot alter any conclusion of paperE3/paperE4 as they
stand. Purpose: test whether the E4 verdicts (reactive rules earn a nominal
supply margin at the physical threshold; nothing protects the institutional
threshold) transfer to a second pool.

Declared porting choices (comparability assumptions for a future v3)
--------------------------------------------------------------------
  * Recharge driver : W = Basin_1 + Basin_2 (Uvalde-area basins).
  * Pumpage driver  : P = uvalde_kaf.
  * Train / audit   : fit on transitions to <= 1990; audit 1991-2023.
  * Thresholds      : the Uvalde Pool's OWN critical-period levels at J-27
                      (EAA/EAHCP): Stage V trigger = 840 ft MSL; historic
                      stages < 845 (I), < 840 (II), < 835 (III).
                      K_inst = 840 ft is the declared institutional line;
                      a sweep over {835, 840, 845} tests threshold sensitivity.
                      The Uvalde Pool has NO spring-cessation analog, so no
                      "physical" threshold is invented here.
  * Policy family   : BAU = training-mean pumping; flat caps 0-90%;
                      "S1uv" reactive (historic Stage I, 20% cut below 845);
                      "cpm_uv" cascade at 845/840/835 with cuts 20/30/35%.
  * Floors          : perpetual drought-of-record; q05; q10 of training recharge.
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
TRAIN_END = 1990
H_LO, H_HI = 820.0, 900.0   # declared model domain (J-27 clip bounds)
HORIZONS = [1, 2, 3, 5, 8, 10, 13, 20, "inf"]

# Uvalde Pool critical-period levels at J-27 (declared, EAA/EAHCP)
K_INST = 840.0
UV_STAGES = [845.0, 840.0, 835.0]


# ------------------------------------------------------------------ fitting
def fit_affine(panel, train_end=TRAIN_END):
    yr = panel["year"].to_numpy()
    H = panel["H_mean"].to_numpy(float)
    W = panel["R_uv_12"].to_numpy(float)
    P = panel["P_uv"].to_numpy(float)
    dH = H[1:] - H[:-1]
    X = np.column_stack([np.ones(len(dH)), W[1:], P[1:], H[:-1]])
    m_tr = yr[1:] <= train_end
    m_oos = yr[1:] > train_end
    coef, *_ = np.linalg.lstsq(X[m_tr], dH[m_tr], rcond=None)
    alpha, beta, gamma, delta = [float(c) for c in coef]
    a = 1.0 + delta
    res_tr = dH[m_tr] - X[m_tr] @ coef
    res_oos = dH[m_oos] - X[m_oos] @ coef
    return {"alpha": alpha, "beta": beta, "gamma": gamma, "delta": delta, "a": a,
            "n_train": int(m_tr.sum()), "n_oos": int(m_oos.sum()),
            "train_resid_max": float(np.abs(res_tr).max()),
            "train_resid_sd": float(np.std(res_tr, ddof=1)),
            "oos_resid_max": float(np.abs(res_oos).max()),
            "oos_resid_sd": float(np.std(res_oos, ddof=1)),
            "signs": {"beta_positive": bool(beta > 0),
                      "gamma_negative": bool(gamma < 0),
                      "contraction_0_lt_a_lt_1": bool(0.0 < a < 1.0)}}


# ---------------------------------------------------------------- policies
def make_policies(P_bar):
    pol = {}
    flat = lambda rho: {"fn": (lambda H, rho=rho: rho * P_bar),
                        "thresholds": [], "label": f"flat-{rho:.1f}"}
    pol["BAU"] = flat(1.0)
    for rho in (0.9, 0.8, 0.7, 0.6, 0.5, 0.0):
        pol[f"flat_{int(round(rho * 100))}"] = flat(rho)

    def s1uv(H):   # historic Uvalde Stage I: 20% cut below 845
        return 0.8 * P_bar if H < UV_STAGES[0] else P_bar
    pol["S1uv"] = {"fn": s1uv, "thresholds": [UV_STAGES[0]],
                   "label": "Uvalde Stage I reactive: 20% cut below 845 ft"}

    def cpm_uv(H):  # historic cascade 845/840/835, cuts 20/30/35%
        cut = 0.0
        if H < 845.0: cut += 0.20
        if H < 840.0: cut += 0.10
        if H < 835.0: cut += 0.05
        return (1.0 - cut) * P_bar
    pol["cpm_uv"] = {"fn": cpm_uv, "thresholds": [845.0, 840.0, 835.0],
                     "label": "Uvalde cascade 845/840/835, cuts 20/30/35%"}
    return pol


# ----------------------------------------------------------------- kernels
def _pieces(thresholds):
    """Split [H_LO, H_HI] at policy jump thresholds -> [(lo, hi), ...].

    Mirrors wave_e_edwards/src/run_intervention.py::_pieces. The H_LO edge is
    load-bearing: omitting it collapses a constant (no-threshold) policy to a
    degenerate point interval and wrongly empties every flat-policy kernel.
    """
    ts = sorted(t for t in thresholds if H_LO < t <= H_HI)
    bounds = [H_LO] + ts + [H_HI]
    out = []
    for i in range(len(bounds) - 1):
        lo, hi = bounds[i], bounds[i + 1]
        if hi > lo:
            out.append((lo, hi))
    return out


def _normalize(iv):
    ivs = sorted((float(lo), float(hi)) for lo, hi in iv if hi > lo + 1e-12)
    merged = []
    for lo, hi in ivs:
        if merged and lo <= merged[-1][1] + 1e-12:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))
    return merged


def kernel(policy, fit, W_lo, K, T):
    a, alpha, beta, gamma = fit["a"], fit["alpha"], fit["beta"], fit["gamma"]
    fn, th = policy["fn"], policy["thresholds"]
    pcs = _pieces(th)
    K0 = _normalize([(K, H_HI)])
    cur = K0
    max_iter = 1 if T == 1 else (400 if T == "inf" else int(T))
    for _ in range(max_iter):
        nxt = []
        for (plo, phi) in pcs:
            c = alpha + beta * W_lo + gamma * fn(0.5 * (plo + min(phi, plo + 1e-9)))
            for (ulo, uhi) in cur:
                pl, ph = (ulo - c) / a, (uhi - c) / a
                lo = max(pl, plo, K)
                hi = min(ph, phi, H_HI)
                if hi > lo:
                    nxt.append((lo, hi))
        nxt = _normalize(nxt)
        if not nxt:
            return None
        if T == "inf" and len(nxt) == len(cur) and all(
                abs(nl - cl) < 1e-9 and abs(nh - ch) < 1e-9
                for (nl, nh), (cl, ch) in zip(nxt, cur)):
            return nxt
        cur = nxt
    return cur


def boundary(k):
    return None if not k else float(k[-1][1])


def contains(k, x):
    return bool(k) and any(lo <= x <= hi for lo, hi in k)


def supply_replay(panel, policy):
    m = (panel["year"] >= 1941) & (panel["year"] <= TRAIN_END)
    H = panel.loc[m, "H_mean"].to_numpy(float)
    P = panel.loc[m, "P_uv"].to_numpy(float)
    fn = policy["fn"]
    presc = np.array([fn(h) for h in H])
    return {"train_mean_P": float(P.mean()), "replay_mean_P": float(presc.mean()),
            "cut_active_frac": float(np.mean(presc < 1e-9 + presc.max()) < 1)}


def main():
    print("=" * 78)
    print("EXPLORATORY — Uvalde Pool (J-27) port of the frozen E4 intervention leg")
    print("=" * 78)

    j27 = R.build_j27_panel()
    panel = (j27.merge(R.load_recharge_uv(), on="year", how="left")
                .merge(R.load_pumpage_uv(), on="year", how="left"))
    panel = panel[panel["H_mean"].notna() & panel["R_uv_12"].notna()
                  & panel["P_uv"].notna()].reset_index(drop=True)

    fit = fit_affine(panel)
    tr = panel[panel.year <= TRAIN_END]
    P_bar = float(tr["P_uv"].mean())
    W_series = tr["R_uv_12"].to_numpy(float)
    floors = {"UC_min": float(W_series.min()),
              "UC_q05": float(np.percentile(W_series, 5)),
              "UC_q10": float(np.percentile(W_series, 10))}

    print(f"\nJ-27 map (OLS on transitions to <= {TRAIN_END}, n={fit['n_train']}):")
    print(f"   a = 1+delta = {fit['a']:.4f}   alpha = {fit['alpha']:.3f}   "
          f"beta(R) = {fit['beta']:.5f}   gamma(P) = {fit['gamma']:.5f}")
    print(f"   signs: {fit['signs']}")
    print(f"   train |resid| max = {fit['train_resid_max']:.2f} ft ; "
          f"OOS |resid| max = {fit['oos_resid_max']:.2f} ft  "
          f"(n_oos={fit['n_oos']})")
    print(f"   training mean pumping P_bar = {P_bar:.2f} x10^3 acre-ft/yr")
    print(f"   floors (recharge, x10^3 acre-ft): " +
          ", ".join(f"{k}={v:.1f}" for k, v in floors.items()))
    print(f"   declared institutional threshold K_inst = {K_INST:.0f} ft (Uvalde Stage V)")

    policies = make_policies(P_bar)
    eps = fit["train_resid_max"]          # declared-defect erosion, as in E4

    results = {}
    print("\n-- robust kernels (nominal) by threshold and floor --")
    for K in [835.0, 840.0, 845.0]:
        for uc, W_lo in floors.items():
            row = {}
            for name in ["BAU", "flat_90", "flat_80", "flat_70", "flat_60",
                         "flat_50", "flat_0", "S1uv", "cpm_uv"]:
                k = kernel(policies[name], fit, W_lo, K, "inf")
                row[name] = boundary(k)
            results[f"K{int(K)}_{uc}"] = row
        b = results[f"K{int(K)}_UC_min"]
        print(f"   K={K:.0f}: UC_min fixpoint boundaries -> " +
              ", ".join(f"{n}={'-' if v is None else f'{v:.1f}'}"
                        for n, v in b.items()))

    # ---- certified layer under the declared training defect
    print(f"\n-- certified layer (threshold eroded by train eps = {eps:.2f} ft) --")
    cert = {}
    for name in ["BAU", "flat_90", "flat_60", "S1uv", "cpm_uv"]:
        ts = []
        for T in [1, 2, 3, 5, 8]:
            k = kernel(policies[name], fit, floors["UC_min"], K_INST + eps, T)
            ts.append((T, k is not None))
        first_empty = next((T for T, ok in ts if not ok), None)
        cert[name] = {"first_empty_T": first_empty,
                      "table": {str(T): ok for T, ok in ts}}
        print(f"   {name:8s} nonempty at T={[T for T,ok in ts if ok]}")
    results["certified"] = cert

    # ---- supply at matched protection (UC_min, K_inst)
    print("\n-- supply at matched protection (UC_min floor, K_inst=840) --")
    sup = {}
    for name in ["BAU", "flat_90", "flat_80", "flat_70", "flat_60",
                 "flat_50", "flat_0", "S1uv", "cpm_uv"]:
        s = supply_replay(panel, policies[name])
        sup[name] = s["replay_mean_P"]
    print("   replay mean pumping: " +
          ", ".join(f"{n}={v:.1f}" for n, v in sup.items()))
    results["supply_replay"] = sup

    with open(OUT / "j27_intervention_exploratory.json", "w") as f:
        json.dump({"status": "EXPLORATORY_NOT_FROZEN",
                   "object": "Uvalde Pool J-27 (TWDB 6950302)",
                   "K_inst": K_INST, "uv_stages": UV_STAGES,
                   "train_end": TRAIN_END, "P_bar": P_bar, "floors": floors,
                   "fit": fit, "kernels": results}, f, indent=2)
    print(f"\nwritten: {OUT/'j27_intervention_exploratory.json'}")


if __name__ == "__main__":
    main()
