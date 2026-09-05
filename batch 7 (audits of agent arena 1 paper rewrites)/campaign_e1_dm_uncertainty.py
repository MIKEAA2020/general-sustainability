"""
campaign_e1_dm_uncertainty.py
------------------------------
Diebold-Mariano test + moving-block (Kunsch) bootstrap on the rolling-origin
SSB forecast margins reported in paperE1 v10/v11 (audit item A8 / R3),
following the registered E3 template campaign_e3_dm_uncertainty.py.

Inputs  : wave_e_cod/results/rolling_forecasts.csv    (Specification A, per-origin obs/pred)
          wave_e_cod/results/xte_rolling_forecasts.csv (Specification B, per-origin obs/pred)
          wave_e_cod/data/ncam_2016_table_a2.csv       (registered series A)
          wave_e_cod/data/xtencam_table17_ssb.csv      (registered series B)
Output  : results/e1_dm_uncertainty.csv

Deterministic (seed 0, 20,000 replications). The naive persistence baseline is
not archived per-origin, so its per-origin losses are recomputed from the
registered series on the *identical* origin sets of the archived structural
per-origin file (the origin-matched control the paper already reports); the
recomputed persistence RMSEs are asserted against the paper's frozen values
(98/265 kt on Specification A; 84/300 kt on the Specification B matched
origins) so a mismatch fails loudly.

Post-freeze layer: no frozen verdict, score, or table value is changed.
"""
import os, numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "wave_e_cod"))
ROLL_A = os.path.join(ROOT, "results", "rolling_forecasts.csv")
ROLL_B = os.path.join(ROOT, "results", "xte_rolling_forecasts.csv")
SER_A = os.path.join(ROOT, "data", "ncam_2016_table_a2.csv")
SER_B = os.path.join(ROOT, "data", "xtencam_table17_ssb.csv")
OUT = os.path.join(HERE, "results", "e1_dm_uncertainty.csv")
NB = 20000
SEED = 0
EPS = 1e-3  # the numerical floor of the registered trajectory code (run_ladder.step)

MODELS = ["M1_autonomous_Schaefer", "M1b_autonomous_Allee", "M2_stockflow_regimeC",
          "M3_AR_residual", "M4_delayed_info"]
# H2 margins (vs persistence), H1 declared comparators for the non-nested rungs
# (M2 vs M1; M4 vs M3), and the alternative comparator disclosure (M2 vs M1b).
PAIRS = [(m, "naive_persist") for m in MODELS] + \
        [("M2_stockflow_regimeC", "M1_autonomous_Schaefer"),
         ("M4_delayed_info", "M3_AR_residual"),
         ("M2_stockflow_regimeC", "M1b_autonomous_Allee")]


def dm_hac(lossdiff, horizon):
    """DM statistic with unweighted HAC truncation at lag h-1 (E3 template)."""
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
    """Kunsch moving-block bootstrap of the RMSE of a squared-loss series."""
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


def build(spec, roll_csv, series_csv, expected_persist):
    df = pd.read_csv(roll_csv)
    ser = pd.read_csv(series_csv)[["year", "ssb_kt"]].set_index("year")["ssb_kt"]
    rows = []
    for h in (1, 5):
        sub = df[df.horizon == h]
        origins = sorted(sub.origin.unique())
        # origin-matched persistence losses, recomputed from the registered series
        per = []
        for o in origins:
            y = float(ser.loc[o + h])
            p = float(ser.loc[o])
            assert abs(y - float(sub[sub.origin == o].obs.iloc[0])) < 1e-9, \
                f"obs mismatch at origin {o}, horizon {h} ({spec})"
            per.append((p - y) ** 2)
        persist_loss = pd.Series(per, index=origins)
        rmse_persist = float(np.sqrt(persist_loss.mean()))
        if abs(rmse_persist - expected_persist[h]) > 0.5:
            raise AssertionError(
                f"{spec} h={h}: recomputed origin-matched persistence RMSE {rmse_persist:.2f} "
                f"does not match the paper's frozen value {expected_persist[h]}")
        losses = {"naive_persist": persist_loss}
        for m in MODELS:
            mm = sub[sub.model == m].sort_values("origin")
            assert list(mm.origin) == origins, f"origin set mismatch for {m} ({spec}, h={h})"
            losses[m] = pd.Series(mm.sqerr.values, index=origins)
        blk = max(h, 3)
        for a, b in PAIRS:
            A, B = losses[a], losses[b]
            ld = A - B
            dm, _ = dm_hac(ld, h)
            bA = block_bootstrap_rmse(A, blk)
            bB = block_bootstrap_rmse(B, blk)
            gap = bA - bB
            p = 2 * min(float((gap <= 0).mean()), float((gap >= 0).mean()))
            lo, hi = np.percentile(gap, [2.5, 97.5])
            rows.append(dict(spec=spec, horizon=h, A=a.replace("_", " "), B=b.replace("_", " "),
                             n=int(len(A)), RMSEa=float(np.sqrt(A.mean())),
                             RMSEb=float(np.sqrt(B.mean())),
                             gap_kt=float(np.sqrt(A.mean()) - np.sqrt(B.mean())),
                             DM_z=dm, block=blk, ci95_lo=float(lo), ci95_hi=float(hi),
                             p_bootstrap=float(p)))
    return rows


def main():
    rows = []
    rows += build("A", ROLL_A, SER_A, {1: 98.0, 5: 265.0})
    rows += build("B", ROLL_B, SER_B, {1: 84.0, 5: 300.0})
    R = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    R.to_csv(OUT, index=False)
    print(R.round(3).to_string())
    print("wrote", OUT)


if __name__ == "__main__":
    main()
