r"""Section 6.2 exhibit: the curvature number, and the reserve-life crossover on the article's own
pinned record. Every number printed here is arithmetic on a declared relation; no data are read.

Run:  python3 revision/v5/code/curvature_and_crossover.py
"""
import math

# ---------------------------------------------------------------- Prop 27: kappa on the power-law family
print("Proposition 27 - curvature number on phi(u) = c u^p, with c = 1, u0 = 1, barrier at u = 0")
print("%6s %10s %14s %14s %14s" % ("p", "kappa", "H_loc", "T exact", "T / H_loc"))
for p in (0.0, 0.5, 0.75, 1.0, 1.5, -0.5):
    c, u0 = 1.0, 1.0
    H = u0 / (c * u0 ** p)                      # frozen-rate ratio
    if p == 1.0:
        T = math.inf                            # integral diverges at the barrier
    elif p < 1.0:
        T = u0 ** (1 - p) / (c * (1 - p))       # closed form
    else:
        T = math.inf
    ratio = T / H if math.isfinite(T) else float("inf")
    print("%6.2f %10.2f %14.4f %14.4f %14.4f" % (p, p, H, T, ratio))
print()
print("Closed form check, T = H_loc/(1-kappa) for kappa<1:")
for p in (0.0, 0.5, 0.75, -0.5):
    lhs = 1.0 ** (1 - p) / (1 - p); rhs = 1.0 / (1 - p)
    print("   p = %5.2f : T = %.6f, H_loc/(1-kappa) = %.6f, match: %s" % (p, lhs, rhs, abs(lhs - rhs) < 1e-12))
print("For kappa>=1 the integral diverges at the barrier; the frozen-rate ratio understates by an unbounded factor.")

# ---------------------------------------------------------------- Prop 28: reserve-life crossover
print()
G = 0.03
RES = 74_000_000.0   # kt, world phosphate reserves, USGS Mineral Commodity Summaries 2026 (as tabulated)
PROD = 240_000.0     # kt/yr, world production, same vintage
tau = RES / PROD
print("Proposition 28 - reserve-life crossover on the pinned record")
print("reserves = %s kt, production = %s kt/yr -> tau = %.2f yr (tabulated as ~309 yr)"
      % (f"{RES:,.0f}", f"{PROD:,.0f}", tau))
print("first-order threshold eta >= g*tau/2 = %.3f  (admissible elasticities obey 0 <= eta <= 1)"
      % (0.5 * G * tau))
print("%8s %16s %16s %14s" % ("eta", "T (yr)", "T/tau", "T - tau"))
for eta in (0.0, 0.25, 0.5, 0.75, 0.9, 0.99):
    T = math.log(1 + G * tau / (1 - eta)) / G
    print("%8.2f %16.2f %16.4f %14.2f" % (eta, T, T / tau, T - tau))
print()
print("The ratio exceeds the horizon computed with growth at every admissible eta, and the")
print("condition that would make it conservative requires eta > 1, i.e. reclassification larger")
print("than extraction itself. The reserve-life number is therefore optimistic in a fixed direction.")

# ---------------------------------------------------------------- Prop 26: the sign law, illustrated
print()
print("Proposition 26 - sign of the frozen-rate error, on three declared laws (A0=1, Amin=1e-6)")
laws = (("proportional  phi(A)=qA", lambda A: 0.05 * A),
            ("constant      phi(A)=c", lambda A: 5e-4),
            ("accelerating  phi(A)=cA^0.4", lambda A: 0.02 * A ** 0.4))
for name, phi in laws:
    # numerical horizon by quadrature
    A, dt, T = 1.0, 1e-4, 0.0
    while A > 1e-6 and T < 1e6:
        A -= phi(A) * dt
        T += dt
    H = (1.0 - 1e-6) / phi(1.0)
    print("  %-26s T ~ %10.3f yr   H_loc = %10.3f yr   T>=H_loc: %s" % (name, T, H, T >= H))
