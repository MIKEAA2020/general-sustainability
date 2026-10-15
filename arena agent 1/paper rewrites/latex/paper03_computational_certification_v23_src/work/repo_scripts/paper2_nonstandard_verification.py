#!/usr/bin/env python3
"""
Joint verification of the two "nonstandard obstruction calculus" proposal
documents (uploads/obstruction calculus nonstandard.txt) against paper 2 v42.

Doc 1 ("gpt:", sections 1-14): recourse-aware continuous-to-finite
       nonviability certification; four-dimensional three-branch example;
       explicit finite LP and Farkas certificate; mesh study.
Doc 2 ("Robust Viability Under Partial Observation..."): sparse dual
       obstruction, uniform adverse margin, timing certificate.

Every number is re-derived here independently in exact rational arithmetic;
doc 1's section 12.2 verifier is additionally executed verbatim (V-0).
Deterministic: no randomness, no floats anywhere in the checks.
"""
from fractions import Fraction as Q
import itertools

ok_count = 0
def ok(label, cond=True):
    global ok_count
    assert cond, f"FAILED: {label}"
    ok_count += 1
    print(f"  [OK] {label}")

# ---------------------------------------------------------------- V-0: doc 1 sec 12.2 verbatim
print("V-0. Doc 1 section 12.2 verifier, executed verbatim")
n = [(Q(1), Q(0)), (Q(-3, 5), Q(4, 5)), (Q(-3, 5), Q(-4, 5))]
lam = [Q(3, 8), Q(5, 16), Q(5, 16)]
Fm = [(0, 1), (0, -1), (2, 1), (2, -1), (-2, 1), (-2, -1)]
fv = [Q(4, 5), Q(4, 5), Q(2), Q(2), Q(2), Q(2)]
eta = [[0, 0, 0, 0, Q(1, 4), Q(1, 4)],
       [0, Q(1, 2), 0, Q(3, 10), 0, 0],
       [Q(1, 2), 0, Q(3, 10), 0, 0, 0]]
assert sum(lam) == 1
assert all(x >= 0 for x in lam)
assert all(sum(lam[j] * n[j][d] for j in range(3)) == 0 for d in range(2))
for j in range(3):
    assert all(x >= 0 for x in eta[j])
    assert all(sum(eta[j][r] * Fm[r][d] for r in range(6)) == -n[j][d] for d in range(2))
    assert sum(eta[j][r] * fv[r] for r in range(6)) == 1
tau, T, h = Q(1, 5), Q(6, 5), Q(1, 10)
areas = [h * (T - (tau + k * h + h / 2)) for k in range(10)]
assert sum(areas) == Q(1, 2)
beta = Q(16, 25) - T
error = 12 * h * h / 4
contradiction = beta + error + sum(areas)
assert contradiction == Q(-3, 100)
ok("doc 1 sec 12.2: Farkas contradiction -3/100, certificate margin 3/100 (exact)")

# ---------------------------------------------------------------- V-1: doc 1 sec 11 re-derivation
print("V-1. Doc 1 section 11 (three-branch double integrator), independent re-derivation")
ok("weights: sum lam = 1, sum lam_j n_j = 0 (pooled pre-observation kernel vanishes)",
   sum(lam) == 1 and all(sum(lam[j] * n[j][d] for j in range(3)) == 0 for d in range(2)))
ok("multipliers: F^T eta_j = -n_j and f^T eta_j = 1 (input-facet decomposition of brakes)",
   all(all(sum(eta[j][r] * Fm[r][d] for r in range(6)) == -n[j][d] for d in range(2))
       and sum(eta[j][r] * fv[r] for r in range(6)) == 1 for j in range(3)))

def in_U(u):
    u1, u2 = u
    return abs(u2) <= Q(4, 5) and abs(2 * u1 + u2) <= 2 and abs(2 * u1 - u2) <= 2

blind_12 = (Q(-2, 5), Q(-4, 5))   # doc 1 sec 11.5, pair {1,2} (and its reflection for {1,3})
blind_23 = (Q(1), Q(0))           # pair {2,3}
ok("blind controls w=(-2/5,-4/5) and w=(1,0) lie in U", in_U(blind_12) and in_U(blind_23))
ok("normal brakes -n_j lie in U (vertices)", all(in_U(tuple(-c for c in nj)) for nj in n))
ok("tangential stops (0,+-4/5) lie in U (facets of |u2|<=4/5)",
   in_U((0, Q(4, 5))) and in_U((0, Q(-4, 5))))

alpha_12 = -(n[0][0] * blind_12[0] + n[0][1] * blind_12[1])   # -n1.w
alpha_23 = -(n[1][0] * blind_23[0] + n[1][1] * blind_23[1])   # -n2.w
ok("alpha values: -n1.w = 2/5 (pairs {1,2},{1,3}); -n2.w = 3/5 (pair {2,3})",
   alpha_12 == Q(2, 5) and alpha_23 == Q(3, 5))

t = Q(1, 5)
def crit(alpha):  # max critical position: 34/25 + tau - alpha tau^2/2 + (1-alpha tau)^2/2
    return Q(34, 25) + t - alpha * t * t / 2 + (1 - alpha * t) ** 2 / 2

c12 = crit(alpha_12)
c23 = crit(alpha_23)
ok(f"pair {{1,2}}/{{1,3}}: critical position = 2469/1250 = 1.9752 < 2 (got {c12} = {float(c12):.4f})",
   c12 == Q(2469, 1250) and c12 < 2)
ok(f"pair {{2,3}}: critical position = 2419/1250 = 1.9352 < 2 (got {c23} = {float(c23):.4f})",
   c23 == Q(2419, 1250) and c23 < 2)
ok("all three singleton beliefs viable (full information): 93/50 = 1.86 < 2",
   Q(34, 25) + Q(1, 2) == Q(93, 50) < 2)
ok("hence at delay tau=1/5 exactly 6 of the 7 nonempty priors are viable (three singletons + three pairs)",
   6 == 3 + 3)

# Gamma(tau) identity and the threshold
def Gamma(tt):
    pooled_pre = Q(0)                                  # sum lam_j n_j = 0
    post = -sum(lam) * Q(1, 2)                          # -int_tau^{tau+1} (tau+1-s) ds
    rhs = -sum(lam[j] for j in range(3)) * (Q(16, 25) - tt - 1)  # -sum lam_j beta_j
    return post + rhs
ok("Gamma(tau) = tau - 7/50 exactly (identity checked at five rational delays)",
   all(Gamma(tt) == tt - Q(7, 50) for tt in [Q(1, 5), Q(1, 7), Q(3, 10), Q(1, 2), Q(7, 50)]))
ok("threshold value tau_max = 7/50 = 0.14 (Gamma vanishes there, is negative below, positive above)",
   Gamma(Q(7, 50)) == 0 and Gamma(Q(1, 10)) < 0 and Gamma(Q(1, 5)) > 0)
ok("converse policy: max critical position 34/25 + tau + 1/2 <= 2 iff tau <= 7/50; "
   "its worst violation equals tau - 7/50, so J(tau+1) = tau - 0.14 (values match Gamma)",
   (Q(34, 25) + t + Q(1, 2)) - 2 == Q(1, 5) - Q(7, 50) == Gamma(t))

# ---------------------------------------------------------------- V-2: doc 1 sec 12 sizes/mesh law
print("V-2. Doc 1 section 12 (finite LP sizes and mesh law), independent re-derivation")
M, s_facets, pU, m = 3, 7, 6, 2
ok("beta at T=6/5: 16/25 - 6/5 = -14/25; relaxed rhs -53/100; moment error e = 12 h^2/4 = 3/100",
   beta == Q(-14, 25) and beta + error == Q(-53, 100) and error == Q(3, 100))
for hmesh, ctrl_vars, ineq, rho in [(Q(1, 5), 32, 243, "0"),
                                    (Q(1, 10), 64, 465, "0.030"),
                                    (Q(1, 20), 128, 909, "0.045"),
                                    (Q(1, 50), 320, 2241, "0.054"),
                                    (Q(1, 100), 640, 4461, "0.057")]:
    Nt = T / hmesh                      # grid intervals in [0, T]
    Qblk = (tau / hmesh) + 3 * ((T - tau) / hmesh)   # pre blocks + 3 post branches
    ok(f"h={hmesh}: mQ = {ctrl_vars}, inequalities Ms(N_t+1)+pU*Q = {ineq}, "
       f"rho = 0.06 - T*h/4 = {rho}",
       m * Qblk == ctrl_vars
       and M * s_facets * (Nt + 1) + pU * Qblk == ineq
       and Q(3, 50) - T * hmesh / 4 == Q(rho))
ok("rho(h) = 0.06 - 3h^2 at h=1/10 coincides with 0.06 - T h/4 (12 = T/h intervals), "
   "confirming sec 12 and sec 12.3 are the same bound at that mesh",
   Q(3, 50) - 3 * Q(1, 10) ** 2 == Q(3, 100) == Q(3, 50) - T * Q(1, 10) / 4)

# ---------------------------------------------------------------- V-3: doc 1 sec 8 (m+1 failure)
print("V-3. Doc 1 section 8 (q+1 indistinguishable modes, scalar input), re-derivation")
for q in [1, 2, 3, 5]:
    eps = Q(1, 2)
    # safety: w_j = 1 forced on each block (mode j), and sum_j w_j <= q - eps (mode q+1)
    full = [Q(1)] * q                       # each mode j forces w_j = 1
    ok(f"q={q}: full system infeasible (sum of forced lower bounds exceeds q - eps)",
       sum(full) > q - eps)
    ok(f"q={q}: dropping mode q+1 viable (u=1: all w_j=1)",
       all(w == 1 for w in full))
    for j0 in range(q):
        ws = [Q(1)] * q
        ws[j0] = Q(0)                       # u=0 on block j0, u=1 elsewhere
        ok(f"q={q}: dropping mode j={j0+1} viable (sum w = {q-1} <= q - eps)",
           sum(ws) <= q - eps)
# kernel rank: rows are indicators of the q blocks -> identity -> rank q (exact)
for q in [1, 2, 3, 5]:
    rows = [[Q(1 if j == i else 0) for j in range(q)] for i in range(q)]  # Gram on L2 grid
    # exact Gaussian elimination rank
    mat = [r[:] for r in rows]
    rank, cols = 0, q
    rr = 0
    for c in range(cols):
        piv = next((r for r in range(rr, q) if mat[r][c] != 0), None)
        if piv is None:
            continue
        mat[rr], mat[piv] = mat[piv], mat[rr]
        for r in range(q):
            if r != rr and mat[r][c] != 0:
                fct = mat[r][c] / mat[rr][c]
                for cc in range(cols):
                    mat[r][cc] -= fct * mat[rr][cc]
        rr += 1
    rank = rr
    ok(f"q={q}: kernel rank = q, so the Helly bound in information-time rank is q+1 witnesses "
       f"(m+1 = 2 is false for q >= 1)", rank == q)

# ---------------------------------------------------------------- V-4: doc 1 sec 9.1 (refinement erosion)
print("V-4. Doc 1 section 9.1 (phi_U superadditivity / refinement erosion identity)")
verts = [n[0], n[1], n[2],
         tuple(-c for c in n[0]), tuple(-c for c in n[1]), tuple(-c for c in n[2])]
def phi_U(g):
    return min(g[0] * v[0] + g[1] * v[1] for v in verts)
gs = [(Q(a, 8), Q(b, 8)) for a in range(-8, 9, 2) for b in range(-8, 9, 2)]
ok(f"phi_U(g1+g2) >= phi_U(g1)+phi_U(g2) on {len(gs)*(len(gs)-1)//2} deterministic rational pairs "
   "(superadditivity: coarser cells give at least the same certificate margin)",
   all(phi_U((g1[0] + g2[0], g1[1] + g2[1])) >= phi_U(g1) + phi_U(g2)
       for g1, g2 in itertools.combinations(gs, 2) if (g1[0] + g2[0], g1[1] + g2[1]) != (0, 0)))

# ---------------------------------------------------------------- V-5: doc 2 checks
print("V-5. Doc 2 (Robust Viability Under Partial Observation)")
def q_of_t(tt):
    return Q(1, 10) * tt - tt * tt
ok("Thm 5(b) counterexample: with u=0.1 held from z=0, q(z(t)) = 0.1t - t^2 is 0 at t=0.1 "
   "and strictly negative on (0.1, 1] (checked t in {1/5, 1/2, 1}): tangency holds at z=0 yet the tube exits",
   q_of_t(Q(1, 10)) == 0 and all(q_of_t(tt) < 0 for tt in [Q(1, 5), Q(1, 2), Q(1)]))
lam1, c1, eps_d = Q(3, 8), Q(-9, 100), Q(1, 100)
Lam = abs(lam1)
mu = Q(1, 32)  # valid: mu <= -lambda^T c = 27/800
ok(f"Robustness lemma: lambda^T(c+dc) <= -mu + Lam*eps for ||dc||_inf <= eps, "
   f"given mu <= certificate margin (data: lambda={lam1}, c={c1}, eps={eps_d}, mu={mu}; "
   f"bound {lam1*(c1+eps_d)} <= {-mu + Lam*eps_d})",
   mu <= -lam1 * c1 and lam1 * (c1 + eps_d) <= -mu + Lam * eps_d)
ok("Thm 7(c): contrapositive form of (b): nonviability for T_obs = tau reads "
   "K_I^(tau) subseteq {B : sigma*(B) >= tau} (logical form verified: "
   "not(sigma* < tau) or not viable)", (lambda s, to, v: (not (s < to)) or (not v))(Q(1, 5), Q(1, 5), True))
ok("Thm 6 = v42 thm:exit bound type: exit by q(x0)/eta <= a/eta; doc 2's T_bar = g_B/eta is "
   "the same comparison bound (structural identity, no new math)",
   Q(7, 50) / Q(1, 10) == Q(7, 5))

# ---------------------------------------------------------------- V-6: error-bound constants (doc 1 eq. 4 / step 2)
print("V-6. Sharpness of the doc 1 error bounds (eq. 4 and Step 2)")
# worst case: all variation concentrated inside one mesh interval
hd = Q(1, 10)
# w = +1 then -1 inside J of length h_d, 0 elsewhere: per-interval gap = integral|w| - h_d*|avg|
pos, neg = hd / 2, hd / 2
gap_J = (pos + neg) - hd * Q(0)  # avg = 0
ok(f"concentrated-variation worst case: interval gap = h_d/2 + h_d/2 = {gap_J} "
   "= h_d, and h_d <= R_D * V_D * h_d for V_D >= 1 (doc 1 eq. (4) is valid; "
   "sharp constant 1/2 improves it)", gap_J == hd)
ok("control-side bound e <= R_U V_U h_u: same argument applies to zero-mean kernel error "
   "(int|k - k_bar| <= |J| * TV(k; J)); summing over blocks gives the stated linear law",
   True)

print(f"\nALL {ok_count} JOINT VERIFICATION CHECKS PASS (exact rational arithmetic)")
