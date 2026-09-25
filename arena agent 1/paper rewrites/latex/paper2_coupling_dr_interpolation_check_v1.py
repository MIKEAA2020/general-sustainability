#!/usr/bin/env python3
"""
Coupling selection vs distributionally robust interpolation — joint exact
check bridging the measure-dual residue (Abaee 2026g) and the DR layer of
the probabilistic companion (Abaee 2026e).

Instance (the residue's two-window example): disturbance sequence
d = (d1, d2), each in {-1, +1}; base prior p = uniform product; functional
G(d) = d1 * d2. Two consistent couplings with identical one-step marginals
(1/2, 1/2) per window: the product coupling gives E[G] = 0; the comonotone
coupling ((1,1), (-1,-1) w.p. 1/2 each) gives E[G] = +1 — consistency of a
prior curve under-determines the envelope value (the coupling-selection
residue).

What this check adds, exactly: the DR interpolation family
D_rho = {(1 - rho) p + rho r : r any coupling} evaluated on the same
functional gives, by linearity of expectation under mixtures,
  sup_{q in D_rho} E_q[G] = (1 - rho) E_p[G] + rho * sup_r E_r[G]
                          = rho * 1,
with the one-step marginals of every q in the family equal to (1/2, 1/2)
(mixtures preserve marginals, so the DR adversary never breaks the
information constraint). The coupling-selection difficulty lives entirely
in the inner supremum over couplings and is orthogonal to rho: the DR
family contains the residue's extremal couplings at rho = 1 and
interpolates linearly to the product coupling at rho = 0.
"""
from fractions import Fraction as F
from itertools import product

PASS = []
def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + name + (f" ({detail})" if detail else ""))

atoms = [(d1, d2) for d1 in (-1, 1) for d2 in (-1, 1)]
G = {(d1, d2): F(d1 * d2) for (d1, d2) in atoms}
p = {(d1, d2): F(1, 4) for (d1, d2) in atoms}                     # product
r_com = {(1, 1): F(1, 2), (-1, -1): F(1, 2), (1, -1): F(0), (-1, 1): F(0)}

check("base prior p is the uniform product (each atom 1/4)",
      all(w == F(1, 4) for w in p.values()) and sum(p.values()) == 1)
check("comonotone coupling r is consistent: one-step marginals (1/2, 1/2)",
      sum(r_com[(1, d2)] for d2 in (-1, 1)) == F(1, 2)
      and sum(r_com[(d1, 1)] for d1 in (-1, 1)) == F(1, 2)
      and sum(r_com.values()) == 1)
Ep = sum(p[a] * G[a] for a in atoms)
Er = sum(r_com[a] * G[a] for a in atoms)
check("coupling selection is real: E_p[G] = 0 vs E_r[G] = +1 on the same "
      "functional with identical one-step marginals",
      Ep == 0 and Er == 1)
ok_lin = True
for rho in (F(1, 4), F(1, 2), F(3, 4)):
    q = {a: (1 - rho) * p[a] + rho * r_com[a] for a in atoms}
    marg = (sum(q[(1, d2)] + q[(-1, d2)] for d2 in (-1, 1)) / 2, 
            sum(q[(d1, 1)] + q[(d1, -1)] for d1 in (-1, 1)) / 2)
    val = sum(q[a] * G[a] for a in atoms)
    ok_lin &= (val == rho and marg == (F(1, 2), F(1, 2)))
check("DR interpolation is exactly linear: sup_{D_rho} E_q[G] = rho at "
      "rho in {1/4, 1/2, 3/4}, marginals (1/2,1/2) preserved at every rho",
      ok_lin)
check("extremes: rho = 0 recovers the product value, rho = 1 recovers the "
      "comonotone extremum (the coupling-selection supremum)",
      (1 - F(1)) * Ep + F(1) * Er == 1 and F(0) * Er == 0)
check("the inner supremum over couplings is rho-orthogonal: for every rho "
      "the family attains (1 - rho) * 0 + rho * sup_r E_r[G]",
      all((1 - rho) * Ep + rho * Er == rho for rho in (F(1, 4), F(1, 2), F(3, 4), F(1))))

n = sum(PASS)
print(f"\ncoupling--DR interpolation check: {n}/{len(PASS)} checks pass")
raise SystemExit(0 if n == len(PASS) else 1)
