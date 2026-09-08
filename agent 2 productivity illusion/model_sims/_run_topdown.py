"""Runner for the corrected top-down analysis (model_sims.topdown).

Regenerates the three top-down figures and writes a JSON record of the verified
results, so the manuscript edits can quote them and the record is reproducible.

Figures
-------
* scans/topdown_delay_boundary.png      (A1: tau_g-driven cliff, no tau_g/tau_p ratio)
* scans/topdown_macro_ratios.png        (A7/A2: basin in the macro-ratio plane)
* scans/topdown_ratio_separation.png    (A7: flow-share separation closed form)
"""
import json
import os
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from model_sims import topdown as T
from model_sims.r1_basin import DEFAULT_GRID

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCANS = os.path.join(ROOT, "scans")
os.makedirs(SCANS, exist_ok=True)
OUT_JSON = os.path.join(ROOT, "data", "topdown_results.json")


def fig_delay_boundary(tg_list, tp_list, A0, P0, out, lastR):
    M = np.zeros((len(tg_list), len(tp_list)))
    for i, tg in enumerate(tg_list):
        for j, tp in enumerate(tp_list):
            M[i, j] = 1 if out[(tg, tp)] == "R" else 0
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    ax.imshow(M, aspect="auto", origin="lower", cmap="RdYlGn", vmin=0, vmax=1,
              extent=[min(tp_list), max(tp_list), min(tg_list), max(tg_list)])
    ax.set_xticks(tp_list); ax.set_xticklabels([str(x) for x in tp_list])
    ax.set_yticks([x for x in tg_list if x in tg_list[:6]] + ([max(tg_list)] if max(tg_list) not in tg_list[:6] else []) + [18, 20, 25, 30])
    ax.set_xlabel(r"$\tau_p$ (demographic delay, yr)", fontsize=9)
    ax.set_ylabel(r"$\tau_g$ (regeneration delay, yr)", fontsize=9)
    tp = np.linspace(1, 60, 200)
    ax.plot(tp, 0.8 * tp, color="blue", ls=":", lw=1.5, label=r"$R=\tau_g/\tau_p=0.8$ (refuted)")
    ax.axhline(19.5, color="black", ls="--", lw=1.4, label=r"$\tau_g\approx19$ yr ($\tau_p$-independent)")
    ax.set_title(f"cliff is regeneration-lag-driven ($A_0$={A0}, $P_0$={P0})", fontsize=9.6)
    ax.legend(fontsize=7, loc="lower left"); ax.grid(alpha=.2)
    fig.tight_layout(); fig.savefig(os.path.join(SCANS, "topdown_delay_boundary.png"), dpi=130)
    plt.close(fig)


def _panel(ax, tg, tp):
    """One (R_B, R_A) basin panel; returns summary dict."""
    gridA, gridP = DEFAULT_GRID["gridA"], DEFAULT_GRID["gridP"]
    RB, RA, lab = [], [], []
    for a0 in gridA:
        for p0 in gridP:
            c = T.corrected_s0(tg=tg, tp=tp, A0=float(a0), P0=float(p0), **T.BASELINE)["cls"]
            if c == "O":
                continue
            rB, rA = T.ratios(a0, p0)
            RB.append(rB); RA.append(rA); lab.append(c)
    RB = np.array(RB); RA = np.array(RA); lab = np.array(lab)
    rec = lab == "R"; col = lab == "C"; sm = col & (RB < 1) & (RA < 1)
    ax.scatter(RB[rec], RA[rec], s=28, c="#2ca02c", alpha=.78, label=f"recovers (n={int(rec.sum())})", edgecolors="none")
    ax.scatter(RB[col], RA[col], s=28, c="#d62728", alpha=.78, label=f"collapses (n={int(col.sum())})", edgecolors="none")
    if int(sm.sum()):
        ax.scatter(RB[sm], RA[sm], s=90, c="none", edgecolor="#1f3b8a", lw=1.4, marker="x",
                   label=f"silent collapse: $R_B$<1 & $R_A$<1 ({int(sm.sum())})")
    ax.axvline(1, color="k", ls="--", lw=1.4); ax.axhline(1, color="k", ls="--", lw=1.4)
    # Place the ratio annotation in the whitespace of the upper-right quadrant:
    # above the dashed R_B=1 / R_A=1 axes, clear of the red collapse curve
    # (points with R_A>1.5 lie at R_B>1.44), and left of the dashed x=1 line.
    ax.text(1.02, 1.48, "$R_B=1$ (E=B, the trigger)\n$R_A=1$ (E=bA)", fontsize=7.2, va="bottom")
    ax.set_xlabel("$R_B=E/B$ (footprint ÷ biocapacity)", fontsize=9)
    ax.set_ylabel("$R_A=E/(bA)$ (footprint ÷ flow-yield)", fontsize=9)
    ax.set_title(f"$\\tau_g$={tg:.0f} yr", fontsize=9.6)
    ax.set_xlim(0.2, 1.55); ax.set_ylim(0.2, 1.9); ax.grid(alpha=.3)
    ax.legend(fontsize=6.5, loc="upper left")
    return dict(tg=tg, tp=tp, n_recover=int(rec.sum()), n_collapse=int(col.sum()),
                silent=int(sm.sum()), n_silent_over_collapse=int(sm.sum()) / max(int(col.sum()), 1))


def fig_macro_ratios(delays=((10.0, 25.0), (30.0, 25.0))):
    """Two-panel baseline basin in the macro-ratio plane (tau_g=10 vs 30)."""
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.2))
    out = []
    for (tg, tp), ax in zip(delays, axes):
        out.append(_panel(ax, tg, tp))
    fig.tight_layout()
    fig.savefig(os.path.join(SCANS, "topdown_macro_ratios.png"), dpi=130)
    plt.close(fig)
    return out


def fig_ratio_separation():
    idx = np.linspace(0.02, 8.0, 300)
    RAeq = np.where(idx <= 1, 1.0, (1.0 + idx) / 2.0)
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.plot(idx, RAeq, color="#1f77b4", lw=2.2, label=r"$R_A^{\rm eq}=\frac{1}{2}(1+b_G\rho/b)$")
    ax.plot(idx, np.ones_like(idx), color="k", ls="--", lw=1.6, label="$R_B^{\\rm eq}=1$")
    ax.fill_between(idx, 1, RAeq, color="#1f77b4", alpha=.12)
    ax.axvspan(1, 8, color="orange", alpha=.10)
    ax.set_xscale("log"); ax.set_xticks([0.1, 0.2, 0.5, 1, 2, 4, 8])
    ax.set_xticklabels(["0.1", "0.2", "0.5", "1", "2", "4", "8"])
    ax.text(0.09, 1.5, "flow-dominated\n($b_G\\rho<b$, $R_A\\approx R_B$)", fontsize=7.2, color="#7f7f7f")
    ax.text(1.4, 3.2, "increment-dominated\n(interior MSY, $R_A^{\\rm eq}>1$)", fontsize=7.2, color="#d2691e")
    ax.set_xlabel("regime index  $b_G\\rho/b$", fontsize=9)
    ax.set_ylabel("ratio at the sustainable equilibrium", fontsize=9)
    ax.set_title("flow-share separates the two ratios", fontsize=9.6)
    ax.grid(alpha=.3); ax.legend(fontsize=7, loc="lower right"); ax.set_ylim(0.9, 4.0)
    fig.tight_layout(); fig.savefig(os.path.join(SCANS, "topdown_ratio_separation.png"), dpi=130)
    plt.close(fig)


def main():
    res = {}
    t0 = time.time(); print("A2 neutral direction / D(0)=0 ...", flush=True)
    for Astar in (0.6, 1.0, 1.1):
        l, r, s = T.neutral_direction(Astar)
        res.setdefault("neutral", {})[f"A*={Astar}"] = dict(
            singular_values=[float(x) for x in s], left_null=[float(x) for x in l],
            right_null=[float(x) for x in r])
    print("  %.1fs" % (time.time() - t0), flush=True)

    t0 = time.time(); print("A2 separator accuracy ...", flush=True)
    res["separator"] = []
    for tg, tp in [(0.0, 0.0), (10.0, 25.0), (30.0, 25.0)]:
        res["separator"].append(T.separator_accuracy(tg, tp, mode="neutral"))
        if (tg, tp) in [(0.0, 0.0), (30.0, 25.0)]:
            res["separator"].append(T.separator_accuracy(tg, tp, mode="linear"))
    print("  %.1fs" % (time.time() - t0), flush=True)

    t0 = time.time(); print("A1 delay boundary ...", flush=True)
    tg_list = list(range(0, 41, 1)); tp_list = [0, 5, 10, 15, 20, 25, 40, 60]
    out, lastR = T.delay_boundary(tg_list, tp_list, A0=1.0, P0=0.9)
    res["delay_cliff"] = dict(last_recover_tau_g_by_tau_p={int(k): v for k, v in lastR.items()},
                              n_tau_g=len(tg_list), n_tau_p=len(tp_list))
    fig_delay_boundary(tg_list, tp_list, 1.0, 0.9, out, lastR)
    print("  %.1fs" % (time.time() - t0), flush=True)

    t0 = time.time(); print("A3 overshoot scaling ...", flush=True)
    ov = []
    for tg in [5, 8, 10, 12, 15, 18]:
        pk = T.recovery_overshoot(float(tg)); ov.append(dict(tau_g=tg, A_peak=round(pk, 4),
                                                            overshoot=round(pk / T.AMAX - 1, 5)))
    res["overshoot"] = ov
    print("  %.1fs" % (time.time() - t0), flush=True)

    t0 = time.time(); print("A5 crossing-curve / monotone-only ...", flush=True)
    res["hopf"] = dict(n_crossing_points=T.no_crossing_confirmation())
    print("  %.1fs" % (time.time() - t0), flush=True)

    t0 = time.time(); print("C4 rescue set (recover fraction vs tau_g) ...", flush=True)
    res["rescue_set"] = []
    for tg in [0, 10, 18, 20, 30, 40]:
        res["rescue_set"].append(T.rescue_set(float(tg)))
    print("  %.1fs" % (time.time() - t0), flush=True)

    t0 = time.time(); print("C6 discrete map: fixed points == family; local stability ...", flush=True)
    res["map_fixed_points"] = {str(E): [round(x, 4) for x in T.map_fixed_points(E)] for E in [0.15, 0.30, 0.50]}
    res["map_local_stability"] = T.map_local_stability([0, 10, 18, 20, 30, 40])
    print("  %.1fs" % (time.time() - t0), flush=True)

    t0 = time.time(); print("A7 macro-ratio basin (tau_g=10,30) ...", flush=True)
    res["macro_ratio_basin"] = fig_macro_ratios()
    fig_ratio_separation()
    res["flow_share_closed_form"] = {str(k): round(T.RAeq_from_regime(k), 4) for k in [0.5, 1.0, 1.5, 3.0, 6.0, 12.0]}
    print("  %.1fs" % (time.time() - t0), flush=True)

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(res, f, indent=2)
    print("wrote", OUT_JSON)


if __name__ == "__main__":
    main()
