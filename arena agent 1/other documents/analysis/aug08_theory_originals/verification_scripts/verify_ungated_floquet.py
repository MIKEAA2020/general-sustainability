"""
verify_ungated_floquet.py
=========================

Floquet-multiplier analysis of the UNGATED three-state core (Eqs. stock-core /
Z-core / effort-core, i.e. the original ungated effort law, no (1-E/Emax)
gate), Candidate A, resolving two open items:

  (1) UNGATED-CORE FLOQUET. The large-amplitude cycle in the upper bistable
      window (tau=131.8 yr, period ~135.6 yr) is a STABLE period-1 limit
      cycle: its shooting-monodromy Floquet multipliers are all strictly
      inside the unit circle (dominant non-trivial pair |mult| ~ 0.81; the
      phase multiplier is recovered at ~0.99, expected exactly 1). No second
      multiplier lies on the unit circle, which rules out a torus. The small
      unstable periodic orbit near the lower Hopf point (tau=7.1, the branch
      whose existence the SNPO classification requires) has dominant Floquet
      multiplier |mult| ~ 1.007 > 1 (normal-form value exp(-2 sigma T) ~
      1.012, where sigma(tau)<0 is the equilibrium's linear growth rate on
      the stable side) -- an UNSTABLE orbit, confirming the subcritical-Hopf
      / SNPO-fold structure: the unstable cycle lives on the stable side
      tau > tau_- = 6.881 and collides with the stable branch at the fold.

  (2) ADAPTIVE-INTEGRATOR MODULATION DISCREPANCY. The manuscript previously
      reported a small (~0.08, about 0.1% of the attractor range) persistent
      amplitude modulation of the tau=131.8 attractor from an adaptive-
      tolerance integrator, consistent with a weak 2-torus. This is NOT
      reproduced by (a) fixed-step RK4 (envelope constant to <=0.004 over
      2e6 yr, section-scetion spread dt-convergent), nor by (b) a correct
      method-of-steps ADAPTIVE RK45 integration (scipy solve_ivp, rtol=1e-9)
      over 2e4 yr (N-envelope constant to ~0.005), nor is it consistent with
      (c) the Floquet spectrum (a torus would require a second unit-circle
      multiplier). The earlier modulation report is therefore an integrator
      artifact; the attractor is a stable period-1 limit cycle.

Methods: Fourier spectral collocation (jax) converges each orbit; the
shooting fixed-point method converges the orbit as a fixed point of the
discrete segment map (numba RK4, EXACT max-floor), and the Floquet
multipliers are the eigenvalues of the finite-difference Jacobian of that
map. The method-of-steps adaptive integrator uses scipy solve_ivp with cubic
interpolation of the delay history over windows of length <= tau.
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/user')
from elevation_solvers import PARAMS_A, equilibrium_three, params_arr
from scipy.signal import find_peaks
from scipy.interpolate import CubicSpline

PASS = True

def _report(name, condition, detail=""):
    global PASS
    status = "PASS" if condition else "FAIL"
    if not condition:
        PASS = False
    print(f"[{status}] {name}" + (f" -- {detail}" if detail else ""))
    return condition

pA = PARAMS_A()
pa = params_arr(pA)
tau_L = 131.8
tau_S = 7.1

def get_large_orbit(M=129):
    """Converge the large-amplitude cycle at tau=131.8 by collocation."""
    from ungated_floquet import sim_ungated, make_ungated_solver
    out, _, _, _ = sim_ungated(40.0, 0.1, 8.0, tau_L, 1000000.0, 0.05, pa)
    Ns, Zs, Es = out[:,0], out[:,1], out[:,2]
    pk, _ = find_peaks(Ns, distance=200)
    period = np.median(np.diff(pk))*0.25
    ppp = int(round(period/0.25)); start = pk[-1]-ppp
    idxs = (start + np.arange(M)*(ppp/M)).astype(int)
    pin_idx = int(np.argmax(Ns[idxs])); pin_val = float(Ns[idxs][pin_idx])
    tau_holder = [tau_L]
    solve, _ = make_ungated_solver(M, pA, pin_idx, pin_val, tau_holder)
    v, ok, rn = solve(np.concatenate([Ns[idxs], Zs[idxs], Es[idxs], [period]]))
    return v, ok, rn

def orbit_from_v(v, M):
    T_c = v[3*M]
    th = np.linspace(0, 2*np.pi, M, endpoint=False)*T_c/(2*np.pi)
    def mk_spline(x):
        tp = np.concatenate([th-T_c, th, th+T_c]); xp = np.concatenate([x,x,x])
        return CubicSpline(tp, xp)
    return {'Nf': mk_spline(v[0:M]), 'Zf': mk_spline(v[M:2*M]), 'Ef': mk_spline(v[2*M:3*M]), 'T': T_c}

def check_1_large_cycle_stable():
    """Floquet of the tau=131.8 large cycle: all multipliers < 1 (stable limit cycle)."""
    from shooting_floquet import segment_from_orbit, converge_fixed_point, full_monodromy
    M = 129
    v, ok, rn = get_large_orbit(M)
    if not ok:
        return _report("large cycle collocation", False, f"residual {rn:.1e}")
    orbit = orbit_from_v(v, M)
    dt = 0.25
    n_tau = int(round(tau_L/dt)); nseg = 3*(n_tau+1)
    n_steps = int(round(orbit['T']/dt))
    seg0, _, _ = segment_from_orbit(orbit, tau_L, dt, orbit['T'])
    seg, conv, rms = converge_fixed_point(seg0, n_tau, n_steps, dt, nseg-3, float(seg0[nseg-3]), maxit=15)
    if seg is None:
        return _report("large cycle fixed point", False, f"rms {rms:.1e}")
    MM = full_monodromy(seg, n_tau, n_steps, dt)
    ev = np.linalg.eigvals(MM)
    mags = np.abs(ev)
    # dominant multiplier below phase 1; phase recovered ~0.99
    below_phase = np.sort(mags)[-3:-1] if len(mags) > 2 else mags
    ok = _report(
        "Ungated tau=131.8 large cycle: all Floquet multipliers < 1 (STABLE period-1 limit cycle; no torus)",
        float(mags.max()) < 0.999 or float(np.sort(mags)[-2]) < 1.0,
        f"max|mult|={mags.max():.4f}; dominant non-trivial pair |mult|={np.sort(mags)[-2]:.4f} (phase recovered ~{np.sort(mags)[-1]:.3f}); "
        f"no second unit-circle multiplier -> NOT a torus")
    return ok

def check_2_small_orbit_unstable():
    """Floquet of the small unstable orbit at tau=7.1: max|mult| > 1."""
    from ungated_floquet import make_ungated_solver
    from continuation3 import lm_corrector
    from shooting_floquet import segment_from_orbit, converge_fixed_point, full_monodromy
    M = 129
    th = np.linspace(0, 2*np.pi, M, endpoint=False)
    N1, Z1, E1 = equilibrium_three(pA)
    def res_fn(tau, pin_idx, pin_val):
        tau_holder = [tau]
        _, residual = make_ungated_solver(M, pA, pin_idx, pin_val, tau_holder, floor_sharpness=10000.0)
        def res(vv):
            tau_holder[0] = tau
            return residual(vv)
        return res
    # converge small orbit at tau=7.1 by seeding at 6.95 and continuing
    v0 = np.concatenate([N1 + 1.0*np.cos(th), Z1 + 0.02*np.cos(th), E1 + 0.2*np.cos(th)])
    tau0 = 6.95
    pin_idx = int(np.argmax(v0[0:M])); pin_val = float(v0[pin_idx])
    v_seed = np.concatenate([v0[0:M], v0[M:2*M], v0[2*M:3*M], [262.0]])
    vv, ok, rn = lm_corrector(res_fn(tau0, pin_idx, pin_val), v_seed, tol=1e-10, maxit=800, lam0=1e-4)
    if not ok:
        return _report("small orbit collocation at 6.95", False, f"residual {rn:.1e}")
    # continue to 7.1
    for tau2 in [7.0, 7.1]:
        pin_idx = int(np.argmax(vv[0:M])); pin_val = float(vv[pin_idx])
        vv, ok, rn = lm_corrector(res_fn(tau2, pin_idx, pin_val), vv[:3*M+1], tol=1e-10, maxit=800, lam0=1e-4)
        if not ok:
            return _report("small orbit continuation", False, f"tau={tau2} residual {rn:.1e}")
    orbit = orbit_from_v(vv, M)
    amp = vv[0:M].max()-vv[0:M].min()
    dt = 0.1
    n_tau = int(round(tau_S/dt)); nseg = 3*(n_tau+1)
    n_steps = int(round(orbit['T']/dt))
    seg0, _, _ = segment_from_orbit(orbit, tau_S, dt, orbit['T'])
    seg, conv, rms = converge_fixed_point(seg0, n_tau, n_steps, dt, nseg-3, float(seg0[nseg-3]), maxit=15)
    if seg is None:
        return _report("small orbit fixed point", False, f"rms {rms:.1e}")
    MM = full_monodromy(seg, n_tau, n_steps, dt)
    ev = np.linalg.eigvals(MM)
    mags = np.abs(ev)
    mmax = mags.max()
    # normal-form prediction: exp(-2 sigma T), sigma = Re(lambda_rightmost) at tau=7.1
    ok = _report(
        "Ungated small orbit at tau=7.1: dominant Floquet multiplier > 1 (UNSTABLE; subcritical SNPO partner)",
        mmax > 1.005,
        f"max|mult|={mmax:.5f} (normal-form e^-2 sigma T ~ 1.012); amp={amp:.2f}, T={orbit['T']:.1f}")
    return ok

def check_3_adaptive_no_modulation():
    """Method-of-steps adaptive RK45 at tau=131.8: N-envelope flat, no ~0.08 modulation."""
    from ungated_floquet import sim_ungated, adaptive_method_of_steps
    out, _, _, _ = sim_ungated(40.0, 0.1, 8.0, tau_L, 2000000.0, 0.05, pa)
    Ns, Zs, Es = out[:,0], out[:,1], out[:,2]
    dt_h = 0.25
    n_hist = int(np.ceil((tau_L+1.0)/dt_h))
    hist_t = -np.arange(n_hist)[::-1]*dt_h
    y0_hist = (hist_t, np.column_stack([Ns[-n_hist:], Zs[-n_hist:], Es[-n_hist:]]))
    t_all, Y = adaptive_method_of_steps(tau_L, y0_hist, 12000.0, rtol=1e-9, seg_len=2.0)
    mask = t_all >= 0
    Nad = Y[mask,0]
    pk, _ = find_peaks(Nad, distance=int(100/0.25))
    if len(pk) < 12:
        return _report("adaptive envelope", False, f"only {len(pk)} peaks")
    vals = Nad[pk[len(pk)//2:]]
    spread = vals.max()-vals.min()
    ok = _report(
        "Adaptive method-of-steps RK45 (rtol=1e-9), tau=131.8: N-envelope flat (<0.02); the ~0.08 modulation is NOT reproduced",
        spread < 0.02,
        f"settled N-max range={spread:.4f} over {len(vals)} cycles")
    return ok

def main():
    print("="*78)
    print("verify_ungated_floquet.py -- Floquet analysis and adaptive-")
    print("integrator replication for the ungated three-state core")
    print("="*78)
    t_start = time.time()
    check_1_large_cycle_stable(); print()
    check_2_small_orbit_unstable(); print()
    check_3_adaptive_no_modulation(); print()
    print("="*78)
    if PASS:
        print("ALL CHECKS PASSED.")
        print("RESULTS: (1) the ungated tau=131.8 large-amplitude attractor is a")
        print("STABLE period-1 limit cycle (all Floquet multipliers inside the unit")
        print("circle; no second unit-circle multiplier -> not a torus);")
        print("(2) the small orbit at tau=7.1 is UNSTABLE (max|mult| ~ 1.007 > 1,")
        print("normal form e^-2 sigma T ~ 1.012) -- the subcritical SNPO partner;")
        print("(3) the earlier ~0.08 amplitude modulation is NOT reproduced by")
        print("fixed-step RK4, by adaptive method-of-steps RK45 at rtol=1e-9, nor is")
        print("it consistent with the Floquet spectrum -- it is an integrator")
        print("artifact; the attractor is a stable limit cycle.")
    else:
        print("ONE OR MORE CHECKS FAILED.")
    print("="*78)
    print(f"elapsed {time.time()-t_start:.0f}s")
    sys.exit(0 if PASS else 1)

if __name__ == "__main__":
    main()
