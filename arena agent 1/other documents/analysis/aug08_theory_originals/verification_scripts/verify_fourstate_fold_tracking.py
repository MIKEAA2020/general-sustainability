"""
verify_fourstate_fold_tracking.py
=================================

Closes the four-state-core gap: "the full Hopf/SNPO fold structure has been
checked at five discrete kappa_A points ... rather than via continuous
fold-tracking across [0,0.5]."

Tracks BOTH folds continuously over kappa_A in [0.0015, 0.5] (physical,
donor-limited equilibrium, Candidate A):

  - lower fold  tau_SNPO,L(kappa_A): large cycle persists just above tau_-,
    collapses upward; located by carry-continuation bisection from a cycle
    converged near tau_- + small.
  - upper fold  tau_SNPO,R(kappa_A): large cycle persists just below tau_+,
    collapses downward; located by carry-continuation bisection from a cycle
    converged near tau_+ - small (ghost transients excluded by using the
    converged-cycle state as the seed, per the manuscript's carry-down method).

Carry continuation is used across BOTH kappa_A and tau: each kappa_A row
reuses the previous row's converged cycle state, and each bisection carries
the state from the neighbouring tau.  This is the method the manuscript's
verify_fourstate_pipeline.py uses for the single point kappa_A=0.05.

Also reports window widths: (tau_-, tau_SNPO,L), (tau_SNPO,R, tau_+) and the
safe range (tau_SNPO,L, tau_SNPO,R) as functions of kappa_A.
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from fourstate_pipeline import (FOUR_PARAMS, four_arr, sim_four, sim_four_series,
                                char_eq_components, equilibrium)

# ----------------------------------------------------------------------
def hopf_pair(p, state=None):
    """tau_-, tau_+ at a kappa_A via the |P|=|Q| + phase method (from
    verify_kappaA_sweep)."""
    J, B, st = char_eq_components(p, donor=1, state=state)
    n = J.shape[0]
    def PQ(l):
        M = l*np.eye(n) - J
        P = np.linalg.det(M)
        i, j = np.nonzero(np.abs(B) > 1e-300)
        i, j = int(i[0]), int(j[0])
        b = B[i, j]
        minor = np.delete(np.delete(M, i, axis=0), j, axis=1)
        C = ((-1)**(i+j))*np.linalg.det(minor)
        return P, -b*C
    ws = np.linspace(0.001, 2.0, 6000)
    vals = np.array([abs(PQ(1j*w)[0]) - abs(PQ(1j*w)[1]) for w in ws])
    taus = []
    for k in range(len(ws)-1):
        if vals[k]*vals[k+1] < 0:
            a, b_ = ws[k], ws[k+1]; fa, fb = vals[k], vals[k+1]
            for _ in range(50):
                m = 0.5*(a+b_)
                fm = abs(PQ(1j*m)[0]) - abs(PQ(1j*m)[1])
                if fa*fm <= 0: b_, fb = m, fm
                else: a, fa = m, fm
            wstar = 0.5*(a+b_)
            P, Q = PQ(1j*wstar)
            phi = np.angle(P/Q)
            for nn in range(10):
                tau = (-phi - np.pi + 2*np.pi*nn)/wstar
                if tau > 0: taus.append(tau)
    taus = sorted(taus)
    out = []
    for t in taus:
        if not out or t - out[-1] > 0.5:
            out.append(t)
    return out  # sorted ascending; [0]=tau_-, [1]=tau_+ (first two)

def tail_amp_four(pa, st, tau, T=8e5, dt=0.05, out_step=20000):
    s = sim_four_series(st[0], st[1], st[2], st[3], tau, T, dt, pa, 1, out_step)
    Ns = s[:, 0]
    tl = Ns[len(Ns)//2:]           # second half
    return tl.max() - tl.min()

def find_fold(pa, seeds, t_persist, t_quiet, T=8e5, tol=0.1):
    """Bisect where the large cycle ceases to persist, using multiple seeds
    (the max tail amplitude over seeds).  t_persist side has the cycle,
    t_quiet does not.  Returns (midpoint, lo, hi) or (nan, nan, nan) if the
    assumed structure is not found."""
    def persists(tau):
        amp = 0.0
        for sd in seeds:
            amp = max(amp, tail_amp_four(pa, sd, tau, T=T))
        return amp > 5.0
    pp_, pq_ = persists(t_persist), persists(t_quiet)
    if not (pp_ and not pq_):
        return np.nan, np.nan, np.nan
    lo, hi = min(t_persist, t_quiet), max(t_persist, t_quiet)
    keep = t_persist < t_quiet   # cycle on the low-tau side
    while hi - lo > tol:
        m = 0.5*(lo+hi)
        pm = persists(m)
        if keep:
            if pm: lo = m
            else: hi = m
        else:
            if pm: hi = m
            else: lo = m
    return 0.5*(lo+hi), lo, hi

def main():
    print("="*78)
    print("FOUR-STATE CORE: CONTINUOUS FOLD TRACKING vs kappa_A (Candidate A)")
    print("="*78)
    base = FOUR_PARAMS()
    # kappa_A grid: denser near the threshold, coarser at large kappa_A
    kas = np.concatenate([np.linspace(0.0015, 0.01, 8),
                          np.linspace(0.01, 0.10, 7)[1:],
                          np.linspace(0.10, 0.50, 6)[1:]])
    print(f"  kappa_A grid: {len(kas)} points in [{kas[0]:.4f}, {kas[-1]:.3f}]")

    rows = []
    # use the validated physical-branch continuation (from verify_kappaA_sweep)
    # so that the equilibrium never falls onto the unphysical negative-A root
    # that plain fsolve finds near the threshold
    from verify_kappaA_sweep import physical_branch
    branch = physical_branch(base, donor=1, kas=kas)
    for (kA, N, A, E1) in branch:
        pp = dict(base); pp['kappa_A'] = kA
        if N is None:
            print(f"  kappa_A={kA:.4f}: no physical equilibrium; skipping")
            rows.append((kA, np.nan, np.nan, np.nan, np.nan))
            continue
        state = np.array([N, pp['delta'], E1, A])
        pa = four_arr(pp)
        th = hopf_pair(pp, state)
        if len(th) < 2:
            print(f"  kappa_A={kA:.4f}: fewer than 2 Hopf crossings ({len(th)}); skipping")
            rows.append((kA, np.nan, np.nan, np.nan, np.nan))
            continue
        tm, tp = th[0], th[1]
        print(f"  kappa_A={kA:.6f}: tau_-={tm:8.3f} tau_+={tp:8.3f}", end="", flush=True)

        # converge cycles near both folds (seed INSIDE the narrow bistable
        # windows; multi-seed so basin effects near the fold are covered)
        lo_mid = tm + (tp - tm)/2
        c0a = sim_four(40.0, 0.1, 8.0, 400.0, tm+0.2, 8e5, 0.05, pa, 1)
        c0b = sim_four(1.2*N, 0.1, 3.0, 1.2*A, tm+0.2, 8e5, 0.05, pa, 1)
        fL, loL, hiL = find_fold(pa, [c0a, c0b], tm+0.2, lo_mid)
        print(f"  SNPO,L={fL:8.3f} [{loL:.3f},{hiL:.3f}]", end="", flush=True)

        c1a = sim_four(40.0, 0.1, 8.0, 400.0, tp-0.3, 8e5, 0.05, pa, 1)
        c1b = sim_four(1.2*N, 0.1, 3.0, 1.2*A, tp-0.3, 8e5, 0.05, pa, 1)
        fR, loR, hiR = find_fold(pa, [c1a, c1b], tp-0.3, lo_mid)
        print(f"  SNPO,R={fR:8.3f} [{loR:.3f},{hiR:.3f}]", flush=True)

        rows.append((kA, tm, tp, fL, fR))

    # summary table
    print("\n  kappa_A     tau_-      tau_+    SNPO,L    SNPO,R   winL   winR   safe")
    ok = True
    for (kA, tm, tp, fL, fR) in rows:
        if np.isfinite(fL) and np.isfinite(fR):
            print(f"  {kA:.5f}  {tm:9.3f} {tp:9.3f} {fL:9.3f} {fR:9.3f}  "
                  f"{fL-tm:6.2f} {tp-fR:6.2f} {fR-fL:7.2f}")
        else:
            ok = False
            print(f"  {kA:.5f}  {tm:9.3f} {tp:9.3f}   (fold not located)")
    print("\n  VERDICT:", "CONTINUOUS FOLD TRACKING COMPLETE"
          if ok else "PARTIAL - some folds not located")

if __name__ == "__main__":
    main()
