import numpy as np
from scipy.optimize import root
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;r=0.02
a11=-0.5;a21=0.01;ge=1.0
def F(l,tm,tp): return l**2-a11*l+r*(l-a11)*np.exp(-l*tp)+ge*a21*np.exp(-l*tm)
def dom(tm,tp):
    best=None
    for re in np.linspace(-0.35,0.35,15):
        for im in np.linspace(0.0,1.2,30):
            for s in [1,-1]:
                sol=root(lambda z:[F(complex(z[0],z[1]),tm,tp).real,F(complex(z[0],z[1]),tm,tp).imag],[re,im*s])
                if sol.success:
                    l=complex(sol.x[0],sol.x[1])
                    if abs(F(l,tm,tp))<1e-7:
                        if best is None or l.real>best.real: best=l
    return best
print("SINGLE tau_M (tau_P=0), large values:")
for tm in [80,120,200,300,500,800,1000,2000]:
    l=dom(tm,0)
    print(f"  tau_M={tm:5d}: Re={l.real:+.4f} Im={l.imag:+.4f}" if l else f"  tau_M={tm}: none")
print("SINGLE tau_P (tau_M=0), large values:")
for tp in [80,120,200,300,500,800,1000,2000]:
    l=dom(0,tp)
    print(f"  tau_P={tp:5d}: Re={l.real:+.4f} Im={l.imag:+.4f}" if l else f"  tau_P={tp}: none")
