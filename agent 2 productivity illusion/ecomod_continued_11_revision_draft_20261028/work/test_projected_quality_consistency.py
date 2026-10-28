"""Numerical consistency test for the projected quality law in the local draft.

This test distinguishes (i) equality of two discrete Euler updates at the same
grid, and (ii) convergence of the finite-step trajectory to the continuous
projected baseline. It is not evidence of historical C10 code provenance.
"""
from __future__ import annotations

import numpy as np

import twoland_fixed as legacy_clip
import twoland_fixed_projected as projected


def scalar_quality(tau_g: float, dt: float, T: float = 60.0, q0: float = 0.9):
    """Integrate only q with the projected solver's delay interpolation/update."""
    p = projected.FixPara(rho_c=0.08, q_max=1.0, tau_g=tau_g)
    n = int(round(T / dt))
    i0 = int(round((tau_g + 1.0) / dt))
    q = np.full(i0 + n + 1, q0, dtype=float)
    for k in range(1, n + 1):
        t = k * dt
        i = i0 + k
        q_now = q[i - 1]
        q_lag = projected._interp(q, t, tau_g, dt, i0)
        raw = p.g_c(q_lag)
        dq = projected.projected_quality_velocity(q_now, raw, p.q_max, 0.0)
        q[i] = max(0.0, min(p.q_max, q_now + dt * dq))
    return np.arange(n + 1, dtype=float) * dt, q[i0:i0 + n + 1]


def full_parameters(module, tau_g: float):
    return module.FixPara(
        rho_c=0.08, b_f0=0.85, b_c=0.05, b_Gc=0.80, alpha=0.03,
        eta_f=0.05, e=0.55, r=0.02, eta=0.05, tau_g=tau_g,
        tau_p=25.0, A_tot=2.5, deltab=1.0, t_wave=40.0,
        kappa_w=0.1, mu=0.06, tau_conv=1.0,
    )


def full_run(module, tau_g: float, dt: float, T: float = 400.0):
    p = full_parameters(module, tau_g)
    return module.simulate(
        p, T=T, dt=dt, A_f0=0.6, A_c0=1.5, q0=0.9,
        P0=1.2, D0=0.0, E_fixed=0.825,
    )


def main():
    # At the same finite grid, the copied v45 legacy post-Euler clip (used only
    # as a comparison implementation) and the explicit tangent-cone Euler
    # update should give identical states for admissible q. This is not the
    # historical C10 producer source and does not prove C10 output provenance.
    for tau_g in (5.0, 20.0, 40.0):
        a = full_run(legacy_clip, tau_g, 0.05, T=100.0)
        b = full_run(projected, tau_g, 0.05, T=100.0)
        for name in ("Af", "Ac", "q", "Pp", "Dd", "Ar", "B", "E", "T_b"):
            if not np.array_equal(a[name], b[name]):
                raise AssertionError(f"discrete update mismatch: tau_g={tau_g}, state={name}")
        print(f"same-grid copied-v45-clip/projected-Euler arrays: exact, tau_g={tau_g:g}, dt=0.05 yr")

    # For tau_g=20 and 40, the admissible constant history makes the exact
    # continuous trajectory q(t)=min(1, 0.9+0.0072 t), capped at 125/9 yr.
    for tau_g in (20.0, 40.0):
        t_ref = np.arange(0.0, 60.0 + 0.00025 / 2, 0.00025)
        exact = np.minimum(1.0, 0.9 + 0.0072 * t_ref)
        errors = []
        for dt in (0.1, 0.05, 0.025, 0.0125):
            t, q = scalar_quality(tau_g, dt)
            q_on_ref = np.interp(t_ref, t, q)
            err = float(np.max(np.abs(q_on_ref - exact)))
            errors.append(err)
            print(f"continuous projected q check: tau_g={tau_g:g}, dt={dt:g} yr, sup error={err:.9g}")
        if not (errors[-1] < errors[0]):
            raise AssertionError("projected q interpolation error did not decrease under refinement")

    # tau_g=5 is not in the saturation-degenerate regime. Compare the same
    # projected Euler method under refinement to a fine, linearly interpolated
    # reference, not to the C10 sensitivity table.
    dt_ref = 0.00025
    t_ref, q_ref = scalar_quality(5.0, dt_ref)
    errors = []
    for dt in (0.1, 0.05, 0.025, 0.0125):
        t, q = scalar_quality(5.0, dt)
        err = float(np.max(np.abs(np.interp(t_ref, t, q) - q_ref)))
        errors.append(err)
        print(f"tau_g=5 projected-q refinement: dt={dt:g} yr, sup error vs {dt_ref:g} yr={err:.9g}")
    if not (errors[-1] < errors[0]):
        raise AssertionError("tau_g=5 quality error did not decrease under refinement")

    # Full frozen-demand Figure 1 scenario; all coarse grids divide the fine
    # reference grid exactly. Compare trajectories on common time nodes.
    fine_dt = 0.003125
    ref = full_run(projected, 20.0, fine_dt)
    for dt in (0.1, 0.05, 0.025, 0.0125):
        coarse = full_run(projected, 20.0, dt)
        stride = int(round(dt / fine_dt))
        errors = {}
        for name in ("q", "Ac", "Af", "Pp", "Dd", "B"):
            aligned = ref[name][::stride]
            if len(aligned) != len(coarse[name]):
                raise AssertionError(f"grid alignment failed for {name}, dt={dt}")
            errors[name] = float(np.max(np.abs(coarse[name] - aligned)))
        print(
            "full Figure 1 scenario refinement: "
            f"dt={dt:g} yr; max abs errors vs {fine_dt:g} yr "
            f"q={errors['q']:.9g}, Ac={errors['Ac']:.9g} ha, "
            f"B={errors['B']:.9g} gha, P={errors['Pp']:.9g} cap, "
            f"D={errors['Dd']:.9g} gha yr"
        )

    # The baseline delayed paths for 20 and 40 years are exactly the same under
    # the continuous projected law: t_cap=125/9 yr < 20 yr, and both remain 1.
    _, q20 = scalar_quality(20.0, 0.05)
    _, q40 = scalar_quality(40.0, 0.05)
    if not np.array_equal(q20, q40):
        raise AssertionError("baseline tau_g=20/40 discrete q paths differ")
    print("baseline tau_g=20/40 q paths: exactly equal on dt=0.05 grid; saturation time=125/9 yr")


if __name__ == "__main__":
    main()
