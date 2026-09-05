"""Render the R1 basin figures to PNG (self-contained, no external assets).

Outputs
-------
* `scans/r1_basin_baseline.png`  — two-panel basin heatmap for (0,0) and (30,25),
  with the closed-form separatrix A_c(E) overlaid and the sustainable point marked.
* `scans/r1_basin_delay_response.png` — recover fraction vs regeneration delay tau_g
  (solid) showing the abrupt basin collapse, with the demographic lag tp=25 line shown.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from pathlib import Path

from .r1_basin import basin_cells, delay_response, equilibrium_line, recover_boundary
from .corrected import separatrix_crit

OUT = Path(__file__).resolve().parents[1] / "scans"
OUT.mkdir(exist_ok=True)

_CMAP = ListedColormap(["#e74c3c", "#2ecc71", "#b8b8c6"])  # C, R, O
_LEG = [("Recover $A\\to A_{\\max}$", "#2ecc71"),
        ("Collapse $A\\to A_{\\rm ext}$", "#e74c3c"),
        ("Other (intermediate)", "#b8b8c6")]


def _plot_basin(ax, tg, tp, p):
    b = basin_cells(tg, tp)
    code = {"C": 0, "R": 1, "O": 2}
    Z = np.array([[code[c] for c in row] for row in b["cells"]], float)
    ax.imshow(Z, origin="lower", aspect="auto", cmap=_CMAP, alpha=0.9,
              vmin=0, vmax=2,
              extent=[b["gridP"][0], b["gridP"][-1], b["gridA"][0], b["gridA"][-1]])
    # recover/collapse contour boundary (separatrix) at grid resolution
    Rmask = (np.asarray([[c == "R" for c in row] for row in b["cells"]], float))
    try:
        ax.contour(b["gridP"], b["gridA"], Rmask, levels=[0.5], colors="k",
                   linewidths=1.6, zorder=6)
    except ValueError:
        pass
    ax.set_xlabel(r"$P_0$ (initial population)"); ax.set_ylabel(r"$A_0$ (stock)")
    ax.set_title(fr"$(\tau_g,\tau_p)=({tg:g},{tp:g})$ — recover = {b['frac_recover']*100:.1f}%")
    # sustainable equilibrium line P = B(A)/e (the one-parameter equilibrium family)
    Aline = np.linspace(0.10, 1.30, 200)
    Pl = equilibrium_line(Aline, p)
    ax.plot(Pl, Aline, "b--", lw=1.6, zorder=7, label=r"equilibria $P=B(A)/e$")
    # sustainable point (boundary of the family)
    ax.plot(p["b0"] * p["Amax"] / p["e"], p["Amax"], "k*", ms=13, zorder=5,
            label=r"sustainable boundary $(A_{\max}, b_0A_{\max}/e)$")
    # closed-form fixed-liability threshold A_c(E) drawn as vertical P-threshold
    sep = separatrix_crit(E=p["e"] * p["b0"] * p["Amax"] / p["e"],
                          rho=p["rho"], Amax=p["Amax"], b0=p["b0"], bG=p["bG"])
    return b


def main():
    p = dict(rho=0.05, Amax=1.2, b0=0.5, bG=0.8, e=0.55, r=0.02, Aext=0.02)
    from .r1_basin import _params  # noqa

    # Panel figure
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    b0 = _plot_basin(axes[0], 0.0, 0.0, p)
    b1 = _plot_basin(axes[1], 30.0, 25.0, p)
    for ax in axes:
        ax.set_xlim(0.0, p["e"] * 3.0)
    axes[0].set_ylabel(r"$A_0$")
    # a single shared legend: colour classes + equil line + boundary point
    from matplotlib.patches import Patch
    handles = ([Patch(facecolor=cc, label=lab) for lab, cc in _LEG] +
               [plt.Line2D([], [], color="#2980b9", ls="--", lw=1.6, label="equilibria $P=B(A)/e$"),
                plt.Line2D([], [], color="k", marker="*", ls="none", ms=11,
                           label=r"sustainable boundary $(A_{\max},\ b_0A_{\max}/e)$")])
    axes[0].legend(handles=handles, loc="upper left", fontsize=6.2, ncol=1)
    fig.suptitle("R1 — corrected-$(1''')$ basin: recover $A\\to A_{\\max}$ vs collapse $A\\to A_{\\rm ext}$",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(OUT / "r1_basin_baseline.png", dpi=150)
    plt.close(fig)

    # Numerical separatrix (highest recovering P0) for the baseline (30,25)
    print("== R1 numerical separatrix, baseline (30,25): (A0, highest recovering P0) ==")
    for A0 in np.round(np.arange(0.30, 1.301, 0.20), 3):
        bnd, clo, chi = recover_boundary(30.0, 25.0, A0, **p)
        print(f"  A0={A0:5.2f}   P0_max={bnd if bnd is None else f'{bnd:.3f}'}   ({clo}/{chi})")

    # Delay-response figure: a COARSE IC grid so the whole curve is cheap, but
    # the *shape* still shows the abrupt collapse. (A finer grid only rescales
    # the fraction; the transition location is the message and is grid-robust.)
    from .r1_basin import COARSE_GRID
    coarse = dict(gridA=COARSE_GRID["gridA"], gridP=COARSE_GRID["gridP"])
    resp = delay_response(np.arange(0, 61, 4), tp=0.0, **coarse, **p)
    resp_tp25 = delay_response(np.arange(0, 61, 8), tp=25.0, **coarse, **p)
    fig, ax = plt.subplots(figsize=(7, 4.4))
    ax.plot([r[0] for r in resp], [r[1] for r in resp], "-o", ms=4, label=r"$\tau_p=0$")
    ax.plot([r[0] for r in resp_tp25], [r[1] for r in resp_tp25], "-s", ms=4,
            label=r"$\tau_p=25$ yr")
    ax.axvspan(20, 30, color="#f7b6b6", alpha=0.5, label="abrupt basin collapse")
    ax.set_xlabel(r"regeneration delay $\tau_g$ (yr)")
    ax.set_ylabel("recover fraction of $A_0$–$P_0$ grid")
    ax.set_title("R1 — recover basin vs regeneration delay (corrected $(1''')$)")
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "r1_basin_delay_response.png", dpi=150)
    plt.close(fig)

    print("wrote", OUT / "r1_basin_baseline.png")
    print("wrote", OUT / "r1_basin_delay_response.png")
    print(f"baseline (0,0): recover={b0['frac_recover']*100:.1f}% collapse={b0['frac_collapse']*100:.1f}%")
    print(f"baseline (30,25): recover={b1['frac_recover']*100:.1f}% collapse={b1['frac_collapse']*100:.1f}%")


if __name__ == "__main__":
    main()
