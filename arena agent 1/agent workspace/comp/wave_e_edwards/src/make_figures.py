#!/usr/bin/env python3
"""Figures for the Edwards Wave E manuscript."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RES = ROOT / "results"
MS = ROOT / "manuscript"
MS.mkdir(exist_ok=True)

plt.rcParams.update(
    {
        "figure.dpi": 140,
        "savefig.dpi": 160,
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "legend.fontsize": 8,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


def save(fig, name):
    fig.savefig(MS / f"{name}.png", bbox_inches="tight")
    fig.savefig(MS / f"{name}.svg", bbox_inches="tight")
    plt.close(fig)


def fig1(panel):
    fig, ax = plt.subplots(figsize=(8.2, 3.8))
    ax.plot(panel.year, panel.H_mean, color="#1f4e79", lw=1.4, label="J-17 annual mean")
    ax.fill_between(panel.year, panel.H_min, panel.H_max, color="#1f4e79", alpha=0.12, label="daily high range")
    ax.axhline(660, color="#b45309", ls="--", lw=1, label="Stage I 660 ft (post-2007)")
    ax.axhline(618, color="#9f1239", ls=":", lw=1, label="Comal cease ≈ 618 ft")
    ax.set_ylabel("J-17 elevation (ft AMSL)")
    ax.set_xlabel("Year")
    ax.set_xlim(1934, 2023)
    ax.legend(loc="lower right", frameon=False)
    ax.set_title("Primary z: Edwards San Antonio Pool, well J-17")
    save(fig, "fig1_series")


def fig2(panel, paths):
    fig, axes = plt.subplots(2, 2, figsize=(8.6, 5.8), sharey=True)
    axes = axes.ravel()
    windows = [
        ("dor_drawdown", "DOR drawdown 1951–56"),
        ("dor_recovery", "DOR recovery 1957–61"),
        ("prepermit_wet", "Pre-permit wet 1991–95"),
        ("cpm_era", "CPM era 2015–23"),
    ]
    colors = {
        "naive_persist": "#111827",
        "M1": "#2563eb",
        "M2": "#059669",
        "M2_oracle": "#d97706",
    }
    for ax, (key, title) in zip(axes, windows):
        ax.set_title(title)
        shown = False
        for model, col in colors.items():
            rec = paths.get(f"{key}:{model}")
            if not rec:
                continue
            ls = "--" if model == "M2_oracle" else "-"
            ax.plot(rec["year"], rec["pred"], color=col, ls=ls, lw=1.3, label=model if not shown else None)
        # obs from persist rec
        rec = paths[f"{key}:naive_persist"]
        ax.plot(rec["year"], rec["obs"], color="#1f4e79", lw=2.0, label="obs" if not shown else None)
        ax.axhline(660, color="#b45309", ls="--", lw=0.7)
        shown = True
    handles = [
        plt.Line2D([0], [0], color="#1f4e79", lw=2, label="observed"),
        plt.Line2D([0], [0], color="#111827", lw=1.3, label="persist"),
        plt.Line2D([0], [0], color="#2563eb", lw=1.3, label="M1"),
        plt.Line2D([0], [0], color="#059669", lw=1.3, label="M2 causal"),
        plt.Line2D([0], [0], color="#d97706", lw=1.3, ls="--", label="M2 oracle"),
    ]
    axes[0].legend(handles=handles, loc="best", frameon=False)
    axes[0].set_ylabel("ft AMSL")
    axes[2].set_ylabel("ft AMSL")
    fig.suptitle("Fixed-window multi-step forecasts (oracle is not a retention candidate)")
    fig.tight_layout()
    save(fig, "fig2_windows")


def fig3(summary):
    h1 = summary[summary.horizon == 1].copy()
    h5 = summary[summary.horizon == 5].copy()
    order = ["naive_persist", "naive_mean", "M1", "M2", "M2m", "M3", "M4", "M2_oracle"]
    labels = ["persist", "mean", "M1", "M2", "M2m", "M3", "M4", "M2 oracle"]
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    x = np.arange(len(order))
    w = 0.38
    y1 = [float(h1.set_index("model").loc[m, "rmse"]) for m in order]
    y5 = [float(h5.set_index("model").loc[m, "rmse"]) for m in order]
    ax.bar(x - w / 2, y1, w, color="#1f4e79", label="h = 1")
    ax.bar(x + w / 2, y5, w, color="#94a3b8", label="h = 5")
    ax.axhline(y1[0], color="#9f1239", ls=":", lw=1, label="persist h=1")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("RMSE (ft)")
    ax.set_title("Rolling-origin RMSE on J-17 annual mean")
    ax.legend(frameon=False)
    save(fig, "fig3_rmse")


def fig4(panel):
    fig, ax = plt.subplots(figsize=(8.2, 3.6))
    ax2 = ax.twinx()
    ax.plot(panel.year, panel.H_mean, color="#1f4e79", lw=1.4, label="J-17")
    ax2.plot(panel.year, panel.Q_comal, color="#0f766e", lw=1.1, alpha=0.85, label="Comal (fibre)")
    ax.set_ylabel("J-17 (ft AMSL)", color="#1f4e79")
    ax2.set_ylabel("Comal mean (cfs)", color="#0f766e")
    ax.set_xlabel("Year")
    ax.set_title("Fibre Y: Comal Springs — not used for retention")
    save(fig, "fig4_fibre")


def fig5():
    h = pd.read_csv(RES / "pass2_H_summary.csv")
    h1 = h[h.horizon == 1].set_index("model")["rmse"]
    h5 = h[h.horizon == 5].set_index("model")["rmse"]
    order = [
        "naive_persist",
        "M1",
        "M2_Rar",
        "M2_enso",
        "M2_precip",
        "M2_combo",
        "M2_precip_oracle",
    ]
    labels = ["persist", "M1", "R AR", "ENSO", "lag rain", "combo", "rain oracle"]
    fig, ax = plt.subplots(figsize=(8.0, 3.8))
    x = np.arange(len(order))
    w = 0.38
    y1 = [float(h1.loc[m]) for m in order]
    y5 = [float(h5.loc[m]) for m in order]
    ax.bar(x - w / 2, y1, w, color="#1f4e79", label="h = 1")
    ax.bar(x + w / 2, y5, w, color="#94a3b8", label="h = 5")
    ax.axhline(y1[0], color="#9f1239", ls=":", lw=1, label="persist h=1")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("RMSE (ft)")
    ax.set_title("Pass 2: causal recharge modules on J-17 (rain oracle excluded)")
    ax.legend(frameon=False)
    save(fig, "fig5_pass2")


def main():
    panel = pd.read_csv(DATA / "annual_panel.csv")
    panel = panel[panel.year.between(1934, 2023)]
    summary = pd.read_csv(RES / "rolling_summary.csv")
    with open(RES / "paths.json") as f:
        paths = json.load(f)
    fig1(panel)
    fig2(panel, paths)
    fig3(summary)
    fig4(panel)
    fig5()
    print("wrote figures in", MS)


if __name__ == "__main__":
    main()
