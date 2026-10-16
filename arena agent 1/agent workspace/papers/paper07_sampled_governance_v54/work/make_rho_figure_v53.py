#!/usr/bin/env python3
"""Render the v53 baseline multiplier figure with explicit update labels."""
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "work"))
from p07_core import build, rho  # noqa: E402

model = build()
T = np.geomspace(0.2, 200.0, 3000)
curves = {
    "Mobilising: exponential frozen-assessment": ("mobilising", "exact", "#2563a6", "-"),
    "Mobilising: forward Euler": ("mobilising", "euler", "#ef7f19", "--"),
    "Protective: exponential frozen-assessment": ("protective", "exact", "#25844a", "-"),
    "Protective: forward Euler": ("protective", "euler", "#e23b3b", "--"),
}
fig, ax = plt.subplots(figsize=(9.2, 5.2), constrained_layout=True)
for label, (channel, update, color, style) in curves.items():
    values = [rho(float(t), model, channel, update) for t in T]
    ax.plot(T, values, label=label, color=color, linestyle=style, linewidth=2.0)
ax.axhline(1.0, color="#111827", linewidth=1.1)
ax.axvline(6.5012949481, color="#263648", linestyle=":", linewidth=1.3,
           label="exponential mobilising crossing: 6.501 yr")
ax.set_xscale("log")
ax.set_xlim(0.2, 200)
ax.set_ylim(0.9, 1.4)
ax.set_xlabel(r"Review interval $T_r$ (years)")
ax.set_ylabel(r"Spectral radius $\rho(T_r)$")
ax.set_title("Baseline multiplier scans for the illustrative logistic core")
ax.grid(which="major", color="#ccd5de", linewidth=0.8)
ax.grid(which="minor", color="#e6ebef", linewidth=0.5, linestyle=":")
ax.set_axisbelow(True)
ax.legend(loc="upper left", frameon=True, fontsize=8.4)
fig.savefig(ROOT / "figs/fig_rho_scan_v53.png", dpi=220, bbox_inches="tight")
print(f"saved {ROOT / 'figs/fig_rho_scan_v53.png'}")
