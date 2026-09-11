"""
palc_through_folds.py
=====================

Robust pseudo-arclength continuation (Newton corrector on the full augmented
system, jax analytic Jacobian) to carry the corrected core's periodic-orbit
branches THROUGH their fold regions, answering:

  Q1: does the small-amplitude unstable branch genuinely fold at tau ~ 5.587
      (tau locally maximised, then decreasing), or was that a continuation
      stall?
  Q2: does the stable large-amplitude branch have an unstable continuation
      past its termination ~5.575, and if so does it connect to the small
      branch (one SNPO) or remain a separate fold (two folds)?

The system: collocation residual with tau as a free unknown (3M+2 unknowns),
arclength constraint, Newton with jax analytic Jacobian. The corrector stays
nonsingular through a fold because of the arclength row, so tau can be
followed past a turning point.

IMPORTANT: the Z-floor (max(0, softplus - ln2/k + delta)) is INACTIVE on both
branches (inner >= 0 everywhere; delta = ln2/k), so the floor sharpness does
not affect the dynamics; the earlier "fold at 5.468" attribution to floor
smoothing was incorrect and is corrected to "continuation artifact".
"""
import numpy as np
import jax
import jax.numpy as jnp
from jax import config
config.update("jax_enable_x64", True)
from scipy.signal import find_peaks
from continuation3 import lm_corrector
from corrected_core_common import PARAMS_A as PARAMS_CC
from collocation_corrected import make_residual_fn, newton_corrector
from palc_corrected import make_residual_free_tau

M = 257
FLOOR = 10000.0

def collocate_fixed_tau(v_seed, tau, tol=1e-11, maxit=500):
    N = v_seed[0:M]; pi = int(np.argmax(N)); pv = float(N[pi])
    rf, _, _ = make_residual_fn(M, PARAMS_CC, pi, pv, floor_sharpness=FLOOR)
    v, ok, rn = lm_corrector(lambda x: rf(x, tau), v_seed, tol=tol, maxit=maxit, lam0=1e-8)
    return v, ok, rn

def palc_continuation(w0, w1, ds0=0.02, n_steps=400, tau_lo=5.0, tau_hi=5.75,
                      verbose_every=5):
    """w = [N,Z,E,T,tau] (3M+2). Continues from the two initial points w0,w1."""
    res_free = make_residual_free_tau(M, PARAMS_CC, 0, 0.0, floor_sharpness=FLOOR)
    # NOTE: pin index/value inside res_free are fixed at construction; re-pin per
    # point by rebuilding when needed. For now use the seed's pin.
    N = w0[0:M]; pin_idx = int(np.argmax(N)); pin_val = float(N[pin_idx])
    res_free = make_residual_free_tau(M, PARAMS_CC, pin_idx, pin_val, floor_sharpness=FLOOR)

    tangent = w1 - w0
    tangent = tangent / np.linalg.norm(tangent)
    w_prev = w1.copy()
    w_prev2 = w0.copy()
    ds = ds0
    hist = []
    # use the secant-based arclength constraint
    for it in range(n_steps):
        v_predictor = w_prev + ds * tangent
        def augmented(vv):
            base = res_free(vv)                       # 3M+1
            arc = jnp.dot(jnp.array(tangent), vv - jnp.array(v_predictor)) - ds
            return jnp.concatenate([base, jnp.array([arc])])   # 3M+2
        w_new, ok, rn = newton_corrector(augmented, v_predictor, tol=1e-9, maxit=40)
        if not ok or rn > 1e-6:
            ds *= 0.5
            if ds < 1e-6:
                print(f"  [stall] iter {it}, ds={ds:.1e}, res={rn:.1e}")
                break
            continue
        tau_n = float(w_new[3*M+1]); amp_n = float(w_new[0:M].max()-w_new[0:M].min())
        T_n = float(w_new[3*M])
        hist.append((tau_n, amp_n, T_n))
        # new tangent from secant
        nt = w_new - w_prev
        if np.linalg.norm(nt) > 1e-12:
            tangent = nt / np.linalg.norm(nt)
        w_prev2 = w_prev; w_prev = w_new
        ds = min(ds * 1.15, 0.05)
        if it % verbose_every == 0 or not (tau_lo < tau_n < tau_hi):
            print(f"  iter {it}: tau={tau_n:.5f} amp={amp_n:.4f} T={T_n:.2f} res={rn:.1e}")
        # stop when tau clearly turned around (fold) and came back down,
        # or when it exits the window
        if len(hist) > 4:
            taus_arr = np.array([h[0] for h in hist])
            imax = np.argmax(taus_arr)
            if imax > 2 and imax < len(taus_arr)-2 and taus_arr[-1] < taus_arr[imax]-1e-4:
                print(f"  [FOLD] tau max {taus_arr[imax]:.5f} at step {imax}, turned back to {taus_arr[-1]:.5f}")
                break
        if tau_n > tau_hi or tau_n < tau_lo:
            print(f"  [EXIT] iter {it}: tau={tau_n:.5f}")
            break
    return np.array(hist)

def seed_small_branch(tau_seed=5.55):
    """Seed the small-unstable branch from the checkpoint, collocated at tau_seed."""
    ck = np.load('/home/user/unstable_clean_ckpt.npz')
    taus = ck['taus']; states = ck['states']
    i0 = np.argmin(np.abs(taus - tau_seed))
    v = states[i0].copy()
    # collocate at tau_seed with sharp floor
    v, ok, rn = collocate_fixed_tau(v, tau_seed)
    return v, ok, rn

def seed_stable_branch(tau_seed=5.57):
    """Seed the stable large cycle from simulation, collocated at tau_seed."""
    from elevation_solvers import PARAMS_A, params_arr, simulate_three_series
    pA = PARAMS_A(); pa = params_arr(pA)
    s = simulate_three_series(40.0, 0.1, 8.0, tau_seed, 400000.0, 0.05, pa, True, 5)
    Ns, Zs, Es = s[:,0], s[:,1], s[:,2]
    pk, _ = find_peaks(Ns, distance=400)
    period = np.median(np.diff(pk))*0.25
    ppp = int(round(period/0.25)); start = pk[-1]-ppp
    idxs = (start + np.arange(M)*(ppp/M)).astype(int)
    if idxs.max() >= len(Ns):
        s = simulate_three_series(40.0,0.1,8.0,tau_seed,400000.0+period+200,0.05,pa,True,5)
        Ns,Zs,Es=s[:,0],s[:,1],s[:,2]; pk,_=find_peaks(Ns,distance=400); start=pk[-1]-ppp
        idxs=(start+np.arange(M)*(ppp/M)).astype(int)
    v = np.concatenate([Ns[idxs], Zs[idxs], Es[idxs], [period]])
    v, ok, rn = collocate_fixed_tau(v, tau_seed)
    return v, ok, rn
