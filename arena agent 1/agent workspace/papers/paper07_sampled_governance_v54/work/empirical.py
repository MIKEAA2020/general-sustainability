#!/usr/bin/env python3
"""Rebuild the 42-stock target-band table and BH-adjusted p-values."""
from __future__ import annotations
import csv, json, sys
from pathlib import Path
import numpy as np
from scipy.signal import lombscargle

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "p7_empirical"
sys.path.insert(0, str(SRC))
from ram_crosssection import spectrum, band_power, BANDS, regime  # noqa: E402

DATA = SRC / "ram_target_stocks.csv"
OUT = ROOT / "work" / "empirical_results.csv"
SUMMARY = ROOT / "work" / "empirical_summary.json"
NSIM, SEED = 200, 7


def load_data():
    rows = {}
    with DATA.open(newline="", encoding="utf-8") as f:
        for d in csv.DictReader(f):
            if d["SSB"] in ("", "NA"):
                continue
            rows.setdefault(d["stockid"], []).append((int(d["tsyear"]), float(d["SSB"])))
    return {k: sorted(v) for k, v in rows.items()}


def bh_qvalues(pvals):
    p = np.asarray(pvals, dtype=float)
    m = len(p)
    order = np.argsort(p, kind="mergesort")
    qs = np.empty(m, dtype=float)
    running = 1.0
    for j in range(m - 1, -1, -1):
        i = order[j]
        running = min(running, p[i] * m / (j + 1))
        qs[i] = min(1.0, running)
    return qs


def run():
    data = load_data()
    rows = []
    for sid in sorted(data):
        pair = data[sid]
        years = np.asarray([x[0] for x in pair], dtype=int)
        ssb = np.asarray([x[1] for x in pair], dtype=float)
        if len(ssb) < 20:
            continue
        freq, P, phi = spectrum(years, ssb)
        t = years - years[0]
        rng = np.random.default_rng(SEED)
        sims = np.zeros((NSIM, 2), dtype=float)
        for s in range(NSIM):
            e = rng.standard_normal(len(ssb))
            x = np.zeros(len(ssb)); x[0] = e[0]
            for i in range(1, len(ssb)):
                x[i] = phi * x[i - 1] + e[i]
            x = x / np.std(x)
            b1, b0 = np.polyfit(t, x, 1)
            det = x - (b0 + b1 * t)
            Ps = lombscargle(t, det, 2 * np.pi * freq)
            Ps = Ps / Ps.sum()
            for bi, (_, lo, hi) in enumerate(BANDS[:2]):
                mask = (freq > 1 / hi) & (freq <= 1 / lo)
                sims[s, bi] = Ps[mask].sum()
        band_powers = [band_power(freq, P, lo, hi) for _, lo, hi in BANDS]
        pvals = [float((np.sum(sims[:, bi] >= band_powers[bi]) + 1) / (NSIM + 1))
                 for bi in range(2)]
        rows.append({"stockid": sid, "n": int(len(ssb)),
                     "cv": float(np.std(ssb) / np.mean(ssb)),
                     "review_proxy": regime(sid),
                     "power_A": band_powers[0], "power_B": band_powers[1],
                     "power_C": band_powers[2], "power_D": band_powers[3],
                     "p_A": pvals[0], "p_B": pvals[1]})
    flat = [(i, band) for i, row in enumerate(rows) for band in ("A", "B")]
    pvals = [rows[i][f"p_{b}"] for i, b in flat]
    qvals = bh_qvalues(pvals)
    for q, (i, band) in zip(qvals, flat):
        rows[i][f"q_{band}"] = float(q)
    rejected = [(r["stockid"], b) for r in rows for b in ("A", "B") if r[f"q_{b}"] <= 0.05]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fields = ["stockid", "n", "cv", "review_proxy", "power_A", "p_A", "q_A",
              "power_B", "p_B", "q_B", "power_C", "power_D"]
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for row in rows:
            w.writerow({k: row[k] for k in fields})
    summary = {"input_stockids": len(data), "eligible_stocks": len(rows),
               "eligible_rule": "at least 20 nonmissing annual SSB values",
               "target_band_tests": len(flat), "alpha": 0.05,
               "bh_rejections": len(rejected), "rejected": rejected,
               "minimum_empirical_p": min(pvals),
               "minimum_p_cell": min(((r["stockid"], b, r[f"p_{b}"]) for r in rows for b in ("A", "B")), key=lambda x:x[2]),
               "PANCHNCHSP_B": next({"power": r["power_B"], "p": r["p_B"], "q": r["q_B"]} for r in rows if r["stockid"] == "PANCHNCHSP"),
               "simulations_per_series": NSIM, "seed": SEED,
               "periodogram": "Lomb-Scargle, 1500 frequencies, linear trend removed, unit-total-power normalization",
               "outputs": str(OUT)}
    SUMMARY.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print(f"wrote {OUT}")
    return rows, summary

if __name__ == "__main__":
    run()
