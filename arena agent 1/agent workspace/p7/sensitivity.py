"""Paper 7 (sampled governance): reproduce the 6.501-yr exact-mobilising crossing,
then measure how far it moves under small parameter perturbations.

Model is the Candidate A reconstruction from
arena agent 1/other documents/rerun_campaigns/campaign_p5_crossing_scan.py,
i.e. the paper's own logistic hold-map core.
"""
import numpy as np
from numpy.linalg import eigvals
from scipy.linalg import expm

def build(r=0.02, K=100.0, q=0.001, eta=0.914, Emax=30.0, dref=1.0,
          d0=0.01, tm=5.0, Zref=1.0, delta=None):
    if delta is None:
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
    CE_p = -gate * eta
    E0 = E_star * (Zref + delta) / Zref
    CZ_p = gate * eta * (-E0 * Zref / (Zref + delta) ** 2)
    A_hold = np.array([[A_N, 0.0, A_E], [B_N, -d, B_E], [0.0, 0.0, 0.0]])
    return dict(CE_m=CE_m, CZ_m=CZ_m, CE_p=CE_p, CZ_p=CZ_p, A_hold=A_hold,
                E_star=E_star, N_star=N_star, exploit=q * E_star / r, delta=delta)

def exact_review(T, CE, CZ):
    R = np.eye(3); eC = np.exp(CE * T)
    R[2, 1] = (eC - 1.0) * CZ / CE
    R[2, 2] = eC
    return R

def euler_review(T, CE, CZ):
    R = np.eye(3); R[2, 1] = T * CZ; R[2, 2] = 1 + T * CE
    return R

def rho(T, m, CE, CZ, exact=True):
    R = exact_review(T, CE, CZ) if exact else euler_review(T, CE, CZ)
    return max(abs(eigvals(R @ expm(m["A_hold"] * T))))

def crossings(m, CE, CZ, exact=True, Tmin=0.2, Tmax=200.0, n=4001):
    """Bracket on a grid, then bisect. Returns list of (T, direction)."""
    Ts = np.linspace(Tmin, Tmax, n)
    rs = np.array([rho(T, m, CE, CZ, exact) for T in Ts])
    s = np.sign(rs - 1.0)
    idx = np.where((s[1:] * s[:-1] < 0) & (s[:-1] != 0) & (s[1:] != 0))[0]
    out = []
    for i in idx:
        lo, hi, rlo = Ts[i], Ts[i + 1], rs[i]
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            rm = rho(mid, m, CE, CZ, exact)
            if (rlo - 1) * (rm - 1) < 0:
                hi = mid
            else:
                lo, rlo = mid, rm
        Tk = 0.5 * (lo + hi)
        out.append((Tk, "unstable->stable" if rs[i] > 1 else "stable->unstable"))
    return out

print("=" * 78)
print("1. REPRODUCE THE PAPER'S BASELINE")
m = build()
print("   mobilising exact  rho(1) = %.5f   (paper 1.00035)" % rho(1.0, m, m["CE_m"], m["CZ_m"], True))
print("   mobilising Euler  rho(1) = %.5f   (paper 1.00055)" % rho(1.0, m, m["CE_m"], m["CZ_m"], False))
print("   protective Euler  rho(1) = %.4f    (paper 0.9838)" % rho(1.0, m, m["CE_p"], m["CZ_p"], False))
cr = crossings(m, m["CE_m"], m["CZ_m"], True)
print("   mobilising exact crossings:", [(round(t, 3), d) for t, d in cr])
print("   exploitation ratio q*E*/r = %.6f" % m["exploit"])
BASE = cr[0][0] if cr else float("nan")
print("   >>> BASELINE CROSSING = %.4f yr  (paper 6.501)" % BASE)

print()
print("=" * 78)
print("2. SENSITIVITY: perturb each parameter by +/- a small relative amount")
print("   and recompute the exact mobilising crossing.")
print()
print("   %-8s %10s %10s %10s %10s %10s" % ("param", "-2%", "-1%", "base", "+1%", "+2%"))
print("   " + "-" * 62)
sweep = {}
for pname, base in [("r", 0.02), ("K", 100.0), ("q", 0.001), ("eta", 0.914),
                    ("Emax", 30.0), ("dref", 1.0), ("d0", 0.01), ("tm", 5.0),
                    ("Zref", 1.0)]:
    vals = []
    for f in (0.98, 0.99, 1.0, 1.01, 1.02):
        kw = {pname: base * f}
        mm = build(**kw)
        c = crossings(mm, mm["CE_m"], mm["CZ_m"], True)
        vals.append(c[0][0] if c else float("nan"))
    sweep[pname] = vals
    print("   %-8s %10.3f %10.3f %10.3f %10.3f %10.3f" % (pname, *vals))

print()
print("   sensitivity of the crossing to a +/-1% parameter change (yr, and %):")
rows = []
for p, v in sweep.items():
    d1 = abs(v[4] - v[2]); d2 = abs(v[0] - v[2])
    worst = max(d1, d2)
    rows.append((worst, p, v))
for worst, p, v in sorted(rows, reverse=True):
    print("      %-6s  worst 1%% swing: %8.3f yr  (%6.1f%% of baseline)" % (p, worst, 100 * worst / BASE))

print()
print("=" * 78)
print("3. THE EXPLOITATION RATIO SPECIFICALLY (q*E*/r)")
print("   %-10s %14s %12s %10s" % ("q change", "exploit ratio", "crossing", "% move"))
print("   " + "-" * 52)
for f in (0.98, 0.99, 0.995, 0.998, 1.0, 1.002, 1.005, 1.01, 1.02):
    mm = build(q=0.001 * f)
    c = crossings(mm, mm["CE_m"], mm["CZ_m"], True)
    t = c[0][0] if c else float("nan")
    print("   %-10s %14.6f %12.3f %10.2f%%" % ("%+.1f%%" % (100 * (f - 1)),
                                              mm["exploit"], t, 100 * (t - BASE) / BASE))

print()
print("=" * 78)
print("4. CONDITION NUMBER OF THE CROSSING AT THE BASELINE")
h = BASE * 1e-4
dT = (rho(BASE + h, m, m["CE_m"], m["CZ_m"], True)
      - rho(BASE - h, m, m["CE_m"], m["CZ_m"], True)) / (2 * h)
print("   d(rho)/dT at the crossing = %.3e per yr   (paper: -0.000683)" % dT)
eps = 1e-3  # a 0.1% mis-specification in rho
print("   a %.1e error in rho near the crossing displaces T by ~%.2f yr"
      % (eps, abs(eps / dT)))
