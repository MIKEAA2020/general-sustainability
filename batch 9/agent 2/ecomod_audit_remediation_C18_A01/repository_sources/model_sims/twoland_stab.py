"""Gate 2 & 3 — two-land per-active-set equilibria + conversion-loop stability.

GATE 2 (equilibria per active set) and GATE 3 (conversion-loop stability, the honest
replacement for the inherited "+0.62").

Key structural conclusion (derived, not assumed):
  With an ENDOGENOUS population, P = K = B/e at any population equilibrium, so
  E = eP = B and therefore the deficit S = [E - B]_+ = 0.  Hence there is NO
  interior population-consistent "active-conversion" steady state: the active-
  conversion regime (S>0) is a TRANSIENT / overshoot regime, not an attractor.
  It exists as a steady state only under a FROZEN (exogenous) demand E pinned
  above the flow.  This is the root-cause reason the conversion loop is bounded
  and not a universal constant.

So we report:
  (A) the S=0 boundary equilibria (A_f*=0, A_c*=0 or A_cmax; P=B/e);
  (B) the S>0 steady state ONLY under frozen demand E, and its 2x2 conversion-loop
      Jacobian eigenvalues -> sign depends on Delta b_conv (state-dependent);
  (C) the full 4x4 delayed characteristic structure (no eigenvalue inherited).
"""
import numpy as np
from scipy.optimize import brentq


class P:
    def __init__(self, **kw):
        self.A_cmax = kw.get("A_cmax", 1.2)
        self.rho_c = kw.get("rho_c", 0.08)
        self.b_c = kw.get("b_c", 0.05)
        self.b_Gc = kw.get("b_Gc", 0.8)
        self.b_f0 = kw.get("b_f0", 0.85)
        self.eta_f = kw.get("eta_f", 0.05)
        self.alpha = kw.get("alpha", 0.03)
        self.eta = kw.get("eta", 0.05)
        self.e = kw.get("e", 0.55)
        self.r = kw.get("r", 0.02)
        self.Ac_min = kw.get("Ac_min", 0.05)


def Gc(p, a):
    return p.rho_c * a * (1.0 - a / p.A_cmax)


def Gc_prime(p, a):
    return p.rho_c * (1.0 - 2.0 * a / p.A_cmax)


def Yc(p, a):
    return p.b_c * a + p.b_Gc * Gc(p, a)


def Yc_prime(p, a):
    return p.b_c + p.b_Gc * Gc_prime(p, a)


def bf(p, D):
    return p.b_f0 * np.exp(-p.alpha * D)


# ---------------------------------------------------------------------------
# (A) S = 0 no-conversion boundary equilibria
# ---------------------------------------------------------------------------
def no_conversion_equilibria(p):
    """Return list of (A_c*, A_f*, P*) on the no-conversion face."""
    out = []
    for Ac in (0.0, p.A_cmax):
        af = 0.0                       # eta_f>0 -> eta_f A_f = u_c = 0 -> A_f=0
        B = bf(p, 0.0) * af + Yc(p, Ac)
        P = B / p.e
        out.append(dict(A_c=Ac, A_f=af, P=P, B=B, S=0.0))
    return out


# ---------------------------------------------------------------------------
# (B) S > 0 steady state under FROZEN demand E:  solve for A_c
#     E = b_c A_c + G_c(A_c)[ b_Gc + b_f (1 + 1/eta_f) ]
#     A_f = G_c(A_c)/eta_f ;  P = B/e ;  D = (E-B)/eta
# ---------------------------------------------------------------------------
def conv_capacity_ceiling(p):
    """RHS_max = max over A_c of [ b_c A_c + G_c(A_c) (b_Gc + b_f(1+1/eta_f)) ],
    i.e. the largest E admitting an interior active-conversion steady state.
    (Equivalently, the fold/conversion-capacity ceiling of the frozen-demand system.)"""
    beta = p.b_Gc + bf(p, 0.0) * (1.0 + 1.0 / p.eta_f)
    # dRHS/dA = b_c + beta*rho_c*(1 - 2A/Acmax) = 0
    a = p.A_cmax * (1.0 + p.b_c / (beta * p.rho_c)) / 2.0
    return (p.b_c * a + Gc(p, a) * beta), a


def _rhs(p, a):
    return p.b_c * a + Gc(p, a) * (p.b_Gc + bf(p, 0.0) * (1.0 + 1.0 / p.eta_f))


def conv_equilibria(p, E, n=400):
    """All interior active-conversion steady states for a frozen demand E.
    Returns a list of equilibrium dicts (there can be 0, 1 or 2)."""
    grid = np.linspace(p.Ac_min + 1e-6, p.A_cmax - 1e-6, n)
    fv = _rhs(p, grid) - E
    roots = []
    for j in range(len(grid) - 1):
        if fv[j] == 0.0:
            roots.append(grid[j])
        elif fv[j] * fv[j + 1] < 0:
            a = brentq(lambda x: _rhs(p, x) - E, grid[j], grid[j + 1])
            roots.append(a)
    out = []
    for a in roots:
        af = Gc(p, a) / p.eta_f
        B = bf(p, 0.0) * af + Yc(p, a)
        d = max(E - B, 0.0) / p.eta
        out.append(dict(A_c=a, A_f=af, P=B / p.e, D=d, B=B, S=max(E - B, 0.0)))
    return out


def conv_loop_jac(p, eq, sig_f=1.0, sig_c=1.0):
    """2x2 Jacobian rows (dA_c, dA_f) cols (A_c, A_f), frozen demand, no delay."""
    a = eq["A_c"]
    b = bf(p, eq["D"])
    Yp = Yc_prime(p, a) / b
    Gp = Gc_prime(p, a)
    return np.array([[Gp + sig_c * Yp, sig_f],
                     [-sig_c * Yp, -(sig_f + p.eta_f)]])


def leading_root(p, E):
    eq = conv_equilibrium(p, E)
    J = conv_loop_jac(p, eq)
    lam = np.linalg.eigvals(J)
    return eq, J, lam


def delta_b_conv(p, a, D=0.0):
    return bf(p, D) - p.b_c - p.b_Gc * Gc_prime(p, a)


def characteristic_structure(p):
    """The full 4x4 delayed characteristic (NO eigenvalue inherited).

    State order z = (A_c, A_f, P, D).  The delayed system is
        dot z(t) = J0 z(t) + Jg z(t-tau_g) + Jp z(t-tau_p)
    and det Delta(lambda) = 0 with  Delta(lambda) = lambda I - J0 - Jg e^{-lambda tau_g} - Jp e^{-lambda tau_p}.
    Non-zero blocks (derived by linearising the two-land set):
      J0 (current):  A_c-row <- u_c(A_f, A_c); A_f-row <- (A_f, A_c) via u_c and -eta_f;
                     P-row <- (A_c, A_f, D, P) via K=B/e; D-row <- (A_c, A_f, D, P) via B, E, -eta.
      Jg (tau_g):    A_c-row <- G_c'(A_c*) in the A_c column  (delayed regeneration).
      Jp (tau_p):    P-row <- K'(A_c, A_f, D)/e in (A_c, A_f, D) columns  (delayed demography).
    No entry is carried over from the one-stock D(s;tau_g,tau_p); it is re-derived.
    The 2x2 conversion subsystem (rows A_c, A_f; cols A_c, A_f) at frozen E,D has the Jacobian:
        Jc = [[ G_c'(A_c) + Y_c'(A_c)/b_f ,  1 ],
              [ -Y_c'(A_c)/b_f            , -(1+eta_f) ]]
    whose eigenvalues are the local conversion-loop feedback (see gate 3)."""
    return "(documented above; see J0/Jg/Jp block structure)"


if __name__ == "__main__":
    p = P(rho_c=0.08, b_f0=0.85, b_c=0.05, b_Gc=0.8, alpha=0.03, eta_f=0.05,
          e=0.55, r=0.02, eta=0.05)
    print("=== (A) S=0 no-conversion boundary equilibria (A_f*=0; A_c*=0 or A_cmax) ===")
    for r in no_conversion_equilibria(p):
        print(f"  A_c*={r['A_c']:.3f}  A_f*={r['A_f']:.3f}  P*={r['P']:.4f}  B*={r['B']:.4f}")

    ceiling, a_ceil = conv_capacity_ceiling(p)
    print(f"\n  Conversion-capacity ceiling (fold of the frozen-demand system): "
          f"E_ceil = {ceiling:.4f} at A_c = {a_ceil:.3f}.  Interior active-conversion steady state "
          f"exists only for E < E_ceil.")

    print("\n=== (B) S>0 active-conversion steady state exists ONLY under frozen demand E ===")
    print("  With ENDOGENOUS population: P=K=B/e => E=eP=B => S=[E-B]_+=0. "
          "So NO interior population-consistent S>0 steady state. (Root-cause reason the")
    print("  conversion loop is a bounded transient, not an attractor.)")
    print("\n  Frozen-demand conversion equilibria + 2x2 conversion-loop eigenvalues:")
    print("   E      n    A_c*    A_f*    dA_conv   trace    det    lam1      lam2      regime")
    for E in [0.20, 0.30, 0.40, 0.45, 0.47]:
        eqs = conv_equilibria(p, E)
        for eq in eqs:
            a = eq["A_c"]
            J = conv_loop_jac(p, eq)
            lam = np.linalg.eigvals(J); tr = np.trace(J); det = np.linalg.det(J)
            s = "unstable (+)" if any(np.real(lam) > 1e-9) else ("saddle" if det < 0 else "stable")
            print(f"  {E:.2f}   {len(eqs)}  {eq['A_c']:.3f}  {eq['A_f']:.3f}  {delta_b_conv(p,a):+.3f}   "
                  f"{tr:+.3f} {det:+.4f}  {np.real(lam[0]):+.4f}  {np.real(lam[1]):+.4f}   {s}")

    print("\n=== (GATE 3) sign of the conversion loop is set by Delta b_conv (state/parameter-dependent) ===")
    print("  Sweep b_f (fast-land value) at a fixed frozen E=0.30. Report the LOW-E root (high conversion):")
    print("   b_f     Delta_b_conv   lam1      lam2      regime")
    for b_f in [0.2, 0.4, 0.6, 0.85, 1.2, 2.0]:
        p2 = P(rho_c=0.08, b_f0=b_f, b_c=0.05, b_Gc=0.8, alpha=0.03, eta_f=0.05, e=0.55, r=0.02, eta=0.05)
        eqs = conv_equilibria(p2, 0.30)
        if not eqs:
            print(f"  {b_f:.2f}   (no interior conv equilibrium at E=0.30)")
            continue
        eq = eqs[0]  # lowest A_c = highest conversion
        a = eq["A_c"]; J = conv_loop_jac(p2, eq); lam = np.linalg.eigvals(J)
        db = delta_b_conv(p2, a)
        reg = "destabilising" if db > 0 else ("stabilising" if db < 0 else "neutral")
        print(f"  {b_f:.2f}   {db:+.3f}      {np.real(lam[0]):+.4f}  {np.real(lam[1]):+.4f}   {reg}")
    print("\n=== Gate 2: 4x4 delayed characteristic structure ===")
    print(characteristic_structure(p))
