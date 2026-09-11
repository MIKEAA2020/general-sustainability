"""
corrected_shooting.py
=====================

Shooting-based Floquet analysis for the CORRECTED three-state core
(Eq. eq:stock-core / eq:Z-core / eq:effort-core-corrected, i.e. with the
(1 - E/E_max) gate), Candidate A. The small-amplitude unstable periodic orbit
at tau=3.700 (just above tau_- = 3.666) is seeded from the project's own
checkpoint (unstable_clean_ckpt.npz), re-converged as a fixed point of the
discrete segment map, and its Floquet multipliers are the eigenvalues of the
central-difference Jacobian of that map.

Expected: dominant (radial) multiplier ~ exp(-2 sigma T), with sigma =
Re(lambda_rightmost) = -3.209e-6 at tau=3.7 and T ~ 249.875, giving
exp(-2 sigma T) = 1.001605 -- an UNSTABLE orbit (the subcritical SNPO
partner). The phase multiplier should be recovered at ~1.
"""
import numpy as np
from numba import njit
from elevation_solvers import PARAMS_A, params_arr

@njit(fastmath=True)
def rhs_corrected_local(N, Z, E, Ztau, p):
    r_, K_, q_ = p[0], p[1], p[2]
    eta_, Emax_, Dref_ = p[3], p[4], p[6]
    delta0_, Zref_, k_, taum_ = p[9], p[8], p[7], p[5]
    delta_ = p[10]
    S = r_*N*(1 - N/K_)
    C = q_*E*N
    Ndot = S - C
    ku = k_*(C - S)
    if ku > 30.0:
        sp = ku/k_
    elif ku < -30.0:
        sp = 0.0
    else:
        sp = np.log1p(np.exp(ku))/k_
    inner = sp - np.log(2.0)/k_ + delta_
    Zdot = ((inner if inner > 0.0 else 0.0) - Z)/taum_
    bracket = eta_*E*(Ztau/Dref_ - E/Emax_) + delta0_*Ztau/(Zref_ + Ztau)
    Edot = (1.0 - E/Emax_)*bracket
    return Ndot, Zdot, Edot

@njit(fastmath=True)
def _advance_seg_corrected(seg, n_tau, n_steps, dt, p):
    nseg = 3*(n_tau+1)
    buf = np.empty((n_tau+1, 3))
    for j in range(n_tau+1):
        buf[j,0] = seg[3*j]; buf[j,1] = seg[3*j+1]; buf[j,2] = seg[3*j+2]
    idx = n_tau
    N = seg[nseg-3]; Z = seg[nseg-2]; E = seg[nseg-1]
    for step in range(n_steps):
        Ztau = buf[(idx - n_tau) % (n_tau+1), 1]
        k1N, k1Z, k1E = rhs_corrected_local(N, Z, E, Ztau, p)
        k2N, k2Z, k2E = rhs_corrected_local(N+dt/2*k1N, Z+dt/2*k1Z, E+dt/2*k1E, Ztau, p)
        k3N, k3Z, k3E = rhs_corrected_local(N+dt/2*k2N, Z+dt/2*k2Z, E+dt/2*k2E, Ztau, p)
        k4N, k4Z, k4E = rhs_corrected_local(N+dt*k3N, Z+dt*k3Z, E+dt*k3E, Ztau, p)
        N = N + dt/6.0*(k1N + 2*k2N + 2*k3N + k4N)
        Z = Z + dt/6.0*(k1Z + 2*k2Z + 2*k3Z + k4Z)
        E = E + dt/6.0*(k1E + 2*k2E + 2*k3E + k4E)
        if N < 0.0: N = 0.0
        if E < 0.0: E = 0.0
        if E > Emax_: E = Emax_
        idx = (idx + 1) % (n_tau + 1)
        buf[idx,0] = N; buf[idx,1] = Z; buf[idx,2] = E
    newseg = np.empty(nseg)
    for j in range(n_tau+1):
        jj = (idx - n_tau + j) % (n_tau+1)
        newseg[3*j] = buf[jj,0]; newseg[3*j+1] = buf[jj,1]; newseg[3*j+2] = buf[jj,2]
    return newseg

# Emax as module-level for the numba closure
Emax_ = 30.0

def advance_seg_corrected(seg, n_tau, n_steps, dt):
    return _advance_seg_corrected(np.asarray(seg, dtype=np.float64), n_tau, n_steps, dt,
                                  params_arr(PARAMS_A()))

def converge_fixed_point(seg0, n_tau, n_steps, dt, pin_idx, pin_val, maxit=25, tol=1e-10):
    nseg = len(seg0)
    mask = np.ones(nseg, dtype=bool); mask[pin_idx] = False
    def F(seg):
        return advance_seg_corrected(seg, n_tau, n_steps, dt) - seg
    def F_red(s):
        seg = np.zeros(nseg); seg[mask] = s; seg[pin_idx] = pin_val
        return F(seg)[mask]
    s = seg0[mask]
    for it in range(maxit):
        f = F_red(s)
        rms = np.sqrt(np.mean(f**2))
        if it % 3 == 0:
            print(f"    Newton it {it}: rms|F| = {rms:.3e}")
        if rms < tol:
            seg = np.zeros(nseg); seg[mask] = s; seg[pin_idx] = pin_val
            return seg, True, rms
        h = 1e-6
        J = np.zeros((len(s), len(s)))
        for j in range(len(s)):
            sp = s.copy(); sp[j] += h
            fp = F_red(sp)
            sm = s.copy(); sm[j] -= h
            fm = F_red(sm)
            J[:, j] = (fp - fm)/(2*h)
        try:
            ds = np.linalg.solve(J, -f)
        except np.linalg.LinAlgError:
            ds = np.linalg.lstsq(J, -f, rcond=None)[0]
        alpha = 1.0; improved = False
        for _ in range(30):
            s_new = s + alpha*ds
            f_new = F_red(s_new)
            if np.sqrt(np.mean(f_new**2)) < rms:
                improved = True; break
            alpha *= 0.5
        if not improved:
            return None, False, rms
        s = s + alpha*ds
    seg = np.zeros(nseg); seg[mask] = s; seg[pin_idx] = pin_val
    return seg, False, rms

def full_monodromy_central(seg, n_tau, n_steps, dt, eps=1e-6):
    """Central-difference FD Jacobian of the full segment map (2*nseg advances)."""
    nseg = len(seg)
    M = np.zeros((nseg, nseg))
    for j in range(nseg):
        sp = seg.copy(); sp[j] += eps
        sm = seg.copy(); sm[j] -= eps
        Mp = advance_seg_corrected(sp, n_tau, n_steps, dt)
        Mm = advance_seg_corrected(sm, n_tau, n_steps, dt)
        M[:, j] = (Mp - Mm)/(2*eps)
    return M

def segment_from_checkpoint(ckpt_path, tau, dt):
    """Build the initial segment from the checkpoint orbit (states[0] at tau=3.700)."""
    from scipy.interpolate import CubicSpline
    d = np.load(ckpt_path)
    M = int(d['M']); v = d['states'][0]
    T_c = v[3*M]
    th = np.linspace(0, 2*np.pi, M, endpoint=False)*T_c/(2*np.pi)
    def mk(x):
        tp = np.concatenate([th-T_c, th, th+T_c]); xp = np.concatenate([x,x,x])
        return CubicSpline(tp, xp)
    Nf, Zf, Ef = mk(v[0:M]), mk(v[M:2*M]), mk(v[2*M:3*M])
    n_tau = int(round(tau/dt)); nseg = 3*(n_tau+1)
    seg = np.zeros(nseg)
    for k in range(n_tau+1):
        tt = (k - n_tau)*dt
        seg[3*k] = float(Nf(tt)); seg[3*k+1] = float(Zf(tt)); seg[3*k+2] = float(Ef(tt))
    return seg, n_tau, nseg, T_c
