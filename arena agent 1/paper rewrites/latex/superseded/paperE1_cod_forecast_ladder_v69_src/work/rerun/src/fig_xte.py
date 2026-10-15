#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
ssb = pd.read_csv(ROOT / "data/xtencam_table17_ssb.csv")
ncam = pd.read_csv(ROOT / "data/ncam_2016_table_a2.csv")
lrp = 276.0

fig, ax = plt.subplots(figsize=(7.4, 3.6))
ax.plot(ssb.year, ssb.ssb_kt, color="#1b4f72", lw=1.8, label="xteNCAM SSB (Table 17)")
ax.fill_between(ssb.year, ssb.ssb_lo, ssb.ssb_hi, color="#1b4f72", alpha=0.15, label="xte 95% CI")
ax.plot(ncam.year, ncam.ssb_kt, color="#b9770e", lw=1.4, ls="--", marker="o", ms=3, label="NCAM 2016 (not pooled)")
ax.axhline(lrp, color="#922b21", ls="--", lw=1.1, label=f"xte LRP 40% BMSY = {lrp:.0f} kt")
ax.axhline(884.6, color="#922b21", ls=":", lw=0.9, label="2016 LRP (other Ω)")
ax.set_xlim(1953, 2025)
ax.set_ylim(0, 1800)
ax.set_xlabel("Year")
ax.set_ylabel("SSB (kt)")
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
ax.set_title("Two specifications — not one series")
fig.tight_layout()
fig.savefig(ROOT / "manuscript/fig4_xtencam.png", dpi=160)
fig.savefig(ROOT / "manuscript/fig4_xtencam.svg")
print("wrote fig4")
