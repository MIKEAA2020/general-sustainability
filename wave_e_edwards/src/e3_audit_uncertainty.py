#!/usr/bin/env python3
"""E3 audit layer (post-freeze, labelled): uncertainty on the retention margins.

Implements the E3 joint-audit items that require computation:
  (A8/grok-5) Diebold-Mariano tests and moving-block bootstrap intervals for
    every load-bearing RMSE margin of the frozen retention decisions.
  (grok-10/claude B1) clip-binding check: does the [610, 710] clip bind on any
    fixed-window forecast path (recovery-window M2 trajectory).

Executed AFTER the freeze on the archived per-origin forecast files
(rolling_forecasts.csv, pass2_rolling.csv) and the registered panel
(annual_panel.csv). No frozen verdict is changed; this layer attaches
uncertainty to the already-reported margins. Deterministic (seeded).

Outputs: results/e3_audit_uncertainty.json
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
NBOOT = 10000
BLOCK = 8  # moving-block length for annual rolling-origin errors


def load_main():
    rows = list(csv.DictReader(open(os.path.join(RESULTS, "rolling_forecasts.csv"))))
    table = {}
    for r in rows:
        key = (r["model"], int(r["horizon"]), int(r["origin"]))
        table[key] = float(r["sqerr"])
    models = sorted({k[0] for k in table})
    horizons = sorted({k[1] for k in table})
    return table, models, horizons


def load_pass2_head():
    rows = list(csv.DictReader(open(os.path.join(RESULTS, "pass2_rolling.csv"))))
    table = {}
    for r in rows:
        if r["target"] != "H":
            continue
        key = (r["model"], int(r["horizon"]), int(r["origin"]))
        table[key] = float(r["sqerr"])
    return table


def series(table, model, h):
    origins = sorted(o for (m, hh, o) in table if m == model and hh == h)
    return np.array([table[(model, h, o)] for o in origins]), origins


def dm_test(sq_a, sq_b, h):
    """Diebold-Mariano on the squared-error loss differential with Newey-West HAC."""
    d = sq_a - sq_b
    n = len(d)
    dbar = d.mean()
    L = max(h - 1, 0)
    g0 = np.var(d, ddof=1)
    omega = g0
    for l in range(1, L + 1):
        w = 1.0 - l / (L + 1.0)
        gamma_l = np.mean((d[l:] - dbar) * (d[:-l] - dbar))
        omega += 2.0 * w * gamma_l
    dm = dbar / math.sqrt(omega / n)
    # two-sided p from Student t(n-1) via scipy
    from scipy import stats as _st

    p_two = float(2.0 * _st.t.sf(abs(dm), n - 1)) if dm != 0 else 1.0
    return dm, p_two


def block_bootstrap_margin(sq_a, sq_b, nboot=NBOOT, block=BLOCK, seed=SEED):
    """Moving-block bootstrap of the RMSE margin (RMSE_A - RMSE_B) over origins."""
    rng = np.random.default_rng(seed)
    n = len(sq_a)
    nblocks = int(math.ceil(n / block))
    margins = np.empty(nboot)
    for b in range(nboot):
        starts = rng.integers(0, n - block + 1, size=nblocks)
        idx = np.concatenate([np.arange(s, s + block) for s in starts])[:n]
        ra = math.sqrt(sq_a[idx].mean())
        rb = math.sqrt(sq_b[idx].mean())
        margins[b] = ra - rb
    lo, hi = np.percentile(margins, [2.5, 97.5])
    return lo, hi


def main():
    out = {"seed": SEED, "nboot": NBOOT, "block": BLOCK, "layer": "post-freeze audit layer (E3)"}
    main_table, models, horizons = load_main()
    pass2 = load_pass2_head()

    tests = []
    # (label, modelA, modelB, horizon, table)
    specs = [
        ("M1_vs_persist_h1", "M1", "naive_persist", 1, main_table),
        ("M2m_vs_persist_h1", "M2m", "naive_persist", 1, main_table),
        ("M2m_vs_M1_h1", "M2m", "M1", 1, main_table),
        ("M2_vs_persist_h1", "M2", "naive_persist", 1, main_table),
        ("mean_vs_persist_h5", "naive_mean", "naive_persist", 5, main_table),
        ("M1_vs_persist_h5", "M1", "naive_persist", 5, main_table),
    ]
    for label, ma, mb, h, tab in specs:
        sa, oa = series(tab, ma, h)
        sb, ob = series(tab, mb, h)
        assert oa == ob, (label, "origin mismatch")
        dm, p = dm_test(sa, sb, h)
        lo, hi = block_bootstrap_margin(sa, sb)
        rmse_a = math.sqrt(sa.mean())
        rmse_b = math.sqrt(sb.mean())
        tests.append(
            {
                "comparison": f"{ma} vs {mb} (h={h}, n={len(sa)})",
                "rmse_a": round(rmse_a, 4),
                "rmse_b": round(rmse_b, 4),
                "margin_rmse": round(rmse_a - rmse_b, 4),
                "dm_stat": round(dm, 3),
                "dm_p_two_sided": round(p, 4),
                "blockboot_margin_95ci": [round(lo, 3), round(hi, 3)],
                "ci_covers_zero": bool(lo <= 0.0 <= hi),
            }
        )

    # climate kink: M2_combo vs M1 (h=1, head target, pass2) and vs M2m (joined)
    sa, oa = series(pass2, "M2_combo", 1)
    sb, ob = series(main_table, "M1", 1)
    common = sorted(set(oa) & set(ob))
    ia = np.array([oa.index(o) for o in common])
    ib = np.array([ob.index(o) for o in common])
    sq_combo = sa[ia]
    sq_m1 = sb[ib]
    dm, p = dm_test(sq_combo, sq_m1, 1)
    lo, hi = block_bootstrap_margin(sq_combo, sq_m1)
    tests.append(
        {
            "comparison": f"M2_combo vs M1 (h=1, n={len(common)}, pass2 head)",
            "rmse_a": round(math.sqrt(sq_combo.mean()), 4),
            "rmse_b": round(math.sqrt(sq_m1.mean()), 4),
            "margin_rmse": round(math.sqrt(sq_combo.mean()) - math.sqrt(sq_m1.mean()), 4),
            "dm_stat": round(dm, 3),
            "dm_p_two_sided": round(p, 4),
            "blockboot_margin_95ci": [round(lo, 3), round(hi, 3)],
            "ci_covers_zero": bool(lo <= 0.0 <= hi),
        }
    )
    sm2m, om2m = series(main_table, "M2m", 1)
    im = np.array([om2m.index(o) for o in common])
    sq_m2m = sm2m[im]
    dm, p = dm_test(sq_combo, sq_m2m, 1)
    lo, hi = block_bootstrap_margin(sq_combo, sq_m2m)
    tests.append(
        {
            "comparison": f"M2_combo vs M2m (h=1, n={len(common)}, climate kink)",
            "rmse_a": round(math.sqrt(sq_combo.mean()), 4),
            "rmse_b": round(math.sqrt(sq_m2m.mean()), 4),
            "margin_rmse": round(math.sqrt(sq_combo.mean()) - math.sqrt(sq_m2m.mean()), 4),
            "dm_stat": round(dm, 3),
            "dm_p_two_sided": round(p, 4),
            "blockboot_margin_95ci": [round(lo, 3), round(hi, 3)],
            "ci_covers_zero": bool(lo <= 0.0 <= hi),
        }
    )
    out["dm_tests"] = tests

    # ---- clip-binding check: recovery-window M2 trajectory ----
    rows = [
        r
        for r in csv.DictReader(open(os.path.join(DATA, "annual_panel.csv")))
        if r["H_mean"] and r["R_total"] and r["P_wells"]
    ]
    yrs = np.array([int(r["year"]) for r in rows])
    H = {int(r["year"]): float(r["H_mean"]) for r in rows}
    R = {int(r["year"]): float(r["R_total"]) for r in rows}
    P = {int(r["year"]): float(r["P_wells"]) for r in rows}
    train_rec = [y for y in range(1935, 1957)]  # recovery train: 22 transitions
    train_dr = [y for y in range(1935, 1951)]  # drawdown train: 16 transitions

    def ols_fit(train_years):
        X = np.array([[1.0, R[y], P[y], H[y - 1]] for y in train_years])
        yv = np.array([H[y] for y in train_years])
        c, *_ = np.linalg.lstsq(X, yv, rcond=None)
        return c

    c_dr = ols_fit(train_dr)  # drawdown-window fit (gamma cross-check)
    A, B, C, D = ols_fit(train_rec)  # recovery-window fit
    # forecast 1957..1961 from H[1956] with persisted (R1956, P1956)
    Rp, Pp = R[1956], P[1956]
    traj = []
    h = H[1956]
    for step in range(1, 6):
        raw = A + B * Rp + C * Pp + D * h
        clipped = min(max(raw, 610.0), 710.0)
        traj.append({"year": 1956 + step, "raw": round(raw, 2), "clipped": round(clipped, 2)})
        h = clipped
    # drawdown-window M2 as the published-RMSE cross-check (train 1935-1950)
    A2, B2, C2, D2 = c_dr
    h2 = H[1950]
    traj2 = []
    for step in range(1, 7):
        raw2 = A2 + B2 * R[1950] + C2 * P[1950] + D2 * h2
        traj2.append({"year": 1950 + step, "raw": round(raw2, 2)})
        h2 = raw2
    out["recovery_M2_trajectory"] = {
        "recovery_train_window": "1934-1956 (22 transitions), test 1957-1961",
        "fitted_A_B_C_D_recovery": [round(v, 5) for v in (A, B, C, D)],
        "drawdown_crosscheck": {
            "train_window": "1934-1950 (16 transitions)",
            "fitted_A_B_C_D": [round(v, 5) for v in c_dr],
            "gamma": round(C2, 4),
            "paper_gamma": 0.021,
            "drawdown_M2_rmse": round(
                math.sqrt(np.mean([(t["raw"] - H[t["year"]]) ** 2 for t in traj2])), 2
            ),
            "paper_drawdown_M2_rmse": 18.11,
        },
        "persisted_R_P": [Rp, Pp],
        "start_H_1956": H[1956],
        "trajectory": traj,
        "clip_binds": any(t["raw"] < 610.0 or t["raw"] > 710.0 for t in traj),
        "first_binding_year": next(
            (t["year"] for t in traj if t["raw"] < 610.0 or t["raw"] > 710.0), None
        ),
        "observed_1957_1961": [H[y] for y in range(1957, 1962)],
        "rmse_vs_observed": round(
            math.sqrt(np.mean([(t["clipped"] - H[t["year"]]) ** 2 for t in traj])), 2
        ),
        "paper_recovery_M2_rmse": 55.32,
    }

    path = os.path.join(RESULTS, "e3_audit_uncertainty.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))
    print("\nwritten:", path)


if __name__ == "__main__":
    main()
