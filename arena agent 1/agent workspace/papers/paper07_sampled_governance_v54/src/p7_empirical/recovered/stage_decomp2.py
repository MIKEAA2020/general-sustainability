"""
Corrected stage decomposition (validated integrators, nonlinear tau=0 test)
============================================================================
Integrator strategy (each validated against a known case):
  * g=0, tau>0   -> droop_test.integrate_dde (base core, already validated:
                    tau=5.5 -> P~268, amp~7.2)
  * g>0,  tau=0  -> single-delay integrator (delay g only), same RK4+
                    interpolation pattern as droop_test.integrate_dde
                    (delay always >> dt, so no future-state read)
  * g>0,  tau>0  -> two-delay integrator, used ONLY when min(g,tau) > 8*dt

tau=0 stability classification is NONLINEAR (ground truth): integrate the
tau=0 system from a 1% perturbation and measure the tail:
    stable            : |N - N*| -> ~0
    oscillatory       : sustained cycle, period detected
    drift (monotone)  : no cycle, |N - N*| not -> 0
"""
import numpy as np
from droop_test import (softplus, K, qc, Emax, delta0, Dref, taum, Zref,
                        delta, k, integrate_dde)
from stage_r_window import stage_jacobians, stage_crossings

def single_delay_tau0(r, g, eta_v, T=4000.0, dt=0.05, pert=1e-3):
    """tau=0 system: only delay g (on N in stock eq and deficit)."""
    res = stage_jacobians(r, g, eta_v)
    N0, E0, Z0 = res[0], res[1], res[2]
    y0 = np.array([N0*(1+pert), Z0*(1+pert), E0*(1+pert)])
    g_ = max(g, 4*dt)
    nsteps = int(round(T/dt)); h = T/nsteps
    ys = np.zeros((nsteps+1, 3)); ys[0] = y0
    eq = np.array([N0, Z0, E0])

    def f(y, nd):
        N, Z, E = y
        reg = r*nd*(1.0 - nd/K)
        d = qc*E*N - reg
        src = max(0.0, softplus(d) - np.log(2.0)/k + delta)
        dN = reg - qc*E*N
        dZ = (src - Z)/taum
        fb = eta_v*E*(Z/Dref - E/Emax) + delta0*Z/(Zref + Z)
        dE = (1.0 - E/Emax)*fb
        return np.array([dN, dZ, dE])

    def delayed_n(t):
        tt = t - g_
        if tt <= 0: return eq[0]
        ti = tt/h; i = int(np.floor(ti))
        if i >= nsteps: return ys[nsteps, 0]
        fr = ti - i
        return (1-fr)*ys[i, 0] + fr*ys[i+1, 0]

    for i in range(nsteps):
        t = i*h; y = ys[i]
        k1 = f(y, delayed_n(t))
        k2 = f(y + h/2*k1, delayed_n(t + h/2))
        k3 = f(y + h/2*k2, delayed_n(t + h/2))
        k4 = f(y + h*k3, delayed_n(t + h))
        ys[i+1] = y + h/6*(k1 + 2*k2 + 2*k3 + k4)
    # classify tail
    tail = ys[int(len(ys)*0.6):]
    N = tail[:, 0]
    mn = N.mean()
    cr = [j for j in range(1, len(N)) if N[j-1] < mn <= N[j]]
    per = np.median(np.diff(cr))*dt if len(cr) >= 3 else None
    amp = N.max() - N.min()
    Ne = tail[-1, 0]
    if per is not None and amp > 0.5:
        cls = 'oscillatory'
    elif abs(Ne - N0) < 0.5:
        cls = 'stable'
    else:
        cls = 'drift'
    return cls, per, amp, Ne

def two_delay_tau_gt0(r, g, tau, eta_v, T=4000.0, dt=0.05, pert=1e-3):
    assert g > 8*dt and tau > 8*dt, "two-delay integrator needs delays >> dt"
    res = stage_jacobians(r, g, eta_v)
    N0, E0, Z0 = res[0], res[1], res[2]
    y0 = np.array([N0*(1+pert), Z0*(1+pert), E0*(1+pert)])
    nsteps = int(round(T/dt)); h = T/nsteps
    ys = np.zeros((nsteps+1, 3)); ys[0] = y0
    eq = np.array([N0, Z0, E0])
    def dN(t):
        tt = t - g
        if tt <= 0: return eq[0]
        ti = tt/h; i = int(np.floor(ti))
        if i >= nsteps-1: return ys[nsteps,0]
        f = ti - i
        return (1-f)*ys[i,0] + f*ys[i+1,0]
    def dZ(t):
        tt = t - tau
        if tt <= 0: return eq[1]
        ti = tt/h; i = int(np.floor(ti))
        if i >= nsteps-1: return ys[nsteps,1]
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
    tail_ = ys[int(len(ys)*0.6):]
    N = tail_[:,0]; mn = N.mean()
    cr = [j for j in range(1,len(N)) if N[j-1] < mn <= N[j]]
    per = np.median(np.diff(cr))*dt if len(cr) >= 3 else None
    amp = N.max() - N.min()
    return per, amp, tail_[-1,0]

if __name__ == "__main__":
    print("=" * 72)
    print("1. INTEGRATOR VALIDATION")
    print("=" * 72)
    # (a) g=0 base via droop_test.integrate_dde
    from droop_test import base_rhs, base_equilibrium
    y0 = base_equilibrium(0.02, True); y0[0] *= 1.001
    hist = lambda t: base_equilibrium(0.02, True)
    ys = integrate_dde(base_rhs, y0, hist, 3000, 5.5, 0.02, True, None, dt=0.05)
    N = ys[int(len(ys)*0.6):, 0]; mn = N.mean()
    cr = [j for j in range(1,len(N)) if N[j-1] < mn <= N[j]]
    P = np.median(np.diff(cr))*0.05
    print(f"   base tau=5.5 (g=0): P={P:.1f} yr (expect ~268) amp={N.max()-N.min():.2f} (expect ~7.2)")
    # (b) single-delay tau=0 at r=0.02, g=5: hand calc says stock mode -0.0194 (stable)
    cls, per, amp, Ne = single_delay_tau0(0.02, 5.0, 0.914)
    print(f"   tau=0, r=0.02, g=5: {cls} (per={per}, amp={amp:.3f}, N_end={Ne:.2f}, N*={89.55:.2f})")
    # (c) two-delay tau>0 at r=0.02, g=5, tau=5.5
    per, amp, Ne = two_delay_tau_gt0(0.02, 5.0, 5.5, 0.914)
    print(f"   tau=5.5, r=0.02, g=5: P={per if per is None else round(per,1)} amp={amp:.3f} N_end={Ne:.2f}")
    print()
    print("=" * 72)
    print("2. tau=0 STABILITY CLASSIFICATION (nonlinear ground truth)")
    print("=" * 72)
    for eta_v in (0.914, 3.0):
        print(f"  eta = {eta_v}")
        for g in (1.0, 2.0, 5.0, 10.0):
            row = []
            for r in (0.02, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0):
                cls, per, amp, Ne = single_delay_tau0(r, g, eta_v)
                cr = stage_crossings(r, g, eta_v=eta_v, nw=3000)
                ncr = len(cr) if cr else 0
                row.append(f"r={r:4.2f}:{cls[0]}{ncr}")
            print(f"    g={g:4.1f}: " + "  ".join(row))
    print()
    print("=" * 72)
    print("3. KEY CASES: tau=0 classification + crossings + tau>0 behaviour")
    print("=" * 72)
    for (r, g, eta_v, note) in [
        (0.02, 5.0, 0.914, "slow r, g=5"),
        (0.3,  5.0, 0.914, "r=0.3 (slow-fish), g=5"),
        (0.5,  5.0, 0.914, "fish r, g=5"),
        (1.0,  1.0, 0.914, "fish r, g=1"),
        (1.0,  5.0, 0.914, "fish r, g=5"),
        (0.3,  5.0, 3.0,   "r=0.3, g=5, eta=3"),
    ]:
        cls, per0, amp0, Ne0 = single_delay_tau0(r, g, eta_v)
        cr = stage_crossings(r, g, eta_v=eta_v, nw=3000)
        s = f"  {note}: tau=0 -> {cls}"
        if per0: s += f" (P0={per0:.1f} yr)"
        s += f" | crossings={len(cr) if cr else 0}"
        if cr:
            w, tau0, P = cr[0]
            s += f" (first: P={P:.1f} yr, tau0={tau0:.2f} yr)"
        print(s)
        if cls == 'stable' and cr:
            per, amp, Ne = two_delay_tau_gt0(r, g, tau0 + 0.5, eta_v)
            print(f"       tau={tau0+0.5:.2f}: P={per if per is None else round(per,1)}"
                  f" amp={amp:.2f} N_end={Ne:.2f}")
