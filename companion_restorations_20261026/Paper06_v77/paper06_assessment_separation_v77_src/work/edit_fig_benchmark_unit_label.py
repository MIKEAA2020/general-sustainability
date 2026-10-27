#!/usr/bin/env python3
"""Relabel only the benchmark figure's quota-axis unit for Paper06 v77.

The clean input raster is preserved from the v76 PDF. The plot values and all
other artwork remain unchanged. Model biomass coordinates are synthetic model
biomass units (MBU), not physical kilotonnes. Paths resolve relative to this
file, so the script can be run from any directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
FIGS = ROOT / "paper06_assessment_separation_v77_src" / "figs"
BASE = FIGS / "fig_benchmark_original_v76.png"
OUT = FIGS / "fig_benchmark.png"

im = Image.open(BASE).convert("RGBA")
width, height = im.size
if (width, height) != (3120, 1200):
    raise ValueError(f"Unexpected benchmark figure dimensions: {im.size}")

# The original vertical label occupies x=1509..1565, y=334..798 in the
# 3120x1200 raster. Clear only its white margin; preserve the adjacent tick
# labels and plot border.
pix = np.asarray(im).copy()
x0, y0, x1, y1 = 1490, 305, 1570, 830
pix[y0:y1, x0:x1, :3] = 255
pix[y0:y1, x0:x1, 3] = 255
background = Image.fromarray(pix, mode="RGBA")

fig = plt.figure(figsize=(width / 300, height / 300), dpi=300, frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, width)
ax.set_ylim(height, 0)
ax.axis("off")
ax.text(
    1530,
    567,
    r"quota $H^*(t)$ (MBU/yr)",
    fontsize=11.5,
    color="#262626",
    rotation=90,
    ha="center",
    va="center",
)
fig.canvas.draw()
overlay = np.asarray(fig.canvas.buffer_rgba()).copy()
plt.close(fig)

alpha = overlay[:, :, 3:4].astype(np.float32) / 255
foreground = overlay[:, :, :3].astype(np.float32)
base = np.asarray(background).astype(np.float32)
result = np.empty_like(base)
result[:, :, :3] = alpha * foreground + (1 - alpha) * base[:, :, :3]
result[:, :, 3] = 255
Image.fromarray(np.clip(result, 0, 255).astype(np.uint8), "RGBA").save(OUT, dpi=(300, 300))
print(f"Relabeled quota axis in {OUT} from {BASE}")
