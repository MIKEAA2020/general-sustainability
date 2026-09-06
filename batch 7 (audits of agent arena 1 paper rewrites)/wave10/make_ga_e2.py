#!/usr/bin/env python3
"""Graphical abstract for paperE2_cod_intervention (latest v21).

House style: 3-panel banner, 1328 x 531 px (h x w), 200 dpi PNG, 400 dpi
TIFF, vector PDF. Sizing discipline: 1 pt = 2.78 px; >= 3 px clearance;
fail-loud auto-fit. Every number is the paper's registered value
(r = 0.2369; K = 5000 kt; LRP 884.6 kt; largest robust constant catch
91.6 kt; survival 0.91 at zero catch and 0.65 at 120 kt; bootstrap 90%
CI [0, 87.1] kt; kernels empty beyond 7 yr; K >= 2K* = 1769.2 kt);
nothing is invented.
  A  AFTER THE COLLAPSE : the object, the map, the floor
  B  WHAT CATCH CAN HOLD: the 91.6-kt robust catch under the worst case
  C  WHEN CATCH CANNOT HELP: no dominance, empty kernels, good years

Wave-11 owner-directed fixes, root-caused: the wave-10 vlines stacker drew
each box's line list BOTTOM-TO-TOP, so every multi-line box rendered in
reverse reading order (bold headline at the bottom) - the owner's two E2
comments exposed it ("zone rule holds ... does not make sense" = the top
line of the reversed panel-B lower box; "first and second sentence should
swap" = the two reversed fragments of the panel-C margin sentence). vlines
now renders lists in reading order (headline on top, the ECOMOD house
convention; stack geometry unchanged). On top of that root fix: panel B's
lower box restores the paper's registered abstract wording verbatim
("zero catch and the moratorium hold the safe set; the critical-zone and
cascade rules hold the LRP from itself" - wave-10 had also dropped the
"from" and the cascade). Panel C's lower box: wave-11 put it in the
owner-directed margin-first order (a compensation issued while the box
still rendered bottom-to-top); the owner's wave-12 directive - "the LRP
line should be at top" - restores the headline-first house convention:
bold "the LRP is protected by good years" on top, then "the margin good
years must supply is smaller than the frozen convention implied" ("they"
resolved to "good years", the paper's own Section-4 wording).
Outputs: graphical_abstracts/graphical_abstract_e2.{pdf,png,tiff}
"""
import hashlib
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
OUT = PR / "graphical_abstracts"
OUT.mkdir(parents=True, exist_ok=True)
STEM = OUT / "graphical_abstract_e2"

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
# PANEL A — AFTER THE COLLAPSE
# =====================================================================
head(218, "AFTER THE COLLAPSE", "Northern cod \u00b7 NAFO 2J3KL", 396, 330)
facts = [
    ("the 1992 moratorium", "can any catch policy hold the LRP?", 316, STOCK, "#fbeaea"),
    ("the fitted surplus map", "r = 0.2369 \u00b7 K = 5000 kt (at bound)", 244, BLUE, "#eaf1f7"),
    ("limit reference point", "884.6 kt (2016) \u2014 a floor on SSB", 172, FLOW, "#e7f4ec"),
]
for (t1, t2, yy, col, bg) in facts:
    ATTR.clear()
    ATTR[t1] = {"weight": "bold"}
    ATTR[t2] = {"color": col}
    box(28, yy, 380, 64, fc=bg, ec=col, lw=1.5)
    vlines(218, yy, 380, 64, [(t1, 7.6), (t2, 6.8)])
box(28, 92, 380, 64, fc="#ffffff", ec=GREY, lw=1.2)
ATTR.clear()
ATTR["protocol frozen before any score"] = {"weight": "bold", "color": DARK}
ATTR["kernels \u00b7 boundaries \u00b7 replays \u00b7 selection"] = {"color": GREY}
vlines(218, 92, 380, 64, [("protocol frozen before any score", 7.0),
                          ("kernels \u00b7 boundaries \u00b7 replays \u00b7 selection", 6.4)])

# =====================================================================
# PANEL B — WHAT CATCH CAN HOLD
# =====================================================================
head(644, "WHAT CATCH CAN HOLD", "under the worst-case floor", 400, 340)
box(446, 322, 394, 58, fc="#fff3e0", ec=ACCENT, lw=1.4)
ATTR.clear()
ATTR["worst-case productivity floor"] = {"weight": "bold"}
ATTR["the 10th-percentile class"] = {"color": ACCENT}
vlines(643, 322, 394, 58, [("worst-case productivity floor", 7.4),
                           ("the 10th-percentile class", 6.8)])
ATTR.clear()
ATTR["91.6 kt"] = {"weight": "bold", "color": FLOW}
ATTR["largest robust constant catch"] = {"color": DARK}
vlines(644, 284, 380, 40, [("91.6 kt", 8.2), ("largest robust constant catch", 6.6)])
# catch dial
AX_Y = 252
ax.annotate("", xy=(820, AX_Y), xytext=(470, AX_Y),
            arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.2), zorder=5)
txt(462, AX_Y, "0", size=6.4, color=GREY, ha="right")
# green robust segment 0 -> 91.6 kt (scale: 470 + c/130 * 350)
def cx(c):
    return 470 + c / 130.0 * 350
ax.add_patch(Rectangle((cx(0), 262), cx(91.6) - cx(0), 20,
                       facecolor=FLOW, edgecolor="none", alpha=0.92, zorder=4))
txt(cx(87.1), 272, "87.1", size=6.0, color="#ffffff", ha="right", z=7)
ax.plot([cx(87.1), cx(87.1)], [AX_Y, 282], color=DARK, lw=1.0, ls=(0, (2, 2)), zorder=5)
ax.plot([cx(120)], [AX_Y], "x", ms=8, mec=STOCK, mew=1.8, zorder=7)
ATTR.clear()
ATTR["0 kt: survival 0.91 \u00b7 CI [0, 87.1]"] = {"color": DARK}
vlines(644, 212, 380, 34, [("0 kt: survival 0.91 \u00b7 CI [0, 87.1]", 6.4)])
txt(836, 190, "120 kt: survival 0.65",
    size=fit("120 kt: survival 0.65", 200, maxsize=6.2), color=STOCK, ha="right")
box(446, 96, 394, 74, fc="#e7f4ec", ec=FLOW, lw=1.4)
ATTR.clear()
ATTR["zero catch and the moratorium"] = {"weight": "bold"}
vlines(643, 96, 394, 74, [("zero catch and the moratorium", 7.0),
                          ("hold the safe set; the critical-zone and", 6.4),
                          ("cascade rules hold the LRP from itself", 6.4)])

# =====================================================================
# PANEL C — WHEN CATCH CANNOT HELP
# =====================================================================
head(1090, "WHEN CATCH CANNOT HELP", "the map is expansive at the LRP", 436, 350)
calls = [
    ("no non-BAU policy dominates BAU", "under the declared partial order", 330, STOCK, "#fbeaea"),
    ("positive-catch rules: empty", "at the 5th-percentile floor, T = \u221e", 258, GREY, "#ffffff"),
    ("certified kernels: empty", "beyond 7 yr \u00b7 K \u2265 2K* = 1769.2 kt", 186, BLUE, "#eaf1f7"),
]
for (t1, t2, yy, col, bg) in calls:
    ATTR.clear()
    ATTR[t1] = {"weight": "bold", "color": DARK}
    ATTR[t2] = {"color": col}
    box(876, yy, 422, 56, fc=bg, ec=col, lw=1.4)
    vlines(1087, yy, 422, 56, [(t1, 7.2), (t2, 6.6)])
box(876, 96, 422, 74, fc="#f0f4f8", ec="#c3d3e3", lw=1.4)
ATTR.clear()
ATTR["the LRP is protected by good years"] = {"weight": "bold"}
ATTR["smaller than the frozen convention implied"] = {"color": GREY, "style": "italic"}
vlines(1087, 96, 422, 74, [("the LRP is protected by good years", 7.0),
                           ("the margin good years must supply is", 6.6),
                           ("smaller than the frozen convention implied", 6.6)])

txt(W / 2, 40, "Robust Viability of the 2J3KL Limit Reference Point under a Surplus-Production",
    size=fit("Robust Viability of the 2J3KL Limit Reference Point under a Surplus-Production",
             W - 40, "bold", 9.0), color=DARK, weight="bold")
txt(W / 2, 13, "Map: Policy Scoring, Expansion, and When Catch Cannot Help",
    size=fit("Map: Policy Scoring, Expansion, and When Catch Cannot Help",
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
