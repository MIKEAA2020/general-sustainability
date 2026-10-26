#!/usr/bin/env python3
"""Move the Figure 2 equality labels without changing other figure content.

Run from the Paper06_v74 package root.  The immutable v72 image is the input;
this script writes the corrected image to the normal Figure 2 filename.
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
FIGS = ROOT / "paper06_assessment_separation_v74_src" / "figs"
BASE = FIGS / "fig_witness_triangle_original_v72.png"
OUT = FIGS / "fig_witness_triangle.png"

image = cv2.imread(str(BASE), cv2.IMREAD_COLOR)
if image is None:
    raise FileNotFoundError(BASE)
height, width = image.shape[:2]

# The hatch texture is exactly phase-matched by translating (x,y) to
# (x+d,y-d).  Replace only dark text pixels that disagree with this texture
# (or the constant light-gray region), and retain the original diagonal line.
patches = [
    {"box": (420, 200, 550, 320), "intercept": -214, "shift": 20},
    {"box": (1510, 185, 1665, 320), "intercept": -1325, "shift": 15},
]
for spec in patches:
    x0, y0, x1, y1 = spec["box"]
    intercept = spec["intercept"]
    shift = spec["shift"]
    yy, xx = np.mgrid[y0:y1, x0:x1]
    roi = image[y0:y1, x0:x1]
    source_x, source_y = xx + shift, yy - shift
    source = image[
        np.clip(source_y, 0, height - 1),
        np.clip(source_x, 0, width - 1),
    ]

    patterned_side = yy < xx + intercept
    distance_to_diagonal = np.abs(yy - (xx + intercept))
    chroma = roi.max(axis=2) - roi.min(axis=2)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    difference = np.max(
        np.abs(roi.astype(np.int16) - source.astype(np.int16)), axis=2
    )

    # Remove neutral, dark remnants of the original rotated text on the
    # hatched side. The surrounding hatch pixels are unchanged because the
    # reference sample has the same hatch phase.
    mask_hatch = (
        patterned_side
        & (difference > 4)
        & (chroma < 135)
        & (gray < 225)
        & (distance_to_diagonal > 1.8)
    )
    roi[mask_hatch] = source[mask_hatch]

    # Clear corresponding dark text pixels on the plain gray side. The
    # chroma test preserves the red FAST/SLOW arrows.
    mask_gray = (
        (~patterned_side)
        & (chroma < 95)
        & (gray < 225)
        & (distance_to_diagonal > 1.8)
    )
    roi[mask_gray] = (237, 237, 237)

# Add both labels horizontally, immediately above the corresponding diagonal
# at the left edge of each label.  Image-coordinate y increases downward.
fig = plt.figure(figsize=(width / 200, height / 200), dpi=200, frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, width)
ax.set_ylim(height, 0)
ax.axis("off")
for x, y in ((456, 220), (1565, 220)):
    ax.text(
        x,
        y,
        r"$s_1+s_2=2$",
        fontsize=9.3,
        color="#161616",
        ha="left",
        va="center",
        rotation=0,
        path_effects=[pe.Stroke(linewidth=1.2, foreground="#f8f5f4"), pe.Normal()],
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
