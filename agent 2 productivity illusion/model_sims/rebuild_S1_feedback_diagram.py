"""
Rebuild the S1 feedback-loop diagram for the ECOMOD v34 manuscript
(supplementary figure S1, 'Feedback diagram (one-stock comparator)').

The original source drawing script was not retained in the tree, so this script
recreates the same causal / feedback structure faithfully and repositions every
arrow label into clear whitespace (their earlier positions sat on top of the
arrows / on the arrowheads).  Output: scans/feedback_diagram.png (overwritten),
rendered at 1667x995 to match the prior layout.

Boxes (x0,y0,x1,y1) in image pixel coordinates (y down).  Arrow endpoints are
given explicitly so labels can be placed beside, not on, the arrows.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

W, H = 1667, 995

# ---- box geometry (pixel coords, y increases downward) ----
# name: (x0, y0, x1, y1, fill, edge)
BOXES = {
    "G_reg":   (15,  35, 349,  94, "#E0E7FF", "#44445A"),
    "A":       (20, 107, 234, 234, "#DBEAFC", "#44445A"),
    "B":       (455,105, 751, 244, "#DCFCE7", "#44445A"),
    "K":       (752,108, 885, 237, "#D6D8DD", "#44445A"),
    "P":       (915,108,1204, 239, "#FEF9C3", "#44445A"),
    "E":       (1278,107,1454, 240, "#FDE68A", "#44445A"),
    "switch":  (521,403, 883, 526, "#FBE2E2", "#44445A"),
    "D":       (1132,544,1291, 718, "#EEEEEE", "#44445A"),
    "b":       (820,645, 995, 748, "#F4ECFF", "#44445A"),
    "T_b":     (175,645, 470, 748, "#FDF0B8", "#44445A"),
}

# ---- box text ----
TEXT = {
    "G_reg":   r"G(A(t$-\tau_g$))   regeneration",
    "A":       "A\nproductive\nstock",
    "B":       r"B = bA + b$_G$ G(A)"+"\nbiocapacity",
    "K":       "K = B/e\ncarrying cap.",
    "P":       "delayed\nP\npopulation",
    "E":       r"E = e$\cdot$P"+"\nharvest",
    "switch":  r"switch [E $-$ bA]$_+$"+"\nliquidation when E > bA",
    "D":       "D\ndebt",
    "b":       "b (eroded)",
    "T_b":     r"T_b (bounded"+"\ntechnology wave)",
}

fig, ax = plt.subplots(figsize=(W / 100.0, H / 100.0), dpi=100)
ax.set_xlim(0, W); ax.set_ylim(H, 0)   # invert y so pixel coords map directly
ax.axis("off")
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

def box(name):
    x0, y0, x1, y1, fc, ec = BOXES[name]
    w, h = x1 - x0, y1 - y0
    p = FancyBboxPatch((x0, y0), w, h,
                       boxstyle="round,pad=0,rounding_size=14",
                       linewidth=1.8, edgecolor=ec, facecolor=fc,
                       mutation_aspect=1, zorder=2)
    ax.add_patch(p)
    ax.text(x0 + w / 2, y0 + h / 2, TEXT[name], ha="center", va="center",
            fontsize=15, fontweight="bold", color="#1b1b1b", zorder=3)

for n in BOXES:
    box(n)

RED    = "#D64545"
PURPLE = "#7A3CF0"
ORANGE = "#B9770E"
BLUE   = "#2f5fd0"
GRAY   = "#7a7a85"

def arrow(p0, p1, color, lw=3.2, rad=0.0, style="-|>", zorder=1, ms=17):
    a = FancyArrowPatch(p0, p1, connectionstyle=f"arc3,rad={rad}",
                        arrowstyle=style, lw=lw, color=color,
                        mutation_scale=ms, zorder=zorder,
                        shrinkA=0, shrinkB=0)
    ax.add_patch(a)

def lbl(x, y, s, color, ha="center", va="center", rot=0, fs=13.5, pad=None, zorder=5):
    ax.text(x, y, s, color=color, ha=ha, va=va, rotation=rot,
            fontsize=fs, fontweight="bold", zorder=zorder, bbox=None)

# ================= arrows =================
# G_reg -> A (down, short) -- single arrow
arrow((175, 94), (175, 112), BLUE, lw=3.0)
# label 'delayed tau_g': nudge a tiny bit RIGHT and DOWN of the arrow, into whitespace
lbl(210, 104, "delayed " + r"$\tau_g$", BLUE, ha="left", va="center", fs=13.0)

# A -> B (right) 'flow b.A + increment'
arrow((234, 172), (455, 172), GRAY, lw=3.0)
# label above the arrow, moved a tiny bit LEFT into whitespace
lbl(330, 148, "flow b.A" + "\n+ increment", GRAY, ha="center", va="bottom", fs=12.5)

# B -> K -> P -> E (right)
arrow((751, 172), (752, 172), GRAY, lw=3.0)
arrow((885, 172), (915, 172), GRAY, lw=3.0)
arrow((1204, 172), (1278, 172), GRAY, lw=3.0)

# K -> P k(t-tau_p) edge -- label sits UP and somewhat LEFT, in whitespace above the boxes
lbl(893, 88, "k(t" + r"$-\tau_p$" + ")\ndelayed", RED, ha="center", va="bottom", fs=12.0)

# E -> switch (red, curved down-left) label 'E' -- bring it CLOSER to the arrow it describes
arrow((1366, 240), (872, 403), RED, lw=3.4, rad=-0.18)
lbl(1145, 300, "E", RED, ha="center", va="center", fs=15)

# A -> switch (red, down) 'bA' label -- place to the right of the arrow in whitespace
arrow((127, 234), (521, 470), RED, lw=3.4, rad=0.10)
lbl(300, 340, "bA", RED, ha="center", va="center", fs=14)

# switch -> D (purple, down-right) label 'b->' -- move it a bit LEFT so it lands in whitespace
arrow((770, 526), (1185, 640), PURPLE, lw=3.2, rad=-0.08)
lbl(880, 602, "b" + r"$\to$", PURPLE, ha="center", va="center", fs=14)

# D -> b (purple, down-left) label 'e^{-alpha D}' -- bring e^ a little DOWN so it lands in whitespace
arrow((1155, 660), (975, 700), PURPLE, lw=3.2, rad=0.05)
lbl(1044, 726, r"e$^{-\alpha D}$", PURPLE, ha="center", va="center", fs=14)

# T_b -> b (orange, right) '-db'
arrow((470, 700), (820, 700), ORANGE, lw=3.4)
lbl(645, 675, "$\u2212$db", ORANGE, ha="center", va="bottom", fs=14)

# Loop captions (kept in the central whitespace, clear of arrows)
ax.text(430, 300, "Loop 1: liquidation drains A   (A\u2193$\u2192$B\u2193$\u2192$deficit\u2191$\u2192$liquidation\u2191$\u2192$A\u2193)",
        color=RED, fontsize=12.5, fontweight="bold", ha="left")
ax.text(430, 396, "Loop 2: debt erodes yield.   (D\u2191$\u2192$b\u2193$\u2192$B\u2193$\u2192$deficit\u2191$\u2192$D\u2191)",
        color=PURPLE, fontsize=12.5, fontweight="bold", ha="left")

# Title
ax.text(W / 2, 18, "Corrected (1$^{st}$) unified stock-flow model \u2014 causal / feedback structure",
        ha="center", va="center", fontsize=17, fontweight="bold")

# Footer note
ax.text(W / 2, 985,
        "Two positive-feedback loops, which compound:  Loop 1 = stock-liquidation (A drains), Loop 2 = debt-erosion (yield is eroded).\n"
        r"$\tau_g$ (regeneration lag) and $\tau_p$ (carrying-capacity lag) are the only delays.  An exogenous, bounded technology wave T_b lifts b but cannot outrun either loop.",
        ha="center", va="center", fontsize=12, color="#333")

fig.savefig("scans/feedback_diagram.png", dpi=100, bbox_inches=None)
print("wrote scans/feedback_diagram.png", fig.get_size_inches() * fig.dpi)
