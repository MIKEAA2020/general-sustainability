"""P5 sampled governance: complete crossing record + linear trajectory MSE (wave 7).

Objects (all on the logistic hold-map core, mobilising and protective channels,
Candidate A reconstruction identical to p4_exact_hold_monodromy.py):

  1. COMPLETE unit-circle crossing record, forward-Euler and exact held-measurement
     updates, T_r in [0.2, 200] yr, fine scan (200,001 points) + bisection refinement.
     This completes the registered multiplier scan of the paper's Section 2.2/3.4:
     the complete crossing count and the extent of the stable interval.
  2. Protective controller on the same maps (the declared U3 run): maximum spectral
     radius of the exact update over the same grid.
  3. Linear trajectory MSE between the Euler-reviewed and exact-reviewed closed loops
     (the command-step distortion, per channel, per T_r), in the paper's scaled
     state norm ||x||_* = |dN|/K + |dZ|/(rK) + |dE|/E_max.

Validation gate (committed numbers must reproduce before any new number counts):
  protective Euler: rho(1) = 0.9838, crossing ~2.306
  mobilising Euler: rho(1) = 1.00055, crossings 47.536 (complex pair), 79.143 (real -1)
  mobilising exact: rho(1) = 1.00035, single crossing ~6.5
  protective exact: stable at every tested T_r (max rho 0.9967 on [0.2, 120])
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from numpy.linalg import eigvals
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)

# ---------- Candidate A reconstruction (paper formulas, Section 3.1/3.2) ----------
r, K, q = 0.02, 100.0, 0.001
eta, Emax, dref = 0.914, 30.0, 1.0
d0, tm, Zref = 0.01, 5.0, 1.0
delta = np.log(2) / 10.0

a = -eta / Emax
b = eta * delta / dref
c = d0 * delta / (Zref + delta)
E_star = (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
N_star = K * (1 - q * E_star / r)
Z_star = delta

gate = 1 - E_star / Emax
A_N = r * (1 - 2 * N_star / K) - q * E_star
A_E = -q * N_star
B_N = -A_N / (2 * tm)
B_E = -A_E / (2 * tm)
d = 1 / tm
CE_m = gate * eta * (delta / dref - 2 * E_star / Emax)
CZ_m = gate * (eta * E_star / dref + d0 * Zref / (Zref + delta) ** 2)
CE_p = -gate * eta
E0 = E_star * (Zref + delta) / Zref
Ecap_p = -E0 * Zref / (Zref + delta) ** 2
CZ_p = gate * eta * Ecap_p

A_hold = np.array([[A_N, 0.0, A_E], [B_N, -d, B_E], [0.0, 0.0, 0.0]])


def euler_review(T, CE, CZ):
    R = np.eye(3)
    R[2, 1] = T * CZ
    R[2, 2] = 1 + T * CE
    return R


def exact_review(T, CE, CZ):
    R = np.eye(3)
    eC = np.exp(CE * T)
    R[2, 1] = (eC - 1.0) * CZ / CE
    R[2, 2] = eC
    return R


def monodromy(T, CE, CZ, exact):
    R = exact_review(T, CE, CZ) if exact else euler_review(T, CE, CZ)
    return R @ expm(A_hold * T)


def scan(CE, CZ, exact, Tmin=0.2, Tmax=200.0, n=200_001):
    Ts = np.linspace(Tmin, Tmax, n)
    rhos = np.empty(n)
    for i, T in enumerate(Ts):
        rhos[i] = max(abs(eigvals(monodromy(T, CE, CZ, exact))))
    # crossings: sign change of rho - 1
    signs = np.sign(rhos - 1.0)
    idx = np.where((signs[1:] * signs[:-1] < 0) & (signs[:-1] != 0) & (signs[1:] != 0))[0]
    crossings = []
    for i in idx:
        lo, hi = Ts[i], Ts[i + 1]
        rlo, rhi = rhos[i], rhos[i + 1]
        for _ in range(70):
            mid = 0.5 * (lo + hi)
            rm = max(abs(eigvals(monodromy(mid, CE, CZ, exact))))
            if (rlo - 1) * (rm - 1) < 0:
                hi, rhi = mid, rm
            else:
                lo, rlo = mid, rm
        Tk = 0.5 * (lo + hi)
        ev = eigvals(monodromy(Tk, CE, CZ, exact))
        near = sorted(ev, key=lambda x: abs(abs(x) - 1.0))[0]
        kind = "complex-pair" if abs(near.imag) > 1e-6 else ("real+1" if near.real > 0 else "real-1")
        direction = "stable->unstable" if rhos[i] < 1 < rhos[i + 1] else "unstable->stable"
        crossings.append((Tk, kind, near.real, near.imag, direction))
    # stable intervals (rho < 1 - tol) from the fine scan
    tol = 1e-10
    ok = rhos < 1.0 - tol
    intervals = []
    if ok.any():
        start = None
        for j in range(n):
            if ok[j] and start is None:
                start = Ts[j]
            if (not ok[j] or j == n - 1) and start is not None:
                end = Ts[j - 1] if not ok[j] else Ts[j]
                intervals.append((float(start), float(end)))
                start = None
    return rhos, crossings, intervals


def main():
    print("=== VALIDATION GATE ===")
    _, _, _ = scan(CE_p, CZ_p, False)  # protective Euler
    rho = max(abs(eigvals(monodromy(1.0, CE_p, CZ_p, False))))
    assert abs(rho - 0.9838) < 5e-4, rho
    print(f"  protective Euler rho(1) = {rho:.4f} (paper 0.9838) OK")
    _, _, _ = scan(CE_m, CZ_m, False)
    rho = max(abs(eigvals(monodromy(1.0, CE_m, CZ_m, False))))
    assert abs(rho - 1.00055) < 5e-4, rho
    print(f"  mobilising Euler rho(1) = {rho:.5f} (paper 1.00055) OK")
    rho = max(abs(eigvals(monodromy(1.0, CE_m, CZ_m, True))))
    assert abs(rho - 1.00035) < 5e-4, rho
    print(f"  mobilising exact rho(1) = {rho:.5f} (paper 1.00035) OK")
    rhos_p_ex, _, _ = scan(CE_p, CZ_p, True)
    print(f"  protective exact max rho on [0.2,200] = {rhos_p_ex.max():.4f} (paper 0.9967 on [0.2,120])")

    print("\n=== 1. COMPLETE CROSSING RECORD, [0.2, 200] yr ===")
    rows = []
    for label, CE, CZ in (("mobilising", CE_m, CZ_m), ("protective", CE_p, CZ_p)):
        for upd, exact in (("Euler", False), ("exact", True)):
            _, cr, iv = scan(CE, CZ, exact)
            print(f"  {label:11} {upd:6}: crossings = {[(round(x[0],4), x[1], x[4]) for x in cr]}")
            print(f"  {label:11} {upd:6}: stable intervals = {[(round(i[0],3), round(i[1],3)) for i in iv]}")
            for Tk, kind, re, im, direction in cr:
                rows.append(dict(channel=label, update=upd, T_crossing=round(Tk, 4),
                                 kind=kind, eig_real=round(float(re), 4),
                                 eig_imag=round(float(im), 4), direction=direction))
            for s, e_ in iv:
                rows.append(dict(channel=label, update=upd, T_crossing="interval",
                                 kind=f"[{round(s,3)}, {round(e_,3)}]", eig_real="", eig_imag="",
                                 direction="stable"))
    pd.DataFrame(rows).to_csv(OUT / "p5_crossing_record.csv", index=False)

    print("\n=== 2. PROTECTIVE CONTROLLER ON THE SAME MAPS (declared U3 run) ===")
    rho_p_ex_1 = max(abs(eigvals(monodromy(1.0, CE_p, CZ_p, True))))
    rho_p_eu_1 = max(abs(eigvals(monodromy(1.0, CE_p, CZ_p, False))))
    print(f"  protective exact: rho(1) = {rho_p_ex_1:.4f}, max over [0.2,200] = {rhos_p_ex.max():.4f}")
    print(f"  protective Euler: rho(1) = {rho_p_eu_1:.4f} (unstable beyond ~2.306, command-step artefact)")

    print("\n=== 3. LINEAR TRAJECTORY MSE, EULER vs EXACT (command-step distortion) ===")
    Tgrid = [0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0, 40.0, 80.0, 120.0, 200.0]
    n_rev = 3000
    x0 = np.array([1.0 / K, 1.0 / (r * K), 1.0 / Emax])  # unit scaled norm
    mse_rows = []
    for label, CE, CZ in (("mobilising", CE_m, CZ_m), ("protective", CE_p, CZ_p)):
        for T in Tgrid:
            ME = monodromy(T, CE, CZ, False)
            MX = monodromy(T, CE, CZ, True)
            rhoE = max(abs(eigvals(ME)))
            rhoX = max(abs(eigvals(MX)))
            xE, xX = x0.copy(), x0.copy()
            sq = 0.0
            divE = divX = None
            for k in range(n_rev):
                if divE is None and np.linalg.norm(xE) > 1e6:
                    divE = k
                if divX is None and np.linalg.norm(xX) > 1e6:
                    divX = k
                if divE is not None or divX is not None:
                    break
                xE, xX = ME @ xE, MX @ xX
                sq += np.linalg.norm(xE - xX) ** 2
            rmsd = float(np.sqrt(sq / n_rev))
            mse_rows.append(dict(channel=label, T_r=T, rho_euler=round(rhoE, 6),
                                 rho_exact=round(rhoX, 6),
                                 rmsd_scaled_norm=round(rmsd, 6),
                                 euler_diverges_review=divE, exact_diverges_review=divX))
    pd.DataFrame(mse_rows).to_csv(OUT / "p5_linear_trajectory_mse.csv", index=False)
    for row in mse_rows[:12]:
        print(f"  {row['channel']:11} T_r={row['T_r']:6} rhoE={row['rho_euler']:.5f} "
              f"rhoX={row['rho_exact']:.5f} RMSD={row['rmsd_scaled_norm']:.6f} "
              f"div={row['euler_diverges_review']},{row['exact_diverges_review']}")
    print("saved:", OUT)


if __name__ == "__main__":
    main()
