#!/usr/bin/env python3
"""Move the Figure 2 equality labels off, and immediately beside, the diagonal.

The v72 source raster placed each equation over its boundary. This script
reconstructs only the small labelled boundary segments from the preserved
hatch/gray backgrounds, redraws the original diagonal, and places each label
parallel to it on the unhatched side with a visible non-overlap gap. All other
figure content is retained. Run from any directory.

Requirements: Python, NumPy, OpenCV, Pillow, and Matplotlib.
"""
from pathlib import Path

import cv2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
FIGS = ROOT / "paper06_assessment_separation_v77_src" / "figs"
BASE = FIGS / "fig_witness_triangle_original_v72.png"
OUT = FIGS / "fig_witness_triangle.png"

original = cv2.imread(str(BASE), cv2.IMREAD_COLOR)
if original is None:
    raise FileNotFoundError(BASE)
image = original.copy()
height, width = image.shape[:2]

# In source-raster coordinates, the two diagonal boundaries are y=x+b.
# The x windows cover only the old equation labels and a small length of line
# at either end, so the regenerated stroke joins the untouched original line.
regions = [
    {
        "x0": 400,
        "x1": 550,
        "intercept": -214,
        "hatch_shift": 20,
        "label_center_x": 450,
        "hatch_top_y": 151,
        "hatch_right_x": 570,
        "arrow_x": (180, 640),
        "arrow_y": (318, 324),
    },
    {
        "x0": 1515,
        "x1": 1665,
        "intercept": -1325,
        "hatch_shift": 20,
        "label_center_x": 1550,
        "hatch_top_y": 151,
        "hatch_right_x": 1776,
        "arrow_x": (1300, 1750),
        "arrow_y": (318, 324),
    },
]

for region in regions:
    x0, x1 = region["x0"], region["x1"]
    b = region["intercept"]
    shift = region["hatch_shift"]
    y0 = max(0, x0 + b - 50)
    y1 = min(height, x1 + b + 50)
    yy, xx = np.mgrid[y0:y1, x0:x1]
    signed_distance = (yy - xx - b) / np.sqrt(2)
    roi = image[y0:y1, x0:x1]

    # The diagonal hatches run parallel to (+shift,-shift). Sampling in that
    # direction preserves their phase while clearing the old text and line.
    # In image coordinates, the hatch strokes run along (+1,-1). Sample
    # farther into the hatched side while preserving their phase; near the
    # clipped top/right edges, reduce the shift so it stays inside the field.
    available = np.minimum(
        shift,
        np.minimum(
            yy - region["hatch_top_y"] - 2,
            region["hatch_right_x"] - xx - 2,
        ),
    )
    offset = np.clip(available, 0, shift).astype(np.int32)
    source = original[
        np.clip(yy - offset, 0, height - 1),
        np.clip(xx + offset, 0, width - 1),
    ]
    line_band = np.abs(signed_distance) < 4
    patterned_line = line_band & (signed_distance < 0)
    plain_line = line_band & (signed_distance >= 0)
    roi[patterned_line] = source[patterned_line]
    roi[plain_line] = (237, 237, 237)

    # Remove the old dark lettering outside the boundary's own stroke. Only
    # neutral-dark pixels are selected, so colored hatch strokes are retained.
    gray_values = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    chroma = roi.max(axis=2) - roi.min(axis=2)
    old_text = (
        (np.abs(signed_distance) < 22)
        & (gray_values < 225)
        & (chroma < 70)
    )
    old_text_hatch = old_text & (signed_distance < 0)
    old_text_plain = old_text & (signed_distance >= 0)
    roi[old_text_hatch] = source[old_text_hatch]
    roi[old_text_plain] = (237, 237, 237)

    # Restore the short horizontal red dip stroke crossing the boundary. The
    # diagonal hatch texture itself has been phase-reconstructed above.
    ax0, ax1 = region["arrow_x"]
    ay0, ay1 = region["arrow_y"]
    source_arrow = original[ay0:ay1, ax0:ax1]
    source_rgb = cv2.cvtColor(source_arrow, cv2.COLOR_BGR2RGB)
    red_stroke = (
        (source_rgb[:, :, 0] > source_rgb[:, :, 1] + 50)
        & (source_rgb[:, :, 0] > source_rgb[:, :, 2] + 40)
        & (source_rgb[:, :, 0] > 80)
    )
    arrow_target = image[ay0:ay1, ax0:ax1]
    arrow_target[red_stroke] = source_arrow[red_stroke]

    # Restore the straight boundary itself over the short cleared segment.
    cv2.line(
        image,
        (x0, x0 + b),
        (x1, x1 + b),
        (0, 0, 0),
        thickness=3,
        lineType=cv2.LINE_AA,
    )

# Place each equation on the plain gray side, parallel to and immediately
# adjacent to its line. The 20-pixel vertical offset is 14.1 pixels normal to
# the 45-degree boundary; the rendered glyphs remain separated from its stroke.
fig = plt.figure(figsize=(width / 200, height / 200), dpi=200, frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, width)
ax.set_ylim(height, 0)
ax.axis("off")
for region in regions:
    x = region["label_center_x"]
    y = x + region["intercept"] + 20
    ax.text(
        x,
        y,
        r"$s_1+s_2=2$",
        fontsize=8.3,
        color="#161616",
        ha="center",
        va="center",
        rotation=-45,
        rotation_mode="anchor",
        path_effects=[pe.Stroke(linewidth=0.4, foreground="#ededed"), pe.Normal()],
    )

fig.canvas.draw()
rgba = np.asarray(fig.canvas.buffer_rgba()).copy()
plt.close(fig)

alpha = rgba[:, :, 3:4].astype(np.float32) / 255
text_rgb = rgba[:, :, :3].astype(np.float32)
background_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
composite = np.clip(alpha * text_rgb + (1 - alpha) * background_rgb, 0, 255)
Image.fromarray(composite.astype(np.uint8)).save(OUT, dpi=(200, 200))
print(f"Wrote {OUT} ({width} x {height} px, 200 dpi)")
