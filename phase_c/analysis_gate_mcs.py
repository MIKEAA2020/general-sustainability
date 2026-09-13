#!/usr/bin/env python3
"""Phase C analysis 1 — uncertainty-aware gate, hybrid rows, MCS/encompassing.

Consumes phase_c/results/sim_origins_20260913.csv (per-origin sqerr, 5 modules +
naive_persist). For every replicate computes three retention rules and one
encompassing statistic:

  band        : the frozen Definition 2.4 rule (5% tie band, H1/H2/H3)   [reference]
  uncertainty : margin (RMSE_a - RMSE_b) must have a 95% moving-block-bootstrap CI
                (block 4, 999 resamples, seed fixed) fully below zero, both horizons,
                both gates (vs persistence, vs declared comparator).
  hybrid      : band AND uncertainty.
  MCS         : Hansen-Lunde-Nason model confidence set (alpha=0.10, block bootstrap,
                499 resamples) over the 6 candidates; membership of the true module /
                exclusion of persistence / size of the surviving set.

Output: phase_c/results/gate_hybrid_mcs_20260913.json (rates per DGP x sigma x rule)
        phase_c/results/gate_hybrid_mcs_20260913.csv (per-replicate detail)
"""
import os, json, datetime
import numpy as np
import pandas as pd

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(WS, "phase_c", "results")
SRC = os.path.join(R, "sim_origins_20260913.csv")

MODULES = ["M1_autonomous_Schaefer", "M1b_autonomous_Allee",
           "M2_stockflow_regimeC", "M3_AR_residual", "M4_delayed_info"]
COMPARATOR = {"M1_autonomous_Schaefer": None,
              "M1b_autonomous_Allee": "M1_autonomous_Schaefer",
              "M2_stockflow_regimeC": "M1_autonomous_Schaefer",
              "M3_AR_residual": "M2_stockflow_regimeC",
              "M4_delayed_info": "M3_AR_residual"}
TRUTH = {"D1_M1_collapse": "M1_autonomous_Schaefer",
         "D2_M1_recovery": "M1_autonomous_Schaefer",
         "D3_M2_stockflow": "M2_stockflow_regimeC",
         "D4_M1b_depens": "M1b_autonomous_Allee",
         "D5_persist_null": None}
HORIZONS = (1, 5)
SEED = 20260913
NBOOT_MARGIN = 999
NBOOT_MCS = 499
BLOCK = 4


def block_bootstrap_margin(sq_a, sq_b, nboot=NBOOT_MARGIN, block=BLOCK, seed=SEED):
    """Moving-block bootstrap of RMSE_a - RMSE_b over origins. Returns CI and mean."""
    rng = np.random.default_rng(seed)
    n = len(sq_a)
    nblocks = int(np.ceil(n / block))
    margins = np.empty(nboot)
    for b in range(nboot):
        starts = rng.integers(0, n - block + 1, size=nblocks)
        idx = np.concatenate([np.arange(s, s + block) for s in starts])[:n]
        margins[b] = np.sqrt(sq_a[idx].mean()) - np.sqrt(sq_b[idx].mean())
    lo, hi = np.percentile(margins, [2.5, 97.5])
    return lo, hi


def margin_matrix(sqerrs_by_model, models, persist_name="naive_persist"):
    """(models x persist) and (models x comparator) per-horizon margin CIs."""
    pass


def mcs(sqerrs, nboot=NBOOT_MCS, block=BLOCK, seed=SEED, alpha=0.10):
    """Hansen-Lunde-Nason MCS (range statistic, block bootstrap) over candidate losses.

    sqerrs: (n_origins, n_candidates). Returns the surviving set (indices) and the
    elimination order with bootstrap p-values.
    """
    rng = np.random.default_rng(seed)
    n, M = sqerrs.shape
    dbar = sqerrs.mean(axis=0)
    surviving = list(range(M))
    pvals = [1.0] * M
    order = []

    def t_stat(idx_subset):
        # max pairwise |t| over subset; variance via block bootstrap of loss differentials
        m = len(idx_subset)
        ts = np.zeros((m, m))
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                d = sqerrs[:, idx_subset[i]] - sqerrs[:, idx_subset[j]]
                # bootstrap variance of dbar
                nblocks = int(np.ceil(n / block))
                vals = np.empty(nboot)
                for b in range(nboot):
                    starts = rng.integers(0, n - block + 1, size=nblocks)
                    idx = np.concatenate([np.arange(s, s + block) for s in starts])[:n]
                    vals[b] = d[idx].mean()
                sd = vals.std(ddof=1)
                ts[i, j] = (d.mean() - 0.0) / (sd / np.sqrt(n)) if sd > 1e-12 else np.inf
        return ts

    while len(surviving) > 1:
        ts = t_stat(surviving)
        tmax = np.max(np.abs(ts))
        # bootstrap null of T_max (centered)
        nblocks = int(np.ceil(n / block))
        dist = np.empty(nboot)
        for b in range(nboot):
            starts = rng.integers(0, n - block + 1, size=nblocks)
            idx = np.concatenate([np.arange(s, s + block) for s in starts])[:n]
            centered = sqerrs[idx] - sqerrs[idx].mean(axis=0)
            dbar_b = centered.mean(axis=0)
            mm = len(surviving)
            tv = np.zeros((mm, mm))
            for i in range(mm):
                for j in range(mm):
                    if i == j:
                        continue
                    d = sqerrs[idx, surviving[i]] - sqerrs[idx, surviving[j]]
                    sd = d.std(ddof=1)
                    tv[i, j] = (dbar_b[i] - dbar_b[j]) / (sd / np.sqrt(n)) if sd > 1e-12 else 0.0
            dist[b] = np.max(np.abs(tv))
        crit = np.quantile(dist, 1.0 - alpha)
        if tmax <= crit:
            break
        # eliminate the model with the largest row-sum of |t|
        rowsum = np.abs(ts).sum(axis=1)
        worst = int(np.argmax(rowsum))
        pvals[surviving[worst]] = float(np.mean(dist >= tmax))
        order.append(surviving[worst])
        del surviving[worst]
    return surviving, order, pvals


def main():
    df = pd.read_csv(SRC)
    records = []
    for (dname, sigma, rep), g in df.groupby(["dgp", "sigma", "rep"]):
        truth = TRUTH[dname]
        rec = dict(dgp=dname, sigma=float(sigma), rep=int(rep))
        # per-horizon per-model sqerr arrays aligned on origins
        for h in HORIZONS:
            sub = g[g.horizon == h]
            origins = sorted(sub.origin.unique())
            mat = {}
            for m in MODULES + ["naive_persist"]:
                rows = sub[sub.model == m]
                if len(rows) != len(origins):
                    mat[m] = None
                else:
                    s = rows.sort_values("origin").sqerr.to_numpy()
                    mat[m] = s
            persist = mat["naive_persist"]
            band = {}
            unc = {}
            for m in MODULES:
                sq = mat[m]
                if sq is None or persist is None:
                    band[m], unc[m] = False, False
                    continue
                rmse_m, rmse_p = np.sqrt(sq.mean()), np.sqrt(persist.mean())
                band_m = rmse_m < rmse_p * 0.95
                lo, hi = block_bootstrap_margin(sq, persist)
                unc_m = hi < 0.0
                comp = COMPARATOR[m]
                if comp is not None and mat[comp] is not None:
                    sqc = mat[comp]
                    band_m = band_m and (rmse_m < np.sqrt(sqc.mean()) * 0.95)
                    loc, hic = block_bootstrap_margin(sq, sqc)
                    unc_m = unc_m and (hic < 0.0)
                band[m], unc[m] = bool(band_m), bool(unc_m)
            rec[f"band_retained_h{h}"] = band
            rec[f"unc_retained_h{h}"] = unc
            rec[f"m1_margin_ci_h{h}"] = [float(x) for x in
                                         block_bootstrap_margin(mat["M1_autonomous_Schaefer"], persist)]
        # rule-level retention: both horizons for band; both for uncertainty; hybrid
        band_ret = {m: rec["band_retained_h1"][m] and rec["band_retained_h5"][m] for m in MODULES}
        unc_ret = {m: rec["unc_retained_h1"][m] and rec["unc_retained_h5"][m] for m in MODULES}
        rec["band_retained"] = band_ret
        rec["unc_retained"] = unc_ret
        rec["hybrid_retained"] = {m: band_ret[m] and unc_ret[m] for m in MODULES}
        # MCS at h=1 over 6 candidates (loss = sqerr)
        sub1 = g[g.horizon == 1]
        origins1 = sorted(sub1.origin.unique())
        cand = MODULES + ["naive_persist"]
        loss = np.zeros((len(origins1), len(cand)))
        for j, m in enumerate(cand):
            rows = sub1[sub1.model == m].sort_values("origin").sqerr.to_numpy()
            loss[:, j] = rows if len(rows) == len(origins1) else np.nan
        ok = ~np.isnan(loss).any(axis=0)
        if ok.sum() >= 2:
            surv, order, pvals = mcs(loss[:, ok])
            names = [cand[i] for i in np.where(ok)[0]]
            rec["mcs_h1_survivors"] = sorted(names[i] for i in surv)
            rec["mcs_h1_eliminated"] = [names[i] for i in order]
            rec["mcs_h1_true_in_set"] = bool(truth in rec["mcs_h1_survivors"]) if truth else None
            rec["mcs_h1_persist_in_set"] = "naive_persist" in rec["mcs_h1_survivors"]
            rec["mcs_h1_size"] = len(surv)
        else:
            rec["mcs_h1_survivors"] = None
        records.append(rec)
    out_df = pd.DataFrame(records)
    out_df.to_csv(os.path.join(R, "gate_hybrid_mcs_20260913.csv"), index=False)

    summary = {}
    for dname in TRUTH:
        truth = TRUTH[dname]
        for sigma in (11.8, 33.8):
            g = out_df[(out_df.dgp == dname) & (out_df.sigma == sigma)]
            if not len(g):
                continue
            row = {"n": int(len(g)),
                   "band_any": float(g.band_retained.apply(lambda d: any(d.values())).mean())}
            if truth:
                row["band_true_power"] = float(g.band_retained.apply(lambda d: d[truth]).mean())
                row["unc_true_power"] = float(g.unc_retained.apply(lambda d: d[truth]).mean())
                row["hybrid_true_power"] = float(g.hybrid_retained.apply(lambda d: d[truth]).mean())
                row["mcs_true_in_set"] = float(g.mcs_h1_true_in_set.mean())
            else:
                row["band_specificity"] = float(1 - g.band_retained.apply(lambda d: any(d.values())).mean())
                row["unc_specificity"] = float(1 - g.unc_retained.apply(lambda d: any(d.values())).mean())
                row["hybrid_specificity"] = float(1 - g.hybrid_retained.apply(lambda d: any(d.values())).mean())
                row["mcs_persist_only"] = float((g.mcs_h1_survivors.apply(
                    lambda s: s == ["naive_persist"] if isinstance(s, list) else False)).mean())
            summary[f"{dname}_s{sigma}"] = row
    out = {"run": "20260913", "nboot_margin": NBOOT_MARGIN, "nboot_mcs": NBOOT_MCS,
           "block": BLOCK, "seed": SEED,
           "written_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "summary": summary}
    with open(os.path.join(R, "gate_hybrid_mcs_20260913.json"), "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(summary, indent=2))
    print(f"\nwrote gate_hybrid_mcs_20260913.{{csv,json}} ({len(out_df)} replicate records)")


if __name__ == "__main__":
    main()
