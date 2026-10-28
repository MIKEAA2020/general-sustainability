"""Reproduce the C11 fixed-point values and matched floor-state integration.

All demand values are constructed from the same unrounded ceiling, rather than
mixing the rounded manuscript display with an increment from another precision.
Units: E and B are gha; D is gha yr; time is yr.
"""
from __future__ import annotations

import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "work"))
from twoland_fixed_projected import FixPara, simulate

p = FixPara(A_tot=2.5, b_f0=0.85, b_c=0.05, b_Gc=0.80, rho_c=0.08,
            alpha=0.03, eta=0.05, eta_f=0.05, mu=0.06, e=0.55,
            r=0.02, q_max=1.0, Ac_min=0.05, K_min=0.02,
            tau_g=20.0, tau_p=25.0, tau_conv=1.0, chi_r=0.0)
k = p.mu / (p.mu + p.eta_f)
Ac0 = p.Ac_min
Af0 = k * (p.A_tot - Ac0)
Ar0 = p.A_tot - Ac0 - Af0
Eceil = p.b_f0 * Af0 + p.b_c * Ac0


def fixed_point(E: float) -> float:
    """Bisect eta*D + B(Ac_min, D, q_max) - E = 0."""
    lo, hi = 0.0, max(10.0, 2.0 * E / p.eta)

    def f(D: float) -> float:
        B = p.b_f0 * math.exp(-p.alpha * D) * Af0 + p.b_c * Ac0
        return p.eta * D + B - E

    if f(lo) > 0 or f(hi) < 0:
        raise AssertionError("failed to bracket debt fixed point")
    for _ in range(120):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


print(f"k={k:.12f}; Eceil={Eceil:.12f} gha; floor state Ac={Ac0:.3f}, Af={Af0:.12f}, Ar={Ar0:.12f} ha")
for offset in (0.02, 0.10):
    E = Eceil + offset
    Dstar = fixed_point(E)
    Bstar = p.b_f0 * math.exp(-p.alpha * Dstar) * Af0 + p.b_c * Ac0
    Sstar = E - Bstar
    trajectory = simulate(p, T=1200.0, dt=0.1, A_c0=Ac0, A_f0=Af0,
                          q0=p.q_max, P0=1.0, D0=0.0, E_fixed=E)
    Dend = float(trajectory["Dd"][-1])
    Bend = float(trajectory["B"][-1])
    if abs(Dend - Dstar) > 1e-7 or abs(trajectory["Ac"][-1] - Ac0) > 1e-12:
        raise AssertionError(f"integration mismatch at E={E:.12f}")
    print(f"E={E:.12f} (Eceil+{offset:.2f}); D*={Dstar:.9f}; B*={Bstar:.9f}; S*={Sstar:.9f}; "
          f"Euler(T=1200,dt=0.1): D={Dend:.9f}, B={Bend:.9f}")
