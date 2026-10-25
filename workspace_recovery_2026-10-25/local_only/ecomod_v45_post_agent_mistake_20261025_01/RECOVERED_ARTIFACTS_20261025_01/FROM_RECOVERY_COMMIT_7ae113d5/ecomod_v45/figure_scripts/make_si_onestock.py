"""Generate the four scoped one-stock-comparator figures used in the SI.

The comparator is kept separate from the two-land model. Account values B and E
are in gha; P and K are in cap; A and A_max use comparator-specific stock units;
G(A) is stock-unit yr^-1; b and T_b are gha per stock unit; b_G is gha yr per
stock unit; D is gha yr. The delay simulations use the exact positive-part
operator, not a smooth approximation.
"""
from pathlib import Path
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)


def growth(A, rho, Amax):
    A = max(float(A), 0.0)
    return rho * A * (1.0 - A / Amax)


def logistic_increment(t, delta_b, kappa, t_wave):
    x = np.clip(-kappa * (t - t_wave), -700, 700)
    return delta_b / (1.0 + np.exp(x))


def interp_history(values, t, dt, t_query, initial):
    """Linear interpolation using a constant prehistory for t<0."""
    if t_query <= 0:
        return float(initial)
    x = t_query / dt
    i0 = int(np.floor(x))
    f = x - i0
    i0 = min(i0, len(values) - 1)
    i1 = min(i0 + 1, len(values) - 1)
    return float(values[i0] * (1.0 - f) + values[i1] * f)


def simulate_full(p, T, dt, A0, P0, D0=0.0):
    """Full delayed one-stock system with current-time account valuation."""
    n = int(round(T / dt))
    t = np.arange(n + 1, dtype=float) * dt
    A = np.zeros(n + 1); P = np.zeros(n + 1); D = np.zeros(n + 1)
    B = np.zeros(n + 1); E = np.zeros(n + 1); b = np.zeros(n + 1)
    A[0], P[0], D[0] = A0, P0, D0

    def b_at(tt, dd):
        wave = logistic_increment(tt, p["delta_b"], p["kappa"], p["t_wave"])
        return (p["b0"] + wave) * np.exp(-p["alpha"] * max(dd, 0.0))

    def account(aa, dd, tt):
        bv = b_at(tt, dd)
        return bv * aa + p["bG"] * growth(aa, p["rho"], p["Amax"])

    b[0] = b_at(0.0, D0)
    B[0] = account(A0, D0, 0.0)
    E[0] = p["e"] * P0
    B0 = B[0]

    for i in range(n):
        ti = t[i]
        def deriv(tt, aa, pp, dd):
            if p["tau_g"] == 0:
                Ag = aa
            else:
                Ag = interp_history(A, t, dt, tt - p["tau_g"], A0)
            if p["tau_p"] == 0:
                Bdel = account(aa, dd, tt)
            else:
                Bdel = interp_history(B, t, dt, tt - p["tau_p"], B0)
            bv = b_at(tt, dd)
            Bnow = bv * aa + p["bG"] * growth(aa, p["rho"], p["Amax"])
            Enow = p["e"] * pp
            Kdel = max(Bdel / p["e"], p.get("Kmin", 1e-6))
            dA = growth(Ag, p["rho"], p["Amax"]) - max(Enow - p["sigma"] * bv * aa, 0.0) / p["bG"]
            dP = p["r"] * pp * (1.0 - pp / Kdel)
            dD = max(Enow - Bnow, 0.0) - p["eta"] * dd
            return dA, dP, dD

        a0, p0, d0 = A[i], P[i], D[i]
        k1 = deriv(ti, a0, p0, d0)
        k2 = deriv(ti + dt/2, a0 + dt*k1[0]/2, p0 + dt*k1[1]/2, d0 + dt*k1[2]/2)
        k3 = deriv(ti + dt/2, a0 + dt*k2[0]/2, p0 + dt*k2[1]/2, d0 + dt*k2[2]/2)
        k4 = deriv(ti + dt, a0 + dt*k3[0], p0 + dt*k3[1], d0 + dt*k3[2])
        A[i+1] = max(p["Aext"], a0 + dt*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6)
        P[i+1] = max(0.0, p0 + dt*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6)
        D[i+1] = max(0.0, d0 + dt*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2])/6)
        b[i+1] = b_at(t[i+1], D[i+1])
        B[i+1] = account(A[i+1], D[i+1], t[i+1])
        E[i+1] = p["e"] * P[i+1]
    return {"t": t, "A": A, "P": P, "D": D, "B": B, "E": E, "b": b}


def simulate_fixed_demand(p, E0, T=120.0, dt=0.01, A0=1.0, D0=0.0):
    """No-delay fixed-demand one-stock case used for the masking illustration."""
    n = int(round(T / dt))
    t = np.arange(n + 1, dtype=float) * dt
    A = np.zeros(n + 1); D = np.zeros(n + 1); B = np.zeros(n + 1); b = np.zeros(n + 1)
    A[0], D[0] = A0, D0

    def b_at(tt, dd):
        wave = logistic_increment(tt, p["delta_b"], p["kappa"], p["t_wave"])
        return (p["b0"] + wave) * np.exp(-p["alpha"] * max(dd, 0.0))

    def account(aa, dd, tt):
        return b_at(tt, dd) * aa + p["bG"] * growth(aa, p["rho"], p["Amax"])

    b[0] = b_at(0.0, D0); B[0] = account(A0, D0, 0.0)
    for i in range(n):
        ti = t[i]
        def deriv(tt, aa, dd):
            bv = b_at(tt, dd)
            Bnow = bv * aa + p["bG"] * growth(aa, p["rho"], p["Amax"])
            dA = growth(aa, p["rho"], p["Amax"]) - max(E0 - p["sigma"] * bv * aa, 0.0) / p["bG"]
            dD = max(E0 - Bnow, 0.0) - p["eta"] * dd
            return dA, dD
        a0, d0 = A[i], D[i]
        k1 = deriv(ti, a0, d0)
        k2 = deriv(ti + dt/2, a0 + dt*k1[0]/2, d0 + dt*k1[1]/2)
        k3 = deriv(ti + dt/2, a0 + dt*k2[0]/2, d0 + dt*k2[1]/2)
        k4 = deriv(ti + dt, a0 + dt*k3[0], d0 + dt*k3[1])
        A[i+1] = max(p["Aext"], a0 + dt*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6)
        D[i+1] = max(0.0, d0 + dt*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6)
        b[i+1] = b_at(t[i+1], D[i+1])
        B[i+1] = account(A[i+1], D[i+1], t[i+1])
    return {"t": t, "A": A, "D": D, "B": B, "b": b}


def simulate_constant(p, T=1800.0, dt=0.2, A0=1.0, P0=0.1):
    """Debt-free, no-wave delayed subsystem used for delay and basin figures."""
    n = int(round(T / dt))
    t = np.arange(n + 1, dtype=float) * dt
    A = np.zeros(n + 1); P = np.zeros(n + 1); B = np.zeros(n + 1)
    A[0], P[0] = A0, P0

    def account(aa):
        return p["b"] * aa + p["bG"] * growth(aa, p["rho"], p["Amax"])

    B[0] = account(A0); B0 = B[0]
    for i in range(n):
        ti = t[i]
        def deriv(tt, aa, pp):
            Ag = aa if p["tau_g"] == 0 else interp_history(A, t, dt, tt - p["tau_g"], A0)
            Bdel = account(aa) if p["tau_p"] == 0 else interp_history(B, t, dt, tt - p["tau_p"], B0)
            Kdel = max(Bdel / p["e"], p.get("Kmin", 1e-6))
            dA = growth(Ag, p["rho"], p["Amax"]) - max(p["e"] * pp - p["sigma"] * p["b"] * aa, 0.0) / p["bG"]
            dP = p["r"] * pp * (1.0 - pp / Kdel)
            return dA, dP
        a0, p0 = A[i], P[i]
        k1 = deriv(ti, a0, p0)
        k2 = deriv(ti + dt/2, a0 + dt*k1[0]/2, p0 + dt*k1[1]/2)
        k3 = deriv(ti + dt/2, a0 + dt*k2[0]/2, p0 + dt*k2[1]/2)
        k4 = deriv(ti + dt, a0 + dt*k3[0], p0 + dt*k3[1])
        A[i+1] = max(p["Aext"], a0 + dt*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6)
        P[i+1] = max(0.0, p0 + dt*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6)
        B[i+1] = account(A[i+1])
    return {"t": t, "A": A, "P": P, "B": B}


def mask_runs(A, B, t, tol=1e-9):
    on = (np.diff(B) > tol) & (np.diff(A) < -tol)
    idx = np.flatnonzero(on)
    if not len(idx):
        return []
    runs = []
    start = last = int(idx[0])
    for j in idx[1:]:
        j = int(j)
        if j != last + 1:
            runs.append((start, last + 1))
            start = j
        last = j
    runs.append((start, last + 1))
    return [(t[i0], t[i1], t[i1] - t[i0], i0, i1) for i0, i1 in runs]


def basin_map(p, gridA, gridP, T=1200.0, dt=0.5):
    cells = []
    for a0 in gridA:
        row = []
        for p0 in gridP:
            z = simulate_constant({**p, "A0": a0, "P0": p0}, T=T, dt=dt, A0=float(a0), P0=float(p0))
            aend = z["A"][-1]
            if aend >= 0.95 * p["Amax"]:
                row.append(1)  # high endpoint at this finite horizon
            elif aend <= 0.05:
                row.append(-1)  # low endpoint at this finite horizon
            else:
                row.append(0)  # intermediate at the finite horizon
        cells.append(row)
    return np.asarray(cells, dtype=int)


def main():
    plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9,
                         "legend.fontsize": 8, "figure.dpi": 150})
    blue, orange, green, red, purple = "#2166ac", "#d17c00", "#1b7837", "#b2182b", "#762a83"

    # Figure 1: full comparator trajectory; B uses the equation's current A.
    p = dict(rho=0.08, Amax=1.2, b0=0.5, bG=0.6, e=0.55, r=0.02,
             eta=0.03, alpha=0.2, delta_b=0.5, kappa=0.04, t_wave=120.0,
             tau_g=15.0, tau_p=25.0, Aext=0.02, sigma=1.0, Kmin=1e-4)
    z = simulate_full(p, T=900.0, dt=0.1, A0=1.0, P0=0.45)
    fig, axs = plt.subplots(2, 2, figsize=(10.4, 6.0), sharex=True)
    axs[0,0].plot(z["t"], z["B"], color=green, label=r"$B$")
    axs[0,0].plot(z["t"], z["E"], color=red, label=r"$E=eP$")
    axs[0,0].set_ylabel("annual account value (gha)")
    axs[0,0].set_title("(a) Annual account values")
    axs[0,0].legend(frameon=False, ncol=2)
    axs[0,1].plot(z["t"], z["A"], color=blue)
    axs[0,1].axhline(p["Aext"], color="0.4", ls=":", lw=1)
    axs[0,1].set_ylabel("stock A (comparator units)")
    axs[0,1].set_title("(b) One-stock state")
    axs[1,0].plot(z["t"], z["P"], color=orange)
    axs[1,0].set_ylabel("population P (cap)")
    axs[1,0].set_title("(c) Population")
    axs[1,1].plot(z["t"], z["D"], color=purple)
    axs[1,1].set_ylabel(r"leaky state D (gha yr)")
    axs[1,1].set_title("(d) Leaky shortfall state")
    for ax in axs.flat:
        ax.set_xlabel("time (yr)")
        ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUT / "si_onestock_full_trajectory.png", dpi=250, bbox_inches="tight")
    plt.close(fig)

    # Figure 2: corrected exact-switch masking example and initial-shortfall sweep.
    pm = dict(rho=0.05, Amax=1.2, b0=0.5, bG=0.8, eta=0.05, alpha=0.03,
              delta_b=1.5, kappa=0.2, t_wave=15.0, Aext=0.02, sigma=1.0)
    A0, E0, dtm = 1.0, 0.60, 0.01
    zm = simulate_fixed_demand(pm, E0, T=120.0, dt=dtm, A0=A0)
    runs = mask_runs(zm["A"], zm["B"], zm["t"], tol=1e-9)
    if runs:
        t0, t1, width, i0, i1 = max(runs, key=lambda r: r[2])
    else:
        t0 = t1 = width = 0.0; i0 = i1 = 0
    deficit0 = max(E0 - zm["b"][0] * A0, 0.0)
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 4.0))
    ax = axs[0]; axr = ax.twinx()
    l1, = ax.plot(zm["t"], zm["A"], color=blue, lw=1.8, label=r"$A$ (stock units)")
    l2, = axr.plot(zm["t"], zm["B"], color=green, lw=1.8, label=r"$B$ (gha)")
    if runs:
        ax.axvspan(t0, t1, color="#fdd835", alpha=0.22)
        ax.axvline(t0, color="#d17c00", ls="--", lw=0.9)
        ax.axvline(t1, color="#d17c00", ls="--", lw=0.9)
        ax.text((t0+t1)/2, min(zm["A"].max(), 1.15), f"simultaneous interval: {width:.2f} yr",
                ha="center", va="top", color="#6b5700", fontsize=8)
    ax.set_xlim(0, 25)
    ax.set_xlabel("time (yr)"); ax.set_ylabel(r"stock $A$ (comparator units)", color=blue)
    axr.set_ylabel(r"annual account value $B$ (gha)", color=green)
    ax.set_title("(a) Aggregate rise during stock decline")
    ax.grid(alpha=0.25)
    ax.legend([l1,l2], [l1.get_label(),l2.get_label()], loc="upper right", frameon=False)

    deltas = np.arange(0.005, 0.081, 0.005)
    widths = []
    binit = zm["b"][0]
    for delta in deltas:
        ee = binit * A0 + delta
        zz = simulate_fixed_demand(pm, ee, T=40.0, dt=0.02, A0=A0)
        rr = mask_runs(zz["A"], zz["B"], zz["t"], tol=1e-9)
        widths.append(max((r[2] for r in rr), default=0.0))
    axs[1].bar(deltas, widths, width=0.004, color=green, alpha=0.82)
    axs[1].set_xlabel(r"initial shortfall $[E(0)-b(0)A_0]_+$ (gha)")
    axs[1].set_ylabel("duration with $\\dot B>0$, $\\dot A<0$ (yr)")
    axs[1].set_title("(b) Window width across initial shortfall")
    axs[1].grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUT / "si_onestock_mask_window.png", dpi=250, bbox_inches="tight")
    plt.close(fig)

    # Figure 3: controlled regeneration-delay pair at the same initial state.
    pc = dict(rho=0.05, Amax=1.2, b=0.5, bG=0.8, e=0.55, r=0.02,
              sigma=1.0, Aext=0.02, Kmin=1e-6, tau_p=25.0)
    z10 = simulate_constant({**pc, "tau_g": 10.0}, T=1800.0, dt=0.2, A0=1.0, P0=0.1)
    z30 = simulate_constant({**pc, "tau_g": 30.0}, T=1800.0, dt=0.2, A0=1.0, P0=0.1)
    fig, axs = plt.subplots(2, 2, figsize=(10.4, 6.0), sharex=True)
    for zz, lab, col in [(z10, r"$\tau_g=10$ yr", blue), (z30, r"$\tau_g=30$ yr", red)]:
        axs[0,0].plot(zz["t"], zz["A"], label=lab, color=col, lw=1.6)
        axs[0,1].plot(zz["t"], zz["B"], label=lab, color=col, lw=1.6)
        axs[1,0].plot(zz["t"], zz["P"], label=lab, color=col, lw=1.6)
    axs[0,0].axhline(pc["Amax"], color="0.3", ls=":", lw=0.9)
    axs[0,0].axhline(pc["Aext"], color="0.5", ls="--", lw=0.8)
    axs[0,0].set_ylabel("stock A (comparator units)"); axs[0,0].set_title("(a) Stock")
    axs[0,1].set_ylabel("annual account value B (gha)"); axs[0,1].set_title("(b) Biocapacity")
    axs[1,0].set_ylabel("population P (cap)"); axs[1,0].set_title("(c) Population")
    axs[1,1].axis("off")
    for ax in axs.flat:
        if ax.has_data():
            ax.set_xlabel("time (yr)"); ax.grid(alpha=0.25); ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / "si_onestock_delay_examples.png", dpi=250, bbox_inches="tight")
    plt.close(fig)

    # Figure 4: initial-condition outcome map, with tau_p held fixed.
    gridA = np.round(np.arange(0.10, 1.301, 0.10), 3)
    gridP = np.round(np.arange(0.05, 1.551, 0.10), 3)
    cmap = ListedColormap(["#d95f5f", "#bdbdbd", "#4daf7c"])
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 4.2), sharex=True, sharey=True)
    for ax, tg in zip(axs, [0.0, 30.0]):
        zgrid = basin_map({**pc, "tau_g": tg}, gridA, gridP, T=1200.0, dt=0.5)
        ax.imshow(zgrid, origin="lower", aspect="auto", interpolation="nearest",
                  extent=[gridP[0]-0.05, gridP[-1]+0.05, gridA[0]-0.05, gridA[-1]+0.05],
                  cmap=cmap, vmin=-1, vmax=1)
        ax.set_title(rf"$\tau_g={tg:g}$ yr, $\tau_p=25$ yr")
        ax.set_xlabel(r"initial population $P_0$ (cap)")
        ax.grid(alpha=0.12, color="white")
    axs[0].set_ylabel(r"initial stock $A_0$ (comparator units)")
    from matplotlib.patches import Patch
    axs[0].legend(handles=[Patch(color="#4daf7c", label=r"high endpoint $A\geq0.95A_{\max}$"),
                           Patch(color="#d95f5f", label=r"low endpoint $A\leq0.05$"),
                           Patch(color="#bdbdbd", label="intermediate at 1200 yr")],
                  loc="upper left", fontsize=7, frameon=True)
    fig.tight_layout()
    fig.savefig(OUT / "si_onestock_basin.png", dpi=250, bbox_inches="tight")
    plt.close(fig)

    print("Figures saved:")
    for f in ["si_onestock_full_trajectory.png", "si_onestock_mask_window.png",
              "si_onestock_delay_examples.png", "si_onestock_basin.png"]:
        print(" ", OUT / f)
    print(f"Mask example: B over interval={zm['B'][i0]:.6f}->{zm['B'][i1]:.6f} gha; "
          f"A over interval={zm['A'][i0]:.6f}->{zm['A'][i1]:.6f} units; "
          f"window={width:.3f} yr; initial shortfall={deficit0:.6f} gha")
    print(f"Full trajectory: A min={z['A'].min():.5f}, B max={z['B'].max():.5f} gha, "
          f"P max={z['P'].max():.5f} cap, D max={z['D'].max():.5f} gha yr")
    print(f"Delay cases: tau_g=10 final A={z10['A'][-1]:.5f}; tau_g=30 final A={z30['A'][-1]:.5f}")


if __name__ == "__main__":
    main()
