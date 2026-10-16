"""
Robust tau=0 rightmost-root solver + two-delay integrator validation.
=====================================================================
1. Validate the two-delay RK4 at g=0 against the base core:
   - (r=0.02, tau=5.5): sustained cycle, P ~ 268 yr, amp(N) ~ 7.2
   - (r=0.02, tau=0):  converges to equilibrium N*=89.55
2. Reliable tau=0 stability classification for the stage model:
   dense |f| scan near the origin + Newton refinement, rightmost real part.
"""
import numpy as np
from scipy.optimize import root as sroot
from stage_r_window import stage_jacobians
from droop_test import (softplus, K, qc, Emax, delta0, Dref, taum, Zref,
                        delta, k)

def char_f(lam, J0, J1t, J1g, g):
    return np.linalg.det(lam * np.eye(3) - J0 - J1t - J1g * np.exp(-lam * g))

def rightmost_robust(r, g, eta_v, smax=0.5, omega_max=1.5,
                     ns=400, nw=400):
    """Return (R_max, roots) with R_max = max real part of tau=0 roots."""
    res = stage_jacobians(r, g, eta_v)
    if res is None:
        return None, []
    N, E, Z, J0, J1g, J1t = res
    sigs = np.linspace(-smax, smax, ns)
    omegs = np.linspace(0.0, omega_max, nw)
    SS, WW = np.meshgrid(sigs, omegs, indexing='ij')
    lam = SS + 1j * WW
    M11 = lam - J0[0,0]-J1t[0,0]-J1g[0,0]*np.exp(-lam*g)
    M12 =      -J0[0,1]-J1t[0,1]-J1g[0,1]*np.exp(-lam*g)
    M13 =      -J0[0,2]-J1t[0,2]-J1g[0,2]*np.exp(-lam*g)
    M21 =      -J0[1,0]-J1t[1,0]-J1g[1,0]*np.exp(-lam*g)
    M22 = lam - J0[1,1]-J1t[1,1]-J1g[1,1]*np.exp(-lam*g)
    M23 =      -J0[1,2]-J1t[1,2]-J1g[1,2]*np.exp(-lam*g)
    M31 =      -J0[2,0]-J1t[2,0]-J1g[2,0]*np.exp(-lam*g)
    M32 =      -J0[2,1]-J1t[2,1]-J1g[2,1]*np.exp(-lam*g)
    M33 = lam - J0[2,2]-J1t[2,2]-J1g[2,2]*np.exp(-lam*g)
    detf = (M11*(M22*M33-M23*M32) - M12*(M21*M33-M23*M31)
            + M13*(M21*M32-M22*M31))
    A = np.abs(detf)
    idx = np.unravel_index(np.argmin(A), A.shape)
    best = (sigs[idx[0]], omegs[idx[1]], A[idx])
    # Newton refinement on [Re f, Im f] = 0 from several starts
    starts = []
    starts.append((best[0], best[1]))
    # also refine the top few local minima
    flat = A.flatten()
    order = np.argsort(flat)[:8]
    for k in order:
        i, j = np.unravel_index(k, A.shape)
        starts.append((sigs[i], omegs[j]))
    roots = []
    for (s0, w0) in starts:
        if w0 < 1e-4:
            w0 = 1e-3
        def F(x):
            s, w = x
            f = char_f(s + 1j*w, J0, J1t, J1g, g)
            return [f.real, f.imag]
        try:
            sol = sroot(F, [s0, w0], method='hybr')
            if sol.success:
                s, w = sol.x
                if abs(F([s, w])[0]) < 1e-5 and abs(F([s, w])[1]) < 1e-5 \
                   and w > 1e-4:
                    roots.append(s)
        except Exception:
            pass
    rmax = max(roots) if roots else -smax
    # real-axis roots separately (omega=0)
    rsig = []
    for s in np.linspace(-smax, smax, 2001):
        f = char_f(s, J0, J1t, J1g, g)
        if abs(f) < 1e-3:
            rsig.append(s)
    if rsig:
        rmax = max(rmax, max(rsig))
    return rmax, roots

# ---------------- two-delay integrator (reuse from stage_tau0) -------------
def two_delay_integrate(r, g, tau, eta_v, T, dt=0.05, pert=1e-3):
    res = stage_jacobians(r, g, eta_v)
    N0, E0, Z0 = res[0], res[1], res[2]
    y0 = np.array([N0*(1+pert), Z0*(1+pert), E0*(1+pert)])
    g_ = max(g, 1e-9); tau_ = max(tau, 1e-9)
    nsteps = int(round(T/dt)); h = T/nsteps
    ys = np.zeros((nsteps+1, 3)); ys[0] = y0
    eq = np.array([N0, Z0, E0])
    def dN(t):
        tt = t - g_
        if tt <= 0: return eq[0]
        ti = tt/h; i = int(np.floor(ti))
        if i >= nsteps: return ys[nsteps,0]
        f = ti - i
        return (1-f)*ys[i,0] + f*ys[i+1,0]
    def dZ(t):
        tt = t - tau_
        if tt <= 0: return eq[1]
        ti = tt/h; i = int(np.floor(ti))
        if i >= nsteps: return ys[nsteps,1]
        f = ti - i
        return (1-f)*ys[i,1] + f*ys[i+1,1]
    def f(y, nd, zd):
        N, Z, E = y
        reg = r*nd*(1.0 - nd/K)
        d = qc*E*N - reg
        src = max(0.0, softplus(d) - np.log(2.0)/k + delta)
        dN_ = reg - qc*E*N
        dZ_ = (src - Z)/taum
        fb = eta_v*E*(zd/Dref - E/Emax) + delta0*zd/(Zref+zd)
        dE_ = (1.0 - E/Emax)*fb
        return np.array([dN_, dZ_, dE_])
    for i in range(nsteps):
        t = i*h; y = ys[i]
        k1 = f(y, dN(t), dZ(t))
        k2 = f(y + h/2*k1, dN(t+h/2), dZ(t+h/2))
        k3 = f(y + h/2*k2, dN(t+h/2), dZ(t+h/2))
        k4 = f(y + h*k3, dN(t+h), dZ(t+h))
        ys[i+1] = y + h/6*(k1 + 2*k2 + 2*k3 + k4)
    return ys

def tail(ys, dt, frac=0.5):
    t = ys[int(len(ys)*frac):]
    N = t[:,0]; mn = N.mean()
    cr = [j for j in range(1,len(N)) if N[j-1] < mn <= N[j]]
    per = np.median(np.diff(cr))*dt if len(cr) >= 3 else None
    return per, N.max()-N.min(), t[-1,0]

if __name__ == "__main__":
    np.set_printoptions(precision=5, suppress=True)
    print("="*70)
    print("1. Integrator validation at g=0 (must match base core)")
    print("="*70)
    for tau in (5.5, 0.0):
        ys = two_delay_integrate(0.02, 0.0, tau, 0.914, 3000, dt=0.05)
        per, amp, Ne = tail(ys, 0.05)
        print(f"   g=0 r=0.02 tau={tau}: P={per if per is None else round(per,1)}"
              f"  amp={amp:.3f}  N_end={Ne:.3f}"
              f"  (base: tau=5.5 -> P~268 amp~7.2 ; tau=0 -> converge to 89.55)")
    print()
    print("2. Robust tau=0 rightmost root classification")
    for (r, g, eta_v, note) in [
        (0.02, 0.0, 0.914, "g=0 base"),
        (0.02, 5.0, 0.914, "slow r + g=5 (hand calc: stock mode -0.0194)"),
        (0.5,  5.0, 0.914, "fish r + g=5 (cohort?)"),
        (0.5,  5.0, 3.0,   "fish r + g=5, eta=3"),
        (0.02, 2.0, 0.914, "slow r + g=2"),
        (1.0,  1.0, 0.914, "r=1, g=1"),
    ]:
        rmax, roots = rightmost_robust(r, g, eta_v)
        print(f"   r={r:5.2f} g={g:4.1f} eta={eta_v}: R_max={rmax:+.5f}"
              f"  ({note})  {'UNSTABLE' if rmax > 0 else 'stable'}")
    print()
    print("3. Nonlinear confirmation of the classification")
    for (r, g, eta_v, note) in [
        (0.02, 5.0, 0.914, "slow r + g=5, tau=0"),
        (0.02, 5.0, 0.914, "slow r + g=5, tau=5.5"),
        (0.5,  5.0, 0.914, "fish r + g=5, tau=0"),
        (0.5,  5.0, 0.914, "fish r + g=5, tau=5.5"),
    ]:
        tau = 0.0 if "tau=0" in note else 5.5
        ys = two_delay_integrate(r, g, tau, eta_v, 6000, dt=0.05)
        per, amp, Ne = tail(ys, 0.05)
        print(f"   {note}: P={per if per is None else round(per,1)}"
              f"  amp={amp:.3f}  N_end={Ne:.2f}")
