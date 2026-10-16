#!/usr/bin/env python3
"""Reproduce the MCS 2026 phosphate arithmetic snapshots and crossover example."""
from __future__ import annotations
import csv
import math
from pathlib import Path

SOURCE = "https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-phosphate.pdf"
CSV_PATH = Path(__file__).with_name("mcs2026_phosphate_snapshot.csv")

with CSV_PATH.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("USGS MCS 2026 phosphate rock; units: thousand metric tons, marketable product")
print("2025e production / 2026-vintage reserve or resource quantity; arithmetic only")
for row in rows:
    production = int(row["production_2025e_kt_per_year"])
    quantity = int(row["reported_quantity_kt"])
    if row["quotient_type"] == "R_over_P":
        quotient = quantity / production
        print(f"{row['area']}: {quantity:,} / {production:,} = {quotient:,.1f} yr (vintage-specific R/P snapshot)")
    else:
        quotient = 0.9 * quantity / production
        print(f"{row['area']}: 0.9 * >{quantity:,} / {production:,} > {quotient:,.0f} yr (resource-threshold arithmetic)")

# Reproducible model-conditioned illustration; g and eta are not estimated.
tau = 73_000_000 / 250_000
g = 0.03
x = g * tau
eta_c = 1 - x / math.expm1(x)
assert tau == 292.0 and math.isclose(eta_c, 0.9986254751869947, rel_tol=1e-13)
print(f"\nIllustrative crossover: tau={tau:.2f} yr, g={g:.3f} yr^-1, x={x:.2f}, eta_c={eta_c:.6f}")
for eta in (0, 0.25, 0.50, 0.75, 0.90, 0.99, eta_c):
    T = math.log1p(x / (1 - eta)) / g
    print(f"eta={eta:.6f}: T={T:.2f} yr; T/tau={T/tau:.3f}")
print("Source:", SOURCE)
