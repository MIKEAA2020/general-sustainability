"""
Faithful, high-DPI recreation of the S1 feedback-loop diagram (ECOMOD v34).

The figure depicts the ONE-STOCK comparator (single capital A) whose two
positive-feedback loops the manuscript describes in Section 7:

    Loop 1  (stock-liquidation / conversion):  A -> B -> deficit -> A
        A down -> B down -> deficit up -> liquidation up -> A down

    Loop 2  (debt-erosion of the flow yield):  D -> b -> B -> deficit -> D
        D up -> b down -> B down -> deficit up -> D up

Both loops converge on the deficit switch  S = [E - bA]_+  but act on different
books.  Unlike the original raster (which labelled the loops only in a caption
and never drew the return edges), this recreation draws BOTH loops as genuinely
closed cycles.

Colour coding (kept from the original):
    gray      forward processing chain (A->B->K->P->E) and its flow labels
    blue      G(A) regeneration edge (delayed tau_g)
    orange    delayed K->P edge (k(t - tau_p)) and the T_b -> b ( -db ) input
    red       Loop 1 (stock-liquidation) and the E -> deficit demand edge
    purple    Loop 2 (debt-erosion)

The meta-labelling title ("Corrected (1st) unified stock-flow model ...") has
been removed; the figure carries only a neutral, descriptive title.
Rendered at 400 dpi.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

RED    = (239/255, 68/255, 68/255)
PURPLE = (124/255, 58/255, 237/255)
ORANGE = (180/255, 83/255, 9/255)
BLUE   = (37/255, 99/255, 235/255)
GRAY   = (108/255, 108/255, 120/255)
BORDER = (51/255, 51/255, 68/255)
TXT    = "#1b1b1b"
FILLS  = {
    "G": "#E0E7FF", "A": "#DBEAFE", "B": "#DCFCE7", "K": "#D1D1D5",
    "P": "#FEF9C3", "E": "#FDE68A", "S": "#FBE2E2", "D": "#E5E7EB",
    "b": "#F3ECFF", "T_b": "#FDF3C7",
}

# ---- boxes: (cx, cy, w, h) ----
BX = {
    "G":   (150,  78, 280, 56),
    "A":   (150, 200, 200, 120),
    "B":   (520, 200, 200, 120),
    "K":   (840, 200, 190, 120),
    "P":   (1180,200, 200, 120),
    "E":   (1520,200, 190, 120),
    "S":   (760, 530, 340, 130),
    "D":   (1360,620, 180, 120),
    "b":   (520, 880, 190, 115),
    "T_b": (150, 880, 250, 115),
}
TEX = {
    "G":   r"G(A(t$-\tau_g$))   regeneration",
    "A":   "A\nproductive\nstock",
    "B":   "B = bA + increment\nbiocapacity",
    "K":   "K = B/e\ncarrying cap.",
    "P":   "delayed\nP\npopulation",
    "E":   "E = e\u00b7P\nharvest",
    "S":   "deficit switch\nS = [E \u2212 bA]$_{+}$",
    "D":   "D\ndebt",
    "b":   "b\nflow yield",
    "T_b": r"T$_b$ (bounded" + "\ntechnology wave)",
}

W, H = 1700, 1120
DPI = 400
fig = plt.figure(figsize=(W/100.0, H/100.0), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(H, 0)
ax.axis("off")

for n, (cx, cy, w, h) in BX.items():
    ax.add_patch(FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                 boxstyle="round,pad=0,rounding_size=12",
                 linewidth=2.0, edgecolor=BORDER, facecolor=FILLS[n], zorder=2))
    ax.text(cx, cy, TEX[n], ha="center", va="center", fontsize=13,
            fontweight="bold", color=TXT, zorder=3, linespacing=1.15)

def arrow(p0, p1, color, lw=3.0, rad=0.0, ms=16, z=4):
    ax.add_patch(FancyArrowPatch(p0, p1, connectionstyle=f"arc3,rad={rad}",
                 arrowstyle="-|>", lw=lw, color=color, mutation_scale=ms,
                 shrinkA=0, shrinkB=0, zorder=z))

def lbl(x, y, s, color, ha="center", va="center", fs=13, rot=0, z=6, ls=1.15):
    ax.text(x, y, s, color=color, ha=ha, va=va, rotation=rot, fontsize=fs,
            fontweight="bold", zorder=z, linespacing=ls)

# ================= title (neutral, no meta-labelling) =================
ax.text(W/2, 26,
        "Feedback structure of the one-stock comparator: two compounding positive-feedback loops",
        ha="center", va="center", fontsize=15.5, fontweight="bold", color="#1b1b1b")

# ================= forward processing chain (gray) =================
arrow((250,200),(420,200), GRAY, lw=2.6)      # A -> B
arrow((620,200),(745,200), GRAY, lw=2.6)      # B -> K
arrow((935,200),(1080,200), GRAY, lw=2.6)     # K -> P
arrow((1280,200),(1425,200), GRAY, lw=2.6)    # P -> E
lbl(350, 236, "flow b.A\n+ increment", GRAY, ha="center", va="top", fs=12)

# ================= regeneration edge (blue) =================
arrow((150,106),(150,140), BLUE, lw=2.8)
lbl(298, 170, r"delayed $\tau_g$", BLUE, ha="right", va="center", fs=13)

# ================= delayed K->P edge (orange) =================
arrow((935,225),(1080,225), ORANGE, lw=2.8)
lbl(1008, 156, r"k(t$-\tau_p$)" + "\ndelayed", ORANGE, ha="center", va="bottom", fs=12)

# ================= supply line B -> deficit switch (gray) =================
arrow((560,260),(660,470), GRAY, lw=2.6, rad=0.0)      # B -> S (bA supply)
lbl(585, 350, "b.A", GRAY, ha="center", va="center", fs=12.5)

# ================= E -> deficit demand edge (red) =================
arrow((1500,262),(890,500), RED, lw=3.2, rad=-0.16)
lbl(1300, 370, "E", RED, ha="center", va="center", fs=15)

# =========== Loop 1 (red, stock-liquidation): A->B->S->A ===========
arrow((560,262),(660,470), RED, lw=0)   # (B->S already gray; Loop1 closes below)
arrow((590,530),(250,270), RED, lw=3.2, rad=0.24)       # S -> A  (RETURN)
lbl(340, 460, "Loop 1: stock-liquidation\n(A\u2193 \u2192 B\u2193 \u2192 deficit\u2191 \u2192 liquidation\u2191 \u2192 A\u2193)",
    RED, ha="center", va="center", fs=12.5)

# =========== Loop 2 (purple, debt-erosion): D->b->B->S->D ===========
arrow((900,565),(1285,610), PURPLE, lw=3.0, rad=-0.10)   # S -> D  (deficit -> debt)
arrow((1355,680),(640,875), PURPLE, lw=3.0, rad=0.10)    # D -> b  (debt erodes yield)
arrow((520,822),(520,262), PURPLE, lw=3.0, rad=0.0)      # b -> B  (yield -> biocapacity) RETURN
lbl(1345, 745, "b\u2193", PURPLE, ha="center", va="center", fs=14)
lbl(538, 300, "b\u2192", PURPLE, ha="left", va="center", fs=13, z=8)
lbl(410, 990, "Loop 2: debt-erosion\n(D\u2191 \u2192 b\u2193 \u2192 B\u2193 \u2192 deficit\u2191 \u2192 D\u2191)",
    PURPLE, ha="center", va="center", fs=12.5)

# ================= T_b -> b input ( -db ) =================
arrow((275,900),(425,900), ORANGE, lw=2.8)
lbl(350, 872, r"$-$db", ORANGE, ha="center", va="bottom", fs=13.5)

# ================= colour legend (bottom-right whitespace) =================
lx, ly, lw2, lh2 = 1220, 760, 470, 292
ax.add_patch(FancyBboxPatch((lx, ly), lw2, lh2,
             boxstyle="round,pad=0,rounding_size=10",
             linewidth=1.5, edgecolor="#9aa0b0", facecolor="white",
             alpha=0.94, zorder=9))
ax.text(lx + 16, ly + 22, "Colour key", ha="left", va="center",
        fontsize=12.5, fontweight="bold", color="#1b1b1b", zorder=10)
rows = [
    (ORANGE, "k(t\u2212\u03c4_p)  \u2014 delayed K\u2192P edge"),
    (ORANGE, "T_b \u2192 b (\u2212db)  \u2014 tech wave lifts b"),
    (GRAY,   "forward chain  A\u2192B\u2192K\u2192P\u2192E"),
    (BLUE,   "regeneration  G(A), delayed \u03c4_g"),
    (RED,    "Loop 1  stock-liquidation (closes S\u2192A)"),
    (PURPLE, "Loop 2  debt-erosion (closes S\u2192D\u2192b\u2192B)"),
]
y0 = ly + 48
for i, (c, t) in enumerate(rows):
    yy = y0 + i * 40
    ax.plot([lx + 24, lx + 74], [yy, yy], color=c, lw=3.2, zorder=10,
            solid_capstyle="round")
    ax.text(lx + 86, yy, t, ha="left", va="center", fontsize=10.5,
            color="#222", zorder=10, linespacing=1.1)

# ================= footer =================
ax.text(W/2, 1080,
        "Both loops close above: each returns to the deficit switch S = [E \u2212 bA]$_{+}$.  "
        r"$\tau_g$ and $\tau_p$ are the only delays; an exogenous bounded technology wave "
        r"$T_b$ lifts $b$ but cannot outrun either loop.",
        ha="center", va="center", fontsize=11.5, color="#333", linespacing=1.5)

fig.savefig("scans/feedback_diagram.png", dpi=DPI)
fig.savefig("supplementary/FIGURES/S1_feedback_diagram.png", dpi=DPI)
print("wrote high-DPI S1 (", W, "x", H, "at", DPI, "dpi )")
