r"""v51 exhibit: curvature and the exact reserve-life crossover.

The reserve-life calculation reads the transcribed USGS MCS 2026 values in
``../data/usgs_mcs2026_phosphate_used.csv``.  The exact crossover threshold is

    eta_* = 1 - x/(exp(x)-1),     x = g*tau,

not the first-order approximation x/2.  At eta = 1 the stipulated net
depletion rate is zero, so the model has no finite exhaustion time.

Run from this directory:
    python3 curvature_and_crossover_v51.py
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data" / "usgs_mcs2026_phosphate_used.csv"

print("Proposition 27 - curvature number on phi(u) = c u^p, with c = 1, u0 = 1, barrier at u = 0")
print("%6s %10s %14s %14s %14s" % ("p", "kappa", "H_loc", "T exact", "T / H_loc"))
for p in (0.0, 0.5, 0.75, 1.0, 1.5, -0.5):
    c, u0 = 1.0, 1.0
    H = u0 / (c * u0**p)                      # frozen-rate ratio
    if p < 1.0:
        T = u0 ** (1 - p) / (c * (1 - p))     # closed form
    else:
        T = math.inf                          # integral diverges at the barrier
    ratio = T / H if math.isfinite(T) else float("inf")
    print("%6.2f %10.2f %14.4f %14.4f %14.4f" % (p, p, H, T, ratio))
print()
print("Closed form check, T = H_loc/(1-kappa) for kappa<1:")
for p in (0.0, 0.5, 0.75, -0.5):
    lhs = 1.0 ** (1 - p) / (1 - p)
    rhs = 1.0 / (1 - p)
    print("   p = %5.2f : T = %.6f, H_loc/(1-kappa) = %.6f, match: %s"
          % (p, lhs, rhs, abs(lhs - rhs) < 1e-12))
print("For kappa>=1 the integral diverges at the barrier; the frozen-rate ratio understates by an unbounded factor.")
print()

rows = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
world = next(row for row in rows if row["row"] == "World total (rounded)")
RES = float(world["reserves_kt"])
PROD = float(world["production_2025e_kt"])
G = 0.03
tau = RES / PROD
x = G * tau
eta_star = 1.0 - x / math.expm1(x)

print("Proposition 28 - exact reserve-life crossover on USGS MCS 2026")
print("reserves = %s kt, production = %s kt/yr -> tau = %.2f yr"
      % (f"{RES:,.0f}", f"{PROD:,.0f}", tau))
print("x = g*tau = %.6f" % x)
print("exact threshold eta_* = 1 - x/(exp(x)-1) = %.9f" % eta_star)
print("first-order approximation x/2 = %.6f (outside the admissible eta range)" % (x / 2))
print("%12s %16s %16s %14s" % ("eta", "T (yr)", "T/tau", "T - tau"))
for eta in (0.0, 0.25, 0.5, 0.75, 0.9, 0.99, 0.995, eta_star, 0.999, 1.0):
    if eta == 1.0:
        print("%12.9f %16s %16s %14s" % (eta, "no finite T", "inf", "inf"))
    else:
        T = math.log1p(x / (1.0 - eta)) / G
        print("%12.9f %16.2f %16.4f %14.2f" % (eta, T, T / tau, T - tau))
print()
print("Per-row reserve-life ratios from the same transcribed source:")
print("%-22s %-58s %14s" % ("row", "reserve convention", "ratio (yr)"))
for row in rows:
    ratio = float(row["reserves_kt"]) / float(row["production_2025e_kt"])
    print("%-22s %-58s %14.2f" % (row["row"], row["reserve_convention"], ratio))
print()
print("The first-order threshold is only a small-x approximation.  On this record x=8.76,")
print("so it points outside [0,1] even though the exact crossover lies just below eta=1.")

print()
print("Proposition 26 - sign of the frozen-rate error, on three declared laws (A0=1, Amin=1e-6)")
laws = (("proportional  phi(A)=qA", lambda A: 0.05 * A),
        ("constant      phi(A)=c", lambda A: 5e-4),
        ("accelerating  phi(A)=cA^0.4", lambda A: 0.02 * A ** 0.4))
for name, phi in laws:
    A, dt, T = 1.0, 1e-4, 0.0
    while A > 1e-6 and T < 1e6:
        A_next = A - phi(A) * dt
        if A_next <= 1e-6:
            # Interpolate the final Euler step so a constant law is not
            # misclassified by accumulated floating-point error.
            T += dt * (A - 1e-6) / (A - A_next)
            A = 1e-6
        else:
            A = A_next
            T += dt
    H = (1.0 - 1e-6) / phi(1.0)
    print("  %-26s T ~ %10.3f yr   H_loc = %10.3f yr   T>=H_loc (1e-6 tol): %s"
          % (name, T, H, T + 1e-6 >= H))
