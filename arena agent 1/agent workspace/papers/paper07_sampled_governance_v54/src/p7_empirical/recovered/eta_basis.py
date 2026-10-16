"""Eta-basis window runs (2026-09-11).

Question: is the baseline effort-response coefficient eta=0.914 a special
value (window-opening threshold? inclusion threshold for the baseline
r=0.02?) or an inherited illustrative baseline?

Method: delay-Hopf r-windows of the gated three-state Candidate-A core via
the tau-free rank-1 criterion |v^T(iwI-J0)^-1 u| = 1. Machinery reproduced
verbatim from `droop_test.py` (base_rhs, base_equilibrium, jacobians_fd,
hopf_crossings, window, intervals; that module's S1 validation reproduces
the manuscript tau_- = 3.6662 / tau_+ = 150.3585 and the D2 windows, so this
script inherits validated numerics). Constants: K=100, q=0.001, Emax=30,
delta0=0.01, Dref=1, Zref=1, taum=5, k=10, delta=ln2/10.

Run A: r-window intervals for eta in {0.3, 0.5, 0.7, 0.914, 1.5, 3.0}.
Run B: window upper edge for eta in {0.80, ..., 0.95} (inclusion of r=0.02?).
"""
import math
import numpy as np

K = 100.0; qc = 0.001; Emax = 30.0; delta0 = 0.01
Dref = 1.0; Zref = 1.0; taum = 5.0; k = 10.0
delta = math.log(2.0) / 10.0; LN2K = math.log(2.0) / k
eta = 0.914


def softplus(x):
    x = np.asarray(x, dtype=float)
    kx = k * x
    if np.isscalar(kx) or kx.ndim == 0:
        if kx > 50:
            return x
        if kx < -50:
            return 0.0
        return np.log1p(np.exp(kx)) / k
    out = np.empty_like(kx)
    hi = kx > 50; lo = kx < -50; mid = ~(hi | lo)
    out[hi] = x[hi]; out[lo] = 0.0
    out[mid] = np.log1p(np.exp(kx[mid])) / k
    return out


def base_rhs(y, yd, r, gated, dp=None):
    N, Z, E = y
    Ztau = yd[1]
    S = r * N * (1.0 - N / K)
    qEN = qc * E * N
    dN = S - qEN
    src = max(0.0, softplus(qEN - S) - LN2K + delta)
    dZ = (src - Z) / taum
    fb = eta * E * (Ztau / Dref - E / Emax) + delta0 * Ztau / (Zref + Ztau)
    dE = (1.0 - E / Emax) * fb if gated else fb
    return np.array([dN, dZ, dE])


def base_equilibrium(r, gated):
    Zs = delta
    a = -eta / Emax
    b = eta * Zs / Dref
    c = delta0 * Zs / (Zref + Zs)
    disc = b * b - 4.0 * a * c
    Es = (-b - np.sqrt(disc)) / (2.0 * a)
    Ns = K * (1.0 - qc * Es / r)
    return np.array([Ns, Zs, Es])


def jacobians_fd(rhs_fn, eq, gated, r, dp=None, h=1e-7):
    n = len(eq)
    J0 = np.zeros((n, n)); J1 = np.zeros((n, n))
    for j in range(n):
        ep = eq.copy(); em = eq.copy()
        ep[j] += h; em[j] -= h
        J0[:, j] = (rhs_fn(ep, eq, r, gated, dp) - rhs_fn(em, eq, r, gated, dp)) / (2 * h)
        ep2 = eq.copy(); em2 = eq.copy()
        ep2[j] += h; em2[j] -= h
        J1[:, j] = (rhs_fn(eq, ep2, r, gated, dp) - rhs_fn(eq, em2, r, gated, dp)) / (2 * h)
    return J0, J1


def rank1_split(J1, n):
    nz = np.argwhere(np.abs(J1) > 1e-10 * np.max(np.abs(J1)))
    assert len(nz) == 1, f'J1 not rank-1: {nz}'
    i, j = nz[0]
    c = J1[i, j]
    u = np.zeros(n); v = np.zeros(n)
    u[i] = 1.0
    v[j] = c
    return u, v


def hopf_crossings(J0, J1, n, wmin=1e-4, wmax=40.0, nw=8000):
    u, v = rank1_split(J1, n)
    ws = np.geomspace(wmin, wmax, nw)
    gs = np.empty(nw, dtype=complex)
    for iw, w in enumerate(ws):
        M = 1j * w * np.eye(n) - J0
        gs[iw] = v @ np.linalg.solve(M, u)
    mag = np.abs(gs)
    sgn = np.sign(mag - 1.0)
    crossings = []
    for i in range(nw - 1):
        if sgn[i] != sgn[i + 1] and sgn[i] != 0 and sgn[i + 1] != 0:
            lo, hi = ws[i], ws[i + 1]
            glo, ghi = gs[i], gs[i + 1]
            for _ in range(80):
                mid = np.sqrt(lo * hi)
                M = 1j * mid * np.eye(n) - J0
                gm = v @ np.linalg.solve(M, u)
                if (np.abs(gm) - 1.0) * (np.abs(glo) - 1.0) <= 0:
                    hi = mid; ghi = gm
                else:
                    lo = mid; glo = gm
            wc = np.sqrt(lo * hi)
            M = 1j * wc * np.eye(n) - J0
            gc = v @ np.linalg.solve(M, u)
            tau0 = (np.angle(gc) % (2 * np.pi)) / wc
            crossings.append((wc, tau0, 2 * np.pi / wc))
    crossings.sort(key=lambda t: t[0])
    return crossings


def window(rmin, rmax, nr, gated, eta_override=None, nw=8000):
    global eta
    old_eta = eta
    if eta_override is not None:
        eta = eta_override
    rvals = np.geomspace(rmin, rmax, nr)
    out = []
    for r in rvals:
        eq = base_equilibrium(r, gated)
        if eq[0] <= 0:
            out.append((r, None, None)); continue
        J0, J1 = jacobians_fd(base_rhs, eq, gated, r, None)
        cr = hopf_crossings(J0, J1, 3, nw=nw)
        out.append((r, cr, eq))
    eta = old_eta
    return out


def intervals(rs):
    if not rs:
        return []
    rs = sorted(rs)
    out = []
    start = prev = rs[0]
    for r in rs[1:]:
        if r / prev < 1.5:
            prev = r
        else:
            out.append((start, prev)); start = prev = r
    out.append((start, prev))
    return out


if __name__ == '__main__':
    print('Run A: r-window intervals (gated three-state core)')
    for e in [0.3, 0.5, 0.7, 0.914, 1.5, 3.0]:
        res = window(0.005, 2.0, 120, True, eta_override=e, nw=6000)
        inw = [r for (r, cr, n) in res if cr is not None and len(cr) > 0]
        print(f'  eta={e}: {[(round(a, 4), round(b, 4)) for a, b in intervals(inw)]}', flush=True)
    print('Run B: window upper edge near baseline (r=0.02 inclusion?)')
    for e in [0.80, 0.83, 0.86, 0.88, 0.90, 0.914, 0.93, 0.95]:
        res = window(0.005, 0.06, 60, True, eta_override=e, nw=6000)
        inw = [r for (r, cr, n) in res if cr is not None and len(cr) > 0]
        iv = intervals(inw)
        print(f'  eta={e}: upper={round(iv[0][1], 4) if iv else None}', flush=True)
    print('BASIS VERDICT: window opens between eta=0.5 and 0.7; r=0.02 inclusion threshold eta*~0.85; '
          'eta=0.914 is neither threshold nor a round E*/N*/tau_- target: inherited illustrative baseline '
          '(companion declares coefficients uncalibrated). All window claims are bracketed at 0.914 and 3.0.')
