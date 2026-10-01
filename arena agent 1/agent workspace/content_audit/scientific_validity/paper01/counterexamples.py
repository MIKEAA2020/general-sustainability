#!/usr/bin/env python3
"""Independent exact-arithmetic checks against paper01 v63 as WRITTEN.

Not a verifier of the full manuscript. Run: python3 counterexamples.py.
Only the 48-cell class comparison, an LP-example check, and two minimal
counterexamples are established here.
"""
from fractions import Fraction as F
from itertools import product

# Main §9: z[k+1]=z[k]+theta*u[k], two hidden regimes, floor z>=1.
def survives(z0, seq):
    for theta in (-1, 1):
        z = z0
        for u in seq:
            z += theta*u
            if z < 1:
                return False
    return True

held_nonviable = open_nonviable = disagreements = 0
for T in (1, 2, 3):
    for i in range(10, 26):
        z0 = F(i, 10)
        held = any(survives(z0, (u,)*T) for u in (-1,1))
        sequential = any(survives(z0, seq) for seq in product((-1,1), repeat=T))
        held_nonviable += not held
        open_nonviable += not sequential
        disagreements += held != sequential
        assert not held or sequential
        assert sequential == (z0 >= 2), (T,z0)
assert (held_nonviable, open_nonviable, disagreements) == (42,30,12)
seq=(1,-1,1)
assert survives(F(2),seq)
print('§9 grid: held nonviable 42/48; unrestricted in-window time-varying nonviable 30/48; 12 false nonviability cells if unrestricted')
print('§9 explicit policy: z0=2, Tobs=3, u=(+1,-1,+1) gives both branches z>=1')

# §3.3 Example 'relaxation gap': z[k+1]=9z[k]/10 + theta*u[k].
z0=F(2); theta=-1;u=1
worst=F(9,10)*z0+theta*u
assert worst==F(4,5)<1
relaxed=F(9,10)*z0
assert relaxed==F(9,5)>=1 and F(9,10)**7*z0<1
print('§3.3 decaying model: z0=2, finite +/-1 fails at step 1 (worst=4/5), unlike claimed sigma*=z0-1=1; u=0 also exits by step 7')

# §3.7 recourse proposition: f(x,u)=-1+x*u, q=x-1, U=[-1,1],
# B0={1,2}, both branches have constant uninformative observation, T=1,
# tau=1/2, D singleton. Store only the x0=1 label (weight 1; zero weights
# on any other labels are allowed). X_f0(t,s)=1, xbar(s)=1-s on that branch.
# beta=q(xbar(T))=-1, k(s)=xbar(s)=1-s.
# h_U(k)=abs(k)=1-s, integral 0..1=1/2; Gamma_h=-1/2.
beta=F(-1)
int0tau=F(1,2)-F(1,8)  # integral_0^{1/2} (1-s) ds = 3/8
inttau1=F(1,8)
gamma=beta+int0tau+inttau1
assert gamma==F(-1,2)
# Actual control u=+1 has x(t)=1+(x0-1)*exp(t): the first branch
# stays at 1 and the second (x0=2) stays >=2, both safe for all time.
assert -1+1*1==0 and -1+2*1==1
print('§3.7 control-affine B(x)=x: Gamma_h=-1/2<0 using a label from x0=1, while u=+1 keeps both x0=1 and x0=2 branches safe for all t')

# §10 degenerate proposition: B={s}, b(s)=1, D={good,bad}; F(s,a,
# good)=s, F(s,a,bad)=bottom, T(good)=99/100, T(bad)=1/100.
# Robust W_1 excludes B, but stochastic POMDP V_1=99/100 > 1-min b=0.
vgood=F(99,100);bad=1-vgood
assert bad>0 and vgood>0
print('§10 support-only stochastic transition: W_1 excludes singleton B, yet V_1=99/100 > 1-min_x b(x)=0')
