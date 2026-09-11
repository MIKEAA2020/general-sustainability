"""
Pseudo-arclength continuation (PALC) for periodic orbits of the CORRECTED
core DDE (Eq. eq:effort-core-corrected, the (1-E/Emax)-gated law), built to
resolve the fold in the small unstable orbit's amplitude discovered by
natural-parameter continuation in scratch_cont_check2.py (which showed the
amplitude growing smoothly from ~1.05 at tau=3.7 to ~19.5 near tau=5.4-5.7,
with residuals degrading exactly as expected approaching a turning point --
contradicting a previous, hardcoded claim in verify_snpo_fold_refinement.py
that this orbit's amplitude stays flat near 1.05 throughout).

Unknowns: v = [N(1..M), Z(1..M), E(1..M), T, tau]  (size 3M+2)
"""
import jax
import jax.numpy as jnp
from jax import config
config.update("jax_enable_x64", True)
import numpy as np
from corrected_core_common import PARAMS_A


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


def make_residual_free_tau(M, params, pin_index, pin_value, floor_sharpness=200.0):
    """Residual as a function of v=[N,Z,E,T,tau] (size 3M+2), tau now free."""
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

    def residual(v):
        N = v[0:M]; Z = v[M:2*M]; E = v[2*M:3*M]; T = v[3*M]; tau = v[3*M+1]
        dN = D @ N; dZ = D @ Z; dE = D @ E
        shift_frac = tau / T
        Zd = fourier_shift_jax(Z, shift_frac)
        fN, fZ, fE = rhs(N, Z, Zd, E)
        resN = (2*jnp.pi/T)*dN - fN
        resZ = (2*jnp.pi/T)*dZ - fZ
        resE = (2*jnp.pi/T)*dE - fE
        pin_res = jnp.array([N[pin_index] - pin_value])
        return jnp.concatenate([resN, resZ, resE, pin_res])  # size 3M+1

    return residual


def newton_corrector(residual_fn, v0, tol=1e-11, maxit=60, verbose=False):
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


def palc_step(residual_free_tau_fn, v_prev, tangent, ds):
    """One pseudo-arclength continuation step: v = [N,Z,E,T,tau], tangent is a
    unit vector in the same (3M+2)-dim space, secant-approximated by the caller."""
    v_predictor = v_prev + ds * tangent

    def augmented_residual(v):
        base_res = residual_free_tau_fn(v)  # size 3M+1
        arclength_res = jnp.dot(jnp.array(tangent), v - jnp.array(v_predictor))
        return jnp.concatenate([base_res, jnp.array([arclength_res])])  # size 3M+2

    v_new, converged, resnorm = newton_corrector(augmented_residual, v_predictor)
    return v_new, converged, resnorm
