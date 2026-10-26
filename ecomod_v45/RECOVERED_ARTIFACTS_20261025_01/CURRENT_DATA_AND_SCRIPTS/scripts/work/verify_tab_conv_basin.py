"""Independent numerical check for the ECOMOD v45 canonical solver.

Copied from agent 2 productivity illusion/model_sims at repository main SHA
1ba3d3c8a286a055b1342b5102731b601ec3d428. It checks the fast-land composition
contrast (gha ha^-1), deficit-side leading eigenvalue (yr^-1), and initial-
population floor thresholds (cap) against analytic expressions. It imports the
canonical delayed-quality solver; no parameter is recalibrated by this helper.
"""
import numpy as np
from scipy.optimize import brentq
from twoland_fixed import FixPara


def mk(b_f0):
    return FixPara(rho_c=0.08, b_f0=b_f0, b_c=0.05, b_Gc=0.80, alpha=0.03,
                   eta_f=0.05, e=0.55, r=0.02, eta=0.05, tau_g=20.0, tau_p=25.0,
                   A_tot=2.5, deltab=1.0, t_wave=40.0, kappa_w=0.1, mu=0.06, tau_conv=1.0)


def delta_b_conv(p, q, b_f):
    return b_f - (p.b_c + p.b_Gc * p.g_c(q))


def _J2(p, E):
    """2x2 active-conversion Jacobian at frozen demand E [gha] on the deficit side.
    Land states and A_r are in ha; model time is in yr; its eigenvalues are yr^-1.
    Linearises u_c=S/(b_f tau_conv) about the interior no-conversion balance point."""
    k = p.mu / (p.mu + p.eta_f)
    Ups = p.b_c + p.b_Gc * p.g_c(p.q_max)
    bf = p.b_f0
    tau, mu, et, sf, sc = p.tau_conv, p.mu, p.eta_f, p.sigma_f, p.sigma_c

    def B_eq(Ac):
        return p.b_f0 * k * (p.A_tot - Ac) + Ups * Ac

    gr = brentq(lambda Ac: B_eq(Ac) - E, 1e-3, p.A_tot - 1e-3)
    Af, Ac = k * (p.A_tot - gr), gr
    du_dAf = -sf / tau                 # d(u_c)/dA_f  (S = E - sf bf Af - sc Ups Ac)
    du_dAc = -sc * Ups / (bf * tau)    # d(u_c)/dA_c
    return np.array([[du_dAf - mu - et, du_dAc - mu],
                     [-du_dAf, -du_dAc]])


def lead_lambda(p, E):
    J = _J2(p, E)
    lam = np.linalg.eigvals(J)
    return np.real(lam[np.argmax(np.real(lam))])


def basin_threshold(A_c0, p=None):
    """Endogenous-demand run; largest P0 [cap] avoiding A_c floor contact [ha]."""
    if p is None:
        p = mk(0.85)
    from twoland_fixed import simulate

    def minAc(P0):
        r = simulate(p, T=800.0, dt=0.1, A_c0=A_c0, A_f0=0.6, q0=0.9, P0=P0)
        return np.min(r["Ac"])

    def crash(P0):
        return minAc(P0) <= p.Ac_min + 1e-6  # floor-contact tolerance, ha

    lo, hi = 1.0, 5.0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if crash(mid):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def main():
    bf_list = [0.60, 0.85, 1.20, 2.00]
    p = mk(0.85)
    q_star = p.q_max / 2.0
    b_ceff = p.b_c + p.b_Gc * p.g_c(q_star)
    print("=== tab:conv ===")
    print(f"  q*={q_star} (dimensionless); b_c_eff={b_ceff:.4f} gha/ha")
    print(f"{'b_f (gha/ha)':>14} {'Delta_b_conv (gha/ha)':>24} {'lambda_+ (yr^-1)':>20}")
    for bf in bf_list:
        pm = mk(bf)
        db = delta_b_conv(pm, q_star, bf)
        # use a mid-branch frozen demand at 70% of this b_f's E_ceil
        k = pm.mu / (pm.mu + pm.eta_f)
        ec = pm.b_f0 * k * pm.A_tot - pm.Ac_min * (pm.b_f0 * k - pm.b_c)
        lam = lead_lambda(pm, 0.7 * ec)
        print(f"{bf:6.2f} {db:+13.3f} {lam:+14.4f}")

    print("\n  No-CSD check (baseline b_f=0.85 gha/ha): leading eigenvalue vs E -> E_ceil (gha)")
    p = mk(0.85)
    k = p.mu / (p.mu + p.eta_f)
    ec = p.b_f0 * k * p.A_tot - p.Ac_min * (p.b_f0 * k - p.b_c)
    for frac in (0.50, 0.90, 0.99, 0.999):
        print(f"    E={frac*ec:.3f} gha ({frac:.3f} E_ceil)  lead Re(lambda)={lead_lambda(p, frac*ec):+.5f} yr^-1")

    print("\n=== tab:basin ===")
    for Ac0 in (0.40, 0.70, 1.00, 1.18):
        print(f"  A_c0={Ac0:.2f} ha  threshold P0 ~ {basin_threshold(Ac0):.3f} cap")


if __name__ == "__main__":
    main()
