"""
Fourier spectral collocation periodic-orbit solver for the corrected three-state core
(eq:stock-core, eq:Z-core, eq:effort-core-corrected), mirroring palc_corrected.py's
residual structure exactly (soft_floor regularisation of max(0,.), (1-E/Emax) gate).

Solves for a periodic orbit at FIXED tau: v = [N(0..M-1), Z(0..M-1), E(0..M-1), T].
Uses jax for exact Jacobians.
"""
import numpy as np
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

def make_solver(M, params, pin_index, pin_value, floor_sharpness=200.0):
    D = jnp.array(fourier_diff_matrix(M))
    r_, K_, q_ = params['r'], params['K'], params['q']
    eta_, Emax_, Dref_ = params['eta'], params['Emax'], params['Dref']
    delta0_, Zref_, k_, taum_ = params['delta0'], params['Zref'], params['k'], params['taum']
    delta_ = np.log(2.0)/k_
    kk = jnp.arange(M)
    kk = jnp.where(kk > M//2, kk - M, kk)

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
        bracket = eta_*E*(Zd/Dref_ - E/Emax_) + delta0_*Zd/(Zref_ + Zd)
        fE = (1.0 - E/Emax_)*bracket
        return fN, fZ, fE

    def residual(v):
        N = v[0:M]; Z = v[M:2*M]; E = v[2*M:3*M]; T = v[3*M]
        dN = D @ N; dZ = D @ Z; dE = D @ E
        shift_frac = tau_val[0] / T
        Zd = fourier_shift(Z, shift_frac)
        fN, fZ, fE = rhs(N, Z, Zd, E)
        resN = (2*jnp.pi/T)*dN - fN
        resZ = (2*jnp.pi/T)*dZ - fZ
        resE = (2*jnp.pi/T)*dE - fE
        pin = jnp.array([N[pin_index] - pin_value])
        return jnp.concatenate([resN, resZ, resE, pin])

    # wrap tau as mutable closure
    tau_val = [0.0]
    jac_fn = jax.jacobian(residual)

    def solve(v0, tau, tol=1e-10, maxit=100, verbose=False):
        tau_val[0] = tau
        v = jnp.array(v0, dtype=jnp.float64)
        for it in range(maxit):
            F = residual(v)
            rn = float(jnp.linalg.norm(F))
            if verbose and it % 10 == 0:
                print(f"     iter {it}: |F|={rn:.3e}")
            if rn < tol:
                return np.array(v), True, rn
            J = jac_fn(v)
            try:
                dv = jnp.linalg.solve(J, -F)
            except Exception:
                return np.array(v), False, rn
            # damped step
            alpha = 1.0; ok = False
            for _ in range(60):
                vt = v + alpha*dv
                if float(jnp.linalg.norm(residual(vt))) < rn:
                    ok = True; break
                alpha *= 0.5
            if not ok:
                return np.array(v), False, rn
            v = v + alpha*dv
        return np.array(v), False, rn

    return solve, residual

def cycle_state_from_sim(N0, Z0, E0, tau, Tsim, dt, p, gated, M=129):
    """Simulate long enough to get onto the cycle, then sample one period at M points."""
    from elevation_solvers import simulate_three, params_arr
    pa = params_arr(p)
    # warm up
    Nf, Zf, Ef, _ = simulate_three(N0, Z0, E0, tau, Tsim, dt, pa, gated)
    # now run again capturing full series (coarse) to detect period and sample
    from numba import njit
    from elevation_solvers import rhs_three
    @njit(fastmath=True)
    def series(N0,Z0,E0,tau,T,dt,p,gated,step_out):
        n_delay=max(1,int(round(tau/dt)))
        N,Z,E=N0,Z0,E0
        buf=np.full(n_delay+1,Z); idx=0
        n=int(T/dt); out=np.zeros((int(n/step_out),3)); oi=0
        for step in range(n):
            Ztau=buf[idx]
            k1N,k1Z,k1E = rhs_three(N,Z,E,Ztau,p,gated)
            k2N,k2Z,k2E = rhs_three(N+dt/2*k1N,Z+dt/2*k1Z,E+dt/2*k1E,Ztau,p,gated)
            k3N,k3Z,k3E = rhs_three(N+dt/2*k2N,Z+dt/2*k2Z,E+dt/2*k2E,Ztau,p,gated)
            k4N,k4Z,k4E = rhs_three(N+dt*k3N,Z+dt*k3Z,E+dt*k3E,Ztau,p,gated)
            N=N+dt/6*(k1N+2*k2N+2*k3N+k4N); Z=Z+dt/6*(k1Z+2*k2Z+2*k3Z+k4Z); E=E+dt/6*(k1E+2*k2E+2*k3E+k4E)
            if N<0: N=0.0
            buf[idx]=Z; idx=(idx+1)%(n_delay+1)
            if step%step_out==0 and oi<out.shape[0]: out[oi]=N; oi+=1
        return out
    # capture at dt_out=0.25 yr
    dt_out = 0.25
    s = series(Nf, Zf, Ef, tau, 2000.0, dt, pa, gated, int(dt_out/dt))
    Ns = s[:,0]
    # find period via autocorrelation of detrended N
    Ns = Ns - Ns.mean()
    ac = np.correlate(Ns, Ns, mode='full')[len(Ns)-1:]
    peaks = []
    for i in range(1, len(ac)-1):
        if ac[i] > ac[i-1] and ac[i] > ac[i+1] and ac[i] > 0.5*ac[0]:
            peaks.append(i)
    if len(peaks) < 2:
        return None
    period_samples = peaks[1] - peaks[0]
    period = period_samples * dt_out
    # sample M points over one period starting at a peak
    start = peaks[-1]
    idxs = (start + np.arange(M)*(period_samples/M)).astype(int)
    # need series longer than start+period: rerun longer if needed
    need = int((start + period_samples) * dt_out / dt)
    T2 = need*dt + 2000.0
    s2 = series(Nf, Zf, Ef, tau, T2, dt, pa, gated, int(dt_out/dt))
    N2 = s2[:,0]; Z2 = s2[:,1]; E2 = s2[:,2]
    if idxs.max() >= len(N2):
        return None
    return N2[idxs], Z2[idxs], E2[idxs], period
