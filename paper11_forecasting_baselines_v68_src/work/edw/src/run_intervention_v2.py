#!/usr/bin/env python3
"""
Wave E intervention-selection leg — Edwards Aquifer, San Antonio Pool.

Executes protocol_intervention.md (locked 2026-08-26): robust viability
kernels for a declared governance-operator family under declared
persistent-recharge uncertainty classes, with the R04.Cor2 / R03.Cor5
erosion conversion (discrete-contraction form), supply replays, the
1950s stress counterfactual, and the frozen retention rule.

No forecast module is promoted or demoted here. The fibre and the oracle
are not used. No two-pool claim. z = J-17 annual mean only.

Batch-5 corrected edition (v2).  One change relative to run_intervention.py,
documented in BATCH5_JOINT_AUDIT_EVALUATION.md (finding W12): the retention
comparator `lt` is ported from the cod runner's corrected semantics, so an
empty kernel counts as worst (+inf) in BOTH arguments instead of the latent
asymmetric v1 semantics (module-empty counting as improving on a nonempty
BAU kernel; genuine improvements over an empty BAU kernel not credited).
The v1 asymmetry was mechanically verified inert for the committed Edwards
artifacts (zero module-empty/BAU-nonempty pairs across all 216 module
readings; the second direction only makes retention harder), and this v2
re-execution regenerates both outputs with values identical to the committed
ones — the fix is code hygiene with no numerical effect.

Run:  python3 src/run_intervention_v2.py
Out:  results/intervention_results_v2.json
      results/intervention_boundaries_v2.csv
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"

H_LO, H_HI = 610.0, 710.0          # declared model domain (ladder clip bounds)
K_PHYS, K_INST = 618.0, 660.0      # declared [N] thresholds (protocol.md)
TRAIN_END = 1990                    # fit window 1934-1990; OOS 1991-2023 audit
HORIZONS = [1, 2, 3, 5, 8, 10, 15, 20, "inf"]

# ---------------------------------------------------------------- panel


def load_panel() -> pd.DataFrame:
    p = pd.read_csv(DATA / "annual_panel.csv")
    p = p[p["year"].between(1934, 2023)].copy()
    need = ["H_mean", "R_total", "P_wells"]
    if p[need].isna().any().any():
        raise SystemExit("incomplete primary panel 1934-2023")
    return p.reset_index(drop=True)


# ---------------------------------------------------------------- fit


def fit_affine(panel: pd.DataFrame) -> dict:
    yr = panel["year"].to_numpy()
    H = panel["H_mean"].to_numpy(float)
    R = panel["R_total"].to_numpy(float)
    P = panel["P_wells"].to_numpy(float)
    dH = H[1:] - H[:-1]
    X = np.column_stack([np.ones(len(dH)), R[1:], P[1:], H[:-1]])
    m_tr = yr[1:] <= TRAIN_END
    m_oos = yr[1:] > TRAIN_END
    coef, *_ = np.linalg.lstsq(X[m_tr], dH[m_tr], rcond=None)
    alpha, beta, gamma, delta = [float(c) for c in coef]
    a = 1.0 + delta
    res_tr = dH[m_tr] - X[m_tr] @ coef
    res_oos = dH[m_oos] - X[m_oos] @ coef
    ar1 = 0.0
    if len(res_tr) > 2:
        ar1 = float(np.dot(res_tr[1:], res_tr[:-1]) / np.dot(res_tr[:-1], res_tr[:-1]))
    i_max_tr = int(np.argmax(np.abs(res_tr)))
    i_max_oos = int(np.argmax(np.abs(res_oos)))
    return {
        "alpha": alpha, "beta": beta, "gamma": gamma, "delta": delta, "a": a,
        "n_train_transitions": int(m_tr.sum()),
        "n_oos_transitions": int(m_oos.sum()),
        "train_residual_sd": float(np.std(res_tr, ddof=1)),
        "train_residual_max": float(np.abs(res_tr).max()),
        "train_residual_max_year": int(yr[1:][m_tr][i_max_tr]),
        "oos_residual_sd": float(np.std(res_oos, ddof=1)),
        "oos_residual_max": float(np.abs(res_oos).max()),
        "oos_residual_max_year": int(yr[1:][m_oos][i_max_oos]),
        "train_residual_ar1": ar1,
        "signs": {"beta_positive": bool(beta > 0), "gamma_negative": bool(gamma < 0),
                  "contraction_0_lt_a_lt_1": bool(0.0 < a < 1.0)},
    }


# ---------------------------------------------------------------- policies


def make_policies(P_bar: float) -> dict:
    """Each policy: dict with fn(H)->P, thresholds (jump set), label."""
    pol = {}

    def flat(rho):
        return {"fn": lambda H, rho=rho: rho * P_bar, "thresholds": [],
                "label": f"flat-{rho:.1f} (P = {rho:.1f} Pbar)"}

    pol["BAU"] = flat(1.0)
    for rho in (0.9, 0.8, 0.7, 0.6, 0.5, 0.0):
        pol[f"flat_{int(round(rho*100))}"] = flat(rho)

    def s1(H):
        return 0.8 * P_bar if H < 660.0 else P_bar
    pol["S1"] = {"fn": s1, "thresholds": [660.0],
                 "label": "Stage I reactive: 20% cut below 660 ft (verified)"}

    def cpm(H):
        cut = 0.0
        if H < 660.0:
            cut += 0.20
        if H < 650.0:
            cut += 0.10
        if H < 640.0:
            cut += 0.05
        if H < 630.0:
            cut += 0.05
        return (1.0 - cut) * P_bar
    pol["cpm"] = {"fn": cpm, "thresholds": [660.0, 650.0, 640.0, 630.0],
                  "label": "CPM cascade 660/650/640/630, cuts 20/30/35/40% (stages II-IV declared [N])"}
    return pol


# ---------------------------------------------------------------- kernels


def _pieces(thresholds):
    """Split [H_LO, H_HI] at policy jump thresholds -> [(lo, hi), ...]."""
    ts = sorted(t for t in thresholds if H_LO < t <= H_HI)
    bounds = [H_LO] + ts + [H_HI]
    out = []
    for i in range(len(bounds) - 1):
        lo, hi = bounds[i], bounds[i + 1]
        if hi > lo:
            out.append((lo, hi))
    return out


def _normalize(intervals):
    ivs = sorted((float(lo), float(hi)) for lo, hi in intervals if hi > lo + 1e-12)
    merged = []
    for lo, hi in ivs:
        if merged and lo <= merged[-1][1] + 1e-12:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))
    return merged


def kernel(policy, fit, R_lo, K, T):
    """Robust T-year kernel (T='inf' -> fixpoint). Union of intervals or None.

    K_{n+1} = { H in [K, H_HI] : aH + alpha + beta R_lo + gamma P(H) in K_n },
    K_0 = [K, H_HI].  worst_next is piecewise affine increasing (a>0) with
    downward jumps at cut-removal thresholds, so kernels are interval unions.
    """
    a, alpha, beta, gamma = fit["a"], fit["alpha"], fit["beta"], fit["gamma"]
    fn, th = policy["fn"], policy["thresholds"]
    pcs = _pieces(th)

    def piece_const(lo, hi):
        return fn(0.5 * (lo + min(hi, lo + 1e-9)))

    K0 = _normalize([(K, H_HI)])
    cur = K0
    max_iter = 1 if T == 1 else (300 if T == "inf" else int(T))
    for _ in range(max_iter):
        nxt = []
        for (plo, phi) in pcs:
            c = alpha + beta * R_lo + gamma * piece_const(plo, phi)
            for (ulo, uhi) in cur:
                # preimage of [ulo, uhi] under H -> aH + c  (a > 0)
                pl = (ulo - c) / a
                ph = (uhi - c) / a
                lo = max(pl, plo, K)
                hi = min(ph, phi, H_HI)
                if hi > lo:
                    nxt.append((lo, hi))
        nxt = _normalize(nxt)
        if not nxt:
            return None
        if T == "inf":
            if len(nxt) == len(cur) and all(
                abs(nl - cl) < 1e-9 and abs(nh - ch) < 1e-9
                for (nl, nh), (cl, ch) in zip(nxt, cur)
            ):
                return nxt
        cur = nxt
    return cur


def kernel_inf_stable(policy, fit, R_lo, K):
    out = kernel(policy, fit, R_lo, K, "inf")
    if out is None:
        return None
    # verify stability: one more step must not shrink
    a, alpha, beta, gamma = fit["a"], fit["alpha"], fit["beta"], fit["gamma"]
    fn, th = policy["fn"], policy["thresholds"]
    pcs = _pieces(th)
    nxt = []
    for (plo, phi) in pcs:
        c = alpha + beta * R_lo + gamma * fn(0.5 * (plo + min(phi, plo + 1e-9)))
        for (ulo, uhi) in out:
            lo = max((ulo - c) / a, plo, K)
            hi = min((uhi - c) / a, phi, H_HI)
            if hi > lo:
                nxt.append((lo, hi))
    nxt = _normalize(nxt)
    if not nxt:
        return None
    return out if len(nxt) == len(out) else None


def boundary(k):
    if k is None:
        return None
    return round(k[0][0], 3)


def contains(k, x):
    if k is None:
        return False
    return any(lo <= x <= hi for lo, hi in k)


# ---------------------------------------------------------------- replays


def supply_replay_actual(panel, policy):
    """Mean prescribed pumping with P_{t+1} = pi(H_t^obs). No dynamics used."""
    yr = panel["year"].to_numpy()
    H = panel["H_mean"].to_numpy(float)
    m = (yr >= 1934) & (yr <= TRAIN_END - 0)  # transitions t->t+1 with t in train
    Ps = [policy["fn"](H[i]) for i in range(len(H) - 1) if yr[i] <= TRAIN_END]
    P_bar = float(np.mean([p for p in Ps]))
    cut_frac = float(np.mean([1.0 if policy["fn"](H[i]) < policy["fn"](H_HI) - 1e-9 else 0.0
                              for i in range(len(H) - 1) if yr[i] <= TRAIN_END]))
    # OOS replay: t in 1991..2022 (transition into 1992..2023)
    Ps_oos = [policy["fn"](H[i]) for i in range(len(H) - 1) if yr[i] > TRAIN_END]
    return {
        "train_mean_P": round(P_bar, 2),
        "train_cut_active_fraction": round(cut_frac, 3),
        "oos_mean_P": round(float(np.mean(Ps_oos)), 2) if Ps_oos else None,
    }


def model_replay(panel, policy, fit, y0, y1):
    """Closed-loop model replay from the observed head in year y0, using the
    actual recharge sequence, policy reacting to model heads."""
    yr = panel["year"].to_numpy()
    H = panel["H_mean"].to_numpy(float)
    R = panel["R_total"].to_numpy(float)
    i0 = int(np.where(yr == y0)[0][0])
    i1 = int(np.where(yr == y1)[0][0])
    h = H[i0]
    path = [(int(yr[i0]), round(float(h), 2))]
    for i in range(i0, i1):
        P = policy["fn"](h)
        h = fit["a"] * h + fit["alpha"] + fit["beta"] * R[i + 1] + fit["gamma"] * P
        path.append((int(yr[i + 1]), round(float(h), 2)))
    return path


# ---------------------------------------------------------------- main


def main() -> None:
    panel = load_panel()
    fit = fit_affine(panel)
    if not all(fit["signs"].values()):
        raise SystemExit(f"fit sign/contraction assumptions violated: {fit['signs']}")

    yr = panel["year"].to_numpy()
    tr_mask = yr <= TRAIN_END
    P_bar = float(panel["P_wells"].to_numpy(float)[tr_mask].mean())
    R_tr = panel["R_total"].to_numpy(float)[tr_mask]
    UC = {
        "UC_min": float(R_tr.min()),
        "UC_q05": float(np.percentile(R_tr, 5)),
        "UC_q10": float(np.percentile(R_tr, 10)),
    }
    policies = make_policies(P_bar)

    # erosion factors (discrete contraction accumulation)
    a, eps = fit["a"], fit["train_residual_max"]
    erosion = {str(T): (eps / (1 - a) if T == "inf"
                        else eps * (1 - a ** T) / (1 - a))
               for T in HORIZONS}
    erosion = {k: round(v, 3) for k, v in erosion.items()}

    # kernels: policy -> uc -> K-name -> T -> {nominal, certified}
    kern = {}
    for pid, pol in policies.items():
        kern[pid] = {}
        for ucid, R_lo in UC.items():
            kern[pid][ucid] = {}
            for Kname, K in (("K_phys_618", K_PHYS), ("K_inst_660", K_INST)):
                row = {}
                for T in HORIZONS:
                    rT = erosion[str(T)]
                    nom = (kernel_inf_stable(pol, fit, R_lo, K) if T == "inf"
                           else kernel(pol, fit, R_lo, K, T))
                    cert = (kernel_inf_stable(pol, fit, R_lo, K + rT) if T == "inf"
                            else kernel(pol, fit, R_lo, K + rT, T))
                    row[str(T)] = {
                        "nominal": [list(iv) for iv in nom] if nom else None,
                        "certified": [list(iv) for iv in cert] if cert else None,
                    }
                kern[pid][ucid][Kname] = row

    # worst-case steady states (attractor of the worst-case map from below)
    steady = {}
    for pid, pol in policies.items():
        steady[pid] = {}
        for ucid, R_lo in UC.items():
            if not pol["thresholds"]:
                c0 = fit["alpha"] + fit["beta"] * R_lo
                s = (c0 + fit["gamma"] * pol["fn"](H_LO)) / (1 - fit["a"])
                steady[pid][ucid] = round(float(s), 2)
            else:
                # iterate the worst-case map from the domain floor; the cut
                # branch active near the attractor is the one the trajectory
                # locks onto (attractor < 660 for every declared UC here)
                h = H_LO
                for _ in range(400):
                    h2 = fit["a"] * h + fit["alpha"] + fit["beta"] * R_lo \
                        + fit["gamma"] * pol["fn"](h)
                    if abs(h2 - h) < 1e-10:
                        break
                    h = h2
                steady[pid][ucid] = round(float(h), 2)

    # minimal flat cut securing K_phys under UC_min (analytic, s* >= 618)
    c0_min = fit["alpha"] + fit["beta"] * UC["UC_min"]
    rho_star = (K_PHYS * (1 - fit["a"]) - c0_min) / (fit["gamma"] * P_bar)
    rho_star = float(min(max(rho_star, 0.0), 1.0))

    # supply replays (actual-head prescription; no dynamics)
    supply = {pid: supply_replay_actual(panel, pol) for pid, pol in policies.items()}

    # 1950s stress counterfactual (model replay from observed 1950 head)
    stress = {}
    for pid, pol in policies.items():
        path = model_replay(panel, pol, fit, 1950, 1956)
        hs = [h for _, h in path]
        stress[pid] = {
            "path": path,
            "min_H": round(min(hs), 2),
            "stayed_above_618": bool(min(hs) >= K_PHYS),
            "note": "model replay from observed H_1950 with actual 1951-1956 recharge",
        }
    # fit diagnostic: open-loop replay with ACTUAL R and P vs actual heads
    yr_ = panel["year"].to_numpy()
    H_ = panel["H_mean"].to_numpy(float)
    R_ = panel["R_total"].to_numpy(float)
    P_ = panel["P_wells"].to_numpy(float)
    i0 = int(np.where(yr_ == 1950)[0][0])
    i1 = int(np.where(yr_ == 1956)[0][0])
    h = H_[i0]
    openloop = []
    for i in range(i0, i1 + 1):
        if i > i0:
            h = fit["a"] * h + fit["alpha"] + fit["beta"] * R_[i] + fit["gamma"] * P_[i]
        openloop.append((int(yr_[i]), round(float(h), 2), round(float(H_[i]), 2)))
    ol_err = [m - a for _, m, a in openloop[1:]]
    bau_diag = {
        "openloop_actual_RP": openloop,
        "openloop_max_abs_error": round(float(np.max(np.abs(ol_err))), 2),
        "note": "model with actual recharge and pumpage vs actual heads, 1951-1956",
    }

    # classification of actual annual states (T=5 kernels)
    H_all = panel["H_mean"].to_numpy(float)
    yr_all = panel["year"].to_numpy(int)
    i_act = panel.set_index("year")["H_mean"]
    focus_years = [1951, 1952, 1953, 1954, 1955, 1956, 2011, 2012, 2013, 2014]
    classification = {}
    for pid in ("BAU", "S1", "cpm"):
        classification[pid] = {}
        for ucid in UC:
            classification[pid][ucid] = {}
            for Kname, K in (("K_phys_618", K_PHYS), ("K_inst_660", K_INST)):
                r5 = erosion["5"]
                k_nom = kernel(policies[pid], fit, UC[ucid], K, 5)
                k_cert = kernel(policies[pid], fit, UC[ucid], K + r5, 5)
                out_nom = [int(y) for y, h in zip(yr_all, H_all) if not contains(k_nom, h)]
                out_cert = [int(y) for y, h in zip(yr_all, H_all) if not contains(k_cert, h)]
                classification[pid][ucid][Kname] = {
                    "nominal_outside_T5": out_nom,
                    "certified_outside_T5": out_cert,
                    "focus_years_inside_nominal": {
                        str(y): contains(k_nom, float(i_act.loc[y])) for y in focus_years},
                    "focus_years_inside_certified": {
                        str(y): contains(k_cert, float(i_act.loc[y])) for y in focus_years},
                }

    # retention mechanics (frozen rule, mechanical ingredients)
    flats = ["flat_90", "flat_80", "flat_70", "flat_60", "flat_50", "flat_0"]
    mods = ["S1", "cpm"]

    def bnd(pid, ucid, Kname, T, level="nominal"):
        k = kern[pid][ucid][Kname][str(T)][level]
        return None if k is None else k[0][0]  # None = empty = worst

    def le(p, q):
        # p <= q with empty = +inf
        if p is None:
            return q is None
        return q is None or p <= q + 1e-9

    def lt(p, q):
        # v2: strictly more protective with empty = +inf (worst) in BOTH
        # arguments, consistent with le — ported from the cod runner's
        # corrected comparator. The v1 form treated a module's empty kernel
        # as improving on a nonempty BAU kernel (p is None -> q is not None)
        # and did not credit improvement over an empty BAU kernel; both
        # directions were verified inert for the committed artifacts.
        if p is None:
            return False
        return q is None or p < q - 1e-9

    def retention_rule(level):
        out = {}
        for pid in mods:
            a_ok = True
            improves = False
            for ucid in UC:
                for Kname in ("K_phys_618", "K_inst_660"):
                    for T in HORIZONS:
                        if not le(bnd(pid, ucid, Kname, T, level),
                                  bnd("BAU", ucid, Kname, T, level)):
                            a_ok = False
                        if lt(bnd(pid, ucid, Kname, T, level),
                               bnd("BAU", ucid, Kname, T, level)):
                            improves = True
            per_reading = {}
            for ucid in UC:
                for Kname in ("K_phys_618", "K_inst_660"):
                    reading = f"{ucid}/{Kname}"
                    dominating = [r for r in ["BAU"] + flats
                                  if all(le(bnd(r, ucid, Kname, T, level),
                                            bnd(pid, ucid, Kname, T, level))
                                         for T in HORIZONS)]
                    best = None
                    for r in dominating:
                        if supply[pid]["train_mean_P"] > supply[r]["train_mean_P"] + 1e-9:
                            if best is None or supply[r]["train_mean_P"] > supply[best]["train_mean_P"]:
                                best = r
                    improves_here = any(lt(bnd(pid, ucid, Kname, T, level),
                                            bnd("BAU", ucid, Kname, T, level))
                                         for T in HORIZONS)
                    per_reading[reading] = {
                        "module_improves_on_BAU": improves_here,
                        "flat_caps_at_least_as_protective": dominating,
                        "supply_win_vs": best,
                        "module_supply": supply[pid]["train_mean_P"],
                    }
            retained_readings = [r for r, v in per_reading.items()
                                 if v["module_improves_on_BAU"] and v["supply_win_vs"]]
            out[pid] = {
                "clause_a_at_least_as_protective_as_BAU_everywhere": a_ok,
                "improves_somewhere": improves,
                "per_reading": per_reading,
                "retained_readings": retained_readings,
                "retained": bool(a_ok and improves and retained_readings),
            }
        return out

    retention = retention_rule("nominal")
    retention_certified = retention_rule("certified")

    # certified horizon per policy: largest T with nonempty certified kernel
    cert_horizon = {}
    for pid in policies:
        cert_horizon[pid] = {}
        for ucid in UC:
            for Kname in ("K_phys_618", "K_inst_660"):
                hs = [T for T in HORIZONS
                      if kern[pid][ucid][Kname][str(T)]["certified"] is not None]
                cert_horizon[pid][f"{ucid}/{Kname}"] = (
                    max([t for t in hs if t != "inf"], default=None)
                    if "inf" not in hs else "inf")

    results = {
        "provenance": {
            "protocol": "protocol_intervention.md (locked 2026-08-26)",
            "data": "data/annual_panel.csv (locked 20-column panel; no new data)",
            "fit_window": "1934-1990 (transitions with both endpoints <= 1990)",
            "oos_window": "1991-2023 (defect audit only; no refitting)",
            "z": "J-17 annual mean ft AMSL (measured; not an assessment inversion)",
            "mapping_type": "APPROXIMATION (R04.Cor2); never EXACT_SPECIALIZATION of A005",
            "k_thresholds_declared_N": {"K_phys": K_PHYS, "K_inst": K_INST},
        },
        "fit": fit,
        "declared": {
            "P_bar_train": round(P_bar, 2),
            "uncertainty_classes": {k: round(v, 1) for k, v in UC.items()},
            "policies": {pid: pol["label"] for pid, pol in policies.items()},
            "horizons": [str(T) for T in HORIZONS],
            "model_domain": [H_LO, H_HI],
        },
        "erosion": {
            "eps_uniform_declaration_train_max": eps,
            "eps_audit_oos_max": fit["oos_residual_max"],
            "eps_audit_train_sd": fit["train_residual_sd"],
            "r_T": erosion,
            "formula": "r_T = eps (1 - a^T)/(1 - a); discrete-contraction form of the Cor2/Cor5 conversion",
        },
        "steady_states_worst_case": steady,
        "minimal_flat_cut_K_phys_UC_min": {
            "rho_star": round(rho_star, 4),
            "cut_percent": round((1 - rho_star) * 100, 2),
            "meaning": "smallest flat cut whose worst-case steady state >= 618 ft under UC_min",
        },
        "supply": supply,
        "stress_replay_1950s": stress,
        "fit_diagnostic_1950s": bau_diag,
        "classification_T5": classification,
        "retention": retention,
        "retention_certified": retention_certified,
        "certified_horizon_nonempty": cert_horizon,
        "kernels": kern,
    }

    OUT.mkdir(exist_ok=True)
    with open(OUT / "intervention_results_v2.json", "w") as f:
        json.dump(results, f, indent=1)

    # boundaries CSV
    with open(OUT / "intervention_boundaries_v2.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["policy", "uc", "K", "T", "nominal_boundary", "certified_boundary",
                    "nominal_intervals", "certified_intervals"])
        for pid in policies:
            for ucid in UC:
                for Kname in ("K_phys_618", "K_inst_660"):
                    for T in HORIZONS:
                        row = kern[pid][ucid][Kname][str(T)]
                        w.writerow([pid, ucid, Kname, T,
                                    boundary(row["nominal"]), boundary(row["certified"]),
                                    row["nominal"], row["certified"]])

    # console summary
    print(f"fit: a={fit['a']:.4f} beta={fit['beta']:.4f} gamma={fit['gamma']:.5f}")
    print(f"eps train max={fit['train_residual_max']:.2f} sd={fit['train_residual_sd']:.2f} "
          f"oos max={fit['oos_residual_max']:.2f}")
    print(f"P_bar={P_bar:.1f} UC={ {k: round(v,1) for k,v in UC.items()} }")
    print(f"minimal flat cut for K_phys under UC_min: {(1-rho_star)*100:.1f}%")
    print("steady states (worst-case attractors):")
    for pid in steady:
        print(f"  {pid:8s} " + "  ".join(f"{u}={s}" for u, s in steady[pid].items()))
    for pid in ("BAU", "flat_80", "S1", "cpm"):
        s = supply[pid]
        print(f"supply {pid:8s} train mean P={s['train_mean_P']} cut frac={s['train_cut_active_fraction']}")
    for pid in ("BAU", "flat_80", "S1", "cpm"):
        st = stress[pid]
        print(f"stress {pid:8s} min H={st['min_H']} >=618: {st['stayed_above_618']}")
    print("certified horizons (largest nonempty T):")
    for pid in ("BAU", "flat_90", "flat_80", "S1", "cpm", "flat_0"):
        print(f"  {pid:8s} " + "  ".join(f"{r}={t}" for r, t in cert_horizon[pid].items()))
    print("retention (nominal):")
    for pid, r in retention.items():
        print(f"  {pid}: retained={r['retained']} "
              f"(a_ok={r['clause_a_at_least_as_protective_as_BAU_everywhere']}, "
              f"improves={r['improves_somewhere']}, readings={r['retained_readings']})")
    print("retention (certified):")
    for pid, r in retention_certified.items():
        print(f"  {pid}: retained={r['retained']} "
              f"(a_ok={r['clause_a_at_least_as_protective_as_BAU_everywhere']}, "
              f"improves={r['improves_somewhere']}, readings={r['retained_readings']})")
    print("wrote results/intervention_results_v2.json and results/intervention_boundaries_v2.csv")


if __name__ == "__main__":
    main()
