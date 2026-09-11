"""
Multiple-shooting periodic-orbit solver for DDEs with correct Floquet
multipliers (DDE-BIFTOOL style).

Key correction vs. naive single shooting
----------------------------------------
For a DDE periodic orbit, perturbing y(0) also perturbs the orbit's history
on [-tau, 0] (which is the orbit's own tail on [T-tau, T]).  A forward
variational integration with W(t<0)=0 computes the shooting Jacobian with
history held fixed, whose eigenvalues are NOT the Floquet multipliers.

The correct monodromy is assembled from the full multiple-shooting Jacobian
J_{jk} = d(end_j)/d(s_k), where end_j is segment j's endpoint and s_k are
all M node states.  The cyclic linearised continuity equations
    sum_k J_{jk} ds_k = ds_{j+1}   (j = 0..M-2)
    sum_k J_{M-1,k} ds_k = M ds_0  (cyclic)
determine ds_1..ds_{M-1} from ds_0; the last row gives column i of the
monodromy M.  This automatically includes the history coupling and yields
the exact Floquet multipliers (one is ~1, the phase mode).

J is assembled by central finite differences over node perturbations, which
robustly captures the delay-induced dense coupling.  The T-column is by
forward finite difference.
"""

import numpy as np
from dde_core import integrate_dde, rhs, equilibrium, CoreParams


def history_from_global(global_t, global_y, T):
    n = global_y.shape[1]
    def hfunc(t, gt=global_t, gy=global_y, T=T, n=n):
        return np.array([np.interp(t, gt, gy[:, j], period=T)
                         for j in range(n)])
    return hfunc


def integrate_segments(nodes, T, p, dt, gh_iter=2):
    """Integrate M segments of length h=T/M, each starting from node j.  The
    global history used for delayed values is built from the concatenated
    segment trajectories and iterated gh_iter times for consistency.
    """
    M, n = nodes.shape
    h = T / M
    # Initial global trajectory: linear interpolation between nodes (closed).
    grid_t = np.linspace(0, T, M + 1)
    grid_y = np.vstack([nodes, nodes[0:1]])
    all_ts = all_ys = ends = None
    for _ in range(gh_iter):
        hfunc = history_from_global(grid_t, grid_y, T)
        all_ts = []
        all_ys = []
        ends = np.zeros((M, n))
        for j in range(M):
            yT, _, ts, ys = integrate_dde(nodes[j], hfunc, h, p, dt,
                                          compute_monodromy=False)
            ends[j] = yT
            all_ts.append(ts[:-1] + j * h)
            all_ys.append(ys[:-1])
        # Close the loop with node 0 (not the integrated end of the last seg)
        grid_t = np.concatenate(all_ts + [np.array([T])])
        grid_y = np.vstack(all_ys + [nodes[0:1]])
    return ends, T, h, all_ts, all_ys


def assemble_jacobian(nodes, T, p, dt, ends, gh_iter=2, eps=1e-6,
                      frozen_T=False, phase_tangent=None):
    """Full (M*n+1) x (M*n+1) finite-difference Jacobian of the shooting
    constraints.  Last row is the phase condition: tangent dot ds_0 = 0
    (orthogonality to the trajectory's tangent vector)."""
    M, n = nodes.shape
    Nvar = M * n + 1
    J = np.zeros((M * n + 1, Nvar))
    base_scale = np.maximum(np.max(np.abs(nodes), axis=0), 1e-6)
    for jj in range(M):
        for kk in range(n):
            e = eps * base_scale[kk]
            nodes_p = nodes.copy(); nodes_p[jj, kk] += e
            nodes_m = nodes.copy(); nodes_m[jj, kk] -= e
            ends_p, _, _, _, _ = integrate_segments(nodes_p, T, p, dt, gh_iter)
            ends_m, _, _, _, _ = integrate_segments(nodes_m, T, p, dt, gh_iter)
            col = np.zeros(M * n)
            for j in range(M):
                col[j * n:(j + 1) * n] = (ends_p[j] - ends_m[j]) / (2 * e)
                if (j + 1) % M == jj:
                    col[j * n + kk] -= 1.0
            J[:M * n, jj * n + kk] = col
    if not frozen_T:
        # Central finite difference in T.  Because integrate_dde now chooses
        # h = T/nsteps with nsteps ~ round(h_target/dt), perturbing T changes
        # the step size h but not the number of steps (for small dT), giving
        # a smooth, accurate derivative.
        dT = T * 1e-5
        ends_p, _, _, _, _ = integrate_segments(nodes, T + dT, p, dt, gh_iter)
        ends_m, _, _, _, _ = integrate_segments(nodes, T - dT, p, dt, gh_iter)
        for j in range(M):
            J[j * n:(j + 1) * n, M * n] = (ends_p[j] - ends_m[j]) / (2 * dT)
    # Phase row: orthogonality to trajectory tangent (dot(s0 - s0_ref, v) = 0)
    if phase_tangent is not None:
        J[M * n, :n] = phase_tangent
    else:
        J[M * n, 0] = 1.0
    return J


def monodromy_from_jacobian(J, M, n):
    """Extract the n x n Floquet monodromy from the (M*n) x (M*n) Jacobian
    of the cyclic continuity constraints.

    J[j*n:(j+1)*n, k*n:(k+1)*n] = d(end_j - s_{j+1})/d(s_k).
    For a perturbation ds_0, the first M-1 rows determine ds_1..ds_{M-1};
    the last row (j=M-1) gives M_lin * ds_0.
    """
    Jm = J[:M * n, :M * n].copy()
    # Unknowns: ds_1..ds_{M-1}, columns n..M*n.  Known: ds_0, columns 0..n.
    # For j=0..M-2: sum_k Jm[j*n:(j+1)*n, k*n:(k+1)*n] ds_k = 0
    # i.e. A x = -b ds_0 where x = (ds_1,...,ds_{M-1}), A = rows 0..(M-2)*n,
    # cols n..M*n; b = rows 0..(M-2)*n, cols 0..n.
    nrows = (M - 1) * n
    A = Jm[:nrows, n:]
    b = Jm[:nrows, :n]
    # Solve A X = -b for X, shape ((M-1)*n, n), where column i gives
    # (ds_1,...,ds_{M-1}) for ds_0=e_i.
    X = np.linalg.lstsq(A, -b, rcond=None)[0]
    # Last row: sum_k Jm[(M-1)*n:, k*n:(k+1)*n] ds_k = Mono ds_0
    last = Jm[(M - 1) * n:, :]
    # last[:, :n] ds_0 + last[:, n:] X ds_0 = Mono ds_0
    Mono = last[:, :n] + last[:, n:] @ X
    return Mono


def multi_shoot(nodes0, T0, tau, p: CoreParams, dt, M=12,
                maxit=40, tol=1e-8, phase_anchor_idx=0,
                phase_anchor_val=None, verbose=False,
                fp_iterations=12, gh_iter=2, fd_eps=1e-6,
                freeze_T_until=1.0):
    p.tau = tau
    n = nodes0.shape[1]
    M = nodes0.shape[0]
    nodes = nodes0.astype(float).copy()
    T = float(T0)
    if phase_anchor_val is None:
        phase_anchor_val = float(nodes[0, phase_anchor_idx])

    # ---- Picard: node_{j+1} <- end_j, phase-rotate ----
    for p_it in range(fp_iterations):
        ends, T, h, _, _ = integrate_segments(nodes, T, p, dt, gh_iter)
        new_nodes = np.zeros_like(nodes)
        for j in range(M):
            new_nodes[(j + 1) % M] = ends[j]
        cont = max(np.linalg.norm(ends[j] - nodes[(j + 1) % M])
                   for j in range(M))
        anchor = new_nodes[:, phase_anchor_idx]
        shift = 0
        for j in range(M):
            ja = (j + 1) % M
            if anchor[j] < phase_anchor_val <= anchor[ja]:
                shift = ja
                break
        if shift:
            new_nodes = np.roll(new_nodes, -shift, axis=0)
        nodes = new_nodes
        if verbose and p_it % 3 == 0:
            print(f"  Picard {p_it}: cont={cont:.3e} T={T:.3f}")

    # Reference node for the orthogonality phase condition
    s0_ref = nodes[0].copy()

    # ---- Newton ----
    last_res = np.inf
    converged = False
    best_state = (nodes.copy(), T)
    best_J = None
    best_rn = np.inf
    for it in range(maxit):
        ends, T, h, seg_ts, seg_ys = integrate_segments(nodes, T, p, dt,
                                                        gh_iter)
        res = np.zeros(M * n + 1)
        for j in range(M):
            res[j * n:(j + 1) * n] = ends[j] - nodes[(j + 1) % M]
        g_t = np.concatenate(seg_ts + [np.array([T])])
        g_y = np.vstack(seg_ys + [nodes[0:1]])
        def gh(t):
            return np.array([np.interp(t, g_t, g_y[:, k], period=T)
                             for k in range(n)])
        s_tau = gh(T - p.tau)
        v = rhs(nodes[0], s_tau, p)
        vnorm = np.linalg.norm(v)
        if vnorm > 1e-12:
            v = v / vnorm
        res[M * n] = float(np.dot(nodes[0] - s0_ref, v))
        rn = np.linalg.norm(res[:M * n])
        if rn < best_rn:
            best_rn = rn
            best_state = (nodes.copy(), T)
            best_seg = (seg_ts, seg_ys, ends.copy())
            best_v = v.copy()
        last_res = rn
        if rn < tol:
            converged = True
            break
        if not np.isfinite(rn):
            break

        frozen_T = rn > freeze_T_until
        J = assemble_jacobian(nodes, T, p, dt, ends, gh_iter, fd_eps,
                              frozen_T=frozen_T, phase_tangent=v)
        if frozen_T:
            J[:, M * n] = 0.0
        if rn < best_rn:
            best_J = J.copy()
        try:
            sol, *_ = np.linalg.lstsq(J, -res, rcond=None)
        except np.linalg.LinAlgError:
            if verbose:
                print(f"  singular at it {it}")
            break
        dnodes = sol[:M * n].reshape(M, n)
        dT = 0.0 if frozen_T else sol[M * n]

        # line search
        best = None
        bestr = rn
        for s in [1.0, 0.5, 0.25, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]:
            ns = nodes + s * dnodes
            Tn = T + s * dT
            if Tn < dt * 4 * M or np.any(ns[:, 0] <= 0):
                continue
            try:
                ends_n, Tn, _, _, _ = integrate_segments(ns, Tn, p, dt,
                                                         gh_iter)
            except (FloatingPointError, OverflowError, ValueError):
                continue
            r = max(np.linalg.norm(ends_n[j] - ns[(j + 1) % M])
                    for j in range(M))
            if np.isfinite(r) and r < bestr:
                bestr = r
                best = (s, ns, Tn)
        if best is None:
            if verbose:
                print(f"  line search fail at it {it}, res={rn:.2e}")
            break
        s, nodes, T = best
        if verbose and (it % 2 == 0 or bestr < 1e-4):
            print(f"  Newton {it}: res={bestr:.3e} T={T:.4f} s={s}"
                  f"{' (T frozen)' if frozen_T else ''}")
        last_res = bestr
        if bestr < tol:
            converged = True
            break

    # Use best state
    nodes, T = best_state
    ends, T, h, seg_ts, seg_ys = integrate_segments(nodes, T, p, dt, gh_iter)
    if best_J is None or best_rn > 1e-3:
        g_t = np.concatenate(seg_ts + [np.array([T])])
        g_y = np.vstack(seg_ys + [nodes[0:1]])
        s_tau = np.array([np.interp(T - p.tau, g_t, g_y[:, k], period=T)
                          for k in range(n)])
        v = rhs(nodes[0], s_tau, p)
        vnorm = np.linalg.norm(v)
        if vnorm > 1e-12:
            v = v / vnorm
        J = assemble_jacobian(nodes, T, p, dt, ends, gh_iter, fd_eps,
                              frozen_T=False, phase_tangent=v)
    else:
        J = best_J
    Mono = monodromy_from_jacobian(J, M, n)
    mults = np.linalg.eigvals(Mono)
    global_t = np.concatenate(seg_ts + [np.array([T])])
    global_y = np.vstack(seg_ys + [nodes[0:1]])
    return {
        'y0': nodes[0].copy(), 'T': T, 'tau': tau,
        'converged': converged, 'residual': last_res,
        'monodromy': Mono, 'multipliers': mults,
        'nodes': nodes.copy(), 'ts': global_t, 'ys': global_y,
    }


def orbit_to_nodes(ts, ys, T, M):
    n = ys.shape[1]
    grid_t = np.linspace(0, T, M, endpoint=False)
    nodes = np.zeros((M, n))
    for j in range(M):
        for k in range(n):
            nodes[j, k] = np.interp(grid_t[j], ts, ys[:, k], period=T)
    return nodes


def continue_branch(nodes0, T0, tau_values, p, dt, M=10,
                    phase_anchor_idx=0, phase_anchor_val=50.0,
                    fp_iterations=10, gh_iter=2, verbose=True, **kw):
    """Natural-parameter continuation in tau.  Returns list of result dicts."""
    results = []
    nodes = nodes0.copy()
    T = T0
    for i, tau in enumerate(tau_values):
        res = multi_shoot(nodes, T, tau, p, dt, M=M,
                          phase_anchor_idx=phase_anchor_idx,
                          phase_anchor_val=phase_anchor_val,
                          fp_iterations=fp_iterations, gh_iter=gh_iter,
                          verbose=False, **kw)
        if res['converged']:
            results.append(res)
            nodes = res['nodes']
            T = res['T']
            if verbose:
                mu = sorted(res['multipliers'], key=lambda z: -abs(z))
                # phase mode ~1; report next two
                non_phase = [m for m in mu if abs(abs(m) - 1.0) > 1e-3]
                dom = non_phase[0] if non_phase else mu[0]
                amp = res['ys'][:, 0].max() - res['ys'][:, 0].min()
                print(f"tau={tau:8.3f}  T={T:8.3f}  amp={amp:7.2f}  "
                      f"|mu_dom|={abs(dom):.5f}  mu_dom={dom:.4f}  "
                      f"res={res['residual']:.1e}")
        else:
            if verbose:
                print(f"tau={tau:8.3f}  ** did not converge "
                      f"(res={res['residual']:.2e})")
            break
    return results
