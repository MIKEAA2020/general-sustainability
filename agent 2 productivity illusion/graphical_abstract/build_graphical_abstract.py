#!/usr/bin/env python3
"""Graphical abstract for the 'productivity illusion' manuscript.

Single-row, three-panel narrative banner (landscape) at the journal's
graphical-abstract target size: 1328 x 531 px (0.40 h/w), 200 dpi.
  A  THE ORCHARD   : biocapacity = flow yield + stock increment
  B  THE COUPLING  : the delayed feedback loop, deficit switch, debt
  C  THE ILLUSION  : biocapacity rises while the stock falls; R_B = 1

Outputs: vector .pdf (journal), .png (online), .tiff (print).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle

W, H = 1328, 531
DPI = 200
fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H)
ax.axis("off")

FLOW   = "#1f8a4c"
STOCK  = "#b23a48"
DARK   = "#1f3a5f"
ACCENT = "#e0a458"
GREY   = "#5c6b73"
LIGHT  = "#f2f6f9"
BLUE   = "#3f7cac"
PURPLE = "#7d5ba6"

def box(x, y, w, h, fc=LIGHT, ec=DARK, lw=1.3, r=8, z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                linewidth=lw, edgecolor=ec, facecolor=fc, zorder=z))

def arrow(x1, y1, x2, y2, color=DARK, lw=1.5, style="-|>", rad=0.0, z=4, ms=9, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=ms,
                                 linewidth=lw, color=color, connectionstyle=f"arc3,rad={rad}",
                                 zorder=z, shrinkA=2, shrinkB=2, linestyle=ls))

def txt(x, y, s, size=6.0, color=DARK, weight="normal", ha="center", va="center",
        style="normal", z=6):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
            style=style, zorder=z, linespacing=1.2)

def header(cx, title, sub):
    txt(cx, 458, title, size=8.8, color=DARK, weight="bold")
    txt(cx, 441, sub, size=6.2, color=GREY, style="italic")

# ============================================================
# PANEL A — THE ORCHARD  (frame 6..430)
# ============================================================
ax.add_patch(Rectangle((6, 52), 424, 402, facecolor="#fbfdfc", edgecolor="#d6e2dc", lw=1.0, zorder=0))
header(218, "THE ORCHARD", "biocapacity is two things")

# tree (small, top-left)
def tree(x, base, s, z=6):
    ax.add_patch(Rectangle((x-5*s, base-26*s), 10*s, 30*s, facecolor="#7a4a23",
                           edgecolor="#5a3414", lw=0.7, zorder=z))
    for dx, dy, r in [(-15, 24, 19), (15, 24, 19), (0, 34, 21)]:
        ax.add_patch(Circle((x+dx*s, base+dy*s), r*s, facecolor=FLOW,
                            edgecolor="none", alpha=0.86, zorder=z))
tree(96, 250, s=1.7, z=6)

# flow box (upper right)
box(224, 300, 186, 44, fc="#e8f5ee", ec=FLOW, lw=1.2)
txt(317, 328, "flow yield  b·A", size=6.2, color=FLOW, weight="bold")
txt(317, 311, "(the fruit — base intact)", size=5.0, color=GREY)
arrow(140, 322, 220, 322, color=FLOW, lw=1.8)

# increment box (mid right)
box(224, 216, 186, 44, fc="#fbeaea", ec=STOCK, lw=1.2)
txt(317, 244, "stock increment  b_G·G(A)", size=6.2, color=STOCK, weight="bold")
txt(317, 227, "(the timber — cut the base)", size=5.0, color=GREY)
arrow(140, 238, 220, 238, color=STOCK, lw=1.8)

# equation box (bottom right)
box(224, 132, 186, 44, fc="#ffffff", ec=DARK, lw=1.2, r=7)
txt(317, 160, "B  =  b·A  +  b_G·G(A)", size=6.8, color=DARK, weight="bold")
txt(317, 143, "(flow + stock increment)", size=5.0, color=GREY)

# caveat (bottom, under tree, clear of tree)
txt(160, 84, "Take more than the regrowth,\nand you pay from the base.", size=6.0, color=STOCK, weight="bold")

# ============================================================
# PANEL B — THE COUPLING  (frame 442..856)
# ============================================================
ax.add_patch(Rectangle((442, 52), 414, 402, facecolor="#f7fafd", edgecolor="#d3e2ef", lw=1.0, zorder=0))
header(649, "THE COUPLING", "overshoot is paid from the base")

xs = [456, 584, 712]; bw = 116; bh = 44; row1 = 320
lbl1 = ["stock  A", "biocapacity  B", "carrying cap.\nK = B/e"]
for x, l in zip(xs, lbl1):
    box(x, row1, bw, bh)
    txt(x+bw/2, row1+bh/2, l, size=5.6, color=DARK, weight="bold")
arrow(xs[0]+bw, row1+bh/2, xs[1], row1+bh/2, color=BLUE, lw=1.5)
arrow(xs[1]+bw, row1+bh/2, xs[2], row1+bh/2, color=BLUE, lw=1.5)

row2 = 252
box(xs[2], row2, bw, bh)
txt(xs[2]+bw/2, row2+bh/2, "population  P", size=5.6, color=DARK, weight="bold")
arrow(xs[2]+bw/2, row1, xs[2]+bw/2, row2+bh, color=BLUE, lw=1.5)
box(xs[1], row2, bw, bh)
txt(xs[1]+bw/2, row2+bh/2, "footprint  E = eP", size=5.6, color=DARK, weight="bold")
arrow(xs[2], row2+bh/2, xs[1]+bw, row2+bh/2, color=BLUE, lw=1.5)

# deficit switch
sw_y = 176; sw_h = 36
box(xs[0], sw_y, bw+72, sw_h, fc="#fff7e8", ec=ACCENT, lw=1.3)
txt(xs[0]+(bw+72)/2, sw_y+26, "deficit switch", size=5.8, color=DARK, weight="bold")
txt(xs[0]+(bw+72)/2, sw_y+11, "if E > bA, liquidate stock", size=4.9, color=GREY)
arrow(xs[1]+bw/2, row2, xs[0]+(bw+72)/2, sw_y+sw_h, color=ACCENT, lw=1.4, ls=(0,(3,2)))

# debt
debt_y = 108; debt_h = 32
box(xs[0], debt_y, bw+72, debt_h, fc="#fbeaea", ec=STOCK, lw=1.3)
txt(xs[0]+(bw+72)/2, debt_y+22, "ecological debt  D", size=5.7, color=STOCK, weight="bold")
txt(xs[0]+(bw+72)/2, debt_y+8, "compounds; erodes yield", size=4.8, color=GREY)
arrow(xs[0]+(bw+72)/2, sw_y, xs[0]+(bw+72)/2, debt_y+debt_h, color=STOCK, lw=1.4)
arrow(xs[0]+(bw+72)/2, debt_y, xs[0]+bw/2, row1, color=STOCK, lw=1.5, rad=0.32)

# two delays (moved to top-right of panel B, clear of debt)
box(xs[1], 176, bw+72, 36, fc="#eef2f7", ec=GREY, lw=1.1)
txt(xs[1]+(bw+72)/2, 195, "two delays", size=5.7, color=DARK, weight="bold")
txt(xs[1]+(bw+72)/2, 181, "τ_g regen  ·  τ_p demo", size=4.9, color=GREY)

# ============================================================
# PANEL C — THE ILLUSION  (frame 868..1322)
# ============================================================
ax.add_patch(Rectangle((868, 52), 454, 402, facecolor="#fcfbf7", edgecolor="#e7e2d2", lw=1.0, zorder=0))
header(1095, "THE ILLUSION", "a healthy-looking harvest can mask decay")

# chart
sx, sy, sw, sh = 884, 246, 176, 148
tmax = 14.0
t = np.linspace(0, tmax, 500)
B = 1.00 + 0.145*np.exp(-((t-3.3)**2)/6.0) - 0.045*(t/tmax)**1.3
A = 1.00 - 0.34*(t/tmax)**1.12
box(sx-8, sy-8, sw+16, sh+18, fc="#ffffff", ec="#d8cfa8", lw=1.0, r=6, z=1)
ax.plot(sx + t/tmax*sw, sy + A*sh, color=STOCK, lw=2.1, zorder=5)
ax.plot(sx + t/tmax*sw, sy + B*sh, color=FLOW, lw=2.3, zorder=6)
lo = sx + 1.6/tmax*sw; wb = (6.6-1.6)/tmax*sw
ax.add_patch(Rectangle((lo, sy-6), wb, sh+12, facecolor=ACCENT, alpha=0.20, edgecolor="none", zorder=2))
txt(sx + sw*0.20, sy-24, "stock A  (falls)", size=5.6, color=STOCK, weight="bold")
txt(sx + sw*0.74, sy+sh+24, "biocapacity B  (rises)", size=5.6, color=FLOW, weight="bold")
txt(sx + sw*0.72, sy+sh-12, "'mask' \u2248 5 yr", size=5.5, color=ACCENT, weight="bold")

# right badges (fit inside panel frame 868..1322 with margin)
bx0 = 1096; bw2 = 212
box(bx0, 374, bw2, 38, fc="#eaf1f7", ec=BLUE, lw=1.3)
txt(bx0+bw2/2, 396, "Operating boundary:", size=5.6, color=DARK, weight="bold")
txt(bx0+bw2/2, 381, "R_B = 1  (footprint = total biocapacity)", size=4.8, color=DARK)
box(bx0, 328, bw2, 38, fc="#ffffff", ec=BLUE, lw=1.1)
txt(bx0+bw2/2, 349, "R_A = 1  (flow-only)", size=5.5, color=GREY)
txt(bx0+bw2/2, 334, "leading signal, not the trigger", size=4.7, color=GREY)
box(bx0, 282, bw2, 38, fc="#fff3e6", ec=ACCENT, lw=1.2)
txt(bx0+bw2/2, 302, "long τ_g — neither warns", size=5.5, color=DARK, weight="bold")
txt(bx0+bw2/2, 288, "(silent collapse)", size=4.7, color=GREY)
box(bx0, 236, bw2, 36, fc=STOCK, ec="none", r=7)
txt(bx0+bw2/2, 254, "Rising biocapacity \u2260", size=5.6, color="#ffffff", weight="bold")
txt(bx0+bw2/2, 241, "improving health", size=5.6, color="#ffffff", weight="bold")

# takeaway
txt(1095, 190, "The decisive lever is the regeneration delay;", size=5.8, color=DARK, weight="bold")
txt(1095, 174, "no early warning or rescue-by-stock exists.", size=5.8, color=DARK, weight="bold")
txt(1095, 154, "Structural decline needs no oscillatory trigger.", size=5.4, color=GREY, style="italic")

# ---------------- title strip ----------------
txt(W/2, 26, "The productivity illusion: emergent carrying capacity in a delayed coupled human–environment model",
    size=8.0, color=DARK, weight="bold")

plt.savefig("graphical_abstract.pdf", dpi=DPI, facecolor="white")
plt.savefig("graphical_abstract.png", dpi=DPI, facecolor="white")
plt.savefig("graphical_abstract.tiff", dpi=DPI, facecolor="white", format="tiff")
print("wrote graphical_abstract.pdf / .png / .tiff")
print("print size cm:", round(W/DPI*2.54, 2), "x", round(H/DPI*2.54, 2))
