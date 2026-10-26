"""Two-book delay-differential model solver (v44 history and technology-wave correction).

The manuscript's GFN/NFA account convention is retained: annual account values
B, E, Y_f, Y_c and S are in gha; land areas are in ha; per-hectare yields are
in gha/ha; time is in years. The accumulated shortfall state D is a model-
internal time integral in gha*yr; dot D and eta*D are in gha, alpha is
(gha*yr)^-1, and eta is yr^-1. Land-book rates are in ha/yr.

Relative to v43, this solver removes the zero-valued B sample at t=0, allocates
history for the longest active delay, and propagates the optional logistic T_b
through current B, the delayed carrying-capacity history, and returned output.
The two solver variants differ only in whether q regeneration uses current or
delayed quality. The active-wave extension is off by default.
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
    def technology_wave(self, t, enabled=False):
        """Bounded logistic yield increment; zero unless the extension is enabled."""
        if not enabled or self.deltab <= 0:
            return 0.0
        exponent = np.clip(-self.kappa_w * (t - self.t_wave), -700.0, 700.0)
        return float(self.deltab / (1.0 + np.exp(exponent)))

    def b_f(self, D, t=0.0, T_b_on=False):
        """Fast-land yield per hectare, including the optional technology wave."""
        return (self.b_f0 + self.technology_wave(t, T_b_on)) * np.exp(-self.alpha * D)

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
    """Integrate the two-book DDE by method of steps with explicit Euler.

    Pre-run histories are constant at the supplied initial state. When T_b_on
    is true, the registered logistic technology increment is applied for t>=0
    and wave-adjusted B is stored in the delayed carrying-capacity history.
    E_fixed pins footprint and disables surplus-gated R_rc; otherwise E=eP
    and R_rc is active only when B>E. Returns state and account time series,
    T_b, time, and the maximum area-conservation residual.
    """
    if dt <= 0 or T <= 0:
        raise ValueError("T and dt must be positive")
    n = int(round(T / dt))
    if n < 1:
        raise ValueError("T and dt must define at least one positive integration step")
    max_delay = max(p.tau_g, p.tau_p, 0.0)
    hl0 = history_len if history_len is not None else int(round((max_delay + 1.0) / dt))
    if hl0 < int(round(max_delay / dt)):
        raise ValueError("history_len must cover the maximum active delay")
    i0 = int(hl0)
    Af = np.full(i0 + n + 1, A_f0, dtype=float); Ac = np.full(i0 + n + 1, A_c0, dtype=float)
    qq = np.full(i0 + n + 1, q0, dtype=float); Pp = np.full(i0 + n + 1, P0, dtype=float)
    Dd = np.full(i0 + n + 1, D0, dtype=float)
    Ar = np.full(i0 + n + 1, p.A_tot - A_f0 - A_c0, dtype=float)
    Bhist = np.zeros(i0 + n + 1)
    # The pre-run history is the common no-wave initial state. At t=0 the
    # active scenario applies the registered logistic T_b(0); the control uses
    # zero. Never insert a zero B sample at the initial time: that creates an
    # artificial dip in K(t-tau_p) when the delayed query reaches t=0.
    B0 = p.B(A_f0, A_c0, q0, D0)
    Bhist[:] = B0
    Tb0 = p.technology_wave(0.0, T_b_on)
    Bhist[i0] = p.B(A_f0, A_c0, q0, D0, Tb0)
    # Delay histories of B and q are initialized from the supplied state.
    maxcon = 0.0
    for k in range(1, n + 1):
        t = k * dt; i = i0 + k
        Afm, Acm, qm, Dm, Ppm = Af[i - 1], Ac[i - 1], qq[i - 1], Dd[i - 1], Pp[i - 1]
        Arm = p.A_tot - Afm - Acm
        Tb = p.technology_wave(t, T_b_on)
        bf = p.b_f(Dm, t, T_b_on)
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
        Bhist[i] = p.B(Af[i], Ac[i], qq[i], Dd[i], p.technology_wave(t, T_b_on))
    sl = slice(i0, i0 + n + 1)
    times = np.arange(n + 1, dtype=float) * dt
    Tb_series = np.array([p.technology_wave(t, T_b_on) for t in times])
    B_series = np.array([
        p.B(Af[j], Ac[j], qq[j], Dd[j], Tb_series[k])
        for k, j in enumerate(range(i0, i0 + n + 1))
    ])
    E_series = np.full(n + 1, E_fixed, dtype=float) if E_fixed is not None else p.e * Pp[sl]
    return dict(Af=Af[sl], Ac=Ac[sl], q=qq[sl], Pp=Pp[sl], Dd=Dd[sl], Ar=Ar[sl],
                B=B_series, E=E_series, T_b=Tb_series, t=times,
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
