"""P5 stage-map reconstruction (turn 45) — pre-registered 2026-09-01.

Pre-registration: stage_reconstruction_preregistration.md (frozen before any run).
No parameter below was chosen with reference to the legacy windows; all are cited
literature values or the paper's own declared controller values. The record is a
NEW declared object, not the object that produced the legacy exploratory bands.

Plant (new declared object): two-stage delayed-recruitment Beverton-Holt map
    A_{t+1} = s_A A_t + s_J J_t - q E A_t
    J_{t+1} = f(A_{t-tau}),  f(A) = alpha*A/(1+beta*A)
    s_A = s_J = exp(-M);  c = 4h/(1-h);  beta = (c-1)/A0;  alpha = c(1-s_A)/s_J
    surplus S(A) = s_J f(A) - (1-s_A) A   (discrete analogue of the paper's S)

Controller (the paper's declared object, unchanged): P5 v4 Sec 2.1 eqs. (1)-(4)
in annual discrete form; softplus signal Phi_k with shift delta = ln2/10;
projected forward-Euler review with F_B; contemporaneous exact assessment.
Extractive channel: nonlinear law (primary). Protective channel: the paper's
declared quota-tracking gains CE_p, CZ_p applied in the linearized review map
(the same convention the paper's logistic protective record uses).

Records: (1) multiplier record M(T_r) = DP_{T_r}(X*) by central finite
differences of the annual map composed per the chain rule (cross-checked
against direct full-map FD), T_r in {1..50} yr; (2) trajectory classification
(2000 review-steps, tail 500, relative tail sd thresholds 2% / 0.1%);
(3) FFT dominant periods, effort/biomass excursions, 30% assessment-error
robustness; (4) one post-hoc comparison against the legacy windows with the
criteria fixed in the pre-registration.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
OUT = HERE / "results"
OUT.mkdir(exist_ok=True)

# ---------------- controller (paper values, unchanged from the logistic core) --
q_primary, q_sensitivity = 0.001, 0.1
eta, Emax, dref = 0.914, 30.0, 1.0
d0, tm, Zref = 0.01, 5.0, 1.0
delta = np.log(2) / 10.0
PHI_SLOPE_0 = 0.5  # softplus derivative at 0, independent of k

# ---------------- class parameter sets (frozen; sources in the pre-registration)
# M: anchovy Pauly & Tsukayama 1987; sprat Baltic SMS mid-range (IBPBASH 2022);
#    cod ICES 2021 fixed M; slow-stock Branch 2001 (orange roughy).
# tau (age at 50% maturity): anchovy 1 (Pauly & Tsukayama 1987); sprat 2
#    (ICES WGBFAS ogives); cod 5 (DFO 2011/037); slow-stock 25 (Branch 2001).
CLASSES = {
    "anchovy":   dict(M=0.90,  tau=1),
    "sprat":     dict(M=0.40,  tau=2),
    "cod":       dict(M=0.20,  tau=5),
    "slow_stock": dict(M=0.045, tau=25),
}
H = 0.75        # declared default steepness convention
H_SENS = (0.6, 0.9)
A0 = 100.0      # declared scale (matches the logistic core's K)


K_SOFT = 10.0  # the wave-7 comparator machinery's declared softplus sharpness


def softplus_k(s):
    # Phi_k(s) = max{0, (1/k)log(1+e^{ks}) - (log 2)/k + delta}; Phi_k(0) = delta
    return max(0.0, np.log(1 + np.exp(K_SOFT * s)) / K_SOFT
               - np.log(2) / K_SOFT + delta)


def build_class(M, tau, h=H):
    s = np.exp(-M)
    c = 4 * h / (1 - h)
    beta = (c - 1) / A0
    alpha = c * (1 - s) / s
    return dict(M=M, tau=tau, h=h, s=s, c=c, beta=beta, alpha=alpha)


def equilibrium(p, q):
    """Controller fixed point (plant-independent) and plant equilibrium."""
    a, b, c3 = -eta / Emax, eta * delta / dref, d0 * delta / (Zref + delta)
    E_star = (-b - np.sqrt(b * b - 4 * a * c3)) / (2 * a)
    s = p["s"]
    A_star = (s * p["alpha"] / (q * E_star + 1 - s) - 1) / p["beta"]
    J_star = p["alpha"] * A_star / (1 + p["beta"] * A_star)
    return E_star, A_star, J_star


def surplus(A, p):
    return p["s"] * p["alpha"] * A / (1 + p["beta"] * A) - (1 - p["s"]) * A


def effort_law(E, Z):
    return (1 - E / Emax) * (eta * E * (Z / dref - E / Emax)
                             + d0 * Z / (Zref + Z))


def annual_step(x, p, q, E_held):
    """One year of plant + signal with effort held. x = [A, J, mem(tau), Z]."""
    tau = p["tau"]
    A, J, Z = x[0], x[1], x[-1]
    mem = x[2:2 + tau]
    S = surplus(A, p)
    A_new = p["s"] * A + p["s"] * J - q * E_held * A
    J_new = p["alpha"] * mem[-1] / (1 + p["beta"] * mem[-1])
    Z_new = Z + (1 / tm) * (softplus_k(q * E_held * A - S) - Z)
    mem_new = np.concatenate(([A], mem[:-1]))
    return np.concatenate(([A_new, J_new], mem_new, [Z_new]))


def review_map(x, T, p, q, channel="extractive"):
    """One full review interval + command update. x = [A, J, mem(tau), Z, E]."""
    tau = p["tau"]
    xp = x.copy()
    for _ in range(int(T)):
        xp[:-1] = annual_step(xp[:-1], p, q, xp[-1])
    E, Z = xp[-1], xp[-2]
    if channel == "extractive":
        E_new = min(max(E + T * effort_law(E, Z), 0.0), Emax)
    else:  # protective: paper's declared quota-tracking gains (linearized review)
        gate = 1 - E / Emax
        CE_p, CZ_p = -gate * eta, gate * eta * (-(E * (Zref + delta) / Zref)
                                               * Zref / (Zref + delta) ** 2)
        E_new = min(max(E + T * (CE_p * E + CZ_p * Z), 0.0), Emax)
    xp[-1] = E_new
    return xp


def jacobian(x_star, T, p, q, channel="extractive"):
    """Central finite differences of the review map at the fixed point
    (chain rule on the annual map; cross-checked against direct full-map FD)."""
    n = len(x_star)
    h = 1e-6
    # annual-map Jacobian at the fixed point (E held) via FD on the T=1 map
    def one_year(xx):
        y = xx.copy()
        y[:-1] = annual_step(y[:-1], p, q, y[-1])
        return y

    J1 = np.zeros((n, n))
    for j in range(n):
        e = np.zeros(n)
        e[j] = h
        J1[:, j] = (one_year(x_star + e) - one_year(x_star - e)) / (2 * h)
    # T_r-fold composition
    JT = np.linalg.matrix_power(J1, int(T))
    # review step derivative (E update depends on E and Z)
    def rev(xx):
        return review_map(xx, T, p, q, channel)

    M = np.zeros((n, n))
    for j in range(n):
        e = np.zeros(n)
        e[j] = h
        M[:, j] = (rev(x_star + e) - rev(x_star - e)) / (2 * h)
    # cross-check: chain-rule product R_local @ JT, with R_local the LOCAL
    # derivative of the update step (E_new depends on the post-flow Z and E only)
    R = np.eye(n)
    if channel == "extractive":
        F_Bz = (effort_law(x_star[-1], x_star[-2] + h)
                - effort_law(x_star[-1], x_star[-2] - h)) / (2 * h)
        F_Be = (effort_law(x_star[-1] + h, x_star[-2])
                - effort_law(x_star[-1] - h, x_star[-2])) / (2 * h)
        R[-1, -2], R[-1, -1] = T * F_Bz, 1 + T * F_Be
    else:
        gate = 1 - x_star[-1] / Emax
        CE_p = -gate * eta
        CZ_p = gate * eta * (-(x_star[-1] * (Zref + delta) / Zref)
                             * Zref / (Zref + delta) ** 2)
        R[-1, -2], R[-1, -1] = T * CZ_p, 1 + T * CE_p
    return M, R @ JT


def trajectory(p, q, T, channel="extractive", steps=2000, tail=500,
               assess_error=0.0, seed=0):
    rng = np.random.default_rng(seed)
    tau = p["tau"]
    E_star, A_star, J_star = equilibrium(p, q)
    A, J = A0, p["alpha"] * A0 / (1 + p["beta"] * A0)
    mem = np.full(tau, A0)
    Z = delta
    E = 0.5 * E_star
    x = np.concatenate(([A, J], mem, [Z, E]))
    As, Es = [], []
    for _ in range(steps):
        xp = x.copy()
        for _ in range(int(T)):
            xp[:-1] = annual_step(xp[:-1], p, q, xp[-1])
        E, Z = xp[-1], xp[-2]
        if assess_error > 0:
            Z = (1 + assess_error * (2 * rng.random() - 1)) * Z  # +/-30%
        if channel == "extractive":
            xp[-1] = min(max(E + T * effort_law(E, Z), 0.0), Emax)
        else:
            gate = 1 - E / Emax
            CE_p, CZ_p = -gate * eta, gate * eta * (-(E * (Zref + delta) / Zref)
                                                   * Zref / (Zref + delta) ** 2)
            xp[-1] = min(max(E + T * (CE_p * E + CZ_p * Z), 0.0), Emax)
        x = xp
        As.append(x[0]); Es.append(x[-1])
    A_t, E_t = np.array(As[-tail:]), np.array(Es[-tail:])
    rel = A_t.std() / A_t.mean()
    kind = "persistent" if rel >= 0.02 else ("weak" if rel >= 0.001 else "converged")
    # FFT dominant periods (mean-removed tail)
    def dom_period(series):
        y = series - series.mean()
        spec = np.abs(np.fft.rfft(y))
        freqs = np.fft.rfftfreq(len(y), d=1.0)
        if len(spec) < 3 or spec[1:].max() < 1e-12:
            return None
        i = int(np.argmax(spec[1:])) + 1
        return float(1.0 / freqs[i])
    return dict(A_tail=A_t, E_tail=E_t, rel=rel, kind=kind,
                exc_A=float((A_t.max() - A_t.min()) / A_t.mean()),
                exc_E=float((E_t.max() - E_t.min()) / E_t.mean()),
                peak_A=dom_period(A_t), peak_E=dom_period(E_t))


def main():
    rows = []
    print("=== equilibrium sanity (E* plant-independent) ===")
    for cls, cdict in CLASSES.items():
        p = build_class(cdict["M"], cdict["tau"])
        E_star, A_star, J_star = equilibrium(p, q_primary)
        rows.append(dict(class_=cls, M=p["M"], tau=p["tau"], h=p["h"],
                         E_star=round(E_star, 4), A_star=round(A_star, 3)))
        print(f"  {cls:11} M={p['M']:.3f} tau={p['tau']:2d} "
              f"E*={E_star:.4f} A*={A_star:.2f}")
    pd.DataFrame(rows).to_csv(OUT / "p5_stage_equilibria.csv", index=False)

    # ---- multiplier record ----
    rec = []
    Ts = np.arange(1, 51)
    for cls, cdict in CLASSES.items():
        for q in (q_primary, q_sensitivity):
            p = build_class(cdict["M"], cdict["tau"])
            E_star, A_star, J_star = equilibrium(p, q)
            mem = np.full(p["tau"], A_star)
            x_star = np.concatenate(([A_star, J_star], mem, [delta, E_star]))
            for T in Ts:
                M_fd, M_chain = jacobian(x_star, T, p, q, "extractive")
                rho_fd = float(max(abs(np.linalg.eigvals(M_fd))))
                rho_chain = float(max(abs(np.linalg.eigvals(M_chain))))
                # tolerance 1e-4: FD errors amplify through the T_r-th matrix
                # power; the record uses the direct FD value (pre-registration)
                assert abs(rho_fd - rho_chain) < 1e-4, (cls, q, T, rho_fd, rho_chain)
                rec.append(dict(class_=cls, q=q, channel="extractive", T_r=int(T),
                                rho=round(rho_fd, 8)))
            for T in Ts:
                M_fd, _ = jacobian(x_star, T, p, q, "protective")
                rho_fd = float(max(abs(np.linalg.eigvals(M_fd))))
                rec.append(dict(class_=cls, q=q, channel="protective", T_r=int(T),
                                rho=round(rho_fd, 8)))
    rec = pd.DataFrame(rec)
    rec.to_csv(OUT / "p5_stage_multiplier_record.csv", index=False)
    print("\n=== multiplier record highlights (extractive, q=0.001) ===")
    for cls in CLASSES:
        sub = rec[(rec["class_"] == cls) & (rec.q == q_primary)
                  & (rec.channel == "extractive")]
        rho1 = sub[sub.T_r == 1].rho.iloc[0]
        i_max = sub.rho.idxmax()
        print(f"  {cls:11} rho(1)={rho1:.6f}  max rho={sub.rho.max():.6f} "
              f"at T_r={sub.loc[i_max,'T_r']}  "
              f"unstable Ts: {list(sub[sub.rho > 1].T_r)[:8]}")

    # ---- trajectory classification (extractive, q=0.001 primary) ----
    traj = []
    print("\n=== trajectory classification (extractive, q=0.001) ===")
    for cls, cdict in CLASSES.items():
        p = build_class(cdict["M"], cdict["tau"])
        for T in Ts:
            tr = trajectory(p, q_primary, T)
            traj.append(dict(class_=cls, q=q_primary, T_r=int(T), kind=tr["kind"],
                             rel_A=round(tr["rel"], 5),
                             exc_A=round(tr["exc_A"], 3), exc_E=round(tr["exc_E"], 3),
                             peak_A=tr["peak_A"], peak_E=tr["peak_E"]))
        line = [(t["T_r"], t["kind"][0]) for t in traj
                if t["class_"] == cls and t["T_r"] <= 20]
        print(f"  {cls:11} " + " ".join(f"{T}:{k}" for T, k in line))
    traj = pd.DataFrame(traj)
    traj.to_csv(OUT / "p5_stage_trajectories.csv", index=False)

    # ---- 30% assessment-error robustness at each class's window ----
    print("\n=== 30% multiplicative assessment-error robustness ===")
    windows = {"anchovy": (2, 3, 4), "sprat": (6, 8, 10, 12), "cod": (1, 5, 10, 20),
               "slow_stock": (5, 10, 20, 30, 40, 50)}
    rob = []
    for cls, Ts_w in windows.items():
        p = build_class(CLASSES[cls]["M"], CLASSES[cls]["tau"])
        for T in Ts_w:
            tr = trajectory(p, q_primary, T, assess_error=0.3)
            rob.append(dict(class_=cls, T_r=int(T), kind=tr["kind"],
                            rel_A=round(tr["rel"], 5)))
            print(f"  {cls:11} T={T:2d}: {tr['kind']:10} (rel {tr['rel']:.4f})")
    pd.DataFrame(rob).to_csv(OUT / "p5_stage_robustness30.csv", index=False)

    # ---- h sensitivity (declared layer) ----
    print("\n=== h sensitivity (extractive, q=0.001): rho max over grid ===")
    hsen = []
    for cls, cdict in CLASSES.items():
        for h in H_SENS:
            p = build_class(cdict["M"], cdict["tau"], h=h)
            E_star, A_star, J_star = equilibrium(p, q_primary)
            mem = np.full(p["tau"], A_star)
            x_star = np.concatenate(([A_star, J_star], mem, [delta, E_star]))
            rho_max, rho1 = 0.0, None
            for T in Ts:
                M_fd, _ = jacobian(x_star, T, p, q_primary, "extractive")
                r = float(max(abs(np.linalg.eigvals(M_fd))))
                rho_max = max(rho_max, r)
                if T == 1:
                    rho1 = r
            hsen.append(dict(class_=cls, h=h, rho_1=round(rho1, 6),
                             rho_max=round(rho_max, 6)))
            print(f"  {cls:11} h={h}: rho(1)={rho1:.6f} max={rho_max:.6f}")
    pd.DataFrame(hsen).to_csv(OUT / "p5_stage_h_sensitivity.csv", index=False)

    # ---- comparison against the legacy windows (pre-registered criteria) ----
    print("\n=== comparison vs legacy windows (criteria pre-registered) ===")
    comp = []
    def verdict(cls, cond, crit):
        v = "MATCH" if cond else "MISMATCH"
        comp.append(dict(class_=cls, criterion=crit, verdict=v))
        print(f"  {cls:11} {crit:52} {v}")

    t_anch = traj[(traj["class_"] == "anchovy")]
    verdict("anchovy", any(t_anch[(t_anch.T_r == T)].kind.iloc[0] == "persistent"
                           for T in (3, 4)), "persistent oscillation at T_r=3-4")
    verdict("anchovy", t_anch[t_anch.T_r == 2].rel_A.iloc[0]
            < min(t_anch[t_anch.T_r == 3].rel_A.iloc[0],
                  t_anch[t_anch.T_r == 4].rel_A.iloc[0]),
            "weak response at T_r=2 (below 3-4)")
    verdict("anchovy", t_anch[t_anch.T_r == 1].kind.iloc[0] == "converged",
            "annual-review convergence")
    t_spr = traj[traj["class_"] == "sprat"]
    verdict("sprat", any(t_spr[(t_spr.T_r >= 6) & (t_spr.T_r <= 12)].kind
                         == "persistent"), "persistent oscillation at T_r=6-12")
    t_cod = traj[traj["class_"] == "cod"]
    verdict("cod", all(t_cod[(t_cod.T_r >= 1) & (t_cod.T_r <= 20)].kind
                       == "converged"), "convergence for every T_r in [1,20]")
    t_sl = traj[traj["class_"] == "slow_stock"]
    osc_below = any(t_sl[(t_sl.T_r <= 20)].kind == "persistent")
    conv_above = all(t_sl[(t_sl.T_r >= 30) & (t_sl.T_r <= 50)].kind == "converged")
    verdict("slow_stock", osc_below and conv_above,
            "oscillation below 20-30, convergence 30-50")
    pd.DataFrame(comp).to_csv(OUT / "p5_stage_comparison.csv", index=False)
    print("\nsaved:", OUT)


if __name__ == "__main__":
    main()
