"""Verify the continuous benchmark of paper2_worked_systems_v17 (section: benchmark)
as the worked case for paper 1. Exact rational arithmetic, standard library only.

System: state (x1,x2) >= 0, aggregate Y = x1 + x2, Y-fibre = all states with that
aggregate -- a CONTINUUM of states. Demand floor: allocation u >= 0 with u1+u2 >= 2.
Y-dependent caps:
    cap1(Y) = 3/2  - (Y-2)/10
    cap2(Y) = 59/50 - (Y-2)/10
u is feasible on the fibre iff u_i <= cap_i(Y).

Claim (prop:bench): the Y-fibre admits a feasible input iff cap1(Y)+cap2(Y) >= 2,
iff Y <= 27/5. For Y >= 27/5 the dual measure (1/2,1/2) certifies the obstruction
with exact margin  (2 - cap1 - cap2)/2 = (Y - 27/5)/10.
"""
from fractions import Fraction as F

def cap1(Y): return F(3, 2) - (Y - 2) / 10
def cap2(Y): return F(59, 50) - (Y - 2) / 10

print("=" * 74)
print("1. CAP ARITHMETIC AT THE AUDITED AGGREGATES")
for Y in (F(4), F(9, 2), F(5), F(27, 5), F(6)):
    s = cap1(Y) + cap2(Y)
    print("   Y=%-5s cap1=%-7s cap2=%-7s sum=%-8s %s"
          % (Y, cap1(Y), cap2(Y), s, "ABOVE 2 -> viable" if s >= 2 else "BELOW 2 -> OBSTRUCTED"))

print()
print("=" * 74)
print("2. CRITICAL AGGREGATE: cap sum == 2 exactly where?")
# cap sum = 67/25 - (Y-2)/5 ; solve = 2
Ystar = 2 + 5 * (F(67, 25) - 2)
print("   closed form Y* = 2 + 5*(67/25 - 2) =", Ystar, " = 27/5 ?", Ystar == F(27, 5))
print("   cap sum at Y* =", cap1(Ystar) + cap2(Ystar), "(should be exactly 2)")

print()
print("=" * 74)
print("3. THE DUAL-MEASURE CERTIFICATE")
lam = (F(1, 2), F(1, 2))          # l1-normalized dual measure on the two cap rows
for Y in (F(5), F(27, 5), F(6), F(7), F(10)):
    s = cap1(Y) + cap2(Y)
    margin = (2 - s) / 2
    formula = (Y - F(27, 5)) / 10
    # dual bound: lambda^T (cap - u) <= (cap sum)/2 - 1 for every u in U
    bound = s / 2 - 1
    ok = (margin == formula)
    print("   Y=%-4s capsum=%-8s margin=%-8s (Y-27/5)/10=%-8s match=%s  dual bound=%s"
          % (Y, s, margin, formula, ok, bound))

print()
print("=" * 74)
print("4. VERIFY THE TWO EXPLICIT FIBRES")
Y = F(5)
w = (F(6, 5), F(4, 5))            # claimed witness
print("   Y=5 fibre: witness u =", w)
print("     u1+u2 =", w[0] + w[1], ">= 2 ?", w[0] + w[1] >= 2)
print("     u1 <= cap1 ?", w[0], "<=", cap1(Y), w[0] <= cap1(Y))
print("     u2 <= cap2 ?", w[1], "<=", cap2(Y), w[1] <= cap2(Y))
print("     -> VIABLE" if (w[0] + w[1] >= 2 and w[0] <= cap1(Y) and w[1] <= cap2(Y)) else "     -> NOT viable")
Y = F(6)
print("   Y=6 fibre: cap sum =", cap1(Y) + cap2(Y), "< 2 ?", cap1(Y) + cap2(Y) < 2)
print("     obstruction margin =", (2 - (cap1(Y) + cap2(Y))) / 2, "= 3/50 ?",
      (2 - (cap1(Y) + cap2(Y))) / 2 == F(3, 50))
print("     -> OBSTRUCTED, certified by dual measure (1/2,1/2)")

print()
print("=" * 74)
print("5. THE HALF-LINE: exact for every Y >= 27/5")
bad = []
for k in range(0, 200):
    Y = F(27, 5) + F(k, 4)
    s = cap1(Y) + cap2(Y)
    if s >= 2 - F(1, 10**9) and Y > F(27, 5):
        bad.append(Y)
    if abs(((2 - s) / 2) - ((Y - F(27, 5)) / 10)) > 0:
        bad.append(("margin mismatch", Y))
print("   checked Y = 27/5 + k/4 for k=0..199")
print("   violations:", bad if bad else "NONE -- crossover exact on the whole half-line")

print()
print("=" * 74)
print("6. WHY THIS IS A WORKED CASE FOR THE GAP")
print("""   The Y-fibre is a CONTINUUM: every (x1,x2) >= 0 with x1+x2 = Y. The kernel
   question on such a fibre is not a finite computation -- there is no finite
   object to enumerate. Yet the certificate is two rationals (the dual measure)
   and one rational inequality, and it is EXACT: it holds for every Y >= 27/5
   with margin (Y - 27/5)/10, verified above in exact arithmetic.

   Scope, stated honestly: this section audits FIBRE FEASIBILITY, not the full
   transition dynamics. So what is certified is a static obstruction on the
   fibre, not the full dynamic epistemic kernel. That is exactly the strength
   of prop:bench and it should be stated that way, not overclaimed.""")
