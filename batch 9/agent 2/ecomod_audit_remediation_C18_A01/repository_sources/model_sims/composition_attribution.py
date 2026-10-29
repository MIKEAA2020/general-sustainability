#!/usr/bin/env python3
"""Fig. 2 (main text) — measured land-type composition of the aggregate biocapacity change.

World, National Footprint & Biocapacity Accounts (land-type matrix), 1961 -> 2022.

Panel (a): additive decomposition of the aggregate (+24.5%, land-type Total) growth.
    Each bar = how much that land type contributed to the change in the aggregate,
    expressed as a share of the 1961 aggregate (so the bars sum to the total growth).
Panel (b): the measured 1961->2022 change ratio per land type (multiplicative).

The point of the figure (the "composition illusion"): a single rising aggregate number
conceals that the growth is almost entirely cropland and built-up (human-converted land),
while the natural land types (forest, grazing, fishing) all declined. This is the
identifiability-motivated reason the aggregate alone cannot reveal composition.

Outputs: reports/composition_attribution.png (main-text figure).
"""
import csv, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA = "data/nfa/NFA_world_landtype_biocapacity_footprint_1961_2023.csv"

def load():
    rows = list(csv.DictReader(open(DATA)))
    def wt(year):
        for r in rows:
            if r["Record"].strip() == "BiocapTotGHA" and r["year"].strip() == year \
               and r["Country Name"].strip() == "World":
                return r
        raise KeyError(year)
    return wt("1961"), wt("2022")

a, b = load()
types = ["Cropland", "Forest Products", "Grazing Land",
         "Fishing Grounds", "Built-up Land"]
va = {t: float(a[t]) for t in types}
vb = {t: float(b[t]) for t in types}
ratio = {t: vb[t] / va[t] for t in types}
dln = {t: math.log(vb[t] / va[t]) for t in types}

tot61 = float(a["Total"]); tot22 = float(b["Total"])
add_growth = tot22 / tot61 - 1.0            # +0.245 (land-type Total), additive
# additive contribution of each land type as a share of the 1961 aggregate
contrib = {t: (vb[t] - va[t]) / tot61 for t in types}

names = ["Cropland", "Forest", "Grazing", "Fishing", "Built-up"]
cols  = ["#1f8a4c", "#5c6b73", "#5c6b73", "#5c6b73", "#e0a458"]
ct    = [contrib[t] for t in types]
rt    = [ratio[t] for t in types]

fig, (ax, ax2) = plt.subplots(1, 2, figsize=(8.4, 4.0), dpi=200)

# ---- Panel (a): additive decomposition of the aggregate growth ----
ax.bar(range(len(types)), np.array(ct) * 100, color=cols, edgecolor="#222222", lw=0.6)
ax.axhline(0, color="#555555", lw=0.9)
# fraction each positive/negative group sums to, annotate
pos = sum(c for c in ct if c > 0) * 100
neg = sum(c for c in ct if c < 0) * 100
ax.set_xticks(range(len(types))); ax.set_xticklabels(names)
ax.set_ylabel("contribution to aggregate growth\n(share of 1961 aggregate), %")
ax.set_title("(a) What drives the aggregate rise", fontsize=10, weight="bold")
ax.axhline(add_growth * 100, color="#1f3a5f", lw=1.5, ls="--")
ax.text(len(types) - 0.45, add_growth * 100 + 1.2,
        f"aggregate +{add_growth*100:.1f}%", ha="right", fontsize=8, color="#1f3a5f")
for i in range(len(types)):
    v = ct[i] * 100
    ax.text(i, v + (1.2 if v >= 0 else -3.2), f"{v:+.1f}",
            ha="center", fontsize=8, color="#222222")
ax.set_ylim(min(ct) * 100 - 5, max(ct) * 100 + 7)
ax.spines[["top", "right"]].set_visible(False)
ax.annotate(f"gross +{pos:.1f}% vs natural declines {neg:.1f}%",
            xy=(0.02, 0.97), xycoords="axes fraction", ha="left", va="top",
            fontsize=8, color="#444444")

# ---- Panel (b): measured change ratio per land type ----
ax2.bar(range(len(types)), rt, color=cols, edgecolor="#222222", lw=0.6)
ax2.axhline(1.0, color="#555555", lw=0.9)
ax2.set_xticks(range(len(types))); ax2.set_xticklabels(names)
ax2.set_ylabel("change ratio, 1961 $\\to$ 2022")
ax2.set_title("(b) Measured change ratio per land type", fontsize=10, weight="bold")
for i in range(len(types)):
    ax2.text(i, rt[i] + 0.06, f"{rt[i]:.2f}$\\times$", ha="center", fontsize=8)
ax2.set_ylim(-0.4, max(rt) * 1.28)
ax2.spines[["top", "right"]].set_visible(False)

fig.tight_layout()
out = "reports/composition_attribution.png"
fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
print("wrote", out)
print("ratios:", {t: round(ratio[t], 3) for t in types})
print("additive growth:", round(add_growth, 4))
print("contrib%:", {t: round(contrib[t]*100, 2) for t in types})
print("sum contrib% =", round(sum(contrib.values())*100, 2))
