#!/usr/bin/env python3
"""Phase C — reconcile Section 4.3 operating-characteristic cells against fresh CSVs.

For every cell published in Section 4.3 (D1-D7 x sigma), compute the fresh
retention/power/specificity rates, compare with the published numbers, and classify:
  PASS   : fresh rate within binomial-CI-compatible distance of the published value
           (|diff| <= 1.96*sqrt(p(1-p)/n), n = fresh reps)  OR both directions agree on
           the qualitative verdict (power >= .80 vs not; specificity >= .90 vs not).
  CHANGE : quantitative disagreement -> the cell must be replaced (Phase C, N1).
  DISCLOSE : cell that cannot be recomputed -> must be disclosed as unreproduced.

Cell key legend (same as paper's Table 4.3/§4.3):
  D1 .. D7 x sigma {11.8, 33.8}, plus T=71 cells D1_T71, D5_T71.

Outputs: phase_c/results/reconcile_s43_20260913.md (table + verdicts) and .json.
"""
import os, json, math
import numpy as np
import pandas as pd

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(WS, "phase_c", "results")

# published Section 4.3 numbers (frozen record, extracted from paperF1 v15 lines 19/178-184/315/439-446)
PUB = {
    # (cell, sigma): (reported_any_module_retention, reported_true_module_power, specificity_1_minus_fr)
    ("D1", 11.8): dict(any=None, true=0.965, qual="power>=0.80: yes (0.965)"),
    ("D1", 33.8): dict(any=None, true=0.985, qual="power>=0.80: yes (0.985)"),
    ("D2", 11.8): dict(any=None, true=0.710, qual="power 0.710 (high-noise 0.130)"),
    ("D2", 33.8): dict(any=None, true=0.130, qual="power 0.130 (low-noise 0.710)"),
    ("D3", 11.8): dict(any=None, true=0.090, qual="power>=0.80: NO (0.090)"),
    ("D3", 33.8): dict(any=None, true=0.110, qual="power>=0.80: NO (0.110)"),
    ("D4", 11.8): dict(any=None, true=0.005, qual="power>=0.80: NO (0.005)"),
    ("D4", 33.8): dict(any=None, true=0.015, qual="power>=0.80: NO (0.015)"),
    ("D5", 11.8): dict(any=0.015, true=None, qual="specificity 0.985 (1 - 0.015)"),
    ("D5", 33.8): dict(any=0.030, true=None, qual="specificity 0.970 (1 - 0.030)"),
    ("D6", 11.8): dict(any=0.680, true=None, qual="mechanism misattribution 0.680"),
    ("D6", 33.8): dict(any=0.760, true=None, qual="mechanism misattribution 0.760"),
    ("D7", 11.8): dict(any=0.975, true=None, qual="mechanism misattribution 0.975"),
    ("D7", 33.8): dict(any=0.925, true=None, qual="mechanism misattribution 0.925"),
    ("D1_T71", 11.8): dict(any=None, true=None, qual="published: NOT EXECUTED (benchmark only)"),
    ("D1_T71", 33.8): dict(any=None, true=None, qual="published: NOT EXECUTED (benchmark only)"),
    ("D5_T71", 11.8): dict(any=None, true=None, qual="published: NOT EXECUTED (benchmark only)"),
    ("D5_T71", 33.8): dict(any=None, true=None, qual="published: NOT EXECUTED (benchmark only)"),
}


def fresh_power_df():
    path = os.path.join(R, "sim_retention_power_20260913.csv")
    if not os.path.exists(path):
        return {}
    df = pd.read_csv(path)
    out = {}
    for (d, s), g in df.groupby(["dgp", "sigma"]):
        truth = g.truth.iloc[0]
        rec = dict(any=float(g.groupby("rep").retained.any().mean()), n=int(g.rep.nunique()),
                   true=float(g[g.module == truth].retained.mean()) if isinstance(truth, str) else None)
        out[(d.split("_")[0], float(s))] = rec
    return out


def fresh_miss_df():
    path = os.path.join(R, "sim_misspecified_20260913.csv")
    if not os.path.exists(path):
        return {}
    df = pd.read_csv(path)
    out = {}
    for (c, s), g in df.groupby(["cell", "sigma"]):
        truth = g.truth.iloc[0]
        rec = dict(any=float(g.groupby("rep").retained.any().mean()), n=int(g.rep.nunique()),
                   true=float(g[g.module == truth].retained.mean()) if isinstance(truth, str) else None)
        out[(c.split("_")[0] + ("_T71" if "_T71" in c else ""), float(s))] = rec
    return out


def classify(pub, fresh, cell, sigma):
    if fresh is None:
        return "DISCLOSE", f"not recomputable in this run"
    if pub["qual"].startswith("published: NOT EXECUTED"):
        note = (f"first execution: any-module retention {fresh['any']:.3f}"
                + (f", true-module power {fresh['true']:.3f}" if fresh["true"] is not None else "")
                + f" (n={fresh['n']})")
        return "NEW", note
    n = fresh["n"]
    se = math.sqrt(pub["true"] * (1 - pub["true"]) / n) if pub["true"] is not None else None
    verdicts = []
    if pub["true"] is not None and fresh["true"] is not None:
        p, f = pub["true"], fresh["true"]
        ok = abs(f - p) <= 1.96 * se
        verdicts.append(f"true-module power: pub {p:.3f} vs fresh {f:.3f} (n={n}, CI95 halfwidth {1.96 * se:.3f}) -> {'PASS' if ok else 'FAIL'}")
        return ("PASS" if ok else "CHANGE"), "; ".join(verdicts)
    if pub["any"] is not None and fresh["any"] is not None:
        p, f = pub["any"], fresh["any"]
        se = math.sqrt(p * (1 - p) / n)
        ok = abs(f - p) <= 1.96 * se
        verdicts.append(f"any-module retention: pub {p:.3f} vs fresh {f:.3f} (n={n}, CI95 halfwidth {1.96 * se:.3f}) -> {'PASS' if ok else 'FAIL'}")
        return ("PASS" if ok else "CHANGE"), "; ".join(verdicts)
    return "REPORT", f"fresh {fresh} (no published point number; qualitative only)"


def main():
    power, miss = fresh_power_df(), fresh_miss_df()
    rows, missing = [], []
    for (cell, sigma), pub in PUB.items():
        fresh = power.get((cell, sigma)) or miss.get((cell, sigma))
        cls, note = classify(pub, fresh, cell, sigma)
        rows.append(dict(cell=cell, sigma=sigma, published=pub["qual"],
                         fresh_n=fresh["n"] if fresh else None,
                         fresh_any=None if not fresh else round(fresh["any"], 3),
                         fresh_true=None if (not fresh or fresh["true"] is None) else round(fresh["true"], 3),
                         verdict=cls, note=note))
        if fresh is None:
            missing.append((cell, sigma))
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(R, "reconcile_s43_20260913.csv"), index=False)
    with open(os.path.join(R, "reconcile_s43_20260913.json"), "w") as f:
        json.dump(rows, f, indent=2)
    print(df.to_string(index=False))
    print(f"\nverdicts: PASS {sum(r['verdict'] == 'PASS' for r in rows)}, "
          f"CHANGE {sum(r['verdict'] == 'CHANGE' for r in rows)}, "
          f"DISCLOSE/REPORT {sum(r['verdict'] in ('DISCLOSE', 'REPORT') for r in rows)}")
    print("missing:", missing)


if __name__ == "__main__":
    main()
