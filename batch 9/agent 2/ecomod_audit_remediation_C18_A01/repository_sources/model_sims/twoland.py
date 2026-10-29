"""Two-land (scope-A) model — verification of the corrected static geometry.

Implements the scope-A governing set (Part A of V33_scopeA_revision_plan.md):

    G_c(A_c)   = rho_c A_c (1 - A_c/A_c,max)
    b_f        = (b_f0 + T_b(t)) e^{-alpha D}
    Y_f        = b_f A_f
    Y_c        = b_c A_c + b_G,c G_c(A_c)
    B          = Y_f + Y_c
    E          = e P
    S          = [E - sigma_f Y_f - sigma_c Y_c]_+
    dA_c/dt    = G_c(A_c(t-tau_g)) - S/kappa - L_c
    dA_f/dt    = S/kappa - eta_f A_f
    dP/dt      = r P [1 - P / K(t-tau_p)],   K = B/e
    dD/dt      = [E - B]_+ - eta D

Two-land G_c is a *growth flow* into capital-land accounting capacity (not an
`A_r -> A_c` area transition unless stated).  `A_r` carries the residual balance
`dA_r/dt = -G_c(A_c) + L_c + eta_f A_f` so `A_f + A_c + A_r = A_tot` dynamically.

This file only builds STATIC geometry + equilibrium/local information.  It is the
contract the manuscript will rest on.  Dynamic integration is added separately.
"""
import numpy as np


def ramp(x):
    return max(x, 0.0)


class TwoLand:
    """Container for the two-land static/dynamic functions at fixed state."""

    def __init__(self, *, A_cmax=1.2, rho_c=0.03, b_f0=0.5, b_c=0.15, b_Gc=0.8,
                 eta_f=0.05, e=0.55, r=0.02, alpha=0.03, eta=0.05, kappa=None,
                 sigma_f=1.0, sigma_c=1.0, D=0.0, T_b=0.0):
        self.A_cmax = A_cmax
        self.rho_c = rho_c
        self.b_f0 = b_f0
        self.b_c = b_c
        self.b_Gc = b_Gc
        self.eta_f = eta_f
        self.e = e
        self.r = r
        self.alpha = alpha
        self.eta = eta
        self.sigma_f = sigma_f
        self.sigma_c = sigma_c
        self.D = D
        self.T_b = T_b
        # conversion coefficient (unit-fix): kappa = b_f, so S/kappa is in ha/yr
        self.kappa = kappa if kappa is not None else self.b_f(D)
        self.V = None            # filled by diagnostic (placeholder for A-identification)
        self.Veco = 1.0 / rho_c  # ecological turnover timescale of capital land

    # ---- per-state definitions -------------------------------------------
    def b_f(self, D):
        return (self.b_f0 + self.T_b) * np.exp(-self.alpha * D)

    def G_c(self, A_c):
        return self.rho_c * A_c * (1.0 - A_c / self.A_cmax)

    def G_c_prime(self, A_c):
        return self.rho_c * (1.0 - 2.0 * A_c / self.A_cmax)

    def Y_f(self, A_f):
        return self.b_f(self.D) * A_f

    def Y_c(self, A_c):
        return self.b_c * A_c + self.b_Gc * self.G_c(A_c)

    def B(self, A_f, A_c):
        return self.Y_f(A_f) + self.Y_c(A_c)

    def b_c_eff(self, A_c):
        return self.b_c + self.b_Gc * self.G_c_prime(A_c)

    def delta_b_conv(self, A_c, D=None):
        """GPT §9/§11 diagnostic: direct capacity effect of conversion."""
        b_f = self.b_f(self.D if D is None else D)
        return b_f - self.b_c - self.b_Gc * self.G_c_prime(A_c)

    def psi_c(self, A_c):
        """capital-land flow share psi_c(A_c) = b_c A_c / Y_c(A_c)."""
        Y = self.Y_c(A_c)
        return self.b_c * A_c / Y if Y != 0 else np.nan

    # ---- static geometry (the corrected results) -------------------------
    @property
    def has_interior_capacity_max(self):
        # Y_c'(A_c)=0 has a root in (0,A_cmax) iff b_Gc*rho_c > b_c  (ratio boundary)
        return self.b_Gc * self.rho_c > self.b_c

    def A_c_star(self):
        if not self.has_interior_capacity_max:
            return None
        return 0.5 * self.A_cmax * (1.0 + self.b_c / (self.b_Gc * self.rho_c))

    def psi_c_star(self):
        a = self.A_c_star()
        if a is None:
            return None
        return self.psi_c(a)

    # ---- no-conversion-face equilibria (GPT verification (a)) ------------
    def no_conversion_equilibria(self):
        """With S=0, L_c=0, eta_f>0 the only equilibria are boundary.  Verify
        G_c(A_c*)=0 at A_c=0 and A_c=A_cmax, and A_f*=0 at the fixed point."""
        roots = [a for a in (0.0, self.A_cmax)
                 if abs(self.G_c(a)) < 1e-12]
        A_fstar = 0.0 if self.eta_f > 0 else np.nan  # eta_f A_f = 0 with eta_f>0 -> A_f=0
        return dict(G_c_roots=roots, A_f_star=A_fstar)


def report(m, label=""):
    print(f"\n===== {label} =====")
    print(f"rho_c={m.rho_c}  V_eco=1/rho_c={m.Veco:.1f} yr  A_cmax={m.A_cmax}")
    print(f"b_f0={m.b_f0}  b_c={m.b_c}  b_Gc={m.b_Gc}  kappa=b_f={m.kappa:.3g}")
    print(f"ratio b_Gc*rho_c / b_c = {m.b_Gc*m.rho_c/ m.b_c:.3f} "
          f"(interior capacity max iff > 1: {m.has_interior_capacity_max})")
    a = m.A_c_star()
    if a is not None:
        print(f"A_c* = {a:.4f}  (formula (A_cmax/2)(1 + b_c/(b_Gc rho_c)) "
              f"= {0.5*m.A_cmax*(1+m.b_c/(m.b_Gc*m.rho_c)):.4f})")
        print(f"psi_c* = {m.psi_c_star():.4f}  = 2b_c/(b_c+b_Gc rho_c) "
              f"= {2*m.b_c/(m.b_c+m.b_Gc*m.rho_c):.4f}")
    else:
        print("A_c* = None  (no interior capacity maximum)")
    # psi_c*=1 and =1/2 thresholds
    print(f"psi_c*=1 iff b_Gc*rho_c=b_c (=> here 1 iff {m.b_Gc*m.rho_c:.4f}=={m.b_c})")
    print(f"psi_c*=1/2 iff b_Gc*rho_c=3 b_c (=> here {3*m.b_c:.4f})")
    print("no-conversion face equilibria:", m.no_conversion_equilibria())


def conversion_diagnostic_sweep(m, A_lo=0.6, A_hi=1.0, n=5):
    """GPT §9: does conversion raise current accounting capacity over A_c?"""
    print(f"\n--- Delta b_conv = b_f - b_c - b_Gc G_c'(A_c) ---")
    for A in np.linspace(A_lo, A_hi, n):
        print(f"  A_c={A:.3f}  G_c'(A)={m.G_c_prime(A):+.4f}  "
              f"b_c_eff={m.b_c_eff(A):+.4f}  Delta b_conv={m.delta_b_conv(A):+.4f}")


if __name__ == "__main__":
    # Two candidate regimes for the capital-land productivity/regeneration:
    #  (1) FOREST-scale slow capital land: rho_c ~ 1/30..1/50 yr^-1
    #  (2) FAST harvesting-basket baseline (the honest V=1.6 yr signature lives
    #      on the *_fast_flow_* arrow, not here): rho_c larger.
    forest = TwoLand(rho_c=1/30.0, b_f0=0.5, b_c=0.15, b_Gc=0.8,
                     alpha=0.03, eta_f=0.05)
    report(forest, "FOREST-scale capital land  (rho_c=1/30 yr^-1)")
    conversion_diagnostic_sweep(forest)

    # A faster capital land (still distinguishable from crop flow land):
    fast = TwoLand(rho_c=0.08, b_f0=0.5, b_c=0.15, b_Gc=0.8, alpha=0.03, eta_f=0.05)
    report(fast, "FASTER capital/regeneration land  (rho_c=0.08 yr^-1)")
    conversion_diagnostic_sweep(fast)
