"""Top-down analysis of the corrected S0, aligned to the corrected model.

This is the completed, reproducible home for the corrected top-down framework
it supersedes the AI's draft `top-down ecol.txt`.  It depends only on the
committed `model_sims/corrected.py` (simulator) and `model_sims/char_eq.py`
(linearisation / crossing curves).

Model (corrected S0, deficit region E>bA), baseline:
    rho=0.05, A_max=1.2, b=0.5, b_G=0.8, e=0.55, r=0.02, A_ext=0.02
    G(A)=rho A (1 - A/A_max),  B = bA + b_G G(A),  K = B/e,
    R_B = E/B (standard GFN overshoot),  R_A = E/(bA) (footprint / flow yield),
    psi = bA/B (flow share).

Sections
--------
A1  delay_boundary / tau_g-driven cliff (no dimensionless tau_g/tau_p ratio)
A2  neutral_direction + neutral_separator (R_B=1 family) + balanced accuracy
A3  recovery overshoot scaling (IC-dependent, steep)
A5  crossing-curve / monotone-only confirmation
A7  macro ratios, flow-share closed form, silent-collapse quantification
"""
import numpy as np

from .corrected import _G, _B, corrected_s0
from .r1_basin import DEFAULT_GRID, _params as _basin_params

# ---------------------------------------------------------------- baseline
RHO, AMAX, B0, BG, E, R = 0.05, 1.2, 0.5, 0.8, 0.55, 0.02
AEXT = 0.02

BASELINE = dict(rho=RHO, Amax=AMAX, b0=B0, bG=BG, e=E, r=R, Aext=AEXT)


def Gp(A):
    return RHO * (1 - 2 * np.asarray(A, float) / AMAX)


def equilibrium_family(A):
    """One-parameter family of S0 equilibria P = B(A)/e  (== R_B = 1 locus)."""
    return _B(np.asarray(A, float), B0, BG, RHO, AMAX) / E


# ------------------------------------------------------------- A7: ratios
def ratios(A0v, P0v):
    """R_B = E/B, R_A = E/(b0 A).  R_A = R_B / psi."""
    BF = _B(A0v, B0, BG, RHO, AMAX)
    bA = B0 * A0v
    return (E * P0v) / BF, (E * P0v) / max(bA, 1e-9)


def flow_share(A0v):
    bA = B0 * A0v
    return bA / _B(A0v, B0, BG, RHO, AMAX)


def neutral_separator(A0v, P0v):
    """Predict by the neutral family (R_B = 1): below -> recover, above -> collapse."""
    RB, RA = ratios(A0v, P0v)
    return ("R" if RB < 1.0 else "C"), RB, RA


def RAeq_from_regime(index):
    """Closed form at the interior MSY: R_A^eq = (1 + b_G rho/b)/2 (index<=1 -> 1)."""
    return 1.0 if index <= 1.0 else (1.0 + index) / 2.0


# ----------------------------------------------------------- A2: neutral
def linearised_matrices(Astar):
    """A0, Ag, Ap for the corrected S0 about (A*, P*=K(A*)).  Correct objects."""
    a1 = Gp(Astar)                                  # regeneration, DELAYED tau_g
    a3 = B0 / BG                                    # depletion, current (+A)
    aE = -E / BG                                    # depletion -> P, current
    a4 = R * (B0 + BG * Gp(Astar)) / E              # K -> P, DELAYED tau_p
    A0 = np.array([[a3, aE], [0.0, -R]])
    Ag = np.array([[a1, 0.0], [0.0, 0.0]])
    Ap = np.array([[0.0, 0.0], [a4, 0.0]])
    return A0, Ag, Ap


def neutral_direction(Astar):
    """(left_null, right_null, singular_values) of J = A0+Ag+Ap.
    The adjoint (separator) needs the LEFT null vector = U[:,-1] (the AI used the
    RIGHT null vector Vh[-1] -- a bug).  D(0)=0 <=> a zero singular value."""
    A0, Ag, Ap = linearised_matrices(Astar)
    J = A0 + Ag + Ap
    U, s, Vh = np.linalg.svd(J)
    return U[:, -1], Vh[-1, :], s


def balanced_metrics(counts):
    """From a 2x2 confusion matrix [[tp,fn],[fp,tn]] return (raw, sens, spec, balanced)."""
    tp, fn, fp, tn = (int(counts[k]) for k in ("tp", "fn", "fp", "tn"))
    acc = (tp + tn) / max(tp + tn + fp + fn, 1)
    sen = tp / max(tp + fn, 1)
    spec = tn / max(tn + fp, 1)
    return acc, sen, spec, 0.5 * (sen + spec)


def separator_accuracy(tg, tp, mode="neutral", **kw):
    """Raw + balanced accuracy of the neutral-family (or linear/) separator on the
    basin grid.  mode='neutral' uses R_B<1; mode='linear' fits a linear functional."""
    gridA = kw.get("gridA", DEFAULT_GRID["gridA"])
    gridP = kw.get("gridP", DEFAULT_GRID["gridP"])
    A, P, lab = [], [], []
    for a0 in gridA:
        for p0 in gridP:
            c = corrected_s0(tg=tg, tp=tp, A0=float(a0), P0=float(p0),
                             dt=kw.get("dt", 0.5), T=kw.get("T", 1200.0), **BASELINE)["cls"]
            if c == "O":
                continue
            A.append(a0); P.append(p0); lab.append(1 if c == "R" else 0)
    A = np.array(A); P = np.array(P); lab = np.array(lab)
    if mode == "neutral":
        pred = (equilibrium_family(A) > P).astype(int)     # below family -> recover
    else:
        X = np.column_stack([np.ones_like(A), A, P])
        w, *_ = np.linalg.lstsq(X, lab, rcond=None)
        pred = (X @ w > 0.5).astype(int)
    tpv = int(((pred == 1) & (lab == 1)).sum()); fn = int(((pred == 0) & (lab == 1)).sum())
    fp = int(((pred == 1) & (lab == 0)).sum()); tn = int(((pred == 0) & (lab == 0)).sum())
    acc, sen, spec, bal = balanced_metrics(dict(tp=tpv, fn=fn, fp=fp, tn=tn))
    return dict(tg=tg, tp=tp, mode=mode, n_recover=int((lab == 1).sum()),
                n_collapse=int((lab == 0).sum()), raw=acc, sens=sen, spec=spec, balanced=bal)


# ------------------------------------------------------------- A1: cliff
def delay_boundary(tg_list, tp_list, A0=1.0, P0=0.9, **kw):
    """Outcome ('R'/'C') grid + the last-recover tau_g per tau_p (the cliff)."""
    out = {}
    lastR = {}
    for tp in tp_list:
        last = None
        for tg in tg_list:
            c = corrected_s0(tg=float(tg), tp=float(tp), A0=A0, P0=P0,
                             dt=kw.get("dt", 0.25), T=kw.get("T", 1500.0), **BASELINE)["cls"]
            out[(tg, tp)] = c
            if c == "R":
                last = tg
        lastR[tp] = last
    return out, lastR


# ------------------------------------------------------------- A3: overshoot
def recovery_overshoot(tg, A0=0.20, P0=0.10, tp=25.0, T=4000.0, dt=0.2):
    """Peak stock A_peak on a recovering trajectory; returns A_peak and overshoot."""
    n = int(T / dt); idx0 = int(max(tg, tp) / dt) + 10
    A = np.full(idx0 + n + 1, A0); P = np.full(idx0 + n + 1, P0)

    def hist(v, t, d):
        xf = (t - d) / dt + idx0; j = int(np.floor(xf)); fr = xf - j
        j0 = max(0, min(len(v) - 1, j)); j1 = max(0, min(len(v) - 1, j + 1))
        return v[j0] * (1 - fr) + v[j1] * fr

    for k in range(n):
        i = idx0 + k; t = k * dt; At = A[i]; Pt = P[i]
        Ag = hist(A, t, tg) if tg > 0 else At
        Kp = hist(A, t, tp) if tp > 0 else At
        Kd = max(_B(Kp, B0, BG, RHO, AMAX) / E, 1e-6)
        Gdel = _G(Ag, RHO, AMAX)

        def der(aa, qq):
            dep = E * qq - B0 * aa
            return Gdel - max(dep, 0.0) / BG, R * qq * (1 - qq / Kd)

        k1 = der(At, Pt); k2 = der(At + dt / 2 * k1[0], Pt + dt / 2 * k1[1])
        k3 = der(At + dt / 2 * k2[0], Pt + dt / 2 * k2[1]); k4 = der(At + dt * k3[0], Pt + dt * k3[1])
        A[i + 1] = max(At + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), AEXT)
        P[i + 1] = max(Pt + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]), 0.0)
    return float(A[idx0:].max())


# ------------------------------------------------------------- A5: Hopf
def no_crossing_confirmation(Astar=1.0, omega_range=(0.02, 1.5), n=300,
                             tau_g_max=100.0, branches=4):
    """Number of imaginary-axis crossing points over the whole (tau_g, tau_p) plane.
    0 => monotone-only (no Hopf), confirming R2."""
    from .char_eq import lin_coeffs, crossing_curves
    c = lin_coeffs(Astar)
    pts = crossing_curves(c, omega_range=omega_range, n=n, tau_g_max=tau_g_max,
                          branches=branches)
    return len(pts)


# ------------------------------------------------------------- C4: rescue set
def rescue_set(tg, tp=25.0, gridA=None, gridP=None, **kw):
    """Fraction of the IC box that recovers (the 'rescue set'), plus the set's
    extent along the A direction.  As tau_g grows this -> a measure-zero strip at
    A=A_max (domain-wide collapse): the C4 premise, stated as a measurable quantity."""
    gridA = DEFAULT_GRID["gridA"] if gridA is None else gridA
    gridP = DEFAULT_GRID["gridP"] if gridP is None else gridP
    rec = col = 0
    rec_A = []
    for a0 in gridA:
        for p0 in gridP:
            c = corrected_s0(tg=tg, tp=tp, A0=float(a0), P0=float(p0),
                             dt=kw.get("dt", 0.5), T=kw.get("T", 1200.0), **BASELINE)["cls"]
            if c == "R":
                rec += 1; rec_A.append(float(a0))
            elif c == "C":
                col += 1
    tot = rec + col
    return dict(tg=tg, tp=tp, recover=rec, collapse=col, total=tot,
                frac_recover=rec / tot if tot else 0.0,
                rescue_A_min=min(rec_A) if rec_A else None,
                rescue_A_max=max(rec_A) if rec_A else None,
                rescue_A_span=len(set(round(x, 3) for x in rec_A)))


# ------------------------------------------------------------- C6: discrete map
def method_of_steps(A_prev, A_cur, E, tg):
    """One method-of-steps map step sampled at the regeneration-lag period:
        A_{k+1} = A_k + tg [ G(A_{k-1}) - (E - b A_k)_+ / b_G ].
    Fixed points (map) satisfy b A + b_G G(A) = E  ==  the equilibrium family."""
    Gdel = _G(A_prev, RHO, AMAX)
    dep = max(E - B0 * A_cur, 0.0)
    return A_cur + tg * (Gdel - dep / BG)


def map_fixed_points(E, tg=5.0, n=2001):
    """Fixed points of the method-of-steps map inside [A_ext, A_max].
    These coincide with the equilibrium-family roots (bA + b_G G(A) = E)."""
    from scipy.optimize import brentq
    a0 = np.asarray(np.linspace(AEXT, AMAX, n), float)

    def H(Av):
        return _G(Av, RHO, AMAX) - ((E - B0 * Av) / BG if E > B0 * Av else 0.0)

    F = np.array([H(a) for a in a0])
    roots = []
    for i in np.where(np.diff(np.sign(F)) != 0)[0]:
        try:
            roots.append(float(brentq(H, a0[i], a0[i + 1])))
        except Exception:
            pass
    return roots


def map_local_stability(tg_list, tp=25.0, Astar=1.0):
    """Leading Re(lambda) of the map/DDE linearisation vs tau_g (constant +0.62).
    The map fixed points are the family, but the local stability does NOT flip at
    tau_g~19 -> the cliff is a NONLOCAL basin-boundary crisis, not a map bifurcation."""
    from .char_eq import lin_coeffs, largest_real_root
    c = lin_coeffs(Astar)
    return [dict(tau_g=int(tg), Re_lambda_max=float(largest_real_root(tg, tp, c))) for tg in tg_list]

