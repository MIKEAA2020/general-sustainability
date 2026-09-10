import numpy as np
from scipy.optimize import root
a11=-0.5;r=0.02;gea=0.01
def F(l,tm,tp): return l**2-a11*l+r*(l-a11)*np.exp(-l*tp)+gea*np.exp(-l*tm)
def dom(tm,tp):
    best=None
    for re in np.linspace(-0.3,0.3,13):
        for im in np.linspace(0,0.8,25):
            for s in [1,-1]:
                sol=root(lambda z:[F(complex(z[0],z[1]),tm,tp).real,F(complex(z[0],z[1]),tm,tp).imag],[re,im*s])
                if sol.success:
                    l=complex(sol.x[0],sol.x[1])
                    if abs(F(l,tm,tp))<1e-7:
                        if best is None or l.real>best.real: best=l
    return best
# scan sums 50..79
print("Scanning sum from 50 to 79 for any Re>0:")
found=0
for s in range(50,80):
    for tm in range(0,s+1):
        tp=s-tm
        l=dom(tm,tp)
        if l is not None and l.real>1e-6:
            print(f"  SUM {s}: tm={tm} tp={tp} Re={l.real:+.4f}")
            found+=1
            break
print("total unstable (sum<=79):", found)
