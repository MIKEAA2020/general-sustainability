import numpy as np
from scipy.optimize import root

def makeeq(rho, e, which):
    Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;r=0.02
    Ms=Mmax*(1-gam*e*b0/(rho*ropt)); a11=rho*(1-2*Ms/Mmax); a21=r*b0/ropt; gea=gam*e*a21
    def eq(lam, tau):
        if which=='tau_m':
            return lam**2-a11*lam+gea*np.exp(-lam*tau)+r*(lam-a11)
        else:
            return lam**2-a11*lam+gea+r*(lam-a11)*np.exp(-lam*tau)
    return eq

def dominant(eq, tau, re_lim=0.35, im_lim=0.8):
    best=None
    for re_ in np.linspace(-re_lim,re_lim,15):
        for im_ in np.linspace(0,im_lim,25):
            for sg in [1,-1]:
                f=lambda z:[eq(complex(z[0],z[1]),tau).real,eq(complex(z[0],z[1]),tau).imag]
                sol=root(f,[re_,im_*sg])
                if sol.success:
                    l=complex(sol.x[0],sol.x[1])
                    if abs(eq(l,tau))<1e-7:
                        if best is None or l.real>best.real: best=l
    return best

# SOLVE char(i w, tau)=0 jointly for (w, tau) -> the Hopf point
def solve_hopf(rho, e, which):
    Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;r=0.02
    Ms=Mmax*(1-gam*e*b0/(rho*ropt)); a11=rho*(1-2*Ms/Mmax); a21=r*b0/ropt; gea=gam*e*a21
    # lambda=i w, tau unknown. char = real + i imag. Solve real=0, imag=0 for (w,tau).
    def F(z):
        w_,tau=z
        return [eq_ri(w_,tau,which,a11,gea,r,0)]
    def eq_ri(w_,tau,which,a11,gea,r):
        if which=='tau_m':
            # lam=i w: lam^2=-w^2; -a11 lam=-a11 iw; +gea e^{-iw tau}
            e=i=None
            # real: -w^2 - r a11 + gea cos(w tau) ; imag: (r-a11) w - gea sin(w tau)
            real=-w**2 - r*a11 + gea*np.cos(w*tau)
            imag=(r-a11)*w - gea*np.sin(w*tau)
        else:
            # tau_m=0: lam^2 + (-a11+gea)?? no. char=lam^2-a11 lam+gea+r(lam-a11)e^{-lam tau}
            # lam=i w: lam^2=-w^2; -a11 lam=-a11 iw; +gea; +r(iw-a11)(cos-isin)
            real= -w**2 + gea + r*(-a11*np.cos(w*tau) + w*np.sin(w*tau))
            imag= -a11*w + r*(w*np.cos(w*tau) + a11*np.sin(w*tau))
        return [real,imag]
    best=None
    for w0 in np.linspace(0.005,0.4,60):
        for tau0 in np.linspace(5,300,120):
            sol=root(F,[w0,tau0])
            if sol.success:
                w_,tau=sol.x
                re_,im_=eq_ri(w_,tau,which,a11,gea,r)
                if abs(re_)<1e-7 and abs(im_)<1e-7 and w_>1e-4:
                    if best is None or w_<abs(best[0]) or True:
                        # collect unique
                        pass
                    best=(w_,tau)
    return best

# simpler: scan tau, find where dominant Re lambda crosses zero (sign change)
print("=== tau_m=0 (demographic delay only): find tau where Re lambda crosses zero ===")
for rho,e,label in [(1.5,1.0,'base A'),(1.6,1.0,'rho=1.6'),(1.5,1.15,'B (e=1.15)')]:
    eq=makeeq(rho,e,'tau_p')
    prev=None; prevtau=None
    print(f"--- {label} (rho={rho}, e={e}) ---")
    for tau in np.arange(0,300,2.0):
        l=dominant(eq,tau)
        if l is None: continue
        if prev is not None and prev<0<=l.real:
            print(f"   Hopf crossing between tau={prevtau:.0f} (Re={prev:+.4f}) and tau={tau:.0f} (Re={l.real:+.4f}), w={abs(l.imag):.4f}")
        prev=l.real; prevtau=tau
