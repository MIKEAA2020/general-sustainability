#!/usr/bin/env python3
"""Generate the v51 graphical abstract for the typed-ledger paper.

Outputs editable/vector and raster versions beside the manuscript:
``paper3_material_ledgers_v51_graphical_abstract.{svg,pdf,png}``.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle


# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------
NAVY = "#17324F"
INK = "#243447"
Muted = "#687687"
TEAL = "#0E7C7B"
TEAL_DARK = "#075E63"
GREEN = "#4C956C"
AMBER = "#E9A13B"
RED = "#C44536"
PURPLE = "#6C5B7B"
LIGHT = "#F6F8FA"
LIGHT_TEAL = "#E7F3F2"
LIGHT_AMBER = "#FFF3DE"
LIGHT_RED = "#FBE9E5"
LIGHT_PURPLE = "#F0ECF5"
LINE = "#CFD8E3"

mpl.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "mathtext.fontset": "dejavusans",
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
    }
)


def rounded_box(ax, xy, width, height, facecolor="white", edgecolor=LINE,
                linewidth=1.4, radius=0.09, zorder=2, alpha=1.0):
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle=f"round,pad=0.025,rounding_size={radius}",
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
        zorder=zorder,
        alpha=alpha,
    )
    ax.add_patch(patch)
    return patch


def arrow(ax, start, end, color=NAVY, linewidth=2.2, mutation_scale=17,
          connectionstyle="arc3,rad=0.0", linestyle="-", zorder=5,
          shrinkA=1, shrinkB=1):
    patch = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=mutation_scale,
        linewidth=linewidth,
        color=color,
        linestyle=linestyle,
        connectionstyle=connectionstyle,
        shrinkA=shrinkA,
        shrinkB=shrinkB,
        zorder=zorder,
    )
    ax.add_patch(patch)
    return patch


def panel_title(ax, x, y, number, title, color):
    ax.add_patch(Circle((x + 0.22, y), 0.19, facecolor=color, edgecolor="none", zorder=6))
    ax.text(x + 0.22, y - 0.015, str(number), ha="center", va="center",
            fontsize=13, weight="bold", color="white", zorder=7)
    ax.text(x + 0.52, y, title, ha="left", va="center", fontsize=17,
            weight="bold", color=NAVY, zorder=7)


def component_bar(ax, x, y, label, value, color):
    centre = x + 1.58
    scale = 0.18
    ax.add_patch(Circle((x + 0.18, y), 0.17, facecolor=color,
                        edgecolor="none", zorder=5))
    ax.text(x + 0.18, y - 0.01, label, ha="center", va="center", fontsize=10.5,
            weight="bold", color="white", zorder=6)
    ax.plot([centre, centre], [y - 0.23, y + 0.23], color="#9AA8B8", lw=1.2, zorder=3)
    left = centre if value >= 0 else centre + value * scale
    width = abs(value) * scale
    ax.add_patch(Rectangle((left, y - 0.14), width, 0.28, facecolor=color,
                           edgecolor="none", zorder=4))
    label_x = centre + value * scale + (0.09 if value >= 0 else -0.09)
    align = "left" if value >= 0 else "right"
    ax.text(label_x, y, f"{value:+d}", ha=align, va="center", fontsize=11,
            weight="bold", color=color)


def ledger_node(ax, xy, width, height, title, subtitle, face, edge):
    rounded_box(ax, xy, width, height, facecolor=face, edgecolor=edge,
                linewidth=1.6, radius=0.12, zorder=4)
    x, y = xy
    ax.text(x + width / 2, y + height * 0.61, title, ha="center", va="center",
            fontsize=11.5, weight="bold", color=NAVY, zorder=6)
    ax.text(x + width / 2, y + height * 0.31, subtitle, ha="center", va="center",
            fontsize=8.8, color=INK, zorder=6)


def certificate_row(ax, x, y, width, title, detail, symbol, color, face):
    rounded_box(ax, (x, y - 0.31), width, 0.62, facecolor=face,
                edgecolor=color, linewidth=1.25, radius=0.09, zorder=3)
    ax.add_patch(Circle((x + 0.31, y), 0.20, facecolor=color,
                        edgecolor="none", zorder=5))
    ax.text(x + 0.31, y - 0.01, symbol, ha="center", va="center", fontsize=12,
            weight="bold", color="white", zorder=6)
    ax.text(x + 0.67, y + 0.12, title, ha="left", va="center", fontsize=12.5,
            weight="bold", color=NAVY, zorder=6)
    ax.text(x + 0.67, y - 0.16, detail, ha="left", va="center", fontsize=9.1,
            color=INK, zorder=6)


def time_pill(ax, x, y, width, title, detail, color, face):
    rounded_box(ax, (x, y), width, 0.78, facecolor=face, edgecolor=color,
                linewidth=1.4, radius=0.14, zorder=3)
    # Simple clock glyph.
    cx, cy = x + 0.35, y + 0.39
    ax.add_patch(Circle((cx, cy), 0.20, facecolor="white", edgecolor=color,
                        linewidth=1.8, zorder=5))
    ax.plot([cx, cx], [cy, cy + 0.11], color=color, lw=1.8, zorder=6)
    ax.plot([cx, cx + 0.09], [cy, cy - 0.03], color=color, lw=1.8, zorder=6)
    ax.text(x + 0.68, y + 0.50, title, ha="left", va="center", fontsize=11.7,
            weight="bold", color=NAVY, zorder=6)
    ax.text(x + 0.68, y + 0.23, detail, ha="left", va="center", fontsize=9.4,
            color=INK, zorder=6)


def main() -> None:
    code_dir = Path(__file__).resolve().parent
    manuscript_dir = code_dir.parents[1] / "manuscript"
    stem = manuscript_dir / "paper3_material_ledgers_v51_graphical_abstract"

    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    fig.patch.set_facecolor("white")
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.set_aspect("equal")
    ax.axis("off")

    # Header
    ax.text(8, 8.55, "Don’t compress a material system into one depletion date",
            ha="center", va="center", fontsize=27, weight="bold", color=NAVY)
    ax.text(8, 8.08,
            "A typed ledger separates balance, conservation, safety, closure — and the meaning of “time”.",
            ha="center", va="center", fontsize=14.5, color=Muted)

    # Main panels
    rounded_box(ax, (0.32, 1.98), 4.18, 5.55, facecolor="white",
                edgecolor=LINE, linewidth=1.5, radius=0.16, zorder=1)
    rounded_box(ax, (4.82, 1.98), 5.28, 5.55, facecolor="white",
                edgecolor=LINE, linewidth=1.5, radius=0.16, zorder=1)
    rounded_box(ax, (10.42, 1.98), 5.26, 5.55, facecolor="white",
                edgecolor=LINE, linewidth=1.5, radius=0.16, zorder=1)

    panel_title(ax, 0.58, 7.08, 1, "Scalar compression", RED)
    panel_title(ax, 5.08, 7.08, 2, "Keep the ledger typed", TEAL)
    panel_title(ax, 10.68, 7.08, 3, "Certify separately", PURPLE)

    # Inter-panel arrows
    arrow(ax, (4.53, 4.82), (4.82, 4.82), color=NAVY, linewidth=3.2,
          mutation_scale=20, zorder=8)
    arrow(ax, (10.13, 4.82), (10.42, 4.82), color=NAVY, linewidth=3.2,
          mutation_scale=20, zorder=8)

    # ------------------------------------------------------------------
    # Panel 1: compensatory aggregation
    # ------------------------------------------------------------------
    ax.text(0.66, 6.61, "Schematic component balances", ha="left", va="center",
            fontsize=10.5, style="italic", color=Muted)
    component_bar(ax, 0.66, 6.10, "A", -4, RED)
    component_bar(ax, 0.66, 5.48, "B", +7, TEAL)
    component_bar(ax, 0.66, 4.86, "C", +2, AMBER)
    ax.text(3.88, 6.10, "fails", ha="left", va="center", fontsize=10.5,
            weight="bold", color=RED)

    arrow(ax, (2.42, 4.47), (2.42, 4.08), color=NAVY, linewidth=2.6,
          mutation_scale=18, zorder=6)
    rounded_box(ax, (0.66, 3.02), 3.52, 0.91, facecolor=LIGHT_RED,
                edgecolor=RED, linewidth=1.7, radius=0.13, zorder=3)
    ax.text(2.42, 3.63, r"weighted sum $=+5$", ha="center", va="center",
            fontsize=15, weight="bold", color=NAVY, zorder=5)
    ax.text(2.42, 3.25, "one score · one date · one verdict", ha="center",
            va="center", fontsize=9.4, color=INK, zorder=5)

    ax.text(2.42, 2.58, "The aggregate can pass", ha="center", va="center",
            fontsize=12.2, weight="bold", color=RED)
    ax.text(2.42, 2.29, "while a critical component fails.", ha="center",
            va="center", fontsize=12.2, weight="bold", color=RED)

    # ------------------------------------------------------------------
    # Panel 2: typed stock-flow ledger
    # ------------------------------------------------------------------
    rounded_box(ax, (5.32, 6.25), 4.25, 0.52, facecolor=NAVY,
                edgecolor=NAVY, linewidth=1.2, radius=0.12, zorder=4)
    ax.text(7.445, 6.51, r"$\dot{x}=S_{\mathcal{T}}v+b,\qquad v\geq0$",
            ha="center", va="center", fontsize=15, weight="bold", color="white",
            zorder=6)

    # Nodes (kept strictly inside panel 2: x = 4.82--10.10)
    ledger_node(ax, (5.14, 3.05), 1.34, 0.90, "DONOR", "finite stock",
                "#EAF0F6", NAVY)
    ledger_node(ax, (6.20, 4.62), 1.58, 0.98, "AVAILABLE", "typed stock",
                LIGHT_TEAL, TEAL_DARK)
    ledger_node(ax, (8.25, 4.62), 1.42, 0.98, "IN USE", "pipeline",
                LIGHT_AMBER, "#B87718")
    ledger_node(ax, (8.25, 3.05), 1.42, 0.90, "SINK", "never returned",
                LIGHT_RED, RED)

    # Safety band around available stock
    rounded_box(ax, (6.08, 4.49), 1.82, 1.25, facecolor="none",
                edgecolor=PURPLE, linewidth=1.5, radius=0.16, zorder=2)
    ax.text(6.16, 5.74, "barriers", ha="left", va="center",
            fontsize=8.2, style="italic", color=PURPLE, zorder=7,
            bbox=dict(boxstyle="round,pad=0.12", facecolor="white",
                      edgecolor="none", alpha=0.95))

    # Flux arrows
    arrow(ax, (5.94, 3.96), (6.54, 4.56), color=NAVY, linewidth=2.4,
          mutation_scale=17, zorder=5)
    ax.text(5.91, 4.34, "mobilise", ha="center", va="center", fontsize=9.0,
            color=NAVY, rotation=43)

    arrow(ax, (7.82, 5.13), (8.20, 5.13), color=TEAL_DARK, linewidth=2.6,
          mutation_scale=18, zorder=6)
    # Late-return loop above the two central nodes
    arrow(ax, (8.76, 5.64), (7.30, 5.64), color=TEAL, linewidth=2.4,
          mutation_scale=17, connectionstyle="arc3,rad=0.22", zorder=5)
    ax.text(8.04, 5.99, "late return", ha="center", va="center", fontsize=9.4,
            weight="bold", color=TEAL_DARK,
            bbox=dict(boxstyle="round,pad=0.18", facecolor="white",
                      edgecolor="none", alpha=0.94), zorder=8)

    # Ultimate loss
    arrow(ax, (8.96, 4.58), (8.96, 4.00), color=RED, linewidth=2.5,
          mutation_scale=18, zorder=6)
    ax.text(8.84, 4.29, "ultimate\nloss", ha="right", va="center", fontsize=8.6,
            weight="bold", color=RED)

    # Boundary import and service readout
    arrow(ax, (5.58, 5.82), (6.16, 5.34), color=Muted, linewidth=1.8,
          mutation_scale=15, linestyle=(0, (4, 2)), zorder=5)
    ax.text(5.16, 5.94, r"boundary $b$", ha="left", va="center", fontsize=9.0,
            color=Muted)

    rounded_box(ax, (6.68, 3.58), 1.34, 0.50, facecolor="white",
                edgecolor=PURPLE, linewidth=1.4, radius=0.10, zorder=5)
    ax.text(7.35, 3.83, "service\nreadout", ha="center", va="center",
            fontsize=8.7, weight="bold", color=PURPLE, zorder=6,
            linespacing=0.92)
    arrow(ax, (6.99, 4.47), (6.99, 4.12), color=PURPLE, linewidth=1.9,
          mutation_scale=15, linestyle=(0, (4, 2)), zorder=5)
    ax.text(7.35, 3.39, "not conserved mass", ha="center", va="center",
            fontsize=7.8, style="italic", color=PURPLE)

    # Type discipline chips
    rounded_box(ax, (5.16, 2.25), 2.56, 0.48, facecolor=LIGHT,
                edgecolor=TEAL, linewidth=1.2, radius=0.12, zorder=3)
    ax.text(6.44, 2.49, "substance × place × unit", ha="center", va="center",
            fontsize=9.2, weight="bold", color=TEAL_DARK, zorder=5)
    rounded_box(ax, (7.90, 2.25), 1.80, 0.48, facecolor=LIGHT,
                edgecolor=AMBER, linewidth=1.2, radius=0.12, zorder=3)
    ax.text(8.80, 2.49, "late  ≠  lost", ha="center", va="center",
            fontsize=11.2, weight="bold", color="#8A5A08", zorder=5)

    # ------------------------------------------------------------------
    # Panel 3: separate certification layers
    # ------------------------------------------------------------------
    x3 = 10.78
    w3 = 4.55
    certificate_row(
        ax, x3, 6.28, w3, "BALANCED", r"the declared balance law holds",
        "=", TEAL, LIGHT_TEAL,
    )
    certificate_row(
        ax, x3, 5.43, w3, "CONSERVED", r"$\ell^{\mathsf{T}}S_{\mathcal{T}}=0$ for declared moieties",
        "ℓ", NAVY, "#EDF2F7",
    )
    certificate_row(
        ax, x3, 4.58, w3, "SAFE", "every component stays within its barriers",
        "✓", PURPLE, LIGHT_PURPLE,
    )
    certificate_row(
        ax, x3, 3.73, w3, "CLOSED", "a feasible cycle at declared capacity",
        "↻", "#B87718", LIGHT_AMBER,
    )

    rounded_box(ax, (10.87, 2.28), 4.37, 0.83, facecolor=NAVY,
                edgecolor=NAVY, linewidth=1.2, radius=0.12, zorder=3)
    ax.text(13.055, 2.83, "No free implications", ha="center", va="center",
            fontsize=13.2, weight="bold", color="white", zorder=5)
    ax.text(13.055, 2.50, "cross-layer claims need stated hypotheses",
            ha="center", va="center", fontsize=9.8, color="#DCE6F2", zorder=5)

    # ------------------------------------------------------------------
    # Bottom strip: three meanings of depletion time
    # ------------------------------------------------------------------
    rounded_box(ax, (0.32, 0.28), 15.36, 1.38, facecolor="#F2F6F9",
                edgecolor=LINE, linewidth=1.4, radius=0.16, zorder=1)
    ax.text(0.62, 1.43, "“Depletion time” is not one object:", ha="left",
            va="center", fontsize=13.5, weight="bold", color=NAVY, zorder=5)

    time_pill(ax, 0.62, 0.47, 4.65, "Gross turnover intensity",
              "a pressure scale", TEAL, "white")
    time_pill(ax, 5.67, 0.47, 4.65, "Frozen-rate ratio",
              "a local quotient", "#B87718", "white")
    time_pill(ax, 10.72, 0.47, 4.65, "Scenario hitting time",
              "declared law + barrier", PURPLE, "white")

    ax.text(15.68, 0.10, "Typed Flux Ledgers and Depletion Arithmetic · v51",
            ha="right", va="bottom", fontsize=8.2, color="#8A97A8")

    fig.savefig(stem.with_suffix(".png"), dpi=300, bbox_inches="tight",
                facecolor="white")
    fig.savefig(stem.with_suffix(".svg"), bbox_inches="tight", facecolor="white")
    fig.savefig(stem.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
    plt.close(fig)

    for suffix in (".png", ".svg", ".pdf"):
        path = stem.with_suffix(suffix)
        print(f"created {path.name} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
