#!/usr/bin/env python3
"""paper09 v44 exact core -- independent re-derivation of every closed-form and
recursion-based number quoted in the main text and supplement, plus a reader
for the archived campaign outputs (stochastic layer, bootstraps, profile,
forms, recent windows) that the text quotes verbatim.

Two systems, one certification frame:
  * 2J3KL northern cod (Schaefer surplus map, source-year catch, LRP 884.6 kt)
  * Edwards Aquifer J-17 index well (affine recharge/pumping map, 618/660 ft)

Everything here is re-implemented from the data files; nothing is imported from
the registered runners.  Agreement with the registered artefacts is asserted in
`compare_with_archive()` and recorded in results.json["archive_checks"].

Usage:  python3 p09_core.py            (writes results.json beside this file)
"""
from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SRC_CANDIDATES = [HERE.parent / "src", HERE.parent / "paper09_cod_certification_v44_src" / "src",
                  HERE.parent]
for _c in SRC_CANDIDATES:
    if (_c / "wave_e_cod" / "data" / "ncam_2016_table_a2.csv").exists():
        SRC = _c
        break
else:
    raise SystemExit("cannot locate wave_e_cod/data below " + ", ".join(map(str, SRC_CANDIDATES)))
COD = SRC / "wave_e_cod"
EDW = SRC / "wave_e_edwards"

OUT = {}


def rd(x, n=2):
    return None if x is None else float(round(float(x), n))


def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


# =============================================================================
#  Generic one-dimensional kernel machinery (shared by both systems)
# =============================================================================
#  A policy is a list of pieces (lo, hi, control value) covering the state
#  domain; a map F_c(x) = x + G(x, c) - |e| (cod) or an affine map (Edwards).
#  The T-step closed-loop kernel of the safe set W0 under the worst admissible
#  disturbance is computed by the exact backward recursion
#       W_{t+1} = { x in W0 : F(x) in W_t },
#  carried out on finite unions of closed intervals.  Because every piece of F
#  is strictly increasing on its domain, the preimage of an interval under a
#  piece is an interval, obtained from the inverse of the monotone branch.


def normalise(ints, tol=1e-9):
    ints = sorted([list(i) for i in ints if i[1] - i[0] >= -tol])
    out = []
    for lo, hi in ints:
        if out and lo <= out[-1][1] + tol:
            out[-1][1] = max(out[-1][1], hi)
        else:
            out.append([lo, hi])
    return out


def kernel_recursion(pieces, inverse, W0, T, tol=1e-9):
    """pieces: [(lo, hi, c)], inverse(c, y) -> x with F_c(x) = y (monotone
    increasing branch).  Returns the list of kernels W_0..W_T (each a union of
    intervals, possibly empty)."""
    Ws = [normalise([list(W0)])]
    for _ in range(T):
        tgt = Ws[-1]
        nxt = []
        for lo, hi, c in pieces:
            for tlo, thi in tgt:
                a = inverse(c, tlo)
                b = inverse(c, thi)
                a2, b2 = max(a, lo, W0[0]), min(b, hi, W0[1])
                if b2 - a2 >= -tol:
                    nxt.append([a2, b2])
        Ws.append(normalise(nxt, tol))
        if not Ws[-1]:
            break
    return Ws


def lower_boundary(W):
    return None if not W else W[0][0]


# =============================================================================
#  PART I  --  northern cod
# =============================================================================
S_LO, S_HI = 1.0e-3, 10000.0
K_BOX = 5000.0
TRAIN_END = 2007


def cod_data():
    ncam = read_csv(COD / "data" / "ncam_2016_table_a2.csv")
    cat = {int(r["year"]): float(r["catch_kt"]) for r in read_csv(COD / "data" / "catch_schijns_2021.csv")}
    years = np.array([int(r["year"]) for r in ncam])
    ssb = np.array([float(r["ssb_kt"]) for r in ncam])
    C = np.array([cat[y] for y in years])
    return years, ssb, C


def surplus(S, r, K):
    return r * S * (1.0 - S / K)


def r_closed_form(S0, y, K):
    x = S0 * (1.0 - S0 / K)
    return float(np.dot(x, y) / np.dot(x, x))


def sse_profile(S0, y, K):
    r = r_closed_form(S0, y, K)
    return r, float(np.sum((y - r * S0 * (1 - S0 / K)) ** 2))


def fit_cod(years, ssb, C, y0=1983, y1=TRAIN_END, kmax=K_BOX, kmin=None):
    """Source-year one-step least squares: S_{t+1} - S_t + C_t = r S_t (1 - S_t/K).
    r is linear given K (closed form); K is profiled on a fine grid and then
    refined by golden-section search inside the declared box."""
    m = (years >= y0) & (years <= y1)
    S = ssb[m]
    Cw = C[m]
    S0, y = S[:-1], np.diff(S) + Cw[:-1]
    if kmin is None:
        kmin = float(np.max(S0)) + 10.0
    grid = np.linspace(kmin, kmax, 4001)
    sses = np.array([sse_profile(S0, y, K)[1] for K in grid])
    j = int(np.argmin(sses))
    lo, hi = grid[max(j - 1, 0)], grid[min(j + 1, len(grid) - 1)]
    gr = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    c, d = b - gr * (b - a), a + gr * (b - a)
    for _ in range(200):
        if sse_profile(S0, y, c)[1] < sse_profile(S0, y, d)[1]:
            b = d
        else:
            a = c
        c, d = b - gr * (b - a), a + gr * (b - a)
    K = 0.5 * (a + b)
    if sse_profile(S0, y, kmax)[1] <= sse_profile(S0, y, K)[1] + 1e-9:
        K = kmax
    r, sse = sse_profile(S0, y, K)
    return {"r": r, "K": K, "sse": sse, "n": int(len(y)), "S0": S0, "y": y,
            "pinned": bool(abs(K - kmax) < 1e-6)}


def cod_residuals(years, ssb, C, r, K):
    res = {}
    for j in range(len(years) - 1):
        pred = ssb[j] + surplus(ssb[j], r, K) - C[j]
        res[int(years[j + 1])] = float(ssb[j + 1] - pred)
    return res


def quantile_conventions(e, p):
    out = {}
    for meth in ("linear", "lower", "hazen", "weibull", "inverted_cdf"):
        out[meth] = float(np.percentile(e, 100 * p, method=meth))
    return out


def cod_inverse_factory(r, K, e_abs):
    """inverse of F_c(S) = S + rS(1 - S/K) - c - e_abs on the increasing branch
    (S < K(1+r)/(2r), which is far above S_HI for the registered fit)."""
    def inverse(c, y):
        # (1+r) S - (r/K) S^2 = y + c + e_abs ;  take the smaller root
        A, B, Cc = -r / K, 1.0 + r, -(y + c + e_abs)
        disc = B * B - 4 * A * Cc
        if disc < 0:
            return float("inf")
        return (-B + math.sqrt(disc)) / (2 * A)
    return inverse


def flat_pieces(c):
    return [(S_LO, S_HI, c)]


def cod_policies(K_star):
    P = {}
    P["BAU"] = flat_pieces(5.0)
    for rho, name in ((1.0, "flat_100"), (0.75, "flat_75"), (0.5, "flat_50"), (0.25, "flat_25"), (0.0, "flat_0")):
        P[name] = flat_pieces(rho * 240.0)
    P["S1"] = [(S_LO, K_star, 0.0), (K_star, S_HI, 60.0)]
    P["cpm"] = [(S_LO, 0.5 * K_star, 0.0), (0.5 * K_star, 0.75 * K_star, 5.0),
                (0.75 * K_star, K_star, 30.0), (K_star, S_HI, 60.0)]
    P["graded2"] = [(S_LO, K_star, 0.0), (K_star, 1.25 * K_star, 60.0), (1.25 * K_star, S_HI, 90.0)]
    P["graded3"] = [(S_LO, K_star, 0.0), (K_star, 1.25 * K_star, 30.0), (1.25 * K_star, 1.5 * K_star, 60.0),
                    (1.5 * K_star, S_HI, 90.0)]
    return P


def s_minus(level, r, K):
    """smaller root of g(S) = level (None if level > g_max)."""
    if level > r * K / 4 + 1e-12:
        return None
    return 0.5 * K * (1.0 - math.sqrt(max(0.0, 1.0 - 4.0 * level / (r * K))))


def flat_boundaries(c, e_abs, r, K, K_star, Ts):
    inv = cod_inverse_factory(r, K, e_abs)
    Ws = kernel_recursion(flat_pieces(c), inv, (K_star, S_HI), max(t for t in Ts if t != "inf"))
    out = {}
    for T in Ts:
        if T == "inf":
            sm = s_minus(c + e_abs, r, K)
            out["inf"] = None if sm is None else max(K_star, sm)
        else:
            out[str(T)] = lower_boundary(Ws[T]) if T < len(Ws) else None
    return out


def policy_boundaries(pieces, e_abs, r, K, K_star, Ts, Tmax_inf=400):
    inv = cod_inverse_factory(r, K, e_abs)
    Tn = max(t for t in Ts if t != "inf")
    Ws = kernel_recursion(pieces, inv, (K_star, S_HI), Tn)
    out = {}
    for T in Ts:
        if T != "inf":
            out[str(T)] = lower_boundary(Ws[T]) if T < len(Ws) else None
    # T = infinity by iterating to stabilisation
    Wl = kernel_recursion(pieces, inv, (K_star, S_HI), Tmax_inf)
    if len(Wl) < Tmax_inf + 1:
        out["inf"] = None
    else:
        a, b = Wl[-1], Wl[-2]
        stable = len(a) == len(b) and all(abs(x[0] - y[0]) < 1e-6 and abs(x[1] - y[1]) < 1e-6 for x, y in zip(a, b))
        out["inf"] = lower_boundary(a) if stable else ("unstable", lower_boundary(a))
    return out


def certified_horizon(c, e_abs, r, K, K_star, a_max, eps, Tmax=40):
    """certified kernel at horizon T = nominal T-step kernel of the inflated
    threshold K* + r_T, r_T = eps (a^T - 1)/(a - 1).  Returns the last horizon
    at which it is non-empty and the first at which it is empty."""
    inv = cod_inverse_factory(r, K, e_abs)
    last_nonempty, first_empty = 0, None
    for T in range(1, Tmax + 1):
        rT = eps * (a_max ** T - 1) / (a_max - 1)
        Ws = kernel_recursion(flat_pieces(c), inv, (K_star + rT, S_HI), T)
        if len(Ws) == T + 1 and Ws[T]:
            last_nonempty = T
        else:
            first_empty = T
            break
    return last_nonempty, first_empty


def stochastic_survival(r, K, residuals, catch, S0, T, N, rng, scheme="iid", block=4, K_star=None):
    """fraction of N trajectories that stay >= K_star for all t <= T under the
    registered map with resampled training residuals."""
    e = np.asarray(residuals)
    n = len(e)
    if scheme == "iid":
        idx = rng.integers(0, n, size=(N, T))
    else:
        nb = int(math.ceil(T / block))
        starts = rng.integers(0, n - block + 1, size=(N, nb))
        idx = np.concatenate([starts[:, [j]] + np.arange(block)[None, :] for j in range(nb)], axis=1)[:, :T]
    E = e[idx]
    S = np.full(N, float(S0))
    alive = np.ones(N, dtype=bool)
    for t in range(T):
        S = S + surplus(S, r, K) - catch + E[:, t]
        S = np.clip(S, S_LO, 1e6)
        alive &= S >= K_star
    return float(alive.mean())


def run_cod():
    years, ssb, C = cod_data()
    K_star = float(np.mean(ssb[(years >= 1983) & (years <= 1989)]))
    fit = fit_cod(years, ssb, C)
    r, K = fit["r"], fit["K"]
    res = cod_residuals(years, ssb, C, r, K)
    tr_years = [y for y in sorted(res) if y <= TRAIN_END]
    oos_years = [y for y in sorted(res) if y > TRAIN_END]
    e_tr = np.array([res[y] for y in tr_years])
    e_oos = np.array([res[y] for y in oos_years])
    g_K = surplus(K_star, r, K)
    g_max = r * K / 4
    Fp = 1.0 + r * (1.0 - 2.0 * K_star / K)
    e_min, e_q05, e_q10 = float(e_tr.min()), float(np.percentile(e_tr, 5)), float(np.percentile(e_tr, 10))
    classes = {"UC_min": abs(e_min), "UC_q05": abs(e_q05), "UC_q10": abs(e_q10)}
    eps = float(np.abs(e_tr).max())
    out = {
        "data": {"years": [int(y) for y in years], "ssb_kt": [float(x) for x in ssb], "catch_kt": [float(x) for x in C],
                 "n_years": int(len(years)), "n_transitions": int(len(years) - 1)},
        "K_star": K_star,
        "fit": {"r": r, "K": K, "pinned": fit["pinned"], "n_train": fit["n"], "n_oos": int(len(e_oos)),
                "sse": fit["sse"], "mse": fit["sse"] / fit["n"],
                "train_sd": float(e_tr.std(ddof=1)), "train_mean": float(e_tr.mean()),
                "train_min": e_min, "train_max": float(e_tr.max()), "train_abs_max": eps,
                "train_abs_max_year": int(tr_years[int(np.argmax(np.abs(e_tr)))]),
                "train_q05": e_q05, "train_q10": e_q10,
                "train_lag1_acf": float(np.dot(e_tr[1:], e_tr[:-1]) / np.dot(e_tr[:-1], e_tr[:-1])),
                "oos_sd": float(e_oos.std(ddof=1)), "oos_abs_max": float(np.abs(e_oos).max()),
                "oos_abs_max_year": int(oos_years[int(np.argmax(np.abs(e_oos)))]),
                "residuals_train": {str(y): res[y] for y in tr_years},
                "residuals_oos": {str(y): res[y] for y in oos_years},
                "residual_1992": res[1992], "n_worse_than_172_5": int(np.sum(e_tr < -172.5)),
                "worse_than_172_5": sorted([float(x) for x in e_tr if x < -172.5])},
        "quantiles": {"q05": quantile_conventions(e_tr, 0.05), "q10": quantile_conventions(e_tr, 0.10),
                      "sorted_train": sorted(float(x) for x in e_tr)},
        "constants": {"g_Kstar": g_K, "g_max": g_max, "Fp_Kstar": Fp, "S_peak": K / 2,
                      "S_Fprime_zero": K * (1 + r) / (2 * r),
                      "C_star": {k: g_K - v for k, v in classes.items()},
                      "C_vac": {k: g_max - v for k, v in classes.items()},
                      "phi_star_safe": {k: 1 - v / g_K for k, v in classes.items()},
                      "phi_star_nonempty": {k: 1 - v / g_max for k, v in classes.items()},
                      "classes_abs": classes, "eps_declared": eps,
                      "r_T": {str(T): eps * (Fp ** T - 1) / (Fp - 1) for T in (1, 2, 3, 4, 5, 6, 7, 8, 10, 15, 20)}},
    }
    # Table 1 : nominal kernels, flat catches and reactive rules
    Ts = [1, 2, 3, 5, 8, 10, 15, 20, "inf"]
    pols = cod_policies(K_star)
    kern = {}
    for pid, pieces in pols.items():
        kern[pid] = {}
        for cid, e_abs in classes.items():
            kern[pid][cid] = policy_boundaries(pieces, e_abs, r, K, K_star, Ts)
    out["kernels"] = kern
    # closed-form b_inf for flat catches
    out["b_inf_flat"] = {str(c): {cid: (None if s_minus(c + e_abs, r, K) is None else max(K_star, s_minus(c + e_abs, r, K)))
                                  for cid, e_abs in classes.items()} for c in (0, 5, 60, 91.59, 120, 180, 240)}
    # proportional family regimes (q10 class)
    fam = {}
    for phi in (0.25, 0.5, 0.6, 0.7, 0.75):
        pieces = None  # proportional policies are not piecewise constant: worst map S + (1-phi) g(S) - |e|
        e_abs = classes["UC_q10"]
        lvl = e_abs / (1 - phi)
        sm = s_minus(lvl, r, K)
        regime = "whole safe set" if (1 - phi) * g_K >= e_abs else ("half-line" if sm is not None else "empty")
        fam[str(phi)] = {"C_at_LRP": phi * g_K, "b_inf": (None if sm is None else max(K_star, sm)), "regime": regime,
                         "margin": g_K - e_abs - phi * g_K}
    out["family_A_q10"] = fam
    # certified horizon by catch and class
    hz = {}
    for c in (0.0, 5.0, 30.0, 60.0, round(g_K - classes["UC_q10"], 2), 120.0, 150.0, 180.0, 200.0, round(g_max - classes["UC_q10"], 1)):
        hz[str(c)] = {}
        for cid, e_abs in classes.items():
            ln, fe = certified_horizon(c, e_abs, r, K, K_star, Fp, eps)
            hz[str(c)][cid] = {"last_nonempty": ln, "first_empty": fe}
    out["certified_horizon"] = hz
    # Lipschitz-certified boundaries per horizon (flat catches), for the figures
    lb = {}
    for c in (0.0, 60.0, 120.0, 180.0, 240.0):
        lb[str(c)] = {}
        for cid, e_abs in classes.items():
            inv = cod_inverse_factory(r, K, e_abs)
            bs = []
            for T in range(1, 21):
                rT = eps * (Fp ** T - 1) / (Fp - 1)
                Ws = kernel_recursion(flat_pieces(c), inv, (K_star + rT, S_HI), T)
                bs.append(lower_boundary(Ws[T]) if (len(Ws) == T + 1 and Ws[T]) else None)
                if bs[-1] is None:
                    break
            lb[str(c)][cid] = bs
    out["lipschitz_boundaries"] = lb
    # exact bounded-defect kernel (per-step recursion W_{t+1} = {S : [F(S)-eps, F(S)+eps] subset W_t})
    # versus the Lipschitz inflation certificate used above; also the policy-independent horizon bound

    def exact_bounded_defect(pieces, e_abs, epsv, Tcap=400):
        inv = cod_inverse_factory(r, K, e_abs)
        Ws = [[[K_star, S_HI]]]
        for _ in range(Tcap):
            tgt = Ws[-1]
            nxt = []
            for lo, hi, cc in pieces:
                for tlo, thi in tgt:
                    A = inv(cc, tlo + epsv)
                    Bv = inv(cc, thi - epsv) if thi < S_HI - 1e-9 else float("inf")
                    a2, b2 = max(A, lo, K_star), min(Bv, hi, S_HI)
                    if b2 - a2 >= -1e-9:
                        nxt.append([a2, b2])
            Ws.append(normalise(nxt))
            if not Ws[-1]:
                break
        last = len(Ws) - 2 if not Ws[-1] else None  # None: still non-empty at Tcap
        return Ws, last

    ex = {}
    for pid, pieces in pols.items():
        ex[pid] = {}
        for cid, e_abs in classes.items():
            Ws, last = exact_bounded_defect(pieces, e_abs, eps)
            ex[pid][cid] = {"boundaries_T1_20": [lower_boundary(w) for w in Ws[1:21]],
                            "last_nonempty": last if last is not None else ">=400",
                            "lipschitz_last_nonempty": certified_horizon(pieces[-1][2], e_abs, r, K, K_star, Fp, eps)[0] if len(pieces) == 1 else None}
    out["exact_bounded_defect"] = ex
    out["horizon_bounds_lipschitz"] = {
        "policy_independent_ceiling_bound": math.log(1 + (S_HI - K_star) * (Fp - 1) / eps) / math.log(Fp),
        "note": "T_cert <= log(1 + (S_hi - K*)(a-1)/eps)/log a for every policy: r_T exceeds the whole domain beyond this T"}
    # worst-case orbit from the ceiling, used by the asymptotic bound
    def orbit(c, e_abs, n=10):
        s, o = S_HI, []
        for _ in range(n):
            s = s + surplus(s, r, K) - c - e_abs
            o.append(s)
        return o
    out["orbit_from_ceiling_BAU"] = {cid: orbit(5.0, e_abs) for cid, e_abs in classes.items()}
    # finite-duration floors: n years at the floor, zero residual afterwards
    ff = {}
    for cid in ("UC_min", "UC_q05", "UC_q10"):
        e_abs = classes[cid]
        inv = cod_inverse_factory(r, K, e_abs)
        for pid, c in (("BAU", 5.0), ("flat_60", 60.0), ("S1", 60.0), ("cpm", 60.0), ("flat_120", 120.0)):
            sm0 = s_minus(c, r, K)
            b0 = max(K_star, sm0) if sm0 is not None else None
            if b0 is None:
                continue
            Ws = kernel_recursion(flat_pieces(c), inv, (b0, S_HI), 20)
            ff[f"{cid}|{pid}"] = {str(n): (lower_boundary(Ws[n]) if n < len(Ws) else None) for n in (5, 10, 15, 20)}
    out["finite_floors"] = ff
    # profile over K (closed-form r at each K) and the 95 % F-cut set
    S0, y = fit["S0"], fit["y"]
    from scipy.stats import f as fdist
    Kgrid = np.concatenate([np.arange(1000.0, 5000.0, 25.0), np.arange(5000.0, 50001.0, 250.0)])
    prof = []
    for Kv in Kgrid:
        rv, ss = sse_profile(S0, y, Kv)
        prof.append((float(Kv), rv, ss, surplus(K_star, rv, Kv), 1 + rv * (1 - 2 * K_star / Kv)))
    sse_min = min(p[2] for p in prof)
    fcut = 1.0 + 2.0 * fdist.ppf(0.95, 2, fit["n"] - 2) / (fit["n"] - 2)
    fcut1 = 1.0 + fdist.ppf(0.95, 1, fit["n"] - 2) / (fit["n"] - 2)
    inset = [p for p in prof if p[2] / sse_min <= fcut]
    inset1 = [p for p in prof if p[2] / sse_min <= fcut1]
    out["profile"] = {
        "F_cut_ratio": fcut, "F_cut_ratio_1par": fcut1, "sse_min": sse_min, "sse_box_edge_ratio": fit["sse"] / sse_min,
        "K_set": [inset[0][0], inset[-1][0]], "g_Kstar_range": [min(p[3] for p in inset), max(p[3] for p in inset)],
        "Fp_range": [min(p[4] for p in inset), max(p[4] for p in inset)],
        "C_star_range": [min(p[3] for p in inset) - classes["UC_q10"], max(p[3] for p in inset) - classes["UC_q10"]],
        "K_set_1par": [inset1[0][0], inset1[-1][0]], "g_Kstar_range_1par": [min(p[3] for p in inset1), max(p[3] for p in inset1)],
        "Fp_range_1par": [min(p[4] for p in inset1), max(p[4] for p in inset1)],
        "C_star_range_1par": [min(p[3] for p in inset1) - classes["UC_q10"], max(p[3] for p in inset1) - classes["UC_q10"]],
        "K_min_with_expansion": min((p[0] for p in prof if p[4] > 1), default=None),
        "zero_budget_point": {"K": 5000.0, "r_crit": classes["UC_q10"] / surplus(K_star, 1.0, 5000.0)},
        "grid": [[p[0], p[1], p[2], p[3], p[4]] for p in prof],
    }
    rc = out["profile"]["zero_budget_point"]["r_crit"]
    sse_zb = float(np.sum((y - rc * S0 * (1 - S0 / 5000.0)) ** 2))
    out["profile"]["zero_budget_point"]["sse_ratio"] = sse_zb / sse_min
    out["profile"]["zero_budget_point"]["sse_ratio_vs_committed"] = sse_zb / fit["sse"]
    out["profile"]["zero_budget_point"]["r_crit_C5"] = (classes["UC_q10"] + 5.0) / surplus(K_star, 1.0, 5000.0)
    # recent windows (closed-form r at K = 5000 for the NCAM windows)
    rw = {}
    for lab, y0, y1 in (("NCAM 1995-2015", 1995, 2015), ("NCAM 1995-2007", 1995, 2007)):
        fw = fit_cod(years, ssb, C, y0, y1)
        m = (years >= y0) & (years <= y1)
        Sw, Cw = ssb[m], C[m]
        ew = np.diff(Sw) - (surplus(Sw[:-1], fw["r"], fw["K"]) - Cw[:-1])
        rw[lab] = {"n": fw["n"], "r": fw["r"], "K": fw["K"], "pinned": fw["pinned"], "g_LRP": surplus(K_star, fw["r"], fw["K"]),
                   "g_max": fw["r"] * fw["K"] / 4, "Fp": 1 + fw["r"] * (1 - 2 * K_star / fw["K"]),
                   "e_q10": float(np.percentile(ew, 10)), "e_q05": float(np.percentile(ew, 5)), "e_min": float(ew.min()),
                   "sd": float(ew.std(ddof=1)), "mean": float(ew.mean())}
        rw[lab]["C_star"] = rw[lab]["g_LRP"] - abs(rw[lab]["e_q10"])
        rw[lab]["C_star_worst"] = rw[lab]["g_LRP"] - abs(rw[lab]["e_min"])
        # the same window with K held at the box edge (the registered campaign's optimiser stopped there)
        r5 = r_closed_form(Sw[:-1], np.diff(Sw) + Cw[:-1], 5000.0)
        e5 = np.diff(Sw) - (surplus(Sw[:-1], r5, 5000.0) - Cw[:-1])
        rw[lab]["at_K_5000"] = {"r": r5, "sse": float(np.sum(e5 ** 2)), "sse_exact": fw["sse"],
                                "g_LRP": surplus(K_star, r5, 5000.0), "e_q10": float(np.percentile(e5, 10)),
                                "C_star": surplus(K_star, r5, 5000.0) - abs(float(np.percentile(e5, 10))),
                                "Fp": 1 + r5 * (1 - 2 * K_star / 5000.0)}
    out["recent_windows"] = rw
    # independent stochastic layer (different seed from the registered campaign)
    rng = np.random.default_rng(20261015)
    st = {}
    for scheme in ("iid", "block4"):
        for c in (5.0, 60.0, 120.0):
            st[f"{scheme}|C={c:g}|S0=LRP|T=20"] = stochastic_survival(r, K, e_tr, c, K_star, 20, 20000, rng, scheme, 4, K_star)
        st[f"{scheme}|C=5|S0=1500|T=20"] = stochastic_survival(r, K, e_tr, 5.0, 1500.0, 20, 20000, rng, scheme, 4, K_star)
    out["stochastic_independent"] = st
    out["stochastic_independent"]["ceiling_iid_zero_catch_T20_pstay_theory_note"] = \
        "(23/24)^20 = %.4f is the probability that the 1992 residual is never drawn in 20 i.i.d. years" % ((23 / 24) ** 20)
    # independent fixed-K residual bootstrap of C*
    Bn = 2000
    boot = []
    S_1983 = ssb[0]
    Cw = C[(years >= 1983) & (years <= TRAIN_END)]
    for b in range(Bn):
        eb = rng.choice(e_tr, size=fit["n"], replace=True)
        S = [S_1983]
        for t in range(fit["n"]):
            S.append(max(S_LO, S[-1] + surplus(S[-1], r, K) - Cw[t] + eb[t]))
        S = np.array(S)
        yb = np.diff(S) + Cw[:-1] if False else np.diff(S) + Cw[:fit["n"]]
        rb = r_closed_form(S[:-1], yb, K)
        eb2 = yb - rb * S[:-1] * (1 - S[:-1] / K)
        boot.append((rb, surplus(K_star, rb, K) - classes["UC_q10"], surplus(K_star, rb, K) - abs(np.percentile(eb2, 10))))
    boot = np.array(boot)
    out["bootstrap_independent_fixedK"] = {
        "B": Bn, "seed": 20261015, "design": "trajectory bootstrap from S_1983 with the registered map and observed catches; r refit at K = 5000",
        "r_median": float(np.median(boot[:, 0])), "r_q05_q95": [float(np.percentile(boot[:, 0], 5)), float(np.percentile(boot[:, 0], 95))],
        "frozen_floor": {"Cstar_median": float(np.median(boot[:, 1])), "Cstar_q05_q95": [float(np.percentile(boot[:, 1], 5)), float(np.percentile(boot[:, 1], 95))],
                         "share_nonpositive": float(np.mean(boot[:, 1] <= 0))},
        "reestimated_floor": {"Cstar_median": float(np.median(boot[:, 2])), "Cstar_q05_q95": [float(np.percentile(boot[:, 2], 5)), float(np.percentile(boot[:, 2], 95))],
                              "share_nonpositive": float(np.mean(boot[:, 2] <= 0))}}
    return out


# =============================================================================
#  PART II  --  Edwards Aquifer J-17
# =============================================================================
H_LO, H_HI = 0.0, 710.0
K_PHYS, K_INST = 618.0, 660.0
TRAIN_END_E = 1990


def edwards_data():
    rows = read_csv(EDW / "data" / "annual_panel.csv")
    yrs, H, R, P = [], [], [], []
    for rw in rows:
        y = int(rw["year"])
        if 1934 <= y <= 2023:
            yrs.append(y)
            H.append(float(rw["H_mean"]))
            R.append(float(rw["R_total"]))
            P.append(float(rw["P_wells"]))
    return np.array(yrs), np.array(H), np.array(R), np.array(P)


def fit_edwards(yrs, H, R, P):
    dH = H[1:] - H[:-1]
    X = np.column_stack([np.ones(len(dH)), R[1:], P[1:], H[:-1]])
    m_tr = yrs[1:] <= TRAIN_END_E
    coef, *_ = np.linalg.lstsq(X[m_tr], dH[m_tr], rcond=None)
    res_all = dH - X @ coef
    return coef, res_all, m_tr


def edw_policies(Pbar):
    P = {}
    P["BAU"] = [(H_LO, H_HI, Pbar)]
    for rho in (0.9, 0.8, 0.7, 0.6, 0.5, 0.0):
        P[f"flat_{int(round(rho*100))}"] = [(H_LO, H_HI, rho * Pbar)]
    P["S1"] = [(H_LO, 660.0, 0.8 * Pbar), (660.0, H_HI, Pbar)]
    P["cpm"] = [(H_LO, 630.0, 0.6 * Pbar), (630.0, 640.0, 0.65 * Pbar), (640.0, 650.0, 0.7 * Pbar),
                (650.0, 660.0, 0.8 * Pbar), (660.0, H_HI, Pbar)]
    return P


def run_edwards():
    yrs, H, R, P = edwards_data()
    coef, res_all, m_tr = fit_edwards(yrs, H, R, P)
    alpha, beta, gamma, delta = [float(c) for c in coef]
    a = 1.0 + delta
    e_tr, e_oos = res_all[m_tr], res_all[~m_tr]
    dest = yrs[1:]
    eps = float(np.abs(e_tr).max())
    eps_oos = float(np.abs(e_oos).max())
    Rtr = R[(yrs >= 1934) & (yrs <= TRAIN_END_E)]
    Ptr = P[(yrs >= 1934) & (yrs <= TRAIN_END_E)]
    Pbar = float(np.mean(Ptr))
    # recharge floors from the training window (declared classes)
    F_min, F_q05, F_q10 = float(Rtr.min()), float(np.percentile(Rtr, 5)), float(np.percentile(Rtr, 10))
    floors = {"UC_min": F_min, "UC_q05": F_q05, "UC_q10": F_q10}

    def attractor(Pv, Fv):
        return (alpha + beta * Fv + gamma * Pv) / (1 - a)

    def inverse_factory(Fv, shrink=0.0):
        # F_P(H) = a H + alpha + beta F + gamma P ; inverse of the increasing affine map
        def inverse(Pv, y):
            return (y - alpha - beta * Fv - gamma * Pv) / a
        return inverse

    pols = edw_policies(Pbar)
    out = {"fit": {"alpha": alpha, "beta": beta, "gamma": gamma, "delta": delta, "a": a, "n_train": int(m_tr.sum()),
                   "n_oos": int((~m_tr).sum()), "train_sd": float(e_tr.std(ddof=1)), "train_abs_max": eps,
                   "train_abs_max_year": int(dest[m_tr][int(np.argmax(np.abs(e_tr)))]),
                   "oos_sd": float(e_oos.std(ddof=1)), "oos_abs_max": eps_oos,
                   "oos_abs_max_year": int(dest[~m_tr][int(np.argmax(np.abs(e_oos)))]),
                   "train_ar1": float(np.dot(e_tr[1:], e_tr[:-1]) / np.dot(e_tr[:-1], e_tr[:-1])),
                   "residuals_train": {str(int(y)): float(v) for y, v in zip(dest[m_tr], e_tr)},
                   "residuals_oos": {str(int(y)): float(v) for y, v in zip(dest[~m_tr], e_oos)}},
           "P_bar": Pbar, "floors": floors, "floor_years": {"UC_min": int(yrs[(yrs <= TRAIN_END_E)][int(np.argmin(Rtr))])},
           "r_T": {str(T): eps * (1 - a ** T) / (1 - a) for T in (1, 2, 3, 4, 5, 8, 10, 15, 20)},
           "r_inf": eps / (1 - a),
           "r_T_oos": {str(T): eps_oos * (1 - a ** T) / (1 - a) for T in (1, 2, 3, 4, 5, 10)},
           "r_inf_oos": eps_oos / (1 - a),
           "data": {"years": [int(y) for y in yrs], "H": [float(x) for x in H], "R": [float(x) for x in R], "P": [float(x) for x in P]}}
    # attractors and margins
    att = {}

    def self_consistent(pieces, Fv):
        # the fixed point of the closed loop: the piece whose own attractor lies inside it
        hits = []
        for lo, hi, Pv in pieces:
            Hs = attractor(Pv, Fv)
            if lo <= Hs < hi or (Hs >= hi and hi == H_HI) or (Hs < lo and lo == H_LO):
                hits.append(Hs)
        return hits[0] if hits else None

    for pid, pieces in pols.items():
        att[pid] = {cid: {"low_piece": attractor(pieces[0][2], Fv), "top_piece": attractor(pieces[-1][2], Fv),
                          "self_consistent": self_consistent(pieces, Fv)}
                    for cid, Fv in floors.items()}
    out["attractors"] = att
    out["zero_pumping_attractor"] = {cid: attractor(0.0, Fv) for cid, Fv in floors.items()}
    out["margin_660"] = {cid: attractor(0.0, Fv) - K_INST for cid, Fv in floors.items()}
    out["minimal_flat_cut_618_UCmin"] = {}
    rho_star = (K_PHYS * (1 - a) - alpha - beta * F_min) / (gamma * Pbar)
    out["minimal_flat_cut_618_UCmin"] = {"rho_star": rho_star, "cut_percent": 100 * (1 - rho_star),
                                         "S1_attractor_at_cut": attractor(0.8 * Pbar * 1.0, F_min),
                                         "cut_of_current_mean": None}
    # nominal kernels (threshold 618 and 660) at horizons, by exact recursion, and closed forms
    Ts = [1, 2, 3, 4, 5, 8, 10, 12, 13, 15, 20]
    kern = {}
    for thr_name, thr in (("K_phys_618", K_PHYS), ("K_inst_660", K_INST)):
        kern[thr_name] = {}
        for pid, pieces in pols.items():
            kern[thr_name][pid] = {}
            for cid, Fv in floors.items():
                inv = inverse_factory(Fv)
                Ws = kernel_recursion(pieces, inv, (thr, H_HI), max(Ts))
                d = {str(T): (lower_boundary(Ws[T]) if T < len(Ws) else None) for T in Ts}
                d["first_empty"] = (len(Ws) - 1) if len(Ws) <= max(Ts) else None
                # closed-form (flat policies): B(T) = H* + (thr - H*)/a^T ; T_empty = ln((710-H*)/(thr-H*))/ln(1/a)
                Hs = attractor(pieces[0][2], Fv)
                if thr > Hs:
                    d["T_empty_closed_form"] = math.log((H_HI - Hs) / (thr - Hs)) / math.log(1 / a)
                else:
                    d["T_empty_closed_form"] = None
                kern[thr_name][pid][cid] = d
    out["kernels_nominal"] = kern
    # certified kernels: threshold thr + r_T at horizon T (contracting form)
    cert = {}
    for thr_name, thr in (("K_phys_618", K_PHYS), ("K_inst_660", K_INST)):
        cert[thr_name] = {}
        for pid, pieces in pols.items():
            cert[thr_name][pid] = {}
            for cid, Fv in floors.items():
                inv = inverse_factory(Fv)
                d = {}
                last_ne = 0
                for T in range(1, 13):
                    rT = eps * (1 - a ** T) / (1 - a)
                    Ws = kernel_recursion(pieces, inv, (thr + rT, H_HI), T)
                    ok = len(Ws) == T + 1 and bool(Ws[T])
                    d[str(T)] = lower_boundary(Ws[T]) if ok else None
                    if ok:
                        last_ne = T
                d["last_nonempty"] = last_ne
                cert[thr_name][pid][cid] = d
    out["kernels_certified"] = cert
    # bounded-error recursion: W_{t+1} = {H : F(H) - eps >= low(W_t) and F(H) + eps <= 710 ... }
    # i.e. the one-step image interval [F(H)-eps, F(H)+eps] must lie inside W_t.

    def bounded_error_kernels(pieces, Fv, epsv, thr, T):
        Ws = [[[thr, H_HI]]]
        for _ in range(T):
            tgt = Ws[-1]
            nxt = []
            for lo, hi, Pv in pieces:
                for tlo, thi in tgt:
                    # need F(H) - eps >= tlo and min(F(H) + eps, H_HI) <= thi  (the ceiling clamps, it does not fail)
                    A = (tlo + epsv - alpha - beta * Fv - gamma * Pv) / a
                    B = (thi - epsv - alpha - beta * Fv - gamma * Pv) / a if thi < H_HI - 1e-9 else float("inf")
                    a2, b2 = max(A, lo, thr), min(B, hi, H_HI)
                    if b2 - a2 >= -1e-9:
                        nxt.append([a2, b2])
            Ws.append(normalise(nxt))
            if not Ws[-1]:
                break
        return Ws

    be = {}
    for pid in ("BAU", "flat_90", "flat_80", "S1", "cpm", "flat_0"):
        be[pid] = {}
        for cid in ("UC_min", "UC_q05", "UC_q10"):
            Fv = floors[cid]
            for lab, epsv in (("train", eps), ("oos", eps_oos)):
                Ws = bounded_error_kernels(pols[pid], Fv, epsv, K_PHYS, 8)
                be[pid][f"{cid}|{lab}"] = {"boundaries": [lower_boundary(w) for w in Ws[1:]],
                                            "first_empty": ((len(Ws) - 1) if len(Ws) <= 8 else None)}
        if True:
            # supremum uniform defect at which the T-step bounded-error kernel is still non-empty (bisection)
            sup = {}
            for T in (2, 3, 4, 5):
                lo_e, hi_e = 0.0, 60.0
                for _ in range(60):
                    mid = 0.5 * (lo_e + hi_e)
                    Ws = bounded_error_kernels(pols[pid], floors["UC_min"], mid, K_PHYS, T)
                    if len(Ws) == T + 1 and Ws[T]:
                        lo_e = mid
                    else:
                        hi_e = mid
                sup[str(T)] = lo_e
            be[pid]["sup_eps_UC_min"] = sup
    out["bounded_error"] = be
    # identity (affine contraction): exact bounded-error boundary == Lipschitz-inflated certificate boundary
    ident = []
    for pid in ("BAU", "flat_90", "flat_80", "S1", "cpm", "flat_0"):
        for T in (1, 2, 3):
            b_exact = be[pid]["UC_min|train"]["boundaries"][T - 1] if T - 1 < len(be[pid]["UC_min|train"]["boundaries"]) else None
            b_infl = cert["K_phys_618"][pid]["UC_min"].get(str(T))
            ident.append({"policy": pid, "T": T, "exact": b_exact, "inflated": b_infl,
                          "equal": (b_exact is None and b_infl is None) or (b_exact is not None and b_infl is not None and abs(b_exact - b_infl) < 1e-6)})
    out["lipschitz_vs_exact_identity"] = {"rows": ident, "all_equal": all(x["equal"] for x in ident)}
    # replays: open loop on observed heads (supply) and closed loop with observed recharge
    tr_mask = (yrs >= 1934) & (yrs <= TRAIN_END_E)
    oos_mask = yrs > TRAIN_END_E

    def policy_fn(pieces):
        def fn(h):
            for lo, hi, Pv in pieces:
                if lo <= h < hi or (h >= hi and hi == H_HI):
                    return Pv
            return pieces[-1][2]
        return fn

    sup_tab = {}
    occ = {}
    for pid, pieces in pols.items():
        fn = policy_fn(pieces)
        Ptr_pol = np.array([fn(h) for h in H[tr_mask]])
        Poos_pol = np.array([fn(h) for h in H[oos_mask]])
        sup_tab[pid] = {"train_mean_P": float(Ptr_pol.mean()), "oos_mean_P": float(Poos_pol.mean()),
                        "train_cut_active": float(np.mean(Ptr_pol < Pbar - 1e-9)),
                        "oos_cut_active": float(np.mean(Poos_pol < Pbar - 1e-9))}
    out["supply_open_loop"] = sup_tab
    Htr = H[tr_mask]
    Hoos = H[oos_mask]
    occ["train"] = {"n": int(len(Htr)), "below_660": float(np.mean(Htr < 660)), "below_650": float(np.mean(Htr < 650)),
                    "below_640": float(np.mean(Htr < 640)), "below_630": float(np.mean(Htr < 630)),
                    "counts": [int(np.sum(Htr < t)) for t in (660, 650, 640, 630)]}
    occ["oos"] = {"n": int(len(Hoos)), "below_660": float(np.mean(Hoos < 660)), "below_650": float(np.mean(Hoos < 650)),
                  "below_640": float(np.mean(Hoos < 640)), "below_630": float(np.mean(Hoos < 630)),
                  "counts": [int(np.sum(Hoos < t)) for t in (660, 650, 640, 630)]}
    out["occupancy"] = occ

    def closed_loop(pieces, y_start, y_end, h0=None):
        fn = policy_fn(pieces)
        i0 = int(np.where(yrs == y_start)[0][0])
        h = H[i0] if h0 is None else h0
        path = [(int(yrs[i0]), float(h))]
        Ps = []
        for i in range(i0 + 1, int(np.where(yrs == y_end)[0][0]) + 1):
            Pv = fn(h)
            Ps.append(Pv)
            h = h + alpha + beta * R[i] + gamma * Pv + delta * h
            h = min(max(h, H_LO), H_HI)
            path.append((int(yrs[i]), float(h)))
        hs = [p[1] for p in path]
        return {"mean_P": float(np.mean(Ps)), "cut_active": float(np.mean(np.array(Ps) < Pbar - 1e-9)),
                "end_head": hs[-1], "min_head": float(min(hs)), "max_head": float(max(hs)), "start_head": hs[0],
                "path": path}

    cl = {}
    for pid in ("BAU", "flat_90", "flat_80", "flat_60", "S1", "cpm", "flat_0"):
        # out-of-sample replay starts from the last training head (1990) and steps through the 33 OOS transitions
        cl[pid] = {"train_1934_1990": closed_loop(pols[pid], 1934, 1990), "oos_1991_2023": closed_loop(pols[pid], 1990, 2023)}
    out["closed_loop"] = cl
    # 1950s stress replay (model from observed 1950 head with actual recharge, policy pumping)
    rep = {}
    for pid in pols:
        rep[pid] = closed_loop(pols[pid], 1950, 1956)
    out["replay_1950s"] = rep
    # fit diagnostic 1950s with actual pumping
    i0 = int(np.where(yrs == 1950)[0][0])
    h = H[i0]
    diag = [(1950, float(H[i0]), float(h))]
    for i in range(i0 + 1, i0 + 7):
        h = h + alpha + beta * R[i] + gamma * P[i] + delta * h
        diag.append((int(yrs[i]), float(H[i]), float(h)))
    out["fit_diagnostic_1950s"] = {"rows": diag, "max_abs_error": float(max(abs(d[1] - d[2]) for d in diag)),
                                   "model_1956": diag[-1][2], "observed_1956": diag[-1][1]}
    # finite-duration floors: n years at the floor then mean recharge
    ffl = {}
    Rbar = float(Rtr.mean())
    for pid in ("BAU", "flat_90", "S1", "cpm"):
        pieces = pols[pid]
        for cid in ("UC_min", "UC_q05"):
            Fv = floors[cid]
            # terminal set: T = inf kernel under mean recharge (whole safe set if attractor >= 618)
            inv_bar = inverse_factory(Rbar)
            Wbar = kernel_recursion(pieces, inv_bar, (K_PHYS, H_HI), 400)
            W_term = Wbar[-1] if len(Wbar) == 401 else []
            if not W_term:
                ffl[f"{pid}|{cid}"] = None
                continue
            inv = inverse_factory(Fv)
            d = {}
            for n in (5, 10, 15):
                Ws = [W_term]
                for _ in range(n):
                    tgt = Ws[-1]
                    nxt = []
                    for lo, hi, Pv in pieces:
                        for tlo, thi in tgt:
                            A, B = inv(Pv, tlo), inv(Pv, thi)
                            a2, b2 = max(A, lo, K_PHYS), min(B, hi, H_HI)
                            if b2 - a2 >= -1e-9:
                                nxt.append([a2, b2])
                    Ws.append(normalise(nxt))
                    if not Ws[-1]:
                        break
                d[str(n)] = lower_boundary(Ws[n]) if len(Ws) == n + 1 else None
            ffl[f"{pid}|{cid}"] = d
    out["finite_floors"] = ffl
    out["R_bar_train"] = Rbar
    # floor-class supply: closed loop from 1934 head with recharge pinned at the floor, 57 years
    fcs = {}
    for pid in ("S1", "cpm", "flat_80", "flat_60", "BAU"):
        fn = policy_fn(pols[pid])
        h = H[tr_mask][0]
        Ps = []
        for _ in range(57):
            Pv = fn(h)
            Ps.append(Pv)
            h = min(max(h + alpha + beta * F_min + gamma * Pv + delta * h, H_LO), H_HI)
        fcs[pid] = {"mean_P": float(np.mean(Ps)), "end_head": float(h)}
    out["floor_class_supply"] = fcs
    # independent residual bootstrap of the attractors (different seed)
    rng = np.random.default_rng(20261015)
    X = np.column_stack([np.ones(int(m_tr.sum())), R[1:][m_tr], P[1:][m_tr], H[:-1][m_tr]])
    fitted = X @ coef
    boots = {pid: [] for pid in ("BAU", "flat_90", "flat_80", "flat_60", "flat_0")}
    nonc = 0
    gamma_nonneg = 0
    beta_nonpos = 0
    coef_rel = {"beta_over_1ma": [], "gamma_over_1ma": []}
    for b in range(5000):
        yb = fitted + rng.choice(e_tr, size=len(e_tr), replace=True)
        cb, *_ = np.linalg.lstsq(X, yb, rcond=None)
        ab = 1 + cb[3]
        if not (0 < ab < 1):
            nonc += 1
            continue
        gamma_nonneg += int(cb[2] >= 0)
        beta_nonpos += int(cb[1] <= 0)
        coef_rel["beta_over_1ma"].append(cb[1] / (1 - ab))
        coef_rel["gamma_over_1ma"].append(cb[2] / (1 - ab))
        for pid in boots:
            Pv = pols[pid][0][2]
            boots[pid].append((cb[0] + cb[1] * F_min + cb[2] * Pv) / (1 - ab))
    gap = np.array(boots["flat_90"]) - np.array(boots["BAU"])
    out["bootstrap_independent"] = {"noncontractive": nonc,
                                    "gamma_nonneg_reps": gamma_nonneg, "beta_nonpos_reps": beta_nonpos,
                                    "gap_flat90_minus_BAU_min": float(gap.min()),
                                    "gap_positive_share": float(np.mean(gap > 0)),
                                    "coef_ratio_sd_over_point": {k: float(np.std(v) / abs(np.mean(v))) for k, v in coef_rel.items()},
                                    "attractor_sd": {pid: float(np.std(v)) for pid, v in boots.items()},
                                    "P_attractor_ge_618": {pid: float(np.mean(np.array(v) >= 618)) for pid, v in boots.items()},
                                    "gap_flat90_minus_BAU_q05_q50_q95": [float(np.percentile(np.array(boots["flat_90"]) - np.array(boots["BAU"]), q)) for q in (5, 50, 95)]}
    return out


# =============================================================================
#  archive readers and checks
# =============================================================================


def read_archive():
    A = {}
    A["cod_results"] = json.load(open(COD / "results" / "intervention_results_v3.json"))
    A["edw_results"] = json.load(open(EDW / "results" / "intervention_results_v2.json"))
    A["edw_audit"] = json.load(open(EDW / "results" / "e4_audit_layer.json"))
    A["stoch"] = read_csv(COD / "src" / "results_srcyear_v3" / "e2_elevation_stochastic.csv")
    A["stoch_constructive"] = read_csv(COD / "src" / "results_srcyear_v3" / "e2_elevation_stochastic_constructive.csv")
    A["boot_fixedK"] = read_csv(COD / "src" / "results_srcyear_v3" / "e2_elevation_bootstrap.csv")
    A["boot_joint"] = read_csv(COD / "src" / "results_ident_v3" / "e2_bootstrap_joint.csv")
    A["finite_floors"] = read_csv(COD / "src" / "results_srcyear_v3" / "e2_elevation_finite_floors.csv")
    A["ident"] = read_csv(COD / "src" / "results_ident_v3" / "e2_identification_v3.csv")
    A["recent"] = read_csv(COD / "src" / "results_ident_v3" / "e2_recent_windows.csv")
    A["cadence"] = read_csv(COD / "src" / "results_cadence_v3" / "e2_cadence_v3.csv")
    A["structure"] = read_csv(COD / "src" / "results_struct_v3" / "e2_structure_v3.csv")
    A["fox"] = read_csv(COD / "src" / "results_forms_v3" / "e2_fox_form_v3.csv")
    A["fox_kernels"] = read_csv(COD / "src" / "results_forms_v3" / "e2_fox_kernels_v3.csv")
    A["allee"] = read_csv(COD / "src" / "results_forms_v3" / "e2_allee_rows_v3.csv")
    A["families"] = read_csv(COD / "results" / "e2_families_v3.csv")
    A["k_grid"] = read_csv(COD / "src" / "results_srcyear_v3" / "e2_elevation_k_grid.csv")
    return A


def summarise_archive(A):
    S = {}
    # stochastic layer
    st = {}
    for rw in A["stoch"]:
        st[f'{rw["scheme"]}|{rw["policy"]}|S0={float(rw["S0"]):g}|T={rw["T"]}'] = float(rw["P_stay"])
    S["stochastic"] = st
    sc = {}
    for rw in A["stoch_constructive"]:
        sc.setdefault(rw["scheme"], []).append((float(rw["C"]), float(rw["P_stay"])))
    S["stochastic_constructive"] = sc
    # crossings of P >= 0.9 and 0.8 by scheme (linear interpolation on the catch grid)
    cross = {}
    for scheme, pts in sc.items():
        pts = sorted(pts)
        d = {}
        for lvl in (0.9, 0.8):
            xc = None
            for (c0, p0), (c1, p1) in zip(pts[:-1], pts[1:]):
                if p0 >= lvl > p1:
                    xc = c0 + (p0 - lvl) / (p0 - p1) * (c1 - c0)
                    break
            d[str(lvl)] = xc
        d["ceiling"] = pts[0][1]
        d["P_at_91.59"] = None
        for c, p in pts:
            if abs(c - 92.5) < 1e-9:
                d["P_at_92.5"] = p
        cross[scheme] = d
    S["stochastic_crossings"] = cross
    # bootstrap fixed-K
    b = np.array([[float(r["r"]), float(r["g_Kstar"]) - 80.86978040666266, float(r["Fp"])] for r in A["boot_fixedK"]])
    S["bootstrap_fixedK"] = {"B": int(len(b)), "r_median": float(np.median(b[:, 0])),
                             "r_q05_q95": [float(np.percentile(b[:, 0], 5)), float(np.percentile(b[:, 0], 95))],
                             "Cstar_median": float(np.median(b[:, 1])),
                             "Cstar_q05_q95": [float(np.percentile(b[:, 1], 5)), float(np.percentile(b[:, 1], 95))],
                             "n_nonpositive": int(np.sum(b[:, 1] <= 0)), "share_positive": float(np.mean(b[:, 1] > 0)),
                             "Fp_median": float(np.median(b[:, 2])), "Fp_q05_q95": [float(np.percentile(b[:, 2], 5)), float(np.percentile(b[:, 2], 95))]}
    # bootstrap joint
    j = np.array([[float(r["r"]), float(r["K"]), float(r["Cstar"]), float(r["Fp"]), float(r["g_Kstar"])] for r in A["boot_joint"]])
    Ks = j[:, 1]
    m2 = Ks >= 2 * 884.6
    S["bootstrap_joint"] = {"B": int(len(j)), "r_median": float(np.median(j[:, 0])),
                            "r_q05_q95": [float(np.percentile(j[:, 0], 5)), float(np.percentile(j[:, 0], 95))],
                            "K_median": float(np.median(Ks)), "share_pinned": float(np.mean(Ks >= 4999.0)),
                            "Cstar_median": float(np.median(j[:, 2])),
                            "Cstar_q05_q95": [float(np.percentile(j[:, 2], 5)), float(np.percentile(j[:, 2], 95))],
                            "n_nonpositive": int(np.sum(j[:, 2] <= 0)), "share_Fp_gt_1": float(np.mean(j[:, 3] > 1)),
                            "share_K_ge_2Kstar": float(np.mean(m2)), "n_K_ge_2Kstar": int(m2.sum()),
                            "n_nonpositive_given_2Kstar": int(np.sum(j[m2, 2] <= 0)),
                            "Cstar_median_given_2Kstar": float(np.median(j[m2, 2])),
                            "Cstar_q05_q95_given_2Kstar": [float(np.percentile(j[m2, 2], 5)), float(np.percentile(j[m2, 2], 95))],
                            "Fp_median_given_2Kstar": float(np.median(j[m2, 3]))}
    # finite floors (archived)
    S["finite_floors"] = {f'{r["floor"]}|{r["policy"]}|n={r["n_years"]}': (None if r["Tinf_lower_boundary"] in ("", "None") else float(r["Tinf_lower_boundary"])) for r in A["finite_floors"]}
    # ident rows
    S["ident"] = {f'{r["section"]}|{r["quantity"]}': r["value"] for r in A["ident"]}
    S["recent"] = {r["label"]: {k: (float(v) if k not in ("label", "K_pin") else v) for k, v in r.items()} for r in A["recent"]}
    S["cadence"] = {f'{r["section"]}|{r["quantity"]}': r["value"] for r in A["cadence"]}
    S["structure"] = {r["quantity"]: r["value"] for r in A["structure"]}
    S["fox"] = A["fox"]
    S["fox_kernels"] = A["fox_kernels"]
    S["allee"] = {r["cell"]: r["computed"] for r in A["allee"]}
    S["families"] = {f'{r["policy"]}|{r["class"]}|T={r["T"]}': (None if r["boundary"] in ("", "None") else float(r["boundary"])) for r in A["families"]}
    S["k_grid"] = A["k_grid"]
    S["edw_audit_bootstrap"] = A["edw_audit"]["attractor_bootstrap"]
    S["edw_audit_closed_loop"] = A["edw_audit"]["closed_loop_replay"]
    S["edw_audit_sensitivities"] = A["edw_audit"]["sensitivities"]
    S["edw_results_summary"] = {k: A["edw_results"][k] for k in ("fit", "declared", "erosion", "steady_states_worst_case",
                                                                "minimal_flat_cut_K_phys_UC_min", "supply", "stress_replay_1950s",
                                                                "fit_diagnostic_1950s", "certified_horizon_nonempty")}
    S["cod_results_summary"] = {k: A["cod_results"][k] for k in ("fit", "UC", "erosion", "maximal_robust_flat_catch", "supply",
                                                                "certified_horizon_nonempty")}
    S["cod_kernels_archived"] = A["cod_results"]["kernels"]
    S["edw_kernels_archived"] = A["edw_results"]["kernels"]
    return S


def compare_with_archive(cod, edw, A):
    checks = []

    def chk(name, mine, theirs, tol):
        ok = (mine is None and theirs is None) or (mine is not None and theirs is not None and abs(mine - theirs) <= tol)
        checks.append({"check": name, "mine": mine, "archive": theirs, "tol": tol, "ok": bool(ok)})

    cr = A["cod_results"]
    chk("cod r", cod["fit"]["r"], cr["fit"]["r"], 2e-6)
    chk("cod K", cod["fit"]["K"], cr["fit"]["K"], 1e-6)
    chk("cod train sd", cod["fit"]["train_sd"], cr["fit"]["train_residual_sd"], 1e-3)
    chk("cod e_min", cod["fit"]["train_min"], cr["fit"]["train_residual_min"], 1e-3)
    chk("cod e_q05", cod["fit"]["train_q05"], cr["fit"]["train_residual_q05"], 1e-3)
    chk("cod e_q10", cod["fit"]["train_q10"], cr["fit"]["train_residual_q10"], 1e-3)
    chk("cod oos max", cod["fit"]["oos_abs_max"], cr["fit"]["oos_residual_max"], 1e-3)
    chk("cod a_max", cod["constants"]["Fp_Kstar"], cr["erosion"]["a_max"], 1e-4)
    chk("cod C* q10", cod["constants"]["C_star"]["UC_q10"], cr["maximal_robust_flat_catch"]["UC_q10"]["max_flat_catch_kt"], 0.01)
    for pid in cr["kernels"]:
        for cid in cr["kernels"][pid]:
            for T in ("1", "3", "5", "10", "20", "inf"):
                th = cr["kernels"][pid][cid][T]["nominal"]
                theirs = None if th is None else th[0][0]
                mine = cod["kernels"][pid][cid][T]
                if isinstance(mine, tuple) or isinstance(mine, list):
                    mine = mine[1]
                chk(f"cod kernel {pid}|{cid}|T={T}", mine, theirs, 0.05 if T != "20" else 0.2)
    for key, val in A["finite_floors_summary"].items():
        cid, pid, n = key.split("|")
        pid2 = {"flat_60": "flat_60", "BAU": "BAU", "S1": "S1", "cpm": "cpm", "flat_120": "flat_120", "flat_25": "flat_60", "flat_50": "flat_120"}.get(pid)
        cidn = {"q05": "UC_q05", "q10": "UC_q10", "worst": "UC_min", "min": "UC_min"}.get(cid)
        if cidn is None:
            continue
        k2 = f"{cidn}|{pid2}"
        if k2 in cod["finite_floors"] and cod["finite_floors"][k2] is not None:
            chk(f"cod finite floor {key}", cod["finite_floors"][k2].get(n.split('=')[1]), val, 0.1)
    for lab in ("NCAM 1995-2015", "NCAM 1995-2007"):
        rr = [r for r in A["recent"] if r["label"] == lab][0]
        chk(f"recent {lab} r at K=5000", cod["recent_windows"][lab]["at_K_5000"]["r"], float(rr["r"]), 2e-3)
        chk(f"recent {lab} C* at K=5000", cod["recent_windows"][lab]["at_K_5000"]["C_star"], float(rr["Cstar"]), 1.0)
    er = A["edw_results"]
    for k in ("alpha", "beta", "gamma", "delta", "a"):
        chk(f"edw {k}", edw["fit"][k], er["fit"][k], 1e-6)
    chk("edw train max", edw["fit"]["train_abs_max"], er["fit"]["train_residual_max"], 1e-6)
    chk("edw oos max", edw["fit"]["oos_abs_max"], er["fit"]["oos_residual_max"], 1e-6)
    chk("edw P_bar", edw["P_bar"], er["declared"]["P_bar_train"], 0.01)
    for cid in ("UC_min", "UC_q05", "UC_q10"):
        chk(f"edw floor {cid}", edw["floors"][cid], er["declared"]["uncertainty_classes"][cid], 0.05)
    for pid in er["steady_states_worst_case"]:
        for cid in ("UC_min", "UC_q05", "UC_q10"):
            chk(f"edw attractor {pid}|{cid}", edw["attractors"][pid][cid]["self_consistent"], er["steady_states_worst_case"][pid][cid], 0.01)
    chk("edw rho*", edw["minimal_flat_cut_618_UCmin"]["rho_star"], er["minimal_flat_cut_K_phys_UC_min"]["rho_star"], 1e-3)
    for pid in er["kernels"]:
        for cid in ("UC_min", "UC_q05", "UC_q10"):
            for thr in ("K_phys_618", "K_inst_660"):
                for T in ("1", "2", "3", "5", "8", "10"):
                    th = er["kernels"][pid][cid][thr][T]["nominal"]
                    theirs = None if th is None else th[0][0]
                    chk(f"edw kernel {pid}|{cid}|{thr}|T={T}", edw["kernels_nominal"][thr][pid][cid][T], theirs, 0.01)
                    tc = er["kernels"][pid][cid][thr][T]["certified"]
                    theirs_c = None if tc is None else tc[0][0]
                    mine_c = edw["kernels_certified"][thr][pid][cid].get(T)
                    chk(f"edw certified {pid}|{cid}|{thr}|T={T}", mine_c, theirs_c, 0.01)
    for pid in er["supply"]:
        chk(f"edw supply {pid}", edw["supply_open_loop"][pid]["train_mean_P"], er["supply"][pid]["train_mean_P"], 0.01)
    for pid in er["stress_replay_1950s"]:
        chk(f"edw replay {pid}", edw["replay_1950s"][pid]["min_head"], er["stress_replay_1950s"][pid]["min_H"], 0.01)
    chk("edw 1950s diag max err", edw["fit_diagnostic_1950s"]["max_abs_error"], er["fit_diagnostic_1950s"]["openloop_max_abs_error"], 0.05)
    au = A["edw_audit"]["closed_loop_replay"]["replay"]
    for pid, key in (("S1", "S1"), ("cpm", "CPM"), ("BAU", "BAU"), ("flat_90", "flat-90%"), ("flat_80", "flat-80%")):
        for w in ("train_1934_1990", "oos_1991_2023"):
            chk(f"edw closed-loop supply {pid}|{w}", edw["closed_loop"][pid][w]["mean_P"], au[f"{key}|{w}"]["mean_pumpage"], 0.01)
            chk(f"edw closed-loop end head {pid}|{w}", edw["closed_loop"][pid][w]["end_head"], au[f"{key}|{w}"]["end_head"], 0.15)
    ab = {d["policy"]: d for d in A["edw_audit"]["attractor_bootstrap"]["per_policy"]}
    for pid, key in (("BAU", "BAU"), ("flat_90", "flat-90%"), ("flat_80", "flat-80%"), ("flat_60", "flat-60%"), ("flat_0", "flat-0%")):
        chk(f"edw bootstrap P(attractor>=618) {pid} (independent seed, tol 0.02)", edw["bootstrap_independent"]["P_attractor_ge_618"][pid], ab[key]["p_attractor_ge_618"], 0.02)
    # independent stochastic layer vs the registered campaign (different seed; Monte-Carlo tolerance)
    st = {f'{r["scheme"]}|{r["policy"]}|S0={float(r["S0"]):g}|T={r["T"]}': float(r["P_stay"]) for r in A["stoch"]}
    for scheme, sch2 in (("iid", "iid"), ("block4", "block4")):
        for pid, c in (("BAU", 5), ("flat_25", 60), ("flat_50", 120)):
            key = f"{sch2}|{pid}|S0=884.6|T=20"
            if key in st:
                chk(f"cod stochastic {scheme} C={c} T=20 (independent seed, tol 0.015)", cod["stochastic_independent"][f"{scheme}|C={c}|S0=LRP|T=20"], st[key], 0.015)
    bf = A["boot_fixedK"]
    gk = np.array([float(r["g_Kstar"]) for r in bf]) - 80.86978040666266
    chk("cod fixed-K bootstrap C* median (independent seed, tol 3 kt)", cod["bootstrap_independent_fixedK"]["frozen_floor"]["Cstar_median"], float(np.median(gk)), 3.0)
    chk("cod fixed-K bootstrap share C*<=0 (independent seed, tol 0.02)", cod["bootstrap_independent_fixedK"]["frozen_floor"]["share_nonpositive"], float(np.mean(gk <= 0)), 0.02)
    n_fail = sum(1 for c in checks if not c["ok"])
    return checks, n_fail


def main():
    cod = run_cod()
    edw = run_edwards()
    A = read_archive()
    A["finite_floors_summary"] = {f'{r["floor"]}|{r["policy"]}|n={r["n_years"]}': (None if r["Tinf_lower_boundary"] in ("", "None") else float(r["Tinf_lower_boundary"])) for r in A["finite_floors"]}
    arch = summarise_archive(A)
    checks, n_fail = compare_with_archive(cod, edw, A)
    res = {"cod": cod, "edwards": edw, "archive": arch, "archive_checks": checks, "n_archive_checks": len(checks),
           "n_archive_check_failures": n_fail}
    (HERE / "results.json").write_text(json.dumps(res, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o)))
    print(f"wrote results.json; archive checks {len(checks) - n_fail}/{len(checks)} passed")
    for c in checks:
        if not c["ok"]:
            print("  FAIL", c)
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
