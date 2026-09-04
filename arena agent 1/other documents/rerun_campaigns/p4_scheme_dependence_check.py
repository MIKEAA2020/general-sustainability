#!/usr/bin/env python3
"""Scheme-dependence check for the P4 review-interval monodromy.

Reuses the verified Candidate A Jacobian and gains. Computes:
  1. start-of-period measurement variant  (claude: crossing ~3.0 yr)
  2. M_ZOH  -- physically native zero-order hold (z held, effort run continuously)
Determines whether the 6.50 yr location is or is not scheme-dependent.
"""
import numpy as np
from numpy.linalg import eigvals
from scipy.linalg import expm

r, K, q = 0.02, 100.0, 0.001
eta, Emax, dref = 0.914, 30.0, 1.0
d0, tm, Zref = 0.01, 5.0, 1.0
delta = np.log(2) / 10.0

a = -eta / Emax
b = eta * delta / dref
c = d0 * delta / (Zref + delta)
E_star = (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
N_star = K * (1 - q * E_star / r)

gate = 1 - E_star / Emax
A_N = r * (1 - 2 * N_star / K) - q * E_star
A_E = -q * N_star
B_N = -A_N / (2 * tm)
B_E = -A_E / (2 * tm)
d = 1 / tm

CE_m = gate * eta * (delta / dref - 2 * E_star / Emax)
CZ_m = gate * (eta * E_star / dref + d0 * Zref / (Zref + delta) ** 2)

A_hold = np.array([[A_N, 0.0, A_E], [B_N, -d, B_E], [0.0, 0.0, 0.0]])
# full undelayed Jacobian (with C_Z entry)
J = np.array([[A_N, 0.0, A_E], [B_N, -d, B_E], [0.0, CZ_m, CE_m]])

def exact_review(T, CE, CZ):
    R = np.eye(3)
    eC = np.exp(CE * T)
    R[2, 1] = (eC - 1.0) * CZ / CE
    R[2, 2] = eC
    return R

def find_crossing(mono_fun, lo=0.2, hi=120.0, n=120000):
    """Fine scan of rho-1 sign changes, then bisection refine."""
    grid = np.linspace(lo, hi, n)
    rhos = np.array([abs(eigvals(mono_fun(T))).max() for T in grid])
    signs = np.sign(rhos - 1.0)
    crossings = []
    for i in range(len(grid) - 1):
        if signs[i] != 0 and signs[i] != signs[i + 1]:
            l, h = grid[i], grid[i + 1]
            for _ in range(60):
                m = 0.5 * (l + h)
                rm = abs(eigvals(mono_fun(m))).max()
                rl = abs(eigvals(mono_fun(l))).max()
                if (rl - 1.0) * (rm - 1.0) < 0:
                    h = m
                else:
                    l = m
            T = 0.5 * (l + h)
            ev = eigvals(mono_fun(T))
            k = sorted(ev, key=lambda x: abs(abs(x) - 1.0))[0]
            kind = "complex-pair" if abs(k.imag) > 1e-9 else "real"
            crossings.append((round(T, 4), kind, round(k.real, 4), round(k.imag, 4)))
    return crossings

print("=== (1) start-of-period measurement (update fed z at t_k^- BEFORE flow) ===")
# Under flow-then-update but with the measurement held at the START-of-period value:
# effort row becomes (0, kappa C_Z, e^{C_E T_r}); claude: rho ~ 1.00024@2, 0.99994@3...
def sop_mono(T):
    R = np.eye(3)
    eC = np.exp(CE_m * T)
    R[2, 1] = (eC - 1.0) * CZ_m / CE_m   # effort from START-of-period z
    R[2, 2] = eC
    M = expm(A_hold * T) @ R             # update applied to the pre-flow state, then flow? try both orders
    return M

# claude phrases it as update fed z(t_k^-). Two plausible constructions:
# (a) M = R_updation_then_flow: R applied to pre-review state, then exp(A_hold T)
def sop_mono_a(T):
    R = np.eye(3)
    eC = np.exp(CE_m * T)
    R[2, 1] = (eC - 1.0) * CZ_m / CE_m
    R[2, 2] = eC
    return expm(A_hold * T) @ R
# (b) M = exp(A_hold T) then R applied to flowed state (effort from start value already flowed)
for name, f in [("(a) R-then-flow", sop_mono_a)]:
    ca = find_crossing(f)
    print(f"  start-of-period ({name}): crossings = {ca}")
    for T in (2.0, 3.0, 4.0, 6.5):
        print(f"    rho({T}) = {abs(eigvals(f(T))).max():.6f}")

print()
print("=== (2) M_ZOH (physically native: z held at z_k, effort runs continuously) ===")
def mzoh(T):
    AZ = J.copy()
    AZ[2, 1] = 0.0                 # remove the C_Z entry: effort not impulsively fed
    # continuous effort: dz contribution replaced by held z_k
    # AZ below has C_Z suppressed in the z->e block; here effort ODE runs with held z.
    # Use A_Z as the block with the (2,1) entry removed plus e(t) evolving:
    eA = expm(AZ * T)
    # integral of exp(A_Z s) ds = AZ^{-1}(exp(A_Z T)-I) (AZ invertible? check det)
    if abs(np.linalg.det(AZ)) > 1e-12:
        integ = np.linalg.solve(AZ, expm(AZ * T) - np.eye(3))
    else:
        # use block/expm-based integral via augmented matrix
        aug = np.block([[AZ, np.eye(3)], [np.zeros((3, 3)), np.zeros((3, 3))]])
        integ = expm(aug * T)[0:3, 3:6]
    e3 = np.zeros((3, 1)); e3[2, 0] = 1.0
    e2 = np.zeros((1, 3)); e2[0, 1] = 1.0
    return eA + integ @ (CZ_m * e3 @ e2)

cm = find_crossing(mzoh)
print(f"  M_ZOH mobilising: crossings = {cm}")
for T in (0.2, 1.0, 2.0, 6.5, 20.0, 60.0, 120.0):
    print(f"    rho({T}) = {abs(eigvals(mzoh(T))).max():.6f}")

print()
print("=== (3) consistency / DC-gain sanity (L(0)=0 -> rank-one at large T) ===")
print(f"  L(0) = B_E*0 = {B_E*0.0:.6f}  (filter identity)")
# Verify M_exact large-T tendency: leading eigenvalue
for T in (200.0, 500.0, 1000.0):
    M = exact_review(T, CE_m, CZ_m) @ expm(A_hold * T)
    print(f"  M_exact rho({T}) = {abs(eigvals(M)).max():.6f}")
