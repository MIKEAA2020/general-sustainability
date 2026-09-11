"""
Robust Newton corrector using Levenberg-Marquardt-style regularization to handle
the poorly-conditioned Jacobian (cond ~ 1e7-1e8) encountered near tau~3, which
caused the plain linalg.solve-based Newton iteration to stagnate even though
direct DDE simulation confirms the periodic orbit itself varies completely
smoothly there (no genuine bifurcation) -- i.e. the earlier stall was a solver
artifact, not a real dynamical feature.
"""
import jax
import jax.numpy as jnp
from jax import config
config.update("jax_enable_x64", True)
import numpy as np

def lm_corrector(residual_fn, v0, tol=1e-12, maxit=100, lam0=1e-6, verbose=False):
    jac_fn = jax.jacobian(residual_fn)
    v = jnp.array(v0)
    lam = lam0
    f0 = residual_fn(v)
    cost0 = float(jnp.dot(f0, f0))
    for it in range(maxit):
        resnorm = float(jnp.linalg.norm(f0))
        if verbose and it % 10 == 0:
            print(f"    LM iter {it}: residual={resnorm:.4e}  lambda={lam:.2e}")
        if resnorm < tol:
            return np.array(v), True, resnorm
        J = jac_fn(v)
        JTJ = J.T @ J
        JTf = J.T @ f0
        n = JTJ.shape[0]
        # Levenberg-Marquardt normal equations with adaptive damping
        success = False
        for _ in range(30):
            A = JTJ + lam*jnp.diag(jnp.diag(JTJ) + 1e-12)
            try:
                dv = jnp.linalg.solve(A, -JTf)
            except Exception:
                lam *= 10
                continue
            v_trial = v + dv
            f_trial = residual_fn(v_trial)
            cost_trial = float(jnp.dot(f_trial, f_trial))
            if cost_trial < cost0:
                v = v_trial
                f0 = f_trial
                cost0 = cost_trial
                lam = max(lam*0.3, 1e-14)
                success = True
                break
            else:
                lam *= 3.0
        if not success:
            return np.array(v), False, resnorm
    return np.array(v), False, float(jnp.linalg.norm(f0))
