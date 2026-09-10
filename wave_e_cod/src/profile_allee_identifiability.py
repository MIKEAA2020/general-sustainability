"""
profile_allee_identifiability.py
--------------------------------
Profile-likelihood diagnostic for the Allee threshold parameter (s) of the M1b
depensation module on the Northern cod recovery window (train 1995-2007).

Reported in Section 3.2 (Observation 3.2). For each fixed s on a grid over the
admissible range [0, min_train S_t], r and K are re-optimised from a multi-start
set; the resulting profile objective is converted to a likelihood-ratio statistic
n*log(SSE(s)/SSE_min) and referred to chi2_1.

Admissible range: the depensation factor a(S) = (S - s)/(K - s) is negative for
observations below s, so s above min_train S_t predicts negative production where
the observed increment is positive. min_train S_t = 9.68 kt on this window.

Inputs : wave_e_cod/data/ncam_2016_table_a2.csv
Output : stdout table + results/allee_profile.csv

Deterministic. Bounds and the multi-start initialiser match run_ladder.fit_params.
"""
import os
import numpy as np
import pandas as pd
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
SER = os.path.join(ROOT, "data", "ncam_2016_table_a2.csv")
OUT = os.path.join(ROOT, "results", "allee_profile.csv")

TRAIN = (1995, 2007)
CHI2_1_95 = 3.841


def load():
    ser = pd.read_csv(SER)[["year", "ssb_kt"]].set_index("year")["ssb_kt"]
    S = ser.loc[TRAIN[0]:TRAIN[1]].values.astype(float)
    return S[:-1], np.diff(S)          # predictors S0, increments dS


def profile_at(s, C, S0, dS):
    """Minimise the one-step SSE over (r, K) with s held fixed."""
    loK = float(np.max(S0) + 10.0)

    def obj(theta):
        r, K = theta
        if K <= s:
            return 1e12
        a = (S0 - s) / (K - s)
        return float(np.mean((r * S0 * (1 - S0 / K) * a - C - dS) ** 2))

    best = None
    for K0 in (500.0, 150.0, 1000.0, 3000.0, 5000.0):
        for r0 in (0.2, 0.6, 1.2, 1.9):
            res = minimize(obj, [r0, K0], method="L-BFGS-B",
                           bounds=[(1e-3, 2.0), (max(loK, s + 1e-9), 5000.0)])
            if best is None or res.fun < best.fun:
                best = res
    return float(best.fun), float(best.x[0]), float(best.x[1])


def run(C, label, S0, dS, npts=49):
    n = len(dS)
    smax = float(np.min(S0))                    # admissible upper limit
    grid = np.linspace(0.0, smax * 0.992, npts)
    rows = [(s,) + profile_at(s, C, S0, dS) for s in grid]
    mse = np.array([r[1] for r in rows])
    lr = n * np.log(mse / mse.min())
    ok = grid[lr < CHI2_1_95]

    print(f"\n=== {label} (C = {C} kt) ===")
    print(f"{'s (kt)':>8} {'profile MSE':>12} {'r':>7} {'K':>9} {'LR':>7}")
    for (s, v, r_, K_), l in list(zip(rows, lr))[::6]:
        print(f"{s:8.2f} {v:12.2f} {r_:7.3f} {K_:9.1f} {l:7.2f}")
    print(f"admissible range for s: [0, {smax:.2f}] kt")
    print(f"profile MSE: {mse.min():.2f} to {mse.max():.2f} kt^2")
    print(f"max LR statistic: {lr.max():.2f}  (chi2_1 5% = {CHI2_1_95})")
    print(f"confidence set for s: [{ok.min():.2f}, {ok.max():.2f}] kt "
          f"-> {100 * len(ok) / len(grid):.0f}% of the grid retained")
    Ks = np.array([r[3] for r in rows])
    print(f"K compensates from {Ks[0]:.1f} to {Ks[-1]:.1f} kt; "
          f"r stays at {rows[0][2]:.3f}")
    if lr.max() < CHI2_1_95:
        print("VERDICT: s is not identified -- no admissible value is rejected.")
    return pd.DataFrame(
        {"treatment": label, "C_kt": C, "s_kt": grid, "profile_mse": mse,
         "r": [r[2] for r in rows], "K_kt": Ks, "lr_stat": lr})


def main():
    S0, dS = load()
    out = pd.concat([run(5.0, "coarse regime", S0, dS),
                     run(3.19, "annual landings", S0, dS)], ignore_index=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out.to_csv(OUT, index=False)
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
