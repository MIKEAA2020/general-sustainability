#!/usr/bin/env python3
"""Reproduce Paper10b v3's post-freeze 618/660-ft attractor sensitivity.

This extends the existing E4 residual bootstrap with a second threshold.
It reuses the 1934-1990 OLS fit, iid residual resampling, 5,000 refits,
seed, UC-min floor, and 500-step policy iteration. It does NOT rescore the
frozen retention rule or recompute finite-horizon viability kernels.
"""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
PANEL = HERE / "annual_panel.csv"
OUT_ZERO = HERE / "zero_pumping_660_bootstrap.csv"
OUT_POLICIES = HERE / "policy_attractor_bootstrap_660.csv"
SEED = 20260905
NBOOT = 5_000
TRAIN_START = 1935  # first transition year; H_{1934} is the lag
TRAIN_END = 1990
R_UCMIN = 43.7
PBAR = 282.16
K_PHYS = 618.0
K_INST = 660.0
# Rounded coefficients declared in Paper10b Section 2.2, used for point fits.
POINT_ALPHA, POINT_BETA, POINT_GAMMA, POINT_A = 163.49, 0.0198, -0.02844, 0.7461


def load_panel():
    with PANEL.open(newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r.get("H_mean") and r.get("R_total") and r.get("P_wells")]
    data = {int(r["year"]): r for r in rows}
    years = list(range(1934, 2024))
    if any(y not in data for y in years):
        raise ValueError("Expected a complete annual panel for 1934-2023")
    H = {y: float(data[y]["H_mean"]) for y in years}
    R = {y: float(data[y]["R_total"]) for y in years}
    P = {y: float(data[y]["P_wells"]) for y in years}
    return H, R, P


def policies():
    """Paper's annual-mean policy family as functions of current head."""
    def flat(rho):
        return lambda h: rho * PBAR

    def s1(h):
        return 0.8 * PBAR if h < K_INST else PBAR

    def cpm(h):
        if h < 630.0:
            return 0.60 * PBAR
        if h < 640.0:
            return 0.65 * PBAR
        if h < 650.0:
            return 0.70 * PBAR
        if h < K_INST:
            return 0.80 * PBAR
        return PBAR

    fam = {f"flat-{int(rho * 100)}%": flat(rho) for rho in (0.9, 0.8, 0.7, 0.6, 0.5, 0.0)}
    fam["BAU"] = flat(1.0)
    fam["S1"] = s1
    fam["CPM"] = cpm
    return fam


def iterate_attractor(pi, coefs, steps=500):
    """Match the E4 audit's iteration from H=650 under constant UC-min R."""
    alpha, beta, gamma, a = coefs
    h = 650.0
    for _ in range(steps):
        h = a * h + alpha + beta * R_UCMIN + gamma * pi(h)
    return h


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def main():
    H, R, P = load_panel()
    train = list(range(TRAIN_START, TRAIN_END + 1))
    X = np.array([[1.0, R[y], P[y], H[y - 1]] for y in train], dtype=float)
    y_obs = np.array([H[y] for y in train], dtype=float)
    fit, *_ = np.linalg.lstsq(X, y_obs, rcond=None)
    residuals = y_obs - X @ fit

    family = policies()
    policy_order = ["BAU", "flat-90%", "flat-80%", "S1", "flat-70%", "flat-60%", "CPM", "flat-50%", "flat-0%"]
    stars = {name: np.empty(NBOOT, dtype=float) for name in family}
    noncontractive = 0
    gamma_nonnegative = 0
    rng = np.random.default_rng(SEED)
    for b in range(NBOOT):
        eps = rng.choice(residuals, size=len(train), replace=True)
        yb = X @ fit + eps
        beta_star, *_ = np.linalg.lstsq(X, yb, rcond=None)
        alpha_b, beta_b, gamma_b, a_b = beta_star
        if gamma_b >= 0.0:
            gamma_nonnegative += 1
        if not (0.0 < a_b < 1.0):
            noncontractive += 1
            continue
        for name, pi in family.items():
            stars[name][b] = iterate_attractor(pi, beta_star)

    valid = NBOOT - noncontractive
    if valid != NBOOT:
        raise RuntimeError("This implementation expects all 5,000 draws to be contractive, as in the archived E4 audit")
    panel_sha = hashlib.sha256(PANEL.read_bytes()).hexdigest()

    # The zero-pumping fixed point is affine; use its exact formula as an
    # independent numerical check on the 500-step policy iteration.
    alpha0, beta0, _, a0 = fit
    hstar_zero_exact = (alpha0 + beta0 * R_UCMIN) / (1.0 - a0)
    zero = stars["flat-0%"]
    q05_zero, q50_zero, q95_zero = np.percentile(zero, [5, 50, 95])
    n_zero_ge_618 = int(np.sum(zero >= K_PHYS))
    n_zero_ge_660 = int(np.sum(zero >= K_INST))
    zero_row = {
        "panel_sha256": panel_sha,
        "fit_window": "1934-1990 transitions",
        "bootstrap": "iid residual resampling of training OLS residuals",
        "seed": SEED,
        "n_boot": NBOOT,
        "valid_contractive_refits": valid,
        "noncontractive_refits": noncontractive,
        "gamma_nonnegative_refits": gamma_nonnegative,
        "recharge_floor_R_UCmin": R_UCMIN,
        "zero_pump_point_attractor_ft": float(iterate_attractor(family["flat-0%"], (POINT_ALPHA, POINT_BETA, POINT_GAMMA, POINT_A))),
        "zero_pump_refit_point_attractor_ft": float(hstar_zero_exact),
        "zero_pump_q05_ft": float(q05_zero),
        "zero_pump_median_ft": float(q50_zero),
        "zero_pump_q95_ft": float(q95_zero),
        "n_zero_pump_attractor_ge_618": n_zero_ge_618,
        "share_zero_pump_attractor_ge_618": float(n_zero_ge_618 / valid),
        "n_zero_pump_attractor_ge_660": n_zero_ge_660,
        "share_zero_pump_attractor_ge_660": float(n_zero_ge_660 / valid),
        "scope": "parameter-fit sensitivity only; not a field-safety probability or kernel/retention recalculation",
    }
    write_csv(OUT_ZERO, [zero_row])

    policy_rows = []
    for name in policy_order:
        s = stars[name]
        # Point-attractor values in the manuscript are computed from the
        # paper's declared rounded coefficient vector, not the resampled fit.
        point = iterate_attractor(family[name], (POINT_ALPHA, POINT_BETA, POINT_GAMMA, POINT_A))
        n618 = int(np.sum(s >= K_PHYS))
        n660 = int(np.sum(s >= K_INST))
        q05, q50, q95 = np.percentile(s, [5, 50, 95])
        policy_rows.append({
            "policy": name,
            "point_attractor_ft": float(point),
            "bootstrap_mean_ft": float(np.mean(s)),
            "bootstrap_sd_ft": float(np.std(s, ddof=1)),
            "bootstrap_q05_ft": float(q05),
            "bootstrap_median_ft": float(q50),
            "bootstrap_q95_ft": float(q95),
            "n_attractor_ge_618": n618,
            "share_attractor_ge_618": float(n618 / valid),
            "n_attractor_ge_660": n660,
            "share_attractor_ge_660": float(n660 / valid),
            "n_valid_refits": valid,
            "seed": SEED,
            "recharge_floor_R_UCmin": R_UCMIN,
        })
    write_csv(OUT_POLICIES, policy_rows)

    # Regression checks against the archived E4 audit and the new 660-ft run.
    assert gamma_nonnegative == 0
    assert abs(zero_row["zero_pump_point_attractor_ft"] - 647.32) < 0.02
    assert abs(q05_zero - 628.99) < 0.03 and abs(q50_zero - 647.33) < 0.03
    assert abs(q95_zero - 661.16) < 0.03
    assert n_zero_ge_618 == 4_947 and n_zero_ge_660 == 344
    assert all(row["n_attractor_ge_660"] == 0 for row in policy_rows if row["policy"] != "flat-0%")
    assert sum(row["n_attractor_ge_660"] for row in policy_rows if row["policy"] == "flat-0%") == 344
    assert abs(next(r["share_attractor_ge_618"] for r in policy_rows if r["policy"] == "BAU") - 0.4148) < 1e-12
    assert abs(next(r["share_attractor_ge_618"] for r in policy_rows if r["policy"] == "flat-90%") - 0.5336) < 1e-12

    print(f"wrote {OUT_ZERO}")
    print(f"wrote {OUT_POLICIES}")
    print(f"valid={valid}; noncontractive={noncontractive}; gamma>=0={gamma_nonnegative}")
    print(f"zero-pump point={zero_row['zero_pump_point_attractor_ft']:.2f}; q05/q50/q95={q05_zero:.2f}/{q50_zero:.2f}/{q95_zero:.2f}")
    print(f"zero-pump share(H*>=618)={n_zero_ge_618/valid:.4f}; share(H*>=660)={n_zero_ge_660/valid:.4f}")
    print("P(H*>=660) by policy: " + ", ".join(f"{r['policy']}={r['share_attractor_ge_660']:.4f}" for r in policy_rows))


if __name__ == "__main__":
    main()
