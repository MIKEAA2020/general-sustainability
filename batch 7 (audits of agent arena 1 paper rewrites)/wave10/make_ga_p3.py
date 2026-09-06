#!/usr/bin/env python3
"""Graphical abstract for paper3_material_ledgers (latest v31).

House style: 3-panel banner, 1328 x 531 px (h x w), 200 dpi PNG,
400 dpi TIFF (2656 x 1062, "proportionally more"), vector PDF.
Sizing discipline (audited programmatically): 1 pt = DPI/72 = 2.78 px, so
every stacked-line pair is placed with centre separation >= half-heights
plus padding; every string is short enough that fit() never bottoms out.
Every number is the paper's registered value; nothing is invented.
  A  ONE LABEL, THREE NUMBERS : the three "time to depletion" quantities
  B  THE TYPED LEDGER         : per-moiety compartments, conservation from
                                incidence, positivity from donor limitation
  C  NO WEIGHT HIDES A DEFICIT: the noncompensation obstruction, b*M >= 0
Wave-11 root-cause fix inherited from the owner's E2 feedback: the
vlines stacker drew every multi-line box's list bottom-to-top, so all
boxes rendered in reverse reading order (bold headline at the bottom);
vlines now renders lists in reading order (headline on top, the ECOMOD
house convention; stack geometry unchanged). No other change to this
generator.
Outputs: graphical_abstracts/graphical_abstract_p3.{pdf,png,tiff}
Run twice to pin the MD5s.
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
STEM = OUT / "graphical_abstract_p3"

W, H = 1328, 531
DPI = 200
PX = DPI / 72.0          # px per pt
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

def vlines(x, ybot, w, h, lines):
    """Place 1-4 stacked centred lines inside box (x, ybot, w, h).
    Each line is auto-fitted to width (w-14); stack clearance is computed
    from the fitted sizes (1pt = PX px, 3px inter-line gaps)."""
    # wave-11 root-cause fix: the wave-10 stacker drew the list bottom-to-top,
    # so every multi-line box rendered in REVERSE reading order (the root cause
    # of the owner-flagged E2 text). Reverse here so the list's first line
    # renders at the TOP; the stack geometry is unchanged (same slots).
    lines = list(reversed(lines))
    n = len(lines)
    fitted = []
    for (s, sz) in lines:
        fsz = fit(s, w - 14, lines_weight(s), sz)
        fitted.append((s, fsz))
    halves = [fsz * PX / 2 for (_, fsz) in fitted]
    total = 2 * sum(halves) + 3.0 * (n - 1)
    y = ybot + (h - total) / 2
    for (s, fsz), hh in zip(fitted, halves):
        txt(x, y + hh, s, size=fsz, color=lines_color(s),
            weight=lines_weight(s), style=lines_style(s))
        y += 2 * hh + 3.0

# per-line attribute lookup by string
ATTR = {}
def lines_color(s): return ATTR.get(s, {}).get("color", DARK)
def lines_weight(s): return ATTR.get(s, {}).get("weight", "normal")
def lines_style(s): return ATTR.get(s, {}).get("style", "normal")

def head(cx, t, sub, tw, subw):
    txt(cx, 453, t, size=fit(t, tw, "bold", 10.2), color=DARK, weight="bold")
    txt(cx, 424, sub, size=fit(sub, subw, maxsize=8.0), color=GREY, style="italic")

# ----------------------------- panel frames -----------------------------
for (x0, w, fc, ec) in [(10, 416, "#fbfdfc", "#d6e2dc"),
                        (434, 420, "#f7fafd", "#d3e2ef"),
                        (862, 456, "#fcfbf7", "#e7e2d2")]:
    ax.add_patch(Rectangle((x0, 58), w, 400, facecolor=fc, edgecolor=ec, lw=1.0, zorder=0))

# =====================================================================
# PANEL A — ONE LABEL, THREE NUMBERS
# =====================================================================
head(218, "ONE LABEL, THREE NUMBERS", "each reads as \u201ctime to depletion\u201d", 396, 330)
rows = [
    ("reserve-life ratio", "reserves \u00f7 production",
     "arithmetic \u2014 not a forecast", STOCK, "#fbeaea"),
    ("trend index", "a fitted trend vs its own minimum",
     "an index \u2014 not a stock ratio", BLUE, "#eaf1f7"),
    ("removals-only time", "log margin \u00f7 mortality",
     "a pressure scale \u2014 not depletion", ACCENT, "#fff3e0"),
]
bx, bw = 28, 380
ys = [312, 204, 96]
for (t1, t2, t3, col, bg), y in zip(rows, ys):
    ATTR.clear()
    ATTR[t1] = {"weight": "bold", "color": DARK}
    ATTR[t2] = {"color": DARK}
    ATTR[t3] = {"color": col, "style": "italic"}
    box(bx, y, bw, 88, fc=bg, ec=col, lw=1.5)
    vlines(bx + bw / 2, y, bw, 88, [(t1, 9.0), (t2, 7.4), (t3, 7.4)])
box(bx, 64, bw, 26, fc="#ffffff", ec="#d6e2dc", lw=1.0, r=6)
txt(bx + bw / 2, 77, "public data: G3P \u00b7 USGS \u00b7 RAM",
    size=fit("public data: G3P \u00b7 USGS \u00b7 RAM", bw - 14, maxsize=7.4), color=GREY)

# =====================================================================
# PANEL B — THE TYPED LEDGER
# =====================================================================
head(644, "THE TYPED LEDGER", "each moiety in its own currency", 400, 340)
comps = [("biomass", FLOW, "#e7f4ec"), ("funds", BLUE, "#eaf1f7"), ("biodiversity", ACCENT, "#fff3e0")]
cw, chh2, gap = 122, 52, 12
cx0 = 434 + (420 - (3 * cw + 2 * gap)) / 2
cy = 336
for (name, col, bg), i in zip(comps, range(3)):
    x = cx0 + i * (cw + gap)
    box(x, cy, cw, chh2, fc=bg, ec=col, lw=1.5)
    txt(x + cw / 2, cy + chh2 / 2, name, size=fit(name, cw - 12, "bold", 8.4),
        color=DARK, weight="bold")
for i in range(2):
    x1 = cx0 + (i + 1) * cw + i * gap
    arrow(x1 + 1, cy + chh2 / 2, x1 + gap - 1, cy + chh2 / 2, color=GREY, lw=1.6, ms=9)
txt(644, 314, "typed fluxes \u2014 never summed",
    size=fit("typed fluxes \u2014 never summed", 380, maxsize=7.4), color=GREY, style="italic")
props = [("conservation", "from the incidence structure"),
         ("positivity", "outflows vanish with their donor"),
         ("services", "readouts, not conserved mass")]
py = 252
for (t1, t2) in props:
    ATTR.clear()
    ATTR[t1] = {"weight": "bold"}
    box(446, py, 396, 48, fc="#ffffff", ec=DARK, lw=1.2, r=8)
    vlines(644, py, 396, 48, [(t1, 8.2), (t2, 7.4)])
    py -= 58
ATTR.clear()
box(446, 78, 396, 52, fc="#eef2f7", ec="#c3d3e3", lw=1.2)
ATTR["three depletion times, not one"] = {"weight": "bold"}
vlines(644, 78, 396, 52, [("three depletion times, not one", 7.8),
                          ("turnover \u00b7 frozen rate \u00b7 hitting time", 7.2)])

# =====================================================================
# PANEL C — NO WEIGHT HIDES A DEFICIT
# =====================================================================
head(1090, "NO WEIGHT HIDES A DEFICIT", "the vector carries the certificate", 436, 350)
chx, chy, chw, chh = 876, 208, 422, 172
box(chx, chy, chw, chh, fc="#ffffff", ec="#d8cfa8", lw=1.1, r=7, z=1)
# bubble (top, inside chart)
box(1000, 316, 284, 52, fc="#fff7e8", ec=ACCENT, lw=1.5)
ATTR.clear()
ATTR["weighted aggregate \u2265 0"] = {"weight": "bold"}
ATTR["for every weight \u2265 0"] = {"color": ACCENT, "style": "italic"}
vlines(1142, 316, 284, 52, [("weighted aggregate \u2265 0", 7.6),
                            ("for every weight \u2265 0", 7.0)])
# bars (schematic typed floors)
ix0, iw = 930, 320
zy = 252
ax.plot([ix0, ix0 + iw], [zy, zy], color=GREY, lw=1.0, ls=(0, (3, 2)), zorder=3)
bars = [(0.22, +0.36, FLOW), (0.50, +0.22, FLOW), (0.78, -0.46, STOCK)]
bwid = 0.10
for (xc, val, col) in bars:
    x = ix0 + xc * iw
    hgt = abs(val) * 100
    y0 = zy if val > 0 else zy - hgt
    ax.add_patch(Rectangle((x - bwid * iw / 2, y0), bwid * iw, hgt,
                           facecolor=col, edgecolor="none", alpha=0.92, zorder=4))
txt(ix0 - 24, zy + 4, "0", size=7.0, color=GREY, ha="right")
txt(930, 216, "typed floors", size=6.6, color=GREY, ha="left", style="italic")
# callout row
calls = [("componentwise", "one floor fails", STOCK, "#fbeaea", 876),
         ("double counting", "no phantom mass", GREY, "#eef2f7", 1093)]
for (t1, t2, col, bg, x) in calls:
    ATTR.clear()
    ATTR[t1] = {"weight": "bold"}
    ATTR[t2] = {"color": col}
    box(x, 128, 205, 66, fc=bg, ec=col, lw=1.4)
    vlines(x + 102, 128, 205, 66, [(t1, 7.6), (t2, 6.8)])
# takeaway bar
box(876, 60, 422, 64, fc="#f0f4f8", ec="#c3d3e3", lw=1.4)
ATTR.clear()
ATTR["no weighting certifies all floors"] = {"weight": "bold"}
ATTR["each claim carries its own predicate"] = {"color": GREY, "style": "italic"}
vlines(1087, 60, 422, 64, [("no weighting certifies all floors", 7.0),
                           ("an aggregate \u2265 0 is not each floor \u2265 0", 6.6),
                           ("each claim carries its own predicate", 6.6)])

txt(W / 2, 40, "Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise",
    size=fit("Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise",
             W - 40, "bold", 9.0), color=DARK, weight="bold")
txt(W / 2, 13, "Diagnostics, and the Semantics of Depletion Horizons",
    size=fit("Diagnostics, and the Semantics of Depletion Horizons", W - 40, "bold", 9.0),
    color=DARK, weight="bold")

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
