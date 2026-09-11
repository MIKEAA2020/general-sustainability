"""
Fixed-point shooting + Floquet for periodic orbits of the UNGATED core DDE.

The discrete map P_dt advances a full state-history segment (3*(n_tau+1)
values on [-tau, 0]) by one period length n_steps*dt. A periodic orbit of the
discretised dynamics is a fixed point of P_dt; its Floquet multipliers are
the eigenvalues of D(P_dt) at that fixed point (including the trivial +1
phase multiplier). Converging the fixed point directly (rather than relying
on a separately-computed orbit) removes the period-mismatch error that
breaks naive monodromy tests.
"""
import numpy as np
from numba import njit
from elevation_solvers import PARAMS_A, params_arr

# ---------------- numba segment-map ----------------
@njit(fastmath=True)
def _advance_seg_numba(seg, n_tau, n_steps, dt, pa):
    """Advance a segment (size 3*(n_tau+1), state at times (k-n_tau)*dt) by
    n_steps*dt. Returns the final segment."""
    nseg = 3*(n_tau+1)
    buf = np.empty((n_tau+1, 3))
    for j in range(n_tau+1):
        buf[j,0] = seg[3*j]; buf[j,1] = seg[3*j+1]; buf[j,2] = seg[3*j+2]
    idx = n_tau
    N = seg[nseg-3]; Z = seg[nseg-2]; E = seg[nseg-1]
    for step in range(n_steps):
        Ztau = buf[(idx - n_tau) % (n_tau+1), 1]
        # RK4 with frozen delayed value (standard approx for smooth delay)
        # stage 1
        r_, K_, q_ = pa[0], pa[1], pa[2]
        S = r_*N*(1 - N/K_); C = q_*E*N
        Ndot1 = S - C
        ku = pa[7]*(C - S)
        if ku > 30.0:
            sp1 = ku/pa[7]
        elif ku < -30.0:
            sp1 = 0.0
        else:
            sp1 = np.log1p(np.exp(ku))/pa[7]
        inner = sp1 - np.log(2.0)/pa[7] + pa[10]
        Zdot1 = ((inner if inner > 0.0 else 0.0) - Z)/pa[5]
        Edot1 = pa[3]*E*(Ztau/pa[6] - E/pa[4]) + pa[9]*Ztau/(pa[8] + Ztau)
        # stage 2
        N2 = N + dt/2*Ndot1; Z2 = Z + dt/2*Zdot1; E2 = E + dt/2*Edot1
        S = r_*N2*(1 - N2/K_); C = pa[2]*E2*N2
        Ndot2 = S - C
        ku = pa[7]*(C - S)
        if ku > 30.0:
            sp2 = ku/pa[7]
        elif ku < -30.0:
            sp2 = 0.0
        else:
            sp2 = np.log1p(np.exp(ku))/pa[7]
        inner = sp2 - np.log(2.0)/pa[7] + pa[10]
        Zdot2 = ((inner if inner > 0.0 else 0.0) - Z2)/pa[5]
        Edot2 = pa[3]*E2*(Ztau/pa[6] - E2/pa[4]) + pa[9]*Ztau/(pa[8] + Ztau)
        # stage 3
        N3 = N + dt/2*Ndot2; Z3 = Z + dt/2*Zdot2; E3 = E + dt/2*Edot2
        S = r_*N3*(1 - N3/K_); C = pa[2]*E3*N3
        Ndot3 = S - C
        ku = pa[7]*(C - S)
        if ku > 30.0:
            sp3 = ku/pa[7]
        elif ku < -30.0:
            sp3 = 0.0
        else:
            sp3 = np.log1p(np.exp(ku))/pa[7]
        inner = sp3 - np.log(2.0)/pa[7] + pa[10]
        Zdot3 = ((inner if inner > 0.0 else 0.0) - Z3)/pa[5]
        Edot3 = pa[3]*E3*(Ztau/pa[6] - E3/pa[4]) + pa[9]*Ztau/(pa[8] + Ztau)
        # stage 4
        N4 = N + dt*Ndot3; Z4 = Z + dt*Zdot3; E4 = E + dt*Edot3
        S = r_*N4*(1 - N4/K_); C = pa[2]*E4*N4
        Ndot4 = S - C
        ku = pa[7]*(C - S)
        if ku > 30.0:
            sp4 = ku/pa[7]
        elif ku < -30.0:
            sp4 = 0.0
        else:
            sp4 = np.log1p(np.exp(ku))/pa[7]
        inner = sp4 - np.log(2.0)/pa[7] + pa[10]
        Zdot4 = ((inner if inner > 0.0 else 0.0) - Z4)/pa[5]
        Edot4 = pa[3]*E4*(Ztau/pa[6] - E4/pa[4]) + pa[9]*Ztau/(pa[8] + Ztau)
        N = N + dt/6.0*(Ndot1 + 2*Ndot2 + 2*Ndot3 + Ndot4)
        Z = Z + dt/6.0*(Zdot1 + 2*Zdot2 + 2*Zdot3 + Zdot4)
        E = E + dt/6.0*(Edot1 + 2*Edot2 + 2*Edot3 + Edot4)
        if N < 0.0: N = 0.0
        if E < 0.0: E = 0.0
        idx = (idx + 1) % (n_tau + 1)
        buf[idx,0] = N; buf[idx,1] = Z; buf[idx,2] = E
    newseg = np.empty(nseg)
    for j in range(n_tau+1):
        jj = (idx - n_tau + j) % (n_tau+1)
        newseg[3*j] = buf[jj,0]; newseg[3*j+1] = buf[jj,1]; newseg[3*j+2] = buf[jj,2]
    return newseg

def advance_seg(seg, n_tau, n_steps, dt):
    return _advance_seg_numba(np.asarray(seg, dtype=np.float64), n_tau, n_steps, dt, params_arr(PARAMS_A()))

def segment_from_orbit(orbit, tau, dt, T):
    """Sample orbit splines at times (k - n_tau)*dt, k=0..n_tau."""
    n_tau = int(round(tau/dt)); nseg = 3*(n_tau+1)
    seg = np.zeros(nseg)
    for k in range(n_tau+1):
        tt = (k - n_tau)*dt
        seg[3*k] = float(orbit['Nf'](tt)); seg[3*k+1] = float(orbit['Zf'](tt)); seg[3*k+2] = float(orbit['Ef'](tt))
    return seg, n_tau, nseg

def converge_fixed_point(seg0, n_tau, n_steps, dt, pin_idx, pin_val, maxit=30, tol=1e-9):
    """Damped Newton for F(seg)=0 with phase pin (seg[pin_idx]=pin_val fixed).
    Works on the reduced vector (all but pin_idx)."""
    nseg = len(seg0)
    mask = np.ones(nseg, dtype=bool); mask[pin_idx] = False
    idx_full = np.arange(nseg)[mask]
    def F(seg):
        return advance_seg(seg, n_tau, n_steps, dt) - seg
    def F_red(s):
        seg = np.zeros(nseg); seg[mask] = s; seg[pin_idx] = pin_val
        f = F(seg)
        return f[mask]
    s = seg0[mask]
    for it in range(maxit):
        f = F_red(s)
        rms = np.sqrt(np.mean(f**2))
        if it % 3 == 0:
            print(f"    Newton it {it}: rms|F| = {rms:.3e}")
        if rms < tol:
            seg = np.zeros(nseg); seg[mask] = s; seg[pin_idx] = pin_val
            return seg, True, rms
        # FD Jacobian of F_red
        h = 1e-6
        J = np.zeros((len(s), len(s)))
        for j in range(len(s)):
            sp = s.copy(); sp[j] += h
            fp = F_red(sp)
            sm = s.copy(); sm[j] -= h
            fm = F_red(sm)
            J[:, j] = (fp - fm)/(2*h)
        # solve J ds = -f with damping
        try:
            ds = np.linalg.solve(J, -f)
        except np.linalg.LinAlgError:
            ds = np.linalg.lstsq(J, -f, rcond=None)[0]
        # line search
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

def full_monodromy(seg, n_tau, n_steps, dt, eps=1e-6):
    """FD Jacobian of the full segment map at seg (nseg x nseg)."""
    nseg = len(seg)
    ref = advance_seg(seg, n_tau, n_steps, dt)
    M = np.zeros((nseg, nseg))
    for j in range(nseg):
        sp = seg.copy(); sp[j] += eps
        Mp = advance_seg(sp, n_tau, n_steps, dt)
        M[:, j] = (Mp - ref)/eps
    return M
