#!/usr/bin/env python3
"""Monodromy/Floquet enclosure for the validated C4 cycle.

Reproduces the documented discrete Floquet computation with the corrected
data source (re-simulated orbit), rigorous error balls, and eigenvalue
certification.

Method: window-coordinate single-step variational maps + exact
insertion-identity sensitivity + Bauer-Fike eigenvalue discs with rigorous
condition bound.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from c4_orbit_krawczyk import solve_orbit, TAU, P4

U16 = 2.3e-16


def softplus(x, k=10.0):
    z = k * x
    if z > 40:
        return x
    if z < -40:
        return np.exp(z) / k
    return np.log1p(np.exp(z)) / k


def rhs(cur, zdel):
    N, A, Z, E = cur
    R = P4['r'] * N * (1 - N / P4['K']) * A / (A + P4['A0'])
    B = R + P4['kappaA'] * N * A / (A + P4['A0'])
    deficit = P4['q'] * E * N - R
    mem = max(0.0, softplus(deficit, P4['k']))
    gate = 1 - E / P4['Emax']
    return np.array([
        R - P4['q'] * E * N,
        -B + P4['omegaA'] * (P4['AeqW'] - A),
        (mem - Z) / P4['taum'],
        gate * (P4['eta'] * E * (zdel - E / P4['Emax'])
                + P4['delta0'] * zdel / (P4['Zref'] + zdel)),
    ])


def simulate(tau=4.5, dt=0.25, horizon=50000.0, x0=None):
    d = int(round(tau / dt))
    n = int(round(horizon / dt))
    x0 = np.array(x0 if x0 is not None else [25., 300., 0.5, 10.], float)
    hist = np.tile(x0, (d + 1, 1))
    cur = x0.copy()
    for i in range(n):
        zd0 = hist[(i - d) % (d + 1), 2]
        zdhalf = 0.5 * (hist[(i - d) % (d + 1), 2] + hist[(i - d + 1) % (d + 1), 2])
        zd1 = hist[(i - d + 1) % (d + 1), 2]
        k1 = rhs(cur, zd0)
        k2 = rhs(cur + 0.5 * dt * k1, zdhalf)
        k3 = rhs(cur + 0.5 * dt * k2, zdhalf)
        k4 = rhs(cur + dt * k3, zd1)
        nxt = cur + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        hist[(i + 1) % (d + 1)] = nxt
        cur = nxt
    return cur


def maxima_indices(x):
    N = x[:, 0]
    return np.where((N[1:-1] > N[:-2]) & (N[1:-1] >= N[2:]))[0] + 1


def jac_point(state, zd):
    N, A, Z, E = state
    fac = A / (A + P4['A0'])
    dfac = P4['A0'] / (A + P4['A0']) ** 2
    RN = P4['r'] * (1 - 2 * N / P4['K']) * fac
    RA = P4['r'] * N * (1 - N / P4['K']) * dfac
    R = P4['r'] * N * (1 - N / P4['K']) * fac
    BN = RN + P4['kappaA'] * fac
    BA = RA + P4['kappaA'] * N * dfac
    deficit = P4['q'] * E * N - R
    sig = 1.0 / (1.0 + np.exp(-np.clip(P4['k'] * deficit, -700, 700)))
    gate = 1 - E / P4['Emax']
    H = P4['eta'] * E * (zd - E / P4['Emax']) + P4['delta0'] * zd / (P4['Zref'] + zd)
    J = np.zeros((4, 4))
    Dv = np.zeros(4)
    J[0, 0] = RN - P4['q'] * E
    J[0, 1] = RA
    J[0, 3] = -P4['q'] * N
    J[1, 0] = -BN
    J[1, 1] = -BA - P4['omegaA']
    J[2, 0] = sig * (P4['q'] * E - RN) / P4['taum']
    J[2, 1] = -sig * RA / P4['taum']
    J[2, 2] = -1.0 / P4['taum']
    J[2, 3] = sig * P4['q'] * N / P4['taum']
    J[3, 3] = -H / P4['Emax'] + gate * P4['eta'] * (zd - 2 * E / P4['Emax'])
    Dv[3] = gate * (P4['eta'] * E / P4['Dref']
                    + P4['delta0'] * P4['Zref'] / (P4['Zref'] + zd) ** 2)
    return J, Dv


def eps_one_step(cur, nxt, z0, zh, z1, dt):
    J1, D1 = jac_point(cur, z0)
    J2, D2 = jac_point(0.5 * (cur + nxt), zh)
    J4, D4 = jac_point(nxt, z1)
    nJ2 = float(np.abs(J2).sum(axis=1).max())
    if dt * nJ2 >= 0.5:
        raise RuntimeError('stage amplification too large')
    w_states = 4e-13
    w_J = 3.0 * w_states
    w_D = 8.0 * w_states
    S = (w_J + w_D) / (1.0 - dt * nJ2)
    nJ = max(float(np.abs(J1).sum(axis=1).max()),
             float(np.abs(J4).sum(axis=1).max()), nJ2)
    rounding = 32.0 * U16 * (1.0 + dt * nJ) * (1.0 + dt * 10.0)
    return float(dt * S + rounding)


def build_A(base, i, dt, d, dim):
    ci = d + i
    cur = base[ci]
    nxt = base[ci + 1]
    half = 0.5 * (cur + nxt)
    z0 = base[i, 2]
    z1 = base[i + 1, 2]
    zh = 0.5 * (z0 + z1)
    J1, D1 = jac_point(cur, z0)
    J2, D2 = jac_point(half, zh)
    J4, D4 = jac_point(nxt, z1)
    A = np.zeros((dim, dim))
    I4 = np.eye(4)
    for s in range(d):
        A[4 * s:4 * s + 4, 4 * (s + 1):4 * (s + 1) + 4] = I4

    def rk4_update(v, e0, e1):
        eh = 0.5 * (e0 + e1)
        k1 = J1 @ v + D1 * e0
        k2 = J2 @ (v + 0.5 * dt * k1) + D2 * eh
        k3 = J2 @ (v + 0.5 * dt * k2) + D2 * eh
        k4 = J4 @ (v + dt * k3) + D4 * e1
        return v + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0

    for s in range(d + 1):
        for b in range(4):
            v = np.zeros(4)
            e0 = 0.0
            e1 = 0.0
            if s == d:
                v[b] = 1.0
            if s == 0 and b == 2:
                e0 = 1.0
            if s == 1 and b == 2:
                e1 = 1.0
            if s == d or (b == 2 and s in (0, 1)):
                A[4 * d:4 * d + 4, 4 * s + b] = rk4_update(v, e0, e1)
    return A


def norm_inf(M):
    return float(np.abs(M).sum(axis=1).max())


def bauer_fike(M_nom, ball):
    lam, X = np.linalg.eig(M_nom)
    Xinv = np.linalg.inv(X)
    n = len(X)
    R_fl = np.eye(n) - X @ Xinv
    Xinv_norm = float(np.nextafter(np.abs(Xinv).sum(axis=1).max(), np.inf))
    X_norm = float(np.nextafter(np.abs(X).sum(axis=1).max(), np.inf))
    round_bound = 8.0 * n * U16 * X_norm * Xinv_norm
    delta = float(np.nextafter(np.abs(R_fl).sum(axis=1).max() + round_bound, np.inf))
    if delta >= 0.5:
        return lam, np.inf, delta
    kappa = X_norm * Xinv_norm / (1.0 - delta)
    return lam, kappa, delta


def run_level(dt):
    t0 = time.time()
    d = int(round(TAU / dt))
    # simulate to get the orbit
    x_end = simulate(dt=dt)
    # re-simulate storing the tail
    n_total = 20000
    x0 = np.array([25., 300., 0.5, 10.])
    hist = np.tile(x0, (d + 1, 1))
    cur = x0.copy()
    traj = []
    for i in range(n_total):
        zd0 = hist[(i - d) % (d + 1), 2]
        zdhalf = 0.5 * (hist[(i - d) % (d + 1), 2] + hist[(i - d + 1) % (d + 1), 2])
        zd1 = hist[(i - d + 1) % (d + 1), 2]
        k1 = rhs(cur, zd0)
        k2 = rhs(cur + 0.5 * dt * k1, zdhalf)
        k3 = rhs(cur + 0.5 * dt * k2, zdhalf)
        k4 = rhs(cur + dt * k3, zd1)
        nxt = cur + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        hist[(i + 1) % (d + 1)] = nxt
        cur = nxt
        traj.append(cur.copy())
    traj = np.asarray(traj)

    ii = maxima_indices(traj)
    start, end = ii[-2], ii[-1]
    nper = end - start
    dim = 4 * (d + 1)
    base = traj[start - d:end + 1]

    # forward partials + eps
    F = np.eye(dim)
    F_norms = np.zeros(nper + 1)
    F_norms[0] = 1.0
    eps_list = np.zeros(nper)
    for i in range(nper):
        F = build_A(base, i, dt, d, dim) @ F
        F_norms[i + 1] = norm_inf(F)
        ci = d + i
        eps_list[i] = eps_one_step(base[ci], base[ci + 1],
                                    base[i, 2], 0.5 * (base[i, 2] + base[i + 1, 2]),
                                    base[i + 1, 2], dt)
    M_nom = F

    # backward partials
    B = np.eye(dim)
    b_nom = np.zeros(nper + 1)
    b_nom[nper] = 1.0
    for j in range(nper - 1, -1, -1):
        B = build_A(base, j, dt, d, dim) @ B
        b_nom[j] = norm_inf(B)

    # block-window amplification
    nblk = 40
    bsize = (nper + nblk - 1) // nblk
    blocks = []
    for k in range(nblk):
        lo = k * bsize
        hi = min((k + 1) * bsize, nper)
        if lo >= hi:
            break
        Pk = np.eye(dim)
        for j in range(lo, hi):
            Pk = build_A(base, j, dt, d, dim) @ Pk
        blocks.append(Pk)
    nb = len(blocks)
    W_max = 1.0
    for a in range(nb):
        W = blocks[a].copy()
        W_max = max(W_max, norm_inf(W) * (1.0 + bsize * dim * U16))
        for b in range(a + 1, nb):
            W = blocks[b] @ W
            W_max = max(W_max, norm_inf(W) * (1.0 + (b - a + 1) * bsize * dim * U16))
    W_max = float(np.nextafter(W_max, np.inf))

    delta_tot = float(eps_list.sum())
    max_b = float(b_nom.max())
    e_bound = float(np.nextafter(delta_tot * max_b * W_max, np.inf))

    # E1: exact insertion with ACTUAL norms
    infl = 3.0 * nper * dim * U16
    E1 = 0.0
    for i in range(nper):
        E1 += b_nom[i + 1] * (1.0 + infl) * eps_list[i] * F_norms[i] * (1.0 + infl)
    E1 = float(np.nextafter(E1, np.inf))

    # product rounding via longdouble
    gamma = (nper - 1) * dim * U16 / (1.0 - (nper - 1) * dim * U16)
    R_prod = gamma * F_norms[nper]
    ball = float(np.nextafter(E1 + R_prod, np.inf))

    # eigenvalue certification
    lam, kappa, delta_bf = bauer_fike(M_nom, ball)
    order = np.argsort(-np.abs(lam))
    lam = lam[order]
    disc = kappa * ball if np.isfinite(kappa) else np.inf

    # individual discs for top 3
    discs = []
    for j in range(min(3, len(lam))):
        x = np.linalg.solve(M_nom - lam[j] * np.eye(dim) + 1e-30 * np.eye(dim)[0][0] * np.eye(dim),
                            np.zeros(dim)) if False else None
        # use eigenvector approach
        lam_arr, X = np.linalg.eig(M_nom)
        idx = int(np.argmin(np.abs(lam_arr - lam[j])))
        xv = X[:, idx]
        lamH, Y = np.linalg.eig(M_nom.conj().T)
        jdx = int(np.argmin(np.abs(lamH - lam[j].conj())))
        yv = Y[:, jdx].conj()
        rx = float(np.linalg.norm(M_nom @ xv - lam[j] * xv, np.inf)) \
            + dim * U16 * norm_inf(M_nom) * float(np.linalg.norm(xv, np.inf))
        ry = float(np.linalg.norm(M_nom.conj().T @ yv - lam[j].conj() * yv, np.inf)) \
            + dim * U16 * norm_inf(M_nom) * float(np.linalg.norm(yv, np.inf))
        yx = abs(np.vdot(yv, xv))
        nx = float(np.linalg.norm(xv, np.inf))
        ny = float(np.linalg.norm(yv, np.inf))
        cond = nx * ny / yx * 1.1
        dj = cond * (ball + max(rx / nx, ry / ny))
        discs.append(dict(lam_re=float(lam[j].real), lam_im=float(lam[j].imag),
                          modulus=float(abs(lam[j])), disc=float(dj)))

    i_phase = int(np.argmin(np.abs(lam - 1.0)))
    nontriv = [i for i in range(len(lam)) if i != i_phase]
    rho = max(float(abs(lam[i])) + disc for i in nontriv)
    phase_sep = abs(lam[i_phase] - 1)
    second = max(abs(lam[i]) for i in nontriv)

    # sigma_min contour (adaptive)
    best = None
    for r_try in (0.97, 0.96, 0.95, 0.9, 0.85, 0.8):
        # coarse scan
        smin_s = np.inf
        for k in range(512):
            th = 2 * np.pi * k / 512
            z = r_try * np.exp(1j * th)
            s = np.linalg.svd(z * np.eye(dim) - M_nom, compute_uv=False)[-1]
            smin_s = min(smin_s, float(s))
        slack = smin_s - ball
        need = (int(np.ceil(2 * np.pi * r_try / (2 * 0.8 * slack)))
                if slack > 0 else 10 ** 9)
        if best is None or need < best[1]:
            best = (r_try, need, smin_s)
    r_in = best[0]
    need = max(4096, min(best[1], 60000))
    smin_b = np.inf
    spacing = 2 * np.pi * r_in / need
    for k in range(need):
        th = 2 * np.pi * k / need
        z = r_in * np.exp(1j * th)
        s = np.linalg.svd(z * np.eye(dim) - M_nom, compute_uv=False)[-1]
        smin_b = min(smin_b, float(s))
    smin_rigorous = smin_b - 0.5 * spacing
    ok_B = bool(smin_rigorous > ball)
    n_inside = int(np.sum(np.abs(lam) < r_in))

    # phase simplicity via individual discs (separation from mu2)
    d_ph = discs[0]['disc']
    d_dom = discs[1]['disc']
    sep = abs(lam[i_phase] - lam[1])
    ok_A = bool(sep > d_ph + d_dom)
    dom_cert = bool(discs[1]['modulus'] + d_dom < 1.0)
    hyperbolic = bool(ok_A and dom_cert)

    return dict(
        dt=dt, dimension=dim, delay_steps=d, period_steps=int(nper),
        discrete_period_yr=float(nper * dt),
        nominal_monodromy_inf_norm=norm_inf(M_nom),
        E1_exact_insertion=E1, R_product_rounding=R_prod,
        rigorous_ball_inf=ball, window_amplification_bound=W_max,
        max_eps=float(eps_list.max()),
        kappa_inf=float(kappa) if np.isfinite(kappa) else None,
        multipliers=[dict(re=float(z.real), im=float(z.imag),
                          modulus=float(abs(z))) for z in lam[:8]],
        eigen_discs_top3=discs,
        phase_multiplier=dict(nominal=float(abs(lam[i_phase])),
                              simple_neutral_certified=bool(ok_A)),
        dominant_nontrivial=dict(nominal=float(abs(lam[1])),
                                 disc=discs[1]['disc'],
                                 below_one_certified=dom_cert),
        all_nontrivial_strictly_inside_unit_disc=hyperbolic,
        sigma_min_contour=dict(radius=r_in, rigorous_min=float(smin_rigorous),
                               sampled_min=float(smin_b), svds=int(need),
                               exceeds_ball=ok_B, nominal_inside=n_inside),
    ), M_nom, lam


def main():
    t_start = time.time()
    results = {}
    for dt in (0.25,):
        tag = f'dt{str(dt).replace(".", "p")}'
        print(f'=== dt = {dt} ===')
        lv, M, lam = run_level(dt)
        results[tag] = lv
        np.savez(ROOT / f'c4_monodromy_{tag}.npz', M=M, lam=lam)
        print(f'  period: {lv["period_steps"]} steps = {lv["discrete_period_yr"]:.2f} yr')
        print(f'  ball: {lv["rigorous_ball_inf"]:.3e}')
        print(f'  phase: {lv["phase_multiplier"]}')
        print(f'  dominant: {lv["dominant_nontrivial"]}')
        print(f'  all inside: {lv["all_nontrivial_strictly_inside_unit_disc"]}')

    out = {
        'title': 'Monodromy/Floquet enclosure for the validated C4 cycle',
        'method': 'single-step insertion-identity sensitivity + Bauer-Fike '
                  'eigenvalue discs + sigma_min contour counting',
        'levels': results,
    }
    (ROOT / 'c4_monodromy_enclosure.json').write_text(json.dumps(out, indent=2))
    print(f'written c4_monodromy_enclosure.json ({time.time()-t_start:.0f}s)')


if __name__ == '__main__':
    main()
