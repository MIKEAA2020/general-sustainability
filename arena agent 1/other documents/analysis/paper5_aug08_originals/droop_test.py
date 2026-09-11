"""
Droop slow-nutrient coupling test
=================================
Question: does coupling the manuscript's three-state core (Candidate A) to a
Droop-type internal-quota / external-nutrient subsystem shift the delay-
instability window in regeneration rate r upward toward real fish rates
(r ~ 0.2-1.5 /yr), where the base model predicts delay-independent stability?

Method
------
For each r we compute the interior equilibrium, linearise the DDE about it,
and use the exact rank-1 delay-margin criterion for the existence of a Hopf
crossing:

    characteristic function:  det( i w I - J0 - J1 e^{-i w tau} ) = 0
    J1 = u v^T  (rank 1: only the effort equation sees delayed Z)
    =>  crossing exists at frequency w  <=>  | v^T (i w I - J0)^{-1} u | = 1

The r-window is the set of r for which at least one such crossing exists
(i.e. the delay-induced Hopf pair exists for some institutional delay tau).
This reproduces the "wide omega-scan + bisection" used for finding D2 of
deep_research_report.md and needs no choice of tau (tau is eliminated).

The Droop coupling (standard Droop model, droop1973):
    mu(q) = mu_max (1 - q_min/q)               (quota-limited specific growth)
    dN/dt = mu(q) N (1 - N/K) - q_c E N        (replaces r N (1 - N/K))
    dS/dt = D (S_in - S) - rho_max S/(K_S+S) N (external nutrient pool)
    dq/dt = rho_max S/(K_S+S) - mu(q) q        (internal quota, Droop eq.)
At the interior equilibrium mu(q*) = r, so (N*, Z*, E*) are IDENTICAL to the
base core; only the nutrient pair (S*, q*) is added.  This makes the
comparison clean: same equilibrium, extra slow-feedback channel.

Stages
------
  S1  Validation: reproduce the manuscript's Hopf thresholds at r=0.02
      (tau_- ~ 3.666, tau_+ ~ 150.36 yr, corrected/gated core) and D2's
      r-window upper edge ~0.062/yr at eta=3.0.
  S2  Base r-windows (gated and ungated, eta=0.914 and 3.0).
  S3  Droop-coupled r-windows across a nutrient-slowness sweep.
  S4  Nutrient-mode eigenvalue scaling: is the slow pool actually slow at
      large r?  (structural-slowness analysis)
  S5  Direct nonlinear verification at representative points.
"""
import numpy as np

# ---------------------------------------------------------------------------
# Manuscript base core, Candidate A (three-state)
# ---------------------------------------------------------------------------
K   = 100.0
qc  = 0.001
Emax= 30.0
eta = 0.914
delta0=0.01
Dref= 1.0
taum= 5.0
Zref= 1.0
k   = 10.0
delta = np.log(2.0) / 10.0
LN2K = np.log(2.0) / k

def softplus(x):
    x = np.asarray(x, dtype=float)
    kx = k * x
    if np.isscalar(kx) or kx.ndim == 0:
        if kx > 50: return x
        if kx < -50: return 0.0
        return np.log1p(np.exp(kx)) / k
    out = np.empty_like(kx)
    hi = kx > 50; lo = kx < -50; mid = ~(hi | lo)
    out[hi] = x[hi]; out[lo] = 0.0
    out[mid] = np.log1p(np.exp(kx[mid])) / k
    return out

def base_rhs(y, yd, r, gated, dp=None):
    N, Z, E = y
    Ztau = yd[1]
    S = r * N * (1.0 - N / K)
    qEN = qc * E * N
    dN = S - qEN
    src = max(0.0, softplus(qEN - S) - LN2K + delta)
    dZ = (src - Z) / taum
    fb = eta * E * (Ztau / Dref - E / Emax) + delta0 * Ztau / (Zref + Ztau)
    dE = (1.0 - E / Emax) * fb if gated else fb
    return np.array([dN, dZ, dE])

def base_equilibrium(r, gated):
    Zs = delta
    a = -eta / Emax
    b = eta * Zs / Dref
    c = delta0 * Zs / (Zref + Zs)
    disc = b * b - 4.0 * a * c
    Es = (-b - np.sqrt(disc)) / (2.0 * a)
    Ns = K * (1.0 - qc * Es / r)
    return np.array([Ns, Zs, Es])

# ---------------------------------------------------------------------------
# Droop-coupled core (five states: N, Z, E, S, q)
# ---------------------------------------------------------------------------
def droop_params(D=2.0, Sin=100.0, rhomax=2.0, KS=1.0, qmin=0.1):
    return dict(D=D, Sin=Sin, rhomax=rhomax, KS=KS, qmin=qmin)

def mu_of_q(q, r, dp):
    """Droop quota-limited growth, normalised so that the SPECIES' maximal
    rate is the manuscript's regeneration rate r:

        mu(q) = r (1 - q_min / q)   <= r  for all finite q.

    This preserves the manuscript's meaning of r (intrinsic regeneration
    rate); nutrient scarcity only slows growth below r.  (An un-normalised
    version with a separate mu_max would remove r from the growth law
    entirely, making the equilibrium r-independent -- the wrong test.)
    """
    q = max(float(q), dp['qmin'] * (1.0 + 1e-9))
    return r * (1.0 - dp['qmin'] / q)

def rho_of_S(S, dp):
    return dp['rhomax'] * S / (dp['KS'] + S)

def droop_rhs(y, yd, r, gated, dp):
    N, Z, E, S, q = y
    Ztau = yd[1]
    mu = mu_of_q(q, r, dp)
    Sreg = rho_of_S(S, dp)
    gN = mu * N * (1.0 - N / K)
    qEN = qc * E * N
    dN = gN - qEN
    src = max(0.0, softplus(qEN - gN) - LN2K + delta)
    dZ = (src - Z) / taum
    fb = eta * E * (Ztau / Dref - E / Emax) + delta0 * Ztau / (Zref + Ztau)
    dE = (1.0 - E / Emax) * fb if gated else fb
    dS = dp['D'] * (dp['Sin'] - S) - Sreg * N
    dq = Sreg - mu * q
    return np.array([dN, dZ, dE, dS, dq])

def droop_equilibrium(r, gated, dp, verbose=False, tol=1e-12):
    """Newton on (N, S, q) at fixed Z* = delta, E* from the same quadratic as
    the base core.  mu(q*) < r, so the Droop equilibrium is nutrient-limited
    (N* below the base value).  Returns None if no interior equilibrium."""
    Zs = delta
    a = -eta / Emax; b = eta * Zs / Dref; c = delta0 * Zs / (Zref + Zs)
    disc = b * b - 4.0 * a * c
    Es = (-b - np.sqrt(disc)) / (2.0 * a)
    # seed: q0 from rho ~ rhomax*S/(KS+S) with S=Sin/2 and mu(q0)=r (if feasible)
    q0 = max(dp['qmin'] * 1.5, 0.2)
    N0 = K * (1.0 - qc * Es / max(r, qc * Es * 1.01))
    S0 = dp['Sin'] / 2.0
    x = np.array([N0, S0, q0], dtype=float)

    def F(xx):
        Nn, Sn, qn = xx
        mu = mu_of_q(qn, r, dp)
        rho = rho_of_S(Sn, dp)
        return np.array([
            mu * Nn * (1.0 - Nn / K) - qc * Es * Nn,
            dp['D'] * (dp['Sin'] - Sn) - rho * Nn,
            rho - mu * qn,
        ])

    best = (None, np.inf)
    for it in range(300):
        f = F(x)
        res = np.max(np.abs(f))
        if res < best[1]:
            best = (x.copy(), res)
        if res < tol:
            break
        J = np.zeros((3, 3))
        h = 1e-7
        for j in range(3):
            ep = x.copy(); em = x.copy()
            ep[j] += h; em[j] -= h
            J[:, j] = (F(ep) - F(em)) / (2 * h)
        try:
            step = np.linalg.solve(J, -f)
        except np.linalg.LinAlgError:
            break
        # damped Newton
        s = 1.0
        xnew = x + s * step
        while np.max(np.abs(F(xnew))) > res and s > 1e-4:
            s *= 0.5
            xnew = x + s * step
        x = xnew
        if np.max(np.abs(s * step)) < 1e-15:
            break
    x, res = best
    if res > 1e-9:
        if verbose:
            print(f"  Droop eq did not converge at r={r:.4g} (res={res:.1e})")
        return None
    Nn, Sn, qn = x
    if not (Nn > 0 and 0 < Sn < dp['Sin'] and qn > dp['qmin']):
        return None
    return np.array([Nn, Zs, Es, Sn, qn])

# ---------------------------------------------------------------------------
# Jacobians (central finite differences), 3-state and 5-state
# ---------------------------------------------------------------------------
def jacobians_fd(rhs_fn, eq, gated, r, dp=None, h=1e-7):
    n = len(eq)
    J0 = np.zeros((n, n)); J1 = np.zeros((n, n))
    for j in range(n):
        ep = eq.copy(); em = eq.copy()
        ep[j] += h; em[j] -= h
        J0[:, j] = (rhs_fn(ep, eq, r, gated, dp) - rhs_fn(em, eq, r, gated, dp)) / (2 * h)
        ep2 = eq.copy(); em2 = eq.copy()
        ep2[j] += h; em2[j] -= h
        J1[:, j] = (rhs_fn(eq, ep2, r, gated, dp) - rhs_fn(eq, em2, r, gated, dp)) / (2 * h)
    return J0, J1

def rank1_split(J1, n):
    """J1 should be single-entry: u e_i^T with one nonzero scalar."""
    nz = np.argwhere(np.abs(J1) > 1e-10 * np.max(np.abs(J1)))
    assert len(nz) == 1, f"J1 not rank-1: {nz}"
    i, j = nz[0]
    c = J1[i, j]
    u = np.zeros(n); v = np.zeros(n)
    u[i] = 1.0
    v[j] = c
    return u, v

# ---------------------------------------------------------------------------
# tau-free Hopf-crossing criterion: | v^T (i w I - J0)^{-1} u | = 1
# ---------------------------------------------------------------------------
def hopf_crossings(J0, J1, n, wmin=1e-4, wmax=40.0, nw=8000, verbose=False):
    u, v = rank1_split(J1, n)
    ws = np.geomspace(wmin, wmax, nw)
    gs = np.empty(nw, dtype=complex)
    for iw, w in enumerate(ws):
        M = 1j * w * np.eye(n) - J0
        gs[iw] = v @ np.linalg.solve(M, u)
    mag = np.abs(gs)
    sgn = np.sign(mag - 1.0)
    crossings = []
    for i in range(nw - 1):
        if sgn[i] != sgn[i + 1] and sgn[i] != 0 and sgn[i + 1] != 0:
            lo, hi = ws[i], ws[i + 1]
            glo, ghi = gs[i], gs[i + 1]
            for _ in range(80):  # bisection
                mid = np.sqrt(lo * hi)
                M = 1j * mid * np.eye(n) - J0
                gm = v @ np.linalg.solve(M, u)
                if (np.abs(gm) - 1.0) * (np.abs(glo) - 1.0) <= 0:
                    hi = mid; ghi = gm
                else:
                    lo = mid; glo = gm
            wc = np.sqrt(lo * hi)
            M = 1j * wc * np.eye(n) - J0
            gc = v @ np.linalg.solve(M, u)
            # tau_n = (arg g + 2 pi n)/w ; smallest non-negative tau
            tau0 = (np.angle(gc) % (2 * np.pi)) / wc
            crossings.append((wc, tau0, 2 * np.pi / wc))
    crossings.sort(key=lambda t: t[0])
    return crossings

# ---------------------------------------------------------------------------
# r-window scan
# ---------------------------------------------------------------------------
def window(rmin, rmax, nr, gated, droop=None, eta_override=None,
           verbose=False, nw=8000):
    global eta
    old_eta = eta
    if eta_override is not None:
        eta = eta_override
    rvals = np.geomspace(rmin, rmax, nr)
    out = []
    for r in rvals:
        if droop is None:
            eq = base_equilibrium(r, gated)
            if eq[0] <= 0:
                out.append((r, None, None)); continue
            J0, J1 = jacobians_fd(base_rhs, eq, gated, r, None)
            n = 3
        else:
            eq = droop_equilibrium(r, gated, droop)
            if eq is None:
                out.append((r, None, None)); continue
            J0, J1 = jacobians_fd(droop_rhs, eq, gated, r, droop)
            n = 5
        # tau=0 stability (rightmost eigenvalue of J0)
        lam0 = np.linalg.eigvals(J0)
        re_max0 = float(np.max(lam0.real))
        cr = hopf_crossings(J0, J1, n, nw=nw, verbose=verbose)
        out.append((r, cr, eq))
    eta = old_eta
    return out

def window_edges(res):
    """(rmin_in, rmax_in, note) of the delay-induced instability window."""
    inwin = [r for (r, cr, note) in res if cr is not None and len(cr) > 0]
    if not inwin:
        return None
    return (min(inwin), max(inwin))

def intervals(rs):
    """Contiguous (on the log grid) intervals of a sorted r list."""
    if not rs:
        return []
    rs = sorted(rs)
    out = []
    lo = hi = rs[0]
    for x in rs[1:]:
        if x / hi < 1.06:      # consecutive log-grid points (factor ~1.024)
            hi = x
        else:
            out.append((lo, hi))
            lo = hi = x
    out.append((lo, hi))
    return out

# ---------------------------------------------------------------------------
# direct nonlinear verification (fixed-step RK4 DDE)
# ---------------------------------------------------------------------------
def integrate_dde(rhs_fn, y0, hist, T, tau, r, gated, dp, dt=0.05):
    n = len(y0)
    nsteps = int(round(T / dt))
    h = T / nsteps
    ys = np.zeros((nsteps + 1, n))
    ys[0] = y0
    def delayed(t):
        if t <= 0:
            return hist(t)
        ti = t / h
        i = int(np.floor(ti))
        if i >= nsteps:
            return ys[nsteps]
        f = ti - i
        return (1 - f) * ys[i] + f * ys[i + 1]
    for i in range(nsteps):
        t = i * h
        y = ys[i]
        k1 = rhs_fn(y, delayed(t - tau), r, gated, dp)
        k2 = rhs_fn(y + h / 2 * k1, delayed(t + h / 2 - tau), r, gated, dp)
        k3 = rhs_fn(y + h / 2 * k2, delayed(t + h / 2 - tau), r, gated, dp)
        k4 = rhs_fn(y + h * k3, delayed(t + h - tau), r, gated, dp)
        ys[i + 1] = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return ys

def measure_tail(ys, dt, frac=0.5):
    tail = ys[int(len(ys) * frac):]
    N = tail[:, 0]
    mn = N.mean()
    crossings = [j for j in range(1, len(N)) if N[j - 1] < mn <= N[j]]
    if len(crossings) >= 3:
        per = np.median(np.diff(crossings)) * dt
    else:
        per = None
    amp = N.max() - N.min()
    return per, amp

def main():
    np.set_printoptions(precision=6, suppress=True)
    print("=" * 78)
    print("S1  VALIDATION  (manuscript Hopf thresholds at r=0.02, eta=0.914)")
    print("=" * 78)
    for gated in (True, False):
        r = 0.02
        eq = base_equilibrium(r, gated)
        J0, J1 = jacobians_fd(base_rhs, eq, gated, r, None)
        cr = hopf_crossings(J0, J1, 3, wmin=1e-4, wmax=40.0, nw=12000)
        print(f"  gated={gated}: N*={eq[0]:.6f} Z*={eq[1]:.6f} E*={eq[2]:.6f}")
        print(f"    crossings (w, tau0, period):")
        for w, tau0, P in cr:
            print(f"      w={w:.6f}  tau0={tau0:9.4f} yr   period={P:9.3f} yr")
        print(f"    (manuscript corrected core: tau_- ~ 3.666 yr, tau_+ ~ 150.36 yr)")
    print()
    print("=" * 78)
    print("S2  BASE r-WINDOWS (delay-induced Hopf pair exists in r)")
    print("=" * 78)
    for gated in (True, False):
        for eta_v in (0.914, 3.0):
            res = window(0.003, 2.0, 400, gated, eta_override=eta_v)
            ed = window_edges(res)
            print(f"  gated={gated} eta={eta_v}: window_edges={ed}")
    print()
    print("=" * 78)
    print("S3  DROOP-COUPLED r-WINDOWS  (same equilibrium; +S, +q states)")
    print("=" * 78)
    variants = [
        ("rich nutrient     (D=0.5, Sin=500, rhomax=0.5, KS=10)",
         droop_params(0.5, 500.0, 0.5, 10.0)),
        ("moderate nutrient (D=0.5, Sin=100, rhomax=0.5, KS=10)",
         droop_params(0.5, 100.0, 0.5, 10.0)),
        ("lean nutrient     (D=0.2, Sin=50,  rhomax=0.2, KS=10)",
         droop_params(0.2, 50.0, 0.2, 10.0)),
        ("very lean + slow  (D=0.05,Sin=100, rhomax=0.1, KS=10)",
         droop_params(0.05, 100.0, 0.1, 10.0)),
    ]
    for name, dp in variants:
        res = window(0.005, 2.0, 250, True, droop=dp, nw=6000)
        ed = window_edges(res)
        have = [r for (r, cr, n) in res if n is not None]
        inw = [r for (r, cr, n) in res if cr is not None and len(cr) > 0]
        text = f"  {name}:\n    interior equilibrium exists r in {intervals(have)}"
        text += f"\n    delay-Hopf window r in {intervals(inw) if inw else 'NONE (empty)'}"
        print(text)
        # nearest-grid detail rows
        for rtarget in (0.02, 0.2, 0.5, 1.0):
            if not have:
                break
            idx = min(range(len(res)), key=lambda i: abs(res[i][0] - rtarget))
            r, cr, n = res[idx]
            if abs(r - rtarget) / rtarget > 0.15:
                continue
            if n is None:
                print(f"      r~{r:.3g}: no interior equilibrium")
            elif cr:
                w, tau0, P = cr[0]
                print(f"      r~{r:.3g}: eq N*={n[0]:.2f}  crossings={len(cr)}"
                      f"  first P={P:.0f} yr")
            else:
                print(f"      r~{r:.3g}: eq N*={n[0]:.2f}  crossings=0 (delay-stable)")
    print()
    print("=" * 78)
    print("S4  NUTRIENT-MODE SCALING  (is the slow pool slow at large r?)")
    print("=" * 78)
    for name, dp in [("moderate", droop_params(0.5, 100.0, 0.5, 10.0)),
                     ("very lean", droop_params(0.05, 100.0, 0.1, 10.0))]:
        print(f"  {name} nutrient: J0 eigenvalues (Re, Im), sorted by Re;"
              f" quota mode should be ~ -r")
        for r in (0.01, 0.02, 0.1, 0.5, 1.0, 1.5):
            eq = droop_equilibrium(r, True, dp)
            if eq is None:
                print(f"    r={r:5.2f}: no interior equilibrium"); continue
            J0, J1 = jacobians_fd(droop_rhs, eq, True, r, dp)
            lam = np.linalg.eigvals(J0)
            lam = lam[np.argsort(lam.real)]
            s = ", ".join(f"{l.real:+.4f}{l.imag:+.3f}i" for l in lam)
            slowest = lam[-1]  # max real part = slowest-decaying mode
            tsc = 1.0 / abs(slowest.real) if abs(slowest.real) > 0 else np.inf
            print(f"    r={r:5.2f} 1/r={1/r:7.2f} yr: [{s}]"
                  f"  slowest timescale {tsc:8.1f} yr")
    print()
    print("=" * 78)
    print("S5  DIRECT NONLINEAR VERIFICATION (RK4 DDE, gated core, tau=5.5 yr)")
    print("=" * 78)
    TAU = 5.5  # yr, inside the sustained-oscillation regime at r=0.02
    for r in (0.02, 0.3, 1.0):
        eq = base_equilibrium(r, True)
        hist = lambda t: eq
        y0 = eq.copy(); y0[0] *= 1.03   # 3% perturbation
        ys = integrate_dde(base_rhs, y0, hist, 3000.0, TAU, r, True, None, dt=0.05)
        per, amp = measure_tail(ys, 0.05)
        print(f"  BASE   r={r:5.2f}: tail period={per if per is None else round(per,1)} yr"
              f"  tail amp(N)={amp:.3f}")
    dp = droop_params(0.5, 100.0, 0.5, 10.0)  # moderate
    for r in (0.02, 0.2, 0.5):
        eq = droop_equilibrium(r, True, dp)
        if eq is None:
            print(f"  DROOP  r={r:5.2f}: no equilibrium"); continue
        hist = lambda t: eq
        y0 = eq.copy(); y0[0] *= 1.03
        ys = integrate_dde(droop_rhs, y0, hist, 3000.0, TAU, r, True, dp, dt=0.05)
        per, amp = measure_tail(ys, 0.05)
        print(f"  DROOP  r={r:5.2f}: eq N*={eq[0]:.2f}  tail period="
              f"{per if per is None else round(per,1)} yr  tail amp(N)={amp:.3f}"
              f"  N_end={ys[-1,0]:.2f}")

if __name__ == "__main__":
    main()
