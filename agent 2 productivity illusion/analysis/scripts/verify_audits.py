import numpy as np
from scipy.optimize import root

def analyze(rho, e):
    Mmax=1.2; gam=1.0; b0=0.5; ropt=1.0; r=0.02
    Ms=Mmax*(1-gam*e*b0/(rho*ropt))
    a11=rho*(1-2*Ms/Mmax); a21=r*b0/ropt; gea=gam*e*a21
    Mtilde = np.array([[a11,-gam*e],[a21,-r]])
    tr=np.trace(Mtilde); det=np.linalg.det(Mtilde)
    # lambda = rho*Mmax*Ms?  det claim = rho*r*Ms/Mmax
    det_claim = rho*r*Ms/Mmax
    Lam = r**2*a11**2 - (gam*e*a21)**2
    return dict(rho=rho,e=e,Ms=Ms,Ms_frac=Ms/Mmax,a11=a11,a21=a21,gea=gea,
                trace=tr,det=det,det_claim=det_claim,Lam=Lam)

print("=== Routh-Hurwitz: is det = r*rho*M*/Mmax > 0 always? trace condition a11<r ===")
for rho,e in [(1.5,1.0),(1.5,1.15),(1.6,1.0),(0.9,1.0)]:
    d=analyze(rho,e)
    print(f" rho={rho} e={e}: M*/Mmax={d['Ms_frac']:.4f} a11={d['a11']:.4f}  trace={d['trace']:.4f}(need<0)  det={d['det']:.6f} vs rho*r*M*/Mmax={d['det_claim']:.6f}")

print()
print("=== Does strict inequality mean a tau_P-ONLY Hopf exists? (Claude A1) ===")
def singledelay_hophs(rho, e, which):
    # root-find Re(lambda)=Im(lambda)=0 crossing, i.e. find omega>0 satisfying char
    Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;r=0.02
    Ms=Mmax*(1-gam*e*b0/(rho*ropt)); a11=rho*(1-2*Ms/Mmax); a21=r*b0/ropt; gea=gam*e*a21
    def eq(lam, tau, which):
        if which=='tau_m':  # tau_p=0
            return lam**2-a11*lam+gea*np.exp(-lam*tau)+r*(lam-a11)
        else:               # tau_m=0, delay on demographic
            return lam**2-a11*lam+gea+r*(lam-a11)*np.exp(-lam*tau)
    # search omega in [0,0.5]
    oms=np.linspace(0.001,0.5,2000)
    results=[]
    for w_ in oms:
        # residual for tau solving: hunt for tau where char(iw)=0
        # char(iw) as function of tau; use root for the delay with fixed w
        # Use the 1D function of tau: real/imag of eq(iw,tau)
        pass
    # Instead: for a range of tau, find dominant Re(lambda) with our spectral seed method
    def dom(tau):
        best=None
        for re_ in np.linspace(-0.3,0.3,15):
            for im_ in np.linspace(0,0.6,25):
                for sg in [1,-1]:
                    f=lambda z:[eq(complex(z[0],z[1]),tau,which).real,eq(complex(z[0],z[1]),tau,which).imag]
                    sol=root(f,[re_,im_*sg])
                    if sol.success:
                        l=complex(sol.x[0],sol.x[1])
                        if abs(eq(l,tau,which))<1e-7:
                            if best is None or l.real>best.real: best=l
        return best
    out=[]
    for tau in [0,20,40,60,80,100,120,150]:
        l=dom(tau)
        out.append((tau, round(l.real,5) if l else None))
    return out

print("--- baseline rho=1.5, e=1.0 (sustainable). Lam=0 (knife-edge) ---")
d=analyze(1.5,1.0); print("  Lam=%.2e"%d['Lam'])
for which in ['tau_m','tau_p']:
    print(f"  which={which}: ",singledelay_hophs(1.5,1.0,which))
print("--- rho=1.6, e=1.0 (sustainable): Lam>0 -> Claude predicts tau_P-only Hopf ---")
d=analyze(1.6,1.0); print("  Lam=%.2e  a11=%.4f"%(d['Lam'],d['a11']))
for which in ['tau_m','tau_p']:
    print(f"  which={which}: ",singledelay_hophs(1.6,1.0,which))
