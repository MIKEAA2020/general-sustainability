#!/usr/bin/env python3
"""E4 audit layer (post-freeze, labelled): the audit's computational asks.

Implements the E4 joint-audit items that require computation, executed AFTER the
freeze on the registered panel and the paper's own fitted map (no refit of the
governed object; all coefficients as declared in the paper):
  (claude A4 / grok-2)  CLOSED-LOOP historical-replay supply: replay the closed
      loop P_{t+1} = pi(H_t) under ACTUAL recharge with the head simulated by
      the map (not the observed heads the open-loop Table 2 replay used).
  (claude A1 / grok-1)  Residual-bootstrap uncertainty on the worst-case
      attractors: P(attractor >= 618 ft) per policy, BAU vs 10% cut resolvability.
  (grok-6 / claude A2, A3, A6, A5) Analytic sensitivities: OOS-defect erosion,
      current-pumpage baseline, comparator grid (1% grid and interpolated 7.2%),
      horizon-as-function-of-ceiling, certified-threshold-vs-trigger-band.

No frozen verdict is changed. Deterministic (seeded).
Outputs: results/e4_audit_layer.json
"""
import csv
import json
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS = os.path.join(HERE, "results")
DATA = os.path.join(HERE, "data")

SEED = 20260905
NBOOT = 5000

# The paper's declared fit (Definition 2.1, Section 2.1) -- not refit here.
ALPHA, BETA, GAMMA, DELTA = 163.49, 0.0198, -0.02844, -0.2539
A_RATE = 1.0 + DELTA  # 0.7461
EPS_TRAIN = 15.41
EPS_OOS = 21.81
PBAR = 282.16  # training-mean pumpage 1934-1990
KPHYS = 618.0
KINST = 660.0
DOMAIN = (610.0, 710.0)
R_UCMIN = 43.7


def policies():
    """Policy family as declared (Section 2.3). Each pi(H) -> prescribed pumpage."""

    def flat(rho):
        return lambda h: rho * PBAR

    def s1(h):
        return 0.8 * PBAR if h < KINST else PBAR

    def cpm(h):
        if h < 630.0:
            return 0.60 * PBAR
        if h < 640.0:
            return 0.65 * PBAR
        if h < 650.0:
            return 0.70 * PBAR
        if h < KINST:
            return 0.80 * PBAR
        return PBAR

    fam = {f"flat-{int(rho*100)}%": flat(rho) for rho in (0.9, 0.8, 0.7, 0.6, 0.5, 0.0)}
    fam["BAU"] = flat(1.0)
    fam["S1"] = s1
    fam["CPM"] = cpm
    return fam


def attractor(pi, R_floor):
    """Worst-case attractor of the closed loop under constant recharge floor."""
    h = 650.0
    for _ in range(4000):
        h = h + ALPHA + BETA * R_floor + GAMMA * pi(h) + DELTA * h
    return h


def closed_loop_replay():
    """(claude A4) Closed-loop supply under actual recharge, head simulated."""
    rows = [
        r
        for r in csv.DictReader(open(os.path.join(DATA, "annual_panel.csv")))
        if r["H_mean"] and r["R_total"] and r["P_wells"]
    ]
    R = {int(r["year"]): float(r["R_total"]) for r in rows}
    H_obs = {int(r["year"]): float(r["H_mean"]) for r in rows}
    H0 = H_obs[1934]
    fam = policies()
    out = {}
    for name, pi in fam.items():
        for span, years, h_start in [
            ("train_1934_1990", range(1935, 1991), H0),
            ("oos_1991_2023", range(1991, 2024), H_obs[1990]),
        ]:
            h = h_start
            pump = []
            heads = []
            exited = False
            for y in years:
                p = pi(h)
                pump.append(p)
                h = h + ALPHA + BETA * R[y] + GAMMA * p + DELTA * h
                if not (DOMAIN[0] <= h <= DOMAIN[1]):
                    exited = True
                h = min(max(h, DOMAIN[0]), DOMAIN[1])
                heads.append(h)
            out[f"{name}|{span}"] = {
                "mean_pumpage": round(float(np.mean(pump)), 2),
                "cut_active_fraction": round(
                    float(np.mean([p < 282.16 - 1e-9 for p in pump])), 3
                ),
                "end_head": round(heads[-1], 1),
                "min_head": round(min(heads), 1),
                "max_head": round(max(heads), 1),
                "domain_exit_raw": exited,
                "start_head": round(h_start, 1),
            }
    # open-loop supplies (paper Table 2) for the margin comparison
    table2 = {
        "BAU": 282.16, "flat-90%": 253.94, "flat-80%": 225.73, "flat-70%": 197.51,
        "S1": 262.36, "CPM": 254.93, "flat-60%": 169.29, "flat-50%": 141.08,
        "flat-0%": 0.0,
    }
    comparison = []
    for name in table2:
        cl = out[f"{name}|train_1934_1990"]["mean_pumpage"]
        ol = table2[name]
        comparison.append(
            {
                "policy": name,
                "openloop_supply_table2": ol,
                "closedloop_supply": cl,
                "closedloop_minus_openloop": round(cl - ol, 2),
                "closedloop_pct_change": round(100.0 * (cl - ol) / ol, 2) if ol > 0 else None,
            }
        )
    # retention margins recomputed on the closed-loop supplies
    s1_cl = out["S1|train_1934_1990"]["mean_pumpage"]
    cpm_cl = out["CPM|train_1934_1990"]["mean_pumpage"]
    f90_cl = out["flat-90%|train_1934_1990"]["mean_pumpage"]
    f80_cl = out["flat-80%|train_1934_1990"]["mean_pumpage"]
    f60_cl = out["flat-60%|train_1934_1990"]["mean_pumpage"]
    comparison_summary = {
        "S1_vs_flat90_closedloop_pct": round(100.0 * (s1_cl - f90_cl) / f90_cl, 2),
        "S1_vs_flat80_closedloop_pct": round(100.0 * (s1_cl - f80_cl) / f80_cl, 2),
        "CPM_vs_flat60_closedloop_pct": round(100.0 * (cpm_cl - f60_cl) / f60_cl, 2),
        "CPM_vs_flat90_closedloop_pct": round(100.0 * (cpm_cl - f90_cl) / f90_cl, 2),
        "closedloop_bias_1990_BAU": {
            "simulated_end_1990": out["BAU|train_1934_1990"]["end_head"],
            "observed_1990": round(H_obs[1990], 1),
        },
    }
    return {
        "replay": out,
        "table2_comparison": comparison,
        "closedloop_margin_summary": comparison_summary,
    }


def attractor_bootstrap():
    """(claude A1) Residual bootstrap of the OLS fit -> attractor distribution."""
    rows = [
        r
        for r in csv.DictReader(open(os.path.join(DATA, "annual_panel.csv")))
        if r["H_mean"] and r["R_total"] and r["P_wells"]
    ]
    H = {int(r["year"]): float(r["H_mean"]) for r in rows}
    R = {int(r["year"]): float(r["R_total"]) for r in rows}
    P = {int(r["year"]): float(r["P_wells"]) for r in rows}
    train = list(range(1935, 1991))
    X = np.array([[1.0, R[y], P[y], H[y - 1]] for y in train])
    yv = np.array([H[y] for y in train])
    beta, *_ = np.linalg.lstsq(X, yv, rcond=None)
    resid = yv - X @ beta
    fam = policies()
    rng = np.random.default_rng(SEED)
    stars = {name: np.full(NBOOT, np.nan) for name in fam}
    noncontractive = 0
    for b in range(NBOOT):
        e = rng.choice(resid, size=len(train), replace=True)
        yb = X @ beta + e
        bb, *_ = np.linalg.lstsq(X, yb, rcond=None)
        al, be, ga, a_star = bb  # X regresses H_t on [1, R, P, H_{t-1}]
        de = a_star - 1.0  # delta*
        if not (0.0 < a_star < 1.0):
            noncontractive += 1
            continue  # no finite attractor on this refit; recorded separately
        for name, pi in fam.items():
            h = 650.0
            for _ in range(500):
                h = h + al + be * R_UCMIN + ga * pi(h) + de * h
            stars[name][b] = h
    valid = ~np.isnan(stars["BAU"])
    summary = []
    for name in fam:
        s = stars[name][valid]
        summary.append(
            {
                "policy": name,
                "attractor_point": round(attractor(fam[name], R_UCMIN), 2),
                "boot_mean": round(float(s.mean()), 2),
                "boot_sd": round(float(s.std(ddof=1)), 2),
                "boot_q05_q50_q95": [round(float(q), 2) for q in np.percentile(s, [5, 50, 95])],
                "p_attractor_ge_618": round(float((s >= KPHYS).mean()), 4),
            }
        )
    return {
        "nboot": NBOOT,
        "seed": SEED,
        "noncontractive_reps": int(noncontractive),
        "valid_reps": int(valid.sum()),
        "note": "residual bootstrap of the 1934-1990 OLS fit; replications with "
        "1+delta* outside (0,1) have no finite attractor and are reported "
        "separately, not dropped silently",
        "per_policy": summary,
        "resolvability": {
            "p_BAU_ge_618": round(float((stars["BAU"][valid] >= KPHYS).mean()), 4),
            "p_flat90_ge_618": round(float((stars["flat-90%"][valid] >= KPHYS).mean()), 4),
            "p_flat80_ge_618": round(float((stars["flat-80%"][valid] >= KPHYS).mean()), 4),
            "p_S1_ge_618": round(float((stars["S1"][valid] >= KPHYS).mean()), 4),
            "p_CPM_ge_618": round(float((stars["CPM"][valid] >= KPHYS).mean()), 4),
            "p_flat60_ge_618": round(float((stars["flat-60%"][valid] >= KPHYS).mean()), 4),
            "BAU_minus_flat90_gap_boot_q05_q95": [
                round(float(q), 2)
                for q in np.percentile(stars["flat-90%"][valid] - stars["BAU"][valid], [5, 95])
            ],
        },
    }


def sensitivities():
    """(grok-6, claude A2/A3/A5/A6) analytic sensitivity table."""
    out = {}
    # OOS-defect erosion (grok-6)
    def rT(eps, T):
        return eps * (1.0 - A_RATE ** T) / (1.0 - A_RATE)

    out["erosion"] = {
        "eps_train": EPS_TRAIN,
        "eps_oos": EPS_OOS,
        "r_T_train": {str(T): round(rT(EPS_TRAIN, T), 2) for T in (1, 3, 4, 5, 10)},
        "r_T_oos": {str(T): round(rT(EPS_OOS, T), 2) for T in (1, 3, 4, 5, 10)},
    }
    out["erosion"]["r_T_train"]["inf"] = round(EPS_TRAIN / (1 - A_RATE), 2)
    out["erosion"]["r_T_oos"]["inf"] = round(EPS_OOS / (1 - A_RATE), 2)
    # certified threshold vs the 660 trigger (claude A5)
    out["certified_threshold_vs_trigger"] = {
        "K_star_plus_rT_train": {
            T: round(KPHYS + rT(EPS_TRAIN, T), 2) for T in (1, 3, 4, 5)
        },
        "trigger_crossing": "K*+r_T crosses 660 ft between T=4 (659.9) and T=5 (664.7); "
        "any threshold-erosion certificate makes every below-660 trigger rule "
        "identical to BAU from T>=4",
        "contraction_identical_across_policies": True,
    }
    # current-baseline re-expression (claude A2)
    p_cur = 382.16  # 1991-2023 mean actual pumpage (companion Table 7)
    h_bau_cur = (ALPHA + BETA * R_UCMIN + GAMMA * p_cur) / (1 - A_RATE)
    # securing cut at current baseline: rho such that attractor = 618
    # attractor(rho) = (alpha + beta R + gamma rho P_cur)/(1-a)
    target_num = KPHYS * (1 - A_RATE) - ALPHA - BETA * R_UCMIN
    rho_star_cur = target_num / (GAMMA * p_cur)
    h_s1_cur = (ALPHA + BETA * R_UCMIN + GAMMA * 0.8 * p_cur) / (1 - A_RATE)
    h_flat80_cur = h_s1_cur
    out["current_baseline"] = {
        "mean_actual_pumpage_1991_2023": p_cur,
        "BAU_current_attractor_UCmin": round(h_bau_cur, 2),
        "securing_cut_fraction_current": round(1 - rho_star_cur, 4),
        "securing_cut_percent_current": round(100 * (1 - rho_star_cur), 1),
        "S1_flat80_current_attractor_UCmin": round(h_s1_cur, 2),
        "S1_secures_at_current_baseline": bool(h_s1_cur >= KPHYS),
        "note": "Stage I (20% cut) does NOT hold 618 ft at the current-mean baseline; "
        "the 7.2% securing cut is relative to the 1934-1990 training mean.",
    }
    # comparator grid (claude A3)
    s1_open, cpm_open = 262.36, 254.93
    grid = []
    for rho in (0.93, 0.92, 0.91, "interp_0.928", 0.90):
        if rho == "interp_0.928":
            supply = 0.928 * PBAR
            label = "interpolated 7.2% cut (rho=0.928, outside family)"
        else:
            supply = rho * PBAR
            label = f"flat-{int(rho*100)}% (1% grid)"
        grid.append(
            {
                "comparator": label,
                "supply": round(supply, 2),
                "S1_margin_pct": round(100 * (s1_open - supply) / supply, 2),
                "CPM_margin_pct": round(100 * (cpm_open - supply) / supply, 2),
                "CPM_passes": bool(cpm_open > supply),
            }
        )
    out["comparator_grid"] = grid
    # horizon as function of ceiling (claude A6 / grok-8)
    h_bau = (ALPHA + BETA * R_UCMIN + GAMMA * PBAR) / (1 - A_RATE)
    gap = KPHYS - h_bau

    def t_empty(ceiling):
        return math.log((ceiling - h_bau) / gap) / math.log(1.0 / A_RATE)

    out["horizon_vs_ceiling_BAU_UCmin_618"] = {
        "H_star": round(h_bau, 2),
        "gap_to_618": round(gap, 3),
        "T_empty(710)": round(t_empty(710.0), 2),
        "T_empty(692.7_observed_max_annual_mean)": round(t_empty(692.7), 2),
        "no_ceiling": "the kernel is never empty in the domain sense; every state "
        "converges to the attractor, and 'empty beyond T' means the required "
        "initial head exceeds the ceiling",
        "formula": "T_empty(C) = ln((C - H*)/(K* - H*)) / ln(1/a)",
    }
    return out


def main():
    out = {
        "layer": "post-freeze audit layer (E4)",
        "declared_fit": {
            "alpha": ALPHA, "beta": BETA, "gamma": GAMMA, "delta": DELTA, "a": A_RATE,
        },
    }
    out["closed_loop_replay"] = closed_loop_replay()
    out["attractor_bootstrap"] = attractor_bootstrap()
    out["sensitivities"] = sensitivities()
    path = os.path.join(RESULTS, "e4_audit_layer.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print("written:", path)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
