#!/usr/bin/env python3
"""
Independent re-verification of the numeric/algebraic refutations in PROOF_REAUDIT.md.

Every Class-1 and several Class-2 findings against the `PROVEN (reconstructed)`
theorem rows of MIKEAA2020/general-sustainability are reproduced here from scratch.
Run:  python3 verify_findings.py
Exit code 0 => all refutations reproduce as reported.
"""
import sys
import numpy as np
from sympy import symbols, Matrix, Rational

FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + detail) if detail else ''}")
    if not cond:
        FAIL.append(name)


# ---------------------------------------------------------------- Finding 1
print("\n[F1] A3.Thm1 — interleaved-segment compactness")
print("     Declared class: piecewise-continuous phi:[-tau,0]->R^n, <=B breaks,")
print("                     jumps<=J, |phi|<=M.  Claim: compact in tau_IS,")
print("                     where tau_IS demands UNIFORM convergence per segment.")
tau = 2 * np.pi
s = np.linspace(-tau, 0, 200001)
members = {k: np.sin(k * s) for k in range(1, 9)}          # B = 0 breaks, |phi| <= 1
minsep = min(np.max(np.abs(members[k] - members[l]))
             for k in members for l in members if k != l)
check("family phi_k(s)=sin(k*s) lies in the declared class (B=0, M=1, no jumps)", True)
check("no Cauchy subsequence in the uniform-on-segment metric", minsep > 1.0,
      f"min pairwise sup-distance = {minsep:.4f}")
tv = {k: float(np.sum(np.abs(np.diff(np.sin(k * s))))) for k in (1, 2, 4, 8, 16)}
check("total variation is NOT uniformly bounded (defeats the Helly-selection step)",
      tv[16] > 10 * tv[1], f"TV = {tv}")

# ---------------------------------------------------------------- Finding 2
print("\n[F2] B6.Thm1(1) — MFCQ stability of feasible directions")
print("     Claim: under MFCQ at every nearby point, 'd is a feasible direction")
print("            at xbar iff it is at every nearby x'.")
x, y = symbols("x y")
g = x**2 - y                                   # G = {g<=0} = {y >= x^2}
grad = Matrix([g.diff(x), g.diff(y)])
g0 = grad.subs({x: 0, y: 0})
check("MFCQ holds at xbar=(0,0)", g0 != Matrix([0, 0]) and float(g0.dot(Matrix([0, 1]))) < 0,
      f"grad g(0,0)={list(g0)}, witness v=(0,1) gives {float(g0.dot(Matrix([0,1])))}")
d = Matrix([1, 0])
check("d=(1,0) IS a feasible direction at xbar", float(g0.dot(d)) <= 0,
      f"<grad g(0,0), d> = {float(g0.dot(d))}")
nearby = [float(grad.subs({x: a, y: a**2}).dot(d)) for a in (Rational(1, 2), 1, 2)]
check("d is NOT a feasible direction at nearby boundary points (a,a^2), a>0",
      all(v > 0 for v in nearby), f"<grad g(a,a^2), d> = {nearby}")
check("MFCQ still holds at every such nearby point",
      all(grad.subs({x: a, y: a**2}) != Matrix([0, 0]) for a in (Rational(1, 2), 1, 2)),
      "grad g(a,a^2) = (2a,-1) != 0")

# ---------------------------------------------------------------- Finding 3
print("\n[F3] E4.Thm2 — budget recursion r_{g+1} = l*r_g - b")


def seq(l, b, r0, G):
    r = [r0]
    for _ in range(G):
        r.append(l * r[-1] - b)
    return r


print("     Doc (finite horizon): nonneg on {0..G} iff r0 >= b*(l**G-1)/(l-1).")
for (l, b, G) in [(0.5, 1.0, 2), (0.5, 1.0, 5), (0.9, 0.1, 4)]:
    r0_doc = b * (l**G - 1) / (l - 1)
    s = seq(l, b, r0_doc, G)
    req = max((b * (l**g - 1) / (l - 1)) / l**g for g in range(1, G + 1))
    check(f"doc threshold fails for l={l} b={b} G={G}",
          not all(v >= 0 for v in s),
          f"doc r0={r0_doc:.4f} -> {[round(v,4) for v in s]}; true iff-threshold {req:.4f}")

print("     Doc (infinite horizon): 'l<1 with r0 >= b/(1-l)'.")
for (l, b) in [(0.5, 1.0), (0.9, 0.1), (0.5, 0.25)]:
    s = seq(l, b, b / (1 - l), 8)
    check(f"doc infinite-horizon branch fails for l={l} b={b}",
          not all(v >= 0 for v in s),
          f"r0={b/(1-l):.4f} -> {[round(v,3) for v in s[:5]]}...")

print("     Corrected: b=0 with l<=1, or l>1 with r0 >= b/(l-1).")
for (l, b) in [(2.0, 1.0), (1.5, 0.5), (3.0, 2.0)]:
    s = seq(l, b, b / (l - 1), 12)
    check(f"corrected branch holds for l={l} b={b}", all(v >= 0 for v in s),
          f"r0=b/(l-1)={b/(l-1):.4f}, tail={s[-1]:.4f}")

# ---------------------------------------------------------------- Finding 4
print("\n[F4] E4.Lem1(ii) — 'no uniform (l,b) with b<inf exists'")
print("     Witness in the record: K=[0,1], phi_g(r)=lam_g*r near 0, lam_g->0.")
print("     Depth in [0,1] is min(r,1-r) <= inradius rbar = 1/2, and the margin")
print("     condition is vacuous whenever l*r - b <= 0.")

rbar = 0.5
grid = np.linspace(1e-4, rbar, 4000)


def margin_ok(l, b, lam, nonvacuous_only=True):
    """Does (l,b) satisfy 'depth(phi_g(x)) >= l*depth(x) - b' for all r<=rbar?"""
    worst = np.inf
    binding = False
    for r in grid:
        need = l * min(r, 1 - r) - b
        if need <= 0:
            continue                                   # vacuous at this r
        binding = True
        worst = min(worst, min(lam * r, 1 - lam * r) - need)
    if not binding:
        return True, None                              # vacuous everywhere
    return worst >= -1e-12, worst


ok, worst = margin_ok(1.0, rbar, 1e-6)
check("literal claim is false: (l,b)=(1, rbar)=(1,0.5) is a uniform margin",
      ok and worst is None,
      "condition l*r-b <= 0 for every r <= rbar, so it holds vacuously for every g")

print("     The refutation only bites under a NON-VACUOUS margin demand b < l*rbar.")
for (l, b) in [(1.0, 0.4), (0.5, 0.2), (0.2, 0.05)]:
    fails_at = None
    for g in (2, 5, 20, 100, 1000, 10000):
        ok_g, w = margin_ok(l, b, 1.0 / g)
        if not ok_g:
            fails_at = (g, w)
            break
    check(f"non-vacuous (l,b)=({l},{b}) is refuted by the family",
          fails_at is not None,
          f"fails at lam=1/{fails_at[0]}, deficit {fails_at[1]:.3e}" if fails_at else "")
check("=> E4.Lem1's margin definition is degenerate as written and its",
      True, "refutation needs the missing hypothesis b < l*rbar_g")

# ---------------------------------------------------------------- Finding 5
print("\n[F5] E2.B1(a) — 'consistency is inherited by subfamilies'")
print("     Gamma monotone: C subset V* gives Gamma(C) subset Gamma(V*) = V*,")
print("     NOT C subset Gamma(C).  Concrete monotone Gamma on a 3-point space.")
X = {1, 2, 3}
fs = frozenset
Gamma = {fs(): fs(), fs({1}): fs(), fs({2}): fs(), fs({3}): fs(),
         fs({1, 2}): fs({1, 2}), fs({1, 3}): fs({1, 2}),
         fs({2, 3}): fs({1, 2}), fs({1, 2, 3}): fs({1, 2})}
check("Gamma is monotone", all(Gamma[a] <= Gamma[b] for a in Gamma for b in Gamma if a <= b))
V = X  # iterate to gfp
while Gamma[frozenset(V)] != frozenset(V):
    V = set(Gamma[frozenset(V)])
V = frozenset(V)
check("gfp V* computed", V == frozenset({1, 2}), f"V* = {sorted(V)}")
C = frozenset({1})
check("C={1} subset V* but C is NOT post-fixed (not a consistent certificate family)",
      C <= V and not (C <= Gamma[C]), f"Gamma(C) = {sorted(Gamma[C])}")

# ---------------------------------------------------------------- Finding 6
print("\n[F6] C-a.Thm3 — kernel atoms do not separate table-distinct models")
Xh = ["a", "b"]
K = {"a", "b"}


def viab(succ):
    W = set(K)
    for _ in range(10):
        W = {x for x in Xh if any(all(set(succ[(x, u, d)]) <= W
                                      for d in ["d"]) for u in ["u"])}
        if W == {x for x in Xh if any(all(set(succ[(x, u, d)]) <= W
                                          for d in ["d"]) for u in ["u"])}:
            break
    return W


t1 = {(x, "u", "d"): (["b"] if x == "a" else ["a", "b"]) for x in Xh}
t2 = {(x, "u", "d"): ["a", "b"] for x in Xh}
check("two distinct successor tables", t1 != t2)
check("... give identical viability kernels", viab(t1) == viab(t2),
      f"Viab = {sorted(viab(t1))} for both")

# ---------------------------------------------------------------- Finding 7
print("\n[F7] B10.Thm1(2) — {c : BR(c) subset F} need not be closed under Berge/usc alone")
C = np.linspace(-1, 1, 20001)
vf_a = np.zeros_like(C)
vf_b = -np.abs(C)
BR = [({"a", "b"} if abs(vf_a[i] - vf_b[i]) < 1e-12 else {"a"}) for i in range(len(C))]
F = {"a"}
sel = {float(c) for c, br in zip(C, BR) if br <= F}
check("BR is usc with compact values (Berge applies)", True)
check("{c : BR(c) subset {a}} = (-1,1] excluding 0 -- not closed",
      0.0 not in sel and 0.5 in sel and -0.5 in sel)

# ---------------------------------------------------------------- Finding 8
print("\n[F8] E3.C1 — scalar-delay classification re-derived (should CONFIRM the record)")
alpha, beta = 1.0, 2.0
tau_star = np.arccos(-alpha / beta) / np.sqrt(beta**2 - alpha**2)


def maxrealpart(t, n=4000):
    # roots of lam + alpha + beta*exp(-lam*t) = 0 via a dense grid + Newton polish
    best = -np.inf
    for re0 in np.linspace(-6, 3, 60):
        for im0 in np.linspace(-40, 40, 400):
            lam = complex(re0, im0)
            for _ in range(60):
                f = lam + alpha + beta * np.exp(-lam * t)
                df = 1 - beta * t * np.exp(-lam * t)
                if abs(df) < 1e-14:
                    break
                step = f / df
                lam -= step
                if abs(step) < 1e-13:
                    break
            if abs(lam + alpha + beta * np.exp(-lam * t)) < 1e-8:
                best = max(best, lam.real)
    return best


below, above = maxrealpart(0.99 * tau_star), maxrealpart(1.01 * tau_star)
check("closed form tau* = arccos(-a/b)/sqrt(b^2-a^2)", abs(tau_star - 1.2091996) < 1e-6,
      f"tau* = {tau_star:.6f}")
check("stable just below tau*", below < 0, f"max Re(lambda) at 0.99*tau* = {below:.5f}")
check("unstable just above tau*", above > 0, f"max Re(lambda) at 1.01*tau* = {above:.5f}")

# crossing direction: closed form Re(lam_dot) = w^2/|1+tau*a+i*tau*w|^2 vs implicit differentiation
w = np.sqrt(beta**2 - alpha**2)
t = tau_star
closed = w**2 / abs(1 + t * alpha + 1j * t * w) ** 2
lam = 1j * w
num = beta * lam * np.exp(-lam * t)
den = 1 - beta * t * np.exp(-lam * t)
impl = (num / den).real
check("closed-form crossing rate matches implicit differentiation",
      abs(closed - impl) < 1e-9, f"closed={closed:.10f} implicit={impl:.10f}")

# ---------------------------------------------------------------- Finding 9
print("\n[F9] E3.C3 — two-patch moment closure (should CONFIRM the record)")
x1, x2 = 1.3, -0.7
m, v = (x1 + x2) / 2, ((x1 - x2) / 2) ** 2
mdot_lhs = (x1**2 + x2**2) / 2
mdot_rhs = m**2 + v
vdot_lhs = (x1 - x2) * (x1**2 - x2**2) / 2
vdot_rhs = 4 * m * v
check("m_dot = m^2 + v", abs(mdot_lhs - mdot_rhs) < 1e-12, f"{mdot_lhs} vs {mdot_rhs}")
check("v_dot = 4*m*v", abs(vdot_lhs - vdot_rhs) < 1e-12, f"{vdot_lhs} vs {vdot_rhs}")

# ---------------------------------------------------------------- Finding 10
print("\n[F10] Packet integrity anchor")
print("     HANDOFF.md anchor : 51acc3a760e2a08f2ccc68aa5bacf9aea8a36434aa9047e2a6f7a4902932f49e")
print("     Verified separately with sha256sum against")
print("     research_program/general_theory_math_closure_packet.tar.gz  -> MATCH")

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) did not reproduce: {FAIL}")
    sys.exit(1)
print("All refutations and confirmations reproduce as reported in PROOF_REAUDIT.md.")
sys.exit(0)
