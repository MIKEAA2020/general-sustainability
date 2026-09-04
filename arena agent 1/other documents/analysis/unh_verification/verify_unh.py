#!/usr/bin/env python3
"""UNH verification for the Tikhonov reduction — corrected algebra + FD cross-check.

Fast subsystem (Layer-4 macro block, eps boundary-layer; physical eps=1):
  eps K' = s*Q - dK*K - th*K*Dt            Q = a*(K/Kref)^alpha*(L/Lref)^beta*Sagg^dS (Kref=Lref=1)
  eps L' = rL0*L*(1 - L/Lmax(Q))           Lmax(Q)=max(Lmin, L0*(Q/Q0)^eta)   (L0=Q0=1)
  eps a' = etaA0*a*(1-a/amax) - eps*nu*a*Dt
  eps T' = (etaT00 + etaT10*Dt*T)*(1-T/Tmax)
QSS: a*=amax, T*=Tmax, K*=sQ/D (D=dK+th*Dt), L* solves L = max(Lmin, Q(L)^eta).
Jacobian at QSS (M=Lmax, M'=dLmax/dQ=eta*M/Q interior; 0 at floor):
  J_KL = [[-(1-alpha)D,        beta*s*Q/L ],
          [ eta*alpha*rL0*M/K, -rL0*(1-eta*beta) ]]        (M=L at the root)
  trace = -(1-alpha)D - rL0(1-eta*beta);  det = rL0*D*(1-alpha-eta*beta)
  Hurwitz  <=>  alpha + eta*beta < 1   (uniform in Dt>=0, Q>0; D>=dK>0)
  lambda_a = -(etaA0 + nu*Dt) < 0;  lambda_T = -(etaT00+etaT10*Dt*Tmax)/Tmax < 0  (uniform)
Verified below: (i) sympy on the hand-built J_KL; (ii) finite-difference cross-check of the
full 4x4 analytic Jacobian against the vector field; (iii) the class sweep with the correct
condition, violation fraction, and margin.
"""
import json
import numpy as np
import sympy as sp

# ---- symbolic: hand-built J_KL (K row uses sQ/K=D at QSS) ----
s, dK, th, Dt, rL0, eta, alpha, beta = sp.symbols("s dK th Dt rL0 eta alpha beta", positive=True)
Q, M, L = sp.symbols("Q M L", positive=True)
J_KL = sp.Matrix([[-(1-alpha)*(dK+th*Dt), beta*s*Q/L],
                  [eta*alpha*rL0*M/s, -rL0*(1-eta*beta)]])
J_KL = J_KL.subs(M, L).subs(s, L*0 + (dK+th*Dt)*L/Q)  # no-op guard
J_KL = sp.Matrix([[-(1-alpha)*(dK+th*Dt), beta*s*Q/L],
                  [eta*alpha*rL0*(dK+th*Dt)*L/(s*Q), -rL0*(1-eta*beta)]])
J_KL = J_KL.subs(L, M)
tr = sp.simplify(J_KL.trace())
det = sp.simplify(J_KL.det())
print("K-L block at QSS (M=L):")
print("  trace =", tr)
print("  det   =", sp.factor(det), "   [= rL0*D*(1-alpha-eta*beta)]")
print("  Hurwitz  <=>  alpha + eta*beta < 1")

# ---- vector field + analytic Jacobian + FD cross-check ----
def fvec(y, p, eps=1.0):
    K, L, a, T = y
    alpha, beta, dS, eta, s, dK, th, nu, rL0, etaA0, etaT00, etaT10, Dt, Sagg = p
    Q = a*K**alpha*L**beta*Sagg**dS
    Lmax = max(0.05, Q**eta)
    return np.array([(s*Q - dK*K - th*K*Dt)/eps,
                     (rL0*L*(1 - L/Lmax))/eps,
                     (etaA0*a*(1-a) - eps*nu*a*Dt)/eps,
                     (etaT00 + etaT10*Dt*T)*(1-T)/eps])

def analytic_J(y, p):
    K, L, a, T = y
    alpha, beta, dS, eta, s, dK, th, nu, rL0, etaA0, etaT00, etaT10, Dt, Sagg = p
    D = dK + th*Dt
    Q = a*K**alpha*L**beta*Sagg**dS
    Lmax = max(0.05, Q**eta)
    Mprime = (eta*Lmax/Q) if Lmax > 0.0500001 else 0.0
    J = np.zeros((4, 4))
    J[0, 0] = s*alpha*Q/K - D
    J[0, 1] = s*beta*Q/L
    J[0, 2] = s*Q/a
    J[1, 0] = rL0*Mprime*alpha*Q/K
    J[1, 1] = -rL0 + rL0*Mprime*beta*Q/L
    J[1, 2] = rL0*Mprime*Q/a
    J[2, 2] = -etaA0 - nu*Dt
    J[3, 3] = -(etaT00 + etaT10*Dt*T)
    return J

def qss_roots(p):
    alpha, beta, dS, eta, s, dK, th, nu, rL0, etaA0, etaT00, etaT10, Dt, Sagg = p
    D = dK + th*Dt
    c = (s/D)**(alpha/(1-alpha)) * Sagg**(dS/(1-alpha))
    s_exp = eta*beta/(1-alpha)
    if abs(s_exp - 1) < 1e-9 or c <= 0:
        L_hi = 100.0
    else:
        log_upper = eta/(1-s_exp)*np.log(c)
        L_hi = max(100.0, min(1e6, 2.0*np.exp(min(log_upper, 60))))
    grid = np.concatenate([np.linspace(0.05, 1.0, 300), np.geomspace(1.0, max(1.001, L_hi), 700)])
    r = np.maximum(0.05, c**eta*grid**s_exp) - grid
    sgn = np.sign(r); cand = []
    for i in range(len(grid)-1):
        if sgn[i] == 0: cand.append(grid[i])
        elif sgn[i] != sgn[i+1]:
            lo, hi = grid[i], grid[i+1]
            for _ in range(60):
                mid = (lo+hi)/2
                rr = np.maximum(0.05, c**eta*mid**s_exp) - mid
                if rr == 0 or hi-lo < 1e-12: break
                if np.sign(rr) == sgn[i]: lo = mid
                else: hi = mid
            cand.append((lo+hi)/2)
    roots = []
    for cnd in cand:
        if all(abs(cnd-r0) > 1e-6 for r0 in roots): roots.append(cnd)
    return roots

# FD cross-check on 400 random draws (across full class incl. violations)
rng = np.random.default_rng(11)
worst_err = 0.0
for it in range(400):
    p = None
    while p is None:
        alpha = rng.uniform(0.25, 0.45); beta = rng.uniform(0.30, 0.60); dS = 1-alpha-beta
        if dS <= 0: continue
        p = (alpha, beta, dS, rng.uniform(0.3, 1.2), rng.uniform(0.10, 0.30), rng.uniform(0.03, 0.10),
             rng.uniform(0, 0.05), rng.uniform(0, 0.02), rng.uniform(0.005, 0.03), rng.uniform(0.005, 0.02),
             rng.uniform(0.01, 0.05), rng.uniform(0, 0.5), rng.uniform(0, 5), rng.uniform(0.2, 1.0))
    for Lroot in qss_roots(p):
        alpha, beta, dS, eta, s, dK, th, nu, rL0, etaA0, etaT00, etaT10, Dt, Sagg = p
        Q = (s/(dK+th*Dt))**(alpha/(1-alpha)) * Lroot**(beta/(1-alpha)) * Sagg**(dS/(1-alpha))
        K = s*Q/(dK+th*Dt)
        y = np.array([K, Lroot, 1.0, 1.0])
        Ja = analytic_J(y, p)
        h = 1e-5
        Jfd = np.zeros((4, 4))
        for j in range(4):
            yp, ym = y.copy(), y.copy()
            yp[j] += h; ym[j] -= h
            Jfd[:, j] = (fvec(yp, p) - fvec(ym, p))/(2*h)
        worst_err = max(worst_err, np.abs(Ja - Jfd).max())
print(f"FD cross-check (400 draws x roots): max |J_analytic - J_fd| = {worst_err:.2e}")

# ---- class sweep ----
rng = np.random.default_rng(20260903)
class_def = dict(alpha=(0.25, 0.45), beta=(0.30, 0.60), eta=(0.3, 1.2), s=(0.10, 0.30),
                 dK=(0.03, 0.10), th=(0.0, 0.05), nu=(0.0, 0.02), rL0=(0.005, 0.03),
                 etaA0=(0.005, 0.02), etaT00=(0.01, 0.05), etaT10=(0.0, 0.5),
                 Dt=(0.0, 5.0), Sagg=(0.2, 1.0))
N = 12000
viol = 0; multi = 0; accepted = 0
worst_full = -np.inf; worst_restricted = -np.inf
for _ in range(N):
    p = {}
    for k, (lo, hi) in class_def.items(): p[k] = rng.uniform(lo, hi)
    dS = 1 - p["alpha"] - p["beta"]
    if dS <= 0: continue
    p["dS"] = dS; accepted += 1
    a_plus_eb = p["alpha"] + p["eta"]*p["beta"]
    if a_plus_eb >= 1: viol += 1
    roots = qss_roots(tuple(p[k] for k in
        ["alpha","beta","dS","eta","s","dK","th","nu","rL0","etaA0","etaT00","etaT10","Dt","Sagg"]))
    if len(roots) > 1: multi += 1
    for Lstar in roots:
        D = p["dK"] + p["th"]*p["Dt"]
        Q = (p["s"]/D)**(p["alpha"]/(1-p["alpha"])) * Lstar**(p["beta"]/(1-p["alpha"])) * p["Sagg"]**(p["dS"]/(1-p["alpha"]))
        K = p["s"]*Q/D
        y = np.array([K, Lstar, 1.0, 1.0])
        lam = np.linalg.eigvals(analytic_J(y, tuple(p[k] for k in
            ["alpha","beta","dS","eta","s","dK","th","nu","rL0","etaA0","etaT00","etaT10","Dt","Sagg"]))).real.max()
        worst_full = max(worst_full, lam)
        if a_plus_eb < 1: worst_restricted = max(worst_restricted, lam)
print(f"\nSweep: {accepted} accepted draws; alpha+eta*beta >= 1 violations: {viol} ({100*viol/accepted:.1f}%); multi-root QSS: {multi}")
print(f"Full class worst max Re(lambda): {worst_full:+.6f}")
print(f"Restricted class (alpha+eta*beta<1) worst max Re(lambda): {worst_restricted:+.6f}  -> margin gamma_y = {-worst_restricted:.6f}")
# analytic margin on the restricted class: the K-L eigenvalues have Re <= -min{(1-a)D - rL0(1-eb) offsets...}: report min over class of the analytic bounds
# lower bounds: trace/2 is not a bound; use min of the two diagonal-based bounds: Re(lambda) <= max(J00, J11)-ish. We report the numeric margin instead.
json.dump({"fd_crosscheck_max_err": worst_err,
           "sweep": {"N": accepted, "viol_frac": viol/accepted, "multi_root": multi,
                     "worst_full": worst_full, "worst_restricted": worst_restricted,
                     "margin_restricted": -worst_restricted}},
          open("unh_sweep_results.json", "w"), indent=1)
print("saved unh_sweep_results.json")
