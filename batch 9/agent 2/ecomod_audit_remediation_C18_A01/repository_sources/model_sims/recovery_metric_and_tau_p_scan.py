"""
recovery_metric_and_tau_p_scan.py -- SI S5.4 (recovery metric R_c(T)) and S5.5 (tau_p scan).

Companion to manuscript_ECOMOD_v33.tex (two-land, scope-A). Reproduces the two supplementary
experiments that close GPT items 8 and 9, on the BASE model.

MODEL-FIDELITY NOTE (this is the corrected version).
  The base model is run with the bounded technology step OFF (`simulate(..., T_b_on=False)`),
  the configuration used for every reported result, the composition demonstration and for the
  healthy/degraded reference states. The recovery integrator therefore uses T_b = 0.  An earlier
  version of this section applied the technology wave T_b unconditionally; that produced a
  WAVE-ARTEFACT -- surplus-gating drove A_c to ~2.39 (96% of A_tot), pushed A_r below its stated
  floor (0.049 < 0.10), collapsed B to ~0.17, and let R_c misread as a large "over-restoration"
  with the population "paying" (P_end/P_init ~ 0.26).  That is NOT a model result.  On the base
  model the capital book is bounded by A_tot and A_c^min, A_r never approaches its floor, B stays
  O(1), and the over-restoration is a modest move along the one-parameter equilibrium family
  (R_c ~ 1.07-1.27), i.e. a real but bounded effect, not a domain violation.

  S5.4  R_c(T) = (A_c(T) - A_c^deg) / (A_c^init - A_c^deg).
        A_c^init / P^init are the base-model healthy reference (representative member of the
        one-parameter family); A_c^deg is the degraded crash-equilibrium capital level.
        Tested from the NON-EQUILIBRIUM post-crash state (A_c at floor, land/population still
        interior), because BOTH gates are exactly zero AT the degraded equilibrium (R_B=1 there,
        so B=E and neither (B-E)_+ nor (E-B)_+ can fire) -- the key phase-dependence.
        Rows: none / surplus-gated (chi 0.02,0.05,0.10) / deficit-gated (0.05,0.10), plus the
        policy rows (target-cap restoration, conversion-freeze) and the full end state.

  S5.5  tau_p scan: (a) recover/collapse fraction is FLAT in tau_p (demand-set, not lag-set);
        (b) no sustained limit cycle / no Hopf up to tau_p=2000 yr (the single overshoot pulse
        keeps bounded amplitude ~0.57 and simply shifts later in time).
"""
import numpy as np
from twoland_fixed import FixPara, simulate


def _mk(chi_r=0.0, **kw):
    base = dict(rho_c=0.08, b_f0=0.85, b_c=0.05, b_Gc=0.80, alpha=0.03, eta_f=0.05,
                e=0.55, r=0.02, eta=0.05, tau_g=20.0, tau_p=25.0, A_tot=2.5, deltab=1.0,
                t_wave=40.0, kappa_w=0.1, mu=0.06, tau_conv=1.0, chi_r=chi_r)
    base.update(kw)
    return FixPara(**base)


def references(T=3000.0, dt=0.1):
    """Healthy reference (A_c^init,P^init) and the degraded crash equilibrium."""
    r = simulate(_mk(0.0), T=T, dt=dt, A_c0=0.9, A_f0=0.6, q0=0.9, P0=1.2)
    rd = simulate(_mk(0.0), T=T, dt=dt, A_c0=0.9, A_f0=0.6, q0=0.9, P0=2.5)
    return dict(A_init=r["Ac"][-1], P_init=r["Pp"][-1], B_init=r["B"][-1],
                A_deg=rd["Ac"][-1], P_deg=rd["Pp"][-1], B_deg=rd["B"][-1],
                deg=dict(A_f=rd["Af"][-1], A_r=rd["Ar"][-1], q=rd["q"][-1], P=rd["Pp"][-1]))


def integrate(chi, gate, target=None, freeze_u=False, start="nonequil", T=2000.0, dt=0.1):
    """Base-model (T_b=0) integrator with a chosen gate sign and optional policy constraint."""
    ref = references()
    p = _mk(chi_r=chi)
    if start == "degraded_equil":
        A_c0, A_f0, q0, P0 = ref["A_deg"], ref["deg"]["A_f"], ref["deg"]["q"], ref["deg"]["P"]
    else:
        A_c0, A_f0, q0, P0 = 0.058, 0.6, 0.9, 1.2
    i0 = int(round((p.tau_g + 1) / dt)); n = int(round(T / dt))
    Af = np.full(i0 + n + 1, A_f0); Ac = np.full(i0 + n + 1, A_c0)
    qq = np.full(i0 + n + 1, q0); Pp = np.full(i0 + n + 1, P0); Dd = np.zeros(i0 + n + 1)
    Bhist = np.zeros(i0 + n + 1); Bhist[:] = p.B(A_f0, A_c0, q0, 0.0)
    Ar = np.full(i0 + n + 1, p.A_tot - A_f0 - A_c0)
    minAr, maxAc, conserv, dpeak = np.inf, -np.inf, 0.0, 0.0
    for k in range(n + 1):
        t = k * dt; i = i0 + k
        if i == i0:
            continue
        Afm, Acm, qm, Dm, Pm = Af[i - 1], Ac[i - 1], qq[i - 1], Dd[i - 1], Pp[i - 1]
        Arm = p.A_tot - Afm - Acm
        Yf = p.Y_f(Afm, Dm); Yc = p.Y_c(Acm, qm); B = Yf + Yc; E = p.e * Pm
        S = max(E - p.sigma_f * Yf - p.sigma_c * Yc, 0.0)
        u = 0.0 if freeze_u else min(S / max(p.b_f(Dm), 1e-9), max(Acm - p.Ac_min, 0.0)) / max(p.tau_conv, 1e-9)
        Rrc = (p.chi_r * max(Arm, 0.0) * max(B - E, 0.0)) if gate == "surplus" else \
              (p.chi_r * max(Arm, 0.0) * max(E - B, 0.0)) if gate == "deficit" else 0.0
        if target is not None:
            Rrc = min(Rrc, max(Arm - p.Ac_min, 0.0) / dt, max(target - Acm, 0.0) / dt)
        elif gate != "none":
            Rrc = min(Rrc, max(Arm - p.Ac_min, 0.0) / dt)      # donor-limited
        dAf = u + p.mu * max(Arm, 0.0) - p.eta_f * Afm
        dAc = -u + Rrc; dq = p.g_c(qm)
        Kb = Bhist[max(0, min(len(Bhist) - 1, int((t - p.tau_p) / dt) + i0))] if p.tau_p > 0 else B
        K = max(Kb / p.e, p.K_min); dP = p.r * Pm * (1 - Pm / K) if K > 1e-9 else -p.r * Pm
        dD = max(E - B, 0.0) - p.eta * Dm
        Af[i] = max(0.0, Afm + dt * dAf); Ac[i] = max(p.Ac_min, min(p.A_tot, Acm + dt * dAc))
        qq[i] = max(0.0, min(p.q_max, qm + dt * dq)); Pp[i] = max(0.0, Pm + dt * dP)
        Dd[i] = max(0.0, Dm + dt * dD); Ar[i] = p.A_tot - Af[i] - Ac[i]
        conserv = max(conserv, abs(Af[i] + Ac[i] + Ar[i] - p.A_tot))
        minAr = min(minAr, Ar[i]); maxAc = max(maxAc, Ac[i]); dpeak = max(dpeak, Dd[i])
        Bhist[i] = p.B(Af[i], Ac[i], qq[i], Dd[i])
    sl = slice(i0, i0 + n + 1); Acs = Ac[sl]; Ps = Pp[sl]; Bs = Bhist[sl]
    def Rc(T):
        idx = min(len(Acs) - 1, int(T / dt)); return (Acs[idx] - ref["A_deg"]) / (ref["A_init"] - ref["A_deg"])
    return dict(Ac=Acs[-1], Af=Af[sl][-1], Ar=Ar[sl][-1], B=Bs[-1], E=0.55 * Ps[-1],
                RB=(0.55 * Ps[-1]) / Bs[-1], prev=Ps[-1] / ref["P_init"],
                pdeg=Ps[-1] / ref["P_deg"], minAr=minAr, maxAc=maxAc, dpeak=dpeak, conserv=conserv,
                Rc=Rc)


def s54(chi=0.05):
    ref = references()
    print(f"  A_c^init = {ref['A_init']:.4f}   P^init = {ref['P_init']:.4f}   "
          f"A_c^deg = {ref['A_deg']:.4f}   A_tot = 2.5   A_c^min = 0.05   A_r^min = 0.10\n")
    rows = [
        ("none (R_rc = 0)",                  "none",    0.0,  None, False, "nonequil"),
        ("surplus, chi=0.02",                "surplus", 0.02, None, False, "nonequil"),
        ("surplus, chi=0.05",                "surplus", 0.05, None, False, "nonequil"),
        ("surplus, chi=0.10",                "surplus", 0.10, None, False, "nonequil"),
        ("surplus, chi=0.10, target-cap",    "surplus", 0.10, ref["A_init"], False, "nonequil"),
        ("surplus, chi=0.10, conv-freeze",   "surplus", 0.10, None, True,  "nonequil"),
        ("deficit, chi=0.05",                "deficit", 0.05, None, False, "nonequil"),
        ("deficit, chi=0.10",                "deficit", 0.10, None, False, "nonequil"),
        ("deficit, chi=0.10, conv-freeze",   "deficit", 0.10, None, True,  "nonequil"),
        ("from degraded EQUILIBRIUM (any gate)", "surplus", 0.10, None, False, "degraded_equil"),
    ]
    hdr = "%-34s %6s %6s | %6s %6s %6s %6s %6s | %6s %6s | %5s"%(
        "restoration policy/gate", "R_c100", "R_c900", "A_c", "A_f", "A_r", "B", "P/P0",
        "minA_r", "maxA_c", "D_peak")
    print(hdr)
    for name, g, c, tg, fz, st in rows:
        r = integrate(c, g, tg, fz, start=st)
        note = ""
        if r["minAr"] < 0.10: note += "   !A_r<floor"
        if r["Rc"](900) > 1 + 1e-6: note += "   (over-restoration >1)"
        print("%-34s %6.2f %6.2f | %6.3f %6.3f %6.3f %6.3f %6.2f | %6.3f %6.3f | %5.3f%s"%(
            name, r["Rc"](100), r["Rc"](900), r["Ac"], r["Af"], r["Ar"], r["B"], r["prev"],
            r["minAr"], r["maxAc"], r["dpeak"], note))
    print(f"  (area conservation |max| = {r['conserv']:.1e}; 'from degraded EQUILIBRIUM' shows both gates inert)")


def _run(tau_p, T=1500.0, dt=0.1, A_c0=0.9, A_f0=0.6, P0=1.2, chi_r=0.0, T_g=20.0):
    p = _mk(chi_r=chi_r, tau_p=tau_p, tau_g=T_g)
    return simulate(p, T=T, dt=dt, A_c0=A_c0, A_f0=A_f0, q0=0.9, P0=P0)


def tau_scan():
    print("  (a) recover/collapse fraction vs tau_p (tau_g=20, chi_r=0; crash = min A_c <= A_c^min):")
    def crash(tau_p, P0, Ac0):
        r = _run(tau_p, T=1500.0, dt=0.1, A_c0=Ac0, A_f0=0.6, P0=P0)
        return bool(r["Ac"].min() <= 0.05 + 1e-6)
    for tau_p in [25, 100, 200, 300, 500]:
        tot = fr = 0
        for Ac0 in [0.40, 0.70, 1.00, 1.18]:
            for P0 in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
                tot += 1; fr += 0 if crash(tau_p, P0, Ac0) else 1
        print(f"    tau_p={tau_p:4d}  recover fraction = {fr / tot:.3f} ({fr}/{tot})")
    print("  (b) no sustained limit cycle / no Hopf up to tau_p=2000 (single overshoot pulse, bounded, shifts later):")
    for tau_p in [25, 300, 500, 1000, 1500, 2000]:
        r = _run(tau_p, T=3000.0, dt=0.1)
        P = r["Pp"]; n = len(P)
        amps = [np.ptp(P[a:b]) for a, b in [(0, n // 4), (n // 4, n // 2),
                                            (n // 2, 3 * n // 4), (3 * n // 4, n)]]
        print(f"    tau_p={tau_p:5d}  P-amplitude by quarter: {'  '.join('%.4f' % a for a in amps)}")


if __name__ == "__main__":
    print("=== S5.4 Recovery metric R_c(T): base-model gate-sign asymmetry ===")
    s54()
    print("\n=== S5.5 tau_p-extended delay scan ===")
    tau_scan()
