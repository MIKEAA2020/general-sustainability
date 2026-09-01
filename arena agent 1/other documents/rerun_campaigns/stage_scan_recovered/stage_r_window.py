"""
Stage-structured (maturation-delay) r-window scan
=================================================
Question: does adding a recruit-to-mature maturation delay g to the stock
equation shift the delay-instability window in regeneration rate r upward
toward real fish rates (r ~ 0.2-1.5 /yr)?

Model (delayed-recruitment / stage-lumped form, Gurney-Blythe-Nisbet style):
    dN/dt = r N(t-g) (1 - N(t-g)/K) - q E N
    deficit d = qEN - r N(t-g)(1 - N(t-g)/K)      (perceived extraction minus
                                                    current maturing regeneration)
    dZ/dt = (max(0, softplus(d) - ln2/k + delta) - Z)/tau_m
    dE/dt = (1 - E/Emax) [ eta E (Z(t-tau)/Dref - E/Emax)
                           + delta0 Z(t-tau)/(Zref + Z(t-tau)) ]
Institutional delay tau enters ONLY the effort equation (as in the base core);
the maturation delay g enters the stock equation and the deficit signal.

Equilibrium is IDENTICAL to the base core: Z* = delta; E* from the same
quadratic; N* = K(1 - qE*/r)  (since at steady state N(t-g)=N*).

Criterion (two-delay generalisation of the tau-free Hopf test):
    char. det(i w I - J0 - J1g e^{-i w g} - J1t e^{-i w tau}) = 0
    J1t rank-1 = u v^T  =>  det(A - u v^T z) = det(A)(1 - z v^T A^{-1} u),
    A = i w I - J0 - J1g e^{-i w g}
    crossing exists (for some institutional tau)  <=>  |1/(v^T A^{-1} u)| = 1
At g = 0 the linearisation reduces exactly to the base core (validated below).
"""
import numpy as np
from droop_test import (K, qc, Emax, eta, delta0, Dref, taum, Zref, k,
                        delta, LN2K)

def stage_jacobians(r, g, eta_v=None):
    """Interior equilibrium + J0, J1g, J1t. None if no interior equilibrium."""
    et = eta_v if eta_v is not None else eta
    Zs = delta
    a = -et / Emax; b = et * Zs / Dref; c = delta0 * Zs / (Zref + Zs)
    disc = b * b - 4.0 * a * c
    Es = (-b - np.sqrt(disc)) / (2.0 * a)
    Ns = K * (1.0 - qc * Es / r)
    if Ns <= 0:
        return None
    N, E, Z = Ns, Es, Zs
    h = 0.5                       # softplus'(0); floor inactive at equilibrium
    dS_dN = r * (1.0 - 2.0 * N / K)
    J0 = np.zeros((3, 3))
    J0[0, 0] = -qc * E            # dN/dN(current)
    J0[0, 2] = -qc * N            # dN/dE
    J0[1, 0] = h * qc * E / taum  # dZ/dN
    J0[1, 1] = -1.0 / taum        # dZ/dZ
    J0[1, 2] = h * qc * N / taum  # dZ/dE
    gate = 1.0 - E / Emax
    fb = et * E * (Z / Dref - E / Emax) + delta0 * Z / (Zref + Z)
    J0[2, 2] = (-1.0 / Emax) * fb + gate * et * (Z / Dref - 2.0 * E / Emax)
    J1g = np.zeros((3, 3))
    J1g[0, 0] = dS_dN             # dN/dN(t-g)
    J1g[1, 0] = -h * dS_dN / taum # dZ/dN(t-g)
    J1t = np.zeros((3, 3))
    J1t[2, 1] = gate * (et * E / Dref + delta0 * Zref / (Zref + Z) ** 2)
    return Ns, Es, Zs, J0, J1g, J1t

def stage_crossings(r, g, wmin=1e-4, wmax=40.0, nw=6000, eta_v=None):
    res = stage_jacobians(r, g, eta_v)
    if res is None:
        return None
    N, E, Z, J0, J1g, J1t = res
    u = np.zeros(3); u[2] = 1.0
    v = np.zeros(3); v[1] = J1t[2, 1]
    if abs(J1t[2, 1]) < 1e-12:
        return []
    ws = np.geomspace(wmin, wmax, nw)
    gmag = np.empty(nw)
    for iw, w in enumerate(ws):
        A = 1j * w * np.eye(3) - J0 - J1g * np.exp(-1j * w * g)
        try:
            gmag[iw] = np.abs(1.0 / np.vdot(v, np.linalg.solve(A, u)))
        except np.linalg.LinAlgError:
            gmag[iw] = np.inf
    sgn = np.sign(gmag - 1.0)
    out = []
    for i in range(nw - 1):
        if sgn[i] * sgn[i + 1] < 0:
            lo, hi = ws[i], ws[i + 1]
            glo, ghi = gmag[i], gmag[i + 1]
            for _ in range(80):
                mid = np.sqrt(lo * hi)
                A = 1j * mid * np.eye(3) - J0 - J1g * np.exp(-1j * mid * g)
                gm = np.abs(1.0 / np.vdot(v, np.linalg.solve(A, u)))
                if (gm - 1.0) * (glo - 1.0) <= 0:
                    hi = mid; ghi = gm
                else:
                    lo = mid; glo = gm
            wc = np.sqrt(lo * hi)
            A = 1j * wc * np.eye(3) - J0 - J1g * np.exp(-1j * wc * g)
            zinv = np.vdot(v, np.linalg.solve(A, u))
            z = 1.0 / zinv                     # z = e^{-i w tau}
            tau0 = (-np.angle(z)) % (2 * np.pi) / wc
            out.append((wc, tau0, 2 * np.pi / wc))
    out.sort(key=lambda t: t[0])
    return out

def scan(g_vals, rmin=0.005, rmax=2.0, nr=220, eta_v=None, nw=6000):
    rvals = np.geomspace(rmin, rmax, nr)
    print(f"  eta = {eta_v if eta_v is not None else eta}")
    for g in g_vals:
        inwin = []
        for r in rvals:
            cr = stage_crossings(r, g, nw=nw, eta_v=eta_v)
            if cr is not None and len(cr) > 0:
                inwin.append(r)
        if inwin:
            print(f"    g={g:5.1f} yr: window r in [{min(inwin):.5f}, {max(inwin):.5f}]"
                  f"   (upper edge {max(inwin):.4f} yr^-1)")
        else:
            print(f"    g={g:5.1f} yr: no delay-Hopf window")
    # crossings at fish-like r for each g
    print("  crossings at r >= 0.2 (fish range):")
    for g in g_vals:
        fish = sum(1 for r in np.geomspace(rmin, rmax, nr)
                   if r >= 0.2 and stage_crossings(r, g, nw=nw, eta_v=eta_v) is not None
                   and len(stage_crossings(r, g, nw=nw, eta_v=eta_v)) > 0)
        print(f"    g={g:5.1f}: {fish} grid points with crossings at r>=0.2")

if __name__ == "__main__":
    print("=" * 72)
    print("VALIDATION: g=0 must reproduce the base core windows")
    print("=" * 72)
    for eta_v in (0.914, 3.0):
        inwin = []
        for r in np.geomspace(0.005, 2.0, 220):
            cr = stage_crossings(r, 0.0, eta_v=eta_v)
            if cr is not None and len(cr) > 0:
                inwin.append(r)
        print(f"  eta={eta_v}: g=0 window r in [{min(inwin):.5f}, {max(inwin):.5f}]"
              f"   (base from droop_test: (0.0080,0.0223) / (0.0068,0.0612))")
    print()
    print("=" * 72)
    print("STAGE-SCANNED r-WINDOWS  (gated core)")
    print("=" * 72)
    gs = [0.5, 1.0, 2.0, 5.0, 10.0, 15.0, 20.0, 50.0]
    scan(gs, eta_v=0.914, nw=5000)
    print()
    scan(gs, eta_v=3.0, nw=5000)
