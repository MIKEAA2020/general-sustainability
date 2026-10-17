#!/usr/bin/env python3
"""Add causal climate predictors to the annual panel. No model fitting."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
MISSING = -90.0
CLIM = range(1991, 2021)


def load_nino34() -> dict[int, np.ndarray]:
    rows = {}
    for line in (DATA / "psl_nino34_long.data").read_text().splitlines():
        parts = line.split()
        if parts and parts[0].isdigit() and len(parts) >= 13:
            y = int(parts[0])
            rows[y] = np.array([float(x) for x in parts[1:13]])
    return rows


def son_anomaly(rows: dict[int, np.ndarray]) -> pd.DataFrame:
    clim = np.mean([rows[y] for y in CLIM], axis=0)
    recs = []
    for y, v in sorted(rows.items()):
        a = v - clim
        a[v < MISSING] = np.nan
        son = float(np.nanmean(a[8:11]))  # Sep, Oct, Nov
        recs.append({"year": y, "nino34_son": son, "nino34_ann": float(np.nanmean(a))})
    return pd.DataFrame(recs)


def load_precip() -> pd.DataFrame:
    by = defaultdict(dict)
    with open(DATA / "climdiv-pcpndv-v1.0.0-20260806") as f:
        for line in f:
            key = line[:10]
            if not key.startswith("41"):
                continue
            if key[4:6] != "01":
                continue
            div = key[2:4]
            if div not in ("06", "07"):
                continue
            year = int(key[6:10])
            vals = []
            for tok in line[10:].split()[:12]:
                v = float(tok)
                vals.append(np.nan if v < MISSING or v > 80 else v)
            if len(vals) == 12 and np.isfinite(vals).sum() >= 10:
                by[year][div] = float(np.nansum(vals))
    recs = []
    for y in sorted(by):
        d06 = by[y].get("06", np.nan)
        d07 = by[y].get("07", np.nan)
        recs.append(
            {
                "year": y,
                "pcp_cd06": d06,
                "pcp_cd07": d07,
                "pcp_mean": float(np.nanmean([d06, d07])),
            }
        )
    return pd.DataFrame(recs)


def main():
    panel = pd.read_csv(DATA / "annual_panel.csv")
    nino = son_anomaly(load_nino34())
    pcp = load_precip()
    out = panel.merge(nino, on="year", how="left").merge(pcp, on="year", how="left")
    out.to_csv(DATA / "annual_panel.csv", index=False)

    sub = out[out.year.between(1934, 2023)]
    assert sub[["nino34_son", "pcp_mean"]].notna().all().all()
    print("1934-2023 climate complete", len(sub))
    print("1956 pcp_mean", float(sub.loc[sub.year == 1956, "pcp_mean"].iloc[0]))
    print("1992 pcp_mean", float(sub.loc[sub.year == 1992, "pcp_mean"].iloc[0]))
    print("2011 pcp_mean", float(sub.loc[sub.year == 2011, "pcp_mean"].iloc[0]))
    print("1956 SON", float(sub.loc[sub.year == 1956, "nino34_son"].iloc[0]))
    print("1997 SON", float(sub.loc[sub.year == 1997, "nino34_son"].iloc[0]))
    print("2015 SON", float(sub.loc[sub.year == 2015, "nino34_son"].iloc[0]))
    # contemporaneous identity checks, not scores
    print("corr R, pcp same year", float(sub.R_total.corr(sub.pcp_mean)))
    print("corr R, SON same year", float(sub.R_total.corr(sub.nino34_son)))


if __name__ == "__main__":
    main()
