"""
Adaptive-mesh / local-collocation replacement for the SNPO classification,
cleaned and self-contained (numpy/scipy only).

Based on the external AI's piecewise-collocation design, with the following
CORRECTIONS applied before running:
  1. HTML entities (&gt; &lt; &amp;) unescaped;  `if **name**` repaired.
  2. Invalid tuple-unpacking `tau_o,*,* , T_o = prev2` repaired.
  3. SIGN FIX: dZtau/dT = +(tau/T^2) (Dz @ Zv)  (the pasted code had '-',
     which is wrong: d/dT Z(s - tau/T) = +Z'(s - tau/T) * tau/T^2).
  4. rk4_dense_orbit is included self-contained (was missing from the paste).
  5. Slight robustness in lagrange_weights (exact Vandermonde solve).

Model (Candidate A):  eq N*=89.5519 Z*=0.06931 E*=2.08962;  Hopf pair
3.6662 / 150.3585;  large cycle tau=4: T~375.3, N in [41,95], E in [0.33,23];
folds ~5.574-5.575 (stable), ~5.587 (unstable), ~148.3 (upper).
"""
import numpy as np
import csv
import math
from scipy.linalg import lu_factor, lu_solve, eigvals

# ---------------- parameters (Candidate A) ----------------
r, K, q = 0.02, 100.0, 0.001
eta, Emax = 0.914, 30.0
delta0, Dref, taum, Zref = 0.01, 1.0, 5.0, 1.0
k = 10.0
delta = np.log(2.0) / 10.0

# ---------------- nonlinearities ----------------
def softplus(x):
    x = np.asarray(x, float)
    kx = k * x
    out = np.empty_like(kx)
    hi, lo = kx > 50, kx < -50
    out[hi] = x[hi]
    out[lo] = 0.0
    mid = ~(hi | lo)
    out[mid] = np.log1p(np.exp(kx[mid])) / k
    return out

def sigmoid(x):
    x = np.asarray(x, float)
    out = np.empty_like(x)
    hi, lo = x > 50, x < -50
    out[hi] = 1.0
    out[lo] = 0.0
    mid = ~(hi | lo)
    out[mid] = 1.0 / (1.0 + np.exp(-x[mid]))
    return out

def equilibrium():
    Zs = delta
    a = -eta / Emax
    b = eta * Zs / Dref
    c = delta0 * Zs / (Zref + Zs)
    Es = (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
    Ns = K * (1 - q * Es / r)
    return np.array([Ns, Zs, Es])

def dde_rhs(y, ytau):
    N, Z, E = y
    Ztau = ytau[1]
    S = r * N * (1 - N / K)
    qEN = q * E * N
    src = max(0.0, softplus(qEN - S) - np.log(2.0) / k + delta)
    Zden = max(Zref + Ztau, 1e-8)
    bracket = eta * E * (Ztau / Dref - E / Emax) + delta0 * Ztau / Zden
    return np.array([
        S - qEN,
        (src - Z) / taum,
        (1 - E / Emax) * bracket
    ])

# ---------------- self-contained RK4 DDE + dense-orbit seeder ----------------
def rk4_dde(y0, history, T, tau, dt=0.1):
    n = len(y0)
    nsteps = int(round(T / dt))
    h = T / nsteps
    ys = np.zeros((nsteps + 1, n))
    ys[0] = y0

    def delayed(t):
        if t <= 0:
            return history(t)
        ti = t / h
        i = int(np.floor(ti))
        if i >= nsteps:
            return ys[nsteps]
        fr = ti - i
        return (1 - fr) * ys[i] + fr * ys[i + 1]

    for i in range(nsteps):
        t = i * h
        y = ys[i]
        yd = delayed(t - tau)
        k1 = dde_rhs(y, yd)
        yd2 = delayed(t + h / 2 - tau)
        k2 = dde_rhs(y + h / 2 * k1, yd2)
        k3 = dde_rhs(y + h / 2 * k2, yd2)
        yd4 = delayed(t + h - tau)
        k4 = dde_rhs(y + h * k3, yd4)
        ys[i + 1] = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return ys

def rk4_dense_orbit(tau, dt=0.05, T_warmup=80000.0, pert=0.15):
    """Settle onto the stable large-amplitude cycle; return one period as
    orb = [N,Z,E] shape (3, npts), phase-aligned so N max at index 0.
    IC = (N=99, Z=delta, E=0.5): the manuscript's documented cycle basin
    (large stock, low effort).  NOTE: eq*1.15 puts N=103 > K and lands on
    the WRONG orbit in the bistable window."""
    eq = equilibrium()
    y0 = np.array([99.0, eq[1], 0.5])
    hist = lambda t: eq
    ys = rk4_dde(y0, hist, T_warmup, tau, dt)
    tail = ys[int(0.5 * len(ys)):]
    N = tail[:, 0]
    mn = N.mean()
    cross = [j for j in range(1, len(N)) if N[j - 1] < mn <= N[j]]
    if len(cross) < 4:
        return None, None, None
    periods = np.diff(cross) * dt
    T = float(np.median(periods[-3:]))
    j0 = cross[-1]
    nT = int(round(T / dt))
    if nT < 24:
        return None, None, None
    # Take one full period ENDING at the last mean-crossing (j0), going
    # backward so the segment stays inside the tail (j0 is deep in the
    # tail; forward-with-wrap would stitch a random-phase gap).
    seg = tail[j0 - nT:j0] if j0 >= nT else tail[:j0]
    kk = int(np.argmax(seg[:, 0]))
    seg = np.vstack((seg[kk:], seg[:kk]))
    return seg.T, T, dt

# ---------------- mesh utilities ----------------
def periodic_gradient(f, ds):
    return (np.roll(f, -1) - np.roll(f, 1)) / (2 * ds)

def smooth_periodic(w, q=5):
    if q <= 0:
        return w.copy()
    ker = np.ones(2 * q + 1) / (2 * q + 1)
    wp = np.concatenate([w[-q:], w, w[:q]])
    return np.convolve(wp, ker, mode="same")[q:q + len(w)]

def monitor_from_E(E, ds, weight=25.0):
    dE = periodic_gradient(E, ds)
    mag = np.abs(dE)
    mon = 1.0 + weight * mag / (mag.mean() + 1e-12)
    return smooth_periodic(mon, 5)

def adapt_mesh(s, w, N):
    w = np.maximum(np.asarray(w, float), 1e-8)
    n = len(s)
    ds = np.empty(n)
    ds[:-1] = np.diff(s)
    ds[-1] = 1.0 + s[0] - s[-1]
    interval = 0.5 * (w + np.roll(w, -1)) * ds
    C = np.concatenate(([0.0], np.cumsum(interval)))
    total = C[-1]
    targets = np.linspace(0.0, total, N, endpoint=False)
    s_new = np.zeros(N)
    for it, target in enumerate(targets):
        if target <= 0.0:
            s_new[it] = 0.0
            continue
        idx = np.searchsorted(C, target, side="right") - 1
        if idx >= n:
            idx = n - 1
        denom = interval[idx]
        frac = (target - C[idx]) / denom if denom > 0 else 0.0
        val = s[idx] + frac * ds[idx]
        if val >= 1.0:
            val -= 1.0
        s_new[it] = val
    if not np.all(np.diff(s_new) > -1e-12):
        s_new = np.sort(s_new)
        s_new = (s_new - s_new[0]) % 1.0
    s_new[0] = 0.0
    return s_new

def roll_phase(s, u):
    n = len(s)
    Nv = u[:n]
    i = int(np.argmax(Nv))
    if i == 0:
        return s, u
    order = np.r_[i:n, 0:i]
    s_new = s[order].copy()
    origin = s_new[0]
    s_new = (s_new - origin) % 1.0
    u_new = np.concatenate([
        u[:n][order],
        u[n:2 * n][order],
        u[2 * n:3 * n][order]
    ])
    return s_new, u_new

def adapt_solution(s, u, T, N, weight=25.0):
    n = len(s)
    D = periodic_interp_matrix(s, s, m=7, deriv=1)
    E = u[2 * n:3 * n]
    dE = D @ E
    mag = np.abs(dE)
    monitor = 1.0 + weight * mag / (mag.mean() + 1e-12)
    monitor = smooth_periodic(monitor, 5)
    s_new = adapt_mesh(s, monitor, N)
    P = periodic_interp_matrix(s, s_new, m=5, deriv=0)
    u_new = np.concatenate([
        P @ u[:n],
        P @ u[n:2 * n],
        P @ u[2 * n:3 * n]
    ])
    return s_new, u_new

# ---------------- local Lagrange weights ----------------
def lagrange_weights(x, x0, deriv=0):
    m = len(x)
    if m <= deriv:
        raise ValueError("stencil too small for derivative order")
    A = np.empty((m, m))
    for p in range(m):
        A[p, :] = (x - x0) ** p
    b = np.zeros(m)
    b[deriv] = math.factorial(deriv)
    try:
        return np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return np.linalg.lstsq(A, b, rcond=None)[0]

# ---------------- interpolation / differentiation matrices ----------------
def periodic_interp_matrix(s, targets, m=5, deriv=0):
    n = len(s)
    m = min(m, n)
    if deriv > 0 and m < 2:
        return np.zeros((len(targets), n))
    A = np.zeros((len(targets), n))
    r = m // 2
    for row, tgt in enumerate(targets):
        i = np.searchsorted(s, tgt, side="right") - 1
        if i < 0:
            i = n - 1
        start = i - r
        idx = np.mod(np.arange(start, start + m), n)
        if len(np.unique(idx)) < m:
            idx = np.arange(n)
            m_loc = n
        else:
            m_loc = m
        if deriv > 0 and m_loc <= deriv:
            continue
        xrel = (s[idx] - tgt + 0.5) % 1.0 - 0.5
        try:
            w = lagrange_weights(xrel, 0.0, deriv)
        except Exception:
            w = np.zeros(m_loc)
            if deriv == 0:
                w[0] = 1.0
        A[row, idx] = w
    return A

def interp_matrix(s, targets, m=5, deriv=0):
    n = len(s)
    m = min(m, n)
    if deriv > 0 and m < 2:
        return np.zeros((len(targets), n))
    A = np.zeros((len(targets), n))
    r = m // 2
    for row, tgt in enumerate(targets):
        i = np.searchsorted(s, tgt, side="right") - 1
        start = i - r
        start = min(max(start, 0), max(0, n - m))
        idx = np.arange(start, start + m)
        if len(np.unique(idx)) < m:
            idx = np.arange(n)
            m_loc = n
        else:
            m_loc = m
        if deriv > 0 and m_loc <= deriv:
            continue
        try:
            w = lagrange_weights(s[idx], tgt, deriv)
        except Exception:
            w = np.zeros(m_loc)
            if deriv == 0:
                w[0] = 1.0
        A[row, idx] = w
    return A

# ---------------- adaptive collocation BVP ----------------
def solve_collocation(tau, s, u0, T0, tol=1e-10, max_iter=60):
    n = len(s)
    D = periodic_interp_matrix(s, s, m=7, deriv=1)

    def delay_matrices(T):
        alpha = tau / T
        targets = (s - alpha) % 1.0
        Sh = periodic_interp_matrix(s, targets, m=5, deriv=0)
        Dz = periodic_interp_matrix(s, targets, m=5, deriv=1)
        return Sh, Dz

    def residual(v):
        u = v[:-1]
        T = v[-1]
        Nv = u[:n]
        Zv = u[n:2 * n]
        Ev = u[2 * n:3 * n]
        Sh, Dz = delay_matrices(T)
        Ztau = Sh @ Zv
        Zden = np.maximum(Zref + Ztau, 1e-8)
        S = r * Nv * (1 - Nv / K)
        qEN = q * Ev * Nv
        src = np.maximum(0.0, softplus(qEN - S) - np.log(2.0) / k + delta)
        inner = eta * Ev * (Ztau / Dref - Ev / Emax) + delta0 * Ztau / Zden
        gate = 1 - Ev / Emax
        rN = (D @ Nv) / T - (S - qEN)
        rZ = (D @ Zv) / T - (src - Zv) / taum
        rE = (D @ Ev) / T - gate * inner
        ph = D[0] @ Nv
        return np.concatenate([rN, rZ, rE, [ph]])

    def jacobian(v):
        u = v[:-1]
        T = v[-1]
        Nv = u[:n]
        Zv = u[n:2 * n]
        Ev = u[2 * n:3 * n]
        Sh, Dz = delay_matrices(T)
        Ztau = Sh @ Zv
        Zden = np.maximum(Zref + Ztau, 1e-8)
        S = r * Nv * (1 - Nv / K)
        Sp = r * (1 - 2 * Nv / K)
        qEN = q * Ev * Nv
        d = qEN - S
        src_arg = softplus(d) - np.log(2.0) / k + delta
        h = np.where(src_arg > 0, sigmoid(k * d), 0.0)
        fN_N = Sp - q * Ev
        fN_E = -q * Nv
        fZ_N = h * (q * Ev - Sp) / taum
        fZ_E = h * q * Nv / taum
        inner = eta * Ev * (Ztau / Dref - Ev / Emax) + delta0 * Ztau / Zden
        gate = 1 - Ev / Emax
        dR_dE = -(1.0 / Emax) * inner + gate * eta * (Ztau / Dref - 2 * Ev / Emax)
        dR_dZtau = gate * (eta * Ev / Dref + delta0 * Zref / (Zden * Zden))
        J = np.zeros((3 * n + 1, 3 * n + 1))
        J[:n, :n] = D / T - np.diag(fN_N)
        J[:n, 2 * n:3 * n] = -np.diag(fN_E)
        J[n:2 * n, :n] = -np.diag(fZ_N)
        J[n:2 * n, n:2 * n] = D / T + np.eye(n) / taum
        J[n:2 * n, 2 * n:3 * n] = -np.diag(fZ_E)
        J[2 * n:3 * n, n:2 * n] = -np.diag(dR_dZtau) @ Sh
        J[2 * n:3 * n, 2 * n:3 * n] = D / T - np.diag(dR_dE)
        J[:n, 3 * n] = -(D @ Nv) / (T * T)
        J[n:2 * n, 3 * n] = -(D @ Zv) / (T * T)
        dZtau_dT = +(tau / (T * T)) * (Dz @ Zv)      # SIGN FIXED
        J[2 * n:3 * n, 3 * n] = (
            -(D @ Ev) / (T * T) - dR_dZtau * dZtau_dT
        )
        J[3 * n, :n] = D[0]
        return J

    v = np.concatenate([u0, [T0]])
    f = residual(v)
    norm = np.linalg.norm(f, np.inf)
    for it in range(max_iter):
        if norm < tol:
            return v[:-1], v[-1], norm, True
        Jm = jacobian(v)
        try:
            step = np.linalg.solve(Jm, -f)
        except np.linalg.LinAlgError:
            step = np.linalg.lstsq(Jm, -f, rcond=None)[0]
        lam = 1.0
        nt = np.inf
        accepted = False
        for _ in range(35):
            vt = v + lam * step
            if vt[-1] <= 0.0:
                lam *= 0.5
                continue
            ft = residual(vt)
            nt = np.linalg.norm(ft, np.inf)
            if np.isfinite(nt) and nt < (1.0 - 1e-4 * lam) * norm:
                accepted = True
                break
            lam *= 0.5
        if not accepted:
            if np.isfinite(nt) and nt < norm:
                accepted = True
            else:
                return v[:-1], v[-1], norm, False
        v = v + lam * step
        f = residual(v)
        norm = np.linalg.norm(f, np.inf)
    return v[:-1], v[-1], norm, norm < tol

# ---------------- Floquet multipliers from collocation map ----------------
def floquet_collocation(u, T, s, tau, m_deriv=7, m_interp=5, K=None):
    n = len(s)
    Nv = u[:n]
    Zv = u[n:2 * n]
    Ev = u[2 * n:3 * n]
    s_ivp = np.concatenate([s, [1.0]])
    np_ = n + 1
    Niv = np.concatenate([Nv, [Nv[0]]])
    Ziv = np.concatenate([Zv, [Zv[0]]])
    Eiv = np.concatenate([Ev, [Ev[0]]])
    alpha = tau / T
    targets_coeff = (s_ivp - alpha) % 1.0
    Pcoeff = periodic_interp_matrix(s, targets_coeff, m=m_interp, deriv=0)
    Ztau = Pcoeff @ Zv
    Zden = np.maximum(Zref + Ztau, 1e-8)
    S = r * Niv * (1 - Niv / K)
    Sp = r * (1 - 2 * Niv / K)
    qEN = q * Eiv * Niv
    d = qEN - S
    src_arg = softplus(d) - np.log(2.0) / k + delta
    h = np.where(src_arg > 0, sigmoid(k * d), 0.0)
    fN_N = Sp - q * Eiv
    fN_E = -q * Niv
    fZ_N = h * (q * Eiv - Sp) / taum
    fZ_E = h * q * Niv / taum
    inner = eta * Eiv * (Ztau / Dref - Eiv / Emax) + delta0 * Ztau / Zden
    gate = 1 - Eiv / Emax
    dR_dE = -(1.0 / Emax) * inner + gate * eta * (Ztau / Dref - 2 * Eiv / Emax)
    dR_dZtau = gate * (eta * Eiv / Dref + delta0 * Zref / (Zden * Zden))
    Divp = interp_matrix(s_ivp, s_ivp, m=m_deriv, deriv=1)
    S_cur = np.zeros((np_, np_))
    rows_cur = np.where((s_ivp >= alpha) & (np.arange(np_) > 0))[0]
    if len(rows_cur) > 0:
        targets_cur = s_ivp[rows_cur] - alpha
        S_cur[rows_cur, :] = interp_matrix(s_ivp, targets_cur, m=m_interp, deriv=0)
    if K is None:
        K = max(48, min(256, int(np.ceil(tau / 0.5)) + 1))
    eta_hist = np.linspace(0.0, 1.0, K)
    theta_hist = -tau + eta_hist * tau
    H_z = np.zeros((np_, K))
    rows_hist = np.where((s_ivp < alpha) & (np.arange(np_) > 0))[0]
    if len(rows_hist) > 0:
        target_eta = s_ivp[rows_hist] / alpha
        m_hist = min(m_interp, K)
        if m_hist >= 2:
            H_z[rows_hist, :] = interp_matrix(eta_hist, target_eta, m=m_hist, deriv=0)
    A = np.zeros((3 * np_, 3 * np_))
    A[0, 0] = 1.0
    A[np_, np_] = 1.0
    A[2 * np_, 2 * np_] = 1.0
    for i in range(1, np_):
        Drow = Divp[i, :] / T
        A[i, :np_] = Drow
        A[i, i] -= fN_N[i]
        A[i, 2 * np_ + i] -= fN_E[i]
        A[np_ + i, np_:2 * np_] = Drow
        A[np_ + i, i] -= fZ_N[i]
        A[np_ + i, np_ + i] += 1.0 / taum
        A[np_ + i, 2 * np_ + i] -= fZ_E[i]
        A[2 * np_ + i, 2 * np_:3 * np_] = Drow
        A[2 * np_ + i, 2 * np_ + i] -= dR_dE[i]
    dR = dR_dZtau.copy()
    dR[0] = 0.0
    A[2 * np_:3 * np_, np_:2 * np_] -= np.diag(dR) @ S_cur
    B = np.zeros((3 * np_, 3 * K))
    B[0, K - 1] = 1.0
    B[np_, K + (K - 1)] = 1.0
    B[2 * np_, 2 * K + (K - 1)] = 1.0
    if len(rows_hist) > 0:
        B[2 * np_ + rows_hist, K:2 * K] = (
            dR[rows_hist, None] * H_z[rows_hist, :]
        )
    try:
        lu, piv = lu_factor(A)
        X = lu_solve((lu, piv), B)
    except Exception:
        X = np.linalg.lstsq(A, B, rcond=None)[0]
    s_out = 1.0 - alpha + eta_hist * alpha
    Out = interp_matrix(s_ivp, s_out, m=m_interp, deriv=0)
    M = np.vstack([
        Out @ X[:np_, :],
        Out @ X[np_:2 * np_, :],
        Out @ X[2 * np_:, :]
    ])
    return eigvals(M)

def classify_multipliers(ev):
    idx_trivial = int(np.argmin(np.abs(ev - 1.0)))
    trivial = ev[idx_trivial]
    nontriv = np.delete(ev, idx_trivial)
    if len(nontriv) == 0:
        dom = 1j
    else:
        dom = nontriv[int(np.argmax(np.abs(nontriv)))]
    cls = ""
    if abs(abs(dom) - 1.0) < 0.03:
        if abs(np.imag(dom)) < 0.05 and np.real(dom) > 0.90:
            cls = "SNPO"
        elif abs(np.imag(dom)) < 0.05 and np.real(dom) < -0.90:
            cls = "PD"
        else:
            cls = "Torus"
    return dom, trivial, cls

# ---------------- continuation driver ----------------
def prepare_first_guess(tau, N=240):
    orb, T, dt_orb = rk4_dense_orbit(tau, dt=0.05, T_warmup=80000.0)
    if orb is None:
        return None, None, None
    npts = orb.shape[1]
    s_uniform = np.linspace(0.0, 1.0, npts, endpoint=False)
    ds = 1.0 / npts
    monitor = monitor_from_E(orb[2], ds, weight=25.0)
    s = adapt_mesh(s_uniform, monitor, N)
    P = periodic_interp_matrix(s_uniform, s, m=5, deriv=0)
    u = np.concatenate([
        P @ orb[0],
        P @ orb[1],
        P @ orb[2]
    ])
    return s, u, T

def run_branch(tau_list, N=240, K=None, csv_filename=None):
    print(f"{'tau':>9s} {'ok':>3s} {'T':>10s} {'res':>10s} "
          f"{'|mu_dom|':>9s} {'mu_dom':>22s} {'triv':>16s} {'class':>6s}")
    prev = None
    prev2 = None
    rows = []
    for tau in tau_list:
        if prev is None:
            guess = prepare_first_guess(tau, N=N)
            if guess[0] is None:
                print(f"{tau:9.4f} no  (RK4 seed failed)")
                continue
            s, u0, T0 = guess
        else:
            tau_p, s_p, u_p, T_p = prev
            s, u0 = adapt_solution(s_p, u_p, T_p, N)
            if prev2 is not None:
                tau_o, s_o, u_o, T_o = prev2
                if abs(tau_p - tau_o) > 1e-12:
                    T0 = T_p + (T_p - T_o) / (tau_p - tau_o) * (tau - tau_p)
                else:
                    T0 = T_p
            else:
                T0 = T_p
        u, T, res, ok = solve_collocation(tau, s, u0, T0)
        if not ok:
            print(f"{tau:9.4f} no  {'':10s} {res:10.2e}  (Newton failed)")
            continue
        s, u = roll_phase(s, u)
        ev = floquet_collocation(u, T, s, tau, K=K)
        dom, triv, cls = classify_multipliers(ev)
        print(f"{tau:9.4f} yes {T:10.3f} {res:10.2e} "
              f"{abs(dom):9.5f} ({np.real(dom):+9.5f},{np.imag(dom):+9.5f}) "
              f"({np.real(triv):+8.5f},{np.imag(triv):+6.3f}) {cls:>6s}")
        rows.append({
            "tau": tau, "T": T, "residual": res,
            "mu_dom_abs": abs(dom), "mu_dom_real": float(np.real(dom)),
            "mu_dom_imag": float(np.imag(dom)),
            "trivial_real": float(np.real(triv)),
            "trivial_imag": float(np.imag(triv)),
            "class": cls
        })
        prev2 = prev
        prev = (tau, s, u, T)
    if csv_filename and rows:
        with open(csv_filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nSaved: {csv_filename}")
    return rows

if __name__ == "__main__":
    print("Equilibrium:", np.round(equilibrium(), 6))
    print()
    print("== Lower fold region: tau -> ~5.574-5.575 ==")
    run_branch(
        [4.0, 4.5, 5.0, 5.3, 5.45, 5.5, 5.55, 5.565, 5.572, 5.574],
        N=240, K=96, csv_filename="snpo_lower_fold_adaptive.csv"
    )
    print()
    print("== Upper fold region: tau -> ~148.3 ==")
    run_branch(
        [149.5, 149.0, 148.7, 148.5, 148.4, 148.35, 148.32],
        N=240, K=192, csv_filename="snpo_upper_fold_adaptive.csv"
    )


def monodromy_variational(orb, T, tau, dt=0.01):
    """Variational RK4 monodromy along a dense periodic orbit (3 x npts).
    Returns Floquet multipliers.  Phase multiplier should be ~1."""
    npts = orb.shape[1]
    Nf, Zf, Ef = np.fft.fft(orb[0]), np.fft.fft(orb[1]), np.fft.fft(orb[2])
    kf = np.fft.fftfreq(npts, 1.0 / npts)

    def state(t):
        th = (t % T) / T * 2 * np.pi
        ex = np.exp(1j * kf * th)
        return np.array([np.real(np.dot(Nf, ex) / npts),
                         np.real(np.dot(Zf, ex) / npts),
                         np.real(np.dot(Ef, ex) / npts)])

    def A(t):
        y, yd = state(t), state(t - tau)
        Nt, Zt, Et = y
        Ztau = yd[1]
        St = r * Nt * (1 - Nt / K); Spt = r * (1 - 2 * Nt / K)
        qENt = q * Et * Nt
        d = qENt - St
        sp = sigmoid(k * d)
        val = softplus(d) - np.log(2.0) / k + delta
        h = sp if val > 0 else 0.0
        J0 = np.zeros((3, 3))
        J0[0, 0] = Spt - q * Et; J0[0, 2] = -q * Nt
        J0[1, 0] = h * (q * Et - Spt) / taum; J0[1, 1] = -1.0 / taum
        J0[1, 2] = h * q * Nt / taum
        Zden = max(Zref + Ztau, 1e-8)
        bracket = eta * Et * (Ztau / Dref - Et / Emax) + delta0 * Ztau / Zden
        J0[2, 2] = -(1.0 / Emax) * bracket + (1 - Et / Emax) * eta * (Ztau / Dref - 2 * Et / Emax)
        J1 = np.zeros((3, 3))
        J1[2, 1] = (1 - Et / Emax) * (eta * Et / Dref + delta0 * Zref / (Zden * Zden))
        return J0, J1

    nsteps = int(round(T / dt)); h = T / nsteps
    Whist = np.zeros((nsteps + 1, 3, 3)); Whist[0] = np.eye(3)

    def W_at(tt):
        if tt <= 0: return np.eye(3)
        i = int(tt / h)
        if i >= nsteps: return Whist[nsteps]
        fr = tt / h - i
        return (1 - fr) * Whist[i] + fr * Whist[i + 1]

    for i in range(nsteps):
        t = i * h
        J0, J1 = A(t)
        k1 = J0 @ Whist[i] + J1 @ W_at(t - tau)
        J0b, J1b = A(t + h / 2)
        k2 = J0b @ (Whist[i] + h / 2 * k1) + J1b @ W_at(t + h / 2 - tau)
        k3 = J0b @ (Whist[i] + h / 2 * k2) + J1b @ W_at(t + h / 2 - tau)
        J0c, J1c = A(t + h)
        k4 = J0c @ (Whist[i] + h * k3) + J1c @ W_at(t + h - tau)
        Whist[i + 1] = Whist[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return np.linalg.eigvals(Whist[nsteps])


def scan_variational(tau_list, N=240, K=None, csv_filename=None, dt_mon=0.01):
    """Track the stable large-amplitude branch via piecewise collocation +
    variational monodromy.  The collocation gives the correct orbit; the
    variational monodromy gives the multipliers."""
    print(f"{'tau':>9s} {'ok':>3s} {'T':>10s} {'res':>10s} "
          f"{'|mu_dom|':>9s} {'mu_dom':>22s} {'phase_mu':>9s} {'class':>6s}")
    prev = None
    prev2 = None
    rows = []
    for tau in tau_list:
        if prev is None:
            guess = prepare_first_guess(tau, N=N)
            if guess[0] is None:
                print(f"{tau:9.4f} no  (seed failed)"); continue
            s, u0, T0 = guess
        else:
            tau_p, s_p, u_p, T_p = prev
            s, u0 = adapt_solution(s_p, u_p, T_p, N)
            if prev2 is not None:
                tau_o, s_o, u_o, T_o = prev2
                T0 = T_p + (T_p - T_o) / (tau_p - tau_o) * (tau - tau_p) \
                    if abs(tau_p - tau_o) > 1e-12 else T_p
            else:
                T0 = T_p
        u, T, res, ok = solve_collocation(tau, s, u0, T0)
        if not ok:
            print(f"{tau:9.4f} no  {res:10.2e} (Newton failed)"); continue
        s, u = roll_phase(s, u)
        # resample collocation solution onto dense uniform mesh for monodromy
        n_dense = 2048
        s_d = np.linspace(0, 1, n_dense, endpoint=False)
        Pd = periodic_interp_matrix(s, s_d, m=5, deriv=0)
        orb = np.vstack([Pd @ u[:N], Pd @ u[N:2*N], Pd @ u[2*N:3*N]])
        ev = monodromy_variational(orb, T, tau, dt=dt_mon)
        ev = ev[np.argsort(-np.abs(ev))]
        i_triv = int(np.argmin(np.abs(ev - 1.0)))
        triv = ev[i_triv]
        nontriv = np.delete(ev, i_triv)
        dom = nontriv[0]
        cls = ""
        if abs(abs(dom) - 1.0) < 0.03:
            if abs(np.imag(dom)) < 0.05 and np.real(dom) > 0.90: cls = "SNPO"
            elif abs(np.imag(dom)) < 0.05 and np.real(dom) < -0.90: cls = "PD"
            else: cls = "Torus"
        print(f"{tau:9.4f} yes {T:10.3f} {res:10.2e} {abs(dom):9.5f} "
              f"({np.real(dom):+9.5f},{np.imag(dom):+9.5f}) {abs(triv):9.5f} {cls:>6s}")
        rows.append(dict(tau=tau, T=T, residual=res, mu_dom_abs=abs(dom),
                         mu_dom_real=float(np.real(dom)),
                         mu_dom_imag=float(np.imag(dom)),
                         phase_mu_abs=abs(triv), cls=cls))
        prev2 = prev
        prev = (tau, s, u, T)
    if csv_filename and rows:
        with open(csv_filename, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader(); w.writerows(rows)
        print(f"Saved: {csv_filename}")
    return rows
