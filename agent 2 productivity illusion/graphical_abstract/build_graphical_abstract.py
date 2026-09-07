#!/usr/bin/env python3
"""Graphical abstract — two-land composition illusion (v34).

3-panel banner, 1328 x 531 px (h/w 0.40), 200 dpi. Every box sits on a
non-overlapping grid and every string auto-fits its box.

  A  THE TWO BOOKS   : fast provisioning land (A_f) vs ecological capital land (A_c),
                       linked by conversion u_c; B = b_f A_f + Upsilon_c A_c
  B  THE COUPLING    : A_f, A_c -> B -> K -> P -> E -> deficit S -> conversion/debt/delays
  C  THE COMPOSITION ILLUSION : B rises while A_c falls (needs b_f > b_c,eff); driven to
                       a typed floor (floor collision, not a fold); no critical slowing;
                       recovery needs a gated restoration flow; composition step not
                       identifiable from the aggregate alone.

Outputs: .pdf (vector), .png (online), .tiff (print).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle

W, H = 1328, 531
DPI = 200
fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
fig.canvas.draw(); RENDER = fig.canvas.get_renderer()

FLOW, STOCK, DARK, ACCENT = "#1f8a4c", "#b23a48", "#1f3a5f", "#e0a458"
GREY, BLUE = "#5c6b73", "#3f7cac"


def meas(s, size, weight="normal"):
    t = ax.text(0, 0, s, fontsize=size, fontweight=weight)
    bb = t.get_window_extent(RENDER); t.remove()
    return bb.width


def fit(s, maxw, weight="normal", maxsize=7.0, minsize=3.6):
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


def txt(x, y, s, size=6.6, color=DARK, weight="normal", ha="center", va="center",
        z=8, style="normal"):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
            style=style, zorder=z, linespacing=1.12)


def head(cx, t, sub, subw):
    txt(cx, 452, t, size=fit(t, 250, "bold", 9.6), color=DARK, weight="bold")
    txt(cx, 431, sub, size=fit(sub, subw), color=GREY, style="italic")


# ----------------------------- panel frames -----------------------------
for (x0, w, fc, ec) in [(10, 416, "#fbfdfc", "#d6e2dc"),
                        (434, 420, "#f7fafd", "#d3e2ef"),
                        (862, 456, "#fcfbf7", "#e7e2d2")]:
    ax.add_patch(Rectangle((x0, 58), w, 400, facecolor=fc, edgecolor=ec, lw=1.0, zorder=0))

# =====================================================================
# PANEL A — THE TWO BOOKS
# =====================================================================
head(218, "THE TWO BOOKS", "two kinds of ground \u00b7 B adds them", 320)


def book(cx, by, w, h, title, sub, sub2, fc, ec):
    box(cx, by, w, h, fc=fc, ec=ec, lw=1.6)
    txt(cx + w / 2, by + h - 16, title, size=fit(title, w - 14, "bold", 7.4), color=ec, weight="bold")
    txt(cx + w / 2, by + h / 2 - 6, sub, size=fit(sub, w - 14), color=DARK)
    txt(cx + w / 2, by + 12, sub2, size=fit(sub2, w - 14), color=GREY)


bw, bh, bx = 206, 76, 116
by = 330
book(bx, by, bw, bh, "FAST PROVISION A_f", "b_f · A_f  ·  high yield, quick", "small standing value", "#e7f4ec", FLOW)
by = 214
book(bx, by, bw, bh, "ECOLOGICAL CAPITAL A_c", "\u03a5_c · A_c, big standing value", "b_c + b_G G_c(q)", "#fbeaea", STOCK)
arrow(bx + bw / 2, 290, bx + bw / 2, 330, color=STOCK, lw=2.0)
txt(bx + bw / 2 + 26, 310, "conversion u_c · A_c\u2193 A_f\u2191", size=fit("conversion u_c · A_c\u2193 A_f\u2191", 150, "bold", 6.2), color=STOCK, weight="bold", ha="left")
# B node
box(bx, 120, bw, 70, fc="#ffffff", ec=BLUE, lw=1.6)
txt(bx + bw / 2, 172, "BIOCAPACITY B", size=fit("BIOCAPACITY B", bw - 14, "bold", 7.4), color=BLUE, weight="bold")
txt(bx + bw / 2, 146, "= b_f A_f + \u03a5_c A_c", size=fit("= b_f A_f + \u03a5_c A_c", bw - 14, "bold", 6.6), color=DARK, weight="bold")
txt(bx + bw / 2, 128, "area conserved; capacity a state", size=fit("area conserved; capacity a state", bw - 14), color=GREY)
arrow(bx + bw, 330 + bh / 2, bx + bw + 52, 330 + bh / 2, color=FLOW, lw=1.8)
arrow(bx + bw, 214 + bh / 2, bx + bw + 52, 214 + bh / 2, color=STOCK, lw=1.8)
# composition condition note
box(20, 62, 396, 46, fc="#fff8e8", ec=ACCENT, lw=1.4)
txt(218, 92, "composition condition:  b_f \u2212 b_c,eff > 0", size=fit("composition condition:  b_f \u2212 b_c,eff > 0", 372, "bold", 6.8), color="#8a5b00", weight="bold")
txt(218, 72, "\u21d2 converting A_c into A_f raises B", size=fit("\u21d2 converting A_c into A_f raises B", 372, "bold", 6.4), color=DARK, weight="bold")

# =====================================================================
# PANEL B — THE COUPLING (loop + composition)
# =====================================================================
head(644, "THE COUPLING", "loop, deficit switch, debt, delays", 330)
nw, nh = 104, 42
def node(cx, cy, lbl, fc="#ffffff", ec=DARK, size=6.0):
    box(cx - nw / 2, cy - nh / 2, nw, nh, fc=fc, ec=ec, lw=1.3, r=8)
    txt(cx, cy, lbl, size=fit(lbl, nw - 10, "bold", size), color=DARK, weight="bold")

L, M, Rb = 512, 644, 776
r1, r2 = 300, 200
node(L, r1, "A_f \u00b7 A_c")
node(M, r1, "B = b_fA_f+\u03a5_cA_c", size=5.4)
node(Rb, r1, "carrying  K")
node(Rb, r2, "population  P")
node(M, r2, "footprint  E")
node(L, r2, "deficit  S")
arrow(L + nw / 2, r1, M - nw / 2, r1, color=BLUE, lw=1.7)
arrow(M + nw / 2, r1, Rb - nw / 2, r1, color=BLUE, lw=1.7)
arrow(Rb, r1 - nh / 2, Rb, r2 + nh / 2, color=BLUE, lw=1.7)
arrow(Rb - nw / 2, r2, M + nw / 2, r2, color=BLUE, lw=1.7)
arrow(M - nw / 2, r2, L + nw / 2, r2, color=DARK, lw=1.7)
# deficit -> conversion (back up to books) and -> debt
arrow(L, r2 - nh / 2, L, r1 + nh / 2, color=ACCENT, lw=1.9, ls=(0, (3, 2)))
txt(L + nw / 2 + 8, (r1 + r2) / 2, "u_c>R_fc \u21d2 A_c\u2193", size=fit("u_c>R_fc \u21d2 A_c\u2193", 96, "bold", 6.0),
    color=ACCENT, weight="bold", ha="left")
# dynamics strip
strip = [("two delays", "regeneration & demography", GREY, "#eef2f7"),
         ("ecological debt", "erodes the flow yield", STOCK, "#fbeaea"),
         ("restoration", "R_rc; gate sign", BLUE, "#eaf1f7")]
sw, sh, sgap = 118, 46, 18
strip_y = 78
scx = [440 + sw / 2 + i * (sw + sgap) for i in range(3)]
for (tt, sub, col, bg2), sx in zip(strip, scx):
    box(sx - sw / 2, strip_y, sw, sh, fc=bg2, ec=col, lw=1.4, r=8)
    txt(sx, strip_y + sh - 13, tt, size=fit(tt, sw - 10, "bold", 6.4), color=DARK, weight="bold")
    txt(sx, strip_y + 11, sub, size=fit(sub, sw - 10), color=col)
arrow(L, r2 - nh / 2, scx[0], strip_y + sh, color=GREY, lw=1.4, ls=(0, (3, 2)), rad=-0.12)
arrow(scx[0] + sw / 2, strip_y + sh / 2, scx[1] - sw / 2, strip_y + sh / 2, color=STOCK, lw=1.5, ls=(0, (3, 2)))
arrow(scx[1] + sw / 2, strip_y + sh / 2, scx[2] - sw / 2, strip_y + sh / 2, color=BLUE, lw=1.5, ls=(0, (3, 2)))
arrow(scx[2], strip_y + sh, Rb, r2 - nh / 2, color=BLUE, lw=1.4, ls=(0, (3, 2)), rad=0.0)

# =====================================================================
# PANEL C — THE COMPOSITION ILLUSION
# =====================================================================
head(1090, "THE COMPOSITION ILLUSION", "B up while A_c down", 300)
cax, cay, caw, cah = 876, 150, 196, 200
box(cax, cay, caw, cah, fc="#ffffff", ec="#d8cfa8", lw=1.1, r=7, z=1)
ix0, iy0, iw, ih = cax + 24, cay + 20, caw - 48, cah - 40
tmax = 14.0
t = np.linspace(0, tmax, 400)
B = 1.00 + 0.16 * np.exp(-((t - 3.4) ** 2) / 6.0) - 0.03 * (t / tmax) ** 1.4
Ac = 1.00 - 0.36 * (t / tmax) ** 1.05
ax.plot(ix0 + t / tmax * iw, iy0 + Ac * ih, color=STOCK, lw=2.5, zorder=4)
ax.plot(ix0 + t / tmax * iw, iy0 + B * ih, color=FLOW, lw=2.7, zorder=5)
lo = ix0 + 1.6 / tmax * iw; wb = (6.8 - 1.6) / tmax * iw
ax.add_patch(Rectangle((lo, iy0 - 6), wb, ih + 12, facecolor=ACCENT, alpha=0.22,
                       edgecolor="none", zorder=2))
txt(lo + wb / 2, iy0 + 24, "mask", size=fit("mask", wb + 26, "bold", 6.2), color=ACCENT, weight="bold")
txt(cax + caw - 6, cay + cah - 10, "B  (rises)", size=fit("B  (rises)", caw - 14, "bold", 6.0),
    color=FLOW, weight="bold", ha="right")
txt(cax + caw - 6, cay + 12, "A_c  (falls)", size=fit("A_c  (falls)", caw - 14, "bold", 6.0),
    color=STOCK, weight="bold", ha="right")
# callout stack
bx0, bw2 = 1084, 214
calls = [("B\u2191 while A_c\u2193", "the composition illusion", FLOW, "#eaf5ee"),
         ("demand>E_ceil\u22481.14", "A_c \u2192 typed floor (floor collision, not a fold)", STOCK, "#fbeaea"),
         ("no critical slowing", "leader stays \u2248 \u22120.054 yr\u207b\u00b9", ACCENT, "#fff3e6")]
ys = [318, 260, 202]
for (t1, t2, col, bg2), yy in zip(calls, ys):
    box(bx0, yy, bw2, 46, fc=bg2, ec=col, lw=1.4, r=8)
    txt(bx0 + bw2 / 2, yy + 31, t1, size=fit(t1, bw2 - 14, "bold", 6.8), color=DARK, weight="bold")
    txt(bx0 + bw2 / 2, yy + 12, t2, size=fit(t2, bw2 - 14), color=GREY)
box(bx0, 144, bw2, 46, fc=BLUE, ec="none", r=10)
txt(bx0 + bw2 / 2, 175, "composition step", size=fit("composition step", bw2 - 14, "bold", 6.8),
    color="#ffffff", weight="bold")
txt(bx0 + bw2 / 2, 155, "NOT identifiable from B alone", size=fit("NOT identifiable from B alone", bw2 - 14, "bold", 6.6),
    color="#ffffff", weight="bold")
# takeaway bar
box(876, 92, 422, 44, fc="#f0f4f8", ec="#c3d3e3", lw=1.3)
txt(1087, 124, "Recovery needs a gated restoration flow;", size=fit("Recovery needs a gated restoration flow;", 404, "bold", 6.4),
    color=DARK, weight="bold")
txt(1087, 104, "the collapse trigger is demand, not a delay.", size=fit("the collapse trigger is demand, not a delay.", 404),
    color=DARK)

txt(W / 2, 26, "Emergent Carrying Capacity and the Composition Illusion: Two-Land Conversion and the Identifiability of Collapse",
    size=fit("Emergent Carrying Capacity and the Composition Illusion: Two-Land Conversion and the Identifiability of Collapse",
             W - 40, "bold", 8.2), color=DARK, weight="bold")

for ext, fmt in [("pdf", "pdf"), ("png", "png"), ("tiff", "tiff")]:
    plt.savefig(f"graphical_abstract.{ext}", dpi=DPI, facecolor="white", format=fmt)
print("ok  print cm:", round(W / DPI * 2.54, 2), "x", round(H / DPI * 2.54, 2))
