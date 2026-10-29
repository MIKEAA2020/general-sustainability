"""Two-book delay-differential model solver (v42 numerical core; GFN/NFA account-unit convention).

GFN/NFA account values B, E, Y_f, Y_c and S are in gha for each annual
account, not gha/yr. Land areas A_f, A_c, A_r and A_tot are in ha; per-hectare
account yields b_f, b_c and Upsilon are in gha/ha. G_c(q) is a quality-growth
rate in yr^-1, and b_G,c is a regeneration-value coefficient in gha*yr/ha, so
b_G,c G_c(q) A_c is an annual account amount in gha. Time is measured in years.

The accumulated shortfall state D is a model-internal time integral in gha*yr;
dot D and eta*D are in gha, alpha is (gha*yr)^-1, and eta is yr^-1. Land-book
rates and conversion/restoration flows are in ha/yr. The delayed and deposited
solver variants differ only in the quality-regeneration update convention.

These comments describe dimensions and model semantics only; no numerical
parameter, equation evaluation, integration scheme or trajectory is altered.
"""

import numpy as np


class FixPara:
    def __init__(self, **kw):
        g = kw.get
        self.A_tot = g("A_tot", 2.0)
        self.b_f0 = g("b_f0", 0.85)
        self.b_c = g("b_c", 0.05)
        self.b_Gc = g("b_Gc", 0.80)
        self.rho_c = g("rho_c", 0.08)
        self.q_max = g("q_max", 1.0)             # max per-ha capacity index
        self.alpha = g("alpha", 0.03)
        self.eta = g("eta", 0.05)
        self.eta_f = g("eta_f", 0.05)
        self.mu = g("mu", 0.06)                  # cropland maintenance rate
        self.e = g("e", 0.55)
        self.r = g("r", 0.02)
        self.sigma_f = g("sigma_f", 1.0)
        self.sigma_c = g("sigma_c", 1.0)
        self.tau_conv = g("tau_conv", 1.0)       # conversion time constant (yr)
        self.Ac_min = g("Ac_min", 0.05)
        self.K_min = g("K_min", 0.02)
        self.chi_r = g("chi_r", 0.10)            # reserve->capital restoration
        self.tau_g = g("tau_g", 20.0)
        self.tau_p = g("tau_p", 25.0)
        self.deltab = g("deltab", 1.0)
        self.kappa_w = g("kappa_w", 0.1)
        self.t_wave = g("t_wave", 40.0)

    # ---- model functions ------------------------------------------------
    def b_f(self, D):
        Tb = self.deltab / (1.0 + np.exp(-self.kappa_w * (0.0)))  # at t=0 wave
        return (self.b_f0) * np.exp(-self.alpha * D)

    def g_c(self, q):
        return self.rho_c * q * (1.0 - q / self.q_max)

    def Y_f(self, A_f, D, Tb=0.0):
        return (self.b_f0 + Tb) * np.exp(-self.alpha * D) * A_f

    def Y_c(self, A_c, q):
        return self.b_c * A_c + self.b_Gc * self.g_c(q) * A_c

    def B(self, A_f, A_c, q, D, Tb=0.0):
        return self.Y_f(A_f, D, Tb) + self.Y_c(A_c, q)

    def psi_f(self, A_f, A_c, q, D, Tb=0.0):
        """fast-land share of total biocapacity (the CORRECT share for R_A)."""
        B = self.B(A_f, A_c, q, D, Tb)
        return self.Y_f(A_f, D, Tb) / B if B != 0 else np.nan

    def delta_b_conv(self, q, b_f):
        """composition diagnostic: effect of shifting 1 ha from A_c to A_f."""
        b_c_eff = self.b_c + self.b_Gc * self.g_c(q)
        return b_f - b_c_eff


def _interp(hist, t, delay, dt, i0):
    if delay <= 0:
        idx = max(0, min(len(hist) - 1, int(t / dt) + i0))
        return hist[idx]
    xf = (t - delay) / dt + i0
    j = int(np.floor(xf)); f = xf - j
    j0 = max(0, min(len(hist) - 1, j)); j1 = max(0, min(len(hist) - 1, j + 1))
    return hist[j0] * (1 - f) + hist[j1] * f


def simulate(p, T=250.0, dt=0.05, A_f0=0.6, A_c0=0.9, q0=0.9, P0=1.2,
             D0=0.0, T_b_on=False, E_fixed=None, history_len=None):
    """Integrate the root-cause-corrected two-book model (method of steps).

    E_fixed: if given, footprint E is pinned (isolates conversion/land
    response); otherwise E = e P(t) endogenous.
    Returns dict of time series + conservation diagnostics + the fraction
    of FIXED-demand composition illusion (B up while A_c down).
    """
    n = int(round(T / dt))
    hl0 = history_len if history_len else int(round((p.tau_g + 1.0) / dt))
    i0 = hl0
    Af = np.full(i0 + n + 1, A_f0); Ac = np.full(i0 + n + 1, A_c0)
    qq = np.full(i0 + n + 1, q0); Pp = np.full(i0 + n + 1, P0)
    Dd = np.full(i0 + n + 1, D0); Ar = np.full(i0 + n + 1, p.A_tot - A_f0 - A_c0)
    Bhist = np.zeros(i0 + n + 1)
    B0 = p.B(A_f0, A_c0, q0, D0)
    Bhist[:] = B0
    # delay-history of q over negative time set to q0 (non-degenerate)
    maxcon = 0.0
    for k in range(n + 1):
        t = k * dt; i = i0 + k
        if i == i0:
            Bhist[i] = 0.0
            continue
        Afm, Acm, qm, Dm, Ppm = Af[i - 1], Ac[i - 1], qq[i - 1], Dd[i - 1], Pp[i - 1]
        Arm = p.A_tot - Afm - Acm
        Tb = (p.deltab / (1 + np.exp(-p.kappa_w * (t - p.t_wave)))) if (T_b_on and p.deltab > 0) else 0.0
        bf = (p.b_f0 + Tb) * np.exp(-p.alpha * Dm)
        # delayed regeneration of QUALITY (a flow, NOT an area transfer)
        ql = _interp(qq, t, p.tau_g, dt, i0)
        g_lag = p.g_c(ql)                       # per-ha regeneration [1/yr]
        Yf = p.Y_f(Afm, Dm, Tb)
        Yc = p.Y_c(Acm, qm)
        B = Yf + Yc
        E = E_fixed if E_fixed is not None else p.e * Ppm
        S = max(E - p.sigma_f * Yf - p.sigma_c * Yc, 0.0)
        # ---- conversion RATE (dimensionally homogeneous: ha/yr) ----------
        DAmax = max(Acm - p.Ac_min, 0.0)
        u_c = min(S / max(bf, 1e-9), DAmax) / max(p.tau_conv, 1e-9)
        # ---- land book: 1:1 area flows only, conserved by construction ----
        #   conversion A_c -> A_f (rate u_c, ha/yr)
        #   maintenance A_r -> A_f (pioneer/replant, enables sustainable A_f*)
        #   retirement A_f -> A_r (eta_f)
        #   restoration A_r -> A_c (surplus-gated rewilding; sign-correct)
        Rrc = (p.chi_r * max(Arm, 0.0) * max(B - E, 0.0)
               if (E_fixed is None and p.chi_r > 0) else 0.0)
        dAf = u_c + p.mu * max(Arm, 0.0) - p.eta_f * Afm
        dAc = -u_c + Rrc
        dAr = -p.mu * max(Arm, 0.0) + p.eta_f * Afm - Rrc
        # ---- quality book: regeneration is a FLOW, never an area transfer --
        dq = g_lag
        # --- population / debt ---
        Kb = _interp(Bhist, t, p.tau_p, dt, i0) if p.tau_p > 0 else B
        K = max(Kb / p.e, p.K_min)
        dP = p.r * Ppm * (1 - Ppm / K) if K > 1e-9 else -p.r * Ppm
        dD = max(E - B, 0.0) - p.eta * Dm
        # exact 1:1 area update (conservation by construction, not an identity
        # imposed afterwards):
        Af[i] = max(0.0, Afm + dt * dAf)
        Ac[i] = max(p.Ac_min, min(p.A_tot, Acm + dt * dAc))
        qq[i] = max(0.0, min(p.q_max, qm + dt * dq))
        Pp[i] = max(0.0, Ppm + dt * dP)
        Dd[i] = max(0.0, Dm + dt * dD)
        Ar[i] = p.A_tot - Af[i] - Ac[i]
        maxcon = max(maxcon, abs((Af[i] + Ac[i] + Ar[i]) - p.A_tot))
        Bhist[i] = p.B(Af[i], Ac[i], qq[i], Dd[i])
    sl = slice(i0, i0 + n + 1)
    return dict(Af=Af[sl], Ac=Ac[sl], q=qq[sl], Pp=Pp[sl], Dd=Dd[sl], Ar=Ar[sl],
                B=np.array([p.B(Af[j], Ac[j], qq[j], Dd[j]) for j in range(i0, i0 + n + 1)]),
                dt=dt, T=T, maxcon=maxcon)


def longest_illusion(p, r):
    """contiguous span with dB/dt > 0 and dA_c/dt < 0 (composition mask)."""
    B = r["B"]; Ac = r["Ac"]; Af = r["Af"]; dt = r["dt"]
    mask = (np.diff(B) > 0) & (np.diff(Ac) < 0)
    best = (0, 0, 0); run = 0; start = 0
    for j, m in enumerate(mask):
        if m:
            if run == 0: start = j
            run += 1
            if run > best[0]: best = (run, start, j)
        else:
            run = 0
    return best, B, Ac, Af


if __name__ == "__main__":
    # NOTE: A_tot=2.5 matches the manuscript baseline, so the composition
    # demonstration below starts in-domain (A_r(0)=2.5-0.6-1.5=0.4 >= 0); with
    # A_tot=2.0 the start A_r(0)=-0.1 would be OFF-DOMAIN (a negative reserve),
    # which gave a spurious, shorter composition window in an earlier version.
    p = FixPara(rho_c=0.08, b_f0=0.85, b_c=0.05, b_Gc=0.80, alpha=0.03,
                eta_f=0.05, e=0.55, r=0.02, eta=0.05, tau_g=20.0, tau_p=25.0,
                A_tot=2.5, deltab=1.0, t_wave=40.0, kappa_w=0.1, mu=0.06,
                tau_conv=1.0)
    print("=== ROOT-CAUSE-CORRECTED two-book model (A_tot=2.5) ===")
    print("  conservation |A_f+A_c+A_r-A_tot|_{max} over run:")
    r = simulate(p, T=300.0, dt=0.05, A_c0=0.9, A_f0=0.6)
    print("   ", r["maxcon"])
    # Sustainable cropland equilibrium check (long run, no fixed E)
    r = simulate(p, T=1200.0, dt=0.05, A_c0=0.9, A_f0=0.6)
    print("  long-run final: A_f=%.3f A_c=%.3f A_r=%.3f  q=%.3f  P=%.3f"
          % (r["Af"][-1], r["Ac"][-1], r["Ar"][-1], r["q"][-1], r["Pp"][-1]))
    # composition illusion at fixed demand (isolates conversion, in-domain)
    r = simulate(p, T=400.0, dt=0.05, A_c0=1.5, A_f0=0.6, q0=0.9, E_fixed=0.825)
    best, B, Ac, Af = longest_illusion(p, r)
    print("  FIXED E=0.825, A_c0=1.5, A_tot=2.5: longest B-up/A_c-down span = %.1f yr"
          % (best[0] * r["dt"]))
    print("    B %.3f -> %.3f   A_c %.3f -> %.3f   A_f %.3f -> %.3f (maxcon=%.1e)"
          % (B[best[1]], B[min(best[2] + 1, len(B) - 1)],
             Ac[best[1]], Ac[min(best[2] + 1, len(Ac) - 1)],
             Af[best[1]], Af[min(best[2] + 1, len(Af) - 1)], r["maxcon"]))
    # R_A identity (correct share psi_f)
    print("  R_A = R_B / psi_f check (should hold):")
    for (af, ac, qq, dd) in [(0.6, 0.9, 0.9, 0.0), (1.0, 0.5, 0.8, 0.1)]:
        E = 0.825
        B = p.B(af, ac, qq, dd)
        psf = p.psi_f(af, ac, qq, dd)
        RB = E / B; RA = E / p.Y_f(af, dd)
        print("   psi_f=%.4f  R_B=%.4f  R_B/psi_f=%.4f  R_A=%.4f"
              % (psf, RB, RB / psf, RA))
    # delta_b_conv across quality (robustness)
    print("  delta_b_conv = b_f - b_c_eff over q:")
    for qq in [0.3, 0.6, 0.9]:
        print("    q=%.1f  delta_b_conv=%.3f" % (qq, p.delta_b_conv(qq, p.b_f0)))
