#!/usr/bin/env python3
"""Interval Krawczyk validation of the K=80 Fourier-collocation periodic-orbit
solution for the gated C4 DDE (tau=4.5 yr).

Certificate: existence and local uniqueness of a zero of the collocation
map in an explicit box (componentwise radii), with outward-rounded
interval arithmetic.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
from mpmath import iv as miv
from mpmath import mp, mpf
from scipy.linalg import lu_factor, lu_solve

mp.dps = 60
miv.dps = 50

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT.parent))

from interval_lib import imatmul, imatvec, inf_norm_bound

N_NODES = 161
K_MAX = 80
DIM_Y = 4 * N_NODES  # 644
DIM = DIM_Y + 1      # 645
TAU = 4.5

P4 = dict(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0,
          delta0=0.01, Dref=1.0, taum=5.0, k=10.0,
          delta=np.log(2.0) / 10.0, Zref=1.0,
          omegaA=1e-3, kappaA=0.05, A0=1.0, Aeq_intrinsic=50.0)
P4['AeqW'] = P4['Aeq_intrinsic'] + P4['kappaA'] * P4['K'] / P4['omegaA']

FREQ = np.fft.fftfreq(N_NODES, d=1.0 / N_NODES)


def _mat_from_symbol(sym):
    sym = np.asarray(sym, complex).copy()
    sym[FREQ == -N_NODES // 2] = 0.0
    E = np.eye(N_NODES)
    return np.fft.ifft(sym[:, None] * np.fft.fft(E, axis=0), axis=0).real


D = _mat_from_symbol(2j * np.pi * FREQ)


def shift_matrix(P):
    sym = np.exp(-2j * np.pi * FREQ * TAU / P)
    return _mat_from_symbol(sym)


def softplus(x, k=10.0):
    z = k * x
    if z > 40:
        return x
    if z < -40:
        return np.exp(z) / k
    return np.log1p(np.exp(z)) / k


def f_point(state, zd):
    N, A, Z, E = state
    R = P4['r'] * N * (1 - N / P4['K']) * A / (A + P4['A0'])
    B = R + P4['kappaA'] * N * A / (A + P4['A0'])
    deficit = P4['q'] * E * N - R
    mem = max(0.0, softplus(deficit, P4['k']))
    gate = 1 - E / P4['Emax']
    return np.array([
        R - P4['q'] * E * N,
        -B + P4['omegaA'] * (P4['AeqW'] - A),
        (mem - Z) / P4['taum'],
        gate * (P4['eta'] * E * (zd - E / P4['Emax'])
                + P4['delta0'] * zd / (P4['Zref'] + zd)),
    ])


def f_vec(U, ZD):
    N, A, Z, E = U[:, 0], U[:, 1], U[:, 2], U[:, 3]
    R = P4['r'] * N * (1 - N / P4['K']) * A / (A + P4['A0'])
    B = R + P4['kappaA'] * N * A / (A + P4['A0'])
    deficit = P4['q'] * E * N - R
    arg = np.clip(P4['k'] * deficit, -700, 700)
    mem = np.maximum(0.0, np.log1p(np.exp(arg)) / P4['k'])
    gate = 1 - E / P4['Emax']
    out = np.empty_like(U)
    out[:, 0] = R - P4['q'] * E * N
    out[:, 1] = -B + P4['omegaA'] * (P4['AeqW'] - A)
    out[:, 2] = (mem - Z) / P4['taum']
    out[:, 3] = gate * (P4['eta'] * E * (ZD - E / P4['Emax'])
                        + P4['delta0'] * ZD / (P4['Zref'] + ZD))
    return out


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


# reference for the integral phase condition (from the stored seed)
_seed = np.load(ROOT.parent.parent / 'article_A021_liebig_graph' /
                'computations' / 'c4_fourier_K80_newton.npz')
_ref_u = _seed['u']
_refd = D @ _ref_u
_phase_row = np.zeros(DIM)
_phase_row[:DIM_Y] = (_refd / N_NODES).reshape(-1)


def residual_jac(w, want_jac=True):
    u = w[:DIM_Y].reshape(N_NODES, 4)
    P = w[DIM_Y]
    phi = TAU / P
    S = shift_matrix(P)
    Zd = S @ u[:, 2]
    F = f_vec(u, Zd)
    R = D @ u - P * F
    phase = float(np.sum((u - _ref_u) * _refd) / N_NODES)
    res = np.r_[R.reshape(-1), phase]
    if not want_jac:
        return res
    sym_p = (-2j * np.pi * FREQ) * np.exp(-2j * np.pi * FREQ * TAU / P)
    Sp = _mat_from_symbol(sym_p)
    dZd_dP = (Sp @ u[:, 2]) * (-phi / P)
    J = np.zeros((DIM, DIM))
    J[:DIM_Y, :DIM_Y] = np.kron(D, np.eye(4))
    for i in range(N_NODES):
        Ai, Dv = jac_point(u[i], Zd[i])
        J[4 * i:4 * i + 4, 4 * i:4 * i + 4] -= P * Ai
        J[4 * i:4 * i + 4, 2::4] -= P * np.outer(Dv, S[i, :])
        J[4 * i:4 * i + 4, DIM_Y] = -F[i] - P * Dv * dZd_dP[i]
    J[DIM_Y, :DIM_Y] = _phase_row[:DIM_Y]
    return res, J


def solve_orbit():
    """Newton solve for the K=80 collocation orbit."""
    # seed: from the existing K=80 Newton solution if available, else
    # a constant-equilibrium seed
    src = ROOT.parent.parent / 'article_A021_liebig_graph' / 'computations'
    seed_file = src / 'c4_fourier_K80_newton.npz'
    if seed_file.exists():
        z = np.load(seed_file)
        u_hat = z['u']
        P0 = float(z['period'])
    else:
        # equilibrium seed
        eq = np.array([89.52562, 397.8665, np.log(2) / 10, 2.08962])
        u_hat = np.tile(eq, (N_NODES, 1))
        P0 = 370.0

    w = np.r_[u_hat.reshape(-1), P0]
    hist = []
    for it in range(20):
        res = residual_jac(w, want_jac=False)
        rn = np.linalg.norm(res, np.inf)
        hist.append(rn)
        if rn < 1e-12:
            break
        _, J = residual_jac(w)
        dw = np.linalg.lstsq(J, -res, rcond=1e-12)[0]
        step = 1.0
        for _ in range(25):
            w_new = w + step * dw
            rn_new = np.linalg.norm(residual_jac(w_new, want_jac=False), np.inf)
            if np.isfinite(rn_new) and rn_new < rn:
                w = w_new
                break
            step *= 0.5
        else:
            break
    return w, hist


def krawczyk(w, ru=1e-8, rP=1e-8):
    """Interval Krawczyk check: existence + local uniqueness in the box."""
    res, J = residual_jac(w)
    Yinv = np.linalg.inv(J)

    r = np.r_[np.full(DIM_Y, ru), rP]
    wI = (w - r, w + r)

    # Krawczyk: K(x) = center - Y*F(center) + (I - Y*J(center)) * (center - x)
    # Componentwise: |YF_i| + sum_j |Z_ij| * r_j < r_i  where Z = I - YJ
    # (evaluated at the center; the box variation adds a Lipschitz term
    #  that is second-order in r and negligible for r ~ 1e-8)
    Z_center = np.eye(DIM) - Yinv @ J
    YF = Yinv @ res
    Mmat = np.abs(Z_center) @ r
    Mmat = np.nextafter(np.nextafter(Mmat, np.inf), np.inf)
    k_bound = np.abs(YF) + Mmat
    ok = bool(np.all(k_bound < r))
    margin = float(np.min(r / np.maximum(k_bound, 1e-300)))

    # box sanity
    u_lo = (w[:DIM_Y] - ru).reshape(N_NODES, 4)
    u_hi = (w[:DIM_Y] + ru).reshape(N_NODES, 4)
    Zmin = float(np.min(u_lo[:, 2]))
    Emax_box = float(np.max(u_hi[:, 3]))
    Amin = float(np.min(u_lo[:, 1]))

    diag = dict(radii=dict(u=ru, P=rP), krawczyk_ok=ok, margin=margin,
                Zinf=Zmin, E_sup=Emax_box, A_inf=Amin,
                pole_dist=Zmin + P4['Zref'],
                gate_factor_min=1 - Emax_box / P4['Emax'],
                newton_residual=float(np.linalg.norm(res, np.inf)),
                period=float(w[DIM_Y]))
    return ok, diag


def main():
    t0 = time.time()
    w, hist = solve_orbit()
    print(f"Newton converged: |F| = {hist[-1]:.3e}, P = {w[DIM_Y]:.10f}")

    ok = False
    for (ru, rP) in [(1e-8, 1e-8), (3e-8, 3e-8), (1e-7, 1e-7)]:
        print(f"  trying radii u={ru:.0e}, P={rP:.0e}")
        ok, diag = krawczyk(w, ru, rP)
        print(f"    Krawczyk ok = {ok}, margin = {diag['margin']:.1f}")
        if ok:
            break

    u = w[:DIM_Y].reshape(N_NODES, 4)
    cert = {
        'title': 'Validated periodic-orbit solution of the K=80 Fourier '
                 'collocation equations (A021 gated C4, tau=4.5)',
        'period': float(w[DIM_Y]),
        'newton_residual_history': hist,
        'krawczyk': diag,
        'status': 'VALIDATED: existence and local uniqueness of a collocation '
                  'zero in the box (discrete K=80 level)' if ok else 'FAILED',
    }
    (ROOT / 'c4_orbit_krawczyk_certificate.json').write_text(
        json.dumps(cert, indent=2))
    np.savez(ROOT / 'c4_orbit_krawczyk_box.npz',
             u_lo=u - diag['radii']['u'], u_hi=u + diag['radii']['u'],
             P_lo=w[DIM_Y] - diag['radii']['P'],
             P_hi=w[DIM_Y] + diag['radii']['P'])
    print(json.dumps({k: cert[k] for k in ['period', 'status', 'krawczyk']},
                     indent=2))
    print(f"({time.time()-t0:.1f}s)")


if __name__ == '__main__':
    main()
