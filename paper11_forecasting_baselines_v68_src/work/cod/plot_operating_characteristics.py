#!/usr/bin/env python3
"""Build Paper11 Fig. 6 from the hash-validated power-summary CSV.

D1--D4 show the true-module retention rate; D5--D7 show any-module
retention. For the manuscript, the CSV must contain all 200 replicates per
cell. The --reps option exists for explicit interim smoke tests only.
"""
from __future__ import annotations

import argparse
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CELLS = [
    "D1_M1_collapse", "D2_M1_recovery", "D3_M2_stockflow", "D4_M1b_depens",
    "D5_persist_null", "D6_timevarying_r", "D7_obs_error",
]
SIGMAS = (11.8, 33.8)
ROW_LABELS = [
    "D1 autonomous, collapse fit (truth M1)",
    "D2 autonomous, recovery fit (truth M1)",
    "D3 stock-flow (truth M2)",
    r"D4 depensation, $\mathfrak{s}=15$ kt (truth M1b)",
    "D5 persistence-true (no structure)",
    "D6 drifting productivity (outside class)",
    "D7 smooth path + observation error (outside class)",
]


def build_fig6(summary_path: str, output_prefix: str, expected_reps: int = 200) -> None:
    """Validate and plot the two rates used for each DGP/noise cell."""
    summary = pd.read_csv(summary_path)
    required = {
        "cell", "sigma", "n_reps", "true_module_rate", "any_module_retention_rate",
    }
    missing = required - set(summary.columns)
    if missing:
        raise ValueError(f"summary lacks required columns: {sorted(missing)}")
    if summary.duplicated(["cell", "sigma"]).any():
        raise ValueError("summary has duplicate cell/noise rows")
    expected = {(cell, sigma) for cell in CELLS for sigma in SIGMAS}
    observed = {(str(r.cell), float(r.sigma)) for r in summary.itertuples(index=False)}
    if observed != expected:
        raise ValueError(f"summary cell coverage mismatch: missing={expected-observed}, extra={observed-expected}")
    if not (summary["n_reps"].astype(int) == expected_reps).all():
        raise ValueError(f"Fig. 6 requires exactly {expected_reps} replicates in every cell")

    keyed = summary.set_index(["cell", "sigma"])
    rates = []
    for i, cell in enumerate(CELLS):
        metric = "true_module_rate" if i < 4 else "any_module_retention_rate"
        rates.append([float(keyed.loc[(cell, sigma), metric]) for sigma in SIGMAS])
    vals = pd.DataFrame(rates).to_numpy(dtype=float)
    if not ((vals >= 0.0) & (vals <= 1.0)).all():
        raise ValueError("retention rates must be finite and lie in [0, 1]")

    plt.rcParams.update({
        "font.size": 9, "axes.titlesize": 9.5, "axes.labelsize": 9,
        "xtick.labelsize": 8, "ytick.labelsize": 8,
        "axes.spines.top": False, "axes.spines.right": False,
        "figure.dpi": 150, "savefig.dpi": 300,
        "pdf.fonttype": 42, "lines.linewidth": 1.4,
    })
    fig, ax = plt.subplots(figsize=(7.2, 3.5))
    im = ax.imshow(vals, cmap=plt.get_cmap("Blues"), vmin=0, vmax=1, aspect="auto")
    for i in range(vals.shape[0]):
        for j in range(2):
            rate = vals[i, j]
            if i <= 3:
                mark = "✓" if rate >= 0.80 else ("~" if rate >= 0.30 else "✗")
            else:
                mark = "✓" if rate <= 0.10 else "✗"
            ax.text(j, i, f"{rate:.3f}  {mark}", ha="center", va="center", fontsize=8.5,
                    color="white" if rate > 0.55 else "black")
    ax.set_xticks([0, 1])
    ax.set_xticklabels([r"$\sigma=11.8$ kt", r"$\sigma=33.8$ kt"])
    ax.set_yticks(range(7))
    ax.set_yticklabels(ROW_LABELS, fontsize=8)
    ax.axhline(3.5, color="k", lw=0.8)
    ax.axhline(4.5, color="k", lw=0.8)
    ax.text(1.62, 1.5, "power\nP(true module retained)\npre-declared bar: ≥ 0.80\n✓ met, ~ 0.30–0.80, ✗ < 0.30",
            va="center", fontsize=7.5)
    ax.text(1.62, 4.0, "false retention, in-class null\nP(any module retained)\nbar: ≤ 0.10",
            va="center", fontsize=7.5)
    ax.text(1.62, 5.5, "false retention, truth outside the class\nP(any module retained)\nbar: ≤ 0.10",
            va="center", fontsize=7.5)
    ax.set_xlim(-0.5, 3.4)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(length=0)
    fig.tight_layout()

    outdir = os.path.dirname(os.path.abspath(output_prefix))
    os.makedirs(outdir, exist_ok=True)
    for ext in ("pdf", "png"):
        fig.savefig(f"{output_prefix}.{ext}", bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {output_prefix}.pdf and {output_prefix}.png (n={expected_reps} per cell)")
    for cell, vals_row in zip(CELLS, vals):
        print(f"  {cell}: {vals_row[0]:.3f}, {vals_row[1]:.3f}")


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", default=os.path.join(here, "power_simulation_repro_summary.csv"))
    parser.add_argument("--output", default=os.path.join(here, "..", "figs", "fig6_operating"))
    parser.add_argument("--reps", type=int, default=200,
                        help="expected replicates per cell (use non-200 only for explicitly interim checks)")
    args = parser.parse_args()
    build_fig6(args.summary, args.output, expected_reps=args.reps)


if __name__ == "__main__":
    main()
