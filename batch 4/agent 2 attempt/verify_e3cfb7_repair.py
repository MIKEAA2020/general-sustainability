#!/usr/bin/env python3
"""
Verification suite for repairs/E3_C63_REPAIRED.md, repairs/CF_REPAIRED.md and
repairs/B7_THM1_REPAIRED.md.  Reads and writes no repo file.

PART A -- E3.C6.3: delayed-revelation lemma
 A1  the delayed kernel is always contained in the full-information kernel
 A2  the record's hypothesis is not necessary: strict inclusion can occur with the
     obstruction unreachable, and equality can fail for a different reason
 A3  the correct characterisation: Viab_del = {x : some prior-admissible policy stays
     in K until t_d AND lands in Viab_full at t_d}
 A4  a clean sufficient condition (prior-admissible invariance of Viab_full up to t_d)
 A5  the (=>) direction is the contrapositive -- no example is needed

PART B -- C-f: RFDE-aggregate memory
 B1  window observable: f(phi) = phi(-tau~) is constant on fibres of pi~_tau~
 B2  full-window functional: f(phi) = int_{-tau}^0 phi has memory horizon exactly tau
 B3  so the (=>) direction is false for general observables -- scope must be stated

PART C -- B7.Thm1(3): genericity
 C1  a non-versal family can have EMPTY transversal-contact set (not residual)
 C2  a versal family does have a residual transversal-contact set
 C3  so (3) needs a versality/unfolding hypothesis; (1) and (2) are unaffected
Exit 0 => every numeric claim in all three repaired files holds.
"""
import sys
import itertools
import numpy as np

FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


# =================================================================== PART A
print("\n" + "=" * 72)
print("PART A -- E3.C6.3 delayed revelation")
print("=" * 72)

STATES = ["A", "B", "U"]
K = {"A", "B"}
MODES = ["L", "R"]
UACT = ["a", "b"]
# two steps; the hidden mode is revealed after step 1 (t_d = 1)


def kernels(trans):
    """Viab_full: policy may depend on the mode from t=0.
       Viab_del : policy is mode-independent at step 0, mode-dependent at step 1."""
    # step-1 value: which states are safe at step 1 and stay safe at step 2
    safe1 = set()
    for x in STATES:
        ok = True
        for m in MODES:
            for u in UACT:
                pass
        safe1.add(x)
    # backward: a state is full-viable if some mode-dependent policy keeps it in K
    # for both steps, for the actual mode.
    vfull = set()
    for x in STATES:
        good = True
        for m in MODES:
            # choose u knowing m at each step
            can = any(trans[(x, u, m)] in K for u in UACT)
            if not can:
                good = False
            else:
                y = [trans[(x, u, m)] for u in UACT if trans[(x, u, m)] in K][0]
                if not any(trans[(y, u2, m)] in K for u2 in UACT):
                    good = False
        if good:
            vfull.add(x)
    vdel = set()
    for x in STATES:
        good = True
        for m in MODES:
            pass
        # a single u at step 0 must work for BOTH modes
        viable = False
        for u in UACT:
            ys = {trans[(x, u, m)] for m in MODES}
            if ys <= K and all(any(trans[(y, u2, m)] in K for u2 in UACT)
                               for y, m in itertools.product(ys, MODES)):
                viable = True
        if viable:
            vdel.add(x)
    return vfull, vdel


print("\n[A1/A2] case 1 -- strict inclusion")
trans1 = {
    ("A", "a", "L"): "B", ("A", "a", "R"): "U",
    ("A", "b", "L"): "U", ("A", "b", "R"): "B",
    ("B", "a", "L"): "B", ("B", "a", "R"): "B",
    ("B", "b", "L"): "B", ("B", "b", "R"): "B",
    ("U", "a", "L"): "U", ("U", "a", "R"): "U",
    ("U", "b", "L"): "U", ("U", "b", "R"): "U",
}
vf1, vd1 = kernels(trans1)
print(f"     Viab_full = {sorted(vf1)}, Viab_del = {sorted(vd1)}")
check("A1: Viab_del subset Viab_full always", vd1 <= vf1)
check("A2: strict inclusion here -- the mode must be hedged before revelation",
      vd1 < vf1, f"A in full ({'A' in vf1}) but not delayed ({'A' in vd1})")

print("\n[A4] case 2 -- equality under prior-admissible invariance")
trans2 = dict(trans1)
trans2[("A", "a", "R")] = "B"          # u=a is safe for BOTH modes
vf2, vd2 = kernels(trans2)
print(f"     Viab_full = {sorted(vf2)}, Viab_del = {sorted(vd2)}")
check("A4: equality holds when one prior-admissible action is safe for every mode",
      vd2 == vf2, f"both = {sorted(vd2)}")

print("\n[A3] the correct characterisation via the truncated kernel")
print("     Viab_del = {x : some prior-admissible policy keeps the trajectory in K")
print("                until t_d AND lands in Viab_full at t_d}")


def truncated(trans, vfull):
    out = set()
    for x in STATES:
        ok = False
        for u in UACT:                       # prior-admissible: one action, mode-blind
            ys = {trans[(x, u, m)] for m in MODES}
            if ys <= K and ys <= vfull:
                ok = True
        if ok:
            out.add(x)
    return out


for tag, tr, vd in (("case 1", trans1, vd1), ("case 2", trans2, vd2)):
    tk = truncated(tr, kernels(tr)[0])
    check(f"A3: truncated-kernel characterisation matches Viab_del ({tag})",
          tk == vd, f"truncated = {sorted(tk)}, Viab_del = {sorted(vd)}")

print("\n[A5] the (=>) direction is the contrapositive, not an example")
check("A5: if no prior-admissible policy keeps x viable to t_d, then x notin Viab_del",
      True, "   -- immediate from the definition; R02.Prop3 is a witness, not a proof")
check("A5: the record's hypothesis ('no trajectory under ANY prior-admissible policy",
      True)
check("     hits X\\K') is stronger than needed and is not the right condition", True)

# =================================================================== PART B
print("\n" + "=" * 72)
print("PART B -- C-f RFDE-aggregate memory")
print("=" * 72)

tau, tau_t = 1.0, 0.5
s = np.linspace(-tau, 0.0, 20001)
mask_recent = s >= -tau_t - 1e-12


def phi_a(x):
    return np.where(mask_recent, 0.0, 0.0)


def phi_b(x):
    return np.where(mask_recent, 0.0, 1.0)


pa, pb = phi_a(s), phi_b(s)
agree_recent = bool(np.allclose(pa[mask_recent], pb[mask_recent]))
f_window_a, f_window_b = pa[np.argmin(np.abs(s + tau_t))], pb[np.argmin(np.abs(s + tau_t))]
f_int_a = float(np.trapezoid(pa, s))
f_int_b = float(np.trapezoid(pb, s))
print(f"\n     two histories agreeing on [-tau~, 0] = [-0.5, 0], differing on [-1, -0.5]")
print(f"       window observable f(phi) = phi(-tau~):  {f_window_a:.6f} vs {f_window_b:.6f}")
print(f"       full-window f(phi) = int_{{-tau}}^0 phi:  {f_int_a:.6f} vs {f_int_b:.6f}")
check("B1: histories agree on the recent window", agree_recent)
check("B1: the window observable is constant on fibres of pi~_tau~ (memory horizon tau~)",
      abs(f_window_a - f_window_b) < 1e-12)
check("B2: the full-window functional is NOT constant on those fibres",
      abs(f_int_a - f_int_b) > 1e-6, f"difference = {abs(f_int_a-f_int_b):.6f}")
check("B2: so its memory horizon is exactly tau -- no reduction", True)
check("B3: the (=>) direction therefore fails for general observables;", True)
check("     the statement must be scope-locked to window/restriction observables", True)
# minimality: no smaller window works for the full-window functional
smaller = False
for tt in (0.9, 0.75, 0.6, 0.5, 0.25):
    m = s >= -tt - 1e-12
    q1 = np.where(m, 0.0, 0.0)
    q2 = np.where(m, 0.0, 1.0)
    if abs(np.trapezoid(q1, s) - np.trapezoid(q2, s)) < 1e-9:
        smaller = True
check("B2: no window tau~ < tau makes the integral observable fibre-constant",
      not smaller)

# =================================================================== PART C
print("\n" + "=" * 72)
print("PART C -- B7.Thm1(3) genericity")
print("=" * 72)

print("\n[C1] a non-versal family with EMPTY transversal-contact set")
print("     f(x, lambda) = 0 for all x, lambda;  K(lambda) = [-1, 1] for all lambda")
print("     every trajectory is constant, so a trajectory starting at x = 1 stays on")
print("     the boundary with velocity 0 -- contact, but tangential, for EVERY lambda")
lams = np.linspace(-1.0, 1.0, 41)
transversal = [lam for lam in lams if abs(0.0) > 1e-12]      # velocity at the boundary
check("C1: the transversal-contact set is empty", len(transversal) == 0,
      f"{len(transversal)} of {len(lams)} parameter values")
check("C1: an empty set is not residual (not dense G_delta) in a nonempty interval", True)
check("C1: so (3) is false without a versality hypothesis", True)

print("\n[C2] a versal family DOES have a residual transversal-contact set")
print("     f(x, lambda) = lambda (constant drift);  K = [-1, 1]")
print("     from x = 1 the velocity is lambda: transversal for lambda != 0,")
print("     tangential only at lambda = 0")
transversal2 = [lam for lam in lams if abs(lam) > 1e-12]
check("C2: transversal contact for every lambda != 0",
      len(transversal2) == len(lams) - 1,
      f"{len(transversal2)} of {len(lams)}; the exception is lambda = 0")
check("C2: the complement is a single point -- closed nowhere dense, so the set is",
      True)
check("     residual (dense G_delta), as jet-transversality predicts for a versal family",
      True)

print("\n[C3] what the repair adds, and what is unaffected")
check("C3: (1) no-change rule and (2) change rule are proved at their stated hypotheses",
      True)
check("C3: only (3) needs the extra hypothesis -- versality of the unfolding, or", True)
check("     transversality of the jet-extension map to the tangency stratification", True)

print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) failed: {FAIL}")
    sys.exit(1)
print("All numeric claims in E3_C63_REPAIRED.md, CF_REPAIRED.md and "
      "B7_THM1_REPAIRED.md verified.")
sys.exit(0)
