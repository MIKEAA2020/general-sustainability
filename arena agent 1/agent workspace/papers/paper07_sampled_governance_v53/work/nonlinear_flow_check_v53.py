#!/usr/bin/env python3
"""Finite-difference audit of the nonlinear plant + frozen-assessment controller flow.

The ecological states are integrated under held effort over each review interval.
At the review, the nonlinear effort-rate law is integrated with the endpoint
assessment frozen for one review-length. The comparison matrix is the exact
linearization of that flow composed after the held-plant flow.
"""
from __future__ import annotations
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigvals, expm
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "work"))
from p07_core import build, exact_review  # noqa: E402

P = build()
par = P["parameters"]
r, K, q = (par[k] for k in ("r", "K", "q"))
tm, Emax = par["tm"], par["Emax"]
eta, d0, Dref, Zref = (par[k] for k in ("eta", "d0", "dref", "Zref"))
delta = P["delta"]
XSTAR = np.array([P["N_star"], P["Z_star"], P["E_star"]], dtype=float)
CE, CZ = P["mobilising"]


def phi(x: float) -> float:
    # Equivalent to the shifted/floored softplus in the paper because
    # delta = log(2)/10 and k = 10.
    return max(0.0, math.log1p(math.exp(10.0 * x)) / 10.0)


def effort_rate(E: float, Zhat: float) -> float:
    return (1.0 - E / Emax) * (
        eta * E * (Zhat / Dref - E / Emax)
        + d0 * Zhat / (Zref + Zhat)
    )


def nonlinear_map(X: np.ndarray, T: float) -> np.ndarray:
    N0, Z0, E0 = map(float, X)

    def plant_rhs(_t, y):
        N, Z = y
        surplus = r * N * (1.0 - N / K)
        deficit = q * E0 * N - surplus
        return [surplus - q * E0 * N, (phi(deficit) - Z) / tm]

    plant = solve_ivp(plant_rhs, (0.0, T), [N0, Z0], method="DOP853",
                      rtol=2e-12, atol=2e-14)
    if not plant.success:
        raise RuntimeError(plant.message)
    Nf, Zf = map(float, plant.y[:, -1])

    # Exact nonlinear controller flow over one review-length with the
    # contemporaneous endpoint assessment frozen.
    ctl = solve_ivp(lambda _s, y: [effort_rate(float(y[0]), Zf)],
                    (0.0, T), [E0], method="DOP853", rtol=2e-12, atol=2e-14)
    if not ctl.success:
        raise RuntimeError(ctl.message)
    Ef = min(Emax, max(0.0, float(ctl.y[0, -1])))
    return np.array([Nf, Zf, Ef], dtype=float)


def reference_matrix(T: float) -> np.ndarray:
    R = exact_review(T, CE, CZ)
    return R @ expm(P["A_hold"] * T)


def fd_jacobian(T: float, h: float) -> np.ndarray:
    J = np.zeros((3, 3), dtype=float)
    scales = np.maximum(1.0, np.abs(XSTAR))
    for j in range(3):
        step = h * scales[j]
        d = np.zeros(3)
        d[j] = step
        J[:, j] = (nonlinear_map(XSTAR + d, T) - nonlinear_map(XSTAR - d, T)) / (2.0 * step)
    return J


def radius_from_fd(T: float, h: float) -> float:
    return float(np.max(np.abs(eigvals(fd_jacobian(T, h)))))


def main() -> None:
    tests = []
    for T in (1.0, 6.501294948075468):
        M = reference_matrix(T)
        rec = {"T_years": T, "reference_radius": float(np.max(np.abs(eigvals(M)))),
               "fixed_point_residual_inf": float(np.max(np.abs(nonlinear_map(XSTAR, T) - XSTAR))),
               "finite_difference": []}
        for h in (1e-4, 3e-5, 1e-5, 3e-6, 1e-6, 3e-7):
            J = fd_jacobian(T, h)
            rec["finite_difference"].append({
                "relative_step": h,
                "max_abs_jacobian_error": float(np.max(np.abs(J - M))),
                "spectral_radius": float(np.max(np.abs(eigvals(J)))),
            })
        tests.append(rec)

    crossings = []
    for h in (1e-4, 3e-5, 1e-5, 3e-6, 1e-6):
        root = brentq(lambda T: radius_from_fd(T, h) - 1.0,
                      6.3, 6.7, xtol=2e-8, rtol=1e-12, maxiter=100)
        crossings.append({"relative_step": h, "T_years": float(root),
                          "rho_below": radius_from_fd(root - 0.02, h),
                          "rho_above": radius_from_fd(root + 0.02, h)})

    result = {
        "edition": "paper07_v53_nonlinear_flow_check",
        "method": "DOP853 ecological flow under held effort, then exact nonlinear effort-rate flow with endpoint assessment frozen for Tr; central finite-difference Jacobian",
        "equilibrium": {"N_star": float(XSTAR[0]), "Z_star": float(XSTAR[1]), "E_star": float(XSTAR[2])},
        "linear_monodromy_crossing_years": 6.501294948075468,
        "jacobian_checks": tests,
        "finite_difference_crossings": crossings,
        "limitations": ["local finite differences only", "no invariant-circle continuation", "assessment noise and projection inactive in the local check"]
    }
    out = ROOT / "work" / "nonlinear_flow_check_v53.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"jacobian_checks": tests, "finite_difference_crossings": crossings}, indent=2))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
