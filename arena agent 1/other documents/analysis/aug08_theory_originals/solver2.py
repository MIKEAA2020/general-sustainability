"""
Robust multiple-shooting DDE periodic-orbit solver.

- Fixed-step RK4 with h = T/nsteps (T fully continuous).
- Segment integration with global periodic history, iterated to consistency.
- Broyden's quasi-Newton for the full (nodes, T) system — avoids the
  finite-difference Jacobian cost and is robust to the dense DDE coupling.
- Orthogonality phase condition.
- Floquet monodromy assembled from a finite-difference Jacobian at the
  converged solution (cheap relative to the continuation as a whole).
"""
import numpy as np
from dde_core import integrate_dde, rhs, equilibrium, CoreParams


def history_from_global(gt, gy, T, n):
    def hfunc(t):
        return np.array([np.interp(t, gt, gy[:, j], period=T)
                         for j in range(n)])
    return hfunc


def integrate_segments(nodes, T, p, dt, gh_iter=3):
    M, n = nodes.shape
    h = T / M
    gt = np.linspace(0, T, M + 1)
    gy = np.vstack([nodes, nodes[0:1]])
    ends = None
    for _ in range(gh_iter):
        hfunc = history_from_global(gt, gy, T, n)
        all_ts, all_ys = [], []
        ends = np.zeros((M, n))
        for j in range(M):
            yT, _, ts, ys = integrate_dde(nodes[j], hfunc, h, p, dt,
                                          compute_monodromy=False)
            ends[j] = yT
            all_ts.append(ts[:-1] + j * h)
            all_ys.append(ys[:-1])
        gt = np.concatenate(all_ts + [np.array([T])])
        gy = np.vstack(all_ys + [nodes[0:1]])
    return ends, T, h, all_ts, all_ys


def shooting_residual(x, M, n, p, dt, anchor_val, anchor_idx, gh_iter):
    """x = flattened nodes (M*n) then T.  Returns M*n continuity + 1 phase.
    Phase condition: nodes[0, 0] = anchor_val[0] (fix N at t=0)."""
    nodes = x[:M * n].reshape(M, n)
    T = x[M * n]
    ends, T, h, _, _ = integrate_segments(nodes, T, p, dt, gh_iter)
    res = np.zeros(M * n + 1)
    for j in range(M):
        res[j * n:(j + 1) * n] = ends[j] - nodes[(j + 1) % M]
    res[M * n] = nodes[0, 0] - anchor_val[0]
    return res, ends, T


def broyden_solve(x0, M, n, p, dt, anchor_val, anchor_idx, gh_iter=3,
                  maxit=60, tol=1e-7, verbose=False, fd_jac_init=True):
    """Broyden's method.  Initial Jacobian by finite differences if
    fd_jac_init, else identity."""
    x = x0.copy()
    F, ends, T = shooting_residual(x, M, n, p, dt, anchor_val, anchor_idx,
                                   gh_iter)
    nrm = np.linalg.norm(F)
    if verbose:
        print(f"  init res={nrm:.4e} T={T:.4f}")
    ndim = len(x)
    if fd_jac_init:
        # Small finite-difference Jacobian, with componentwise eps.  Use
        # bounded perturbations to avoid overflow in the DDE.
        J = np.zeros((ndim, ndim))
        for i in range(ndim):
            scale = 1e-5 * max(abs(x[i]), 1e-3)
            xp = x.copy(); xp[i] += scale
            try:
                Fp, _, _ = shooting_residual(xp, M, n, p, dt, anchor_val,
                                            anchor_idx, gh_iter)
                if np.all(np.isfinite(Fp)):
                    J[:, i] = (Fp - F) / scale
                else:
                    J[i, i] = 1.0
            except (FloatingPointError, OverflowError, ValueError):
                J[i, i] = 1.0
    else:
        J = np.eye(ndim)

    best_x = x.copy()
    best_nrm = nrm
    lam = 1e-3  # Levenberg-Marquardt damping
    for it in range(maxit):
        # Levenberg-Marquardt: (J^T J + lam I) dx = -J^T F
        JTJ = J.T @ J
        try:
            dx = np.linalg.solve(JTJ + lam * np.eye(ndim), -J.T @ F)
        except np.linalg.LinAlgError:
            dx = np.linalg.lstsq(J, -F, rcond=None)[0]
        # line search (Armijo)
        step = 1.0
        accepted = False
        for _ in range(20):
            xn = x + step * dx
            # bounds: T positive and in a reasonable band, nodes positive
            Tn_try = xn[M * n]
            if (Tn_try <= 1.0 or Tn_try > 10 * x[M * n]
                    or np.any(xn[:M * n:n] <= 0)):
                step *= 0.5
                continue
            try:
                Fn, ends_n, Tn = shooting_residual(
                    xn, M, n, p, dt, anchor_val, anchor_idx, gh_iter)
            except (FloatingPointError, OverflowError, ValueError):
                step *= 0.5
                continue
            if not np.all(np.isfinite(Fn)):
                step *= 0.5
                continue
            nr = np.linalg.norm(Fn)
            if nr < nrm:
                x = xn
                # Broyden rank-1 update
                y = Fn - F
                svec = step * dx
                J += np.outer(y - J @ svec, svec) / np.dot(svec, svec)
                F = Fn
                ends = ends_n
                T = Tn
                nrm = nr
                accepted = True
                lam *= 0.5  # trust region grows
                break
            step *= 0.5
        if not accepted:
            lam *= 4.0  # shrink trust region
            if lam > 1e8:
                if verbose:
                    print(f"  it {it}: LM damping too high, res={nrm:.4e}")
                break
        if nrm < best_nrm:
            best_nrm = nrm
            best_x = x.copy()
        if verbose and (it % 3 == 0 or nrm < 1e-4):
            print(f"  it {it}: res={nrm:.4e} T={T:.4f} step={step:.3g}")
        if nrm < tol:
            break
    return best_x, best_nrm


def compute_monodromy(x, M, n, p, dt, anchor_val, anchor_idx, gh_iter=3,
                      eps=1e-6):
    """Assemble the Floquet monodromy from the finite-difference Jacobian
    of the cyclic continuity constraints g_j = end_j - s_{j+1} (cyclic).

    Column k of Jm = d(g)/d(s_k).  For a perturbation ds_0, rows 0..M-2
    (equations g_0..g_{M-2}=0) determine ds_1..ds_{M-1}; the last row
    g_{M-1} = Mono ds_0 gives the monodromy.
    """
    ndim = M * n
    # Base residual (continuity part only).  We perturb nodes only (not T),
    # holding T fixed at the converged value, which is correct for the
    # monodromy of the period-T map.
    nodes_base = x[:M * n].reshape(M, n)
    T_base = x[M * n]
    ends_base, _, _, _, _ = integrate_segments(nodes_base, T_base, p, dt,
                                               gh_iter)
    g_base = np.zeros(ndim)
    for j in range(M):
        g_base[j * n:(j + 1) * n] = ends_base[j] - nodes_base[(j + 1) % M]
    Jm = np.zeros((ndim, ndim))
    for i in range(ndim):
        nodes_p = nodes_base.copy()
        nodes_p.flat[i] += eps * max(abs(nodes_p.flat[i]), 1.0)
        ends_p, _, _, _, _ = integrate_segments(nodes_p, T_base, p, dt,
                                                gh_iter)
        g_p = np.zeros(ndim)
        for j in range(M):
            g_p[j * n:(j + 1) * n] = ends_p[j] - nodes_p[(j + 1) % M]
        Jm[:, i] = (g_p - g_base) / (eps * max(abs(x[i]), 1.0))
    nrows = (M - 1) * n
    A = Jm[:nrows, n:]          # d(g_0..g_{M-2})/d(s_1..s_{M-1})
    b = Jm[:nrows, :n]          # d(g_0..g_{M-2})/d(s_0)
    X = np.linalg.lstsq(A, -b, rcond=None)[0]  # X: (M-1)*n x n
    last = Jm[(M - 1) * n:, :]  # d(g_{M-1})/d(s_0..s_{M-1})
    Mono = last[:, :n] + last[:, n:] @ X
    return Mono, Jm


def picard_refine(nodes, T, p, dt, M, n, gh_iter, n_iter, anchor_val,
                  verbose=False, damping=0.5):
    """Damped fixed-point iteration: node_{j+1} <- (1-d)*node_{j+1} + d*end_j,
    with phase rotation."""
    for it in range(n_iter):
        ends, T, h, _, _ = integrate_segments(nodes, T, p, dt, gh_iter)
        raw = np.zeros_like(nodes)
        for j in range(M):
            raw[(j + 1) % M] = ends[j]
        new_nodes = (1 - damping) * nodes + damping * raw
        res = max(np.linalg.norm(ends[j] - nodes[(j + 1) % M])
                  for j in range(M))
        nodes = new_nodes
        if verbose and it % 5 == 0:
            print(f"  Picard {it}: res={res:.3e} T={T:.3f}")
    return nodes, T


def solve_orbit(nodes0, T0, tau, p, dt, M=8, gh_iter=3, tol=1e-6,
                maxit=60, verbose=True, anchor_val=None,
                picard_iter=15, fd_jac_init=False):
    p.tau = tau
    n = nodes0.shape[1]
    if anchor_val is None:
        anchor_val = nodes0[0].copy()
    nodes = nodes0.copy()
    T = T0
    nodes, T = picard_refine(nodes, T, p, dt, M, n, gh_iter,
                             picard_iter, anchor_val, verbose=verbose)
    x0 = np.concatenate([nodes.ravel(), [T]])
    x, nrm = broyden_solve(x0, M, n, p, dt, anchor_val, 0, gh_iter,
                           maxit, tol, verbose, fd_jac_init=fd_jac_init)
    nodes = x[:M * n].reshape(M, n)
    T = x[M * n]
    Mono, Jm = compute_monodromy(x, M, n, p, dt, anchor_val, 0, gh_iter)
    mults = np.linalg.eigvals(Mono)
    return dict(converged=nrm < tol, residual=nrm, nodes=nodes, T=T,
                monodromy=Mono, multipliers=mults, x=x)
