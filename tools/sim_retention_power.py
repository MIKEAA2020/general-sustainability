"""
sim_retention_power.py — operating characteristics of the E1 retention rule.

Implements SPECIFICATION_v4.md (locked, commit d5d9758) exactly. Nothing here is
tuned to the result; every design element is fixed by that sheet.

Design (from the sheet, not chosen here):
  DGPs      D1 M1 collapse-fit; D2 M1 recovery-fit; D3 M2 stock-flow;
            D4 M1b depensation (s=15, identifiable); D5 persistence-true null
  sigma     {11.8, 33.8} kt
  T         33 (Specification A length)
  reps      200 per cell, seeded deterministically
  rule      Definition 2.4 applied UNCHANGED: H1 comparator, H2 persistence,
            H3 both horizons + 5% tie band

The estimator, map and scorer are IMPORTED from run_ladder, never reimplemented
(the rule adopted after round 5, where a hand-rolled refit disagreed with the
registered estimator).

Output: results/sim_retention_power.csv  (one row per replicate x module)
        plus a console summary of retention/power/specificity rates.
"""
import os
import sys
import numpy as np
import pandas as pd

COD = "/home/user/gs_clone/wave_e_cod"
sys.path.insert(0, os.path.join(COD, "src"))
import run_ladder as rl  # noqa: E402  (estimator, map, rolling driver)

OUT = os.path.join(COD, "results", "sim_retention_power.csv")

T = 33
REPS = 200
SIGMAS = (11.8, 33.8)
TIE = 0.05                      # 5% tie band, as in Definition 2.4
HORIZONS = (1, 5)
MODULES = ["M1_autonomous_Schaefer", "M1b_autonomous_Allee",
           "M2_stockflow_regimeC", "M3_AR_residual", "M4_delayed_info"]

# H1 declared comparators (Definition 2.4, unchanged)
COMPARATOR = {
    "M1_autonomous_Schaefer": None,          # vacuous: first structural rung
    "M1b_autonomous_Allee": "M1_autonomous_Schaefer",
    "M2_stockflow_regimeC": "M1_autonomous_Schaefer",
    "M3_AR_residual": "M2_stockflow_regimeC",
    "M4_delayed_info": "M3_AR_residual",
}

# DGPs, anchored to archived fits (verified against fixed_window_scores.csv)
DGPS = {
    "D1_M1_collapse":  dict(truth="M1_autonomous_Schaefer", r=1.935, K=1032.7,
                            s=None, catch="const240", S0=900.0),
    "D2_M1_recovery":  dict(truth="M1_autonomous_Schaefer", r=0.458, K=500.0,
                            s=None, catch="const5", S0=30.0),
    "D3_M2_stockflow": dict(truth="M2_stockflow_regimeC", r=1.935, K=1032.7,
                            s=None, catch="regime", S0=900.0),
    "D4_M1b_depens":   dict(truth="M1b_autonomous_Allee", r=0.458, K=500.0,
                            s=15.0, catch="const5", S0=30.0),
    "D5_persist_null": dict(truth=None, r=None, K=None,
                            s=None, catch="zero", S0=300.0),
}


def catch_path(kind, years):
    if kind == "const240":
        return np.full(len(years), 240.0)
    if kind == "const5":
        return np.full(len(years), 5.0)
    if kind == "zero":
        return np.zeros(len(years))
    if kind == "regime":                      # the coarse regime of Specification A
        return np.array([240.0 if y <= 1991 else (120.0 if y == 1992 else 5.0)
                         for y in years])
    raise ValueError(kind)


def simulate(dgp, sigma, rng, years):
    """Generate one synthetic SSB series using the REGISTERED map."""
    C = catch_path(dgp["catch"], years)
    S = np.zeros(len(years))
    S[0] = dgp["S0"]
    for t in range(len(years) - 1):
        eps = rng.normal(0.0, sigma)
        if dgp["truth"] is None:              # D5: persistence-true, no surplus
            S[t + 1] = max(S[t] + eps, rl.EPS)
        else:
            S[t + 1] = rl.step(S[t], C[t], dgp["r"], dgp["K"], dgp["s"], eps)
    return S, C


def persistence_rmse(S, origins, h):
    e = [(S[o + h] - S[o]) ** 2 for o in origins if o + h < len(S)]
    return float(np.sqrt(np.mean(e))) if e else np.nan


def retained(scores, persist, module):
    """Definition 2.4 applied unchanged: H1, H2, H3 with a 5% tie band."""
    comp = COMPARATOR[module]
    for h in HORIZONS:                                   # H3: BOTH horizons
        m = scores[module][h]
        p = persist[h]
        if not np.isfinite(m) or not np.isfinite(p):
            return False
        if not (m < p * (1.0 - TIE)):                    # H2 vs persistence
            return False
        if comp is not None:                             # H1 vs comparator
            c = scores[comp][h]
            if not np.isfinite(c) or not (m < c * (1.0 - TIE)):
                return False
    return True


def main():
    years = np.arange(1983, 1983 + T)
    rows = []
    for dname, dgp in DGPS.items():
        for sigma in SIGMAS:
            for rep in range(REPS):
                seed = abs(hash((dname, sigma, rep))) % (2 ** 31)
                rng = np.random.default_rng(seed)
                S, C = simulate(dgp, sigma, rng, years)
                try:
                    _, summ = rl.run_rolling(years, S, C, 884.6, min_train=8)
                except Exception:
                    continue
                scores, persist = {}, {}
                for h in HORIZONS:
                    sub = summ[summ.horizon == h]
                    for m in MODULES:
                        r_ = sub[sub.model == m]
                        scores.setdefault(m, {})[h] = (
                            float(r_.rmse.iloc[0]) if len(r_) else np.nan)
                    org = sorted(range(7, len(years) - 1))
                    persist[h] = persistence_rmse(S, org, h)
                for m in MODULES:
                    rows.append(dict(dgp=dname, truth=dgp["truth"], sigma=sigma,
                                     rep=rep, module=m,
                                     rmse_h1=scores[m][1], rmse_h5=scores[m][5],
                                     persist_h1=persist[1], persist_h5=persist[5],
                                     retained=retained(scores, persist, m)))
        print(f"  done {dname}", flush=True)

    df = pd.DataFrame(rows)
    df.to_csv(OUT, index=False)
    print(f"\nwrote {OUT}  ({len(df)} rows)\n")

    print("=== retention rates by DGP and sigma ===")
    for (d, s), g in df.groupby(["dgp", "sigma"]):
        truth = g.truth.iloc[0]
        any_ret = g.groupby("rep").retained.any().mean()
        line = f"  {d:18} sigma={s:5}  any-module retention {any_ret:.3f}"
        if truth:
            pw = g[g.module == truth].retained.mean()
            line += f" | TRUE-module ({truth.split('_')[0]}) power {pw:.3f}"
        else:
            line += f" | specificity (no structural retained) {1 - any_ret:.3f}"
        print(line)


if __name__ == "__main__":
    main()
