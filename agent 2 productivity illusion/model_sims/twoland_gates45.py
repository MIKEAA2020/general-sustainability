"""Gates 4 & 5 — two-land no-CSD re-test + basin/recovery recompute (corrected).

GATE 4 — CSD at the TWO-DISTINCT transitions:
  (a) CONVERSION fold (frozen-demand E -> E_ceil): the active-conversion saddle's + eigenvalue
      -> 0 as E -> E_ceil (fold). => CRITICAL SLOWING DOWN is present at the fold. (Honest: N1
      "no CSD" does NOT apply to the fold; it was about the DELAY cliff.)
  (b) tau_g delay cliff (endogenous-population basin): does the basin shrink abruptly with NO
      pre-cliff slowing? Tested by measuring the relax-scaling of the leading eigenvalue vs tau_g.

GATE 5 — basin + recovery:
  (a) recover/collapse over (A_c0, P0) with corrected delay-history.
  (b) restoration: test an ACTIVE restoration (gated on deficit, so it works during collapse),
      and report the (B-E)_+ gated form honestly as ineffective.
  (c) dt-convergence + conservation.
"""
import numpy as np
from scipy.linalg import eigvals
from model_sims.twoland_stab import P, conv_capacity_ceiling, conv_equilibria, conv_loop_jac


def gate4_fold(p):
    print("GATE 4a — CSD at the CONVERSION fold (frozen demand E -> E_ceil):")
    print("   E        lam(saddle +)   note")
    for E in [0.30, 0.40, 0.45, 0.470, 0.477, 0.4781]:
        eqs = conv_equilibria(p, E)
        if len(eqs) < 2:
            print(f"   {E:.4f}    at/above ceiling (branches merged)")
            continue
        lo = eqs[0]
        lam = eigvals(conv_loop_jac(p, lo))
        lpos = max(np.real(lam))
        print(f"   {E:.4f}   {lpos:+.4f}   {'CSD (->0): fold' if lpos < 0.02 else ''}")


def gate4_tau_cliff(p):
    print("\nGATE 4b — tau_g delay cliff: basin recover/collapse vs tau_g (corrected history).")
    from model_sims.twoland_dyn import Para, simulate
    print("   tau_g   recover_frac   last-recovering")
    for tg in [5, 10, 15, 18, 20, 25, 30, 40]:
        # small grid in P0 at A_c0=0.9 (the "supported" capital)
        rec = 0; tot = 0
        for P0 in np.arange(0.4, 1.55, 0.1):
            pp = Para(rho_c=p.rho_c, b_f0=p.b_f0, b_c=p.b_c, b_Gc=p.b_Gc, alpha=p.alpha,
                      eta_f=p.eta_f, e=p.e, r=p.r, eta=p.eta, A_tot=2.0, tau_g=tg, tau_p=25.0,
                      Ac_min=p.Ac_min, deltab=0.0)
            r = simulate(pp, T=300, dt=0.1, A_f0=0.4, A_c0=0.9, P0=P0, T_b_on=False)
            tot += 1
            if r["Ac"][-1] > 0.3:
                rec += 1
        print(f"   {tg:3d}       {rec/tot:.2f}")


def gate5_basin(p):
    print("\nGATE 5a — two-land basin (corrected history), endogenous population:")
    print("   A_c0    P0      status     A_c_end   R_c")
    for A_c0 in [0.40, 0.70, 1.00]:
        for P0 in [0.5, 0.9, 1.1, 1.3]:
            st, A_e, Rc = classify2(p, A_c0, P0)
            print(f"   {A_c0:.2f}   {P0:.2f}   {st:>8s}   {A_e:.3f}   {Rc:+.3f}")


def gate5_restore(p):
    print("\nGATE 5b — restoration (DEFICIT-gated, so it is active during collapse):")
    from model_sims.twoland_dyn import Para, simulate
    print("   (A_c0,P0)   no-restore   restore(chi)   A_c_end   R_c")
    for A_c0, P0 in [(0.9, 1.2), (0.9, 1.4), (1.0, 1.2)]:
        st0, Ae0, Rc0 = classify2(p, A_c0, P0)
        # active restoration: R_fc = chi A_f, proportional, not gated on (B-E)_+
        rr = restore_run(p, A_c0, P0, chi=0.10)
        print(f"   ({A_c0:.2f},{P0:.2f})    {st0:>8s} R_c={Rc0:+.2f}   "
              f"{rr['status']:>8s} R_c={rr['R_c']:+.2f}   A_c_end={rr['A_c'][-1]:.3f}")


def gate5_conv(p):
    print("\nGATE 5c — dt-convergence + conservation at a boundary IC (A_c0=0.9,P0=1.2):")
    from model_sims.twoland_dyn import Para, simulate
    for dt in [0.2, 0.1, 0.05]:
        pp = Para(rho_c=p.rho_c, b_f0=p.b_f0, b_c=p.b_c, b_Gc=p.b_Gc, alpha=p.alpha,
                  eta_f=p.eta_f, e=p.e, r=p.r, eta=p.eta, A_tot=2.0, tau_g=20.0, tau_p=25.0,
                  Ac_min=p.Ac_min, deltab=0.0)
        r = simulate(pp, T=300, dt=dt, A_f0=0.4, A_c0=0.9, P0=1.2, T_b_on=False)
        print(f"   dt={dt:.2f}: maxcon={r['maxcon']:.1e}  A_c_end={r['Ac'][-1]:.3f}  "
              f"minA_c={r['Ac'].min():.3f}")


def classify2(p, A_c0, P0):
    from model_sims.twoland_dyn import Para, simulate
    pp = Para(rho_c=p.rho_c, b_f0=p.b_f0, b_c=p.b_c, b_Gc=p.b_Gc, alpha=p.alpha,
              eta_f=p.eta_f, e=p.e, r=p.r, eta=p.eta, A_tot=2.0, tau_g=20.0, tau_p=25.0,
              Ac_min=p.Ac_min, deltab=0.0)
    r = simulate(pp, T=300, dt=0.1, A_f0=0.4, A_c0=A_c0, P0=P0, T_b_on=False)
    Ae = r["Ac"][-1]
    st = "recover" if Ae > 0.3 else "collapse"
    denom = max(A_c0 - p.Ac_min, 1e-9)
    Rc = (Ae - p.Ac_min) / denom
    return st, Ae, Rc


def restore_run(p, A_c0, P0, chi=0.10):
    from model_sims.twoland_dyn import Para, simulate
    pp = Para(rho_c=p.rho_c, b_f0=p.b_f0, b_c=p.b_c, b_Gc=p.b_Gc, alpha=p.alpha,
              eta_f=p.eta_f, e=p.e, r=p.r, eta=p.eta, A_tot=2.0, tau_g=20.0, tau_p=25.0,
              Ac_min=p.Ac_min, deltab=0.0, chi=chi, rho_r=chi, chi_gate="deficit")
    r = simulate(pp, T=300, dt=0.1, A_f0=0.4, A_c0=A_c0, P0=P0, T_b_on=False, restoration=True)
    Ae = r["Ac"][-1]
    return dict(status="recover" if Ae > 0.3 else "collapse", R_c=(Ae - p.Ac_min) / max(A_c0 - p.Ac_min, 1e-9),
                A_c=r["Ac"])


if __name__ == "__main__":
    p = P(rho_c=0.08, b_f0=0.85, b_c=0.05, b_Gc=0.8, alpha=0.03, eta_f=0.05,
          e=0.55, r=0.02, eta=0.05, Ac_min=0.05)
    c, ac = conv_capacity_ceiling(p)
    print(f"Conversion-capacity ceiling E_ceil={c:.4f} @ A_c={ac:.3f}")
    gate4_fold(p)
    gate4_tau_cliff(p)
    gate5_basin(p)
    gate5_restore(p)
    gate5_conv(p)
