#!/usr/bin/env python3
"""Build the C19 GA01 graphical abstract from the selected model and NFA outputs.

The figure is a 1328 x 531 px banner at 200 dpi. It uses the actual selected
projected delayed-quality fixed-demand run, not a hand-drawn trajectory.
No existing C19 file is modified.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True

import numpy as np
from PIL import Image
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

ROOT = Path(__file__).resolve().parent
C19 = ROOT / "source_snapshot"  # Byte-exact inputs copied from the frozen C19 release.
W, H, DPI = 1328, 531, 200
plt.rcParams["svg.hashsalt"] = "ecomod_C19_GA01"
DARK, GREY, BLUE = "#18324a", "#5c6b73", "#246588"
FLOW, STOCK, ACCENT = "#237a57", "#b45438", "#b37b18"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


twoland = load_module(C19 / "code/reproduce_two_land_C18_A01.py", "c19_twoland_ga01")
a = twoland.run(1.5, 1.5, 0.0, 250.0, 0.05, Efixed=0.825)
t = np.arange(len(a)) * 0.05
mask = (np.diff(a[:, 6]) > 0) & (np.diff(a[:, 1]) < 0)
idx = np.flatnonzero(mask)
j = int(idx[-1] + 1)
Yc = (0.05 + 0.064 * a[:, 2] * (1 - a[:, 2])) * a[:, 1]
baseline = {
    "fixed_demand_gha": 0.825,
    "restoration": "off",
    "quality_law": "selected projected delayed quality",
    "mask_end_yr": j * 0.05,
    "B_initial_gha": float(a[0, 6]),
    "B_end_gha": float(a[j, 6]),
    "B_change_pct": float(100 * (a[j, 6] / a[0, 6] - 1)),
    "Ac_initial_ha": float(a[0, 1]),
    "Ac_end_ha": float(a[j, 1]),
    "Ac_change_pct": float(100 * (a[j, 1] / a[0, 1] - 1)),
    "capital_contribution_initial_gha": float(Yc[0]),
    "capital_contribution_end_gha": float(Yc[j]),
    "capital_contribution_change_pct": float(100 * (Yc[j] / Yc[0] - 1)),
}
assert round(baseline["mask_end_yr"], 1) == 149.0
assert round(baseline["B_change_pct"], 0) == 39
assert round(baseline["Ac_change_pct"], 2) == -46.16
assert round(baseline["capital_contribution_change_pct"], 2) == -51.72

with (C19 / "data/empirical_endpoints_C18_A01.csv").open(newline="") as handle:
    endpoints = {int(row["year"]): row for row in csv.DictReader(handle)}
with (C19 / "data/empirical_components_C18_A01.csv").open(newline="") as handle:
    component_rows = list(csv.DictReader(handle))
components = {(int(row["year"]), row["component"]): row for row in component_rows}
e = endpoints[2023]
nfa = {
    "edition": "NFA Edition 2026, results and metadata v1.0",
    "window": "1961–2023",
    "B_change_pct": float(e["B_change_pct"]),
    "B_per_person_change_pct": float(e["BP_change_pct"]),
    "cropland_ratio": float(components[(2023, "crop")]["ratio"]),
    "forest_ratio": float(components[(2023, "forest")]["ratio"]),
    "built_up_ratio": float(components[(2023, "built")]["ratio"]),
    "excluded_estimate_years": [2024, 2025],
}
assert round(nfa["B_change_pct"], 2) == 24.86
assert round(nfa["B_per_person_change_pct"], 2) == -52.71
assert round(nfa["cropland_ratio"], 4) == 2.8701
assert round(nfa["forest_ratio"], 4) == 0.8996
assert round(nfa["built_up_ratio"], 4) == 8.7935

fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor="white")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")
fig.canvas.draw()
renderer = fig.canvas.get_renderer()


def measure(s, size, weight="normal"):
    item = ax.text(0, 0, s, fontsize=size, fontweight=weight)
    box = item.get_window_extent(renderer)
    item.remove()
    return box.width


def fit(s, width, weight="normal", maxsize=7.0, minsize=5.0):
    size = maxsize
    while size > minsize and measure(s, size, weight) > width:
        size -= 0.1
    return size


def text(x, y, s, size=6.6, color=DARK, weight="normal", ha="center", va="center", style="normal", z=8):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
            style=style, zorder=z, linespacing=1.12)


def box(x, y, w, h, fc="white", ec=DARK, lw=1.2, radius=8, z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={radius}",
                                facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z))


def arrow(x1, y1, x2, y2, color=STOCK):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=10,
                                linewidth=1.7, color=color, zorder=6, shrinkA=2, shrinkB=2))


def head(cx, title, subtitle, width):
    text(cx, 429, title, size=fit(title, width, "bold", 9.0), weight="bold")
    text(cx, 407, subtitle, size=fit(subtitle, width, "normal", 6.5), color=GREY, style="italic")


for x0, width, fc, ec in [(10, 416, "#fbfdfc", "#d6e2dc"),
                          (434, 420, "#f8fafc", "#d3e2ef"),
                          (862, 456, "#fcfbf7", "#e7e2d2")]:
    ax.add_patch(Rectangle((x0, 108), width, 338, facecolor=fc, edgecolor=ec, lw=1.0, zorder=0))

text(W / 2, 507, "A rising biocapacity total can mask ecological-capital land drawdown: a two-land model",
     size=fit("A rising biocapacity total can mask ecological-capital land drawdown: a two-land model", W - 36, "bold", 10.8), weight="bold")
text(W / 2, 481, "Composition mechanism  ·  selected simulation  ·  identification limits  ·  separate NFA account evidence",
     size=fit("Composition mechanism  ·  selected simulation  ·  identification limits  ·  separate NFA account evidence", W - 60, "normal", 6.8), color=GREY)

# Panel A: exact model objects and annual-account interpretation.
head(218, "COMPOSITION MECHANISM", "annual account contributions; area conserved", 386)
box(30, 319, 376, 64, fc="#e7f4ec", ec=FLOW, lw=1.4)
text(218, 365, "FAST-PROVISIONING AREA  $A_f$", size=7.2, color=FLOW, weight="bold")
text(218, 340, "annual contribution  $b_f A_f$", size=7.4)
box(30, 237, 376, 64, fc="#fbeaea", ec=STOCK, lw=1.4)
text(218, 283, "ECOLOGICAL-CAPITAL AREA  $A_c$", size=fit("ECOLOGICAL-CAPITAL AREA  $A_c$", 352, "bold", 7.2), color=STOCK, weight="bold")
text(218, 258, "annual contribution  $\\Upsilon_c(q) A_c$", size=7.4)
arrow(218, 301, 218, 319)
text(236, 310, "conversion  $u_c$", size=6.0, color=STOCK, weight="bold", ha="left")
text(218, 222, "Reserve $A_r$:  $A_f+A_c+A_r=A_{\\mathrm{tot}}$; transfers conserve area",
     size=fit("Reserve $A_r$:  $A_f+A_c+A_r=A_{\\mathrm{tot}}$; transfers conserve area", 378, "normal", 6.1), color=GREY)
box(30, 157, 376, 53, fc="white", ec=BLUE, lw=1.4)
text(218, 192, "ANNUAL ACCOUNT  $B$", size=7.1, color=BLUE, weight="bold")
text(218, 170, "$B=b_f A_f+\\Upsilon_c(q) A_c$", size=7.5, weight="bold")
box(20, 116, 396, 32, fc="#fff8e8", ec=ACCENT, lw=1.2)
text(218, 137, "$\\Delta b_{\\mathrm{conv}}=b_f(D)-\\Upsilon_c(q)>0$",
     size=fit("$\\Delta b_{\\mathrm{conv}}=b_f(D)-\\Upsilon_c(q)>0$", 378, "bold", 6.6), color="#7b570e", weight="bold")
text(218, 123, "conversion adds to $B$; $A_c$ falls when $u_c>R_{rc}$",
     size=fit("conversion adds to $B$; $A_c$ falls when $u_c>R_{rc}$", 378, "bold", 6.1), weight="bold")

# Panel B: actual selected delayed-quality trajectory, normalized only for display.
head(644, "SELECTED FIXED-DEMAND RUN", "projected delayed quality; representative—not fitted", 390)
pax = fig.add_axes([475 / W, 220 / H, 355 / W, 145 / H], facecolor="white")
pax.plot(t, a[:, 6] / a[0, 6], color=FLOW, lw=2.2, label="$B/B_0$")
pax.plot(t, a[:, 1] / a[0, 1], color=STOCK, lw=2.2, label="$A_c/A_{c0}$")
pax.fill_between(t[:-1], 0.45, 1.45, where=mask, color=ACCENT, alpha=0.12, linewidth=0)
pax.scatter([t[j]], [a[j, 6] / a[0, 6]], s=18, color=FLOW, zorder=5)
pax.scatter([t[j]], [a[j, 1] / a[0, 1]], s=18, color=STOCK, zorder=5)
pax.set(xlim=(0, 150), ylim=(0.45, 1.45))
pax.tick_params(labelsize=6, length=2, pad=1)
text(644, 378, "fraction of initial", size=5.8, color=GREY)
pax.grid(alpha=0.18, linewidth=0.5)
for spine in pax.spines.values():
    spine.set_color("#9eabb3")
    spine.set_linewidth(0.7)
pax.legend(loc="upper left", frameon=False, fontsize=6.5, ncol=2, columnspacing=1.0, handlelength=2.0)
text(644, 190, "time (yr)  ·  shading: $\\dot B>0$ and $\\dot A_c<0$  ·  mask ends at 149 yr",
     size=fit("time (yr)  ·  shading: $\\dot B>0$ and $\\dot A_c<0$  ·  mask ends at 149 yr", 382, "normal", 6.0), color=GREY)
for x, value, label, color, bg in [(446, "+39%", "account total", FLOW, "#eaf5ee"),
                                    (578, "−46.16%", "capital area", STOCK, "#fbeaea"),
                                    (710, "−51.72%", "capital contribution", BLUE, "#eaf1f7")]:
    box(x, 139, 124, 39, fc=bg, ec=color, lw=1.1)
    text(x + 62, 164, value, size=7.0, color=color, weight="bold")
    text(x + 62, 147, label, size=fit(label, 116, "normal", 5.3, 4.6), color=DARK)
text(644, 122, "$E=0.825$ gha  ·  restoration off  ·  conditional run",
     size=fit("$E=0.825$ gha  ·  restoration off  ·  conditional run", 392, "normal", 6.0), color=GREY)

# Panel C: identification, reduced-branch scope, and recovery—no universal collapse claim.
head(1090, "IDENTIFICATION & LIMITS", "what follows, and under which assumptions", 410)
callouts = [
    (320, "AGGREGATE ≠ ALLOCATION", "$B$ alone cannot identify $A_c$", "Independent observations sharpen compatible-area bounds", BLUE, "#eaf1f7"),
    (240, "REDUCED FIXED-DEMAND BRANCH", "minimum-area floor at $E_{\\mathrm{ceil}}=1.138$ gha", "No fold or critical slowing under the stated assumptions", STOCK, "#fbeaea"),
    (160, "RECOVERY", "requires an explicit gated restoration flow $R_{rc}$", "Lower demand alone does not restore $A_c$", FLOW, "#eaf5ee"),
]
for y, title, line1, line2, color, bg in callouts:
    box(882, y, 416, 62, fc=bg, ec=color, lw=1.2)
    text(1090, y + 47, title, size=fit(title, 390, "bold", 6.9), color=DARK, weight="bold")
    text(1090, y + 28, line1, size=fit(line1, 390, "normal", 6.2), color=DARK)
    text(1090, y + 12, line2, size=fit(line2, 390, "normal", 5.9), color=GREY)
text(1090, 139, "No universal collapse or delay threshold",
     size=fit("No universal collapse or delay threshold", 410, "bold", 6.2), color=STOCK, weight="bold")
text(1090, 121, "Model and NFA evidence remain separate",
     size=fit("Model and NFA evidence remain separate", 410, "normal", 5.9), color=GREY)

# Current primary empirical strip; 2022 remains only a sensitivity in the manuscript.
box(10, 20, 1308, 73, fc="#f0f4f8", ec="#c3d3e3", lw=1.1, radius=6)
text(669, 78, "NFA EDITION 2026  ·  WORLD  ·  1961–2023 COMPLETE OBSERVATIONS", size=7.0, color=DARK, weight="bold")
nfa_line = f"B +{nfa['B_change_pct']:.2f}%   |   B/person {nfa['B_per_person_change_pct']:.2f}%   |   cropland {nfa['cropland_ratio']:.4f}×   |   forest {nfa['forest_ratio']:.4f}×   |   built-up {nfa['built_up_ratio']:.4f}×"
text(669, 56, nfa_line, size=fit(nfa_line, 1260, "bold", 6.8), color=DARK, weight="bold")
text(669, 35, "Annual account values—not physical-stock observations. Estimated 2024–2025 rows excluded; 2022 is a sensitivity check.",
     size=fit("Annual account values—not physical-stock observations. Estimated 2024–2025 rows excluded; 2022 is a sensitivity check.", 1260, "normal", 6.2), color=GREY)

fig.canvas.draw()
metadata = {"Title": "ECOMOD C19 GA01 graphical abstract", "CreationDate": datetime(2026, 10, 31, tzinfo=timezone.utc), "ModDate": datetime(2026, 10, 31, tzinfo=timezone.utc)}
fig.savefig(ROOT / "ecomod_C19_GA01_graphical_abstract.pdf", dpi=DPI, facecolor="white", metadata=metadata)
fig.savefig(ROOT / "ecomod_C19_GA01_graphical_abstract.png", dpi=DPI, facecolor="white")
fig.savefig(ROOT / "ecomod_C19_GA01_graphical_abstract.svg", dpi=DPI, facecolor="white",
            metadata={"Title": "ECOMOD C19 GA01 graphical abstract", "Date": "2026-10-31", "Creator": "C19 GA01 builder"})
fig.savefig(ROOT / "ecomod_C19_GA01_graphical_abstract.tiff", dpi=DPI, facecolor="white", pil_kwargs={"compression": "tiff_lzw"})
plt.close(fig)

# Submission-friendly rasters: opaque RGB, fixed resolution, lossless TIFF.
for suffix in ("png", "tiff"):
    raster_path = ROOT / f"ecomod_C19_GA01_graphical_abstract.{suffix}"
    with Image.open(raster_path) as source:
        rgba = source.convert("RGBA")
        rgb = Image.new("RGB", rgba.size, "white")
        rgb.paste(rgba, mask=rgba.getchannel("A"))
    save_options = {"dpi": (DPI, DPI)}
    if suffix == "tiff":
        save_options["compression"] = "tiff_lzw"
    rgb.save(raster_path, **save_options)

claims = {
    "version": "C19_GA01",
    "date": "2026-10-31",
    "manuscript_title": "A rising biocapacity total can mask ecological-capital land drawdown: a two-land model",
    "canvas": {"width_px": W, "height_px": H, "dpi": DPI},
    "baseline": baseline,
    "NFA_primary_1961_2023": nfa,
    "reduced_branch": {"E_ceiling_gha": 1.138409091, "slow_eigenvalue_per_yr_approx": -0.054, "scope": "reduced fixed-demand equality relation; no universal collapse or delay claim"},
    "source_hashes": {
        "selected_model_code": sha(C19 / "code/reproduce_two_land_C18_A01.py"),
        "empirical_endpoints": sha(C19 / "data/empirical_endpoints_C18_A01.csv"),
        "empirical_components": sha(C19 / "data/empirical_components_C18_A01.csv"),
        "quality_law_comparison": sha(C19 / "data/quality_law_comparison_C18_A01.csv"),
    },
    "scientific_boundaries": [
        "B and its land-class contributions are annual account amounts, not physical-stock measurements.",
        "The selected trajectory is a representative conditional model run, not a forecast or fitted historical reconstruction.",
        "The no-fold/no-critical-slowing statement applies to the reduced fixed-demand branch.",
        "NFA 1961–2023 evidence is separate from the model simulation; 2022 is a same-edition sensitivity.",
    ],
}
(ROOT / "graphical_abstract_claims_C19_GA01.json").write_text(json.dumps(claims, indent=2) + "\n")
print(json.dumps({"baseline": baseline, "NFA": nfa, "outputs": ["pdf", "png", "svg", "tiff"]}, indent=2))
