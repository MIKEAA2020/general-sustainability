import numpy as np
def ramp(x,w=0.02):
    x=np.asarray(x,float); y=x/w
    z=np.where(y>0, y+np.log1p(np.clip(np.exp(-y),0,None)), np.log1p(np.clip(np.exp(y),0,None)))
    return w*z
def integrate(p,T=1500.0,dt=0.1,A0=1.0,P0=0.45):
    rho=p['rho'];Amax=p['Amax'];b0=p['b0'];bG=p['bG'];e=p['e'];r=p['r'];Aext=p['Aext'];w=p['w']
    def G(a): a=max(a,0.0); return rho*a*(1-a/Amax)
    n=int(T/dt); A=np.zeros(n+1);P=np.zeros(n+1); A[0]=A0;P[0]=P0
    for i in range(n):
        a=A[i];pp=P[i]
        def F(aa,qq):
            Bv=b0*aa+bG*G(aa)
            return (G(aa)-ramp(e*qq-b0*aa,w)/bG, r*qq*(1-qq/max(Bv/e,1e-6)))
        k1=F(a,pp);k2=F(a+dt/2*k1[0],pp+dt/2*k1[1]);k3=F(a+dt/2*k2[0],pp+dt/2*k2[1]);k4=F(a+dt*k3[0],pp+dt*k3[1])
        A[i+1]=max(a+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),Aext)
        P[i+1]=max(pp+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),0.0)
    return A,P
p=dict(rho=0.08,Amax=1.2,b0=0.5,bG=0.6,e=0.55,r=0.02,Aext=0.02,w=0.02)
print("Corrected S0, narrow ramp w=0.02, alpha=0, no tech, tau=0. Recover=A settles near Amax, Collapse=A->Aext.")
def cls(A0,P0):
    A,P=integrate(p,A0=A0,P0=P0)
    return 'R' if A[-1]>1.15 else ('C' if A[-1]<0.1 else '?')
gridA=[0.4,0.6,0.8,1.0,1.15]; gridP=[0.05,0.1,0.2,0.3,0.5,0.7,0.9]
print("   " + " ".join(f"{a:.2f}" for a in gridA))
for P0 in gridP:
    print(f" P0={P0:.2f}: " + "   ".join(cls(a,P0) for a in gridA))
# where does a 'sustainable' IC settle? trace a few
for (A0,P0) in [(1.0,0.10),(1.0,0.30),(1.0,0.50),(0.8,0.10),(0.8,0.90)]:
    A,P=integrate(p,A0=A0,P0=P0)
    print(f"  IC({A0},{P0}): final A*={A[-1]:.3f} P*={P[-1]:.3f}")
