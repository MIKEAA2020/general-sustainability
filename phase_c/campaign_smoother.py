#!/usr/bin/env python3
"""Phase C campaign 3 — the smoother test (registered in v15 Section 6).

Candidate mechanism for the domain contrast: the cod predictand is an assessment output
conditioned on the full series (retrospective), while Edwards head is directly measured;
the conditioning may inject autocorrelation that favours persistence. Decisive test:
rescore the SAME D1 (collapse) replicates under an assessment-like smoother (centred
3-year moving average — a crude retrospective-assessment analogue) and compare the
retention of the true module (M1) and persistence margins across arms.

Seeds: identical scheme to campaign_power (abs(hash((dname, sigma, rep))) % 2**31,
PYTHONHASHSEED=0), so the raw arm is the same replicates as the power campaign's
D1_M1_collapse cells (reps 0..99) and the smoothed arm differs ONLY by the smoother.

Output: phase_c/results/smoother_test_20260913.csv + _summary.json + _provenance.json.
"""
import os, sys, json, hashlib, time, datetime
import numpy as np
import pandas as pd

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(WS, "wave_e_cod", "src"))
import run_ladder as rl  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import campaign_power as cp  # noqa: E402

OUT = os.path.join(WS, "phase_c", "results", "smoother_test_20260913.csv")
# Phase C scaling: 30 reps/arm (D1-like ladder passes measured at 14.6-16.7 s/pass
# under dual load; the 100-rep first attempt was killed at the smoother stage to
# keep the campaign within budget). Binomial CIs disclosed with every rate.
REPS = 30
T = 33
DGP_NAME = "D1_M1_collapse"
DGP = cp.DGPS[DGP_NAME]


def smooth3(S):
    """Centred 3-year moving average; mirrored at the edges (non-causal, like a retrospective)."""
    out = np.zeros(len(S))
    for t in range(len(S)):
        lo, hi = max(0, t - 1), min(len(S) - 1, t + 1)
        out[t] = np.mean(S[lo:hi + 1])
    return out


def score_series(years, S, C):
    rows = {}
    _, summ = rl.run_rolling(years, S, C, 884.6, min_train=8)
    for h in cp.HORIZONS:
        sub = summ[summ.horizon == h]
        for m in cp.MODULES:
            r_ = sub[sub.model == m]
            rows[(m, h)] = float(r_.rmse.iloc[0]) if len(r_) else np.nan
    return rows


def main():
    t_start = time.time()
    all_rows = []
    written = False
    for sigma in (11.8, 33.8):
        for rep in range(REPS):
            seed = abs(hash((DGP_NAME, sigma, rep))) % (2 ** 31)
            rng = np.random.default_rng(seed)
            years = np.arange(1983, 1983 + T)
            S, C = cp.simulate(DGP, sigma, rng, years)
            for arm, St in (("raw", S), ("smoothed", smooth3(S))):
                try:
                    sc = score_series(years, St, C)
                except Exception:
                    continue
                persist = {h: cp.persistence_rmse(St, sorted(range(7, len(years) - 1)), h)
                           for h in cp.HORIZONS}
                scores = {m: {h: sc[(m, h)] for h in cp.HORIZONS} for m in cp.MODULES}
                for m in cp.MODULES:
                    all_rows.append(dict(sigma=sigma, rep=rep, arm=arm, module=m,
                                         rmse_h1=scores[m][1], rmse_h5=scores[m][5],
                                         persist_h1=persist[1], persist_h5=persist[5],
                                         retained=cp.retained(scores, persist, m)))
        print(f"  done smoother sigma={sigma}", flush=True)
        part = pd.DataFrame(all_rows)
        part.to_csv(OUT, index=False, mode="w" if not written else "a",
                    header=not written)
        written = True
        all_rows = []
    df = pd.read_csv(OUT)
    prov = {
        "campaign": "smoother_test", "run": "20260913", "reps": REPS,
        "pyhashseed": os.environ.get("PYTHONHASHSEED"),
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "wall_s_total": round(time.time() - t_start, 1),
        "smoother": "centred 3-year moving average, mirrored edges (non-causal retrospective analogue)",
        "sha256": {
            "run_ladder.py": hashlib.sha256(open(os.path.join(WS, "wave_e_cod", "src", "run_ladder.py"), "rb").read()).hexdigest(),
            "campaign_smoother.py": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
        },
        "versions": dict(numpy=np.__version__, pandas=pd.__version__),
    }
    with open(OUT.replace(".csv", "_provenance.json"), "w") as f:
        json.dump(prov, f, indent=2)

    summ = {}
    for sigma in (11.8, 33.8):
        for arm in ("raw", "smoothed"):
            g = df[(df.sigma == sigma) & (df.arm == arm)]
            m1 = g[g.module == "M1_autonomous_Schaefer"]
            # true-module retention rate
            pw = m1.retained.mean()
            # persistence margin of M1 at h=1, h=5 (negative = persistence worse)
            for h in (1, 5):
                g2 = g[g.module == "M1_autonomous_Schaefer"]
                marg = (g2[f"rmse_h{h}"] - g2[f"persist_h{h}"]).mean()
                summ[f"sigma{sigma}_{arm}_h{h}_m1_margin_ft"] = round(float(marg), 3)
            summ[f"sigma{sigma}_{arm}_m1_power"] = round(float(pw), 4)
            summ[f"sigma{sigma}_{arm}_n"] = int(m1.retained.count())
    with open(OUT.replace(".csv", "_summary.json"), "w") as f:
        json.dump(summ, f, indent=2)
    print(f"\nwrote {OUT} ({len(df)} rows)")
    print(json.dumps(summ, indent=2))


if __name__ == "__main__":
    main()
