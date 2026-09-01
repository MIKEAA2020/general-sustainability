"""
tau=0 decomposition of the stage-structured r-window
=====================================================
Raw Hopf-crossing existence in the stage model mixes TWO mechanisms:
  (a) institutional-delay-amplified instability (the manuscript's mechanism;
      requires tau=0 to be STABLE so that increasing tau destabilises), and
  (b) maturation-delay-only biological instability (cohort resonance;
      already present at tau=0, institutional delay irrelevant).

For each (r, g, eta) we compute the rightmost real part R_max of the tau=0
characteristic roots  det(lambda I - J0 - J1t - J1g e^{-lambda g}) = 0:
    R_max < 0  =>  tau=0 stable  =>  crossings are institutional-delay-induced
    R_max >= 0 =>  tau=0 (marginally) unstable => biological cohort oscillation

We also verify representative points with a two-delay RK4 integrator
(delays g on N, tau on Z).
"""
import numpy as np
from scipy.optimize import root as scipy_root
from stage_r_window import stage_jacobians, stage_crossings

def char_tau0(lam, J0, J1t, J1g, g):
    """det(lambda I - J0 - J1t - J1g e^{-lambda g})."""
    return np.linalg.det(lam * np.eye(3) - J0 - J1t - J1g * np.exp(-lam * g))

def rightmost_tau0(r, g, eta_v, mesh_sigma=(-0.15, 0.08, 231), mesh_omega=(0.0, 6.0, 241)):
    res = stage_jacobians(r, g, eta_v)
    if res is None:
        return None, None
    N, E, Z, J0, J1g, J1t = res
    sigs = np.linspace(*mesh_sigma)
    omegs = np.linspace(*mesh_omega)
    SS, WW = np.meshgrid(sigs, omegs, indexing='ij')
    lam = SS + 1j * WW
    M11 = lam - J0[0, 0] - J1t[0, 0] - J1g[0, 0] * np.exp(-lam * g)
    M12 = -J0[0, 1] - J1t[0, 1] - J1g[0, 1] * np.exp(-lam * g)
    M13 = -J0[0, 2] - J1t[0, 2] - J1g[0, 2] * np.exp(-lam * g)
    M21 = -J0[1, 0] - J1t[1, 0] - J1g[1, 0] * np.exp(-lam * g)
    M22 = lam - J0[1, 1] - J1t[1, 1] - J1g[1, 1] * np.exp(-lam * g)
    M23 = -J0[1, 2] - J1t[1, 2] - J1g[1, 2] * np.exp(-lam * g)
    M31 = -J0[2, 0] - J1t[2, 0] - J1g[2, 0] * np.exp(-lam * g)
    M32 = -J0[2, 1] - J1t[2, 1] - J1g[2, 1] * np.exp(-lam * g)
    M33 = lam - J0[2, 2] - J1t[2, 2] - J1g[2, 2] * np.exp(-lam * g)
    detf = (M11 * (M22 * M33 - M23 * M32)
            - M12 * (M21 * M33 - M23 * M31)
            + M13 * (M21 * M32 - M22 * M31))
    A = np.abs(detf)
    # candidate roots: local minima of |detf| on the mesh
    cands = []
    for i in range(1, sigs.size - 1):
        for j in range(1, omegs.size - 1):
            if A[i, j] < A[i - 1, j] and A[i, j] < A[i + 1, j] \
               and A[i, j] < A[i, j - 1] and A[i, j] < A[i, j + 1]:
                if A[i, j] < 0.05:
                    cands.append((sigs[i], omegs[j], A[i, j]))
    cands.sort(key=lambda t: t[2])
    roots = []
    for (s0, w0, _) in cands[:12]:
        def F(x):
            s, w = x
            l = s + 1j * w
            f = char_tau0(l, J0, J1t, J1g, g)
            return [f.real, f.imag]
        sol = scipy_root(F, [s0, w0], method='hybr')
        if sol.success and abs(F(sol.x)[0]) < 1e-6 and abs(F(sol.x)[1]) < 1e-6:
            s, w = sol.x
            if w > 1e-6:
                roots.append(s)
    rmax = max(roots) if roots else None
    # also real-axis roots (w ~ 0): scan sigma directly
    rsig = []
    for s in np.linspace(-0.5, 0.2, 1401):
        f = char_tau0(s, J0, J1t, J1g, g)
        if abs(f) < 1e-3:
            rsig.append(s)
    rmax_r = max(rsig) if rsig else None
    all_max = -np.inf
    if rmax is not None: all_max = max(all_max, rmax)
    if rmax_r is not None: all_max = max(all_max, rmax_r)
    if all_max == -np.inf:
        # no roots found: conservative: assume stable (mesh shows none near axis)
        all_max = -0.5
    return all_max, (N, E, Z)

def two_delay_integrate(r, g, tau, eta_v, T, dt=0.05, pert=1e-3):
    """RK4 for the stage model with delays g (N) and tau (Z)."""
    from droop_test import softplus
    res = stage_jacobians(r, g, eta_v)
    N0, E0, Z0 = res[0], res[1], res[2]
    y0 = np.array([N0 * (1 + pert), Z0 * (1 + pert), E0 * (1 + pert)])
    g_ = max(g, 1e-9); tau_ = max(tau, 1e-9)
    nsteps = int(round(T / dt))
    h = T / nsteps
    ys = np.zeros((nsteps + 1, 3))
    ys[0] = y0
    eq = np.array([N0, Z0, E0])
    def hist(t):
        return eq
    def delayed_n(t):
        tt = t - g_
        if tt <= 0: return hist(tt)[0]
        ti = tt / h
        i = int(np.floor(ti))
        if i >= nsteps: return ys[nsteps, 0]
        f = ti - i
        return (1 - f) * ys[i, 0] + f * ys[i + 1, 0]
    def delayed_z(t):
        tt = t - tau_
        if tt <= 0: return hist(tt)[1]
        ti = tt / h
        i = int(np.floor(ti))
        if i >= nsteps: return ys[nsteps, 1]
        f = ti - i
        return (1 - f) * ys[i, 1] + f * ys[i + 1, 1]
    def rhs(y, nd, zd):
        N, Z, E = y
        fN = r * nd * (1 - nd / K_) if False else 0  # placeholder
        return None
    # direct loop
    def f(y, nd, zd):
        N, Z, E = y
        reg = r * nd * (1.0 - nd / K_)
        d = qc_ * E * N - reg
        src = max(0.0, softplus(d) - np.log(2.0) / k_ + delta_)
        dN = reg - qc_ * E * N
        dZ = (src - Z) / taum_
        fb = eta_v * E * (zd / Dref_ - E / Emax_) + delta0_ * zd / (Zref_ + zd)
        dE = (1.0 - E / Emax_) * fb
        return np.array([dN, dZ, dE])
    for i in range(nsteps):
        t = i * h
        y = ys[i]
        nd1 = delayed_n(t); zd1 = delayed_z(t)
        k1 = f(y, nd1, zd1)
        nd2 = delayed_n(t + h / 2); zd2 = delayed_z(t + h / 2)
        k2 = f(y + h / 2 * k1, nd2, zd2)
        k3 = f(y + h / 2 * k2, nd2, zd2)
        nd4 = delayed_n(t + h); zd4 = delayed_z(t + h)
        k4 = f(y + h * k3, nd4, zd4)
        ys[i + 1] = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return ys

def tail_stats(ys, dt, frac=0.5):
    tail = ys[int(len(ys) * frac):]
    N = tail[:, 0]
    mn = N.mean()
    cross = [j for j in range(1, len(N)) if N[j - 1] < mn <= N[j]]
    per = np.median(np.diff(cross)) * dt if len(cross) >= 3 else None
    amp = N.max() - N.min()
    return per, amp, tail[-1, 0]

if __name__ == "__main__":
    # import constants
    from droop_test import K as K_, qc as qc_, Emax as Emax_, delta0 as delta0_
    from droop_test import Dref as Dref_, taum as taum_, Zref as Zref_, delta as delta_
    from droop_test import k as k_
    np.set_printoptions(precision=5, suppress=True)

    print("=" * 74)
    print("A. tau=0 decomposition of the stage windows")
    print("   (raw crossings vs crossings that are institutional-delay-induced)")
    print("=" * 74)
    for eta_v in (0.914, 3.0):
        print(f"  eta = {eta_v}")
        for g in (0.5, 1.0, 2.0, 5.0, 10.0, 20.0):
            raw_hi, inst_hi = 0.0, 0.0
            raw_lo, inst_lo = 1e9, 1e9
            fish_raw = fish_inst = 0
            for r in np.geomspace(0.005, 2.0, 200):
                rmax, _ = rightmost_tau0(r, g, eta_v)
                cr = stage_crossings(r, g, eta_v=eta_v, nw=3000)
                has_cr = cr is not None and len(cr) > 0
                if has_cr:
                    raw_lo = min(raw_lo, r); raw_hi = max(raw_hi, r)
                    if r >= 0.2: fish_raw += 1
                    if rmax is not None and rmax < 0:
                        inst_lo = min(inst_lo, r); inst_hi = max(inst_hi, r)
                        if r >= 0.2: fish_inst += 1
            def fmt(lo, hi):
                return f"[{lo:.4f}, {hi:.4f}]" if hi > 0 else "EMPTY"
            print(f"    g={g:5.1f}: raw window {fmt(raw_lo, raw_hi)}   "
                  f"institutional-only window (tau=0 stable) {fmt(inst_lo, inst_hi)}"
                  f"   fish-r crossings: raw {fish_raw}, institutional {fish_inst}")
    print()
    print("=" * 74)
    print("B. Nonlinear two-delay verification (RK4)")
    print("=" * 74)
    checks = [
        ("r=0.02, g=5, tau=5.5  (institutional window, tau=0 stable)", 0.02, 5.0, 5.5, 0.914, 4000),
        ("r=0.02, g=5, tau=0    (should be stable)",                   0.02, 5.0, 0.0, 0.914, 4000),
        ("r=0.5,  g=5, tau=5.5  (fish r, cohort mechanism?)",          0.5,  5.0, 5.5, 0.914, 4000),
        ("r=0.5,  g=5, tau=0    (fish r, maturation delay alone)",     0.5,  5.0, 0.0, 0.914, 4000),
        ("r=0.5,  g=5, tau=5.5  eta=3.0",                              0.5,  5.0, 5.5, 3.0,   4000),
    ]
    for name, r, g, tau, eta_v, T in checks:
        ys = two_delay_integrate(r, g, tau, eta_v, T, dt=0.05)
        per, amp, Nend = tail_stats(ys, 0.05)
        rmax, eq = rightmost_tau0(r, g, eta_v)
        print(f"  {name}:")
        print(f"     tau0 R_max={rmax:+.4f} | tail period="
              f"{per if per is None else round(per,1)} yr | tail amp(N)={amp:.3f}"
              f" | N_end={Nend:.2f}")
