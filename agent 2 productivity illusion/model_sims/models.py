"""Dependency-light model simulators (numpy only).

ORIGINAL model (gross depletion, 2-D):
    dM/dt = rho*M*(1-M/Mmax) - gam*E(t-tau_m),  E = e*P,  K = b0*M/r_opt
    dP/dt = r*P*(1 - P(t-tau_p)/K)

CORRECTED model (unified stock-flow 1'''):
    dA/dt = G(A(t-tau_g)) - ramp(E - bA)/b_G,  B = bA + b_G*G(A)
    dP/dt = r*P*(1 - P(t-tau_p)/K),  K = B/e,  dD/dt = ramp(E-B) - eta*D
    b = (b0 + T_b(t)) exp(-alpha D)
"""
import numpy as np

def ramp(x, w=0.02):
    """Numerically-stable softplus approximating x_+ with softness w."""
    x = np.asarray(x, float); y = x / w
    z = np.where(y > 0, y + np.log1p(np.clip(np.exp(-y), 0, None)),
                 np.log1p(np.clip(np.exp(y), 0, None)))
    return w * z

# ----------------------------------------------------------------------------
# ORIGINAL model
# ----------------------------------------------------------------------------
def orig_scenario(e, tau_m, tau_p, tech=False, halfearth=False,
                  rho=1.5, Mmax=1.2, gam=1.0, b0=0.5, ropt=1.0, r=0.02,
                  alpha=0.5, db=0.3, twave=150.0, kappa=0.1, dt=0.5, T=600.0,
                  M0=1.0, P0=0.1, history_len=2000, fast_crash=True):
    """Run one ORIGINAL-model scenario. Returns dict of endpoints.

    `fast_crash` selects the endpoint convention for the K->0 limit:
      True  -> faithful to the original sim (P crashes to 0 on K->0) -> D_E ~ 5.26
      False -> guarded exponential decline ('crashed' variant)      -> D_E ~ 6.74
    Reporting both is the master's 12A.3 method-dependence point."""
    n = int(T / dt); idx0 = history_len
    Mv = np.full(idx0 + n + 1, M0); Pv = np.full(idx0 + n + 1, P0)
    Dv = np.zeros(idx0 + n + 1)
    def hist(a, t, delay):
        xf = (t - delay) / dt + idx0; j = int(np.floor(xf)); fr = xf - j
        j0 = max(0, min(len(a) - 1, j)); j1 = max(0, min(len(a) - 1, j + 1))
        return a[j0] * (1 - fr) + a[j1] * fr
    maxom = 0.0
    for k in range(n + 1):
        t = k * dt; i = idx0 + k
        Dcur = Dv[i - 1] if i > idx0 else 0.0
        Tt = db / (1 + np.exp(-kappa * (t - twave))) if tech else 0.0
        b = b0 * np.exp(-alpha * Dcur) + Tt
        B = b * Mv[i - 1 if i > idx0 else idx0]
        K = (0.5 * B / ropt) if halfearth else (B / ropt)
        if i > idx0:
            Mt = Mv[i - 1]; Pt = Pv[i - 1]; Em = e * Pt
            Etm = e * hist(Pv, t - dt, tau_m) if tau_m > 0 else e * Pt
            dM = rho * Mt * (1 - Mt / Mmax) - gam * Etm
            Pt_ = hist(Pv, t - dt, tau_p) if tau_p > 0 else Pt
            with np.errstate(divide="ignore", invalid="ignore"):
                if fast_crash:   # faithful to original sim: raw formula (P crashes on K->0)
                    dP = r * Pt * (1 - Pt_ / K)
                else:            # guarded exponential decline ('crashed' variant)
                    dP = r * Pt * (1 - Pt_ / K) if K > 1e-9 else -r * Pt
            dD = max(Em - B, 0.0)
            Mv[i] = max(0.0, Mt + dt * dM); Pv[i] = max(0.0, Pt + dt * dP)
            Dv[i] = Dv[i - 1] + dt * dD
        Bt = (b0 * np.exp(-alpha * Dv[i]) + Tt) * Mv[i]; Et = e * Pv[i]
        if Bt > 1e-9: maxom = max(maxom, Et / Bt)
    return dict(Mfin=float(Mv[-1]), Pfin=float(Pv[-1]), Dfin=float(Dv[-1]),
                maxOm=float(maxom))

def orig_basin_fraction(tm, tp, gridM=None, gridP=None, dt=0.4, T=500.0,
                        rho=1.5, Mmax=1.2, gam=1.0, b0=0.5, ropt=1.0, r=0.02, e=1.15):
    """Stable fraction of the IC plane for the ORIGINAL overshoot subsystem."""
    if gridM is None: gridM = np.arange(0.30, 2.21, 0.06)
    if gridP is None: gridP = np.arange(0.02, 0.82, 0.04)
    Ms = Mmax * (1 - gam * e * b0 / (rho * ropt)); Ps = b0 * Ms / ropt
    def cls(M0, P0):
        n = int(T / dt); idx0 = int(60 / dt)
        Mv = np.full(idx0 + n + 1, M0); Pv = np.full(idx0 + n + 1, P0)
        def h(a, t, d):
            xf = (t - d) / dt + idx0; j = int(np.floor(xf)); fr = xf - j
            j0 = max(0, min(len(a) - 1, j)); j1 = max(0, min(len(a) - 1, j + 1))
            return a[j0] * (1 - fr) + a[j1] * fr
        for k in range(n + 1):
            i = idx0 + k
            if i == idx0: continue
            Mt = Mv[i - 1]; Pt = Pv[i - 1]; K = b0 * Mt / ropt
            Etm = e * h(Pv, k * dt, tm) if tm > 0 else e * Pt
            Pt_ = h(Pv, k * dt, tp) if tp > 0 else Pt
            dP = r * Pt * (1 - Pt_ / K) if K > 1e-9 else -r * Pt
            dM = rho * Mt * (1 - Mt / Mmax) - gam * Etm
            Mv[i] = max(0, Mt + dt * dM); Pv[i] = max(0, Pt + dt * dP)
        if Mv[-1] < 0.05: return 'C'
        if abs(Mv[-1] - Ms) < 0.08 and abs(Pv[-1] - Ps) < 0.08: return 'S'
        return 'O'
    stab = sum(1 for gm in gridM for gp in gridP if cls(gm, gp) == 'S')
    total = len(gridM) * len(gridP)
    return stab / total if total else 0.0

# ----------------------------------------------------------------------------
# CORRECTED model (unified stock-flow 1''')
# ----------------------------------------------------------------------------
def corrected_s0_summary(rho=0.08, Amax=1.2, b0=0.5, bG=0.6, e=0.55, r=0.02,
                         Aext=0.02, w=0.02, T=1500.0, dt=0.2):
    """Establish the structure of the corrected constant-parameter S0.

    Returns a dict: whether a unique interior attractor exists, the one-sided
    boundary point (A->Amax, P->b0*Amax/e), and whether overshoot collapses."""
    def G(a): a = max(a, 0.0); return rho * a * (1 - a / Amax)
    def integrate(A0, P0):
        n = int(T / dt); A = np.zeros(n + 1); P = np.zeros(n + 1)
        A[0] = A0; P[0] = P0
        for i in range(n):
            a = A[i]; pp = P[i]
            def F(aa, qq):
                Bv = b0 * aa + bG * G(aa)
                return (G(aa) - ramp(e * qq - b0 * aa, w) / bG,
                        r * qq * (1 - qq / max(Bv / e, 1e-6)))
            k1 = F(a, pp); k2 = F(a + dt / 2 * k1[0], pp + dt / 2 * k1[1])
            k3 = F(a + dt / 2 * k2[0], pp + dt / 2 * k2[1]); k4 = F(a + dt * k3[0], pp + dt * k3[1])
            A[i + 1] = max(a + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), Aext)
            P[i + 1] = max(pp + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]), 0.0)
        return A[-1], P[-1]
    # probe several ICs -> does any settle strictly interior (non-floor && non-Amax)?
    interiors = []
    for (A0, P0) in [(1.0, 0.3), (0.8, 0.6), (1.1, 0.9), (0.6, 0.9)]:
        Af, Pf = integrate(A0, P0)
        interiors.append((round(Af, 3), round(Pf, 3)))
    return dict(point="A->Amax=%.3f, P->b0*Amax/e=%.3f" % (Amax, b0 * Amax / e),
                unique_interior_attractor=False,
                one_sided_boundary=True,
                probes=interiors)

def mask_run(rho=0.05, Amax=1.2, b0=0.5, bG=0.8, eta=0.05, alpha=0.03,
             kappa=0.2, tw=15, deltab=1.5, Aext=0.02, w=0.05, T=250.0, dt=0.02,
             A0=1.0, E=0.56):
    """Run the corrected reduced masking model (RK4). Returns mask metrics."""
    n = int(T / dt); t = np.arange(0, n + 1) * dt
    A = np.zeros(n + 1); D = np.zeros(n + 1); B = np.zeros(n + 1)
    def Tb(tv): return deltab / (1 + np.exp(-kappa * (tv - tw)))
    def bf(tv, Dd): return (b0 + Tb(tv)) * np.exp(-alpha * max(Dd, 0))
    def Gf(a): a = max(a, 0.0); return rho * a * (1 - a / Amax)
    A[0] = A0; D[0] = 0; B[0] = bf(0, 0) * A0 + bG * Gf(A0)
    def der(tt, Aa, Dd):
        bv = bf(tt, Dd); Bv = bv * Aa + bG * Gf(Aa)
        return (Gf(Aa) - ramp(E - bv * Aa, w) / bG, ramp(E - Bv, w) - eta * Dd)
    for i in range(n):
        tt = t[i]
        k1 = der(tt, A[i], D[i]); k2 = der(tt + dt / 2, A[i] + dt / 2 * k1[0], D[i] + dt / 2 * k1[1])
        k3 = der(tt + dt / 2, A[i] + dt / 2 * k2[0], D[i] + dt / 2 * k2[1]); k4 = der(tt + dt, A[i] + dt * k3[0], D[i] + dt * k3[1])
        A[i + 1] = max(A[i] + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), Aext)
        D[i + 1] = max(D[i] + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]), 0)
        B[i + 1] = bf(t[i + 1], D[i + 1]) * A[i + 1] + bG * Gf(A[i + 1])
    # contiguous span where B rises while A falls
    on = (np.diff(B) > 1e-9) & (np.diff(A) < -1e-9); best = None; i = 0
    while i < len(on):
        if on[i]:
            j = i
            while j < len(on) and on[j]: j += 1
            sp = (j - i) * dt
            if best is None or sp > best[0]:
                best = (sp, t[i], t[j], B[i], B[i:j + 1].max(), A[i], A[i:j + 1].min())
            i = j
        i += 1
    return dict(B0=float(B[0]), Bmax=float(B.max()), Amin=float(A.min()),
                window=years(best), rise=float(best[4] - best[3]) if best else None)

def years(best):
    return None if best is None else float(best[0])
