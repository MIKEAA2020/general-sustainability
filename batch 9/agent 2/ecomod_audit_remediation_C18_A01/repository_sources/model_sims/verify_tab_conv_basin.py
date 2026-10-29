"""
verify_tab_conv_basin.py  -- re-verify tab:conv and tab:basin on the corrected operator.

Reproduces the two spectral/empirical tables of manuscript_ECOMOD_v33.tex:

  tab:conv  : Delta_b_conv = b_f - b_c_eff at q*=q_max/2, and the leading eigenvalue
              lambda_+ of the corrected-operator frozen-demand active-conversion subsystem,
              at each fast-land yield b_f.
  tab:basin : capital-crash demand threshold P0 by initial capital stock A_c0
              (crash = A_c reaches its typed floor A_c^min=0.05).

Key corrected-operator results re-derived here:
  * b_c_eff(0.5) = b_c + b_Gc*g_c(0.5) = 0.0660.   Delta_b_conv = +0.534/+0.784/+1.134/+1.934.
  * Leading eigenvalue is NEGATIVE and CONSTANT ALONG THE BRANCH (no CSD: it does not vanish
    as E -> E_ceil), but it is NOT a single universal number: it varies monotonically with b_f
    (-0.0522 at b_f=0.60, -0.0537 at baseline 0.85, -0.0547 at 1.20, -0.0556 at 2.00).
  * tab:basin thresholds (monotone increasing in A_c0): ~2.39/2.68/2.96/3.12.
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
    """2x2 active-conversion subsystem Jacobian at frozen demand E, on the deficit side,
    about the unique interior equilibrium A_c* (no-conversion face). First order in the
    conversion closure u_c = S/(b_f tau_conv) and area book A_r = A_tot - A_f - A_c."""
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
    """Endogenous-demand run; largest P0 that does NOT crash A_c to its floor."""
    if p is None:
        p = mk(0.85)
    from twoland_fixed import simulate

    def minAc(P0):
        r = simulate(p, T=800.0, dt=0.1, A_c0=A_c0, A_f0=0.6, q0=0.9, P0=P0)
        return np.min(r["Ac"])

    def crash(P0):
        return minAc(P0) <= p.Ac_min + 1e-6

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
    print(f"  q*={q_star}  b_c_eff = b_c + b_Gc*g_c(q*) = {b_ceff:.4f}")
    print(f"{'b_f':>6} {'Delta_b_conv':>13} {'lambda_+ (lead)':>15}")
    for bf in bf_list:
        pm = mk(bf)
        db = delta_b_conv(pm, q_star, bf)
        # use a mid-branch frozen demand at 70% of this b_f's E_ceil
        k = pm.mu / (pm.mu + pm.eta_f)
        ec = pm.b_f0 * k * pm.A_tot - pm.Ac_min * (pm.b_f0 * k - pm.b_c)
        lam = lead_lambda(pm, 0.7 * ec)
        print(f"{bf:6.2f} {db:+13.3f} {lam:+14.4f}")

    print("\n  No-CSD check (baseline b_f=0.85): leading eigenvalue vs E -> E_ceil")
    p = mk(0.85)
    k = p.mu / (p.mu + p.eta_f)
    ec = p.b_f0 * k * p.A_tot - p.Ac_min * (p.b_f0 * k - p.b_c)
    for frac in (0.50, 0.90, 0.99, 0.999):
        print(f"    E={frac*ec:.3f} ({frac:.3f} E_ceil)  lead Re(lambda)={lead_lambda(p, frac*ec):+.5f}")

    print("\n=== tab:basin ===")
    for Ac0 in (0.40, 0.70, 1.00, 1.18):
        print(f"  A_c0={Ac0:.2f}  threshold P0 ~ {basin_threshold(Ac0):.3f}")


if __name__ == "__main__":
    main()
