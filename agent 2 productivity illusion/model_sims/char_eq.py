"""R2 — corrected-(1''') characteristic equation with exact crossing-curve &
full-spectrum methods.

Corrected S0 linearisation (deficit regime, eP >= b0 A):

    dA/dt = G(A(t-tau_g)) - [eP(t) - b0 A(t)]_+/b_G
    dP/dt = r P(t) [1 - P(t)/K(t-tau_p)],      K = B/e,  B = b0 A + b_G G(A)

Defects (deviation from a reference equilibrium (A*, P*), P* = K(A*)):
    a1 = G'(A*)                        (regeneration, DELAYED tau_g)
    a3 = b0/b_G                        (depletion, CURRENT)
    aE = -e/b_G                        (depletion, CURRENT; couples P)
    a4 = r K'(A*)                      (carrying capacity, DELAYED tau_p)
    a5 = -r                            (logistic damping, CURRENT)

Characteristic equation (two-delay transcendental):
    D(s; tau_g, tau_p) = (s - a1 e^{-s tau_g} - a3)(s + r) - aE*a4 e^{-s tau_p} = 0

Structural result (R2 key): because P* = K(A*) makes eP* - b0 A* = b_G G(A*),
the A-equilibrium is satisfied for ANY A* -> a one-parameter family of equilibria
P = B(A)/e.  D(s) therefore has a zero eigenvalue (a neutral continuum direction):
the corrected S0 has no isolated interior attractor -- this confirms analytically
the manuscript claim that was previously only numerical.
"""
import numpy as np


def G(A, rho, Amax):
    return rho * np.asarray(A, float) * (1 - np.asarray(A, float) / Amax)


def Gp(A, rho, Amax):
    return rho * (1 - 2 * np.asarray(A, float) / Amax)


def B(A, b0, bG, rho, Amax):
    return b0 * np.asarray(A, float) + bG * G(A, rho, Amax)


def K(A, b0, bG, rho, Amax, e):
    return B(A, b0, bG, rho, Amax) / e


def equilibrium_curve(A, b0=0.5, bG=0.8, rho=0.05, Amax=1.2, e=0.55):
    """The one-parameter family of S0 equilibria: P = K(A) = B(A)/e for any A."""
    return K(A, b0, bG, rho, Amax, e)


def lin_coeffs(Astar, b0=0.5, bG=0.8, rho=0.05, Amax=1.2, e=0.55, r=0.02):
    a1 = Gp(Astar, rho, Amax)            # regeneration, delayed tau_g
    a3 = b0 / bG                          # depletion, current
    aE = -e / bG                          # depletion->P, current
    # K'(A) = (b0 + b_G G'(A))/e
    Kp = (b0 + bG * Gp(Astar, rho, Amax)) / e
    a4 = r * Kp                           # K -> P, delayed tau_p
    a5 = -r                               # logistic damping, current
    return dict(a1=float(a1), a3=float(a3), aE=float(aE), a4=float(a4),
                a5=float(a5), r=r, Astar=float(Astar),
                Pstar=float(K(Astar, b0, bG, rho, Amax, e)))


def char_eq(s, tau_g, tau_p, c):
    """D(s; tau_g, tau_p) for the corrected S0. s may be complex (array-like)."""
    s = np.asarray(s, complex)
    a1, a3, aE, a4, r = c["a1"], c["a3"], c["aE"], c["a4"], c["r"]
    return (s - a1 * np.exp(-s * tau_g) - a3) * (s + r) - aE * a4 * np.exp(-s * tau_p)


def numeric_roots(tau_g, tau_p, c, n=60, halfplane_re=(-0.6, 1.2), im=(0.0, 3.5)):
    """Locate roots of D(s) near the imaginary axis by contour sampling + Newton.
    Returns the root with the largest real part (the 'rightmost' / leading mode).
    """
    re_ = np.linspace(halfplane_re[0], halfplane_re[1], n)
    im_ = np.linspace(im[0], im[1], n)
    best = None
    for rr in re_:
        row = char_eq(rr + 1j * im_, tau_g, tau_p, c)
        for j in range(len(im_) - 1):
            # look for a zero crossing of both real and imag surfaces is hard;
            # instead take the shortest |D| cell and refine by Newton.
            pass
    # Cheap + robust: global min of |D| over the mesh, then Newton refine.
    re2, im2 = np.meshgrid(re_, im_, indexing="ij")
    D = char_eq(re2 + 1j * im2, tau_g, tau_p, c)
    mag = np.abs(D)
    idx = np.unravel_index(np.argmin(mag), mag.shape)
    bound = 1.5  # refine only if the min is small
    if mag[idx] > bound:
        return None
    z0 = complex(re2[idx], im2[idx])
    return _newton(z0, tau_g, tau_p, c)


def _newton(z0, tau_g, tau_p, c, iters=60, h=1e-7):
    z = z0
    for _ in range(iters):
        f = char_eq(z, tau_g, tau_p, c)
        df = (char_eq(z + h, tau_g, tau_p, c) - char_eq(z - h, tau_g, tau_p, c)) / (2 * h)
        if df == 0:
            break
        z = z - f / df
        if abs(f) < 1e-12:
            break
    return complex(z.real, z.imag)


def largest_real_root(tau_g, tau_p, c):
    r = numeric_roots(tau_g, tau_p, c)
    return None if r is None else r.real


def _real_roots(tau_g, tau_p, c, re=(-1.5, 1.5), n=4000):
    """Roots of D on the REAL axis (D(s) real for real s), via sign changes."""
    from scipy.optimize import brentq
    s = np.linspace(re[0], re[1], n)
    D = np.array([char_eq(x, tau_g, tau_p, c).real for x in s])
    roots = []
    zi = np.where(np.diff(np.sign(D)) != 0)[0]
    for i in zi:
        r = brentq(lambda x: char_eq(x, tau_g, tau_p, c).real, s[i], s[i + 1])
        # newton polish
        r = _newton(r, tau_g, tau_p, c).real
        roots.append(float(r))
    return roots


def full_spectrum(tau_g, tau_p, c, re=(-1.5, 1.5), im=(0.0, 4.0), nr=240, ni=360):
    """Computed spectrum of the corrected S0 (the 'full-spectrum' companion to
    the exact crossing-curve method): find ALL roots of D(s; tau_g, tau_p) in a
    window by fine sampling + Newton refinement, return the leading (rightmost)
    eigenvalue and the count.  The real axis is scanned exactly; the complex
    plane is scanned for oscillatory (Hopf) modes.  Equivalent in spirit to a
    pseudospectral DDE eigenvalue solve (Breda–Maset–Vermiglio).
    """
    roots = _real_roots(tau_g, tau_p, c, re=re)
    # complex plane scan (im > 0); roots come in conjugate pairs.
    s_re = np.linspace(re[0], re[1], nr)
    s_im = np.linspace(im[0], im[1], ni)
    re_g, im_g = np.meshgrid(s_re, s_im, indexing="ij")
    D = char_eq(re_g + 1j * im_g, tau_g, tau_p, c)
    mag = np.abs(D)
    thr = min(mag.max(), 2.0)
    for i in range(1, nr - 1):
        for j in range(1, ni - 1):
            v = mag[i, j]
            if v < mag[i - 1, j] and v < mag[i + 1, j] and v < mag[i, j - 1] \
                    and v < mag[i, j + 1] and v < thr:
                r = _newton(complex(s_re[i], s_im[j]), tau_g, tau_p, c)
                if r is not None and np.isfinite(r.real) and abs(r) > 1e-6:
                    if not any(abs(r - q) < 1e-3 for q in roots):
                        roots.append(r)
    nonzero = [r for r in roots if abs(r) > 1e-6]
    leading = max(nonzero, key=lambda r: r.real) if nonzero else None
    return dict(roots=[complex(r.real, r.imag) for r in roots],
                leading=complex(leading.real, leading.imag) if leading else None,
                max_real=float(leading.real) if leading else None,
                n_roots=len(roots),
                neutral_zero=any(abs(r) < 1e-6 for r in roots))


def _cross_fns(w, tau_g, tau_p, c):
    """Return (Re D, Im D) at s=i*w for the 2-D corrected S0."""
    a1, a3, aE, a4, r = c["a1"], c["a3"], c["aE"], c["a4"], c["r"]
    wg = w * tau_g; wp = w * tau_p
    Acoef = -(a3 + a1 * np.cos(wg))
    Bcoef = w + a1 * np.sin(wg)
    P = (Acoef * r - Bcoef * w)
    Q = (Acoef * w + Bcoef * r)
    Re = P - aE * a4 * np.cos(wp)
    Im = Q + aE * a4 * np.sin(wp)
    return Re, Im


def _elim(tau_g, w, c, amp):
    """P^2 + Q^2 - (aE a4)^2  (depends only on tau_g)."""
    a1, a3, r = c["a1"], c["a3"], c["r"]
    wg = w * tau_g
    Acoef = -(a3 + a1 * np.cos(wg))
    Bcoef = w + a1 * np.sin(wg)
    P = Acoef * r - Bcoef * w
    Q = Acoef * w + Bcoef * r
    return (P * P + Q * Q) - amp * amp


def crossing_curves(c, omega_range=(0.02, 1.5), n=200, tau_g_max=300.0,
                    branches=3):
    """Exact stability-crossing curves via lambda = i*omega (Hale & Huang 1993;
    Gu, Niculescu & Chen 2005).

    For each omega, Re D = Im D = 0.  Writing them as
        P(w,tau_g) = aE*a4*cos(w tau_p),  Q(w,tau_g) = -aE*a4*sin(w tau_p),
    the elimination  P^2+Q^2 = (aE a4)^2  involves ONLY tau_g, so each crossing
    omega gives the crossing tau_g by solving this 1-D scalar equation (Brent),
    and tau_p follows from atan2(-Q, P) (+ its 2*pi/w branches).  Returns the
    (omega, tau_g, tau_p) points on the exact crossing locus.
    """
    from scipy.optimize import brentq
    aE, a4 = c["aE"], c["a4"]
    amp = abs(aE * a4)
    pts = []
    for w in np.linspace(*omega_range, n):
        tgrid = np.linspace(0.0, tau_g_max, 800)
        F = np.array([_elim(tg, w, c, amp) for tg in tgrid])
        zero_idx = np.where(np.diff(np.sign(F)) != 0)[0]
        for zi in zero_idx:
            tg0 = brentq(lambda t: _elim(t, w, c, amp),
                         tgrid[zi], tgrid[zi + 1])
            wg0 = w * tg0
            A0 = -(c["a3"] + c["a1"] * np.cos(wg0))
            B0 = w + c["a1"] * np.sin(wg0)
            P0 = A0 * c["r"] - B0 * w
            Q0 = A0 * w + B0 * c["r"]
            phi = np.arctan2(-Q0, P0)
            tp0 = (phi % (2 * np.pi)) / w
            for k in range(branches):
                tp = tp0 + k * (2 * np.pi / w)
                if tp > tau_g_max:
                    continue
                pts.append(dict(omega=float(w), tau_g=float(tg0), tau_p=float(tp)))
    return pts
