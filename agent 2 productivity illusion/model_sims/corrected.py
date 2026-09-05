"""Corrected-model (unified stock-flow 1''' ) simulators and basin recompute (R1).

The corrected constant-parameter subsystem (S0) is structurally DIFFERENT from the
original gross-depletion model:

    dA/dt = G(A(t-tau_g)) - [E(t) - b A(t)]_+ / b_G ,
    dP/dt = r P(t) [1 - P(t) / K(t-tau_p)] ,      K(t) = B(t)/e ,
    B(t)  = b A(t) + b_G G(A(t)) ,                G(A) = rho A (1 - A/A_max) ,
    E(t)  = e P(t) ,   sigma = 1 (no reservation/half-earth in S0) .

Its "sustainable" state is a ONE-SIDED boundary at A -> A_max, P -> b A_max / e
(the flow-only / orchard limit, where E = B = bA).  There is NO robust interior
attractor: any population overshoot into E > bA triggers the vicious-cycle
collapse A -> A_ext.  So the natural basin question (R1) is:

    for each initial condition (A0, P0), does the corrected S0 RECOVER
    (A -> A_max) or COLLAPSE (A -> A_ext)?

This module computes that basin, reports the recover fraction as a function of
(tau_g, tau_p) (the analogue of the original model's 12G.2 0.506 -> 0.042), and
locates the separatrix / analytic boundary.
"""
import numpy as np

from .models import ramp


def _G(A, rho, Amax):
    return rho * np.asarray(A, float) * (1 - np.asarray(A, float) / Amax)


def _B(A, b, bG, rho, Amax):
    return b * np.asarray(A, float) + bG * _G(A, rho, Amax)


def corrected_s0(endpoint="final", rho=0.05, Amax=1.2, b0=0.5, bG=0.8, e=0.55,
                 r=0.02, Aext=0.02, Afloor=0.05, tg=30.0, tp=25.0, dt=0.2, T=2000.0,
                 A0=1.0, P0=0.1, sigma=1.0, w=0.02, ramp_soft=False):
    """Integrate the corrected S0 with a method-of-steps + RK4 scheme.

    Returns dict with endpoints, min A over the run, and a class:
      'R' recover  -> A_end near Amax (one-sided sustainable boundary)
      'C' collapse -> A_end near Aext (vicious-cycle liquidation)
      'O' other    -> neither (should be rare / a boundary point)
    """
    n = int(T / dt)
    idx0 = int(max(tg, tp) / dt) + 10
    A = np.full(idx0 + n + 1, A0)
    P = np.full(idx0 + n + 1, P0)

    def hist(v, t, delay):
        xf = (t - delay) / dt + idx0
        j = int(np.floor(xf)); fr = xf - j
        j0 = max(0, min(len(v) - 1, j)); j1 = max(0, min(len(v) - 1, j + 1))
        return v[j0] * (1 - fr) + v[j1] * fr

    for k in range(n):
        i = idx0 + k
        t = k * dt
        At = A[i]; Pt = P[i]
        Ag = hist(A, t, tg) if tg > 0 else At
        Kp = hist(A, t, tp) if tp > 0 else At
        # K at (t - tau_p) is a function of A(t-tau_p) (b constant in S0)
        K_del = _B(Kp, b0, bG, rho, Amax) / e

        # Delayed quantities are held constant across the RK4 step (method-of-steps).
        Gdel = _G(Ag, rho, Amax)                    # regeneration at A(t - tau_g)
        Kd = max(_B(Kp, b0, bG, rho, Amax) / e, 1e-6)   # carrying capacity at t - tau_p

        def der(aa, pp):
            def dA(x, q):
                surplus = sigma * b0 * np.asarray(x, float)
                dep = (e * q - surplus)
                d = ramp(dep, w) if ramp_soft else np.maximum(dep, 0.0)
                return Gdel - d / bG     # NB: regeneration is the DELAYED value
            def dP(x, q):
                # P(t) * (1 - P(t)/K(t-tau_p)); K is a function of A(t-tau_p) (=Kp)
                return r * q * (1 - q / Kd)
            return dA(aa, pp), dP(aa, pp)

        k1 = der(At, Pt)
        k2 = der(At + dt / 2 * k1[0], Pt + dt / 2 * k1[1])
        k3 = der(At + dt / 2 * k2[0], Pt + dt / 2 * k2[1])
        k4 = der(At + dt * k3[0], Pt + dt * k3[1])
        A[i + 1] = max(At + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), Aext)
        P[i + 1] = max(Pt + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]), 0.0)

    Aend = A[-1]; Pend = P[-1]
    Amin = float(A[idx0:].min())
    # classification relative to the one-sided boundary
    if Aend >= 0.95 * Amax:
        cls = "R"
    elif Aend <= Afloor:
        cls = "C"
    else:
        cls = "O"
    return dict(Aend=float(Aend), Pend=float(Pend), Amin=Amin, cls=cls,
                Aext=Aext, Amax=Amax)


def corrected_basin_fraction(tg, tp, gridA=None, gridP=None, **kw):
    """Recover fraction of the (A0, P0) plane for the corrected S0.

    `gridA`/`gridP` default to a mesh straddling the flow-only boundary
    A -> Amax, P -> b Amax / e.  Returns {frac_recover, frac_collapse,
    frac_other, total, boundary_P(a)}.
    """
    rho = kw.get("rho", 0.05); Amax = kw.get("Amax", 1.2); b0 = kw.get("b0", 0.5)
    bG = kw.get("bG", 0.8); e = kw.get("e", 0.55); r = kw.get("r", 0.02)
    Aext = kw.get("Aext", 0.02)
    dt = kw.get("dt", 0.2); T = kw.get("T", 2000.0)
    if gridA is None:
        gridA = np.arange(0.10, 1.21, 0.05)
    if gridP is None:
        gridP = np.arange(0.05, max(1.4, b0 * Amax / e + 0.3) + 1e-9, 0.05)
    tot = len(gridA) * len(gridP)
    rec = 0; col = 0; oth = 0
    for A0 in gridA:
        for P0 in gridP:
            res = corrected_s0(tg=tg, tp=tp, A0=float(A0), P0=float(P0),
                               rho=rho, Amax=Amax, b0=b0, bG=bG, e=e, r=r,
                               Aext=Aext, dt=dt, T=T)
            if res["cls"] == "R":
                rec += 1
            elif res["cls"] == "C":
                col += 1
            else:
                oth += 1
    return dict(frac_recover=rec / tot if tot else 0.0,
                frac_collapse=col / tot if tot else 0.0,
                frac_other=oth / tot if tot else 0.0,
                total=tot, tg=tg, tp=tp,
                P_sustainable=b0 * Amax / e)


def separatrix_crit(E, rho, Amax, b0, bG):
    """Closed-form fixed-liability threshold A_c(E) and E_sn (master 12G.2 / 4.2)."""
    rad = (bG * rho + b0) ** 2 - 4 * bG * rho * E / Amax
    if rad < 0:
        return None
    Ac = ((bG * rho + b0) - np.sqrt(rad)) * Amax / (2 * bG * rho)
    Esn = Amax * (b0 + bG * rho) ** 2 / (4 * bG * rho)
    return dict(Ac=float(Ac), E_sn=float(Esn))


def basin_map(tg, tp, gridA=None, gridP=None, **kw):
    """Full recover/collapse grid for the corrected S0 -> ('R'/'C'/'O') per cell,
    plus per-cell data.  Used to render the R1 basin figure and report fractions."""
    rho = kw.get("rho", 0.05); Amax = kw.get("Amax", 1.2); b0 = kw.get("b0", 0.5)
    bG = kw.get("bG", 0.8); e = kw.get("e", 0.55); r = kw.get("r", 0.02)
    Aext = kw.get("Aext", 0.02); dt = kw.get("dt", 0.5); T = kw.get("T", 1000.0)
    if gridA is None:
        gridA = np.round(np.arange(0.14, 1.201, 0.06), 3)
    if gridP is None:
        gridP = np.round(np.arange(0.05, 1.501, 0.06), 3)
    rec = col = oth = 0
    cells = []
    for A0 in gridA:
        row = []
        for P0 in gridP:
            res = corrected_s0(tg=tg, tp=tp, A0=float(A0), P0=float(P0),
                               rho=rho, Amax=Amax, b0=b0, bG=bG, e=e, r=r,
                               Aext=Aext, dt=dt, T=T)
            row.append(res["cls"])
            if res["cls"] == "R":
                rec += 1
            elif res["cls"] == "C":
                col += 1
            else:
                oth += 1
        cells.append(row)
    return dict(gridA=list(map(float, gridA)), gridP=list(map(float, gridP)),
                cells=cells, frac_recover=rec / len(gridA) / len(gridP),
                frac_collapse=col / len(gridA) / len(gridP),
                frac_other=oth / len(gridA) / len(gridP),
                nA=len(gridA), nP=len(gridP), total=len(gridA) * len(gridP),
                tg=tg, tp=tp, P_sustainable=b0 * Amax / e)
