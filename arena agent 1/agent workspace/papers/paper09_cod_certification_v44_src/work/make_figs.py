#!/usr/bin/env python3
"""Figures for paper09 v44, generated from work/results.json only.
Run from work/:  python3 -u make_figs.py   -> ../figs/fig_*.pdf (and .png)
"""
import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(HERE, "results.json")))
C, E, A = R["cod"], R["edwards"], R["archive"]
FIGS = os.path.join(HERE, "..", "figs")
os.makedirs(FIGS, exist_ok=True)

plt.rcParams.update({"font.size": 9, "axes.titlesize": 9.5, "axes.labelsize": 9, "legend.fontsize": 7.5,
                     "xtick.labelsize": 8, "ytick.labelsize": 8, "figure.dpi": 150, "savefig.bbox": "tight",
                     "axes.spines.top": False, "axes.spines.right": False})
COL = {"BAU": "#1f3b73", "flat_0": "#6a994e", "flat_25": "#bc4749", "flat_50": "#e07a1f", "flat_75": "#8e44ad",
       "flat_100": "#555555", "S1": "#2a9d8f", "cpm": "#d1495b", "flat_90": "#bc4749", "flat_80": "#e07a1f",
       "flat_60": "#8e44ad"}
LAB_COD = {"BAU": "BAU (5 kt)", "flat_0": "zero catch", "flat_25": "flat 60 kt", "flat_50": "flat 120 kt",
           "flat_75": "flat 180 kt", "flat_100": "flat 240 kt", "S1": "Stage I", "cpm": "cascade"}
LAB_EDW = {"BAU": "BAU", "flat_90": "flat 90%", "flat_80": "flat 80%", "flat_60": "flat 60%", "flat_0": "zero pumping",
           "S1": "Stage I", "cpm": "cascade"}
CLS = {"UC_min": "worst floor", "UC_q05": "5th-percentile floor", "UC_q10": "10th-percentile floor"}


def save(fig, name):
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGS, f"{name}.{ext}"))
    plt.close(fig)
    print("wrote", name)


# --------------------------------------------------------------------------- fig 1: data
def fig_data():
    d = C["data"]
    yrs = np.array(d["years"]); S = np.array(d["ssb_kt"]); Ct = np.array(d["catch_kt"])
    oos = C["fit"].get("oos_years") or []
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.7))
    ax = axes[0]
    ax.bar(yrs, Ct, color="#c9c9c9", width=0.8, label="catch (kt)")
    ax.plot(yrs, S, "o-", ms=2.5, lw=1.2, color=COL["BAU"], label="SSB (kt)")
    ax.axhline(C["K_star"], color=COL["cpm"], lw=1, ls="--", label=f"LRP {C['K_star']:.0f} kt")
    ax.axvspan(2007.5, yrs.max() + 0.5, color="#f1e3a8", alpha=0.5, lw=0, label="out of sample 2008-2015")
    ax.set_yscale("log"); ax.set_ylabel("kt (log scale)"); ax.set_title("(a) Northern cod 2J3KL, 1983-2015 (fit 1983-2007)")
    ax.legend(loc="center right", ncol=1, frameon=False)
    ax = axes[1]
    de = E["data"]
    y = np.array(de["years"]); H = np.array(de["H"]); P = np.array(de["P"]); Rr = np.array(de["R"])
    ax2 = ax.twinx()
    ax2.bar(y, Rr, color="#d9ecf2", width=0.8, label="recharge")
    ax2.plot(y, P, color="#999999", lw=0.9, label="pumping")
    ax2.set_ylabel("10^3 acre-ft", color="#666666"); ax2.spines["right"].set_visible(True)
    ax.plot(y, H, color=COL["BAU"], lw=1.3, label="J-17 head (ft)")
    ax.axhline(618, color=COL["cpm"], lw=1, ls="--", label="618 ft"); ax.axhline(660, color=COL["S1"], lw=1, ls=":", label="660 ft")
    ax.axvspan(1990.5, y.max() + 0.5, color="#f1e3a8", alpha=0.5, lw=0)
    ax.set_zorder(ax2.get_zorder() + 1); ax.patch.set_visible(False)
    ax.set_ylabel("ft above msl"); ax.set_title("(b) Edwards Aquifer J-17, 1934-2023")
    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper left", ncol=2, frameon=False)
    save(fig, "fig_data")


# --------------------------------------------------------------------------- fig 2: cod kernels vs T
def fig_cod_kernels():
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 2.8), sharey=True)
    Ts = [1, 2, 3, 5, 8, 10, 15, 20]
    for ax, cls in zip(axes, ("UC_min", "UC_q05", "UC_q10")):
        for pid in ("BAU", "flat_25", "flat_50", "flat_75"):
            k = C["kernels"][pid][cls]
            ys = [k[str(T)] for T in Ts]
            ax.plot([T for T, v in zip(Ts, ys) if v is not None], [v for v in ys if v is not None], "o-", ms=2.5, lw=1.1,
                    color=COL[pid], label=LAB_COD[pid] + " (nominal)")
            ex = C["exact_bounded_defect"][pid][cls]["boundaries_T1_20"]
            xs = [t + 1 for t, v in enumerate(ex) if v is not None]
            ax.plot(xs, [v for v in ex if v is not None], "s--", ms=2.3, lw=0.9, color=COL[pid], alpha=0.75,
                    label=LAB_COD[pid] + " (exact bounded defect)")
        cflat = {"BAU": "0.0", "flat_25": "60.0", "flat_50": "120.0", "flat_75": "180.0"}
        lb = C["lipschitz_boundaries"]["0.0"][cls]
        xs = [t + 1 for t, v in enumerate(lb) if v is not None]
        ax.plot(xs, [v for v in lb if v is not None], "^:", ms=3, lw=0.9, color="black", label="zero catch (Lipschitz certificate)")
        ax.axhline(C["K_star"], color="grey", lw=0.8, ls="--")
        ax.axhline(10000, color="grey", lw=0.6, ls=":")
        ax.set_yscale("log"); ax.set_xlabel("horizon T (years)"); ax.set_title(CLS[cls])
        ax.set_xlim(0.5, 20.5)
    axes[0].set_ylabel("lower kernel boundary (kt, log)")
    h, l = axes[2].get_legend_handles_labels()
    fig.legend(h, l, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.08))
    save(fig, "fig_cod_kernels")


# --------------------------------------------------------------------------- fig 3: cod identification
def fig_cod_ident():
    kg = A["k_grid"]
    Ks = np.array([float(r["K"]) for r in kg]); g = np.array([float(r["g_Kstar"]) for r in kg])
    Fp = np.array([float(r["Fp_Kstar"]) for r in kg])
    cstar = g - C["constants"]["classes_abs"]["UC_q10"]
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.7))
    ax = axes[0]
    ax.plot(Ks, cstar, "o-", ms=2.5, lw=1.1, color=COL["BAU"], label="C* under the q10 floor")
    ax.axhline(0, color="grey", lw=0.7)
    ax.axhline(60, color=COL["flat_25"], lw=0.9, ls="--", label="60 kt (Stage I, cascade, flat 60)")
    ax.axhline(120, color=COL["flat_50"], lw=0.9, ls="--", label="120 kt")
    ax.axvspan(C["profile"]["K_set"][0], 50000, color="#e8f1e4", lw=0, label="profile 95% set (2-par cut)")
    ax.axvline(1775, color="#6a994e", lw=0.8, ls=":", label="F'(LRP)=1 at K=2 LRP")
    ax.set_xscale("log"); ax.set_xlabel("carrying capacity K (kt, log)"); ax.set_ylabel("kt")
    ax.set_title("(a) C* and the catch levels across K"); ax.legend(frameon=True, framealpha=0.95, edgecolor="none", loc="lower right", fontsize=7)
    ax = axes[1]
    b = C["bootstrap_independent_fixedK"]
    arch = A["bootstrap_fixedK"]
    ff = b["frozen_floor"]
    ax.bar([0], [ff["Cstar_median"]], color=COL["BAU"], width=0.5)
    ax.errorbar([0], [ff["Cstar_median"]], yerr=[[ff["Cstar_median"] - ff["Cstar_q05_q95"][0]], [ff["Cstar_q05_q95"][1] - ff["Cstar_median"]]],
                fmt="none", ecolor="black", capsize=4)
    rf = b["reestimated_floor"]
    ax.bar([1], [rf["Cstar_median"]], color=COL["S1"], width=0.5)
    ax.errorbar([1], [rf["Cstar_median"]], yerr=[[rf["Cstar_median"] - rf["Cstar_q05_q95"][0]], [rf["Cstar_q05_q95"][1] - rf["Cstar_median"]]],
                fmt="none", ecolor="black", capsize=4)
    ax.axhline(C["constants"]["C_star"]["UC_q10"], color="grey", lw=0.9, ls="--", label=f"registered C* = {C['constants']['C_star']['UC_q10']:.1f} kt")
    ax.axhline(60, color=COL["flat_25"], lw=0.9, ls="--", label="60 kt")
    ax.axhline(0, color="black", lw=0.7)
    ax.set_xticks([0, 1]); ax.set_xticklabels([f"frozen floor\n(P(C*<=0)={ff['share_nonpositive']:.3f})", f"re-estimated floor\n(P(C*<=0)={rf['share_nonpositive']:.3f})"])
    ax.set_ylabel("C* (kt): median and 90% interval"); ax.set_title("(b) Fixed-K trajectory bootstrap, B=2000")
    ax.legend(frameon=False, loc="upper left")
    save(fig, "fig_cod_ident")


# --------------------------------------------------------------------------- fig 4: edwards kernels
def fig_edw_kernels():
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.0), gridspec_kw={"width_ratios": [1.25, 1]})
    ax = axes[0]
    pids = ["BAU", "flat_90", "S1", "flat_80", "cpm", "flat_60", "flat_0"]
    x = np.arange(len(pids))
    w = 0.27
    for j, cls in enumerate(("UC_min", "UC_q05", "UC_q10")):
        vals = [E["attractors"][p][cls]["self_consistent"] for p in pids]
        ax.bar(x + (j - 1) * w, vals, width=w, color=["#1f3b73", "#5b7db1", "#a9bedc"][j], label=CLS[cls])
    ab = {r["policy"]: r for r in A["edw_audit_bootstrap"]["per_policy"]}
    key = {"BAU": "BAU", "flat_90": "flat-90%", "flat_80": "flat-80%", "flat_60": "flat-60%", "flat_0": "flat-0%", "S1": "flat-80%", "cpm": "flat-60%"}
    for i, p in enumerate(pids):
        if key[p] in ab:
            q = ab[key[p]]["boot_q05_q50_q95"]
            ax.plot([i - w, i - w], [q[0], q[2]], color="black", lw=1)
    ax.axhline(618, color=COL["cpm"], lw=1, ls="--", label="618 ft"); ax.axhline(660, color=COL["S1"], lw=1, ls=":", label="660 ft")
    ax.set_ylim(585, 705); ax.set_xticks(x); ax.set_xticklabels([LAB_EDW[p] for p in pids], rotation=30, ha="right")
    ax.set_ylabel("attractor H* (ft)"); ax.set_title("(a) Attractors by rule and floor (90% bootstrap bars)")
    ax.legend(frameon=False, loc="upper left", ncol=2)
    ax = axes[1]
    Ts = list(range(1, 13))
    for p in ("BAU", "flat_80", "S1", "cpm", "flat_0"):
        k = E["kernels_certified"]["K_phys_618"][p]["UC_min"]
        ys = [k[str(T)] for T in Ts]
        xs = [T for T, v in zip(Ts, ys) if v is not None]
        ax.plot(xs, [v for v in ys if v is not None], "o-", ms=3, lw=1.1, color=COL[p], label=LAB_EDW[p] + " (certified)")
    kb = E["kernels_nominal"]["K_phys_618"]["BAU"]["UC_min"]
    xs = [T for T in Ts if kb.get(str(T)) is not None]
    ax.plot(xs, [kb[str(T)] for T in xs], "s--", ms=2.5, lw=0.9, color=COL["BAU"], alpha=0.6, label="BAU (nominal)")
    be = E["bounded_error"]["BAU"]["UC_min|oos"]["boundaries"]
    xs = [t + 1 for t, v in enumerate(be) if v is not None]
    ax.plot(xs, [v for v in be if v is not None], "^:", ms=3.5, lw=0.9, color="black", label="BAU (out-of-sample defect)")
    ax.axhline(710, color="grey", lw=0.7, ls=":"); ax.axhline(618, color=COL["cpm"], lw=1, ls="--")
    ax.set_xlabel("horizon T (years)"); ax.set_ylabel("lower kernel boundary (ft)"); ax.set_title("(b) 618-ft kernels, worst floor")
    ax.set_xlim(0.5, 12.5); ax.set_ylim(610, 715)
    ax.legend(frameon=False, loc="upper center", ncol=2, bbox_to_anchor=(0.5, -0.22))
    save(fig, "fig_edw_kernels")


# --------------------------------------------------------------------------- fig 5: edwards replays
def fig_edw_replay():
    de = E["data"]; y = np.array(de["years"]); H = np.array(de["H"])
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.7), sharey=True)
    for ax, win, title in zip(axes, ("train_1934_1990", "oos_1991_2023"), ("(a) Closed loop 1934-1990", "(b) Closed loop from the 1990 head")):
        ax.plot(y, H, color="black", lw=1.0, label="observed")
        for p in ("BAU", "flat_90", "S1", "cpm", "flat_0"):
            path = E["closed_loop"][p][win]["path"]
            ax.plot([q[0] for q in path], [q[1] for q in path], lw=1.1, color=COL[p], label=LAB_EDW[p])
        ax.axhline(618, color=COL["cpm"], lw=0.9, ls="--"); ax.axhline(660, color=COL["S1"], lw=0.9, ls=":")
        ax.set_title(title); ax.set_xlabel("year")
        if win.startswith("train"):
            ax.set_xlim(1933, 1991)
        else:
            ax.set_xlim(1989, 2024)
    axes[0].set_ylabel("J-17 head (ft)"); axes[0].legend(frameon=False, ncol=2, loc="lower left")
    save(fig, "fig_edw_replay")


# --------------------------------------------------------------------------- fig 6: horizons
def fig_horizons():
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.6), gridspec_kw={"width_ratios": [1.5, 1]})
    ax = axes[0]
    pids = ["BAU", "flat_0", "flat_25", "S1", "cpm", "flat_50", "flat_75", "flat_100"]
    x = np.arange(len(pids)); w = 0.26
    for j, cls in enumerate(("UC_min", "UC_q05", "UC_q10")):
        ex = []
        for p in pids:
            v = C["exact_bounded_defect"][p][cls]["last_nonempty"]
            ex.append(400 if isinstance(v, str) else v)
        ax.bar(x + (j - 1) * w, ex, width=w, color=["#1f3b73", "#5b7db1", "#a9bedc"][j], label=f"exact, {CLS[cls]}")
        lip = []
        for p in pids:
            v = C["exact_bounded_defect"][p][cls]["lipschitz_last_nonempty"]
            if v is None:  # staged rules: certificate of the stage at the LRP (60 kt)
                v = C["certified_horizon"]["60.0"][cls]["last_nonempty"]
            lip.append(v)
        ax.plot(x + (j - 1) * w, lip, "_", color="black", ms=7, mew=1.5, label="Lipschitz certificate" if j == 0 else None)
    ax.set_xticks(x); ax.set_xticklabels([LAB_COD[p] for p in pids], rotation=30, ha="right")
    ax.set_ylabel("certified horizon (years)"); ax.set_title("(a) Cod LRP: exact kernel vs Lipschitz certificate")
    ax.set_ylim(0, 32); ax.legend(frameon=False, ncol=1, loc="upper right")
    ax = axes[1]
    pids = ["BAU", "flat_90", "flat_80", "S1", "cpm", "flat_0"]
    x = np.arange(len(pids)); w = 0.38
    tr = [E["bounded_error"][p]["UC_min|train"]["first_empty"] - 1 for p in pids]
    oo = [E["bounded_error"][p]["UC_min|oos"]["first_empty"] - 1 for p in pids]
    ax.bar(x - w / 2, tr, width=w, color="#1f3b73", label="declared defect (15.4 ft)")
    ax.bar(x + w / 2, oo, width=w, color="#a9bedc", label="out-of-sample defect (21.8 ft)")
    ax.set_xticks(x); ax.set_xticklabels([LAB_EDW[p] for p in pids], rotation=30, ha="right")
    ax.set_title("(b) Edwards 618 ft, worst floor"); ax.set_ylim(0, 6); ax.legend(frameon=False, loc="upper left")
    save(fig, "fig_horizons")


if __name__ == "__main__":
    fig_data(); fig_cod_kernels(); fig_cod_ident(); fig_edw_kernels(); fig_edw_replay(); fig_horizons()
    print("figures done")
