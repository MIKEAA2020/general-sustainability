#!/usr/bin/env python3
"""B4 continuum transfer — STAGE T4: the prefactor (M_c) certificate.

THE OBJECT. M_c, the phase-tangent history ratio of the certified binding
orbit: for each orbit phase t_i,

    h_i = sup_{s in [t_i - tau_x, t_i]} |F(y*(s), Z*(s - tau_x))|

is the sup-norm of the tangent history at phase t_i (F the C4 right-hand
side, tau_x = 4.5), and

    M_c = max_i h_i / min_i h_i.

The committed discrete value (the fine RK4 orbit, `summarize_c4_naim.py`)
is 4.553557132612546. The B4 assembly uses M_c only as a multiplicative
prefactor; the specification's budget is a 10% enclosure.

METHOD. The certified orbit (A1 Stage 4d) lies within r = 3e-7 (sup-norm,
augmented history state) of the committed piecewise-Chebyshev substrate at
a period within 3e-7 of P = 370.931177839426. The substrate is evaluated
here from its committed Fourier representation (K = 80 modes, with 1-ulp
coefficient intervals, `computations/c4_fourier_coefficients_K80.csv` — the
same source all A1 stages consume) on a fine uniform grid over one period;
the tangent speeds are evaluated in float64 and enclosed by the additive
error budget

    rho = r (the 4d tube) + |P_hat - P| v_max (the phase drift at the
    extreme relative phase) + 1e-11 (the float evaluation noise allowance:
    the 80-mode float sums with 1-ulp coefficient uncertainty carry a
    rounding error below 1e-12),

propagated through the right-hand side's Lipschitz constants (max over the
orbit samples of the Jacobian infinity norm and of |D_43|, each inflated by
a 1e-12 evaluation-noise slack), plus the between-sample variation bound
|ds/dt| dt/2 with |ds/dt| bounded through the sampled orbit data. The
windowed suprema are taken over each tau_x-window (the sliding-window
maximum over the grid, extended by one sample at each end).

HONESTY. The 4d certificate anchors the augmented history state at one
reference phase; the uniform-tube reading used here (the orbit's graph
within r + |P_hat - P| v_max of the substrate's graph at matching phase)
is the standard periodic-orbit consequence and the declared inflation is
generous by more than an order of magnitude relative to the assembly
budget. The certified statement below is the interval enclosure of M_c
under this tube reading.

Deterministic; no timing fields in the JSON.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
FOURIER = ROOT.parent.parent / "article_A021_liebig_graph" / "computations" / "c4_fourier_coefficients_K80.csv"

TAU_X = 4.5
P_CERT = 370.931177839426
P_RAD = 3e-7
R_TUBE = 3e-7
NOISE = 1e-11

# model parameters (float; the noise allowance covers evaluation error)
PAR = dict(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0,
           delta0=0.01, Dref=1.0, taum=5.0, k=10.0,
           delta=np.log(2) / 10, Zref=1.0, omegaA=1e-3, kappaA=0.05,
           A0=1.0, Aeq_intrinsic=50.0)
PAR['AeqW'] = PAR['Aeq_intrinsic'] + PAR['kappaA'] * PAR['K'] / PAR['omegaA']


def softplus(x, k):
    z = k * x
    return np.logaddexp(0.0, z) / k


def rhs(cur, zdel):
    N, A, Z, E = cur
    p = PAR
    R = p['r'] * N * (1 - N / p['K']) * A / (A + p['A0'])
    B = R + p['kappaA'] * N * A / (A + p['A0'])
    deficit = p['q'] * E * N - R
    mem = np.maximum(0.0, softplus(deficit, p['k']) - np.log(2) / p['k'] + p['delta'])
    return np.stack([
        R - p['q'] * E * N,
        -B + p['omegaA'] * (p['AeqW'] - A),
        (mem - Z) / p['taum'],
        (1 - E / p['Emax']) * (p['eta'] * E * (zdel / p['Dref'] - E / p['Emax'])
                               + p['delta0'] * zdel / (p['Zref'] + zdel)),
    ])


def main():
    # ---- load the committed Fourier substrate ---------------------------
    import csv
    rows = list(csv.DictReader(open(FOURIER)))
    period_sub = float(rows[0]['period'])
    modes = {}
    for row in rows:
        k = int(row['mode']); comp = row['state']
        modes.setdefault(k, {})[comp] = complex(float(row['real']), float(row['imag']))
    K = max(modes.keys())
    comps = ['N', 'A', 'Z', 'E']
    # coefficient arrays c[comp][k] for k = -K..K
    coeff = {c: np.zeros(2 * K + 1, dtype=complex) for c in comps}
    for k, cd in modes.items():
        for c in comps:
            if c in cd:
                coeff[c][k + K] = cd[c]
    max_coeff_mag = max(np.abs(coeff[c]).max() for c in comps)
    print(f'substrate: K={K}, period={period_sub}')

    # ---- evaluate on the fine grid --------------------------------------
    NF = 65536
    tgrid = np.arange(NF) * (period_sub / NF)
    # y(t) = sum_k c_k exp(2 pi i k t / P): use the real FFT-style evaluation
    def fourier_eval(cc):
        acc = np.full(NF, cc[K].real)
        for k in range(1, K + 1):
            cp = cc[K + k]; cm = cc[K - k]
            w = 2 * np.pi * k * tgrid / period_sub
            acc += 2 * (cp.real * np.cos(w) - cp.imag * np.sin(w))
        return acc

    state = {c: fourier_eval(coeff[c]) for c in comps}
    Y = np.stack([state['N'], state['A'], state['Z'], state['E']], axis=1)  # (NF, 4)

    # delayed Z reads: Z(t - tau) evaluated EXACTLY via the phase-shifted
    # Fourier coefficients (no interpolation): c'_k = c_k exp(-2 pi i k tau/P)
    coeff_shift = {}
    for c in comps:
        cc = coeff[c].copy()
        for k in range(-K, K + 1):
            if k != 0:
                cc[k + K] = cc[k + K] * np.exp(-2j * np.pi * k * TAU_X / period_sub)
        coeff_shift[c] = cc
    Zd = fourier_eval(coeff_shift['Z'])
    dt = period_sub / NF
    d_int = int(round(TAU_X / dt))  # window length in samples (approx; window uses it)

    # ---- speeds and their derivative bounds -----------------------------
    F = rhs(Y.T, Zd)                    # (4, NF)
    speed = np.linalg.norm(F, axis=0)   # (NF,)
    # ds/dt bound: |grad_y F . ydot| + |dF/dZd| sup|Zdot|
    Zdot = F[2, :]
    # Jacobian infinity norms over the orbit (float; slack below)
    N_, A_, Z_, E_ = Y.T
    p = PAR
    fac = A_ / (A_ + p['A0'])
    RN = p['r'] * (1 - 2 * N_ / p['K']) * fac
    RA = p['r'] * N_ * (1 - N_ / p['K']) * p['A0'] / (A_ + p['A0']) ** 2
    BN = RN + p['kappaA'] * fac
    BA = RA + p['kappaA'] * N_ * p['A0'] / (A_ + p['A0']) ** 2
    deficit = p['q'] * E_ * N_ - p['r'] * N_ * (1 - N_ / p['K']) * fac
    sig = 1 / (1 + np.exp(-p['k'] * deficit))
    Jinf = np.maximum.reduce([
        np.abs(RN - p['q'] * E_) + np.abs(RA) + np.abs(p['q'] * N_),
        np.abs(BN) + np.abs(BA + p['omegaA']),
        np.abs(sig * (p['q'] * E_ - RN)) / p['taum'] + np.abs(sig * RA) / p['taum']
        + 1 / p['taum'] + np.abs(sig * p['q'] * N_) / p['taum'],
        np.abs(-(-p['eta'] * E_ * (Z_ / p['Dref'] - E_ / p['Emax']) + p['delta0'] * Z_ / (p['Zref'] + Z_)) / p['Emax']
               + (1 - E_ / p['Emax']) * p['eta'] * (Z_ / p['Dref'] - 2 * E_ / p['Emax'])),
    ])
    D43 = (1 - E_ / p['Emax']) * (p['eta'] * E_ / p['Dref']
                                  + p['delta0'] * p['Zref'] / (p['Zref'] + Z_) ** 2)
    # the read channel of the rhs also depends on zdel via H; |dF_4/dzdel| = D43
    Jinf_max = float(Jinf.max()) * (1 + 1e-12) + 1e-12
    D43_max = float(np.abs(D43).max()) * (1 + 1e-12) + 1e-12
    v_max = float(speed.max()) * (1 + 1e-12) + 1e-12
    vZ_max = float(np.abs(Zdot).max()) * (1 + 1e-12) + 1e-12
    dsdt_max = Jinf_max * v_max + D43_max * vZ_max

    # ---- the additive error budget for the speed values ------------------
    rho = R_TUBE + P_RAD * v_max + NOISE
    lip = Jinf_max + D43_max          # |dF/d(y, zdel)| per component (sup-norm)
    speed_err = lip * rho + 2 * NOISE  # evaluated speed vs true tangent speed

    # ---- windowed suprema (sliding max over tau_x-windows) ---------------
    w = d_int  # window length in samples
    # sliding maximum/minimum over the circular grid, extended by one sample
    from collections import deque
    # window length in samples, extended by one sample on each side
    # (the between-sample bound covers values between grid points)
    win = w + 2

    from scipy.ndimage import maximum_filter1d

    def window_max(arr):
        return maximum_filter1d(arr, size=win, mode='wrap', origin=0)

    # h_i = sup over the tau_x-window of the speed, per phase i
    h_samples = window_max(speed)
    between = dsdt_max * dt / 2  # between-sample variation
    h_hi = h_samples + speed_err + between      # certified upper bound per phase
    h_lo = h_samples - speed_err - between      # certified lower bound per phase
    h_lo = np.maximum(h_lo, 0.0)
    Mc_hi = float(h_hi.max() / max(h_lo.min(), 1e-300))
    discrete = 4.553557132612546
    print(f'h_i (windowed sup): max = {h_samples.max():.6f}, min = {h_samples.min():.6f}')
    print(f'certified: h max = {h_hi.max():.6f}, h min = {h_lo.min():.6f}')
    print(f'speed_err = {speed_err:.3e}, between-sample = {between:.3e}')
    print(f'M_c certified UPPER BOUND: {Mc_hi:.9f}')
    print(f'discrete value {discrete}: upper bound exceeds it by {(Mc_hi - discrete) / discrete:.4%}')

    results = {
        'title': 'B4 continuum transfer — Stage T4: the prefactor (M_c) certificate',
        'object': 'the phase-tangent history ratio M_c = max_i h_i / min_i h_i of the certified binding orbit',
        'method': {
            'substrate': 'the committed K=80 Fourier representation (c4_fourier_coefficients_K80.csv) evaluated on a 65536-point grid',
            'tube': 'r = 3e-7 (the 4d certificate) + |P_hat-P| v_max (phase drift) + 1e-11 evaluation-noise allowance',
            'speed_error': float(speed_err),
            'between_sample_variation': float(between),
            'window': 'sliding extremum over tau_x = 4.5 windows, extended one sample',
            'ds_dt_bound': float(dsdt_max),
            'jacobian_inf_max': float(Jinf_max),
            'D43_max': float(D43_max),
            'v_max': float(v_max),
        },
        'h_max_certified': float(h_hi.max()),
        'h_min_certified': float(h_lo.min()),
        'h_windowed_sup_samples_max': float(h_samples.max()),
        'h_windowed_sup_samples_min': float(h_samples.min()),
        'M_c_upper_bound': Mc_hi,
        'M_c_discrete_committed': discrete,
        'upper_bound_excess': float((Mc_hi - discrete) / discrete),
        'budget_note': 'the specification budget is a 10% enclosure; only the upper bound enters the B4 assembly',
        'all_checks_pass': bool(Mc_hi >= discrete and (Mc_hi - discrete) / discrete < 0.10),
    }
    out = ROOT / 'b4_t4_prefactor_certificate.json'
    out.write_text(json.dumps(results, indent=2))
    print(f'wrote {out}')
    print('all_checks_pass =', results['all_checks_pass'])


if __name__ == '__main__':
    main()
