#!/usr/bin/env python3
"""Numba kernels for the P4 five-regime continuation campaign (pre-registered
2026-09-03, executed by p4_campaign.py).

Two kernels, both method-of-steps RK4 with a circular delay buffer and linear
interpolation of the delayed Z read at the exact delay tau (tau need not be a
multiple of dt):

1. `basin_run` — the nonlinear gated three-state DDE (Candidate A, the
   committed a025_model.PAR, frozen numeric copy verified equivalent to
   a025_model.rhs by p4_campaign.py stage 0).
2. `var_advance` — one period advance of the variational (linearized) system
   along a reference orbit (the collocation orbit sampled on the fine grid),
   used for Floquet multipliers of the discrete period map (the committed
   machinery's own shooting/period-map Floquet method, applied along
   collocation orbits).

The parameter layout (frozen Candidate A numbers):
    pa = [r, K, q, eta, Emax, delta0, Dref, taum, k]
        = [0.02, 100.0, 0.001, 0.914, 30.0, 0.01, 1.0, 5.0, 10.0]
"""
from __future__ import annotations

import numpy as np
from numba import njit


# --------------------------------------------------------------------------
# 1. Basin kernel (nonlinear DDE, method-of-steps RK4, circular Z buffer)
# --------------------------------------------------------------------------
@njit(fastmath=True, cache=True)
def basin_rhs(N, Z, E, Zd, pa):
    r, K, q, eta, Emax, delta0, Dref, taum, k = pa
    S = r * N * (1.0 - N / K)
    C = q * E * N
    ku = k * (C - S)
    if ku > 30.0:
        sp = (C - S)
    elif ku < -30.0:
        sp = np.exp(ku) / k
    else:
        sp = np.log1p(np.exp(ku)) / k
    mem = sp if sp > 0.0 else 0.0        # gate floor: max(0, softplus)
    floor_hit = 1 if sp <= 0.0 else 0
    dN = S - C
    dZ = (mem - Z) / taum
    gate = 1.0 - E / Emax
    dE = gate * (eta * E * (Zd / Dref - E / Emax)
                 + delta0 * Zd / (1.0 + Zd))
    return dN, dZ, dE, floor_hit


@njit(fastmath=True, cache=True)
def basin_run(tau, dt, n_steps, hist_N, hist_Z, hist_E, pa,
              ring, tail_N):
    """Run one basin simulation. `ring` (n_ring, 3) receives the last
    n_ring states of the trajectory (for orbit extraction); `tail_N`
    (n_tail,) receives the last n_tail N values (for the classification
    statistics). Returns a stats vector:
    [max_E, floor_hits, clip_N, clip_E, tail_N_min, tail_N_max,
     tail_N_mean, tail_N_std].
    All histories are constant (H1/H2/H3 as pre-registered), so the initial
    uniform fill of the Z buffer is exact.
    """
    d = tau / dt                       # delay in grid units (fractional)
    n_tau = int(round(d))
    L = n_tau + 2
    zbuf = np.full(L, hist_Z)
    N, Z, E = hist_N, hist_Z, hist_E
    idx = 0
    zbuf[idx] = Z
    n_ring = ring.shape[0]
    n_tail = tail_N.shape[0]
    max_E = E
    floor_hits = 0
    clip_N = 0
    clip_E = 0
    for step in range(n_steps):
        # ---- RK4 stage 1 (t = step*dt) -------------------------------
        c = step - d                     # delayed read position (grid units)
        a = int(np.floor(c))
        fr = c - a
        if fr == 0.0:
            Zd = zbuf[a % L]
        else:
            Zd = (1.0 - fr) * zbuf[a % L] + fr * zbuf[(a + 1) % L]
        dN1, dZ1, dE1, fh = basin_rhs(N, Z, E, Zd, pa)
        floor_hits += fh
        # ---- stage 2 (t + dt/2) --------------------------------------
        N2 = N + 0.5 * dt * dN1
        Z2 = Z + 0.5 * dt * dZ1
        E2 = E + 0.5 * dt * dE1
        c = step + 0.5 - d
        a = int(np.floor(c))
        fr = c - a
        if fr == 0.0:
            Zd = zbuf[a % L]
        else:
            Zd = (1.0 - fr) * zbuf[a % L] + fr * zbuf[(a + 1) % L]
        dN2, dZ2, dE2, fh = basin_rhs(N2, Z2, E2, Zd, pa)
        floor_hits += fh
        # ---- stage 3 (t + dt/2, stage-2 state) -----------------------
        N3 = N + 0.5 * dt * dN2
        Z3 = Z + 0.5 * dt * dZ2
        E3 = E + 0.5 * dt * dE2
        dN3, dZ3, dE3, fh = basin_rhs(N3, Z3, E3, Zd, pa)
        floor_hits += fh
        # ---- stage 4 (t + dt, stage-3 state) -------------------------
        N4 = N + dt * dN3
        Z4 = Z + dt * dZ3
        E4 = E + dt * dE3
        c = step + 1.0 - d
        a = int(np.floor(c))
        fr = c - a
        if fr == 0.0:
            Zd = zbuf[a % L]
        else:
            Zd = (1.0 - fr) * zbuf[a % L] + fr * zbuf[(a + 1) % L]
        dN4, dZ4, dE4, fh = basin_rhs(N4, Z4, E4, Zd, pa)
        floor_hits += fh
        # ---- combine --------------------------------------------------
        N = N + dt / 6.0 * (dN1 + 2.0 * dN2 + 2.0 * dN3 + dN4)
        Z = Z + dt / 6.0 * (dZ1 + 2.0 * dZ2 + 2.0 * dZ3 + dZ4)
        E = E + dt / 6.0 * (dE1 + 2.0 * dE2 + 2.0 * dE3 + dE4)
        if N < 0.0:
            N = 0.0
            clip_N += 1
        if E < 0.0:
            E = 0.0
            clip_E += 1
        if E > 30.0:
            E = 30.0
            clip_E += 1
        if E > max_E:
            max_E = E
        idx = (idx + 1) % L
        zbuf[idx] = Z
        ring[step % n_ring, 0] = N
        ring[step % n_ring, 1] = Z
        ring[step % n_ring, 2] = E
        tail_N[step % n_tail] = N
    if n_steps >= n_tail:
        tn = tail_N.copy()
    else:
        tn = tail_N[:n_steps]
    tmin = tn.min()
    tmax = tn.max()
    tmean = tn.mean()
    tstd = tn.std()
    return np.array([max_E, float(floor_hits), float(clip_N), float(clip_E),
                     tmin, tmax, tmean, tstd])


# --------------------------------------------------------------------------
# 2. Variational segment-map kernel (linearized DDE along a reference orbit)
# --------------------------------------------------------------------------
@njit(fastmath=True, cache=True)
def var_advance(state, zbuf, n_steps, dt, d, L,
                a11, a13, a21, a22, a23, ade, adz, ring3):
    """Advance the variational state one full period (n_steps RK4 steps).

    state  : (3,) in/out — (dN, dZ, dE) at the current grid time.
    zbuf   : (L,) in/out — circular buffer of dZ at past grid times; on
             entry it holds the input segment's dZ column at grid indices
             -L+1..0 (the entry at -L+1 duplicates -L+2; only read when the
             fractional delay rounds up).
    ring3  : (L, 3) out — receives the computed states at grid indices
             (current-L+1..current) so the caller can assemble the output
             segment.
    a11..adz: (2*n_steps+1,) fine-grid (spacing dt/2) coefficient arrays of
             the variational equation, ordered as
             dN' = a11 dN + a13 dE
             dZ' = a21 dN + a22 dZ + a23 dE
             dE' = ade dE + adz * dZ(t - tau)
    """
    dN, dZ, dE = state[0], state[1], state[2]
    idx = 0
    for step in range(n_steps):
        # stage 1: fine index 2*step
        i0 = 2 * step
        c = step - d
        a = int(np.floor(c))
        fr = c - a
        if fr == 0.0:
            Zd = zbuf[a % L]
        else:
            Zd = (1.0 - fr) * zbuf[a % L] + fr * zbuf[(a + 1) % L]
        k1N = a11[i0] * dN + a13[i0] * dE
        k1Z = a21[i0] * dN + a22[i0] * dZ + a23[i0] * dE
        k1E = ade[i0] * dE + adz[i0] * Zd
        # stage 2: fine index 2*step+1, state + dt/2*k1
        i1 = 2 * step + 1
        N2 = dN + 0.5 * dt * k1N
        Z2 = dZ + 0.5 * dt * k1Z
        E2 = dE + 0.5 * dt * k1E
        c = step + 0.5 - d
        a = int(np.floor(c))
        fr = c - a
        if fr == 0.0:
            Zd = zbuf[a % L]
        else:
            Zd = (1.0 - fr) * zbuf[a % L] + fr * zbuf[(a + 1) % L]
        k2N = a11[i1] * N2 + a13[i1] * E2
        k2Z = a21[i1] * N2 + a22[i1] * Z2 + a23[i1] * E2
        k2E = ade[i1] * E2 + adz[i1] * Zd
        # stage 3: fine index 2*step+1, state + dt/2*k2
        N3 = dN + 0.5 * dt * k2N
        Z3 = dZ + 0.5 * dt * k2Z
        E3 = dE + 0.5 * dt * k2E
        k3N = a11[i1] * N3 + a13[i1] * E3
        k3Z = a21[i1] * N3 + a22[i1] * Z3 + a23[i1] * E3
        k3E = ade[i1] * E3 + adz[i1] * Zd
        # stage 4: fine index 2*step+2, state + dt*k3
        i2 = 2 * step + 2
        N4 = dN + dt * k3N
        Z4 = dZ + dt * k3Z
        E4 = dE + dt * k3E
        c = step + 1.0 - d
        a = int(np.floor(c))
        fr = c - a
        if fr == 0.0:
            Zd = zbuf[a % L]
        else:
            Zd = (1.0 - fr) * zbuf[a % L] + fr * zbuf[(a + 1) % L]
        k4N = a11[i2] * N4 + a13[i2] * E4
        k4Z = a21[i2] * N4 + a22[i2] * Z4 + a23[i2] * E4
        k4E = ade[i2] * E4 + adz[i2] * Zd
        dN = dN + dt / 6.0 * (k1N + 2.0 * k2N + 2.0 * k3N + k4N)
        dZ = dZ + dt / 6.0 * (k1Z + 2.0 * k2Z + 2.0 * k3Z + k4Z)
        dE = dE + dt / 6.0 * (k1E + 2.0 * k2E + 2.0 * k3E + k4E)
        idx = (idx + 1) % L
        zbuf[idx] = dZ
        ring3[idx, 0] = dN
        ring3[idx, 1] = dZ
        ring3[idx, 2] = dE
    state[0] = dN
    state[1] = dZ
    state[2] = dE
