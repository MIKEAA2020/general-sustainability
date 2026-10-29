#!/usr/bin/env python3
"""Gated inner three-state DDE (N, Z, E) — Candidate A (A018/A025).

Model (frozen-A inner core, "gated" = effort-saturation-corrected):
    N' = rN(1-N/K) - qEN
    Z' = (mem(N,E) - Z) / tau_m
    E' = (1-E/Emax) * (eta E (Z(t-tau)/Dref - E/Emax)
                       + delta0 Z(t-tau)/(Zref + Z(t-tau)))
    mem(N,E) = softplus(qEN - S(N); k),  S(N) = rN(1-N/K),
    softplus(x; k) = log(1 + exp(k x))/k.
Since delta = ln2/k for k=10, the -ln2/k + delta shift cancels identically.

The characteristic function at the interior equilibrium:
    P(lam) - C_Z L(lam) e^{-lam tau} = 0
    P(lam) = (lam - A_N)(lam + d)(lam - C_E),  d = 1/tau_m,
    L(lam) = B_E(lam - A_N) + A_E B_N.
"""
from __future__ import annotations

import numpy as np

PAR = dict(
    r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0,
    delta0=0.01, Dref=1.0, taum=5.0, k=10.0,
    delta=np.log(2.0) / 10.0, Zref=1.0,
)
LN2 = np.log(2.0)


def softplus(x, kk=PAR['k']):
    z = kk * x
    if z > 40:
        return x
    if z < -40:
        return np.exp(z) / kk
    return np.log1p(np.exp(z)) / kk


def S_of_N(N, p=PAR):
    return p['r'] * N * (1.0 - N / p['K'])


def mem_of(N, E, p=PAR):
    deficit = p['q'] * E * N - S_of_N(N, p)
    return max(0.0, softplus(deficit, p['k']))


def rhs(state, zdel, p=PAR):
    N, Z, E = state
    Sn = p['r'] * N * (1.0 - N / p['K'])
    mem = mem_of(N, E, p)
    dN = Sn - p['q'] * E * N
    dZ = (mem - Z) / p['taum']
    gate = 1.0 - E / p['Emax']
    dE = gate * (p['eta'] * E * (zdel / p['Dref'] - E / p['Emax'])
                 + p['delta0'] * zdel / (p['Zref'] + zdel))
    return np.array([dN, dZ, dE])


def rhs_jac(state, zdel, p=PAR):
    N, Z, E = state
    r, K, q, k = p['r'], p['K'], p['q'], p['k']
    dS_dN = r * (1.0 - 2.0 * N / K)
    deficit = q * E * N - r * N * (1.0 - N / K)
    sig = 1.0 / (1.0 + np.exp(-np.clip(k * deficit, -700, 700)))
    dmem_dN = sig * (q * E - dS_dN)
    dmem_dE = sig * q * N
    gate = 1.0 - E / p['Emax']
    dE_dE = (-1.0 / p['Emax']) * (p['eta'] * E * (zdel / p['Dref'] - E / p['Emax'])
                                  + p['delta0'] * zdel / (p['Zref'] + zdel)) \
            + gate * p['eta'] * (zdel / p['Dref'] - 2.0 * E / p['Emax'])
    dE_dz = gate * (p['eta'] * E / p['Dref']
                    + p['delta0'] * p['Zref'] / (p['Zref'] + zdel) ** 2)
    J = np.zeros((3, 3))
    J[0, 0] = dS_dN - q * E
    J[0, 2] = -q * N
    J[1, 0] = dmem_dN / p['taum']
    J[1, 1] = -1.0 / p['taum']
    J[1, 2] = dmem_dE / p['taum']
    J[2, 2] = dE_dE
    D = np.array([0.0, 0.0, dE_dz])
    return J, D


def equilibrium(p=PAR):
    d = p['delta']
    a = p['Emax'] * d / p['Dref']
    b = p['Emax'] * p['delta0'] * d / (p['eta'] * (p['Zref'] + d))
    E = 0.5 * (a + np.sqrt(a * a + 4.0 * b))
    N = p['K'] * (1.0 - p['q'] * E / p['r'])
    return np.array([N, d, E])


def lin_coeffs(p=PAR):
    N, Z, E = equilibrium(p)
    r, K, q = p['r'], p['K'], p['q']
    A_N = r * (1.0 - 2.0 * N / K) - q * E
    A_E = -q * N
    dS_dN = r * (1.0 - 2.0 * N / K)
    B_N = (q * E - dS_dN) / (2.0 * p['taum'])
    B_E = q * N / (2.0 * p['taum'])
    zdel = Z
    gate = 1.0 - E / p['Emax']
    C_Z = gate * (p['eta'] * E / p['Dref']
                  + p['delta0'] * p['Zref'] / (p['Zref'] + zdel) ** 2)
    C_E = gate * p['eta'] * (zdel / p['Dref'] - 2.0 * E / p['Emax'])
    return dict(A_N=A_N, A_E=A_E, B_N=B_N, B_E=B_E, C_Z=C_Z, C_E=C_E,
                d=1.0 / p['taum'])


def hopf_cubic_coeffs(p=PAR):
    c = lin_coeffs(p)
    AN2, d2, CE2 = c['A_N'] ** 2, c['d'] ** 2, c['C_E'] ** 2
    BE2 = c['B_E'] ** 2
    cross = (c['A_E'] * c['B_N'] - c['A_N'] * c['B_E']) ** 2
    CZ2 = c['C_Z'] ** 2
    c2 = AN2 + d2 + CE2
    c1 = AN2 * d2 + AN2 * CE2 + d2 * CE2 - CZ2 * BE2
    c0 = AN2 * d2 * CE2 - CZ2 * cross
    return dict(c0=c0, c1=c1, c2=c2, cross_term=cross, **c)


def characteristic(lam, tau, p=PAR):
    c = lin_coeffs(p)
    P = (lam - c['A_N']) * (lam + c['d']) * (lam - c['C_E'])
    L = c['B_E'] * (lam - c['A_N']) + c['A_E'] * c['B_N']
    return P - c['C_Z'] * L * np.exp(-lam * tau)


def tau_of_omega(omega, branch_k=0, p=PAR):
    c = lin_coeffs(p)
    i = 1j
    P = (i * omega - c['A_N']) * (i * omega + c['d']) * (i * omega - c['C_E'])
    L = c['B_E'] * (i * omega - c['A_N']) + c['A_E'] * c['B_N']
    arg = np.angle(P / (c['C_Z'] * L))
    return (-arg + 2.0 * np.pi * branch_k) / omega
