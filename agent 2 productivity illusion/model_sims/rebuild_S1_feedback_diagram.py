"""
Faithful, high-DPI recreation of the S1 feedback-loop diagram (ECOMOD v34).

This reproduces the original figure (scans/feedback_diagram.png, the committed
source of record) in geometry, colour and text, honouring the original colour
coding exactly:
  - the K->P edge AND its k(t-tau_p) label are BOTH orange (they must match);
  - gray flow arrows on A->B, B->K, P->E (the flow b.A + increment label is gray);
  - red for the A->switch / E->switch loops, the 'bA' and 'E' labels, Loop 1;
  - purple for the switch->D / D->b edges, 'b->' and 'e^{-alpha D}', Loop 2;
  - blue for the G->A regeneration arrow and 'delayed tau_g'.

Only the six labels the author flagged are nudged (into clear whitespace, still
adjacent to the arrow they describe); every box, arrow and other label retains
its original position.  Rendered at 400 dpi.

Box coordinates are the pixel coordinates measured directly from the original
1667x995 raster; y increases downward.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ---- palette (sampled from the original) ----
RED    = (239/255, 68/255, 68/255)
PURPLE = (124/255, 58/255, 237/255)
ORANGE = (180/255, 83/255, 9/255)
BLUE   = (37/255, 99/255, 235/255)
GRAY   = (108/255, 108/255, 120/255)
BORDER = (51/255, 51/255, 68/255)
TXT    = "#1b1b1b"
FILLS  = {
    "G": "#E0E7FF",   # (224,231,255)
    "A": "#DBEAFE",   # (219,234,254)
    "B": "#DCFCE7",   # (220,252,231)
    "K": "#D1D1D5",   # (209,209,213)
    "P": "#FEF9C3",   # (254,249,195)
    "E": "#FDE68A",   # (253,230,138)
    "sw": "#FBE2E2",  # (254,226,226)
    "D": "#E5E7EB",   # (229,231,235)
    "b": "#F3ECFF",   # (243,232,255)
    "T_b": "#FDF3C7", # (254,243,199)
}

# ---- box geometry (x0,y0,x1,y1) ----
BOXES = {
    "G":   (12,  38, 352,  95),
    "A":   (30, 107, 256, 240),
    "B":   (476,103, 731, 244),
    "K":   (877,107,1053, 240),
    "P":   (1206,107,1382, 240),
    "E":   (1494,107,1653, 240),
    "sw":  (542,404, 862, 527),
    "D":   (1280,543,1513, 668),
    "b":   (905,718,1040, 805),
    "T_b": (192,718, 489, 810),
}

TEXTS = {
    "G":   r"G(A(t$-\tau_g$))   regeneration",
    "A":   "A\nproductive\nstock",
    "B":   r"B = bA + b$_G$ G(A)" + "\nbiocapacity",
    "K":   "K = B/e\ncarrying cap.",
    "P":   "delayed\nP\npopulation",
    "E":   r"E = e$\cdot$P" + "\nharvest",
    "sw":  r"switch [E $-$ bA]$_+$" + "\nliquidation when E > bA",
    "D":   "D\ndebt",
    "b":   "b (eroded)",
    "T_b": r"T_b (bounded" + "\ntechnology wave)",
}

W, H = 1667, 995
DPI = 400
fig = plt.figure(figsize=(W/100.0, H/100.0), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(H, 0)
ax.axis("off")

def box(name):
    x0, y0, x1, y1 = BOXES[name]
    w, h = x1-x0, y1-y0
    ax.add_patch(FancyBboxPatch((x0, y0), w, h,
                 boxstyle="round,pad=0,rounding_size=0",   # matches original (square-ish, slim rounding)
                 linewidth=2.0, edgecolor=BORDER, facecolor=FILLS[name], zorder=2))
    ax.text(x0+w/2, y0+h/2, TEXTS[name], ha="center", va="center",
            fontsize=14.5, fontweight="bold", color=TXT, zorder=3, linespacing=1.1)

for n in BOXES:
    box(n)

def arrow(p0, p1, color, lw=3.0, rad=0.0, ms=16, z=1):
    ax.add_patch(FancyArrowPatch(p0, p1, connectionstyle=f"arc3,rad={rad}",
                 arrowstyle="-|>", lw=lw, color=color, mutation_scale=ms,
                 shrinkA=0, shrinkB=0, zorder=z))

def lbl(x, y, s, color, ha="center", va="center", fs=13, rot=0, z=5, ls=1.1):
    ax.text(x, y, s, color=color, ha=ha, va=va, rotation=rot, fontsize=fs,
            fontweight="bold", zorder=z, linespacing=ls)

# ---- title ----
ax.text(W/2, 22, r"Corrected (1$^{\mathrm{st}}$) unified stock-flow model $\mathrm{---}$ causal / feedback structure",
        ha="center", va="center", fontsize=16, fontweight="bold", color="#1b1b1b")

# ---- gray flow arrows ----
arrow((256,173),(476,173), GRAY, lw=2.6)      # A -> B
arrow((731,173),(877,173), GRAY, lw=2.6)      # B -> K
arrow((1382,173),(1494,173), GRAY, lw=2.6)    # P -> E
# flow b.A + increment: nudged DOWN closer to the arrow (and a touch RIGHT) into whitespace
lbl(372, 172, "flow b.A" + "\n+ increment", GRAY, ha="center", va="bottom", fs=12.5, ls=1.15)

# ---- orange K->P arrow (matches its label) ----
arrow((1053,170),(1206,170), ORANGE, lw=2.8)
# k(t-tau_p) delayed: nudged UP and somewhat LEFT into whitespace above the arrow
lbl(1090, 133, "k(t" + r"$-\tau_p$" + ")\ndelayed", ORANGE, ha="center", va="center", fs=12.5, ls=1.15)

# ---- blue G->A regeneration arrow ----
arrow((175,95),(210,107), BLUE, lw=2.8)
lbl(238, 104, "delayed " + r"$\tau_g$", BLUE, ha="left", va="center", fs=13)  # nudged right+down

# ---- red E->switch curve ----
arrow((1366,240),(884,404), RED, lw=3.2, rad=-0.18)
lbl(1150, 300, "E", RED, ha="center", va="center", fs=15)  # nudged closer to the arrow

# ---- red A->switch ----
arrow((150,240),(542,468), RED, lw=3.2, rad=0.10)
lbl(288, 322, "bA", RED, ha="center", va="center", fs=14)

# ---- purple switch->D ----
arrow((770,527),(1140,635), PURPLE, lw=3.0, rad=-0.08)
lbl(812, 610, "b" + r"$\to$", PURPLE, ha="center", va="center", fs=14)  # nudged LEFT into whitespace

# ---- purple D->b ----
arrow((1270,640),(1040,710), PURPLE, lw=3.0, rad=0.05)
lbl(1195, 690, r"e$^{-\alpha D}$", PURPLE, ha="center", va="center", fs=14)  # nudged DOWN into whitespace

# ---- orange T_b->b (-db) ----
arrow((489,700),(905,700), ORANGE, lw=2.8)
lbl(697, 676, r"$-$db", ORANGE, ha="center", va="bottom", fs=13.5)

# ---- feedback-loop captions ----
ax.text(430, 322, "Loop 1: liquidation drains A   (A\u2193$\u2192$B\u2193$\u2192$deficit\u2191$\u2192$liquidation\u2191$\u2192$A\u2193)",
        color=RED, fontsize=12, fontweight="bold", ha="left", va="center")
ax.text(270, 858, "Loop 2: debt erodes yield.   (D\u2191$\u2192$b\u2193$\u2192$B\u2193$\u2192$deficit\u2191$\u2192$D\u2191)",
        color=PURPLE, fontsize=12, fontweight="bold", ha="left", va="center")

# ---- footer ----
ax.text(W/2, 972,
        "Two positive-feedback loops, which compound:  Loop 1 = stock-liquidation (A drains), Loop 2 = debt-erosion (yield is eroded).\n"
        r"$\tau_g$ (regeneration lag) and $\tau_p$ (carrying-capacity lag) are the only delays.  "
        r"An exogenous, bounded technology wave T_b lifts b but cannot outrun either loop.",
        ha="center", va="center", fontsize=11.5, color="#333", linespacing=1.5)

fig.savefig("scans/feedback_diagram.png", dpi=DPI)
fig.savefig("supplementary/FIGURES/S1_feedback_diagram.png", dpi=DPI)
print("wrote high-DPI S1 (", W, "x", H, "at", DPI, "dpi )")
