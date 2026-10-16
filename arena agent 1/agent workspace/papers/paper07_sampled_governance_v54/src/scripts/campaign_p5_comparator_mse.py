"""P5 sampled governance: executed comparator management-strategy evaluation (wave 7).

The paper's Section 2.2 declares the protective controller and the fixed-plan
controller as comparators "for the prospective management-strategy evaluation ...
not presented as completed experiments". This script executes the model-level
run of that comparison on the logistic hold-map core — the plant the paper's
closed-form operator results are computed on — at the declared evidential
status: deterministic, seed-fixed, on the declared architecture only; it is not
the prospective real-system design of Section 4.5.

Design (all declared here):
  - plant: the logistic hold-map core of eqs (1)-(2) (r = 0.02, K = 100,
    q = 0.001, tau_m = 5 yr, softplus signal Phi_k with k = 10 and floor -delta,
    delta = log 2/10), Candidate A equilibrium (N*, Z*, E*) = (89.55188, delta, 2.08962).
  - review architecture: effort held over the review interval; stock follows the
    closed-form logistic hold flow; the memory integrates the signal (RK4, dt = 0.2);
    the assessment is the end-of-period memory state, with multiplicative
    assessment error eps in {0, 0.3} (the paper's declared robustness experiment).
  - controllers: extractive Euler (the paper's core), extractive exact-hold
    (the separating comparator), protective Euler, protective exact-hold
    (sign-reversed response), and fixed plan (effort frozen at E*, no updates).
  - initial state: N0 = 0.95 N*, Z0 = delta, E0 = E*; H = 800 reviews; metrics on
    the last 60% of reviews; divergence if N leaves (0, 2K).
  - metrics: RMS stock deviation from N* (units of K), RMS effort deviation from
    E* (units of E_max), minimum N (units of K), depletion frequency
    (fraction of post-transient reviews with N < 0.5 N*), divergence review.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)
SEED = 20260831

# ---------- Candidate A (identical reconstruction to the monodromy scripts) ----------
r, K, q = 0.02, 100.0, 0.001
eta, Emax, dref = 0.914, 30.0, 1.0
d0, tm, Zref = 0.01, 5.0, 1.0
delta = np.log(2) / 10.0
k_soft = 10.0
eta_p = 0.914  # protective gain = eta_A

a = -eta / Emax
b = eta * delta / dref
c = d0 * delta / (Zref + delta)
E_star = (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
N_star = K * (1 - q * E_star / r)
Z_star = delta
E0_cap = E_star * (Zref + delta) / Zref

gate = 1 - E_star / Emax
A_N = r * (1 - 2 * N_star / K) - q * E_star
A_E = -q * N_star
B_N = -A_N / (2 * tm)
B_E = -A_E / (2 * tm)
CE_m = gate * eta * (delta / dref - 2 * E_star / Emax)
CZ_m = gate * (eta * E_star / dref + d0 * Zref / (Zref + delta) ** 2)
CE_p = -gate * eta_p
CZ_p = gate * eta_p * (-E0_cap * Zref / (Zref + delta) ** 2)

# linear-monodromy reference (for the validation gate)
from numpy.linalg import eigvals as _eig
from scipy.linalg import expm as _expm

A_hold = np.array([[A_N, 0.0, A_E], [B_N, -1 / tm, B_E], [0.0, 0.0, 0.0]])


def rho_linear(T, CE, CZ, exact):
    R = np.eye(3)
    if exact:
        eC = np.exp(CE * T)
        R[2, 1] = (eC - 1.0) * CZ / CE
        R[2, 2] = eC
    else:
        R[2, 1] = T * CZ
        R[2, 2] = 1 + T * CE
    return max(abs(_eig(R @ _expm(A_hold * T))))


def phi(x):
    sp = np.log1p(np.exp(k_soft * x)) / k_soft
    return np.maximum(-delta, sp)


def surplus(N):
    return r * N * (1 - N / K)


def hold_flow(N0, E, T):
    """Closed-form logistic hold flow (paper Section 3.4)."""
    aE = r - q * E
    if abs(aE) < 1e-12:
        return N0 / (1 + (r / K) * N0 * T)
    eaT = np.exp(aE * T)
    return aE * N0 * eaT / (aE + (r / K) * N0 * (eaT - 1.0))


def flow_memory(N0, Z0, E, T, dt=0.2):
    """Integrate the memory equation over one held-effort review interval (RK4).

    The stock follows the closed-form hold flow at absolute times t in [0, T];
    the memory equation is stepped by RK4 with the stock evaluated at the
    substep start, midpoint, and end.
    """
    n = max(2, int(round(T / dt)))
    h = T / n

    def zderiv(Nv, Zv):
        return (phi(q * E * Nv - surplus(Nv)) - Zv) / tm

    Zt = Z0
    for j in range(n):
        t_j = j * h
        Nj = hold_flow(N0, E, t_j)
        Nm = hold_flow(N0, E, t_j + 0.5 * h)
        Ne = hold_flow(N0, E, t_j + h)
        k1 = zderiv(Nj, Zt)
        k2 = zderiv(Nm, Zt + 0.5 * h * k1)
        k3 = zderiv(Nm, Zt + 0.5 * h * k2)
        k4 = zderiv(Ne, Zt + h * k3)
        Zt = Zt + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return hold_flow(N0, E, T), Zt


def effort_ode(controller, e, zhat):
    if controller == "extractive":
        return (1 - e / Emax) * (eta * e * (zhat / dref - e / Emax) + d0 * zhat / (Zref + zhat))
    if controller == "protective":
        Ecap = E0_cap * Zref / (Zref + zhat)
        return (1 - e / Emax) * eta_p * (Ecap - e)
    raise ValueError(controller)


def run(controller, T, eps, seed, dt=0.2):
    rng = np.random.default_rng(seed)
    N, Z, E = 0.95 * N_star, Z_star, E_star
    H = 800
    hist = []
    div = None
    for n in range(H):
        if N <= 1e-6 or N > 2 * K or not np.isfinite(N):
            div = n
            break
        N, Z = flow_memory(N, Z, E, T, dt=dt)
        zhat = Z * (1 + eps * rng.standard_normal()) if eps > 0 else Z
        if controller == "fixed":
            Enew = E
        else:
            exact = controller.endswith("exact")
            base = "extractive" if controller.startswith("extractive") else "protective"
            if exact:
                sol = solve_ivp(lambda t, e: [effort_ode(base, e[0], zhat)], [0.0, T], [E],
                                rtol=1e-10, atol=1e-12)
                Enew = float(sol.y[0, -1])
            else:
                Enew = E + T * effort_ode(base, E, zhat)
            Enew = min(max(Enew, 0.0), Emax)
        E = Enew
        hist.append((N, Z, E))
    hist = np.array(hist)
    m = len(hist)
    w = hist[int(0.4 * m):]
    if len(w) < 20 or m < 100:
        return dict(controller=controller, T_r=T, eps=eps, rmsd_N=np.nan, rmsd_E=np.nan,
                    min_N=np.nan, depletion_freq=np.nan, divergence_review=div, n_reviews=m)
    rmsd_N = float(np.sqrt(np.mean((w[:, 0] - N_star) ** 2)) / K)
    rmsd_E = float(np.sqrt(np.mean((w[:, 2] - E_star) ** 2)) / Emax)
    return dict(controller=controller, T_r=T, eps=eps, rmsd_N=round(rmsd_N, 6),
                rmsd_E=round(rmsd_E, 6), min_N=round(float(w[:, 0].min() / K), 6),
                depletion_freq=round(float((w[:, 0] < 0.5 * N_star).mean()), 4),
                divergence_review=div, n_reviews=m)


def main():
    print("=== VALIDATION GATE (linear monodromy references) ===")
    assert abs(rho_linear(1.0, CE_p, CZ_p, False) - 0.9838) < 5e-4
    assert abs(rho_linear(1.0, CE_m, CZ_m, False) - 1.00055) < 5e-4
    assert abs(rho_linear(1.0, CE_m, CZ_m, True) - 1.00035) < 5e-4
    print("  committed linear numbers reproduced; nonlinear simulator initialised")

    print("\n=== EXECUTED COMPARATOR MSE (logistic hold-map core, N0 = 0.95 N*) ===")
    controllers = ["extractive-euler", "extractive-exact", "protective-euler",
                   "protective-exact", "fixed"]
    Tgrid = [1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0, 40.0]
    epsgrid = [0.0, 0.3]
    rows = []
    for eps in epsgrid:
        for T in Tgrid:
            for ci, ctl in enumerate(controllers):
                seed = SEED + 1000 * int(eps * 10) + 10 * Tgrid.index(T) + ci
                row = run(ctl, T, eps, seed)
                rows.append(row)
                div = "" if row["divergence_review"] is None else f"  DIVERGED@review {row['divergence_review']}"
                print(f"  eps={eps} T_r={T:5} {ctl:18} rmsd_N={row['rmsd_N']:.4f} "
                      f"rmsd_E={row['rmsd_E']:.4f} min_N={row['min_N']:.3f} "
                      f"depletion={row['depletion_freq']:.3f}{div}")
    pd.DataFrame(rows).to_csv(OUT / "p5_comparator_mse.csv", index=False)
    print("saved:", OUT / "p5_comparator_mse.csv")


if __name__ == "__main__":
    main()
