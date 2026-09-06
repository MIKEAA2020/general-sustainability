#!/usr/bin/env python3
"""Graphical abstract for paper1_assessment_separation (latest v22).

House style: 3-panel banner, 1328 x 531 px (h x w), 200 dpi PNG, 400 dpi
TIFF, vector PDF. Sizing discipline: 1 pt = 2.78 px; >= 3 px clearance;
fail-loud auto-fit. Every statement is the paper's registered result
(the rational witness; for every nonnegative weight an aggregate-safe
action exists while no single action keeps all typed floors; the gap
FP_agg = V_weak \\ V_typ with nonempty relative interior; bridging only
by resource augmentation at a defined cost; convexification closing the
gap on the compensatory region only); nothing is invented.
  A  ONE NUMBER FROM MANY CAPITALS : compensatory aggregation
  B  THE WITNESS                   : aggregate passes, a floor fails
  C  THE SEPARATION                : V_weak strictly contains V_typ
Outputs: graphical_abstracts/graphical_abstract_p1.{pdf,png,tiff}
"""
import hashlib
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
OUT = PR / "graphical_abstracts"
OUT.mkdir(parents=True, exist_ok=True)
STEM = OUT / "graphical_abstract_p1"

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
# PANEL A — ONE NUMBER FROM MANY CAPITALS
# =====================================================================
head(218, "ONE NUMBER FROM MANY CAPITALS", "composite assessment practice", 396, 330)
caps = [("built", BLUE), ("financial", BLUE), ("natural A", FLOW), ("natural B", FLOW)]
cwid, chgt, cgap = 88, 42, 9
cx0 = 28 + (380 - (4 * cwid + 3 * cgap)) / 2
cyy = 330
for (name, col), i in zip(caps, range(4)):
    x = cx0 + i * (cwid + cgap)
    box(x, cyy, cwid, chgt, fc="#ffffff", ec=col, lw=1.4, r=8)
    txt(x + cwid / 2, cyy + chgt / 2, name, size=fit(name, cwid - 10, "bold", 7.0),
        color=DARK, weight="bold")
    arrow(x + cwid / 2, cyy - 4, 218 + (i - 1.5) * 26, 276, color=GREY, lw=1.3, ms=8)
box(118, 218, 200, 56, fc="#eef2f7", ec=DARK, lw=1.5)
ATTR.clear()
ATTR["one index \u2265 0"] = {"weight": "bold"}
ATTR["a surplus offsets a deficit"] = {"color": GREY}
vlines(218, 218, 200, 56, [("one index \u2265 0", 7.8),
                           ("a surplus offsets", 6.4),
                           ("a deficit", 6.4)])
box(28, 130, 380, 64, fc="#fbeaea", ec=STOCK, lw=1.4)
ATTR.clear()
ATTR["compensatory aggregation"] = {"weight": "bold", "color": STOCK}
ATTR["a deficit in one capital can hide"] = {"color": DARK}
ATTR["behind a surplus in another"] = {"color": DARK}
vlines(218, 130, 380, 64, [("compensatory aggregation", 7.2),
                           ("a deficit in one capital can hide", 6.4),
                           ("behind a surplus in another", 6.4)])
box(28, 94, 380, 32, fc="#ffffff", ec=GREY, lw=1.0, r=6)
txt(218, 110, "floors are typed, per moiety", size=fit("floors are typed, per moiety", 340, maxsize=6.4),
    color=GREY, style="italic")

# =====================================================================
# PANEL B — THE WITNESS
# =====================================================================
head(644, "THE WITNESS", "aggregate passes \u00b7 a floor fails", 400, 340)
chx, chy, chw, chh = 446, 170, 394, 212
box(chx, chy, chw, chh, fc="#ffffff", ec="#d8cfa8", lw=1.1, r=7, z=1)
ix0, iy0, iw, ih = chx + 90, chy + 24, chw - 120, chh - 88
zy = iy0 + ih * 0.58
ax.plot([ix0, ix0 + iw], [zy, zy], color=GREY, lw=1.0, ls=(0, (3, 2)), zorder=3)
bars = [(0.16, +0.38, FLOW), (0.44, +0.24, FLOW), (0.72, -0.52, STOCK)]
bwid = 0.13
for (xc, val, col) in bars:
    x = ix0 + xc * iw
    hgt = abs(val) * (ih * 0.66)
    y0 = zy if val > 0 else zy - hgt
    ax.add_patch(Rectangle((x - bwid * iw / 2, y0), bwid * iw, hgt,
                           facecolor=col, edgecolor="none", alpha=0.92, zorder=4))
txt(ix0 - 40, zy + 4, "0", size=7.0, color=GREY, ha="right")
txt(chx + chw / 2, chy + 14, "typed floors (schematic)",
    size=fit("typed floors (schematic)", chw - 30, maxsize=6.6),
    color=GREY, style="italic")
box(chx + 24, chy + chh - 62, chw - 48, 48, fc="#fff7e8", ec=ACCENT, lw=1.5)
ATTR.clear()
ATTR["aggregate floor \u2265 0"] = {"weight": "bold"}
ATTR["for every weight \u2265 0"] = {"color": ACCENT, "style": "italic"}
vlines(chx + chw / 2, chy + chh - 62, chw - 48, 48, [("aggregate floor \u2265 0", 8.0),
                                                     ("for every weight \u2265 0", 7.2)])
box(446, 96, 394, 66, fc="#f7fafd", ec=BLUE, lw=1.4)
ATTR.clear()
ATTR["on an explicit rational witness"] = {"weight": "bold", "color": BLUE}
ATTR["no single action keeps every"] = {"color": DARK}
ATTR["typed floor nonnegative"] = {"color": DARK}
vlines(643, 96, 394, 66, [("on an explicit rational witness", 7.0),
                          ("no single action keeps every", 6.4),
                          ("typed floor nonnegative", 6.4)])

# =====================================================================
# PANEL C — THE SEPARATION
# =====================================================================
head(1090, "THE SEPARATION", "V_weak \u2283 V_typ", 436, 350)
# nested acceptance sets
box(876, 176, 214, 204, fc="#fbeaea", ec=STOCK, lw=1.6, r=10, z=2)
box(902, 222, 162, 118, fc="#ffffff", ec=FLOW, lw=1.6, r=8, z=3)
ATTR.clear()
ATTR["V_weak"] = {"weight": "bold", "color": STOCK}
ATTR["aggregated"] = {"color": STOCK}
vlines(983, 340, 214, 36, [("V_weak", 7.8), ("aggregated", 6.4)])
ATTR.clear()
ATTR["V_typ"] = {"weight": "bold", "color": FLOW}
ATTR["typed"] = {"color": FLOW}
vlines(983, 268, 162, 30, [("V_typ", 7.4), ("typed", 6.2)])
txt(983, 208, "impossibility region", size=fit("impossibility region", 200, maxsize=6.4),
    color=STOCK, style="italic")
txt(983, 189, "FP_agg \u00b7 nonempty interior", size=fit("FP_agg \u00b7 nonempty interior", 214, maxsize=6.2),
    color=STOCK, style="italic")
# right callouts
calls = [
    ("bridging", "resource augmentation", "at a defined cost", 330, ACCENT, "#fff3e0"),
    ("convexification", "closes the gap on the", "compensatory region", 254, GREY, "#ffffff"),
]
for (t1, t2, t3, yy, col, bg) in calls:
    ATTR.clear()
    ATTR[t1] = {"weight": "bold", "color": DARK}
    ATTR[t2] = {"color": col}
    ATTR[t3] = {"color": col}
    box(1098, yy, 200, 62, fc=bg, ec=col, lw=1.4)
    vlines(1198, yy, 200, 62, [(t1, 7.2), (t2, 6.2), (t3, 6.2)])
box(876, 96, 422, 70, fc="#f0f4f8", ec="#c3d3e3", lw=1.4)
ATTR.clear()
ATTR["the separation is structural"] = {"weight": "bold"}
ATTR["not an artifact of weight choice"] = {"color": GREY, "style": "italic"}
vlines(1087, 96, 422, 70, [("the separation is structural", 7.2),
                           ("not an artifact of weight choice", 6.6),
                           ("\u2014 no reweighting repairs it", 6.6)])

txt(W / 2, 40, "The Limits of Compensatory Aggregation:",
    size=fit("The Limits of Compensatory Aggregation:", W - 40, "bold", 9.4),
    color=DARK, weight="bold")
txt(W / 2, 13, "A Formal Separation of Weak and Strong Sustainability Assessment",
    size=fit("A Formal Separation of Weak and Strong Sustainability Assessment",
             W - 40, "bold", 9.4), color=DARK, weight="bold")

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
