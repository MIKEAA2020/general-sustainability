#!/usr/bin/env python3
"""Graphical abstract for paper5_sampled_governance (latest v25).

House style: 3-panel banner, 1328 x 531 px (h x w), 200 dpi PNG, 400 dpi
TIFF, vector PDF. Sizing discipline: 1 pt = 2.78 px; >= 3 px clearance;
fail-loud auto-fit. Every number is the paper's registered value (the
Section 3.3 crossing record: 2.306 / 6.501 / 47.536 / 79.143; the 42-stock
screen; the Northern cod case); nothing is invented.
  A  GOVERNANCE IS PERIODIC     : the sample-and-hold staircase
  B  THE CROSSING RECORD        : exact vs Euler update, T_r axis
  C  STABILITY DOES NOT TRANSFER: distinct operators
Wave-11 owner-directed layout fix: the four row labels (prot.exact /
prot.Euler / extr.exact / extr.Euler) were centred at x=560 and their
right ends (up to x=617.8) overlapped the strips' left end (x=594) by
up to 24 px; they are now right-aligned at x=588 (6 px clear of the
strips, leftmost edge ~x=472, well inside the panel B frame).
Wave-11 root-cause fix inherited from the owner's E2 feedback: the
vlines stacker drew every multi-line box's list bottom-to-top, so all
boxes rendered in reverse reading order (bold headline at the bottom);
vlines now renders lists in reading order (headline on top, the ECOMOD
house convention; stack geometry unchanged).
Outputs: graphical_abstracts/graphical_abstract_p5.{pdf,png,tiff}
"""
import hashlib
import sys
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
OUT = PR / "graphical_abstracts"
OUT.mkdir(parents=True, exist_ok=True)
STEM = OUT / "graphical_abstract_p5"

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
def txt(x, y, s, size=7.6, color=DARK, weight="normal", ha="center", va="center",
        z=8, style="normal"):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
            style=style, zorder=z, linespacing=1.30)

ATTR = {}
def lines_color(s): return ATTR.get(s, {}).get("color", DARK)
def lines_weight(s): return ATTR.get(s, {}).get("weight", "normal")
def lines_style(s): return ATTR.get(s, {}).get("style", "normal")

def vlines(x, ybot, w, h, lines):
    # wave-11 root-cause fix: the wave-10 stacker drew the list bottom-to-top,
    # so every multi-line box rendered in REVERSE reading order (the root cause
    # of the owner-flagged E2 text). Reverse here so the list's first line
    # renders at the TOP; the stack geometry is unchanged (same slots).
    lines = list(reversed(lines))
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
# PANEL A — GOVERNANCE IS PERIODIC (the sample-and-hold staircase)
# =====================================================================
head(218, "GOVERNANCE IS PERIODIC", "assess at cadence \u00b7 hold between", 396, 330)
box(28, 292, 380, 84, fc="#eef6f1", ec=FLOW, lw=1.4)
ATTR.clear()
ATTR["sample-and-hold governance"] = {"weight": "bold"}
vlines(218, 292, 380, 84, [("sample-and-hold governance", 7.6),
                           ("assessment at a fixed cadence;", 6.8),
                           ("controls held between reviews", 6.8)])
# staircase sketch
ax.annotate("", xy=(400, 140), xytext=(40, 140),
            arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.2), zorder=5)
reviews = [60, 130, 200, 270, 340]
levels = [254, 222, 262, 230, 246]
for x in reviews:
    ax.plot([x, x], [146, 162], color=GREY, lw=0.9, ls=(0, (2, 2)), zorder=2)
txt(60, 172, "review", size=6.0, color=GREY, style="italic", ha="center")
pts = [(40, levels[0])]
for i, x in enumerate(reviews[1:], start=1):
    pts.append((x, levels[i - 1]))
    pts.append((x, levels[i]))
pts.append((400, levels[-1]))
xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
ax.plot(xs, ys, color=ACCENT, lw=2.6, zorder=6, solid_joinstyle="miter")
txt(218, 200, "controls held between reviews",
    size=fit("controls held between reviews", 340, maxsize=6.6), color=ACCENT)
box(28, 94, 380, 40, fc="#ffffff", ec=GREY, lw=1.1)
ATTR.clear()
ATTR["neither a continuous delay"] = {"color": GREY}
ATTR["nor an annual step matches"] = {"color": GREY}
vlines(218, 94, 380, 40, [("neither a continuous delay", 6.4),
                          ("nor an annual step matches", 6.4)])

# =====================================================================
# PANEL B — THE CROSSING RECORD (exact vs Euler; the paper's own record)
# =====================================================================
head(644, "THE CROSSING RECORD", "exact vs Euler update \u00b7 T_r", 400, 340)
SX0, SX1 = 594, 836
TMIN, TMAX = 0.2, 200.0
def tx(t):
    return SX0 + math.log(t / TMIN) / math.log(TMAX / TMIN) * (SX1 - SX0)
ROWS = [
    ("prot \u00b7 exact", 348, [(0.2, 200.0, FLOW)], []),
    ("prot \u00b7 Euler", 314, [(0.2, 2.306, FLOW), (2.306, 200.0, STOCK)],
     [(2.306, "v")]),
    ("extr \u00b7 exact", 280, [(0.2, 6.501, STOCK), (6.501, 200.0, FLOW)],
     [(6.501, "D")]),
    ("extr \u00b7 Euler", 246, [(0.2, 47.536, STOCK), (47.536, 79.143, FLOW),
                               (79.143, 200.0, STOCK)],
     [(47.536, "D"), (79.143, "v")]),
]
for (lbl, y, segs, marks) in ROWS:
    # wave-11: right-aligned at x=588 (was centred at 560, riding the strips)
    txt(588, y + 13, lbl, size=fit(lbl, 120, "bold", 6.4), color=DARK,
        weight="bold", ha="right")
    for (t0, t1, c) in segs:
        ax.add_patch(Rectangle((tx(t0), y), tx(t1) - tx(t0), 26,
                               facecolor=c, edgecolor="none", alpha=0.9, zorder=3))
    for (tm, mk) in marks:
        ax.plot([tx(tm)], [y + 13], mk, ms=6, mfc="white", mec=DARK, mew=1.0, zorder=6)
txt(715, 234, "review interval T_r (yr, log)", size=6.4, color=GREY)
txt(644, 208, "\u25c6 6.501 \u2014 the exact crossing",
    size=fit("\u25c6 6.501 \u2014 the exact crossing", 380, maxsize=6.6), color=DARK)
txt(644, 186, "Euler: 2.306 \u00b7 47.5 \u00b7 79.1 \u2014 artefacts",
    size=fit("Euler: 2.306 \u00b7 47.5 \u00b7 79.1 \u2014 artefacts", 380, maxsize=6.2),
    color=GREY, style="italic")
box(446, 96, 394, 74, fc="#f0f4f8", ec="#c3d3e3", lw=1.4)
ATTR.clear()
ATTR["the rapid-review limit is"] = {"weight": "bold"}
vlines(643, 96, 394, 74, [("the rapid-review limit is", 7.2),
                          ("a finite-horizon consistency", 6.6),
                          ("statement, not a stability claim", 6.6)])

# =====================================================================
# PANEL C — STABILITY DOES NOT TRANSFER
# =====================================================================
head(1090, "STABILITY DOES NOT TRANSFER", "distinct operators", 436, 350)
calls = [
    ("the sampled map \u2260 the delay equation",
     "observation and update at discrete reviews", 330, BLUE, "#eaf1f7"),
    ("first-order thresholds", "are command-step artefacts", 258, GREY, "#ffffff"),
    ("a selected 42-stock screen", "the Northern cod case", 186, ACCENT, "#fff3e0"),
]
for (t1, t2, yy, col, bg) in calls:
    ATTR.clear()
    ATTR[t1] = {"weight": "bold", "color": DARK}
    ATTR[t2] = {"color": col}
    box(876, yy, 422, 56, fc=bg, ec=col, lw=1.4)
    vlines(1087, yy, 422, 56, [(t1, 7.2), (t2, 6.6)])
box(876, 96, 422, 74, fc="#f0f4f8", ec="#c3d3e3", lw=1.4)
ATTR.clear()
ATTR["substituting a continuous delay"] = {"weight": "bold"}
vlines(1087, 96, 422, 74, [("substituting a continuous delay", 7.0),
                           ("or an annual step can move or", 6.6),
                           ("delete stability boundaries", 6.6)])

txt(W / 2, 40, "Periodic Review as Sampled Governance: Sample-and-Hold Dynamics of Assessment-Driven",
    size=fit("Periodic Review as Sampled Governance: Sample-and-Hold Dynamics of Assessment-Driven",
             W - 40, "bold", 8.6), color=DARK, weight="bold")
txt(W / 2, 13, "Effort Control, a Selected 42-Stock Spectral Screen, and the Northern Cod Case",
    size=fit("Effort Control, a Selected 42-Stock Spectral Screen, and the Northern Cod Case",
             W - 40, "bold", 8.6), color=DARK, weight="bold")

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
