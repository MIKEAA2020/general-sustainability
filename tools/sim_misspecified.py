"""
sim_misspecified.py — Amendment 1 to SPECIFICATION_v4 (locked bd0008f, 01:56:22Z).

Adds two misspecified-truth DGPs (D6, D7) and a second series length (T=71 for
D1, D5). Written after the amendment was locked; no design element chosen here.

Reuses the retention rule, comparators and estimator from sim_retention_power.py,
which import run_ladder unmodified.
"""
import os, sys
import numpy as np, pandas as pd

sys.path.insert(0, "/home/user/tools")
from sim_retention_power import (rl, MODULES, COMPARATOR, HORIZONS, TIE,
                                 catch_path, persistence_rmse, retained, COD)

OUT = os.path.join(COD, "results", "sim_misspecified.csv")
REPS = 200
SIGMAS = (11.8, 33.8)


def gen_D6(rng, T):
    """Time-varying productivity; catch at 55% of instantaneous MSY."""
    S = np.zeros(T); S[0] = 900.0; K = 1032.7; C = np.zeros(T)
    for t in range(T - 1):
        r = 1.935 * np.exp(-0.05 * t) + 0.35
        C[t] = 0.55 * r * K / 4
        S[t + 1] = rl.step(S[t], C[t], r, K, None, rng.normal(0, gen_D6.sigma))
    C[-1] = C[-2]
    return S, C


def gen_D7(rng, T):
    """Deterministic state, Gaussian observation error."""
    X = np.zeros(T); X[0] = 900.0; r, K, Cc = 0.9, 1032.7, 180.0
    for t in range(T - 1):
        X[t + 1] = rl.step(X[t], Cc, r, K, None, 0.0)
    S = np.maximum(X + rng.normal(0, gen_D7.sigma, T), rl.EPS)
    return S, np.full(T, Cc)


def gen_D1(rng, T):
    S = np.zeros(T); S[0] = 900.0; C = np.full(T, 240.0)
    for t in range(T - 1):
        S[t + 1] = rl.step(S[t], C[t], 1.935, 1032.7, None, rng.normal(0, gen_D1.sigma))
    return S, C


def gen_D5(rng, T):
    S = np.zeros(T); S[0] = 300.0
    for t in range(T - 1):
        S[t + 1] = max(S[t] + rng.normal(0, gen_D5.sigma), rl.EPS)
    return S, np.zeros(T)


CELLS = [("D6_timevarying_r", gen_D6, 33, None),
         ("D7_obs_error",     gen_D7, 33, None),
         ("D1_T71",           gen_D1, 71, "M1_autonomous_Schaefer"),
         ("D5_T71",           gen_D5, 71, None)]


def main():
    rows = []
    for name, gen, T, truth in CELLS:
        years = np.arange(1954, 1954 + T) if T == 71 else np.arange(1983, 1983 + T)
        for sigma in SIGMAS:
            gen.sigma = sigma
            for rep in range(REPS):
                rng = np.random.default_rng(abs(hash((name, sigma, rep))) % (2**31))
                S, C = gen(rng, T)
                try:
                    _, summ = rl.run_rolling(years, S, C, 884.6, min_train=8)
                except Exception:
                    continue
                scores, persist = {}, {}
                for h in HORIZONS:
                    sub = summ[summ.horizon == h]
                    for m in MODULES:
                        r_ = sub[sub.model == m]
                        scores.setdefault(m, {})[h] = float(r_.rmse.iloc[0]) if len(r_) else np.nan
                    persist[h] = persistence_rmse(S, sorted(range(7, len(years) - 1)), h)
                for m in MODULES:
                    rows.append(dict(cell=name, truth=truth, T=T, sigma=sigma, rep=rep,
                                     module=m, retained=retained(scores, persist, m)))
        print(f"  done {name}", flush=True)
    df = pd.DataFrame(rows); df.to_csv(OUT, index=False)
    print(f"\nwrote {OUT} ({len(df)} rows)\n")
    for (c, s), g in df.groupby(["cell", "sigma"]):
        any_ret = g.groupby("rep").retained.any().mean()
        tr = g.truth.iloc[0]
        line = f"  {c:18} sigma={s:5}  any-module retention {any_ret:.3f}"
        if isinstance(tr, str):
            line += f" | TRUE-module power {g[g.module == tr].retained.mean():.3f}"
        else:
            line += f" | FALSE-retention {any_ret:.3f}"
        print(line)


if __name__ == "__main__":
    main()
