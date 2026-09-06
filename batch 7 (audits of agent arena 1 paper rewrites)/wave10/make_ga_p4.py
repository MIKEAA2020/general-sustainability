#!/usr/bin/env python3
"""Graphical abstract for paper4_delay_dynamics (latest v30).

House style: 3-panel banner, 1328 x 531 px (h x w), 200 dpi PNG, 400 dpi
TIFF, vector PDF. Sizing discipline: 1 pt = 2.78 px; every stacked line
pair has >= 3 px clearance; every string auto-fits its box (fail-loud).
Every number is the paper's registered value (Hopf window near 3.7 and
150 yr, loop gain 0.080 < 1, restabilising crossing near 6.5 yr, Euler
artefact 47.5 yr); nothing is invented.
  A  THE DELAY SITS IN GOVERNANCE : the stock-memory-effort loop, tau in
                                    the institutional link, the two laws
  B  TWO CHANNELS, OPPOSITE MATH  : stability vs deployment delay tau
  C  THE REVIEW INTERVAL AS CONTROL: sample-and-hold, 6.5-yr crossing
Outputs: graphical_abstracts/graphical_abstract_p4.{pdf,png,tiff}
"""
import hashlib
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Polygon

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
OUT = PR / "graphical_abstracts"
OUT.mkdir(parents=True, exist_ok=True)
STEM = OUT / "graphical_abstract_p4"

W, H = 1328, 531
DPI = 200
PX = DPI / 72.0
fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
fig.canvas.draw(); RENDER = fig.canvas.get_renderer()

FLOW, STOCK, DARK, ACCENT = "#1f8a4c", "#b23a48", "#1f3a5f", "#e0a458"
GREY, BLUE = "#5c6b73", "#3f7cac"

def meas(s, size, weight="normal"):
    t = ax.text(0, 0, s, fontsize=size, fontweight=weight)
    bb = t.get_window_extent(RENDER); t.remove()
    return bb.width

def fit(s, maxw, weight="normal", maxsize=8.6, minsize=4.6):
    assert len(s) * 0.62 * PX * minsize <= maxw + 1, \
        f"string too long for fit(): {s[:40]!r} ({len(s)} chars, box {maxw}px)"
    size = maxsize
    while size > minsize and meas(s, size, weight) > maxw:
        size -= 0.1
    return size

def box(x, y, w, h, fc="#ffffff", ec=DARK, lw=1.4, r=9, z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                linewidth=lw, edgecolor=ec, facecolor=fc, zorder=z))
def arrow(x1, y1, x2, y2, color=DARK, lw=2.0, rad=0.0, z=5, ms=11, ls="-", shrink=3):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=ms,
                                 linewidth=lw, color=color, connectionstyle=f"arc3,rad={rad}",
                                 zorder=z, shrinkA=shrink, shrinkB=shrink, linestyle=ls))
def txt(x, y, s, size=7.6, color=DARK, weight="normal", ha="center", va="center",
        z=8, style="normal"):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
            style=style, zorder=z, linespacing=1.30)

ATTR = {}
def lines_color(s): return ATTR.get(s, {}).get("color", DARK)
def lines_weight(s): return ATTR.get(s, {}).get("weight", "normal")
def lines_style(s): return ATTR.get(s, {}).get("style", "normal")

def vlines(x, ybot, w, h, lines):
    n = len(lines)
    fitted = [(s, fit(s, w - 14, lines_weight(s), sz)) for (s, sz) in lines]
    halves = [fsz * PX / 2 for (_, fsz) in fitted]
    total = 2 * sum(halves) + 3.0 * (n - 1)
    y = ybot + (h - total) / 2
    for (s, fsz), hh in zip(fitted, halves):
        txt(x, y + hh, s, size=fsz, color=lines_color(s),
            weight=lines_weight(s), style=lines_style(s))
        y += 2 * hh + 3.0

def head(cx, t, sub, tw, subw):
    txt(cx, 453, t, size=fit(t, tw, "bold", 10.2), color=DARK, weight="bold")
    txt(cx, 424, sub, size=fit(sub, subw, maxsize=8.0), color=GREY, style="italic")

for (x0, w, fc, ec) in [(10, 416, "#fbfdfc", "#d6e2dc"),
                        (434, 420, "#f7fafd", "#d3e2ef"),
                        (862, 456, "#fcfbf7", "#e7e2d2")]:
    ax.add_patch(Rectangle((x0, 58), w, 400, facecolor=fc, edgecolor=ec, lw=1.0, zorder=0))

# =====================================================================
# PANEL A — THE DELAY SITS IN GOVERNANCE
# =====================================================================
head(218, "THE DELAY SITS IN GOVERNANCE", "not in the ecology", 396, 330)
nw, nh = 118, 44
def node(cx, cy, lbl, fc="#ffffff", ec=DARK):
    box(cx - nw / 2, cy - nh / 2, nw, nh, fc=fc, ec=ec, lw=1.4, r=8)
    txt(cx, cy, lbl, size=fit(lbl, nw - 12, "bold", 7.6), color=DARK, weight="bold")
node(218, 386, "stock  N")
node(330, 250, "memory  Z", fc="#eaf1f7", ec=BLUE)
node(106, 250, "effort  E", fc="#e7f4ec", ec=FLOW)
arrow(265, 364, 315, 272, color=BLUE, lw=1.8)
txt(300, 318, "signal filtered", size=fit("signal filtered", 120, maxsize=6.6), color=BLUE)
arrow(271, 250, 165, 250, color=ACCENT, lw=2.6)
ax.add_patch(Circle((218, 250), 13, facecolor="#ffffff", edgecolor=ACCENT, lw=2.0, zorder=6))
txt(218, 250, "\u03c4", size=9.0, color=ACCENT, weight="bold", z=9)
txt(218, 216, "deployment delay", size=fit("deployment delay", 200, maxsize=6.8), color=ACCENT)
arrow(150, 272, 185, 364, color=FLOW, lw=1.8)
txt(95, 318, "catch qEN", size=fit("catch qEN", 110, maxsize=6.6), color=FLOW)
box(28, 130, 380, 70, fc="#fff3e0", ec=ACCENT, lw=1.4)
ATTR.clear()
ATTR["the delay is institutional"] = {"weight": "bold"}
ATTR["not an ecological lag"] = {"color": GREY, "style": "italic"}
vlines(218, 130, 380, 70, [("the delay is institutional", 7.6),
                           ("assessment \u2192 decision \u2192 action", 6.8),
                           ("not an ecological lag", 6.6)])
for (x, t1, t2, t3, col, bg) in [
        (28, "mobilising law", "gain grows with", "deployment", STOCK, "#fbeaea"),
        (226, "protective law", "restores toward", "a quota cap", FLOW, "#e7f4ec")]:
    ATTR.clear()
    ATTR[t1] = {"weight": "bold"}
    ATTR[t3] = {"color": col}
    box(x, 60, 186, 62, fc=bg, ec=col, lw=1.4)
    vlines(x + 93, 60, 186, 62, [(t1, 7.2), (t2, 6.4), (t3, 6.4)])

# =====================================================================
# PANEL B — TWO CHANNELS, OPPOSITE MATH (stability vs tau)
# =====================================================================
head(644, "TWO CHANNELS, OPPOSITE MATH", "stability vs the deployment delay \u03c4", 400, 340)
SX0, SX1 = 594, 836
TMIN, TMAX = 0.5, 300.0
import math
def tx(t):
    return SX0 + math.log(t / TMIN) / math.log(TMAX / TMIN) * (SX1 - SX0)
def strip(y, segs):
    for (t0, t1, c) in segs:
        ax.add_patch(Rectangle((tx(t0), y), tx(t1) - tx(t0), 26,
                               facecolor=c, edgecolor="none", alpha=0.9, zorder=3))
txt(528, 339, "mobilising", size=fit("mobilising", 110, "bold", 6.6), color=STOCK,
    weight="bold", ha="center")
txt(528, 257, "protective", size=fit("protective", 110, "bold", 6.6), color=FLOW,
    weight="bold", ha="center")
strip(326, [(0.5, 3.7, STOCK), (3.7, 150, FLOW), (150, 300, STOCK)])
strip(244, [(0.5, 300, FLOW)])
txt(671, 362, "3.7", size=6.0, color=DARK)
txt(805, 362, "150", size=6.0, color=DARK)
for xm in (tx(3.7), tx(150)):
    ax.plot([xm], [339], "D", ms=6, mfc="white", mec=DARK, mew=1.0, zorder=6)
txt(644, 380, "subcritical Hopf pair \u2014 interval-certified",
    size=fit("subcritical Hopf pair \u2014 interval-certified", 380, maxsize=6.4), color=DARK)
txt(715, 308, "the lag, not the feedback,",
    size=fit("the lag, not the feedback,", 240, maxsize=6.6), color=GREY, style="italic")
txt(715, 290, "holds the window stable",
    size=fit("holds the window stable", 240, maxsize=6.6), color=GREY, style="italic")
txt(700, 257, "stable at every \u03c4",
    size=fit("stable at every \u03c4", 230, maxsize=6.4), color="#ffffff", z=7)
txt(715, 238, "\u03c4 (yr, log)", size=6.4, color=GREY)
box(446, 178, 394, 46, fc="#e7f4ec", ec=FLOW, lw=1.4)
ATTR.clear()
ATTR["no-Hopf theorem at every \u03c4"] = {"weight": "bold", "color": FLOW}
vlines(643, 178, 394, 46, [("no-Hopf theorem at every \u03c4", 7.2),
                           ("loop gain peaks at 0.080 < 1", 6.6)])
txt(644, 156, "continuation: a five-regime attractor topology",
    size=fit("continuation: a five-regime attractor topology", 380, maxsize=6.2),
    color=GREY, style="italic")

# =====================================================================
# PANEL C — THE REVIEW INTERVAL AS CONTROL (sample-and-hold)
# =====================================================================
head(1090, "THE REVIEW INTERVAL AS CONTROL", "sample-and-hold governance", 436, 350)
CX0, CX1 = 960, 1290
RMIN, RMAX = 0.2, 200.0
def rx(t):
    return CX0 + math.log(t / RMIN) / math.log(RMAX / RMIN) * (CX1 - CX0)
txt(911, 339, "mobilising", size=fit("mobilising", 92, "bold", 6.4), color=STOCK,
    weight="bold", ha="center")
txt(911, 257, "protective", size=fit("protective", 92, "bold", 6.4), color=FLOW,
    weight="bold", ha="center")
# mobilising row: unstable below 6.5, stable above (exact held update)
ax.add_patch(Rectangle((rx(0.2), 326), rx(6.5) - rx(0.2), 26,
                       facecolor=STOCK, edgecolor="none", alpha=0.9, zorder=3))
ax.add_patch(Rectangle((rx(6.5), 326), rx(200) - rx(6.5), 26,
                       facecolor=FLOW, edgecolor="none", alpha=0.9, zorder=3))
ax.add_patch(Rectangle((rx(0.2), 244), rx(200) - rx(0.2), 26,
                       facecolor=FLOW, edgecolor="none", alpha=0.9, zorder=3))
ax.plot([rx(6.5)], [339], "D", ms=6, mfc="white", mec=DARK, mew=1.0, zorder=6)
txt(rx(6.5), 362, "6.5", size=6.0, color=DARK)
txt(1075, 380, "Neimark\u2013Sacker-type crossing (exact update)",
    size=fit("Neimark\u2013Sacker-type crossing (exact update)", 420, maxsize=6.4), color=DARK)
# protective row: annual review stable (marker at T=1)
ax.plot([rx(1.0)], [257], "o", ms=6, mfc="white", mec=DARK, mew=1.0, zorder=6)
txt(1125, 257, "annual review: stable", size=fit("annual review: stable", 180, maxsize=6.0),
    color="#ffffff", z=7)
# Euler artefact marker on the mobilising row
ax.plot([rx(47.5)], [339], "x", ms=8, mec=GREY, mew=1.6, zorder=7)
txt(1125, 302, "Euler 47.5 \u2014 artefact",
    size=fit("Euler 47.5 \u2014 artefact", 210, maxsize=6.2), color=GREY, ha="center")
txt(1125, 238, "review interval T_r (yr, log)", size=6.4, color=GREY)
box(876, 96, 422, 74, fc="#f0f4f8", ec="#c3d3e3", lw=1.4)
ATTR.clear()
ATTR["the form and timing of response,"] = {"weight": "bold"}
vlines(1087, 96, 422, 74, [("the form and timing of response,", 7.2),
                           ("not ecological lag alone, decide", 6.6),
                           ("whether governance stabilises", 6.6)])

txt(W / 2, 40, "Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective",
    size=fit("Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective",
             W - 40, "bold", 9.0), color=DARK, weight="bold")
txt(W / 2, 13, "Channels of Institutional Feedback, and the Review Interval as Control",
    size=fit("Channels of Institutional Feedback, and the Review Interval as Control",
             W - 40, "bold", 9.0), color=DARK, weight="bold")

pdf = STEM.with_suffix(".pdf"); png = STEM.with_suffix(".png"); tif = STEM.with_suffix(".tiff")
plt.savefig(pdf, dpi=DPI, facecolor="white",
            metadata={"CreationDate": None, "ModDate": None, "Creator": "", "Producer": ""})
plt.savefig(png, dpi=DPI, facecolor="white")
plt.savefig(tif, dpi=400, facecolor="white", format="tiff")
plt.close(fig)

from PIL import Image
assert Image.open(png).size == (W, H), f"PNG size {Image.open(png).size}"
assert Image.open(tif).size == (2 * W, 2 * H), f"TIFF size {Image.open(tif).size}"
assert pdf.stat().st_size > 15000, "PDF too small"
for f in (pdf, png, tif):
    print(f"{f.name}  {f.stat().st_size} bytes  md5={hashlib.md5(f.read_bytes()).hexdigest()}")
sys.exit(0)
