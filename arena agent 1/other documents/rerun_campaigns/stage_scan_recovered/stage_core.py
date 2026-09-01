#!/usr/bin/env python3
"""Local Hopfs of the stage-structured harvest core (adult vs juvenile take)."""
from __future__ import annotations

import json
import math

import numpy as np

OUT = "/home/user/figures"


def eq_and_lin(params, harvest="adult"):
    """States (XA, XJ, Z, E). A frozen, s=A/(A+A0).
    adult:  C = q E XA from adults
    juvenile: C = q E XJ from juveniles (true egg/recruit harvest)
    Birth: B = P0 XA exp(-XA/Nc) * s
    """
    P0, Nc, g, dA, dJ, q, s = (
        params[k] for k in ("P0", "Nc", "g", "dA", "dJ", "q", "s")
    )
    eta, Emax, d0, Dref, Zref, taum, delta, ksoft = (
        params[k] for k in ("eta", "Emax", "d0", "Dref", "Zref", "taum", "delta", "k")
    )
    # effort eq same quadratic as paper I at Z=delta
    a = -eta / Emax
    b = eta * (delta / Dref)
    c = d0 * delta / (Zref + delta)
    rts = np.roots([a, b, c])
    Es = float([np.real(z) for z in rts if abs(np.imag(z)) < 1e-12 and np.real(z) > 0][0])
    # mass eq
    # XA: XJ/g - dA XA - 1_{ad} q E XA = 0 => XJ = g XA (dA + 1_ad q E)
    # XJ: B - XJ/g - dJ XJ - 1_juv q E XJ = 0
    # B = P0 XA e^{-XA/Nc} s
    # => P0 e^{-XA/Nc} s = (dA+1_ad qE)(1 + g(dJ+1_juv qE))
    # wait: XJ/g = XA (dA + ψ_ad q E)
    # B = XJ (1/g + dJ + ψ_j q E) = XA (dA+ψ_ad qE) (1 + g(dJ+ψ_j qE))
    # so P0 e^{-XA/Nc} s = (dA+ψ_ad qE)(1 + g(dJ+ψ_j qE)) =: Theta
    if harvest == "adult":
        Theta = (dA + q * Es) * (1.0 + g * dJ)
    elif harvest == "juvenile":
        Theta = dA * (1.0 + g * (dJ + q * Es))
    else:
        raise ValueError(harvest)
    if P0 * s <= Theta:
        return None
    XA = Nc * math.log(P0 * s / Theta)
    if harvest == "adult":
        XJ = g * XA * (dA + q * Es)
    else:
        XJ = g * XA * dA
    Zs = delta
    return dict(XA=XA, XJ=XJ, Z=Zs, E=Es, Theta=Theta, harvest=harvest)


def rhs(state, Zd, p, harvest):
    XA, XJ, Z, E = state
    P0, Nc, g, dA, dJ, q, s = (p[k] for k in ("P0", "Nc", "g", "dA", "dJ", "q", "s"))
    eta, Emax, d0, Dref, Zref, taum, delta, ksoft = (
        p[k] for k in ("eta", "Emax", "d0", "Dref", "Zref", "taum", "delta", "k")
    )
    B = P0 * XA * math.exp(-XA / Nc) * s
    if B < 0:
        B = 0.0
    if harvest == "adult":
        dXA = XJ / g - dA * XA - q * E * XA
        dXJ = B - XJ / g - dJ * XJ
        deficit = q * E * XA - (XJ / g - dA * XA)  # extraction minus net adult increment w/o harvest?
        # institutional signal: decline of adults or harvest-over-recruitment
        # use -dXA without the identity; paper I uses qEN-S.
        # Adult net recruitment to XA is XJ/g - dA XA; harvest q E XA
        S_ad = XJ / g - dA * XA
        phi = q * E * XA - S_ad  # = -dXA
    else:
        dXA = XJ / g - dA * XA
        dXJ = B - XJ / g - dJ * XJ - q * E * XJ
        # deficit: juvenile harvest vs birth surplus available
        S_j = B - XJ / g - dJ * XJ
        phi = q * E * XJ - S_j  # = -dXJ
    # filter
    kphi = ksoft * phi
    if kphi > 40:
        sp = phi
    elif kphi < -40:
        sp = math.exp(kphi) / ksoft
    else:
        sp = math.log1p(math.exp(kphi)) / ksoft
    filt = sp - math.log(2.0) / ksoft + delta
    if filt < 0:
        filt = 0.0
    dZ = (filt - Z) / taum
    h = eta * E * (Zd / Dref - E / Emax) + d0 * Zd / (Zref + Zd)
    gate = 1.0 - E / Emax
    if gate < 0:
        gate = 0.0
    dE = gate * h
    return np.array([dXA, dXJ, dZ, dE], float)


def jac(eq, p, harvest, eps=1e-7):
    x = np.array([eq["XA"], eq["XJ"], eq["Z"], eq["E"]], float)
    Zd = eq["Z"]
    A0 = np.zeros((4, 4))
    f0 = rhs(x, Zd, p, harvest)
    for j in range(4):
        xp = x.copy()
        xp[j] += eps
        A0[:, j] = (rhs(xp, Zd, p, harvest) - f0) / eps
    At = np.zeros((4, 4))
    At[:, 2] = (rhs(x, Zd + eps, p, harvest) - f0) / eps
    return A0, At


def hopfs(A0, At, taumax=400.0):
    found = []
    for om in np.linspace(0.005, 0.2, 800):
        M1 = 1j * om * np.eye(4) - A0
        try:
            w = np.linalg.eigvals(np.linalg.solve(M1, At))
        except np.linalg.LinAlgError:
            continue
        for lam in w:
            if abs(abs(lam) - 1.0) < 0.02:
                ang = np.angle(lam)  # ω τ if μ = e^{iωτ} is eig of M1^{-1} At
                # check convention: M1 v = At v e^{-iωτ} => M1^{-1} At v = e^{iωτ} v
                for k in range(0, 8):
                    tau = (ang + 2 * np.pi * k) / om
                    if 0.2 < tau < taumax:
                        found.append((abs(abs(lam) - 1), float(tau), float(om)))
    found.sort()
    uniq = []
    for e, tau, om in found:
        if not uniq or min(abs(tau - u[1]) for u in uniq) > 0.5:
            uniq.append((e, tau, om))
    # refine by det
    from scipy.optimize import fsolve

    refined = []
    for _, tau, om in uniq[:20]:
        def obj(v):
            om_, tau_ = v
            D = 1j * om_ * np.eye(4) - A0 - At * np.exp(-1j * om_ * tau_)
            det = np.linalg.det(D)
            return [det.real, det.imag]

        sol = fsolve(obj, [om, tau], xtol=1e-12)
        omr, taur = sol
        D = 1j * omr * np.eye(4) - A0 - At * np.exp(-1j * omr * taur)
        sv = np.linalg.svd(D, compute_uv=False)[-1]
        if sv < 1e-8 and 0.2 < taur < taumax and omr > 0:
            rec = (float(taur), float(omr), float(2 * np.pi / omr), float(sv))
            if all(abs(rec[0] - r[0]) > 0.2 for r in refined):
                refined.append(rec)
    refined.sort()
    return refined


def main():
    base = dict(
        P0=1.2,
        Nc=50.0,
        g=5.0,  # cod-class
        dA=0.15,
        dJ=0.4,
        q=0.01,
        s=0.99,
        eta=0.914,
        Emax=30.0,
        d0=0.01,
        Dref=1.0,
        Zref=1.0,
        taum=5.0,
        delta=math.log(2) / 10,
        k=10.0,
    )
    out = {}
    for harvest in ("adult", "juvenile"):
        for label, extra in [
            ("default_eta", dict(eta=0.914, q=0.001, g=5.0)),
            ("elevated", dict(eta=5.0, q=0.01, g=5.0)),
            ("anchovy_elev", dict(eta=5.0, q=0.01, g=1.0, dA=0.4, dJ=0.8, P0=3.0)),
            ("sprat_elev", dict(eta=5.0, q=0.01, g=2.0, dA=0.25, dJ=0.5, P0=2.0)),
        ]:
            p = dict(base)
            p.update(extra)
            eq = eq_and_lin(p, harvest)
            rec = {"params": {k: p[k] for k in extra}, "eq": eq}
            if eq is None:
                rec["hopf"] = []
                rec["status"] = "no_eq"
            else:
                A0, At = jac(eq, p, harvest)
                rec["hopf"] = hopfs(A0, At)
                rec["status"] = "ok"
                rec["A0_eigs"] = [complex(z).__repr__() for z in np.linalg.eigvals(A0 + At)]
            out[f"{harvest}:{label}"] = rec
            print(harvest, label, rec["status"], rec.get("eq"), rec.get("hopf"))
    with open(OUT + "/stage_hopf.json", "w") as f:
        json.dump(out, f, indent=2, default=str)


if __name__ == "__main__":
    main()
