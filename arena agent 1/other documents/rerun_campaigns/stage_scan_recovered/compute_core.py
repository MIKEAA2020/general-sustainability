#!/usr/bin/env python3
"""Independent recomputation of local Hopf data, Hassard l1, sample-and-hold
monodromy, and inner three-state orbit diagnostics for the gated / ungated cores.
"""
from __future__ import annotations

import json
import math
import os
from dataclasses import asdict, dataclass

import numpy as np
from numpy.linalg import eigvals, inv, norm, solve

OUT = "/home/user/figures"
os.makedirs(OUT, exist_ok=True)
RES = "/home/user/figures/results.json"


@dataclass
class P:
    r: float = 0.02
    K: float = 100.0
    q: float = 0.001
    eta: float = 0.914
    Emax: float = 30.0
    d0: float = 0.01
    Dref: float = 1.0
    Zref: float = 1.0
    taum: float = 5.0
    k: float = 10.0
    delta: float = math.log(2.0) / 10.0
    gated: bool = True
    name: str = "A_gated"


def equilibrium(p: P):
    Zs = p.delta
    # -(eta/Emax) E^2 + eta (Z/Dref) E + d0 Z/(Zref+Z) = 0
    a = -p.eta / p.Emax
    b = p.eta * (Zs / p.Dref)
    c = p.d0 * Zs / (p.Zref + Zs)
    disc = b * b - 4 * a * c
    Es = (-b + math.sqrt(disc)) / (2 * a) if abs(a) > 1e-18 else -c / b
    # quadratic a E^2 + b E + c = 0 with a<0, take the unique positive root
    roots = np.roots([a, b, c]).real
    pos = [float(x) for x in roots if np.isclose(x.imag if hasattr(x, "imag") else 0, 0) and x > 0]
    # np.roots on real coeffs
    rts = np.roots([a, b, c])
    pos = [float(np.real(x)) for x in rts if abs(np.imag(x)) < 1e-12 and np.real(x) > 0]
    Es = pos[0] if pos else float("nan")
    Ns = p.K * (1.0 - p.q * Es / p.r)
    return Ns, Zs, Es


def lin_coeff(p: P, Ns, Zs, Es):
    Sp = p.r * (1.0 - 2.0 * Ns / p.K)
    AN = p.r * (1.0 - 2.0 * Ns / p.K) - p.q * Es
    AE = -p.q * Ns
    BN = 0.5 / p.taum * (p.q * Es - Sp)
    BE = 0.5 / p.taum * p.q * Ns
    g = 1.0 - Es / p.Emax
    h = p.eta * Es * (Zs / p.Dref - Es / p.Emax) + p.d0 * Zs / (p.Zref + Zs)
    if p.gated:
        CE = p.eta * (Zs / p.Dref - 2.0 * Es / p.Emax) * g - h / p.Emax
        CZ = g * (p.eta * Es / p.Dref + p.d0 * p.Zref / (p.Zref + Zs) ** 2)
    else:
        CE = p.eta * (Zs / p.Dref - 2.0 * Es / p.Emax)
        CZ = p.eta * Es / p.Dref + p.d0 * p.Zref / (p.Zref + Zs) ** 2
    return dict(AN=AN, AE=AE, BN=BN, BE=BE, CE=CE, CZ=CZ, d=1.0 / p.taum)


def hopf_cubic(co):
    AN, AE, BN, BE, CE, CZ, d = (co[k] for k in ("AN", "AE", "BN", "BE", "CE", "CZ", "d"))
    # H(x)=(x+AN^2)(x+d^2)(x+CE^2) - CZ^2 [ BE^2 x + (AE BN - AN BE)^2 ]
    # expand as cubic in x
    const = (AE * BN - AN * BE) ** 2
    # use np.poly roots of H
    # H = (x+AN2)(x+d2)(x+CE2) - CZ2 BE2 x - CZ2 const
    a2, b2, c2 = AN**2, d**2, CE**2
    # (x+a2)(x+b2)(x+c2) = x^3 + (a2+b2+c2)x^2 + (a2b2+a2c2+b2c2)x + a2b2c2
    c3 = 1.0
    c2c = a2 + b2 + c2
    c1 = a2 * b2 + a2 * c2 + b2 * c2 - (CZ**2) * (BE**2)
    c0 = a2 * b2 * c2 - (CZ**2) * const
    rts = np.roots([c3, c2c, c1, c0])
    pos = sorted(float(np.real(z)) for z in rts if abs(np.imag(z)) < 1e-8 and np.real(z) > 1e-14)
    return pos, (c3, c2c, c1, c0)


def tau_from_omega(co, omega):
    AN, AE, BN, BE, CE, CZ, d = (co[k] for k in ("AN", "AE", "BN", "BE", "CE", "CZ", "d"))
    lam = 1j * omega
    P = (lam - AN) * (lam + d) * (lam - CE)
    L = BE * (lam - AN) + AE * BN
    # P = CZ L exp(-lam tau) => exp(-i omega tau) = P / (CZ L)
    ratio = P / (CZ * L)
    # tau = (-arg(P/(CZ L)) + 2 pi k) / omega
    ang = -np.angle(ratio)
    taus = []
    for k in range(-2, 8):
        t = (ang + 2 * np.pi * k) / omega
        if t > 1e-8:
            taus.append(float(t))
    return taus, complex(P), complex(L)


def A0_Atau(co):
    AN, AE, BN, BE, CE, CZ, d = (co[k] for k in ("AN", "AE", "BN", "BE", "CE", "CZ", "d"))
    A0 = np.array([[AN, 0.0, AE], [BN, -d, BE], [0.0, 0.0, CE]], dtype=complex)
    At = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, CZ, 0.0]], dtype=complex)
    return A0, At


def char_matrix(co, lam, tau):
    A0, At = A0_Atau(co)
    return lam * np.eye(3) - A0 - At * np.exp(-lam * tau)


def right_left_eigs(co, omega, tau):
    M = char_matrix(co, 1j * omega, tau)
    # right null
    u, s, vh = np.linalg.svd(M)
    p = vh[-1, :].conj()  # last right singular vector of M? vh is V^H, last row of vh is right sing vec for smallest
    # For M v = 0, v is right singular vector for sigma_min = last column of V = last row of vh, conjugated? 
    # svd: M = U S Vh, Vh[-1,:] is the last left-multiplier on v, i.e. conjugate-transpose row.
    # Standard: columns of V = rows of Vh conjugate-transposed. Smallest right sing vec = V[:,-1] = Vh[-1,:].conj()
    p = vh[-1, :].conj()
    # left null w* M = 0 => M^H w = 0, w = left sing vec = U[:,-1]
    q = u[:, -1]
    # check
    res_r = norm(M @ p)
    res_l = norm(q.conj() @ M)
    if res_r > 1e-8 or res_l > 1e-8:
        # fallback eigensolve of M
        w, V = np.linalg.eig(M)
        j = np.argmin(np.abs(w))
        p = V[:, j]
        wL, VL = np.linalg.eig(M.T.conj())
        jL = np.argmin(np.abs(wL))
        q = VL[:, jL]
    A0, At = A0_Atau(co)
    dDelta = np.eye(3) + tau * At * np.exp(-1j * omega * tau)
    nrm = q.conj() @ (dDelta @ p)
    q = q / nrm.conj()  # so q* dDelta p = 1
    # re-check
    nrm2 = q.conj() @ (dDelta @ p)
    p = p / np.sqrt(np.vdot(p, p))
    nrm3 = q.conj() @ (dDelta @ p)
    q = q / nrm3.conj()
    return p, q


# ---------- exact multilinear forms at equilibrium ----------
def phi_and_ders(p: P, N, E):
    """phi = q E N - S(N), S = r N (1-N/K)."""
    S = p.r * N * (1.0 - N / p.K)
    phi = p.q * E * N - S
    phi_N = p.q * E - p.r + 2.0 * p.r * N / p.K
    phi_E = p.q * N
    phi_NN = 2.0 * p.r / p.K
    phi_NE = p.q
    return phi, phi_N, phi_E, phi_NN, phi_NE


def softplus_ders(p: P, phi):
    # numerically stable
    kphi = p.k * phi
    if kphi > 40:
        sig = 1.0
    elif kphi < -40:
        sig = 0.0
    else:
        sig = 1.0 / (1.0 + math.exp(-kphi))
    sp = (phi if kphi > 40 else (math.log1p(math.exp(kphi)) / p.k if kphi > -40 else math.exp(kphi) / p.k))
    spp = p.k * sig * (1.0 - sig)
    sppp = (p.k ** 2) * sig * (1.0 - sig) * (1.0 - 2.0 * sig)
    return sp, sig, spp, sppp


def B_and_C(p: P, Ns, Zs, Es, u, v, w=None):
    """Bilinear B(u,v) and optional trilinear C(u,v,w) of the RFDE
    evaluated on (current, delayed) pairs.
    u,v,w are complex 3-vectors meaning the current state; delayed Z is
    supplied separately via factors e^{-i omega tau} baked into the caller
    by passing the history values as modified vectors.

    We treat the full jet in variables (N, Z, E, Zd).
    u is 4-vector (N,Z,E,Zd) etc.
    """
    # derivatives at eq
    _, phi_N, phi_E, phi_NN, phi_NE = phi_and_ders(p, Ns, Es)
    # at eq phi=0
    _, sig, spp, sppp = softplus_ders(p, 0.0)
    invtm = 1.0 / p.taum

    def hess_N(a, b):
        # only N,E current
        return (
            (-2.0 * p.r / p.K) * a[0] * b[0]
            - p.q * (a[0] * b[2] + a[2] * b[0])
        )

    def hess_Z(a, b):
        # Φ = softplus(phi); Zdot = invtm (Φ - Z)
        # D² Φ (a,b) = spp * Dphi(a) Dphi(b) + sig * D²phi(a,b)
        Dphi_a = phi_N * a[0] + phi_E * a[2]
        Dphi_b = phi_N * b[0] + phi_E * b[2]
        D2phi = phi_NN * a[0] * b[0] + phi_NE * (a[0] * b[2] + a[2] * b[0])
        return invtm * (spp * Dphi_a * Dphi_b + sig * D2phi)

    # effort: Edot = g(E) * h(E, Zd)
    # g = 1 - E/Emax
    # h = eta E (Zd/Dref - E/Emax) + d0 Zd/(Zref+Zd)
    Emax, eta, Dref, d0, Zref = p.Emax, p.eta, p.Dref, p.d0, p.Zref
    g = 1.0 - Es / Emax
    h = eta * Es * (Zs / Dref - Es / Emax) + d0 * Zs / (Zref + Zs)
    # first ders at eq
    hg_E = -1.0 / Emax
    # h_E = eta (Zd/Dref - E/Emax) + eta E (-1/Emax)
    h_E = eta * (Zs / Dref - Es / Emax) - eta * Es / Emax
    h_Zd = eta * Es / Dref + d0 * Zref / (Zref + Zs) ** 2
    # second ders
    h_EE = -2.0 * eta / Emax
    h_EZd = eta / Dref
    h_ZdZd = -2.0 * d0 * Zref / (Zref + Zs) ** 3
    g_EE = 0.0

    def hess_E(a, b):
        # D²(g h) = g D²h + Dg⊗Dh + Dh⊗Dg  (g linear so D²g=0)
        # a,b 4-vectors: indices 0=N,1=Z,2=E,3=Zd
        aE, bE, aZ, bZ = a[2], b[2], a[3], b[3]
        D2h = h_EE * aE * bE + h_EZd * (aE * bZ + aZ * bE) + h_ZdZd * aZ * bZ
        Dh_a = h_E * aE + h_Zd * aZ
        Dh_b = h_E * bE + h_Zd * bZ
        Dg_a = hg_E * aE
        Dg_b = hg_E * bE
        if p.gated:
            return g * D2h + Dg_a * Dh_b + Dg_b * Dh_a
        else:
            return D2h

    def B(a, b):
        out = np.zeros(3, dtype=complex)
        out[0] = hess_N(a, b)
        out[1] = hess_Z(a, b)
        out[2] = hess_E(a, b)
        return out

    if w is None:
        return B(u, v)

    def cub_N(a, b, c):
        return 0.0

    def cub_Z(a, b, c):
        # D³ Φ = sppp Dphi^3 + spp (D²phi cyclic) ; D³phi=0, sig term on D³phi=0
        Dphi_a = phi_N * a[0] + phi_E * a[2]
        Dphi_b = phi_N * b[0] + phi_E * b[2]
        Dphi_c = phi_N * c[0] + phi_E * c[2]
        D2_ab = phi_NN * a[0] * b[0] + phi_NE * (a[0] * b[2] + a[2] * b[0])
        D2_ac = phi_NN * a[0] * c[0] + phi_NE * (a[0] * c[2] + a[2] * c[0])
        D2_bc = phi_NN * b[0] * c[0] + phi_NE * (b[0] * c[2] + b[2] * c[0])
        return invtm * (
            sppp * Dphi_a * Dphi_b * Dphi_c
            + spp * (D2_ab * Dphi_c + D2_ac * Dphi_b + D2_bc * Dphi_a)
        )

    # third ders of h
    h_EEE = 0.0
    h_EEZd = 0.0
    h_EZdZd = 0.0
    h_ZdZdZd = 6.0 * d0 * Zref / (Zref + Zs) ** 4

    def cub_E(a, b, c):
        aE, bE, cE = a[2], b[2], c[2]
        aZ, bZ, cZ = a[3], b[3], c[3]
        D3h = (
            h_ZdZdZd * aZ * bZ * cZ
        )
        D2h_ab = h_EE * aE * bE + h_EZd * (aE * bZ + aZ * bE) + h_ZdZd * aZ * bZ
        D2h_ac = h_EE * aE * cE + h_EZd * (aE * cZ + aZ * cE) + h_ZdZd * aZ * cZ
        D2h_bc = h_EE * bE * cE + h_EZd * (bE * cZ + bZ * cE) + h_ZdZd * bZ * cZ
        Dh_a = h_E * aE + h_Zd * aZ
        Dh_b = h_E * bE + h_Zd * bZ
        Dh_c = h_E * cE + h_Zd * cZ
        Dg_a = hg_E * aE
        Dg_b = hg_E * bE
        Dg_c = hg_E * cE
        if p.gated:
            # D³(gh) = g D³h + cyclic Dg D²h   (D²g=D³g=0)
            return g * D3h + Dg_a * D2h_bc + Dg_b * D2h_ac + Dg_c * D2h_ab
        else:
            return D3h

    def C(a, b, c):
        out = np.zeros(3, dtype=complex)
        out[0] = cub_N(a, b, c)
        out[1] = cub_Z(a, b, c)
        out[2] = cub_E(a, b, c)
        return out

    return B(u, v), C(u, v, w)


def pack4(vec3, zd):
    a = np.zeros(4, dtype=complex)
    a[:3] = vec3
    a[3] = zd
    return a


def hassard_l1(p: P, Ns, Zs, Es, co, omega, tau):
    A0, At = A0_Atau(co)
    pvec, qvec = right_left_eigs(co, omega, tau)
    ei = np.exp(-1j * omega * tau)
    ei2 = np.exp(-2j * omega * tau)
    # 4-vectors at current / delayed
    def v4(amp, factor):
        # current = amp, delayed Z = amp[1]*factor
        return pack4(amp, amp[1] * factor)

    u_p = v4(pvec, ei)
    u_pb = v4(pvec.conj(), np.conj(ei))

    Bpp = B_and_C(p, Ns, Zs, Es, u_p, u_p)
    Bppb = B_and_C(p, Ns, Zs, Es, u_p, u_pb)

    # w20: (2iω I - A0 - At e^{-2iωτ}) w20 = B(p,p)
    M20 = 2j * omega * np.eye(3) - A0 - At * ei2
    w20 = solve(M20, Bpp)
    # w11: -(A0+At) w11 = B(p, pbar)
    M11 = -(A0 + At)
    w11 = solve(M11, Bppb)

    u_w20 = v4(w20, ei2)  # e^{2iω(t-τ)} = e^{2iωt} e^{-2iωτ}
    u_w11 = v4(w11, 1.0)  # equilibrium (delay factor 1)

    Bw20_pb = B_and_C(p, Ns, Zs, Es, u_w20, u_pb)
    Bw11_p = B_and_C(p, Ns, Zs, Es, u_w11, u_p)
    _, Cpppb = B_and_C(p, Ns, Zs, Es, u_p, u_p, u_pb)

    # Kuznetsov: c1 = (1/2) q* [ B(w20, pbar) + 2 B(w11, p) + C(p,p,pbar) ]
    vec = Bw20_pb + 2.0 * Bw11_p + Cpppb
    c1 = 0.5 * (qvec.conj() @ vec)

    # dλ/dτ from differentiating Δ(λ)p = 0
    # (I + τ At e^{-λτ}) dλ + At (-λ) e^{-λτ} dτ  applied... 
    # q* (dDelta/dλ dλ + dDelta/dτ dτ) p = 0
    # dDelta/dτ = -At (-λ) e^{-λτ} wait Delta = λI - A0 - At e^{-λτ}
    # dDelta/dτ = - At e^{-λτ} (-λ) = λ At e^{-λτ}
    dDelta_dlam = np.eye(3) + tau * At * ei
    dDelta_dtau = (1j * omega) * At * ei
    dlam_dtau = -(qvec.conj() @ (dDelta_dtau @ pvec)) / (qvec.conj() @ (dDelta_dlam @ pvec))

    # amplitude eq: ṙ = Re(dλ/dμ) μ r + Re(c1) r^3  with μ=τ-τH
    # paper convention l1 in ȧ = σ a + l1 a³, σ = Re λ
    l1 = float(np.real(c1))
    return {
        "c1_re": float(np.real(c1)),
        "c1_im": float(np.imag(c1)),
        "l1": l1,
        "dlam_dtau_re": float(np.real(dlam_dtau)),
        "dlam_dtau_im": float(np.imag(dlam_dtau)),
        "omega": float(omega),
        "tau": float(tau),
        "svd_ok": True,
        "p_norm": float(norm(pvec)),
    }


def monodromy(co, Tr):
    AN, AE, BN, BE, CE, CZ, d = (co[k] for k in ("AN", "AE", "BN", "BE", "CE", "CZ", "d"))
    Ahold = np.array([[AN, 0.0, AE], [BN, -d, BE], [0.0, 0.0, 0.0]], dtype=float)
    # exp(Ahold Tr)
    from scipy.linalg import expm

    jump = np.array(
        [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, Tr * CZ, 1.0 + Tr * CE]], dtype=float
    )
    M = jump @ expm(Ahold * Tr)
    ev = eigvals(M)
    rho = float(np.max(np.abs(ev)))
    # classify
    pair = []
    for z in ev:
        pair.append((float(np.real(z)), float(np.imag(z)), float(np.abs(z)), float(np.angle(z))))
    return M, ev, rho, pair


def scan_monodromy(co, Trs):
    rows = []
    crossings = []
    prev = None
    for Tr in Trs:
        _, ev, rho, pair = monodromy(co, float(Tr))
        # NS: complex pair with |λ| crossing 1, angle not 0 or pi
        cpx = [z for z in ev if abs(np.imag(z)) > 1e-8]
        rows.append({"Tr": float(Tr), "rho": rho, "ev": [(float(z.real), float(z.imag)) for z in ev]})
        if prev is not None:
            if (prev["rho"] - 1) * (rho - 1) < 0:
                crossings.append({"Tr": float(Tr), "rho": rho, "kind": "rho_cross_1"})
        # also check complex pair modulus
        prev = {"rho": rho, "ev": ev}
    return rows, crossings


def refine_crossings(co, Trs_fine):
    found = []
    rhos = []
    for Tr in Trs_fine:
        _, ev, rho, _ = monodromy(co, float(Tr))
        rhos.append(rho)
    rhos = np.array(rhos)
    for i in range(len(Trs_fine) - 1):
        if (rhos[i] - 1) * (rhos[i + 1] - 1) <= 0:
            # bisection
            a, b = float(Trs_fine[i]), float(Trs_fine[i + 1])
            for _ in range(40):
                m = 0.5 * (a + b)
                _, ev, rm, _ = monodromy(co, m)
                ra = monodromy(co, a)[2]
                if (ra - 1) * (rm - 1) <= 0:
                    b = m
                else:
                    a = m
            Tc = 0.5 * (a + b)
            _, ev, rm, pair = monodromy(co, Tc)
            # period of NS: 2π / arg
            angs = [abs(np.angle(z)) for z in ev if abs(np.abs(z) - 1) < 0.05 and abs(np.imag(z)) > 1e-6]
            per = 2 * np.pi / angs[0] * Tc if angs else None  # samples per cycle * Tr? 
            # discrete rotation: λ = e^{±iθ}, oscillation period = 2π Tr / θ
            found.append(
                {
                    "Tr": Tc,
                    "rho": rm,
                    "ev": [(float(z.real), float(z.imag), float(abs(z)), float(np.angle(z))) for z in ev],
                    "period_yr": (2 * np.pi / angs[0] * Tc) if angs else None,
                }
            )
    return found


# ---------- nonlinear RHS and DDE ----------
def rhs(p: P, N, Z, E, Zd):
    S = p.r * N * (1.0 - N / p.K)
    phi = p.q * E * N - S
    kphi = p.k * phi
    if kphi > 40:
        sp = phi
    elif kphi < -40:
        sp = math.exp(kphi) / p.k
    else:
        sp = math.log1p(math.exp(kphi)) / p.k
    filt = sp - math.log(2.0) / p.k + p.delta
    if filt < 0.0:
        filt = 0.0
    dN = S - p.q * E * N
    dZ = (filt - Z) / p.taum
    h = p.eta * E * (Zd / p.Dref - E / p.Emax) + p.d0 * Zd / (p.Zref + Zd)
    if p.gated:
        g = 1.0 - E / p.Emax
        if g < 0.0:
            g = 0.0
        dE = g * h
    else:
        dE = h
    return dN, dZ, dE


def simulate(p: P, tau, T, dt, hist, burn_frac=0.6):
    nstep = int(T / dt)
    ndel = max(1, int(round(tau / dt)))
    bufN = np.empty(ndel + 1)
    bufZ = np.empty(ndel + 1)
    bufE = np.empty(ndel + 1)
    bufN[:] = hist[0]
    bufZ[:] = hist[1]
    bufE[:] = hist[2]
    N, Z, E = hist
    # store last stretch
    keep_from = int(burn_frac * nstep)
    nkeep = nstep - keep_from
    trN = np.empty(nkeep)
    trZ = np.empty(nkeep)
    trE = np.empty(nkeep)
    kkeep = 0
    idx = 0
    filt_min = 1e9
    Emax_seen = E
    Nmin_seen = N
    floor_hits = 0
    for i in range(nstep):
        Zd = bufZ[idx]  # value from tau ago: we will write at idx after step
        # actually circular: store newest at idx, oldest is idx+1
        # initialize filled with hist; after writing sequentially...
        # Use: pointer `idx` is the slot of the oldest sample (= delayed)
        Zd = bufZ[idx]
        k1 = rhs(p, N, Z, E, Zd)
        N2 = N + 0.5 * dt * k1[0]
        Z2 = Z + 0.5 * dt * k1[1]
        E2 = E + 0.5 * dt * k1[2]
        # delayed at t+dt/2 ≈ same discrete delay (fixed-step)
        k2 = rhs(p, N2, Z2, E2, Zd)
        N3 = N + 0.5 * dt * k2[0]
        Z3 = Z + 0.5 * dt * k2[1]
        E3 = E + 0.5 * dt * k2[2]
        k3 = rhs(p, N3, Z3, E3, Zd)
        N4 = N + dt * k3[0]
        Z4 = Z + dt * k3[1]
        E4 = E + dt * k3[2]
        k4 = rhs(p, N4, Z4, E4, Zd)
        N = N + dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6.0
        Z = Z + dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6.0
        E = E + dt * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2]) / 6.0
        if E < 0.0:
            E = 0.0
        if p.gated and E > p.Emax:
            E = p.Emax
        if N < 0.0:
            N = 0.0
        bufN[idx] = N
        bufZ[idx] = Z
        bufE[idx] = E
        idx += 1
        if idx > ndel:
            idx = 0
        if E > Emax_seen:
            Emax_seen = E
        if N < Nmin_seen:
            Nmin_seen = N
        if i >= keep_from:
            trN[kkeep] = N
            trZ[kkeep] = Z
            trE[kkeep] = E
            kkeep += 1
    return dict(N=trN, Z=trZ, E=trE, Emax_seen=float(Emax_seen), Nmin_seen=float(Nmin_seen))


def amplitude_period(trN, dt):
    x = trN - np.mean(trN)
    amp = 0.5 * (np.max(trN) - np.min(trN))
    # zero crossings of demeaned
    s = np.sign(x)
    s[s == 0] = 1
    zc = np.where(np.diff(s) < 0)[0]  # falling
    if len(zc) >= 3:
        pers = np.diff(zc) * dt
        per = float(np.median(pers))
    else:
        # FFT
        spec = np.fft.rfft(x)
        freqs = np.fft.rfftfreq(len(x), dt)
        spec[0] = 0
        j = np.argmax(np.abs(spec))
        per = float(1.0 / freqs[j]) if freqs[j] > 0 else float("nan")
    return float(amp), per, float(np.max(trN)), float(np.min(trN))


def analyse_system(p: P):
    Ns, Zs, Es = equilibrium(p)
    co = lin_coeff(p, Ns, Zs, Es)
    xs, poly = hopf_cubic(co)
    hops = []
    for x in xs:
        om = math.sqrt(x)
        taus, Pv, Lv = tau_from_omega(co, om)
        # fundamental (smallest) tau
        if not taus:
            continue
        t0 = min(taus)
        h = hassard_l1(p, Ns, Zs, Es, co, om, t0)
        # also next branch
        hops.append(
            {
                "omega": om,
                "period": 2 * math.pi / om,
                "tau0": t0,
                "taus": taus[:4],
                "l1": h["l1"],
                "c1_re": h["c1_re"],
                "c1_im": h["c1_im"],
                "dlam_dtau_re": h["dlam_dtau_re"],
                "criticality": "subcritical" if h["l1"] > 0 else "supercritical",
            }
        )
    hops.sort(key=lambda z: z["tau0"])
    return {
        "name": p.name,
        "eq": {"N": Ns, "Z": Zs, "E": Es},
        "lin": {k: float(v) for k, v in co.items()},
        "H_positive_roots": xs,
        "hopfs": hops,
        "gated": p.gated,
        "params": asdict(p),
    }


def main_local():
    systems = [
        P(name="A_gated", gated=True),
        P(name="A_ungated", gated=False),
        P(name="B_ungated", eta=2.756, Emax=26.0, gated=False),
        P(name="B_gated", eta=2.756, Emax=26.0, gated=True),
    ]
    out = {}
    for p in systems:
        out[p.name] = analyse_system(p)
        print("=" * 60)
        print(p.name, out[p.name]["eq"], out[p.name]["lin"])
        for h in out[p.name]["hopfs"]:
            print(
                "  Hopf tau0=%.6f  T=%.3f  l1=%.6e  dReλ/dτ=%.4e  %s"
                % (h["tau0"], h["period"], h["l1"], h["dlam_dtau_re"], h["criticality"])
            )
    # monodromy scans
    variants = {
        "A_gated": P(name="A_gated", gated=True),
        "A_r08": P(name="A_r08", r=0.8, gated=True),
        "A_r16": P(name="A_r16", r=1.6, gated=True),
        "A_r02_fasteta": P(name="A_r02", gated=True),
    }
    mono = {}
    Trs = np.concatenate(
        [np.linspace(0.05, 2.0, 80), np.linspace(2.0, 20.0, 360), np.linspace(20.0, 40.0, 80)]
    )
    for key, p in variants.items():
        Ns, Zs, Es = equilibrium(p)
        co = lin_coeff(p, Ns, Zs, Es)
        rows, _ = scan_monodromy(co, Trs)
        found = refine_crossings(co, np.linspace(0.2, 20.0, 2001))
        # annual
        _, ev1, rho1, pair1 = monodromy(co, 1.0)
        mono[key] = {
            "eq": {"N": Ns, "E": Es},
            "lin": {k: float(v) for k, v in co.items()},
            "rho_Tr1": rho1,
            "ev_Tr1": pair1,
            "crossings": found,
            "curve": [{"Tr": r["Tr"], "rho": r["rho"]} for r in rows[::2]],
        }
        print(key, "eq", Ns, Es, "rho(1)=", rho1, "cross", found)
    out["monodromy"] = mono
    with open(RES, "w") as f:
        json.dump(out, f, indent=2)
    print("wrote", RES)
    return out


if __name__ == "__main__":
    main_local()
