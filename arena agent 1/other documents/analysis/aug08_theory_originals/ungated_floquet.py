"""
ungated_floquet.py
==================

Floquet-multiplier analysis of the UNGATED three-state core
(Eq. eq:stock-core / eq:Z-core / eq:effort-core, i.e. the original ungated
effort law: Edot = eta*E*(Z_tau/Dref - E/Emax) + delta0*Z_tau/(Zref+Z_tau),
no (1-E/Emax) gate), Candidate A: r=0.02, K=100, q=0.001, eta=0.914,
Emax=30, delta0=0.01, Dref=1.0, taum=5, k=10, delta=ln2/10, Zref=1.0.

Two orbits are analysed:
  (1) the large-amplitude stable cycle in the upper bistable window at
      tau=131.8 yr (period ~135.6 yr) -- the orbit whose earlier-reported
      ~0.08 amplitude modulation (from an adaptive-tolerance integrator) was
      NOT reproduced by fixed-step RK4. If this orbit is a stable limit
      cycle, ALL non-trivial Floquet multipliers lie strictly inside the
      unit circle (only the trivial phase multiplier equals 1), which
      definitively rules out a torus (a torus would show a second multiplier
      on the unit circle) and resolves the modulation discrepancy in favour
      of an integrator artifact.
  (2) the small unstable periodic orbit near the lower Hopf point
      tau_- = 6.881 yr (the unstable branch whose existence the SNPO
      classification requires). If its largest Floquet multiplier exceeds 1,
      the orbit is unstable, consistent with a subcritical Hopf (the
      unstable cycle lives on the stable side tau > tau_- and collides with
      the stable branch at the fold).

Method: Fourier spectral collocation (Newton with jax Jacobian) converges
each orbit to residual < 1e-9; then the monodromy (fundamental matrix of the
linearised DDE over one period) is built as a segment-discretised linear
operator (dimension 3*(n_tau+1), n_tau = ceil(tau/dt)) and its dominant
eigenvalues are computed by Krylov iteration (scipy.sparse.linalg.eigs),
which avoids forming the dense monodromy matrix.

Also implements a correct method-of-steps ADAPTIVE (solve_ivp RK45) DDE
integration to directly test whether the ~0.08 modulation appears under an
adaptive integrator with strict tolerances.
"""
import numpy as np
import scipy.sparse.linalg as spla
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d, CubicSpline

# ---------------- ungated RHS (numba) ----------------
from numba import njit
from elevation_solvers import PARAMS_A, params_arr

@njit(fastmath=True)
def rhs_ungated_local(N, Z, E, Ztau, p):
    r_, K_, q_ = p[0], p[1], p[2]
    eta_, Emax_, Dref_ = p[3], p[4], p[6]
    delta0_, Zref_, k_, taum_ = p[9], p[8], p[7], p[5]
    delta_ = p[10]
    S = r_*N*(1 - N/K_)
    C = q_*E*N
    Ndot = S - C
    ku = k_*(C - S)
    if ku > 30.0:
        sp = ku/k_
    elif ku < -30.0:
        sp = 0.0
    else:
        sp = np.log1p(np.exp(ku))/k_
    inner = sp - np.log(2.0)/k_ + delta_
    Zdot = (max(0.0, inner) - Z)/taum_
    Edot = eta_*E*(Ztau/Dref_ - E/Emax_) + delta0_*Ztau/(Zref_ + Ztau)
    return Ndot, Zdot, Edot

@njit(fastmath=True)
def sim_ungated(N0, Z0, E0, tau, T, dt, p):
    """Fixed-step RK4-DDE, ungated. Returns sampled (N,Z,E) every 0.25 yr and final state."""
    n_delay = max(1, int(round(tau/dt)))
    N, Z, E = N0, Z0, E0
    buf = np.full(n_delay + 1, Z); idx = 0
    n = int(T/dt); out = np.zeros((int(n/5), 3)); oi = 0
    for step in range(n):
        Ztau = buf[idx]
        k1N,k1Z,k1E = rhs_ungated_local(N,Z,E,Ztau,p)
        k2N,k2Z,k2E = rhs_ungated_local(N+dt/2*k1N,Z+dt/2*k1Z,E+dt/2*k1E,Ztau,p)
        k3N,k3Z,k3E = rhs_ungated_local(N+dt/2*k2N,Z+dt/2*k2Z,E+dt/2*k2E,Ztau,p)
        k4N,k4Z,k4E = rhs_ungated_local(N+dt*k3N,Z+dt*k3Z,E+dt*k3E,Ztau,p)
        N = N + dt/6*(k1N+2*k2N+2*k3N+k4N)
        Z = Z + dt/6*(k1Z+2*k2Z+2*k3Z+k4Z)
        E = E + dt/6*(k1E+2*k2E+2*k3E+k4E)
        if N < 0.0: N = 0.0
        if E < 0.0: E = 0.0
        buf[idx] = Z; idx = (idx + 1) % (n_delay + 1)
        if step % 5 == 0 and oi < out.shape[0]:
            out[oi,0]=N; out[oi,1]=Z; out[oi,2]=E; oi += 1
    return out[:oi], N, Z, E

# ---------------- Fourier collocation (ungated) ----------------
import jax
import jax.numpy as jnp
from jax import config
config.update("jax_enable_x64", True)

def fourier_diff_matrix(M):
    h = 2*np.pi/M
    col = np.zeros(M)
    if M % 2 == 0:
        for i in range(1, M):
            col[i] = 0.5*(-1.0)**i/np.tan(i*h/2)
    else:
        for i in range(1, M):
            col[i] = 0.5*(-1.0)**i/np.sin(i*h/2)
    D = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            D[i, j] = col[(i - j) % M]
    return D

def make_ungated_solver(M, params, pin_index, pin_value, tau_val, floor_sharpness=200.0):
    D = jnp.array(fourier_diff_matrix(M))
    r_, K_, q_ = params['r'], params['K'], params['q']
    eta_, Emax_, Dref_ = params['eta'], params['Emax'], params['Dref']
    delta0_, Zref_, k_, taum_ = params['delta0'], params['Zref'], params['k'], params['taum']
    delta_ = np.log(2.0)/k_
    kk = jnp.arange(M); kk = jnp.where(kk > M//2, kk - M, kk)

    def softplus_jax(x):
        return jax.nn.softplus(k_*x)/k_

    def soft_floor(x):
        return jax.nn.softplus(floor_sharpness*x)/floor_sharpness

    def fourier_shift(x, shift_frac):
        Xk = jnp.fft.fft(x)
        phase = jnp.exp(-1j*2*jnp.pi*shift_frac*kk)
        return jnp.real(jnp.fft.ifft(Xk*phase))

    def rhs(N, Z, Zd, E):
        S = r_*N*(1 - N/K_)
        C = q_*E*N
        fN = S - C
        inner = softplus_jax(C - S) - np.log(2.0)/k_ + delta_
        fZ = (1.0/taum_)*(soft_floor(inner) - Z)
        fE = eta_*E*(Zd/Dref_ - E/Emax_) + delta0_*Zd/(Zref_ + Zd)
        return fN, fZ, fE

    def residual(v):
        N = v[0:M]; Z = v[M:2*M]; E = v[2*M:3*M]; T = v[3*M]
        dN = D @ N; dZ = D @ Z; dE = D @ E
        Zd = fourier_shift(Z, tau_val[0]/T)
        fN, fZ, fE = rhs(N, Z, Zd, E)
        resN = (2*jnp.pi/T)*dN - fN
        resZ = (2*jnp.pi/T)*dZ - fZ
        resE = (2*jnp.pi/T)*dE - fE
        pin = jnp.array([N[pin_index] - pin_value])
        return jnp.concatenate([resN, resZ, resE, pin])

    jac = jax.jacobian(residual)

    def solve(v0, tol=1e-10, maxit=80):
        v = jnp.array(v0, dtype=jnp.float64)
        for it in range(maxit):
            F = residual(v)
            rn = float(jnp.linalg.norm(F))
            if rn < tol:
                return np.array(v), True, rn
            J = jac(v)
            try:
                dv = jnp.linalg.solve(J, -F)
            except Exception:
                return np.array(v), False, rn
            alpha = 1.0; ok = False
            for _ in range(50):
                vt = v + alpha*dv
                if float(jnp.linalg.norm(residual(vt))) < rn:
                    ok = True; break
                alpha *= 0.5
            if not ok:
                return np.array(v), False, rn
            v = v + alpha*dv
        return np.array(v), False, rn

    return solve, residual

def period_and_state_from_sim(Ns, Zs, Es, dt_out=0.25):
    """Detect the period from the N series (autocorrelation peaks) and return
    (period, index-of-last-peak)."""
    N = Ns - Ns.mean()
    ac = np.correlate(N, N, mode='full')[len(N)-1:]
    peaks = [i for i in range(1, len(ac)-1)
             if ac[i] > ac[i-1] and ac[i] > ac[i+1] and ac[i] > 0.5*ac[0]]
    if len(peaks) < 2:
        return None, None
    period = (peaks[1]-peaks[0])*dt_out
    return period, peaks[-1]

def sample_period(Ns, Zs, Es, start_idx, period, dt_out, M):
    ppp = int(round(period/dt_out))
    idxs = (start_idx + np.arange(M)*(ppp/M)).astype(int)
    if idxs.max() >= len(Ns):
        return None
    return Ns[idxs], Zs[idxs], Es[idxs], ppp

# ---------------- segment-discretised monodromy (Krylov) ----------------
def make_monodromy_op(orbit, tau, dt):
    """Return a LinearOperator whose action advances a perturbation segment
    (dimension 3*(n_tau+1)) of the linearised DDE around `orbit` over one period.
    orbit = dict(Nf, Zf, Ef, T)."""
    M = len(orbit['Nf'].x)
    T = orbit['T']
    n_tau = max(1, int(round(tau/dt)))
    nseg = 3*(n_tau+1)
    pa = params_arr(PARAMS_A())

    # Precompute linearisation pieces via cubic splines of the orbit
    Nf, Zf, Ef = orbit['Nf'], orbit['Zf'], orbit['Ef']

    def jacobians(t):
        tt = t % T
        N = float(Nf(tt)); Z = float(Zf(tt)); E = float(Ef(tt))
        Ztau = float(Zf((tt - tau) % T))
        r_, K_, q_ = pa[0], pa[1], pa[2]
        eta_, Emax_, Dref_ = pa[3], pa[4], pa[6]
        delta0_, Zref_, k_, taum_ = pa[9], pa[8], pa[7], pa[5]
        Sp = r_*(1 - 2*N/K_)
        u = q_*E*N - r_*N*(1-N/K_)
        # softplus derivative = sigmoid(k*u); floor-active factor
        if k_*u > 30:
            sp = u; sp_prime = 1.0
        elif k_*u < -30:
            sp = 0.0; sp_prime = 0.0
        else:
            eu = np.exp(k_*u)
            sp = np.log1p(eu)/k_; sp_prime = eu/(1.0+eu)
        floor_active = 1.0 if (sp - np.log(2.0)/k_ + pa[10]) > 0 else 0.0
        dsrc_dN = sp_prime*(q_*E - Sp)*floor_active
        dsrc_dE = sp_prime*q_*N*floor_active
        dEdot_dE = eta_*(Ztau/Dref_ - 2*E/Emax_)
        dEdot_dZtau = eta_*E/Dref_ + delta0_*Zref_/(Zref_+Ztau)**2
        J = np.array([[Sp - q_*E, 0.0, -q_*N],
                      [dsrc_dN/taum_, -1.0/taum_, dsrc_dE/taum_],
                      [0.0, 0.0, dEdot_dE]])
        Jt = np.zeros((3,3)); Jt[2,1] = dEdot_dZtau
        return J, Jt

    @njit(fastmath=True)
    def advance_seg(seg, n_tau, dt, T, ja, jb):
        """ja, jb: precomputed Jacobian arrays? -- not feasible; instead use
        the jacobians() closure via passing arrays. We'll implement the
        advance in Python (slower but correct) since dimension is small."""
        pass

    # Python implementation of the monodromy action.
    # The linearized advance is the EXACT linearization of the nonlinear RK4
    # scheme used in sim_ungated (which freezes the delayed value Zdel across
    # the four RK4 stages but evaluates the RHS at the intermediate states),
    # so the Jacobians are evaluated at the four stage times t, t+h/2, t+h/2, t+h.
    def advance(seg):
        x = seg[-3:].copy()
        n_steps = int(round(T/dt))
        buf = np.zeros((n_tau+1, 3))
        for j in range(n_tau+1):
            buf[j] = seg[3*j:3*j+3]
        idx = n_tau
        h = dt
        for step in range(n_steps):
            t0_ = step*h
            J1, Jt1 = jacobians(t0_)
            J2, Jt2 = jacobians(t0_ + 0.5*h)
            J4, Jt4 = jacobians(t0_ + h)
            Zdel = buf[(idx - n_tau) % (n_tau+1)]
            k1 = J1@x + Jt1@Zdel
            k2 = J2@(x + 0.5*h*k1) + Jt2@Zdel
            k3 = J2@(x + 0.5*h*k2) + Jt2@Zdel
            k4 = J4@(x + h*k3) + Jt4@Zdel
            x = x + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
            idx = (idx+1) % (n_tau+1); buf[idx] = x
        newseg = np.zeros(nseg)
        for j in range(n_tau+1):
            newseg[3*j:3*j+3] = buf[(idx - n_tau + j) % (n_tau+1)]
        return newseg

    def matvec(v):
        return advance(v)

    A = spla.LinearOperator((nseg, nseg), matvec=matvec, dtype=np.float64)
    return A, nseg

def top_floquet(orbit, tau, dt, k=8, ncv=None):
    A, nseg = make_monodromy_op(orbit, tau, dt)
    ncv = ncv or min(4*k, nseg)
    try:
        ev, _ = spla.eigs(A, k=k, which='LM', ncv=ncv, maxiter=2000, tol=1e-9)
        return np.sort_complex(ev), nseg
    except Exception as e:
        print("eigs failed:", e)
        return None, nseg

# ---------------- method-of-steps adaptive DDE ----------------
def adaptive_method_of_steps(tau, y0_hist, T_run, rtol=1e-9, seg_len=None):
    """Integrate the ungated DDE with solve_ivp RK45 using the method of
    steps: integrate over successive windows of length seg_len (<= tau), each
    time building the delay history from the previously computed segments via
    cubic interpolation. y0_hist: (t_grid, [N,Z,E]) history on [-tau, 0].
    Returns (t, [N,Z,E]) sampled at 0.25 yr."""
    seg_len = seg_len or min(tau, 5.0)
    pa = params_arr(PARAMS_A())
    # initial history interpolation
    th, Yh = y0_hist
    def Z_of(t):
        # clamp into history window
        tt = min(max(t, th[0]), th[-1])
        return float(np.interp(tt, th, Yh[:,1]))
    # collect segments
    seg_ts = [th.copy()]
    seg_vals = [Yh.copy()]
    t0 = 0.0
    # we integrate time from t0; history covers [t0-tau, t0]
    # but Yh covers [-tau,0] with last point = t0. Good.
    # We'll integrate [t0, t0+seg_len] repeatedly, appending each segment.
    # For delay Z(t-tau): t-tau ranges over [-tau, t0] initially; as t advances
    # beyond tau, we need the just-computed segments. Build a global interpolant
    # from all collected segments.
    all_t = seg_ts[0].copy()
    all_N = seg_vals[0][:,0].copy(); all_Z = seg_vals[0][:,1].copy(); all_E = seg_vals[0][:,2].copy()
    # Note: th ends at 0; seg_ts[0] ends at 0 = t0. So integrate from t0.
    n_windows = int(np.ceil(T_run/seg_len))
    for w in range(n_windows):
        ta, tb = t0 + w*seg_len, t0 + (w+1)*seg_len
        if ta >= t0 + T_run: break
        tb = min(tb, t0 + T_run)
        # Z history interpolant over all_t (covers at least [tb-tau, tb] since seg_len<=tau)
        Z_hist = interp1d(all_t, all_Z, kind='cubic', fill_value='extrapolate', bounds_error=False)
        def rhs(t, y):
            N, Z, E = y
            Zd = max(0.0, float(Z_hist(t - tau)))
            return rhs_ungated_local(N, Z, E, Zd, pa)
        y_start = np.array([all_N[-1], all_Z[-1], all_E[-1]])
        te = np.linspace(ta, tb, int((tb-ta)/0.25)+1)
        sol = solve_ivp(rhs, [ta, tb], y_start, method='RK45', rtol=rtol, atol=rtol*1e-1,
                        max_step=2.0, t_eval=te)
        # append to history (skip first point to avoid duplicate window boundary)
        all_t = np.concatenate([all_t, sol.t[1:]])
        all_N = np.concatenate([all_N, sol.y[0][1:]])
        all_Z = np.concatenate([all_Z, sol.y[1][1:]])
        all_E = np.concatenate([all_E, sol.y[2][1:]])
        if sol.y.shape[1] == 0:
            break
    return all_t, np.column_stack([all_N, all_Z, all_E])
