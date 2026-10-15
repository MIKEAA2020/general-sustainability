#!/usr/bin/env python3
"""
Wave E intervention-selection leg — Northern cod (NAFO 2J3KL), Omega_2016.

Executes protocol_intervention.md (frozen 2026-08-26, before any kernel,
boundary, replay, or retention score was computed): robust viability kernels
of the LRP safe set for a declared catch-policy family under persistent
productivity-shock floors, with the Cor2/Cor5 erosion conversion (expansive
or contraction form, whichever the fitted map admits), supply and stress
replays, a T=5 classification of the observed states, and the frozen
retention rule. The cod-side analogue of wave_e_edwards/src/run_intervention.py.

No forecast module is promoted or demoted here. The survey-start variant, the
oracle, and capelin modules play no role. No Omega_xte row is produced. No
Allee term (the M2 class). Deterministic; no randomness anywhere.

Run:  python3 src/run_intervention.py
Out:  results/intervention_results.json
      results/intervention_boundaries.csv
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results"
sys.path.insert(0, str(ROOT / "src"))
from run_ladder import fit_params, load, surplus  # noqa: E402

S_LO, S_HI = 1.0e-3, 10000.0     # declared model domain (protocol §1)
K_STAR = 884.6                    # LRP safe set [N]; set exactly below
TRAIN_END = 2007                  # fit window 1983-2007; OOS audit 2008-2015
HORIZONS = [1, 2, 3, 5, 8, 10, 15, 20, "inf"]
P_BAR = 240.0                     # pre-1992 directed-fishery level [E]


# ---------------------------------------------------------------- fit


def fit_surplus():
    years, ssb, c_reg, c_ann, idx, lrp = load()
    m_tr = years <= TRAIN_END
    p = fit_params(ssb[m_tr], c_ann[m_tr], allee=False)
    r, K = float(p["r"]), float(p["K"])
    # one-step residuals of the fitted map (annual catch)
    res = {}
    for j in range(len(years) - 1):
        pred = ssb[j] + surplus(ssb[j], r, K) - c_ann[j + 1]
        res[int(years[j + 1])] = float(ssb[j + 1] - pred)
    res_tr = np.array([res[y] for y in sorted(res) if y <= TRAIN_END])
    res_oos = np.array([res[y] for y in sorted(res) if y > TRAIN_END])
    i_max = int(np.argmax(np.abs(res_tr)))
    yrs_sorted = [y for y in sorted(res) if y <= TRAIN_END]
    return {
        "r": r, "K": K,
        "K_pinned_at_bound": bool(K >= 5000.0 - 1e-9),
        "n_train_transitions": int(len(res_tr)),
        "n_oos_transitions": int(len(res_oos)),
        "train_residual_sd": float(res_tr.std(ddof=1)),
        "train_residual_max": float(np.abs(res_tr).max()),
        "train_residual_max_year": int(yrs_sorted[i_max]),
        "train_residual_min": float(res_tr.min()),
        "train_residual_q05": float(np.percentile(res_tr, 5)),
        "train_residual_q10": float(np.percentile(res_tr, 10)),
        "oos_residual_sd": float(res_oos.std(ddof=1)) if len(res_oos) > 1 else None,
        "oos_residual_max": float(np.abs(res_oos).max()),
        "oos_residual_max_year": int([y for y in sorted(res) if y > TRAIN_END]
                                     [int(np.argmax(np.abs(res_oos)))]),
        "oos_exceeds_declaration": bool(np.abs(res_oos).max()
                                        > np.abs(res_tr).max()),
        "signs": {"r_positive": bool(r > 0), "lrp_check": bool(abs(lrp - 884.58) < 0.1)},
        "_years": years, "_ssb": ssb, "_c_ann": c_ann, "_res": res,
    }


# ---------------------------------------------------------------- policies


def make_policies():
    pol = {}

    def flat(c, label):
        return {"fn": lambda S, c=c: c, "thresholds": [], "label": label}

    pol["BAU"] = flat(5.0, "moratorium-level inshore removals (C = 5 kt)")
    for rho, pid in ((1.0, "flat_100"), (0.75, "flat_75"), (0.5, "flat_50"),
                     (0.25, "flat_25"), (0.0, "flat_0")):
        pol[pid] = flat(rho * P_BAR, f"flat cap C = {rho:.2f} x 240 kt")

    def s1(S):
        return 60.0 if S >= K_STAR else 0.0
    pol["S1"] = {"fn": s1, "thresholds": [K_STAR],
                 "label": "PA critical-zone rule: C = 60 kt above LRP, 0 below"}

    def cpm(S):
        if S >= K_STAR:
            return 60.0
        if S >= 0.75 * K_STAR:
            return 30.0
        if S >= 0.5 * K_STAR:
            return 5.0
        return 0.0
    pol["cpm"] = {"fn": cpm, "thresholds": [0.5 * K_STAR, 0.75 * K_STAR, K_STAR],
                  "label": "cascade LRP/0.75LRP/0.5LRP: 60/30/5/0 kt (declared [N])"}
    return pol


# ---------------------------------------------------------------- kernels


def _pieces(thresholds):
    ts = sorted(t for t in thresholds if S_LO < t <= S_HI)
    bounds = [S_LO] + ts + [S_HI]
    return [(bounds[i], bounds[i + 1]) for i in range(len(bounds) - 1)
            if bounds[i + 1] > bounds[i]]


def _normalize(intervals):
    ivs = sorted((float(lo), float(hi)) for lo, hi in intervals if hi > lo + 1e-12)
    merged = []
    for lo, hi in ivs:
        if merged and lo <= merged[-1][1] + 1e-12:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))
    return merged


def _quadratic(r, K, c, e):
    """F(S) = -(r/K) S^2 + (1+r) S + (e - c).  Return (a, b, cc) with
    F(S) = a S^2 + b S + cc."""
    return (-(r / K), 1.0 + r, e - c)


def _roots(a, b, cc, level):
    """Roots of a S^2 + b S + cc = level (a < 0, concave).  Returns
    ('two', (lo, hi)) if two real roots;
    ('below', None) if F < level everywhere (vertex below level);
    ('above', None) if F > level everywhere (vertex above level)."""
    disc = b * b - 4.0 * a * (cc - level)
    if disc < 0.0:
        s_v = -b / (2.0 * a)
        return ("above", None) if (a * s_v * s_v + b * s_v + cc) > level \
            else ("below", None)
    s = np.sqrt(disc)
    x1, x2 = (-b - s) / (2 * a), (-b + s) / (2 * a)
    return ("two", (min(x1, x2), max(x1, x2)))


def _preimage(r, K, c, e, plo, phi, ulo, uhi):
    """{S in [plo, phi] : ulo <= F(S) <= uhi} for the concave quadratic F."""
    a, b, cc = _quadratic(r, K, c, e)
    kind_lo, lo_roots = _roots(a, b, cc, ulo)
    if kind_lo == "below":
        return []                      # F < ulo everywhere
    if kind_lo == "above":
        set_ge_lo = [(plo, phi)]       # F > ulo everywhere
    else:
        A, B = lo_roots
        set_ge_lo = [(max(A, plo), min(B, phi))]
    kind_hi, hi_roots = _roots(a, b, cc, uhi)
    if kind_hi == "above":
        return []                      # F > uhi everywhere
    if kind_hi == "below":
        set_le_hi = [(plo, phi)]       # F < uhi everywhere
    else:
        C, D = hi_roots
        set_le_hi = [(plo, min(C, phi)), (max(D, plo), phi)]
    out = []
    for (l1, h1) in set_ge_lo:
        for (l2, h2) in set_le_hi:
            lo, hi = max(l1, l2), min(h1, h2)
            if hi > lo:
                out.append((lo, hi))
    return out


def kernel(policy, fit, e, K, T):
    """Robust T-step kernel (T='inf' -> fixpoint).  Interval union or None.

    K_{n+1} = { S in [K, S_HI] : F(S) in K_n }, K_0 = [K, S_HI], where F is
    the worst-case closed loop with the persistent floor e and the policy's
    piecewise-constant catch.  The [EPS, 1e6] clip of the ladder's step never
    binds for membership: K_n lives inside [K, S_HI] with K = 884.6 kt >> EPS.
    """
    r, Kc = fit["r"], fit["K"]
    pcs = _pieces(policy["thresholds"])

    def piece_c(plo, phi):
        return float(policy["fn"](0.5 * (plo + phi)))

    K0 = _normalize([(K, S_HI)])
    cur = K0
    max_iter = 1 if T == 1 else (300 if T == "inf" else int(T))
    for _ in range(max_iter):
        nxt = []
        for (plo, phi) in pcs:
            c = piece_c(plo, phi)
            for (ulo, uhi) in cur:
                nxt.extend(_preimage(r, Kc, c, e, max(plo, K), phi, ulo, uhi))
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


def kernel_inf_stable(policy, fit, e, K):
    out = kernel(policy, fit, e, K, "inf")
    if out is None:
        return None
    r, Kc = fit["r"], fit["K"]
    pcs = _pieces(policy["thresholds"])
    nxt = []
    for (plo, phi) in pcs:
        c = float(policy["fn"](0.5 * (plo + phi)))
        for (ulo, uhi) in out:
            nxt.extend(_preimage(r, Kc, c, e, max(plo, K), phi, ulo, uhi))
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


def supply_replay(fit, policy):
    yr, ssb = fit["_years"], fit["_ssb"]
    tr = [policy["fn"](float(ssb[i])) for i in range(len(yr) - 1)
          if yr[i] < TRAIN_END]
    oos = [policy["fn"](float(ssb[i])) for i in range(len(yr) - 1)
           if yr[i] >= TRAIN_END]
    cap = policy["fn"](float(S_HI))
    return {
        "train_mean_C": round(float(np.mean(tr)), 2),
        "train_cut_active_fraction": round(
            float(np.mean([1.0 if c < cap - 1e-9 else 0.0 for c in tr])), 3),
        "oos_mean_C": round(float(np.mean(oos)), 2),
    }


def stress_replay(fit, policy, y0=1990, y1=1995):
    """Closed-loop replay from observed SSB in y0 using the OBSERVED
    residuals y0+1..y1 (the crash years), policy reacting to model states."""
    yr, ssb, res = fit["_years"], fit["_ssb"], fit["_res"]
    r, K = fit["r"], fit["K"]
    i0 = int(np.where(yr == y0)[0][0])
    i1 = int(np.where(yr == y1)[0][0])
    s = float(ssb[i0])
    path = [(int(yr[i0]), round(s, 2))]
    for i in range(i0, i1):
        C = policy["fn"](s)
        s = float(np.clip(s + surplus(s, r, K) - C + res[int(yr[i + 1])],
                          S_LO, 1.0e6))
        path.append((int(yr[i + 1]), round(s, 2)))
    return {
        "path": path,
        "min_S": round(min(v for _, v in path), 2),
        "stayed_above_LRP": bool(min(v for _, v in path) >= K_STAR),
        "note": f"model replay from observed SSB {y0} with the observed "
                f"{y0 + 1}-{y1} residuals, per policy",
    }


# ---------------------------------------------------------------- main


def main() -> None:
    fit = fit_surplus()
    r, K = fit["r"], fit["K"]
    if not fit["signs"]["r_positive"]:
        raise SystemExit("fit sign assumptions violated")

    UC = {
        "UC_min": fit["train_residual_min"],
        "UC_q05": fit["train_residual_q05"],
        "UC_q10": fit["train_residual_q10"],
    }
    policies = make_policies()

    # erosion: the closed loop's expansion rate on the safe domain
    # F'(S) = 1 + r(1 - 2S/K), decreasing in S -> sup over [K_STAR, S_HI]
    # is attained at S = K_STAR.
    a_star = 1.0 + r * (1.0 - 2.0 * K_STAR / K)
    a_at_hi = 1.0 + r * (1.0 - 2.0 * S_HI / K)
    eps = fit["train_residual_max"]
    contractive = bool(a_star < 1.0)
    if contractive:
        erosion = {str(T): (eps / (1 - a_star) if T == "inf"
                            else eps * (1 - a_star ** T) / (1 - a_star))
                   for T in HORIZONS}
        form = (f"contraction form: a = {a_star:.4f} < 1 at the safe-set "
                f"boundary; r_T = eps(1-a^T)/(1-a)")
    else:
        erosion = {str(T): (eps * (a_star ** T - 1.0) / (a_star - 1.0)
                            if T != "inf" else float("inf"))
                   for T in HORIZONS}
        form = (f"expansive form: a_max = sup F' on [K*, S_HI] = {a_star:.4f} "
                f"> 1 at the safe-set boundary (F'(S) decreasing in S; "
                f"F'(S_HI) = {a_at_hi:.4f}); the contraction form of the "
                f"Cor2/Cor5 conversion is INAPPLICABLE; "
                f"r_T = eps(a_max^T - 1)/(a_max - 1)")
    erosion = {k: (round(v, 3) if np.isfinite(v) else None)
               for k, v in erosion.items()}

    # kernels: policy -> uc -> T -> {nominal, certified}
    kern = {}
    for pid, pol in policies.items():
        kern[pid] = {}
        for ucid, e in UC.items():
            row = {}
            for T in HORIZONS:
                rT = erosion[str(T)]
                nom = (kernel_inf_stable(pol, fit, e, K_STAR) if T == "inf"
                       else kernel(pol, fit, e, K_STAR, T))
                cert = None
                if rT is not None:
                    cert = (kernel_inf_stable(pol, fit, e, K_STAR + rT)
                            if T == "inf"
                            else kernel(pol, fit, e, K_STAR + rT, T))
                row[str(T)] = {
                    "nominal": [list(iv) for iv in nom] if nom else None,
                    "certified": [list(iv) for iv in cert] if cert else None,
                }
            kern[pid][ucid] = row

    # worst-case invariant interval of the branch active at the safe set
    # (fixed points of F: g(S) = C - e on the C-branch active at S = K_STAR),
    # the one-step extinction threshold (smaller positive zero of F), and
    # the from-below attractor of the full worst-case closed loop
    steady = {}
    for pid, pol in policies.items():
        steady[pid] = {}
        for ucid, e in UC.items():
            c = float(pol["fn"](K_STAR))
            # fixed points: F(S) = S  <=>  -(r/K) S^2 + r S + (e - c) = 0
            roots = np.roots([-(r / K), r, e - c])
            pos = sorted(x.real for x in roots
                         if abs(x.imag) < 1e-9 and x.real > 0)
            # one-step extinction threshold: smaller positive zero of F
            zeros = np.roots([-(r / K), 1.0 + r, e - c])
            zpos = sorted(x.real for x in zeros
                          if abs(x.imag) < 1e-9 and x.real > 0)
            s = S_LO
            for _ in range(400):
                s2 = float(np.clip(s + surplus(s, r, K)
                                   - float(pol["fn"](s)) + e, S_LO, 1.0e6))
                if abs(s2 - s) < 1e-10:
                    break
                s = s2
            steady[pid][ucid] = {
                "catch_at_LRP_branch": c,
                "worst_case_fixed_points": [round(x, 2) for x in pos],
                "one_step_extinction_threshold": round(zpos[0], 2) if zpos else None,
                "attractor_from_below": round(s, 3),
            }

    # maximal robust flat catch per UC (low equilibrium <= K_STAR)
    max_flat = {}
    for ucid, e in UC.items():
        c_star = float(r * K_STAR * (1.0 - K_STAR / K) + e)
        # verify: fixed points of F with C = c_star  (g(S) = c_star - e)
        roots = np.roots([-(r / K), r, e - c_star])
        pos = sorted(x.real for x in roots if abs(x.imag) < 1e-9 and x.real > 0)
        max_flat[ucid] = {
            "max_flat_catch_kt": round(max(c_star, 0.0), 2),
            "positive": bool(c_star > 0.0),
            "check_fixed_points": [round(x, 2) for x in pos],
            "meaning": "largest constant catch whose worst-case low "
                       "equilibrium stays at or below the LRP",
        }

    supply = {pid: supply_replay(fit, pol) for pid, pol in policies.items()}
    stress = {pid: stress_replay(fit, pol) for pid, pol in policies.items()}

    # T=5 classification of the observed states (nominal level)
    yr_all, ssb_all = fit["_years"], fit["_ssb"]
    classification = {}
    for pid in ("BAU", "S1", "cpm"):
        classification[pid] = {}
        for ucid, e in UC.items():
            k5 = kernel(policies[pid], fit, e, K_STAR, 5)
            classification[pid][ucid] = {
                "nominal_outside_T5": [int(y) for y, s in zip(yr_all, ssb_all)
                                       if not contains(k5, float(s))],
                "note": "observed SSB values outside the policy's T=5 "
                        "nominal kernel at this UC class",
            }

    # retention mechanics (frozen rule, protocol §8)
    flats = ["flat_100", "flat_75", "flat_50", "flat_25", "flat_0"]
    mods = ["S1", "cpm"]

    def bnd(pid, ucid, T, level="nominal"):
        k = kern[pid][ucid][str(T)][level]
        return None if k is None else k[0][0]

    def le(p, q):
        if p is None:
            return q is None
        return q is None or p <= q + 1e-9

    def lt(p, q):
        # strictly more protective: p's boundary strictly below q's, with
        # empty = +inf (worst) — consistent with le; an empty kernel is
        # never an improvement (the Edwards runner's lt treated empty as
        # -inf here, a latent asymmetry that was provably inert for the
        # committed Edwards artifacts: zero module-empty/BAU-nonempty pairs)
        if p is None:
            return False
        return q is None or p < q - 1e-9

    def retention_rule(level):
        out = {}
        for pid in mods:
            a_ok = True
            improves = False
            for ucid in UC:
                for T in HORIZONS:
                    if not le(bnd(pid, ucid, T, level), bnd("BAU", ucid, T, level)):
                        a_ok = False
                    if lt(bnd(pid, ucid, T, level), bnd("BAU", ucid, T, level)):
                        improves = True
            per_reading = {}
            for ucid in UC:
                reading = ucid
                dominating = [q for q in ["BAU"] + flats
                              if all(le(bnd(q, ucid, T, level),
                                        bnd(pid, ucid, T, level))
                                     for T in HORIZONS)]
                best = None
                for q in dominating:
                    if supply[pid]["train_mean_C"] > supply[q]["train_mean_C"] + 1e-9:
                        if best is None or supply[q]["train_mean_C"] > supply[best]["train_mean_C"]:
                            best = q
                improves_here = any(lt(bnd(pid, ucid, T, level),
                                       bnd("BAU", ucid, T, level))
                                    for T in HORIZONS)
                per_reading[reading] = {
                    "module_improves_on_BAU": improves_here,
                    "flat_caps_at_least_as_protective": dominating,
                    "supply_win_vs": best,
                    "module_supply": supply[pid]["train_mean_C"],
                }
            retained_readings = [rdr for rdr, v in per_reading.items()
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

    cert_horizon = {}
    for pid in policies:
        cert_horizon[pid] = {}
        for ucid in UC:
            h = None
            for T in HORIZONS:
                if T == "inf":
                    continue
                if kern[pid][ucid][str(T)]["certified"] is not None:
                    h = T
            cert_horizon[pid][ucid] = h

    results = {
        "title": "Wave E intervention-selection leg — Northern cod "
                 "(Omega_2016): robust kernels of the LRP safe set under "
                 "persistent productivity-shock floors",
        "protocol": "protocol_intervention.md (frozen 2026-08-26, before "
                    "scores)",
        "object": "governed surplus-production object (the ladder's M2 class, "
                  "Allee off); NOT NCAM; no Omega_xte row",
        "fit": {k: v for k, v in fit.items() if not k.startswith("_")},
        "safe_set": {"K_star_kt": K_STAR, "domain": [S_LO, S_HI],
                     "declared": "the 2016 LRP (1983-1989 mean SSB), the "
                                 "single [N] threshold of Omega_2016"},
        "UC": {k: round(v, 2) for k, v in UC.items()},
        "erosion": {
            "form": form,
            "contractive": contractive,
            "a_max": round(a_star, 4),
            "a_at_S_HI": round(a_at_hi, 4),
            "eps_train_max": eps,
            "r_T": erosion,
            "formula": "r_T = eps(1-a^T)/(1-a) if a < 1 (contraction); "
                       "eps(a^T-1)/(a-1) otherwise (expansive); certified "
                       "kernel = nominal kernel of K* + r_T",
        },
        "steady_states": steady,
        "maximal_robust_flat_catch": max_flat,
        "supply": supply,
        "stress_replay_1990s": stress,
        "classification_T5": classification,
        "retention": retention,
        "retention_certified": retention_certified,
        "certified_horizon_nonempty": cert_horizon,
        "kernels": kern,
    }

    OUT.mkdir(exist_ok=True)
    with open(OUT / "intervention_results.json", "w") as f:
        json.dump(results, f, indent=1)

    with open(OUT / "intervention_boundaries.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["policy", "uc", "T", "nominal_boundary", "certified_boundary",
                    "nominal_intervals", "certified_intervals"])
        for pid in policies:
            for ucid in UC:
                for T in HORIZONS:
                    row = kern[pid][ucid][str(T)]
                    w.writerow([pid, ucid, T,
                                boundary(row["nominal"]),
                                boundary(row["certified"]),
                                row["nominal"], row["certified"]])

    # console summary
    print(f"fit (1983-{TRAIN_END}, annual catch): r = {r:.4f}, K = {K:.1f} "
          f"(pinned at bound: {fit['K_pinned_at_bound']})")
    print(f"eps train max = {eps:.1f} kt (year {fit['train_residual_max_year']}); "
          f"sd = {fit['train_residual_sd']:.1f}; "
          f"OOS max = {fit['oos_residual_max']:.1f} "
          f"(exceeds declaration: {fit['oos_exceeds_declaration']})")
    print(f"UC floors: { {k: round(v, 1) for k, v in UC.items()} }")
    print(f"erosion: contractive = {contractive}, a_max = {a_star:.4f}; "
          f"r_1 = {erosion['1']}, r_5 = {erosion['5']}")
    print("worst-case fixed points on the LRP branch "
          "(policy, uc -> [low, high]):")
    for pid in steady:
        for ucid in steady[pid]:
            fp = steady[pid][ucid]["worst_case_fixed_points"]
            print(f"  {pid:9s} {ucid:7s} C={steady[pid][ucid]['catch_at_LRP_branch']:5.1f} "
                  f"-> {fp if fp else 'none (monotone decline)'}")
    print("maximal robust flat catch:", {u: v["max_flat_catch_kt"]
                                         for u, v in max_flat.items()})
    for pid in ("BAU", "flat_25", "S1", "cpm", "flat_0"):
        print(f"supply {pid:9s} train mean C = "
              f"{supply[pid]['train_mean_C']}")
    for pid in ("BAU", "flat_25", "S1", "cpm", "flat_0"):
        print(f"stress {pid:9s} min S = {stress[pid]['min_S']} "
              f">=LRP: {stress[pid]['stayed_above_LRP']}")
    print("kernel lower boundaries (nominal):")
    for pid in ("BAU", "flat_100", "flat_50", "flat_25", "S1", "cpm", "flat_0"):
        line = f"  {pid:9s} "
        for ucid in UC:
            b1 = boundary(kern[pid][ucid]["1"]["nominal"])
            bi = boundary(kern[pid][ucid]["inf"]["nominal"])
            line += f"{ucid}: T1={b1} Tinf={bi}  "
        print(line)
    print("certified horizons (largest nonempty T):")
    for pid in ("BAU", "flat_25", "S1", "cpm", "flat_0"):
        print(f"  {pid:9s} " + "  ".join(f"{u}={cert_horizon[pid][u]}"
                                         for u in UC))
    print("retention (nominal):")
    for pid, rr in retention.items():
        print(f"  {pid}: retained={rr['retained']} "
              f"(a_ok={rr['clause_a_at_least_as_protective_as_BAU_everywhere']}, "
              f"improves={rr['improves_somewhere']}, "
              f"readings={rr['retained_readings']})")
    print("retention (certified):")
    for pid, rr in retention_certified.items():
        print(f"  {pid}: retained={rr['retained']} "
              f"(a_ok={rr['clause_a_at_least_as_protective_as_BAU_everywhere']}, "
              f"improves={rr['improves_somewhere']}, "
              f"readings={rr['retained_readings']})")
    print("wrote results/intervention_results.json and "
          "results/intervention_boundaries.csv")


if __name__ == "__main__":
    main()
