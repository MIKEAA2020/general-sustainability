#!/usr/bin/env python3
"""Outward-rounded interval Hopf certification for the gated inner three-state DDE.

Closes the A025 reproducibility obligation: independently reproduces the
documented Hopf delay enclosures with outward-rounded interval arithmetic.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import iv as miv
from mpmath import mp, mpf

mp.dps = 60
miv.dps = 50

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from a025_model import PAR, equilibrium, lin_coeffs, hopf_cubic_coeffs


def params_iv():
    p = {}
    for kk in ['r', 'K', 'q', 'eta', 'Emax', 'delta0', 'Dref', 'taum', 'k']:
        p[kk] = miv.mpf(str(PAR[kk]))
    p['delta'] = miv.log(miv.mpf(2)) / miv.mpf(10)
    p['Zref'] = miv.mpf(1)
    return p


def equilibrium_iv(p):
    d = p['delta']
    a = p['Emax'] * d / p['Dref']
    b = p['Emax'] * p['delta0'] * d / (p['eta'] * (p['Zref'] + d))
    E = (a + miv.sqrt(a * a + 4 * b)) / 2
    N = p['K'] * (1 - p['q'] * E / p['r'])
    return N, d, E


def lin_coeffs_iv(p, eq):
    N, Z, E = eq
    r, K, q, taum = p['r'], p['K'], p['q'], p['taum']
    half = miv.mpf(1) / 2
    A_N = r * (1 - 2 * N / K) - q * E
    A_E = -q * N
    dS_dN = r * (1 - 2 * N / K)
    B_N = (q * E - dS_dN) * half / taum
    B_E = q * N * half / taum
    gate = 1 - E / p['Emax']
    C_Z = gate * (p['eta'] * E / p['Dref']
                  + p['delta0'] * p['Zref'] / (p['Zref'] + Z) ** 2)
    C_E = gate * p['eta'] * (Z / p['Dref'] - 2 * E / p['Emax'])
    return dict(A_N=A_N, A_E=A_E, B_N=B_N, B_E=B_E, C_Z=C_Z, C_E=C_E,
                d=1 / taum)


def hopf_H(c, x):
    AN2 = c['A_N'] ** 2
    d2 = c['d'] ** 2
    CE2 = c['C_E'] ** 2
    BE2 = c['B_E'] ** 2
    cross = (c['A_E'] * c['B_N'] - c['A_N'] * c['B_E']) ** 2
    return (x + AN2) * (x + d2) * (x + CE2) - c['C_Z'] ** 2 * (BE2 * x + cross)


def hopf_Hp(c, x):
    AN2 = c['A_N'] ** 2
    d2 = c['d'] ** 2
    CE2 = c['C_E'] ** 2
    a, b, g = AN2, d2, CE2
    return 3 * x ** 2 + 2 * (a + b + g) * x + (a * b + a * g + b * g) \
        - c['C_Z'] ** 2 * c['B_E'] ** 2


def iv_intersect(X, Y):
    a = max(X.a, Y.a)
    b = min(X.b, Y.b)
    if a > b:
        return None
    return miv.mpf([a, b])


def interval_newton(c, X, iters=80):
    for _ in range(iters):
        fX = hopf_H(c, X)
        if fX > 0 or fX < 0:
            return None
        m = (X.a + X.b) / 2
        fm = hopf_H(c, miv.mpf([m, m]))
        fpX = hopf_Hp(c, X)
        if fpX.a * fpX.b > 0:
            N = miv.mpf([m, m]) - fm / fpX
            Xn = iv_intersect(X, N)
            if Xn is None:
                return None
            if Xn.a == X.a and Xn.b == X.b:
                return Xn
            X = Xn
        else:
            mid = (X.a + X.b) / 2
            flo = hopf_H(c, miv.mpf([X.a, X.a]))
            fmid = hopf_H(c, miv.mpf([mid, mid]))
            if (flo <= 0 and fmid.b >= 0) or (flo.b >= 0 and fmid.a <= 0):
                X = miv.mpf([X.a, mid])
            else:
                X = miv.mpf([mid, X.b])
    return X


def tau_interval(c, omega, branch_k):
    i = miv.mpc(0, 1)
    iw = i * omega
    P = (iw - c['A_N']) * (iw + c['d']) * (iw - c['C_E'])
    L = c['B_E'] * (iw - c['A_N']) + c['A_E'] * c['B_N']
    ratio = P / (c['C_Z'] * L)
    arg = miv.atan2(miv.im(ratio), miv.re(ratio))
    return (-arg + 2 * miv.pi * branch_k) / omega


def transversality(c, omega, tau_iv):
    i = miv.mpc(0, 1)
    lam = i * omega
    P = (lam - c['A_N']) * (lam + c['d']) * (lam - c['C_E'])
    dP = (lam + c['d']) * (lam - c['C_E']) + (lam - c['A_N']) * (lam - c['C_E']) \
        + (lam - c['A_N']) * (lam + c['d'])
    L = c['B_E'] * (lam - c['A_N']) + c['A_E'] * c['B_N']
    dL = c['B_E']
    denom = dP - (dL / L) * P + tau_iv * P
    dlam = -lam * P / denom
    return miv.re(dlam)


def fmt(x, digits=13):
    a, b = x.a, x.b
    sa = mp.nstr(a, digits + 2, strip_zeros=False)
    sb = mp.nstr(b, digits + 2, strip_zeros=False)
    return f'[{sa}, {sb}]'


def main():
    p = params_iv()
    eq = equilibrium_iv(p)
    c = lin_coeffs_iv(p, eq)

    cross = (c['A_E'] * c['B_N'] - c['A_N'] * c['B_E']) ** 2
    assert cross.b < mpf('1e-30')

    import numpy as np
    sys.path.insert(0, str(ROOT))
    from a025_model import hopf_cubic_coeffs as _hcc
    hcf = _hcc()
    roots = np.roots([1.0, hcf['c2'], hcf['c1'], hcf['c0']])
    pos = sorted(x.real for x in roots if abs(x.imag) < 1e-9 and x.real > 0)

    cert = []
    for xr in pos:
        X0 = miv.mpf([mpf(xr) * (1 - mpf('1e-9')), mpf(xr) * (1 + mpf('1e-9'))])
        X = interval_newton(c, X0)
        if X is None:
            raise RuntimeError(f'interval Newton failed at seed {xr}')
        omega = miv.sqrt(X)
        HpX = hopf_Hp(c, X)
        simple = (HpX.a > 0) or (HpX.b < 0)
        entry = {'x_interval': fmt(X), 'omega_interval': fmt(omega),
                 'simple_root': bool(simple)}
        for kk in (0, 1):
            tau_iv = tau_interval(c, omega, kk)
            if tau_iv.a > 0:
                dl = transversality(c, omega, tau_iv)
                entry[f'tau_k{kk}'] = fmt(tau_iv)
                entry[f'dRe_dtau_k{kk}'] = fmt(dl)
                entry[f'crossing_direction_k{kk}'] = \
                    'right (destabilising)' if dl.a > 0 else \
                    ('left (stabilising)' if dl.b < 0 else 'INCONCLUSIVE')
            else:
                entry[f'tau_k{kk}'] = None
        cert.append(entry)

    out = {
        'model': 'gated inner three-state DDE (N,Z,E), Candidate A',
        'arithmetic': f'mpmath interval arithmetic, dps={miv.dps}',
        'hopf_certificates': cert,
    }
    (ROOT / 'a025_interval_hopf.json').write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
