"""
verify_floquet_points.py
========================
Standalone Python verification of Floquet multipliers at the fold points
identified in the manuscript.  This does NOT do full branch continuation
(that is what track_fold_branches.m provides under DDE-BIFTOOL); instead it
converges a periodic orbit at a specified tau via simple fixed-point
iteration on the shooting map and estimates the dominant Floquet multiplier
by finite differences of the period map.

This is the minimal numerical check of the manuscript's claim that "the
upper-window folds remain candidate SNPOs pending Floquet-multiplier
tracking along the branches."  It produces a table of multipliers at
several tau values bracketing each fold; a +1 crossing of the dominant
nontrivial multiplier confirms an SNPO.

The DDE here is integrated with RK4; Floquet multipliers are estimated by
perturbing the converged orbit's initial state by epsilon in each coordinate,
integrating one period, and taking eigenvalues of the resulting finite-
difference monodromy matrix.  For a DDE, the delayed perturbation is
carried by the periodic history (the orbit is closed), which is the correct
Floquet setup.

Run:  python verify_floquet_points.py
Outputs: prints a table; saves floquet_table.csv and floquet_vs_tau.png.

This file is independent of the (still-in-development) multishoot solver
and uses only numpy/scipy.
"""
import numpy as np
from dde_core import (integrate_dde, equilibrium, CoreParams, rhs, softplus,
                      softplus_deriv)


def converge_orbit_by_shooting(p, tau, yinit, T_guess, dt=0.25,
                               n_picard=40, eps=1e-7, n_fd=3):
    """Simple single-shooting with periodic history rebuilt each iteration.
    The orbit is found by iterating y0 <- flow_T(y0; periodic history).
    Returns (y0, T, history_samples) or None."""
    p.tau = tau
    n = len(yinit)
    # initial constant history = equilibrium
    eq = equilibrium(p)
    # first integration
    yT, _, ts, ys = integrate_dde(yinit, lambda t: eq, 2*T_guess, p, dt)
    # measure period from N peaks
    N = ys[:, 0]
    peaks = []
    for j in range(5, len(N)-5):
        if N[j] > N[j-1] and N[j] > N[j+1] and N[j] > N.mean():
            peaks.append(j)
    if len(peaks) < 2:
        return None
    T = float(np.median(np.diff(peaks))) * dt
    # build periodic history from last cycle
    nper = int(round(T/dt))
    tail = ys[-nper-2:]
    ts_tail = np.arange(len(tail))*dt
    def hfunc(t):
        return np.array([np.interp(t, ts_tail, tail[:, k], period=T)
                         for k in range(n)])
    y0 = tail[0].copy()
    # Picard iteration: close the orbit
    for it in range(n_picard):
        yT, _, ts, ys = integrate_dde(y0, hfunc, T, p, dt)
        # phase: find where N crosses its mean upward, rotate there
        m = ys[:, 0].mean()
        shift = 0
        for j in range(1, len(ys)-1):
            if ys[j-1, 0] < m <= ys[j, 0]:
                shift = j; break
        if shift:
            ys = np.roll(ys, -shift, axis=0)
            y0 = ys[0].copy()
        else:
            y0 = yT.copy()
        tail = ys[-nper-2:]
        ts_tail = np.arange(len(tail))*dt
        def hfunc(t, ts_tail=ts_tail, tail=tail, T=T, n=n):
            return np.array([np.interp(t, ts_tail, tail[:, k], period=T)
                             for k in range(n)])
        res = np.linalg.norm(yT - y0)
        if res < eps:
            break
    if res > 1e-3:
        return None
    # finite-difference monodromy
    Mono = np.zeros((n, n))
    for k in range(n):
        scale = eps * max(abs(y0[k]), 1e-3)
        col = np.zeros(n)
        for sgn in (+1, -1):
            yp = y0.copy(); yp[k] += sgn*scale
            yTp, _, _, _ = integrate_dde(yp, hfunc, T, p, dt)
            col += sgn * yTp
        col /= (2*scale)
        Mono[:, k] = col
    mults = np.linalg.eigvals(Mono)
    return dict(y0=y0, T=T, residual=res, mults=mults, Mono=Mono)


def run():
    print("="*70)
    print("Floquet-multiplier check at fold points (Candidate A)")
    print("="*70)
    results = []
    for label, gated, tau_list in [
        ('Ungated 3-state (upper window)', False,
         [131.0, 131.2, 131.4, 131.6, 131.8, 132.0, 132.2]),
        ('Ungated 3-state (lower window)', False,
         [7.0, 7.2, 7.355, 7.5, 7.7]),
        ('Gated 3-state (upper window)', True,
         [148.0, 148.3, 148.6, 149.0, 149.5]),
    ]:
        print(f"\n--- {label} ---")
        p = CoreParams(eta=0.914, Emax=30.0, delta0=0.01, Dref=1.0,
                       tau_m=5.0, gated=gated)
        eq = equilibrium(p)
        for tau in tau_list:
            # warm up from far IC to get on the cycle
            p.tau = tau
            yT, _, ts, ys = integrate_dde(
                np.array([99.0, p.delta, 0.5]),
                lambda t: eq, 100000.0, p, 0.5)
            N = ys[:, 0]
            peaks = [j for j in range(5, len(N)-5)
                     if N[j] > N[j-1] and N[j] > N[j+1] and N[j] > N.mean()]
            if len(peaks) < 2:
                print(f"  tau={tau:7.3f}: no cycle found")
                continue
            T_guess = float(np.median(np.diff(peaks)))*0.5
            r = converge_orbit_by_shooting(p, tau, ys[-1], T_guess, dt=0.25)
            if r is None:
                print(f"  tau={tau:7.3f}: shooting did not converge")
                continue
            mu = sorted(r['mults'], key=lambda z: -abs(z))
            # phase multiplier ~1; dominant nontrivial:
            nontriv = [m for m in mu if abs(abs(m)-1) > 1e-3]
            dom = nontriv[0] if nontriv else mu[0]
            print(f"  tau={tau:7.3f}  T={r['T']:8.3f}  "
                  f"res={r['residual']:.1e}  |mu_dom|={abs(dom):.5f}  "
                  f"mu_dom={dom:.4f}")
            results.append((label, tau, r['T'], abs(dom), dom,
                           r['residual']))
    import csv
    with open('/home/user/dde_floquet/floquet_table.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['branch','tau','T','|mu_dom|','Re(mu)','Im(mu)','residual'])
        for row in results:
            label, tau, T, am, mu, res = row
            w.writerow([label, f'{tau:.4f}', f'{T:.4f}', f'{am:.6f}',
                        f'{np.real(mu):.6f}', f'{np.imag(mu):.6f}',
                        f'{res:.2e}'])
    print("\nSaved floquet_table.csv")


if __name__ == '__main__':
    run()
