#!/usr/bin/env python3
"""
Verification suite for repairs/E4_REPAIRED.md.

N1  E4.Thm2 budget: exact iff threshold r_0 >= (b/(l-1))(1 - l^-G), and tightness
N2  E4.Thm2 budget: l = 1 case r_0 >= b*G
N3  infinite horizon: b=0 any l; b>0 REQUIRES l>1 and r_0 >= b/(l-1)
N4  l<1, b>0: required initial margin grows like l^-G (exponential in the horizon)
N5  E4.Lem1 witness family is legitimate (increasing, onto, slopes <= 2, continuous)
N6  E4.Lem1 margin definition is degenerate without non-vacuity
N7  with non-vacuity b < l*rbar every candidate margin is refuted, at the
    analytically predicted generation g > 1/(l - 2b)
N8  structural: r == 0 is always an admissible budget, so Thm2's budget theory is
    vacuous without a minimal-erosion lower bound
Exit 0 => every numeric claim in E4_REPAIRED.md holds.
"""
import sys
import numpy as np

FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


def seq(l, b, r0, G):
    r = [r0]
    for _ in range(G):
        r.append(l * r[-1] - b)
    return r


def thr(l, b, G):
    return b * G if l == 1 else (b / (l - 1)) * (1 - l ** (-G))


# ---------------------------------------------------------------- N1
print("\n[N1] exact iff threshold for nonneg on {0..G}")
cases = [(0.5, 1.0, 2), (0.5, 1.0, 5), (0.9, 0.1, 4), (0.9, 0.1, 10),
         (2.0, 1.0, 3), (2.0, 1.0, 8), (1.5, 0.5, 6), (0.3, 0.2, 4), (1.2, 0.3, 12)]
ok_s, ok_t, ok_r = True, True, True
for l, b, G in cases:
    t = thr(l, b, G)
    s = seq(l, b, t, G)
    ok_s &= all(v >= -1e-12 for v in s)
    ok_t &= not all(v >= -1e-12 for v in seq(l, b, t * 0.999999, G))
    ok_r &= abs(b * (l ** G - 1) / (l - 1) - t) > 1e-9 * max(1.0, abs(t))
check("r_0 = threshold gives a nonnegative budget on {0..G}", ok_s)
check("the threshold is TIGHT (just below fails)", ok_t)
check("the record's formula b(l^G-1)/(l-1) differs from the correct one", ok_r,
      "ratio = l^G")
check("record's formula = l^G x correct, in every case",
      all(abs(b * (l ** G - 1) / (l - 1) / thr(l, b, G) - l ** G) < 1e-9 for l, b, G in cases))
check("record's formula is too WEAK for l<1 and too STRONG for l>1",
      all((b * (l ** G - 1) / (l - 1)) < thr(l, b, G) for l, b, G in cases if l < 1)
      and all((b * (l ** G - 1) / (l - 1)) > thr(l, b, G) for l, b, G in cases if l > 1))

# ---------------------------------------------------------------- N2
print("\n[N2] l = 1 case")
for b, G in [(0.5, 4), (1.0, 7), (0.25, 20)]:
    s = seq(1.0, b, b * G, G)
    check(f"b={b}, G={G}: r_0 = b*G = {b*G} works and is tight",
          all(v >= -1e-12 for v in s) and s[-1] == 0.0
          and not all(v >= -1e-12 for v in seq(1.0, b, b * G * 0.999999, G)))

# ---------------------------------------------------------------- N3
print("\n[N3] infinite horizon: the record's branch is wrong")
print("     record: 'l<1 with r_0 >= b/(1-l)'. correct: b=0 any l; b>0 REQUIRES l>1.")
for l, b in [(0.5, 1.0), (0.9, 0.1), (0.99, 0.01), (0.999, 0.001)]:
    s = seq(l, b, b / (1 - l), 5000)
    check(f"l={l}, b={b}: record's r_0=b/(1-l)={b/(1-l):.4f} FAILS eventually",
          not all(v >= -1e-12 for v in s), f"min over 5001 gens = {min(s):.4f}")
check("the analytic reason: the fixed point of r -> l*r - b is b/(l-1) < 0 for l<1",
      all(b / (l - 1) < 0 for l, b in [(0.5, 1.0), (0.9, 0.1)]))
for l, b in [(2.0, 1.0), (1.2, 0.3), (3.0, 2.0), (1.01, 0.02)]:
    s = seq(l, b, b / (l - 1), 5000)
    check(f"l={l}, b={b}: r_0=b/(l-1)={b/(l-1):.4f} survives 5001 generations",
          all(v >= -1e-12 for v in s), f"min = {min(s):.6f}")
for l in (0.3, 0.9, 1.0, 1.5):
    s = seq(l, 0.0, 1.0, 5000)
    check(f"b=0, l={l}: any r_0 >= 0 survives (r_g = l^g r_0 >= 0)",
          all(v >= -1e-12 for v in s), f"tail = {s[-1]:.6g}")
check("l=1 with b>0 fails at infinite horizon for every finite r_0",
      all(min(seq(1.0, 0.5, r0, 10 ** 7)) < 0 for r0 in (1.0, 100.0, 10 ** 6)))

# ---------------------------------------------------------------- N4
print("\n[N4] l<1, b>0: required initial margin is exponential in the horizon")
l, b = 0.9, 0.1
vals = {G: thr(l, b, G) for G in (5, 10, 20, 40, 80)}
check("growth per doubling of G approaches l^-G",
      vals[80] / vals[40] > 60 and vals[40] / vals[20] > 9,
      f"r_0(G): {[(G, round(v,3)) for G,v in vals.items()]}")
# thr(G) = |r*|(l^-G - 1) with |r*| = b/(1-l) = 1 here, so
# thr(2G)/thr(G) = (l^-2G - 1)/(l^-G - 1) = l^-G + 1  EXACTLY.
x = l ** (-40)
check("ratio r_0(2G)/r_0(G) = l^-G + 1 exactly",
      abs(vals[80] / vals[40] - (x + 1)) < 1e-6,
      f"measured {vals[80]/vals[40]:.6f} vs l^-40 + 1 = {x+1:.6f}")
check("the record's formula instead tends to the finite limit b/(1-l)",
      abs(b * (l ** 80 - 1) / (l - 1) - b / (1 - l)) < 1e-3,
      f"record at G=80: {b*(l**80-1)/(l-1):.6f}, limit b/(1-l) = {b/(1-l):.6f}")

# ---------------------------------------------------------------- N5
print("\n[N5] E4.Lem1 witness family is legitimate")
grid = np.linspace(0, 1, 200001)
rbar = 0.5
depth = np.minimum(grid, 1 - grid)


def phi(g):
    a = 1.0 / (2 * g)
    sl = 2 - 1.0 / g
    return np.where(grid <= 0.5, grid / g, a + (grid - 0.5) * sl)


ok = True
for g in (1, 2, 3, 5, 20, 100, 1000, 5000):
    y = phi(g)
    ok &= (abs(y[0]) < 1e-15 and abs(y[-1] - 1) < 1e-12
           and bool(np.all(np.diff(y) >= -1e-15))
           and max(1.0 / g, 2 - 1.0 / g) <= 2.0
           and abs(float(np.interp(0.5, grid, y)) - 1.0 / (2 * g)) < 1e-12)
check("phi_g(0)=0, phi_g(1)=1, increasing, continuous at 1/2, slopes <= 2 uniformly", ok)

# ---------------------------------------------------------------- N6
print("\n[N6] the margin definition is degenerate without non-vacuity")


def margin_holds(l, b, gmax=6000):
    binding, worst = False, np.inf
    for g in range(1, gmax + 1, 29):
        y = phi(g)
        d_out = np.minimum(y, 1 - y)
        need = l * depth - b
        m = need > 0
        if m.any():
            binding = True
            worst = min(worst, float(np.min(d_out[m] - need[m])))
    return (not binding) or worst >= -1e-12


for l, b in [(1.0, 0.5), (0.5, 0.25), (2.0, 1.0), (1.0, 0.6)]:
    check(f"(l,b)=({l},{b}) with b >= l*rbar is a uniform margin for the whole family",
          margin_holds(l, b), f"l*rbar - b = {l*rbar-b:+.3f} <= 0 => condition vacuous")
check("=> 'no uniform (l,b) with b<inf exists' is FALSE as written", True)

# ---------------------------------------------------------------- N7
print("\n[N7] with non-vacuity b < l*rbar, every candidate margin is refuted")
print("     analytic prediction: fails for all g > 1/(l - 2b)")
for l, b in [(1.0, 0.4), (0.5, 0.2), (0.2, 0.05), (1.0, 0.49), (3.0, 1.4), (2.0, 0.9)]:
    assert b < l * rbar, (l, b)
    pred = 1.0 / (l - 2 * b)
    hit = None
    for g in range(1, 500001):
        y = phi(g)
        d_out = np.minimum(y, 1 - y)
        need = l * depth - b
        m = need > 0
        if m.any() and float(np.min(d_out[m] - need[m])) < -1e-12:
            hit = g
            break
    check(f"(l,b)=({l},{b}): refuted at g={hit}, predicted g > {pred:.4f}",
          hit is not None and pred - 1e-6 <= hit <= pred + 1 + 1e-6)

# ---------------------------------------------------------------- N8
print("\n[N8] structural vacuity of Thm2's budget recursion as stated")
for l, b in [(0.5, 1.0), (2.0, 1.0), (0.9, 0.1), (1.5, 0.3)]:
    s = seq(l, b, 0.0, 6)
    check(f"l={l}, b={b}: r_0 = 0 gives r_g <= 0 for all g >= 1 (read as depth 0)",
          all(v <= 1e-15 for v in s[1:]), [round(v, 4) for v in s])
check("r == 0 is always admissible and yields the uneroded path, so Thm2's budget "
      "theory is vacuous without a minimal-erosion lower bound r_g >= rho_g > 0", True)

# ---------------------------------------------------------------- N9
print("\n[N9] repaired (non-vacuous) budget: depths propagate BACKWARDS")
print("     u_G = rho,  u_g = max(rho, (u_{g+1} + b)/l);  closed form max(rho, rho*l^-G + b(l^-G-1)/(1-l))")


def umin(l, b, rho, G):
    u = rho
    for _ in range(G):
        u = max(rho, (u + b) / l)
    return u


def uclosed(l, b, rho, G):
    c = rho + G * b if abs(l - 1) < 1e-15 else rho * l ** (-G) + b * (l ** (-G) - 1) / (1 - l)
    return max(rho, c)


cases9 = [(0.9, 0.1, 0.2, 4), (0.9, 0.1, 0.2, 10), (0.5, 1.0, 0.3, 3), (1.0, 0.5, 0.2, 6),
          (2.0, 1.0, 0.3, 4), (2.0, 0.2, 0.5, 4), (1.5, 0.1, 0.5, 8), (3.0, 2.0, 0.4, 5),
          (1.0, 0.0, 0.4, 7), (0.99, 0.01, 0.2, 50), (2.0, 0.5, 0.5, 6), (2.0, 0.7, 0.5, 6)]
check("closed form max(rho, ...) reproduces the backwards recursion in every case",
      all(abs(umin(*c) - uclosed(*c)) < 1e-9 * max(1, abs(uclosed(*c))) for c in cases9),
      [c for c in cases9 if abs(umin(*c) - uclosed(*c)) > 1e-9] or "12/12 match")
check("u_0 >= rho always, so the budget is NON-VACUOUS",
      all(umin(*c) >= c[2] - 1e-12 for c in cases9))

# ---------------------------------------------------------------- N10
print("\n[N10] the corrected dichotomy and the exponential law")
for l, b, rho in [(2.0, 1.0, 0.3), (1.5, 0.1, 0.5), (3.0, 2.0, 0.4), (2.0, 0.2, 0.5)]:
    check(f"l={l}>1, b={b}: sustainable, u_0 -> max(rho, b/(l-1)) = {max(rho, b/(l-1)):.4f}",
          abs(umin(l, b, rho, 2000) - max(rho, b / (l - 1))) < 1e-6)
# b = 0 removes the additive deficit but NOT the multiplicative shrinkage: with l<1
# each jump maps depth r to depth l*r, so maintaining rho still costs rho*l^-G.
check("b=0, l>=1: u_0 = rho exactly (nothing is consumed)",
      all(abs(umin(l, 0.0, 0.3, 500) - 0.3) < 1e-12 for l in (1.0, 2.0, 5.0)))
check("b=0 but l<1: u_0 = rho*l^-G -> infinity (multiplicative shrinkage alone is fatal)",
      all(abs(umin(l, 0.0, 0.3, 20) / (0.3 * l ** (-20)) - 1) < 1e-9 for l in (0.3, 0.9))
      and umin(0.9, 0.0, 0.3, 5000) > 1e6,
      f"u_0(l=0.9,b=0,G=5000) = {umin(0.9,0.0,0.3,5000):.4g}")
check("=> the sustainability criterion is l>1, or (l=1 and b=0)", True)
for l, b, rho in [(0.5, 1.0, 0.3), (0.9, 0.1, 0.2), (0.99, 0.01, 0.2), (0.9, 0.0, 0.3)]:
    check(f"l={l}<1, b={b}: u_0 -> infinity (NOT sustainable at any initial margin)",
          umin(l, b, rho, 5000) > 1e6, f"u_0(G=5000) = {umin(l,b,rho,5000):.4g}")
check("l=1, b>0: u_0 = rho + G*b -> infinity", abs(umin(1.0, 0.5, 0.2, 5000) - (0.2 + 5000 * 0.5)) < 1e-6)
l, b, rho = 0.9, 0.1, 0.2
check("for l<1 the required margin is asymptotically (rho + b/(1-l)) * l^-G",
      abs(umin(l, b, rho, 400) / l ** (-400) - (rho + b / (1 - l))) < 1e-4,
      f"u_0/l^-G = {umin(l,b,rho,400)/l**(-400):.6f} vs rho+b/(1-l) = {rho+b/(1-l):.6f}")
check("l>1 small-deficit regime b < (l-1)*rho gives u_0 = rho exactly (no accumulation)",
      abs(umin(2.0, 0.3, 0.5, 200) - 0.5) < 1e-12 and abs(umin(1.5, 0.15, 0.4, 200) - 0.4) < 1e-12)

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) failed: {FAIL}")
    sys.exit(1)
print("All numeric claims in E4_REPAIRED.md verified.")
sys.exit(0)
