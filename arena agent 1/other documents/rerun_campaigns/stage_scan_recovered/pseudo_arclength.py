"""
pseudo_arclength.py
===================
Pseudo-arclength continuation for periodic orbits of the manuscript's DDE,
built on top of dde_core.py's single-shooting machinery.

Why this is needed
------------------
Natural-parameter continuation (continue_branch in dde_core.py) steps tau and
solves the shooting system at each new tau using the previous orbit as the
initial guess.  This STALLS at a fold of periodic orbits (saddle-node / SNPO):
past the fold, the stable branch turns back and there is no solution for tau
beyond it, so a fixed-tau Newton solve has nothing to converge to.

Pseudo-arclength continuation solves this by treating tau as an additional
unknown and stepping along the solution curve in (y0, T, tau) space:

    G(y0, T, tau) = 0      shooting residual (periodic orbit condition)
    N(y0, T, tau) = 0      pseudo-arclength constraint:
                            <delta_u, tangent> - ds = 0
where delta_u = u - u_prev and tangent is the unit tangent to the branch.

This lets the continuation round the fold and onto the unstable branch,
which is exactly what is needed to close the manuscript's open items:
tracking the small-amplitude unstable branch born at the subcritical Hopf
point, and demonstrating (or refuting) the sqrt(tau - tau_SNPO) collision
scaling at the fold.

Method
------
* Unknown vector u = (y0[0..n-1], T, tau)   (dimension n+2)
* Shooting residual r(u): integrate the DDE over one period T with periodic
  history built from the orbit, return yT - y0, plus a phase condition
  anchoring one component of y0 (to fix the phase).
* Jacobian by finite differences (robust, no analytic derivatives of the
  shooting map needed; the DDE is already integrated with RK4).
* Keller pseudo-arclength: predictor u_pred = u + ds * tangent;
  Newton corrector with the constraint <u - u_pred, tangent> = 0.

The phase condition is important: without it the system is underdetermined
(the phase of the orbit is a free direction).  We anchor y0[phase_idx] to a
reference value (e.g., N at t=0 crossing a fixed level).

History handling
----------------
The delayed term needs Z(t-tau) on [0, T].  We build a periodic history from
the current orbit guess (the orbit's own tail on [T-tau, T] wrapped to
[-tau, 0]) and iterate it to consistency (the orbit is closed, so the
history is the orbit itself shifted by T).

Usage
-----
    from pseudo_arclength import arc_length_continue
    branch = arc_length_continue(
        y0_start, T_start, tau_start, p, dt,
        ds=0.05, n_steps=120, phase_idx=0, phase_val=..., direction='forward')
    # branch: list of dicts with keys y0, T, tau, residual, mults
"""
import numpy as np
from dde_core import (CoreParams, integrate_dde, rhs, equilibrium,
                      _periodic_history, softplus)


# ---------------------------------------------------------------------------
# Periodic history + one-period integration for an orbit guess (y0, T, tau)
# ---------------------------------------------------------------------------
def integrate_orbit(y0, T, tau, p, dt, history_seed=None, gh_iter=2):
    """Integrate one period of the DDE from y0 with a periodic history.

    Returns (yT, ts, ys) where ys is the on-grid trajectory over [0,T].
    The history for the delayed term is built from the orbit's own tail
    (periodic wrap) and iterated gh_iter times for consistency.
    """
    p.tau = tau
    n = len(y0)
    if history_seed is None:
        # Build a periodic history from a linear-in-time guess?  Better: use
        # the equilibrium as the initial history, then let the iteration
        # refine it.  For a first integration we can use a constant history
        # = equilibrium (the orbit guess is close enough that one pass
        # suffices to bootstrap).
        eq = equilibrium(p)
        def hfunc0(t):
            return eq
        ht0 = np.linspace(-tau, 0, 32)
        hv0 = np.tile(eq, (len(ht0), 1))
    else:
        ht0, hv0 = history_seed
        def hfunc0(t, ht=ht0, hv=hv0, n=n):
            return np.array([np.interp(t, ht, hv[:, j], period=tau + 1e-9)
                             for j in range(n)])

    # First pass: integrate with the seed history
    yT, _, ts, ys = integrate_dde(y0, hfunc0, T, p, dt)
    # Refine: rebuild the periodic history from the integrated trajectory
    for _ in range(gh_iter):
        # Take the last tau-worth of ys as the history on [-tau, 0]
        # (periodic wrap: ys at time t, history at t-tau for t in [0,T])
        ht = ts - T          # shift so that [-tau,0] covers [T-tau, T]
        # Actually: history on [-tau,0] should be y(T + s), s in [-tau,0]
        # = ys at times T+s.  We'll sample ys at those times via interp.
        def hfunc(t, ts=ts, ys=ys, T=T, n=n):
            return np.array([np.interp(t + T, ts, ys[:, j], period=T)
                             for j in range(n)])
        yT, _, ts, ys = integrate_dde(y0, hfunc, T, p, dt)
    return yT, ts, ys, hfunc


def orbit_history(ts, ys, T, tau):
    """Build a periodic history function from a converged orbit over [0,T]."""
    n = ys.shape[1]
    def hfunc(t, ts=ts, ys=ys, T=T, n=n):
        return np.array([np.interp(t + T, ts, ys[:, j], period=T)
                         for j in range(n)])
    ht = np.linspace(-tau, 0, 64)
    hv = np.array([hfunc(tt) for tt in ht])
    return hfunc, ht, hv


# ---------------------------------------------------------------------------
# Shooting residual and its (finite-difference) Jacobian
# ---------------------------------------------------------------------------
def shooting_residual(u, p, dt, phase_idx=0, phase_val=None):
    """Residual of the periodic-orbit shooting system.

    u = (y0[0..n-1], T, tau)
    Returns array of length n+1:
      [0..n-1] : yT - y0   (periodic orbit condition)
      [n]      : y0[phase_idx] - phase_val   (phase condition)
    """
    n = len(u) - 2
    y0 = u[:n]
    T = u[n]
    tau = u[n + 1]
    p.tau = tau
    yT, ts, ys, hfunc = integrate_orbit(y0, T, tau, p, dt)
    res = np.concatenate([yT - y0, [y0[phase_idx] - (phase_val if phase_val is not None else y0[phase_idx])]])
    return res, (ts, ys, hfunc)


def jacobian_shooting(u, p, dt, phase_idx=0, phase_val=None, eps=1e-6):
    """Finite-difference Jacobian of the shooting residual w.r.t. (y0, T, tau)."""
    n = len(u) - 2
    m = n + 1
    J = np.zeros((m, n + 2))
    res0, _ = shooting_residual(u, p, dt, phase_idx, phase_val)
    for i in range(n + 2):
        e = eps * max(abs(u[i]), 1e-4)
        up = u.copy(); up[i] += e
        um = u.copy(); um[i] -= e
        resp, _ = shooting_residual(up, p, dt, phase_idx, phase_val)
        resm, _ = shooting_residual(um, p, dt, phase_idx, phase_val)
        J[:, i] = (resp - resm) / (2 * e)
    return J, res0


# ---------------------------------------------------------------------------
# Pseudo-arclength continuation
# ---------------------------------------------------------------------------
def arc_length_continue(y0_start, T_start, tau_start, p, dt,
                        ds=0.05, n_steps=120, phase_idx=0, phase_val=None,
                        direction='forward', tol=1e-7, maxit=40,
                        verbose=False, eps_jac=1e-6, M_floquet=8,
                        use_multishoot_floquet=True):
    """Pseudo-arclength continuation of a periodic orbit in tau.

    Returns a list of branch points (dicts with keys y0, T, tau, residual,
    multipliers).  The branch is followed past folds (which natural
    parameter continuation cannot do).
    """
    if phase_val is None:
        phase_val = float(y0_start[phase_idx])
    n = len(y0_start)

    # --- Build the initial point, verify it is a solution ---
    u0 = np.concatenate([y0_start, [T_start, tau_start]])
    res0, _ = shooting_residual(u0, p, dt, phase_idx, phase_val)
    print(f"[init] |res| = {np.linalg.norm(res0):.3e}  "
          f"(should be small if y0_start/T_start is an orbit)")
    # If the start is not a perfect orbit, correct it first (Newton with no
    # arclength constraint, i.e., solve G(u)=0 with phase condition).
    if np.linalg.norm(res0) > 1e-6:
        u0 = _newton_fix(u0, p, dt, phase_idx, phase_val, maxit=30, tol=1e-9)
        res0, _ = shooting_residual(u0, p, dt, phase_idx, phase_val)
        print(f"[init-fix] |res| = {np.linalg.norm(res0):.3e}")

    # --- Initial tangent: differencing two nearby solutions, or FD of G ---
    # For the first step, compute the tangent as the null direction of the
    # Jacobian [dG/du] (the branch direction).  G is (n+1) x (n+2); its
    # null space is 1-dim -> the tangent.
    J0, _ = jacobian_shooting(u0, p, dt, phase_idx, phase_val, eps_jac)
    # Null vector of J0 (dG/du) via SVD
    U, S, Vt = np.linalg.svd(J0)
    tangent = Vt[-1]                      # right singular vector for smallest S
    # Orient along 'direction' by the tau-component of the tangent.
    # Note: the branch curve's tau-direction can flip at a fold; for the
    # FIRST step we just want a deterministic choice consistent with
    # 'direction' (increasing tau = 'forward').
    tau_comp = tangent[-1]
    if direction == 'forward' and tau_comp < 0:
        tangent = -tangent
    if direction == 'backward' and tau_comp > 0:
        tangent = -tangent
    tangent = tangent / np.linalg.norm(tangent)

    branch = []
    u = u0.copy()
    tangent_prev = tangent.copy()
    hist_seed = None

    for step in range(n_steps):
        # --- Predictor: u_pred = u + ds * tangent ---
        u_pred = u + ds * tangent

        # --- Corrector: Newton with pseudo-arclength constraint ---
        u_new, tangent_new, res_final, ok = _arclength_newton(
            u, u_pred, tangent, p, dt, phase_idx, phase_val, ds,
            maxit=maxit, tol=tol, eps_jac=eps_jac)
        if not ok:
            if verbose:
                print(f"[step {step}] arclength Newton failed (res={res_final:.2e}); "
                      f"halving ds")
            ds *= 0.5
            if ds < 1e-6:
                print(f"[step {step}] ds too small; stopping")
                break
            continue

        u = u_new
        tangent = tangent_new

        # --- Record ---
        y0 = u[:n]; T = u[n]; tau = u[n + 1]
        # multipliers: use the multishoot Jacobian monodromy (correct DDE
        # Floquet, includes history coupling) by default
        if use_multishoot_floquet:
            try:
                mults = _floquet_multishoot(u, p, dt, M=M_floquet,
                                            eps=eps_jac)
            except Exception:
                mults = _floquet_at(u, p, dt, phase_idx, phase_val, eps_jac)
        else:
            mults = _floquet_at(u, p, dt, phase_idx, phase_val, eps_jac)
        branch.append(dict(y0=y0, T=T, tau=tau, residual=res_final,
                           multipliers=mults))
        if verbose:
            dom = _dominant_nontrivial(mults)
            print(f"[step {step:3d}] tau={tau:8.4f}  T={T:8.3f}  "
                  f"|mu_dom|={abs(dom):.5f}  res={res_final:.1e}")

        # Adaptive step control: grow ds if converged fast
        if step % 5 == 4 and res_final < tol * 10:
            ds = min(ds * 1.2, 0.5)

    return branch


def _arclength_newton(u_prev, u_pred, tangent, p, dt, phase_idx, phase_val,
                      ds, maxit=40, tol=1e-8, eps_jac=1e-6):
    """Newton corrector for pseudo-arclength continuation.

    Solve for u such that:
        G(u) = 0              (shooting residual, length n+1)
        <u - u_pred, tangent> = 0   (arclength constraint)
    The system is (n+2) equations in (n+2) unknowns.
    """
    n = len(u_prev) - 2
    u = u_pred.copy()
    # Jacobian of [G; N] where N = <u-u_pred, tangent>
    for it in range(maxit):
        res, _ = shooting_residual(u, p, dt, phase_idx, phase_val)
        # Build full Jacobian: [JG (n+1 x n+2); tangent (1 x n+2)]
        Jfull = np.zeros((n + 2, n + 2))
        Jfull[:n + 1, :] = jacobian_shooting(u, p, dt, phase_idx, phase_val,
                                             eps_jac)[0]
        Jfull[n + 1, :] = tangent
        F = np.concatenate([res, [np.dot(u - u_pred, tangent)]])
        # Newton step: Jfull du = -F
        try:
            du = np.linalg.solve(Jfull, -F)
        except np.linalg.LinAlgError:
            du = np.linalg.lstsq(Jfull, -F, rcond=None)[0]
        # Line search (simple: full step, then halve if residual grows)
        step = 1.0
        best = None
        bestr = np.inf
        for _ in range(15):
            un = u + step * du
            # Bounds: T>0, tau in a sane band, y0[0]>0
            if (un[n] <= 0.1 or abs(un[n + 1]) > 1e4
                    or un[0] <= 0 or not np.all(np.isfinite(un))):
                step *= 0.5
                continue
            resn, _ = shooting_residual(un, p, dt, phase_idx, phase_val)
            rn = np.linalg.norm(np.concatenate(
                [resn, [np.dot(un - u_pred, tangent)]]))
            if np.isfinite(rn) and rn < bestr:
                bestr = rn
                best = (step, un)
            step *= 0.5
        if best is None:
            return u_prev, tangent, np.linalg.norm(res), False
        step, u = best
        res_final, _ = shooting_residual(u, p, dt, phase_idx, phase_val)
        rnorm = np.linalg.norm(res_final)
        if rnorm < tol:
            break
        if step == 0 and rnorm > 1e-4:
            break
    # New tangent: null vector of dG/du at the new point
    J, _ = jacobian_shooting(u, p, dt, phase_idx, phase_val, eps_jac)
    U, S, Vt = np.linalg.svd(J)
    tnew = Vt[-1]
    # Orient consistently with the previous tangent
    if np.dot(tnew, tangent) < 0:
        tnew = -tnew
    tnew = tnew / np.linalg.norm(tnew)
    ok = rnorm < 1e-5
    return u, tnew, rnorm, ok


def _newton_fix(u0, p, dt, phase_idx, phase_val, maxit=30, tol=1e-9):
    """Newton to solve G(u)=0 with phase condition (no arclength)."""
    n = len(u0) - 2
    u = u0.copy()
    for it in range(maxit):
        res, _ = shooting_residual(u, p, dt, phase_idx, phase_val)
        r = np.linalg.norm(res)
        if r < tol:
            break
        J, _ = jacobian_shooting(u, p, dt, phase_idx, phase_val)
        # J is (n+1) x (n+2); solve least-squares (underdetermined by 1)
        try:
            du = np.linalg.lstsq(J, -res, rcond=None)[0]
        except np.linalg.LinAlgError:
            break
        # line search
        best = None; bestr = r
        for s in [1.0, 0.5, 0.25, 0.1, 0.05, 0.02, 0.01]:
            un = u + s * du
            if un[n] <= 0.1 or un[0] <= 0 or not np.all(np.isfinite(un)):
                continue
            resn, _ = shooting_residual(un, p, dt, phase_idx, phase_val)
            rn = np.linalg.norm(resn)
            if rn < bestr:
                bestr = rn; best = (s, un)
        if best is None:
            break
        u = best[1]
    return u


def _floquet_at(u, p, dt, phase_idx, phase_val, eps=1e-6):
    """Estimate Floquet multipliers at the converged orbit by finite
    differences of the period map.

    Uses the exact scheme validated in verify_floquet_points.py
    (converge_orbit_by_shooting): iterate y0 <- flow_T(y0) with the periodic
    history rebuilt each iteration and phase rotation, until the period-map
    residual is tiny; then difference the converged images.  This correctly
    includes the DDE history coupling (the orbit is closed, so the history
    is the orbit's own tail) and gives stable multipliers ~0.98 for the
    gated core's lower-window cycle.
    """
    from verify_floquet_points import converge_orbit_by_shooting
    n = len(u) - 2
    y0 = u[:n]; T = u[n]; tau = u[n + 1]
    p.tau = tau
    r = converge_orbit_by_shooting(p, tau, y0, T, dt=dt, n_picard=40,
                                   eps=1e-7, n_fd=3)
    if r is None:
        # fallback: rough FD on the period map with the fixed periodic history
        yT0, ts, ys, hfunc = integrate_orbit(y0, T, tau, p, dt)
        Mono = np.zeros((n, n))
        for k in range(n):
            e = eps * max(abs(y0[k]), 1e-3)
            col = np.zeros(n)
            for sgn in (+1, -1):
                yp = y0.copy(); yp[k] += sgn * e
                yTp, _, _, _ = integrate_orbit(yp, T, tau, p, dt,
                                               history_seed=None)
                col += sgn * yTp
            Mono[:, k] = col / (2 * e)
        return np.linalg.eigvals(Mono)
    return r['mults']


def _dominant_nontrivial(mults):
    """Dominant nontrivial Floquet multiplier (exclude phase mode ~1)."""
    mu = sorted(mults, key=lambda z: -abs(z))
    for m in mu:
        if abs(abs(m) - 1.0) > 1e-3:
            return m
    return mu[0]


def _floquet_multishoot(u, p, dt, M=8, phase_idx=0, phase_val=None,
                        eps=1e-6, gh_iter=2):
    """Floquet multipliers via the multishoot cyclic-continuity Jacobian —
    the CORRECT DDE monodromy (includes the history coupling that a naive
    forward variational integration misses).

    u = (y0[0..n-1], T, tau).  Builds M orbit nodes from the single-shooting
    trajectory, runs multishoot's assemble_jacobian + monodromy_from_jacobian,
    and returns the Floquet multipliers.

    This is the clean way to get correct multipliers for the arc-length
    continuation: the multishoot Jacobian accounts for the DDE history
    wrapping around the periodic orbit.
    """
    from multishoot import (orbit_to_nodes, integrate_segments,
                            assemble_jacobian, monodromy_from_jacobian)
    n = len(u) - 2
    y0 = u[:n]; T = u[n]; tau = u[n + 1]
    p.tau = tau
    # Get the orbit trajectory (single-shooting history) for node extraction
    yT, ts, ys, hfunc = integrate_orbit(y0, T, tau, p, dt)
    # Build M nodes from the trajectory
    nodes = orbit_to_nodes(ts, ys, T, M)
    # Integrate segments to get ends for the Jacobian
    ends, Tseg, h, _, _ = integrate_segments(nodes, T, p, dt, gh_iter)
    # Phase tangent: rhs at node 0 with the delayed state (for orthogonality)
    # use the multishoot default (anchor node 0, component phase_idx)
    # Build the full Jacobian (frozen_T=True: the monodromy is the period-T map,
    # T fixed at the converged value)
    J = assemble_jacobian(nodes, T, p, dt, ends, gh_iter, eps,
                          frozen_T=True, phase_tangent=None)
    Mono = monodromy_from_jacobian(J, M, n)
    return np.linalg.eigvals(Mono)
