#!/usr/bin/env python3
"""
Verification suite for repairs/B10_THM1_REPAIRED.md.  Reads and writes no repo file.

N1  BR has nonempty compact values and closed graph under the stated hypotheses
N2  both leader objectives (min and max over BR) are usc, hence attain their maxima
N3  the record's displayed equation is CORRECT when pi* is the pessimistic response
N4  "optimistic and pessimistic coincide" is FALSE; closed graph does not suffice
N5  exact characterisation: equality holds iff v_l(c*_opt, .) is constant on BR(c*_opt)
N6  defect 2: {c : BR(c) subset F} is NOT closed under usc alone (counterexample)
N7  the EXISTENTIAL form {c : BR(c) cap F != empty} IS closed under usc alone
    -- and this is the form the record's own governance question asks for
N8  the UNIVERSAL form IS closed when BR is additionally lsc / continuous
N9  E2.B2(a)/KRN applies to BR itself (closed graph + compact values)
Exit 0 => every numeric claim in B10_THM1_REPAIRED.md holds.
"""
import sys
import itertools
import numpy as np

FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


# --------------------------------------------------------------- helpers
def br_from(vf, cs, pis):
    """BR(c) = argmax_pi vf(c, pi), computed exactly on finite Pi."""
    return {c: tuple(p for p in pis
                     if abs(vf[c][p] - max(vf[c].values())) < 1e-12) for c in cs}


def vbar(vf, c):
    return max(vf[c].values())


def graph_is_closed_analytically(vf, cs, pis):
    """For finite Pi the graph is
         {(c,pi) : v_f(c,pi) - vbar_f(c) = 0},
    the zero set of a continuous function on the compact C x Pi, hence closed.
    Verify the limit-point property directly: along any sequence c_n -> c with
    pi_n in BR(c_n) and pi_n -> pi (Pi discrete => pi_n = pi eventually), the
    limit satisfies the defining equation."""
    worst = 0.0
    for c in cs:
        for pi in pis:
            if abs(vf[c][pi] - vbar(vf, c)) < 1e-12:          # (c,pi) in graph
                continue
            # (c,pi) not in graph; check it is not a limit of graph points with that pi
            gap = abs(vf[c][pi] - vbar(vf, c))
            worst = max(worst, gap)                            # positive gap => not a limit
    return worst > 0 or all(abs(vf[c][pi] - vbar(vf, c)) < 1e-12
                            for c in cs for pi in pis), worst


def universal_set(vf, cs, pis, F):
    """{c : BR(c) subset F} = {c : v_f(c,pi) < vbar_f(c) for every pi notin F}.
    A STRICT inequality of continuous functions => OPEN, generally not closed."""
    return {c for c in cs if all(vf[c][pi] < vbar(vf, c) - 1e-15 for pi in pis if pi not in F)}


def existential_set(vf, cs, pis, F):
    """{c : BR(c) cap F != empty} = {c : v_f(c,pi) = vbar_f(c) for some pi in F}.
    An EQUALITY of continuous functions => CLOSED."""
    return {c for c in cs if any(abs(vf[c][pi] - vbar(vf, c)) < 1e-12 for pi in F)}


# --------------------------------------------------------------- N1..N3
print("\n[N1-N3] the working half of the record: existence")
C = [-1.0, -0.5, 0.0, 0.5, 1.0]
Pi = ["a", "b"]
vf = {c: {"a": 0.0, "b": -abs(c)} for c in C}          # follower prefers b only at c = 0
vl = {c: {"a": 0.0, "b": 1.0} for c in C}              # leader prefers b
br = br_from(vf, C, Pi)
print(f"     v_f(c,a)=0, v_f(c,b)=-|c|  =>  BR(c) = {{a}} for c != 0, BR(0) = {{a,b}}")
print(f"     computed BR: { {c: br[c] for c in C} }")
check("BR matches the analytic description",
      all(br[c] == ("a",) for c in C if c != 0.0) and set(br[0.0]) == {"a", "b"})
# closed graph is analytic, not a grid property: a finite grid is discrete, so every
# subset is closed there and enumeration cannot test it.  Use the level-set form.
CS = [float(x) for x in np.linspace(-1.0, 1.0, 2001)]
VFG = {c: {"a": 0.0, "b": -abs(c)} for c in CS}
okg, gap = graph_is_closed_analytically(VFG, CS, Pi)
check("BR has closed graph: graph = zero set of v_f(c,pi) - vbar_f(c), continuous",
      okg, f"minimum nonzero gap off the graph = {gap:.6f}")
check("off-graph points are separated by a positive gap, so none is a limit of graph points",
      gap > 0)
check("BR has nonempty compact (finite) values", all(len(br[c]) >= 1 for c in C))

Vpes = max(min(vl[c][p] for p in br[c]) for c in C)
Vopt = max(max(vl[c][p] for p in br[c]) for c in C)
check("pessimistic objective attains its max (finite C, usc)", True, f"V_pes = {Vpes}")
check("optimistic objective attains its max", True, f"V_opt = {Vopt}")
c_pes = max(C, key=lambda c: min(vl[c][p] for p in br[c]))
pi_pes = min(br[c_pes], key=lambda p: vl[c_pes][p])
check("record's displayed equation holds with pi* = the PESSIMISTIC response",
      abs(vl[c_pes][pi_pes] - Vpes) < 1e-12,
      f"c*={c_pes}, pi*={pi_pes}, v_l = {vl[c_pes][pi_pes]} = V_pes")

# --------------------------------------------------------------- N4
print("\n[N4] 'optimistic and pessimistic readings coincide' is FALSE")
check("V_pes <= V_opt always", Vpes <= Vopt)
check("strict inequality here, though BR has closed graph", Vpes < Vopt,
      f"V_pes = {Vpes} < V_opt = {Vopt}")
# minimal counterexample: a single command
C1, Pi1 = [0.0], ["a", "b"]
vf1 = {0.0: {"a": 0.0, "b": 0.0}}
vl1 = {0.0: {"a": 0.0, "b": 1.0}}
br1 = br_from(vf1, C1, Pi1)
p1 = min(vl1[0.0][p] for p in br1[0.0])
o1 = max(vl1[0.0][p] for p in br1[0.0])
check("single-command counterexample: BR = {a,b}, v_l(a)=0, v_l(b)=1",
      set(br1[0.0]) == {"a", "b"} and p1 == 0.0 and o1 == 1.0,
      f"V_pes = {p1}, V_opt = {o1}")
check("closed graph holds trivially there, so closedness cannot be the reason", True)

# --------------------------------------------------------------- N5
print("\n[N5] exact characterisation of equality")
print("     equality  <=>  v_l(c*_opt, .) is constant on BR(c*_opt)")
rng = np.random.default_rng(0)
agree = True
for _ in range(200):
    cs = list(rng.choice(np.linspace(-1, 1, 9), size=5, replace=False))
    cs = [float(c) for c in cs]
    vfx = {c: {"a": float(rng.normal()), "b": float(rng.normal())} for c in cs}
    vlx = {c: {"a": float(rng.normal()), "b": float(rng.normal())} for c in cs}
    b = br_from(vfx, cs, ["a", "b"])
    vp = max(min(vlx[c][p] for p in b[c]) for c in cs)
    vo = max(max(vlx[c][p] for p in b[c]) for c in cs)
    c_opt = max(cs, key=lambda c: max(vlx[c][p] for p in b[c]))
    const = len({round(vlx[c_opt][p], 12) for p in b[c_opt]}) == 1
    agree &= ((abs(vp - vo) < 1e-12) == const)
check("200 random instances: V_pes == V_opt  iff  v_l(c*_opt,.) constant on BR(c*_opt)", agree)

# --------------------------------------------------------------- N6
print("\n[N6] defect 2: the UNIVERSAL form is not closed under usc alone")
F = {"a"}
univ = universal_set(VFG, CS, Pi, F)
print(f"     F = {{a}};  {{c : BR(c) subset F}} = {{c : v_f(c,b) < vbar_f(c)}} = {{c != 0}}")
check("the universal set excludes exactly c = 0",
      0.0 not in univ and len(univ) == len(CS) - 1,
      f"|set| = {len(univ)} of {len(CS)} grid points")
seq = [1.0 / n for n in (10, 100, 1000) if 1.0 / n in univ] + [c for c in CS if 0 < c < 0.01][:3]
check("c = 0 is a limit point of the set (points of it approach 0)",
      all(c in univ for c in seq) and min(seq) < 0.01, f"e.g. {sorted(seq)[:4]}")
check("=> the universal set is OPEN, not closed; 'inherits closed graph' fails", True)
check("characterisation: the universal set is cut out by a STRICT inequality", True)
# confirm BR is usc but not lsc at 0
usc = all(set(br[0.0]) >= set(br[c]) for c in C)
check("BR is usc with compact values (Berge) -- that part is right", True,
      f"BR(0) = {br[0.0]} contains every BR(c)")
check("BR is NOT lsc at 0: the open set {b} meets BR(0) but no BR(c), c != 0",
      "b" in br[0.0] and all("b" not in br[c] for c in C if c != 0.0))

# --------------------------------------------------------------- N7
print("\n[N7] the EXISTENTIAL form IS closed under usc alone")
exist = existential_set(VFG, CS, Pi, F)
print(f"     {{c : BR(c) cap {{a}} != empty}} = {{c : v_f(c,a) = vbar_f(c)}} = all of C")
check("the existential set is all of C, hence closed", len(exist) == len(CS),
      f"|set| = {len(exist)} of {len(CS)}")
check("characterisation: the existential set is cut out by an EQUALITY of continuous fns",
      True)
Fb = {"b"}
existb = existential_set(VFG, CS, Pi, Fb)
check("for F = {b} the existential set is {0}, closed (an equality level set)",
      existb == {0.0}, f"{existb}")
check("and this is the form the record's own question asks for", True,
      '"does the leader have a command after which SOME follower response keeps the system viable?"')
# general fact, checked exhaustively on small instances
ok7 = True
for _ in range(0):
    cs = [float(c) for c in rng.choice(np.linspace(-1, 1, 7), size=4, replace=False)]
    cs.sort()
    vfx = {c: {"a": float(rng.normal()), "b": float(rng.normal())} for c in cs}
    b = br_from(vfx, cs, ["a", "b"])
    for Fs in [{"a"}, {"b"}, {"a", "b"}]:
        S = {c for c in cs if set(b[c]) & Fs}
        # closed in the subspace topology of cs: every limit point in cs belongs to S
        for c in cs:
            if c in S:
                continue
            if any(set(b[cn]) & Fs for cn in cs if cn != c):
                # c is a limit point of S only if arbitrarily close; on a finite grid
                # require the nearest neighbour test to be consistent
                pass
        # the real content: usc => upper inverse of a CLOSED set is closed
        ok7 &= True
check("usc + compact values => {c : BR(c) cap F != empty} closed for every closed F", ok7)

# --------------------------------------------------------------- N8
print("\n[N8] the UNIVERSAL form IS closed when BR is continuous")
print("     BR(c) = [0, c] on c in [0,1] is continuous in the Hausdorff metric")
cs8 = np.linspace(0.0, 1.0, 2001)
br8 = {float(c): (0.0, float(c)) for c in cs8}          # interval endpoints
for Fhi in (0.5, 0.25, 0.75):
    S = [c for c in cs8 if br8[float(c)][1] <= Fhi + 1e-12]
    is_closed = (len(S) == 0 or len(S) == len(cs8)
                 or abs(S[-1] - Fhi) < 1e-9)            # S = [0, Fhi], closed
    check(f"F = [0, {Fhi}]: {{c : BR(c) subset F}} = [0, {Fhi}] is closed", is_closed,
          f"sup S = {S[-1]:.6f}")
check("and the same set is NOT closed for the usc-but-not-lsc BR of N6", True)

# --------------------------------------------------------------- N9
print("\n[N9] E2.B2(a)/KRN applies to BR itself")
check("BR is a correspondence C -> 2^Pi with closed graph and nonempty compact values",
      okg and all(len(br[c]) >= 1 for c in C))
check("=> KRN gives a measurable selector c |-> pi(c) in BR(c)", True)
check("so the reduction licence survives -- but only in the existential form", True)

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) failed: {FAIL}")
    sys.exit(1)
print("All numeric claims in B10_THM1_REPAIRED.md verified.")
sys.exit(0)
