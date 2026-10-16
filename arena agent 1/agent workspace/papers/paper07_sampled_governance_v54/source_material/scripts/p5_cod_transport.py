#!/usr/bin/env python3
"""Settle plan section 2.4: run P5's crossing scan on Northern cod's biology.

P5's 6.501 yr crossing was computed on an illustrative baseline
(r = 0.02 /yr, K = 100). E2's T* = 6/6/7 yr was computed on Northern cod
(committed r = 0.2369 /yr, K = 5000 kt). The plan's section 2 asks whether the
two are one quantity. Comparing published numbers across two different systems
cannot answer that; running both objects on one system can.

Model: P5's logistic hold-map core, transcribed from
  arena agent 1/other documents/rerun_campaigns/campaign_p5_crossing_scan.py
State (N, Z, E) = biomass, a low-passed measurement, effort. Continuous hold
for T_r years, then a review update R (Euler or exact) that resets effort from
the measurement. Monodromy M(T) = R(T) @ expm(A_hold * T); the crossing is
max|eig M| = 1.

In scaled coordinates (dN/K, dZ/(rK), dE/Emax) the linearised system depends
only on r, the exploitation ratio N*/K, and the institutional parameters --
K and Emax drop out. So "transport to cod" means changing r and N*/K and
nothing else. Eigenvalues are similarity-invariant, so plugging (r, K, q) into
the unscaled code reproduces the scaled system exactly.

Validation gate first: P5's committed crossing record must reproduce before any
new number counts.
"""
import math

import numpy as np
from numpy.linalg import eigvals
from scipy.linalg import expm

# ---- institutional parameters: HELD at P5's baseline in every run ----------
ETA, EMAX, DREF = 0.914, 30.0, 1.0
D0, TM, ZREF = 0.01, 5.0, 1.0
DELTA = math.log(2) / 10.0


def build(r, K, q):
    """Linearisation of the logistic hold map at (N*, E*)."""
    a = -ETA / EMAX
    b = ETA * DELTA / DREF
    c = D0 * DELTA / (ZREF + DELTA)
    E_star = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    N_star = K * (1 - q * E_star / r)
    if N_star <= 0:
        raise ValueError("equilibrium biomass non-positive: q too large")
    gate = 1 - E_star / EMAX
    A_N = r * (1 - 2 * N_star / K) - q * E_star      # = -r N*/K at equilibrium
    A_E = -q * N_star
    d = 1.0 / TM
    B_N = -A_N / (2 * TM)
    B_E = -A_E / (2 * TM)
    CE_m = gate * ETA * (DELTA / DREF - 2 * E_star / EMAX)
    CZ_m = gate * (ETA * E_star / DREF + D0 * ZREF / (ZREF + DELTA) ** 2)
    CE_p = -gate * ETA
    E0 = E_star * (ZREF + DELTA) / ZREF
    CZ_p = gate * ETA * (-E0 * ZREF / (ZREF + DELTA) ** 2)
    A_hold = np.array([[A_N, 0.0, A_E], [B_N, -d, B_E], [0.0, 0.0, 0.0]])
    return A_hold, CE_m, CZ_m, CE_p, CZ_p, E_star, N_star


def monodromy(T, A_hold, CE, CZ, exact):
    R = np.eye(3)
    if exact:
        eC = math.exp(CE * T)
        R[2, 1] = (eC - 1.0) * CZ / CE
        R[2, 2] = eC
    else:
        R[2, 1] = T * CZ
        R[2, 2] = 1 + T * CE
    return R @ expm(A_hold * T)


def rho(T, A_hold, CE, CZ, exact):
    return max(abs(eigvals(monodromy(T, A_hold, CE, CZ, exact))))


def scan(A_hold, CE, CZ, exact, Tmin=0.05, Tmax=200.0, n=40001):
    Ts = np.linspace(Tmin, Tmax, n)
    rhos = np.array([rho(T, A_hold, CE, CZ, exact) for T in Ts])
    signs = np.sign(rhos - 1.0)
    idx = np.where((signs[1:] * signs[:-1] < 0) & (signs[:-1] != 0)
                   & (signs[1:] != 0))[0]
    out = []
    for i in idx:
        lo, hi, rlo = Ts[i], Ts[i + 1], rhos[i]
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            rm = rho(mid, A_hold, CE, CZ, exact)
            if (rlo - 1) * (rm - 1) < 0:
                hi = mid
            else:
                lo, rlo = mid, rm
        Tk = 0.5 * (lo + hi)
        ev = eigvals(monodromy(Tk, A_hold, CE, CZ, exact))
        near = sorted(ev, key=lambda x: abs(abs(x) - 1.0))[0]
        kind = ("complex-pair" if abs(near.imag) > 1e-6
                else ("real+1" if near.real > 0 else "real-1"))
        direction = ("stable->unstable" if rhos[i] < 1 < rhos[i + 1]
                     else "unstable->stable")
        out.append((Tk, kind, direction))
    return rhos, out


def record(r, K, q, label):
    A_hold, CE_m, CZ_m, CE_p, CZ_p, E_star, N_star = build(r, K, q)
    print("\n%s" % label)
    print("  r = %.4f /yr   K = %.0f   q = %.5f   E* = %.4f   N*/K = %.4f"
          % (r, K, q, E_star, N_star / K))
    print("  A_N = %+.5f  (= -r N*/K)   rho(1) mobilising exact = %.5f"
          % (r * (1 - 2 * N_star / K) - q * E_star,
             rho(1.0, A_hold, CE_m, CZ_m, True)))
    rows = []
    for chan, CE, CZ in (("mobilising", CE_m, CZ_m), ("protective", CE_p, CZ_p)):
        for upd, exact in (("exact", True), ("Euler", False)):
            _, cr = scan(A_hold, CE, CZ, exact)
            if cr:
                for Tk, kind, direction in cr:
                    print("    %-11s %-6s crossing T = %9.4f yr  %-13s %s"
                          % (chan, upd, Tk, kind, direction))
                    rows.append((chan, upd, Tk, kind, direction))
            else:
                print("    %-11s %-6s no crossing on [0.05, 200]"
                      % (chan, upd))
    return rows


print("=" * 78)
print("VALIDATION GATE: P5's committed record must reproduce")
print("  expected: mobilising Euler 47.536 (complex) + 79.143 (real -1);")
print("            mobilising exact ~6.5 (single);")
print("            protective Euler 2.306; protective exact stable throughout")
print("=" * 78)
base = record(0.02, 100.0, 0.001, "P5 baseline (illustrative)")

# ---------------------------------------------------------------- cod
R_COD, K_COD, KSTAR = 0.2369, 5000.0, 884.6
E_STAR = build(0.02, 100.0, 0.001)[5]          # institutional only, r-independent
# calibrate q so that the equilibrium sits at the cod limit reference point
q_lrp = (1 - KSTAR / K_COD) * R_COD / E_STAR
# calibrate q to preserve P5's exploitation ratio (isolates the rate change)
q_same = (1 - 0.8955) * R_COD / E_STAR

cod_lrp = record(R_COD, K_COD, q_lrp,
                 "COD, equilibrium at the limit reference point (N*/K = %.4f)"
                 % (KSTAR / K_COD))
cod_same = record(R_COD, K_COD, q_same,
                  "COD, P5's exploitation ratio held (N*/K = 0.8955)")
cod_raw = record(R_COD, K_COD, 0.001, "COD, q left at P5's value (no recalibration)")

# ------------------------------------------- how does the crossing move with r?
print("\n" + "=" * 78)
print("SWEEP: where does the mobilising-exact crossing sit as r varies?")
print("(N*/K held at P5's 0.8955; institutional parameters unchanged)")
print("=" * 78)
E_S = E_STAR
print("  %8s  %-12s  %s" % ("r /yr", "T_cross (yr)", "note"))
for r_test in (0.02, 0.05, 0.10, 0.15, 0.20, 0.2369, 0.30, 0.40, 0.60, 1.0):
    q_t = (1 - 0.8955) * r_test / E_S
    A, CE_m, CZ_m, _, _, _, _ = build(r_test, 100.0, q_t / 1.0)
    # build with K=100 then rescale q so N*/K is right: q enters only via q*E*/r
    A, CE_m, CZ_m, _, _, _, _ = build(r_test, 100.0, (1 - 0.8955) * r_test / E_S)
    _, cr = scan(A, CE_m, CZ_m, True)
    note = ""
    if abs(r_test - 0.02) < 1e-9:
        note = "<-- P5 baseline"
    if abs(r_test - R_COD) < 1e-4:
        note = "<-- Northern cod"
    if cr:
        print("  %8.4f  %-12s  %s" % (r_test, ", ".join("%.4f" % c[0] for c in cr), note))
    else:
        print("  %8.4f  %-12s  %s" % (r_test, "none", note))
