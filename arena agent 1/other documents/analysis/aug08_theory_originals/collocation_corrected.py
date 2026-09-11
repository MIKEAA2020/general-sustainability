"""
Fourier spectral collocation solver + pseudo-arclength continuation for periodic
orbits of the CORRECTED core DDE (Eq. eq:effort-core-corrected):

    Ndot = S(N) - q*E*N
    Zdot = (1/taum)*( max(0, softplus_k(qEN-S(N)) - ln2/k + delta) - Z )
    Edot = (1 - E/Emax) * [ eta*E*(Zd/Dref - E/Emax) + delta0*Zd/(Zref+Zd) ]

where Zd = Z(t-tau). Represent one period on M equally-spaced collocation
points; differentiation via the exact Fourier differentiation matrix; delay
shift via exact Fourier phase shift (valid since the periodic-orbit
restriction of Z is itself periodic with period T). Unknowns v = [N,Z,E,T]
(3M+1) at fixed tau, or v=[N,Z,E,T,tau] (3M+2) for pseudo-arclength stepping
through a fold.

max(0,.) in the Z equation is smoothed with a soft-plus of high sharpness for
differentiability (the floor is inactive at any point on a moderate-amplitude
orbit above N~30, so this barely matters, but keeps autodiff well-defined).
"""
import jax
import jax.numpy as jnp
from jax import config
config.update("jax_enable_x64", True)
import numpy as np

def fourier_diff_matrix_np(M):
    h = 2*np.pi/M
    col = np.zeros(M)
    if M % 2 == 0:
        for i in range(1, M):
            col[i] = 0.5*(-1)**i/np.tan(i*h/2)
    else:
        for i in range(1, M):
            col[i] = 0.5*(-1)**i/np.sin(i*h/2)
    D = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            D[i, j] = col[(i - j) % M]
    return D

def make_residual_fn(M, params, pin_index, pin_value, floor_sharpness=200.0):
    D = jnp.array(fourier_diff_matrix_np(M))
    r_, K_, q_ = params['r'], params['K'], params['q']
    eta_, Emax_, Dref_ = params['eta'], params['Emax'], params['Dref']
    delta0_, Zref_, k_, taum_ = params['delta0'], params['Zref'], params['k'], params['taum']
    delta_ = jnp.log(2.0)/k_
    kk = jnp.arange(M)
    kk = jnp.where(kk > M//2, kk - M, kk)

    def softplus_jax(x):
        return jax.nn.softplus(k_*x)/k_

    def soft_floor(x):
        # smooth approx to max(0,x)
        return jax.nn.softplus(floor_sharpness*x)/floor_sharpness

    def fourier_shift_jax(x, shift_frac):
        Xk = jnp.fft.fft(x)
        phase = jnp.exp(-1j*2*jnp.pi*shift_frac*kk)
        return jnp.real(jnp.fft.ifft(Xk*phase))

    def rhs(N, Z, Zd, E):
        S = r_*N*(1-N/K_)
        C = q_*E*N
        fN = S - C
        inner = softplus_jax(C - S) - jnp.log(2.0)/k_ + delta_
        fZ = (1.0/taum_)*(soft_floor(inner) - Z)
        bracket = eta_*E*(Zd/Dref_ - E/Emax_) + delta0_*Zd/(Zref_ + Zd)
        fE = (1.0 - E/Emax_) * bracket
        return fN, fZ, fE

    def residual_fixed_tau(v, tau):
        N = v[0:M]; Z = v[M:2*M]; E = v[2*M:3*M]; T = v[3*M]
        dN = D @ N; dZ = D @ Z; dE = D @ E
        shift_frac = tau / T
        Zd = fourier_shift_jax(Z, shift_frac)
        fN, fZ, fE = rhs(N, Z, Zd, E)
        resN = (2*jnp.pi/T)*dN - fN
        resZ = (2*jnp.pi/T)*dZ - fZ
        resE = (2*jnp.pi/T)*dE - fE
        pin_res = jnp.array([N[pin_index] - pin_value])
        return jnp.concatenate([resN, resZ, resE, pin_res])

    def residual_with_tau(v):
        # v = [N,Z,E,T,tau], tau is now an unknown too (for pseudo-arclength)
        tau = v[3*M+1]
        return residual_fixed_tau(v[:3*M+1], tau)

    return residual_fixed_tau, residual_with_tau, rhs

def newton_corrector(residual_fn, v0, tol=1e-10, maxit=60, verbose=False):
    jac_fn = jax.jacobian(residual_fn)
    v = jnp.array(v0)
    resnorm = None
    for it in range(maxit):
        f0 = residual_fn(v)
        resnorm = float(jnp.linalg.norm(f0))
        if verbose:
            print(f"    iter {it}: |res|={resnorm:.4e}")
        if resnorm < tol:
            return np.array(v), True, resnorm
        J = jac_fn(v)
        try:
            dv = jnp.linalg.solve(J, -f0)
        except Exception:
            return np.array(v), False, resnorm
        alpha = 1.0
        improved = False
        for _ in range(50):
            v_trial = v + alpha*dv
            rn = float(jnp.linalg.norm(residual_fn(v_trial)))
            if rn < resnorm:
                improved = True
                break
            alpha *= 0.5
        if not improved:
            return np.array(v), False, resnorm
        v = v + alpha*dv
    return np.array(v), False, resnorm
