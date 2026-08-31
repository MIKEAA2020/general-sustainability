#!/usr/bin/env python3
"""Exact-hold monodromy for P4 (delay dynamics paper), Section 6.4 / Section 7.

Validation gate: first reproduce the committed Euler-reviewed numbers
(protective: rho(1) = 0.9838, rho-crossing at T_r ~ 2.306 on [0.2, 20];
 mobilising: rho(1) = 1.00055, complex unit-circle crossing at 47.536 yr,
 multiplier -1 at 79.143 yr). Only if those reproduce does the exact-hold
result count as verified.

Exact held-measurement update: the effort law de/dt = C_E e + C_Z z is
integrated EXACTLY over the review interval with the measurement z held at
the flowed end-of-period value (the same flow-then-update timing convention
the paper declares for the Euler scheme); the Euler factor 1 + T_r C_E is
replaced by exp(C_E T_r), and T_r C_Z by (exp(C_E T_r) - 1) C_Z / C_E.

M_exact(T_r) = R_exact(T_r) exp(A_hold T_r)
R_exact = [[1,0,0],[0,1,0],[0, (e^{C_E T_r}-1) C_Z/C_E, e^{C_E T_r}]]
"""
import numpy as np
from numpy.linalg import eigvals
from scipy.linalg import expm

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
print(f"equilibrium: E* = {E_star:.6f} (paper ~2.08962), N* = {N_star:.6f} (paper ~89.55188), Z* = {Z_star:.6f}")

gate = 1 - E_star / Emax
A_N = r * (1 - 2 * N_star / K) - q * E_star
A_E = -q * N_star
B_N = -A_N / (2 * tm)
B_E = -A_E / (2 * tm)
d = 1 / tm
print(f"Jacobian: A_N={A_N:.8f} A_E={A_E:.8f} B_N={B_N:.8f} B_E={B_E:.8f} d={d}")

# mobilising gains (bracket of (1) at gated Candidate A)
CE_m = gate * eta * (delta / dref - 2 * E_star / Emax)
CZ_m = gate * (eta * E_star / dref + d0 * Zref / (Zref + delta) ** 2)
# protective gains (quota-tracking law (3) at eta_p = eta_A = 0.914)
CE_p = -gate * eta
E0 = E_star * (Zref + delta) / Zref
Ecap_p = -E0 * Zref / (Zref + delta) ** 2
CZ_p = gate * eta * Ecap_p
print(f"mobilising gains: C_E={CE_m:.6f} (paper -0.0595), C_Z={CZ_m:.6f} (paper +1.785)")
print(f"protective gains: C_E={CE_p:.6f} (paper -0.850336), C_Z={CZ_p:.6f} (paper -1.661702)")

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


def crossings_on_grid(Ts, CE, CZ, exact, label, committed):
    """Return spectral radius at given points + unit-circle crossing diagnostics."""
    out = {}
    for T in Ts:
        R = exact_review(T, CE, CZ) if exact else euler_review(T, CE, CZ)
        M = R @ expm(A_hold * T)
        ev = eigvals(M)
        rho = max(abs(ev))
        out[T] = (rho, ev)
    # crossing detection: sign change of rho-1 between grid points (fine grid)
    fine = np.linspace(Ts[0], Ts[-1], 200001)
    prev = None
    crossings = []
    for T in fine:
        R = exact_review(T, CE, CZ) if exact else euler_review(T, CE, CZ)
        M = R @ expm(A_hold * T)
        rho = max(abs(eigvals(M)))
        if prev is not None and (prev - 1) * (rho - 1) < 0:
            crossings.append(T)
        prev = rho
    # targeted refinement of each detected crossing
    refined = []
    for T in crossings:
        lo, hi = T - 5e-4, T + 5e-4
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            R = exact_review(mid, CE, CZ) if exact else euler_review(mid, CE, CZ)
            M = R @ expm(A_hold * mid)
            rmid = max(abs(eigvals(M)))
            Rl = exact_review(lo, CE, CZ) if exact else euler_review(lo, CE, CZ)
            rl = max(abs(eigvals(Rl @ expm(A_hold * lo))))
            if (rl - 1) * (rmid - 1) < 0:
                hi = mid
            else:
                lo = mid
        Tm = 0.5 * (lo + hi)
        M = exact_review(Tm, CE, CZ) @ expm(A_hold * Tm) if exact else euler_review(Tm, CE, CZ) @ expm(A_hold * Tm)
        ev = eigvals(M)
        near_unit = sorted(ev, key=lambda x: abs(abs(x) - 1.0))[0]
        kind = "complex-pair" if abs(near_unit.imag) > 1e-9 else "real"
        refined.append((round(Tm, 4), kind, round(near_unit.real, 4), round(near_unit.imag, 4)))
    print(f"[{label}] crossings of rho=1: {refined}")
    return out, refined


print()
print("=== VALIDATION GATE: committed Euler numbers ===")
Ts_p = np.linspace(0.2, 20.0, 199)  # paper grid [0.2, 20]
out_p, _ = crossings_on_grid(Ts_p, CE_p, CZ_p, False, "protective Euler", "rho(1)=0.9838, crossing 2.306")
print(f"  protective Euler rho(1)   = {out_p[1.0][0]:.6f} (paper 0.9838)")
for T in (2.3, 2.31):
    rho = max(abs(eigvals(euler_review(T, CE_p, CZ_p) @ expm(A_hold * T))))
    print(f"  protective Euler rho({T}) = {rho:.6f} (paper: crosses at ~2.306)")

Ts_m = np.linspace(0.2, 120.0, 1199)
out_m, _ = crossings_on_grid(Ts_m, CE_m, CZ_m, False, "mobilising Euler", "rho(1)=1.00055, 47.536 / 79.143")
print(f"  mobilising Euler rho(1)   = {out_m[1.0][0]:.6f} (paper 1.00055)")

print()
print("=== EXACT HELD-MEASUREMENT UPDATE ===")
_, rf_p = crossings_on_grid(Ts_p, CE_p, CZ_p, True, "protective exact", "")
print(f"  protective exact rho(1)   = {max(abs(eigvals(exact_review(1.0, CE_p, CZ_p) @ expm(A_hold)))):.6f} vs Euler {out_p[1.0][0]:.6f}")
# protective exact over a long grid: is it stable for ALL T_r?
Ts_pl = np.linspace(0.2, 120.0, 1199)
_, rf_pl = crossings_on_grid(Ts_pl, CE_p, CZ_p, True, "protective exact [0.2,120]", "")
out_pl = {T: (max(abs(eigvals(exact_review(T, CE_p, CZ_p) @ expm(A_hold * T)))),) for T in np.linspace(0.2, 120.0, 1199)}
print(f"  protective exact max rho on [0.2,120]: {max(v[0] for v in out_pl.values()):.6f}")

_, rf_m = crossings_on_grid(Ts_m, CE_m, CZ_m, True, "mobilising exact [0.2,120]", "")
print(f"  mobilising exact rho(1)   = computed below")
R = exact_review(1.0, CE_m, CZ_m)
print(f"  mobilising exact rho(1)   = {max(abs(eigvals(R @ expm(A_hold)))):.6f} vs Euler {out_m[1.0][0]:.6f}")
print(f"  mobilising exact rho(47.5) = {max(abs(eigvals(exact_review(47.5, CE_m, CZ_m) @ expm(A_hold * 47.5)))):.6f}")
print(f"  mobilising exact rho(79.1) = {max(abs(eigvals(exact_review(79.1, CE_m, CZ_m) @ expm(A_hold * 79.1)))):.6f}")

# eigenvalue classification at the key committed points under the exact update
for T in (1.0, 47.536, 79.143):
    M = exact_review(T, CE_m, CZ_m) @ expm(A_hold * T)
    ev = sorted(eigvals(M), key=lambda x: -abs(x))
    print(f"  mobilising exact evals at T={T}: " + ", ".join(f"{x.real:+.5f}{x.imag:+.5f}i (|.|={abs(x):.5f})" for x in ev))
