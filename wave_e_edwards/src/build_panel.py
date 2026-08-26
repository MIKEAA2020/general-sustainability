#!/usr/bin/env python3
"""Build the locked annual panel. No model fitting."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load_j17() -> pd.DataFrame:
    raw = pd.read_csv(DATA / "j17_twdb_6837203_raw.csv")
    raw["date"] = pd.to_datetime(raw["datetime"])
    raw["year"] = raw["date"].dt.year
    raw["H"] = pd.to_numeric(raw["daily_high_water_elevation(ft above msl)"], errors="coerce")
    raw = raw.dropna(subset=["H"])
    g = raw.groupby("year")
    out = pd.DataFrame(
        {
            "n_days": g.size(),
            "H_mean": g["H"].mean(),
            "H_min": g["H"].min(),
            "H_max": g["H"].max(),
            "n_provisional": g["status"].apply(lambda s: int((s == "R").sum())),
        }
    )
    # 240-day floor: 1935 (258) and 1939 (242) are incomplete-coverage
    # means, not gap-filled. Years below 240 are dropped.
    out["H_mean"] = out["H_mean"].where(out["n_days"] >= 240)
    return out.reset_index()


def load_recharge() -> pd.DataFrame:
    rec = pd.read_csv(DATA / "usgs_recharge_1934_2024.txt", sep="\t")
    rec.columns = [c.strip() for c in rec.columns]
    rec["year"] = rec["Year"].astype(int)
    rec["R_total"] = pd.to_numeric(rec["Total"], errors="coerce")
    east = rec[["Basin_5", "Basin_6", "Basin_7", "Basin_9"]].apply(
        pd.to_numeric, errors="coerce"
    )
    rec["R_east"] = east.sum(axis=1)
    return rec[["year", "R_total", "R_east"]]


def load_pumpage() -> pd.DataFrame:
    p = pd.read_csv(DATA / "eaa_table1_discharge_1934_2023.csv")
    p["year"] = p["year"].astype(int)
    return p.rename(columns={"wells_kaf": "P_wells", "springs_kaf": "Q_springs_total"})[
        ["year", "P_wells", "Q_springs_total"]
    ]


def load_comal() -> pd.DataFrame:
    rows = []
    with open(DATA / "usgs_08168710_comal_dv.rdb") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            if line.startswith("agency_cd") or line.startswith("5s"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 5:
                continue
            rows.append(
                {
                    "date": pd.to_datetime(parts[2]),
                    "Q": pd.to_numeric(parts[3], errors="coerce"),
                    "cd": parts[4],
                }
            )
    raw = pd.DataFrame(rows).dropna(subset=["Q"])
    raw["year"] = raw["date"].dt.year
    g = raw.groupby("year")
    out = pd.DataFrame(
        {
            "n_comal": g.size(),
            "Q_comal": g["Q"].mean(),
            "Q_comal_min": g["Q"].min(),
            "n_comal_provisional": g["cd"].apply(lambda s: int(s.str.contains("P").sum())),
            "n_comal_estimated": g["cd"].apply(lambda s: int(s.str.contains("e").sum())),
        }
    )
    out["Q_comal"] = out["Q_comal"].where(out["n_comal"] >= 240)
    return out.reset_index()


CLIMATE_COLS = ("nino34_son", "nino34_ann", "pcp_cd06", "pcp_cd07", "pcp_mean")


def main():
    j17 = load_j17()
    rec = load_recharge()
    pump = load_pumpage()
    comal = load_comal()
    panel = (
        j17.merge(rec, on="year", how="outer")
        .merge(pump, on="year", how="outer")
        .merge(comal, on="year", how="outer")
        .sort_values("year")
    )
    dest = DATA / "annual_panel.csv"
    scratch = DATA / "annual_panel_hrp.csv"
    panel.to_csv(scratch, index=False)

    # F4: never clobber climate columns on the locked panel.
    # If dest already has them and H/R/P/Q match, leave dest bytes alone
    # so the pinned SHA-256 stays valid. Otherwise merge climate back.
    if dest.exists():
        existing = pd.read_csv(dest)
        climate = [c for c in CLIMATE_COLS if c in existing.columns]
        if climate:
            old = existing.set_index("year")
            new = panel.set_index("year")
            hrp_cols = [c for c in new.columns]
            match = True
            common = old.index.intersection(new.index)
            for c in hrp_cols:
                if c not in old.columns:
                    match = False
                    break
                a = pd.to_numeric(old.loc[common, c], errors="coerce")
                b = pd.to_numeric(new.loc[common, c], errors="coerce")
                if not np.allclose(a.fillna(0), b.fillna(0), rtol=0, atol=1e-9, equal_nan=True):
                    # treat NaN==NaN
                    if not ((a.isna() & b.isna()) | (a == b) | (a.sub(b).abs() < 1e-9)).all():
                        match = False
                        break
            if match and set(old.index) == set(new.index):
                print(
                    "F4: H/R/P/Q match committed panel; "
                    f"leaving {dest.name} in place ({len(climate)} climate columns preserved)"
                )
            else:
                for c in hrp_cols:
                    old[c] = new[c]
                old.reset_index().to_csv(dest, index=False)
                print(
                    "F4: rewrote H/R/P/Q on dest and kept climate columns "
                    f"{climate}; pinned hash may change"
                )
        else:
            panel.to_csv(dest, index=False)
            print("F4: dest had no climate columns; wrote H/R/P/Q only")
    else:
        panel.to_csv(dest, index=False)
        print("F4: no dest; wrote H/R/P/Q only (Pass 2 needs climate merge)")

    complete = panel[
        panel["year"].between(1934, 2023)
        & panel["H_mean"].notna()
        & panel["R_total"].notna()
        & panel["P_wells"].notna()
    ]
    print("panel years", int(panel["year"].min()), int(panel["year"].max()))
    print("complete 1934-2023", len(complete), "expected 90")
    print("1934 H_mean", float(panel.loc[panel.year == 1934, "H_mean"].iloc[0]))
    print("1956 H_mean / H_min",
          float(panel.loc[panel.year == 1956, "H_mean"].iloc[0]),
          float(panel.loc[panel.year == 1956, "H_min"].iloc[0]))
    print("1992 H_mean / H_max",
          float(panel.loc[panel.year == 1992, "H_mean"].iloc[0]),
          float(panel.loc[panel.year == 1992, "H_max"].iloc[0]))
    print("1956 R", float(panel.loc[panel.year == 1956, "R_total"].iloc[0]))
    print("1956 P", float(panel.loc[panel.year == 1956, "P_wells"].iloc[0]))
    print("1956 Q_comal", float(panel.loc[panel.year == 1956, "Q_comal"].iloc[0]))
    print("2023 H_mean", float(panel.loc[panel.year == 2023, "H_mean"].iloc[0]))
    # checkpoints vs known J-17 lore
    assert abs(float(panel.loc[panel.year == 1956, "H_min"].iloc[0]) - 612.51) < 0.05
    assert abs(float(panel.loc[panel.year == 1992, "H_max"].iloc[0]) - 703.31) < 0.05
    assert abs(float(panel.loc[panel.year == 1956, "R_total"].iloc[0]) - 43.7) < 0.05
    print("n_days 1935/1939",
          int(panel.loc[panel.year == 1935, "n_days"].iloc[0]),
          int(panel.loc[panel.year == 1939, "n_days"].iloc[0]))
    assert len(complete) == 90
    print("checkpoints OK")


if __name__ == "__main__":
    main()
