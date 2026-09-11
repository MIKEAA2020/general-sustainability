"""
Pseudo-arclength continuation (PALC) of periodic orbits of the corrected core DDE
in the delay parameter tau. This is the correct tool for tracing an unstable
periodic orbit through a fold (SNPO): shooting/simulation can only ever shadow
an unstable orbit transiently (any perturbation grows), but a boundary-value
Newton solver does not care about dynamical stability -- it just solves
F(state) = 0, and pseudo-arclength parametrization lets it continue smoothly
through a turning point in tau where naive "solve for fixed tau" would fail
(the branch folds back, so tau is not a valid continuation parameter locally).

Unknowns: v = [N(1..M), Z(1..M), E(1..M), T, tau]   (size 3M+2)
Equations:
  - 3M dynamics collocation residuals (function of tau now, not a fixed parameter)
  - 1 pin condition (fixes translation invariance in phase, excludes the
    trivial equilibrium "orbit")
  - 1 pseudo-arclength constraint:  t . (v - v_predictor) = 0
    where t is the (secant-approximated) unit tangent to the branch.
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

def make_dynamics_residual(M, params, pin_index, pin_value):
    D = jnp.array(fourier_diff_matrix_np(M))
    r_, K_, q_ = params['r'], params['K'], params['q']
    eta_, Emax_, Dref_ = params['eta'], params['Emax'], params['Dref']
    delta0_, Zref_, k_, taum_ = params['delta0'], params['Zref'], params['k'], params['taum']
    kk = jnp.arange(M)
    kk = jnp.where(kk > M//2, kk - M, kk)

    def softplus_jax(x):
        return jax.nn.softplus(k_*x)/k_

    def fourier_shift_jax(x, shift_frac):
        Xk = jnp.fft.fft(x)
        phase = jnp.exp(-1j*2*jnp.pi*shift_frac*kk)
        return jnp.real(jnp.fft.ifft(Xk*phase))

    def residual(v):
        # v = [N(M), Z(M), E(M), T, tau]
        N = v[0:M]; Z = v[M:2*M]; E = v[2*M:3*M]; T = v[3*M]; tau = v[3*M+1]
        dN_dtheta = D @ N
        dZ_dtheta = D @ Z
        dE_dtheta = D @ E

        shift_frac = tau / T
        Zdelayed = fourier_shift_jax(Z, shift_frac)

        S = r_*N*(1-N/K_)
        C = q_*E*N
        fN = S - C
        fZ = (1/taum_)*(softplus_jax(C - S) - Z)
        fE = eta_*E*(Zdelayed/Dref_ - E/Emax_) + delta0_*Zdelayed/(Zref_ + Zdelayed)

        resN = (2*jnp.pi/T)*dN_dtheta - fN
        resZ = (2*jnp.pi/T)*dZ_dtheta - fZ
        resE = (2*jnp.pi/T)*dE_dtheta - fE

        pin_res = jnp.array([N[pin_index] - pin_value])
        return jnp.concatenate([resN, resZ, resE, pin_res])   # size 3M+1

    return residual

def newton_corrector(residual_and_arclength_fn, v0, tol=1e-12, maxit=50, verbose=False):
    jac_fn = jax.jacobian(residual_and_arclength_fn)
    v = jnp.array(v0)
    for it in range(maxit):
        f0 = residual_and_arclength_fn(v)
        resnorm = float(jnp.linalg.norm(f0))
        if verbose:
            print(f"    corrector iter {it}: residual={resnorm:.3e}")
        if resnorm < tol:
            return np.array(v), True, resnorm
        J = jac_fn(v)
        try:
            dv = jnp.linalg.solve(J, -f0)
        except Exception:
            return np.array(v), False, resnorm
        alpha = 1.0
        improved = False
        for _ in range(40):
            v_trial = v + alpha*dv
            f_trial = residual_and_arclength_fn(v_trial)
            if float(jnp.linalg.norm(f_trial)) < resnorm:
                improved = True
                break
            alpha *= 0.5
        if not improved:
            return np.array(v), False, resnorm
        v = v + alpha*dv
    return np.array(v), False, resnorm

def continuation_step(residual_fn, v_prev, v_prevprev, ds, pin_scale=None):
    """
    One pseudo-arclength continuation step.
    v_prev, v_prevprev: last two converged points (arrays of size 3M+2), used to
    build a secant tangent. On the first step (v_prevprev is None), a simple
    tau-increment predictor is used instead.
    """
    n = len(v_prev)
    if v_prevprev is None:
        # bootstrap: perturb tau slightly, keep state, as the initial predictor
        tangent = np.zeros(n)
        tangent[-1] = 1.0  # pure tau direction
    else:
        tangent = v_prev - v_prevprev
        tangent = tangent / np.linalg.norm(tangent)

    v_predictor = v_prev + ds * tangent

    def augmented_residual(v):
        base_res = residual_fn(v)  # size 3M+1
        arclength_res = jnp.dot(jnp.array(tangent), v - jnp.array(v_predictor))
        return jnp.concatenate([base_res, jnp.array([arclength_res])])  # size 3M+2

    v_new, converged, resnorm = newton_corrector(augmented_residual, v_predictor)
    return v_new, converged, resnorm, tangent
