#!/usr/bin/env python3
"""Graphical abstract — deficit-driven collapse in a delayed coupled model.
3-panel banner, 1328 x 531 px (h/w 0.40), 200 dpi.
Every box sits on a non-overlapping grid and every string auto-fits its box, so
nothing overlaps or overflows.
  A  THE ORCHARD   : flow = biocapacity ; stock = capital that generates it
  B  THE COUPLING  : linear causal loop + feedback, deficit switch, debt, delays
  C  THE ILLUSION  : biocapacity rises while stock falls; R_B = 1
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
    txt(cx, 452, t, size=fit(t, 240, "bold", 9.6), color=DARK, weight="bold")
    txt(cx, 431, sub, size=fit(sub, subw), color=GREY, style="italic")
def tree(x, base, s, z=6):
    ax.add_patch(Rectangle((x-5*s, base-28*s), 10*s, 34*s, facecolor="#7a4a23",
                           edgecolor="#5a3414", lw=0.8, zorder=z))
    for dx, dy, r in [(-16, 26, 19), (16, 26, 19), (0, 35, 21)]:
        ax.add_patch(Circle((x+dx*s, base+dy*s), r*s, facecolor=FLOW,
                            edgecolor="none", alpha=0.88, zorder=z))

# ----------------------------- panel frames -----------------------------
for (x0, w, fc, ec) in [(10, 416, "#fbfdfc", "#d6e2dc"),
                        (434, 420, "#f7fafd", "#d3e2ef"),
                        (862, 456, "#fcfbf7", "#e7e2d2")]:
    ax.add_patch(Rectangle((x0, 58), w, 400, facecolor=fc, edgecolor=ec, lw=1.0, zorder=0))

# =====================================================================
# PANEL A — THE ORCHARD
# =====================================================================
head(218, "THE ORCHARD", "flow = biocapacity  \u00b7  stock = capital", 340)
tree(72, 188, s=1.7, z=6)
acx, aw = 244, 178
by = 338
box(acx, by, aw, 66, fc="#e7f4ec", ec=FLOW, lw=1.6)
txt(acx+aw/2, by+50, "FLOW", size=fit("FLOW", aw-16, "bold", 7.4), color=FLOW, weight="bold")
txt(acx+aw/2, by+25, "the fruit = biocapacity", size=fit("the fruit = biocapacity", aw-14), color=FLOW)
txt(acx+aw/2, by+7, "harvested, base intact", size=fit("harvested, base intact", aw-14), color=GREY)
by = 232
box(acx, by, aw, 66, fc="#fbeaea", ec=STOCK, lw=1.6)
txt(acx+aw/2, by+50, "STOCK", size=fit("STOCK", aw-16, "bold", 7.4), color=STOCK, weight="bold")
txt(acx+aw/2, by+25, "the trees = capital", size=fit("the trees = capital", aw-14), color=STOCK)
txt(acx+aw/2, by+7, "generates the flow", size=fit("generates the flow", aw-14), color=GREY)
by = 126
box(acx, by, aw, 66, fc="#ffffff", ec=DARK, lw=1.4)
txt(acx+aw/2, by+50, "liquidation", size=fit("liquidation", aw-16, "bold", 7.4), color=STOCK, weight="bold")
txt(acx+aw/2, by+25, "cut stock faster than it regrows", size=fit("cut stock faster than it regrows", aw-14), color=DARK)
txt(acx+aw/2, by+7, "\u2192 reduces future biocapacity", size=fit("\u2192 reduces future biocapacity", aw-14), color=DARK)
arrow(150, 371, acx-6, 371, color=FLOW, lw=2.2)
arrow(150, 265, acx-6, 265, color=STOCK, lw=2.2)
arrow(acx+aw/2, 232, acx+aw/2, 192, color=STOCK, lw=1.8)

# =====================================================================
# PANEL B — THE COUPLING (linear causal loop + feedback + dynamics)
# =====================================================================
head(644, "THE COUPLING", "overshoot is paid from the capital", 320)
nw, nh = 118, 44
L, M, R = 503, 644, 785
r1, r2 = 300, 196
def node(cx, cy, lbl, fc="#ffffff", ec=DARK):
    box(cx-nw/2, cy-nh/2, nw, nh, fc=fc, ec=ec, lw=1.3, r=8)
    txt(cx, cy, lbl, size=fit(lbl, nw-12, "bold", 6.2), color=DARK, weight="bold")
node(L, r1, "stock  A")
node(M, r1, "biocapacity  B")
node(R, r1, "carrying  K")
node(R, r2, "population  P")
node(M, r2, "footprint  E")
# main causal chain (solid)
arrow(L+nw/2, r1, M-nw/2, r1, color=BLUE, lw=1.7)                       # A -> B
arrow(M+nw/2, r1, R-nw/2, r1, color=BLUE, lw=1.7)                       # B -> K
arrow(R, r1-nh/2, R, r2+nh/2, color=BLUE, lw=1.7)                       # K -> P
arrow(R-nw/2, r2, M+nw/2, r2, color=BLUE, lw=1.7)                       # P -> E
# feedback: footprint -> stock
arrow(M, r2+nh/2, L, r1-nh/2, color=DARK, lw=1.7, ls=(0, (3, 2)), rad=0.0)
# dynamics strip (bottom)
strip = [("deficit switch", "if E > flow", ACCENT, "#fff7e8"),
         ("ecological debt", "compounds, erodes yield", STOCK, "#fbeaea"),
         ("two delays", "\u03c4_g \u00b7 \u03c4_p", GREY, "#eef2f7")]
sw, sh, sgap = 118, 50, 20
strip_y = 76
scx = [440+sw/2+i*(sw+sgap) for i in range(3)]
for (tt, sub, col, bg2), sx in zip(strip, scx):
    box(sx-sw/2, strip_y, sw, sh, fc=bg2, ec=col, lw=1.4, r=8)
    txt(sx, strip_y+sh-14, tt, size=fit(tt, sw-12, "bold", 6.4), color=DARK, weight="bold")
    txt(sx, strip_y+12, sub, size=fit(sub, sw-12), color=col)
arrow(M, r2-nh/2, scx[0], strip_y+sh, color=ACCENT, lw=1.5, ls=(0, (3, 2)), rad=-0.15)  # E -> deficit
arrow(scx[0]+sw/2, strip_y+sh/2, scx[1]-sw/2, strip_y+sh/2, color=STOCK, lw=1.5, ls=(0, (3, 2)))  # deficit -> debt
arrow(scx[2], strip_y+sh, R, r2-nh/2, color=GREY, lw=1.4, ls=(0, (3, 2)), rad=0.0)  # delays -> population

# =====================================================================
# PANEL C — THE ILLUSION
# =====================================================================
head(1090, "THE ILLUSION", "a shrinking stock can look healthy", 300)
carx, cary, carw, carh = 876, 152, 196, 200
box(carx, cary, carw, carh, fc="#ffffff", ec="#d8cfa8", lw=1.1, r=7, z=1)
ix0, iy0, iw, ih = carx+24, cary+20, carw-48, carh-40
tmax = 14.0
t = np.linspace(0, tmax, 400)
B = 1.00 + 0.145*np.exp(-((t-3.3)**2)/6.0) - 0.045*(t/tmax)**1.3
A = 1.00 - 0.34*(t/tmax)**1.12
ax.plot(ix0 + t/tmax*iw, iy0 + A*ih, color=STOCK, lw=2.4, zorder=4)
ax.plot(ix0 + t/tmax*iw, iy0 + B*ih, color=FLOW, lw=2.6, zorder=5)
lo = ix0 + 1.6/tmax*iw; wb = (6.6-1.6)/tmax*iw
ax.add_patch(Rectangle((lo, iy0-6), wb, ih+12, facecolor=ACCENT, alpha=0.22,
                       edgecolor="none", zorder=2))
txt(lo+wb/2, iy0+26, "'mask' \u2248 5 yr", size=fit("'mask' \u2248 5 yr", wb+24, "bold", 6.0),
    color=ACCENT, weight="bold")
txt(carx+carw-6, cary+carh-10, "B  (rises)", size=fit("B  (rises)", carw-14, "bold", 6.0),
    color=FLOW, weight="bold", ha="right")
txt(carx+carw-6, cary+12, "A  (falls)", size=fit("A  (falls)", carw-14, "bold", 6.0),
    color=STOCK, weight="bold", ha="right")
# callout stack (right)
bx0, bw2 = 1084, 214
calls = [("R_B = 1", "operating boundary", BLUE, "#eaf1f7"),
         ("R_A = 1", "leading, non-causal signal", GREY, "#ffffff"),
         ("long \u03c4_g \u2014 neither warns", "silent collapse", ACCENT, "#fff3e6")]
ys = [312, 254, 196]
for (t1, t2, col, bg2), yy in zip(calls, ys):
    box(bx0, yy, bw2, 46, fc=bg2, ec=col, lw=1.4, r=8)
    txt(bx0+bw2/2, yy+31, t1, size=fit(t1, bw2-14, "bold", 6.8), color=DARK, weight="bold")
    txt(bx0+bw2/2, yy+11, t2, size=fit(t2, bw2-14), color=GREY)
box(bx0, 138, bw2, 46, fc=STOCK, ec="none", r=10)
txt(bx0+bw2/2, 169, "Rising biocapacity", size=fit("Rising biocapacity", bw2-14, "bold", 6.8),
    color="#ffffff", weight="bold")
txt(bx0+bw2/2, 149, "\u2260 improving health", size=fit("\u2260 improving health", bw2-14, "bold", 6.8),
    color="#ffffff", weight="bold")
# takeaway bar
box(876, 92, 422, 44, fc="#f0f4f8", ec="#c3d3e3", lw=1.3)
txt(1087, 124, "The decisive lever is the regeneration delay;", size=fit("The decisive lever is the regeneration delay;", 404, "bold", 6.4),
    color=DARK, weight="bold")
txt(1087, 104, "no early-warning signal or rescue-by-stock exists.", size=fit("no early-warning signal or rescue-by-stock exists.", 404),
    color=DARK)

txt(W/2, 26, "Emergent carrying capacity, the biocapacity ratio, and the productivity illusion",
    size=fit("Emergent carrying capacity, the biocapacity ratio, and the productivity illusion",
             W-40, "bold", 8.4), color=DARK, weight="bold")

plt.savefig("graphical_abstract.pdf", dpi=DPI, facecolor="white")
plt.savefig("graphical_abstract.png", dpi=DPI, facecolor="white")
plt.savefig("graphical_abstract.tiff", dpi=DPI, facecolor="white", format="tiff")
print("ok  print cm:", round(W/DPI*2.54, 2), "x", round(H/DPI*2.54, 2))
