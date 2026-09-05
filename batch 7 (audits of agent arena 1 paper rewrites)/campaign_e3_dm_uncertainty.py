"""
campaign_e3_dm_uncertainty.py
------------------------------
Diebold-Mariano test + moving-block (Kunsch) bootstrap on the rolling-origin
J-17 head forecast margins reported in paperE3 v11, Section 5.7.

Inputs  : results/rolling_forecasts.csv  (per-origin obs/pred)
Output  : results/e3_dm_uncertainty.csv

Deterministic. Uses the registered rolling forecast file (archived); only the
margin test statistics and block-bootstrap intervals are computed here.
"""
import os, numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROLLING = os.path.join(HERE, "results", "rolling_forecasts.csv")
OUT = os.path.join(HERE, "results", "e3_dm_uncertainty.csv")
NB = 20000
SEED = 0


def dm_hac(lossdiff, horizon):
    d = lossdiff.values
    n = len(d)
    lag = max(horizon - 1, 0)
    x = d - d.mean()
    g0 = float((x @ x) / n)
    gamma = np.array([float((x[:-k] @ x[k:]) / n) for k in range(1, lag + 1)]) if lag > 0 else np.array([])
    s2 = g0 + 2 * gamma.sum()
    dm = d.mean() / np.sqrt(s2 / n)
    return float(dm), float(s2 / n)


def block_bootstrap_rmse(series, block, nboot=NB, seed=SEED):
    rng = np.random.default_rng(seed)
    s = series.values
    n = len(s)
    nb = n // block
    starts = np.arange(n - block + 1)
    out = np.empty(nboot)
    for i in range(nboot):
        idx = rng.choice(starts, size=nb, replace=True)
        samp = np.concatenate([s[j:j + block] for j in idx])
        out[i] = np.sqrt(np.mean(samp))
    return out


def main():
    df = pd.read_csv(ROLLING)
    df["err"] = df.obs - df.pred
    df["loss"] = df.err ** 2
    rows = []
    pairs = [("M1", "naive_persist"), ("naive_mean", "naive_persist"), ("M2m", "naive_persist"),
             ("M2", "naive_persist"), ("M2_oracle", "naive_persist")]
    for h in (1, 5):
        for a, b in pairs:
            A = df[(df.horizon == h) & (df.model == a)].sort_values("origin").reset_index(drop=True)
            B = df[(df.horizon == h) & (df.model == b)].sort_values("origin").reset_index(drop=True)
            if len(A) != len(B):
                continue
            ld = A.loss - B.loss
            dm, varh = dm_hac(ld, h)
            rmse_a = float(np.sqrt(A.loss.mean()))
            rmse_b = float(np.sqrt(B.loss.mean()))
            blk = max(h, 1)
            bA = block_bootstrap_rmse(A.loss, blk)
            bB = block_bootstrap_rmse(B.loss, blk)
            gap = bA - bB
            p = 2 * min(float((gap <= 0).mean()), float((gap >= 0).mean()))
            lo, hi = np.percentile(gap, [2.5, 97.5])
            rows.append(dict(horizon=h, A=a, B=b, n=int(len(A)),
                             RMSEa=rmse_a, RMSEb=rmse_b, gap_ft=rmse_a - rmse_b,
                             DM_z=dm, block=blk, ci95_lo=float(lo), ci95_hi=float(hi),
                             p_bootstrap=float(p)))
    R = pd.DataFrame(rows)
    R.to_csv(OUT, index=False)
    print(R.round(3).to_string())
    print("wrote", OUT)


if __name__ == "__main__":
    main()
