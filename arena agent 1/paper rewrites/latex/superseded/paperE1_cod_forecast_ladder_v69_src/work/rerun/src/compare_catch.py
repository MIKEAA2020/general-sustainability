#!/usr/bin/env python3
"""Schijns 2021 vs DFO 2025 Table 1 — overlap audit. No interpolation."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
s = pd.read_csv(ROOT / "data" / "catch_schijns_2021.csv")
d = pd.read_csv(ROOT / "data" / "dfo_2025_table1_landings_partial.csv")
m = s.merge(d, on="year", suffixes=("_schijns", "_dfo"))
m["diff_t"] = m["catch_t_schijns"] - m["catch_t_dfo"]
m["rel"] = m["diff_t"] / m["catch_t_dfo"]
out = ROOT / "results" / "catch_overlap_audit.csv"
m.to_csv(out, index=False)
print(m[["year", "catch_t_schijns", "catch_t_dfo", "diff_t"]].to_string(index=False))
print("max |diff| t =", m["diff_t"].abs().max())
print("n years", len(m), "exact matches", int((m["diff_t"] == 0).sum()))
