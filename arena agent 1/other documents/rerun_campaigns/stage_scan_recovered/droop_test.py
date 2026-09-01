"""droop_test shim — RECONSTRUCTED (2026-09-01), not the original module.

The recovered stage scripts (stage_r_window.py, stage_tau0_decomposition.py,
stage_robust_check.py, stage_decomp2.py) import constants and helpers from a
module named droop_test that was not among the recovered files. This shim
supplies them so the recovered scripts can be executed verbatim.

Constant values are taken from the recovered compute_core.py parameter block
(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0, d0=0.01, Dref=1.0, Zref=1.0,
taum=5.0, k=10.0, delta=ln2/10), which is the base-core parameterization the
stage scripts' own validation targets reference (N*=89.55 at r=0.02;
tau=5.5 -> period ~268 yr, amplitude ~7.2). The base RHS, softplus, and the
single-delay RK4 integrator reproduce compute_core.py's rhs() and simulate()
patterns (gated core, delay on Z in the effort equation).
"""
import math

import numpy as np

K = 100.0
qc = 0.001
Emax = 30.0
eta = 0.914
delta0 = 0.01
Dref = 1.0
Zref = 1.0
taum = 5.0
k = 10.0
delta = math.log(2.0) / 10.0
LN2K = math.log(2.0) / k


def softplus(x):
    """softplus(x) = log1p(exp(k*x))/k with the stage scripts' k=10 convention.
    Called with the RAW deficit d (the k multiplication is inside), so that
    softplus'(0) = 1/2, matching the h = 0.5 linearisations and the
    filt(0) = ln2/k - ln2/k + delta = delta equilibrium convention."""
    kx = k * x
    if kx > 40:
        return x
    if kx < -40:
        return math.exp(kx) / k
    return math.log1p(math.exp(kx)) / k


def base_equilibrium(r, gated=True):
    """Returns [N*, Z*, E*] for the base core at regeneration rate r."""
    Zs = delta
    a = -eta / Emax
    b = eta * (Zs / Dref)
    c = delta0 * Zs / (Zref + Zs)
    rts = np.roots([a, b, c])
    pos = [float(np.real(x)) for x in rts if abs(np.imag(x)) < 1e-12 and np.real(x) > 0]
    Es = pos[0] if pos else float("nan")
    Ns = K * (1.0 - qc * Es / r)
    return np.array([Ns, Zs, Es])


def base_rhs(y, Zd, r, gated=True):
    N, Z, E = y
    S = r * N * (1.0 - N / K)
    phi = qc * E * N - S
    sp = softplus(phi)
    filt = sp - math.log(2.0) / k + delta
    if filt < 0.0:
        filt = 0.0
    dN = S - qc * E * N
    dZ = (filt - Z) / taum
    h = eta * E * (Zd / Dref - E / Emax) + delta0 * Zd / (Zref + Zd)
    if gated:
        g = 1.0 - E / Emax
        if g < 0.0:
            g = 0.0
        dE = g * h
    else:
        dE = h
    return np.array([dN, dZ, dE])


def integrate_dde(rhs, y0, hist, T, tau, r, gated, extra=None, dt=0.05):
    """Single-delay (tau on Z) fixed-step RK4 with history interpolation,
    following the recovered scripts' calling convention:
    integrate_dde(base_rhs, y0, hist, 3000, 5.5, 0.02, True, None, dt=0.05)."""
    nsteps = int(round(T / dt))
    h = T / nsteps
    ys = np.zeros((nsteps + 1, 3))
    ys[0] = y0
    tau_ = max(tau, 1e-9)

    def delayed_z(t):
        tt = t - tau_
        if tt <= 0:
            return hist(tt)[1]
        ti = tt / h
        i = int(np.floor(ti))
        if i >= nsteps:
            return ys[nsteps, 1]
        fr = ti - i
        return (1 - fr) * ys[i, 1] + fr * ys[i + 1, 1]

    for i in range(nsteps):
        t = i * h
        y = ys[i]
        zd1 = delayed_z(t)
        k1 = rhs(y, zd1, r, gated)
        zd2 = delayed_z(t + h / 2)
        k2 = rhs(y + h / 2 * k1, zd2, r, gated)
        k3 = rhs(y + h / 2 * k2, zd2, r, gated)
        zd4 = delayed_z(t + h)
        k4 = rhs(y + h * k3, zd4, r, gated)
        ys[i + 1] = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return ys
