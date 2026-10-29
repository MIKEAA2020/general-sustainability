import numpy as np
from scipy.optimize import root

rho=1.5; Mmax=1.2; gam=1.0; b0=0.5; ropt=1.0; r=0.02
# scenario A
eA=1.0
MstA=Mmax*(1-gam*eA*b0/(rho*ropt))
a11=rho*(1-2*MstA/Mmax)
a21=r*b0/ropt
ge=gam*eA
print("Scenario A: M*", MstA, "a11", a11, "a21", a21)

def F(lam, tau_m, tau_p):
    return lam**2 - a11*lam + r*(lam-a11)*np.exp(-lam*tau_p) + ge*a21*np.exp(-lam*tau_m)

def dominant(tau_m, tau_p, re_max=0.4, im_max=0.6, n=41, tol=1e-9):
    # seeds over a complex grid
    seeds=[]
    for re in np.linspace(-0.4, re_max, 20):
        for im in np.linspace(0, im_max, 25):
            seeds.append(complex(re, im))
            seeds.append(complex(re, -im))
    roots=[]
    for s in seeds:
        sol = root(lambda z: [F(complex(z[0],z[1]), tau_m, tau_p).real,
                              F(complex(z[0],z[1]), tau_m, tau_p).imag],
                   [s.real, s.imag])
        if sol.success:
            l=complex(sol.x[0], sol.x[1])
            # validate residual
            if abs(F(l, tau_m, tau_p))<1e-7 and abs(l.imag)<im_max+0.2 and abs(l.real)<re_max+0.2:
                roots.append(l)
    # unique
    uni=[]
    for l in roots:
        if not any(abs(l-u)<1e-4 for u in uni):
            uni.append(l)
    if not uni:
        return None, 0
    return max(uni, key=lambda z: z.real), len(uni)

# Check baseline (30,25)
lam0, n0 = dominant(30,25)
print("tau_m=30,tau_p=25 dominant:", lam0, "nroots", n0)

# single delay: tau_p=0 vary tau_m; tau_m=0 vary tau_p
print("\n--- single environmental delay (tau_p=0) ---")
for tm in [0,10,20,30,40,50,60,70,80,90,100,120,150]:
    l,_=dominant(tm,0)
    print(f"tau_m={tm:3d}  Re(lam)={l.real:+.4f}  Im={l.imag:+.4f}")
print("\n--- single demographic delay (tau_m=0) ---")
for tp in [0,10,20,30,40,50,60,70,80,90,100]:
    l,_=dominant(0,tp)
    print(f"tau_p={tp:3d}  Re(lam)={l.real:+.4f}  Im={l.imag:+.4f}")
