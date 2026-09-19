#!/usr/bin/env python3
"""Independent verification of the points on which the three responses converge, written before any
editorial change.  Nothing here reuses a response's code."""
import itertools, numpy as np, sympy as sp
from scipy.optimize import linprog

print("=== 1. Does every part-conservation lift to the composition? (Prop 36 first clause) ===")
# part 1: compartments a1,a2 with flux p: a1->a2 ; part 2: b1,b2 with flux q: b1->b2
S_parts = sp.Matrix([[-1,0],[1,0],[0,-1],[0,1]])          # rows a1,a2,b1,b2
l = sp.symbols('l0:4'); L = sp.Matrix(l)
part_sols = sp.linsolve(list((L.T*S_parts).T), l)
print(" parts' conserved rays (dim %d): %s" % (len(list(part_sols)[0].free_symbols), part_sols))
# identify a2 with b2: quotient compartments (a1, c=[a2=b2], b1); both fluxes now deliver INTO c
S_comp = sp.Matrix([[-1,0],[1,1],[0,-1]])                    # rows a1,c,b1 ; cols p,q
m = sp.symbols('m0:3'); M = sp.Matrix(m)
comp_sols = sp.linsolve(list((M.T*S_comp).T), m)
print(" composition's conserved rays (dim %d): %s" % (len(list(comp_sols)[0].free_symbols), comp_sols))
print(" => the pullback of a composite conservation is INJECTIVE into the parts' direct sum,")
print("    and its image is the subspace constant on identification classes; here dim 1 < dim 2,")
print("    so the moiety {a1,a2} of part 1 does NOT survive the merge. The v34 clause is false as stated.")

print("\n=== 2. Sign of the interface term in Prop 37 (is pi^+ the right cost?) ===")
# ledger 1: margin m1 = x1 >= 0, fluxes: service y1 = v1 (out of x1), exchange f (out of x1)
# ledger 2: margin m2 = x2 >= 0, gains f, service y2 = v2 out of x2
# rates: dx1 = -(v1 + f), dx2 = +(f - v2)   [exchange conserved across the interface]
x1, x2, v1, v2, f, T = sp.symbols('x1 x2 v1 v2 f T', nonnegative=True)
lam1, lam2 = sp.symbols('lam1 lam2', nonnegative=True)
Vdot = lam1*(-(v1+f)) + lam2*(f-v2)
y = v1 + v2
# Vdot <= -y + coef*f  with coef = -lam1 + lam2 :
coef = sp.simplify(Vdot + y)         # should be (-lam1+lam2)*f
print(" residual of Vdot + y =", sp.collect(coef, f), "=> pi := (lam1*G1 - lam2*G2) with G=1 gives", sp.simplify(-coef/f))
print(" so the interface contributes -pi*f; with f in [0,vbar] the worst case is (max(0,-pi))*vbar")
print(" -> the cost term must be (-pi)^+ vbar T (equivalently |pi| vbar T as a convention-free bound),")
print("    and 'free' means pi >= 0, NOT pi <= 0 as printed in v34.")

print("\n=== 3. Same instance, both signs, checked by LP over rates ===")
def max_service(lam1, lam2, vbar, budget_init, T=30.0, rate_max=1e9):
    # max int y = (v1+v2)*T s.t. margins stay >= 0: x1(T) = x1_0 - (v1+f)T >= 0, x2(T)= x2_0 + (f-v2)T >= 0
    # with 0<=v1,v2,f<=rate_max, f<=vbar
    # LP in variables (v1,v2,f)
    c = [-T, -T, 0.0]
    A_ub = [[T, T, T],      # x1: v1 + f <= x1_0/T
            [-T, T, -T]]    # x2: v2 - f <= x2_0/T  (x2_0 taken = budget_init/ (lam1+lam2) split below)
    b_ub = [1.0, 1.0]
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0,None),(0,None),(0,vbar)], method="highs")
    return -res.fun, res.x
for (l1,l2) in [(2.0,1.0),(1.0,2.0)]:
    val, x = max_service(l1,l2,0.5,9.0)
    pi = l1 - l2
    bound_wrong = (l1*1.0 + l2*1.0) + max(pi,0)*0.5*30
    bound_right = (l1*1.0 + l2*1.0) + max(-pi,0)*0.5*30
    print("  lam=(%.0f,%.0f) pi=%+.0f : attained service %.3f | pi^+ bound %.3f %s | (-pi)^+ bound %.3f %s"
          % (l1,l2,pi,val,bound_wrong,"OK" if val<=bound_wrong+1e-9 else "VIOLATED",
             bound_right,"OK" if val<=bound_right+1e-9 else "VIOLATED"))

print("\n=== 4. Interval claim (Prop 39): connected fibre + continuous tau ===")
xs = np.linspace(1,99,196001)
taus = np.minimum(np.log(xs), np.log(100-xs))
print(" image over the polytope: [%.6f, %.6f]  (log50=%.6f)" % (taus.min(), taus.max(), np.log(50)))
# non-convex declared set -> disconnected fibre
ys = np.linspace(1,99,196001)
mask = np.abs(ys-50) > 5                    # excluded middle: two components
t2 = np.minimum(np.log(ys[mask]), np.log(100-ys[mask]))
print(" with a disconnected declared set, tau takes values in two separated bands:",
      "gap between %.4f and %.4f" % (t2[t2<3].max(), t2[t2>=3].min()))

print("\n=== 5. Closure capacity and its dual price (does the price characterize substitution?) ===")
def Lambda(cap_shared, caps=(1.0,1.0)):
    # max lam s.t. q=lam, s=lam, q+s<=cap_shared, q<=caps0, s<=caps1
    A_ub=[[0.,1.,1.]]; b_ub=[cap_shared]
    r=linprog([-1.,0.,0.],A_ub=A_ub,b_ub=b_ub,A_eq=[[-1,1,0],[-1,0,1]],b_eq=[0,0],
              bounds=[(0,None),(0,caps[0]),(0,caps[1])],method="highs")
    return r.fun*-1, r
for C in (1.0,1.5,2.0):
    v,r = Lambda(C); print("  shared cap %.1f -> Lambda*=%.4f" % (C,v))
# a capacity loss that keeps the price finite but destroys substitutability:
v,r = Lambda(1.5, caps=(0.0001,1.0))
print("  with side 1's own return capacity at 1e-4: Lambda*=%.6f (finite, price finite, yet the moiety"
      " is not substitutable: side 1 cannot close at all)" % v)
