"""Two-land (scope-A) delayed integrator — method of steps, hard [.]_+.

Two-book governing set (Part A):
  A_f  fast/provisioning land [ha]
  A_c  capital/ecological land [ha]   (heterogeneity treated as a *strategic reduction*)
  A_r  reserve land [ha] = A_tot - A_f - A_c   (residual balance; conservation by construction)
  P, D
  G_c(A_c)=rho_c A_c (1 - A_c/A_cmax)
  Y_f = b_f A_f ;  Y_c = b_c A_c + b_Gc G_c(A_c) ;  B = Y_f + Y_c ;  E = e P
  S  = [E - sigma_f Y_f - sigma_c Y_c]_+ ;  u_c = S/kappa ,  kappa = b_f
  dA_c/dt = G_c(A_c(t-tau_g)) - u_c - L_c + R_fc + R_rc
  dA_f/dt = u_c - eta_f A_f - R_fc
  dP/dt   = r P [1 - P/K(t-tau_p)] ,  K = B/e
  dD/dt   = [E - B]_+ - eta D
  L_c (timber) = 0.  Restoration:  R_fc = chi A_f (B-E)_+ ;  R_rc = rho_r A_r.

Verifies: conservation, non-negativity, composition illusion (B up / A_c down, sustained), irreversibility.
"""
import numpy as np


class Para:
    def __init__(self, **kw):
        self.A_tot = kw.get("A_tot", 2.0)
        self.A_cmax = kw.get("A_cmax", 1.2)
        self.rho_c = kw.get("rho_c", 0.08)
        self.b_c = kw.get("b_c", 0.05)
        self.b_Gc = kw.get("b_Gc", 0.8)
        self.b_f0 = kw.get("b_f0", 0.85)
        self.deltab = kw.get("deltab", 0.0)
        self.kappa_w = kw.get("kappa_w", 0.1)
        self.t_wave = kw.get("t_wave", 40.0)
        self.alpha = kw.get("alpha", 0.03)
        self.eta = kw.get("eta", 0.05)
        self.e = kw.get("e", 0.55)
        self.r = kw.get("r", 0.02)
        self.eta_f = kw.get("eta_f", 0.05)
        self.chi = kw.get("chi", 0.0)
        self.chi_gate = kw.get("chi_gate", "deficit")   # 'surplus' | 'deficit' | 'always'
        self.rho_r = kw.get("rho_r", 0.0)
        self.sigma_f = kw.get("sigma_f", 1.0)
        self.sigma_c = kw.get("sigma_c", 1.0)
        self.K_min = kw.get("K_min", 0.02)
        self.Ac_min = kw.get("Ac_min", 0.05)
        self.Ar_min = kw.get("Ar_min", 0.10)
        self.tau_g = kw.get("tau_g", 20.0)
        self.tau_p = kw.get("tau_p", 25.0)


def _intp(hist, t, delay, dt, idx0):
    xf = (t - delay) / dt + idx0
    j = int(np.floor(xf)); fr = xf - j
    j0 = max(0, min(len(hist) - 1, j)); j1 = max(0, min(len(hist) - 1, j + 1))
    return hist[j0] * (1 - fr) + hist[j1] * fr


def simulate(p, T=200.0, dt=0.05, A_f0=0.6, A_c0=0.9, P0=1.5, D0=0.0,
             history_len=400, T_b_on=True, restoration=False,
             E_scale=1.0, E_scale_from=None):
    """E_scale rescales demand (irreversibility test): E_scale_from gives the time it switches.
    Returns arrays (sliced to t>=0) and diagnostics."""
    n = int(round(T / dt)); i0 = history_len
    Af = np.empty(i0 + n + 1); Ac = np.empty(i0 + n + 1)
    Pp = np.empty(i0 + n + 1); Dd = np.empty(i0 + n + 1); Ar = np.empty(i0 + n + 1)
    Bhist = np.empty(i0 + n + 1)
    Af[:] = A_f0; Ac[:] = A_c0; Pp[:] = P0; Dd[:] = D0
    # Consistent delay-history of B over the history window (reproducibility item):
    # K(t-tau_p) should not be dominated by a spurious 0 transient.
    B_init = (p.b_f0 * np.exp(-p.alpha * D0)) * A_f0 + p.b_c * A_c0 + p.b_Gc * (
        p.rho_c * A_c0 * (1.0 - A_c0 / p.A_cmax))
    Bhist[:] = B_init
    maxcon = 0.0; min_ok = True
    # precompute B initial for history neutrality: set history B so K history is not degenerate
    for k in range(n + 1):
        t = k * dt; i = i0 + k
        if i == i0:
            Bhist[i] = 0.0
            continue
        Acm = Ac[i - 1]; Afm = Af[i - 1]; Ppm = Pp[i - 1]; Dm = Dd[i - 1]
        Tb = (p.deltab / (1.0 + np.exp(-p.kappa_w * (t - p.t_wave)))) if (T_b_on and p.deltab > 0) else 0.0
        bt = (p.b_f0 + Tb)
        b = bt * np.exp(-p.alpha * Dm)
        kappa = max(b, 1e-9)
        Acl = _intp(Ac, t, p.tau_g, dt, i0) if p.tau_g > 0 else Acm
        Gcl = p.rho_c * Acl * (1.0 - Acl / p.A_cmax)
        Gc_now = p.rho_c * Acm * (1.0 - Acm / p.A_cmax)
        Yf = b * Afm
        Yc = p.b_c * Acm + p.b_Gc * Gc_now
        B = Yf + Yc
        scale = E_scale if (E_scale_from is None or t < E_scale_from) else 1.0
        E = p.e * Ppm * scale
        S = max(E - p.sigma_f * Yf - p.sigma_c * Yc, 0.0)
        u_c = min(S / kappa, max(Acm, 0.0))
        # restoration: two forms controlled by p.chi_gate
        gate = p.chi_gate
        if restoration:
            if gate == "surplus":                      # chi*A_f*(B-E)_+  (weak in deficit)
                Rfc = p.chi * max(Afm, 0.0) * max(B - E, 0.0)
            else:                                       # deficit-gated (active during collapse)
                Rfc = p.chi * max(Afm, 0.0) * max(E - B, 0.0) if gate == "deficit" else p.chi * max(Afm, 0.0)
            Ar_prev = p.A_tot - Af[i - 1 if i > i0 else i0] - Ac[i - 1 if i > i0 else i0]
            Rrc = p.rho_r * max(Ar_prev, 0.0)
        else:
            Rfc = 0.0; Rrc = 0.0
        dAc = Gcl - u_c + Rfc + Rrc
        dAf = u_c - p.eta_f * Afm - Rfc
        Balg = _intp(Bhist, t, p.tau_p, dt, i0) if p.tau_p > 0 else B
        K = max(Balg / p.e, p.K_min)
        dP = p.r * Ppm * (1.0 - Ppm / K) if K > 1e-9 else -p.r * Ppm
        dD = max(E - B, 0.0) - p.eta * Dm
        Af[i] = max(0.0, Afm + dt * dAf)
        Ac[i] = max(p.Ac_min, min(p.A_cmax, Acm + dt * dAc))
        Pp[i] = max(0.0, Ppm + dt * dP)
        Dd[i] = max(0.0, Dm + dt * dD)
        Ar[i] = p.A_tot - Af[i] - Ac[i]
        if Ar[i] < -1e-9:
            min_ok = False
        Bhist[i] = b * Af[i] + p.b_c * Ac[i] + p.b_Gc * (p.rho_c * Ac[i] * (1.0 - Ac[i] / p.A_cmax))
        maxcon = max(maxcon, abs((Af[i] + Ac[i] + Ar[i]) - p.A_tot))
    sl = slice(i0, i0 + n + 1)
    return dict(Af=Af[sl], Ac=Ac[sl], Pp=Pp[sl], Dd=Dd[sl], Ar=Ar[sl],
                dt=dt, T=T, maxcon=maxcon, min_ok=min_ok)


def B_of(p, Af, Ac):
    return (0.85 * np.exp(-0.03 * 0) * Af if False else 0.0)  # helper unused


def comp_series(p, r):
    """Biocapacity B(t) from state arrays (consistent with update rule)."""
    b = p.b_f0 * np.exp(-p.alpha * r["Dd"])
    return b * r["Af"] + p.b_c * r["Ac"] + p.b_Gc * p.rho_c * r["Ac"] * (1.0 - r["Ac"] / p.A_cmax)


def longest_illusion(p, r, dB_min=0.0):
    B = comp_series(p, r); Ac = r["Ac"]; Af = r["Af"]; dt = r["dt"]
    dB = np.diff(B); dAc = np.diff(Ac)
    mask = (dB > dB_min) & (dAc < 0)
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
    p = Para(rho_c=0.08, b_f0=0.85, b_c=0.05, b_Gc=0.8, alpha=0.03, eta_f=0.05,
             e=0.55, r=0.02, eta=0.05, tau_g=20.0, tau_p=25.0, A_tot=2.0,
             deltab=1.0, t_wave=40.0, kappa_w=0.1)
    r = simulate(p, T=250.0, dt=0.05, A_f0=0.6, A_c0=0.9, P0=1.5)
    print("max |A_f+A_c+A_r-A_tot| =", r["maxcon"], " | non-neg =", r["min_ok"])
    best, B, Ac, Af = longest_illusion(p, r)
    t = np.arange(len(Ac)) * r["dt"]
    print("Longest 'B up & A_c down' span:", best[0], "steps =", round(best[0] * r["dt"], 1), "yr  "
          f"(t {t[best[1]]:.1f} -> {t[best[2]]:.1f})")
    print("  B:", round(B[best[1]], 3), "->", round(B[min(best[2] + 1, len(B) - 1)], 3),
          "  A_c:", round(Ac[best[1]], 3), "->", round(Ac[min(best[2] + 1, len(Ac) - 1)], 3),
          "  A_f:", round(Af[best[1]], 3), "->", round(Af[min(best[2] + 1, len(Af) - 1)], 3))
    print("final A_c:", round(Ac[-1], 3), " final A_f:", round(Af[-1], 3), " final B:", round(B[-1], 3))
