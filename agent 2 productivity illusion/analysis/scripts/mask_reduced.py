import numpy as np
# Reduced masking mechanism: fixed exogenous demand E, stock equation (1''') with tech wave.
# dA/dt = G(A) - [E - bA]_+/bG ; b=(b0+Tb)e^{-aD} ; dD/dt=[E-B]_+ - eta D ; B=bA+bG*G(A)
def run(p, T=600, dt=0.2, A0=1.2, E=0.62):
    n=int(T/dt); t=np.arange(0,n+1)*dt
    A=np.zeros(n+1);D=np.zeros(n+1);B=np.zeros(n+1);b=np.zeros(n+1)
    rho=p['rho'];Amax=p['Amax'];bG=p['bG'];eta=p['eta'];alpha=p['alpha']
    kap=p['kappa'];tw=p['tw'];db=p['deltab'];b0=p['b0'];Aext=p['Aext']
    def Tb(tv): return db/(1+np.exp(-kap*(tv-tw)))
    def bf(tv,Dd): return (b0+Tb(tv))*np.exp(-alpha*max(Dd,0))
    def Gf(a): a=max(a,0.0); return rho*a*(1-a/Amax)
    def ramp(x,w=0.02): return w*np.log(1+np.exp(x/w))
    A[0]=A0;D[0]=0;b[0]=bf(0,0);B[0]=b[0]*A0+bG*Gf(A0)
    for i in range(n):
        tt=t[i]; bv=bf(tt,D[i]); Bv=bv*A[i]+bG*Gf(A[i])
        dA=Gf(A[i])-ramp(E-bv*A[i])/bG
        dD=ramp(E-Bv)-eta*D[i]
        A[i+1]=max(A[i]+dt*dA,Aext); D[i+1]=max(D[i]+dt*dD,0)
        b[i+1]=bf(t[i+1],D[i+1]); B[i+1]=b[i+1]*A[i+1]+bG*Gf(A[i+1])
    return dict(t=t,A=A,D=D,B=B,b=b)
if __name__=="__main__":
    best=None
    for bG in [0.2,0.5,1.0,2.0]:
      for rho in [0.04,0.06,0.08]:
       for kap in [0.06,0.10,0.15]:
        for tw in [50,70,90]:
         for db in [0.6,0.9,1.2]:
          for E in [0.60,0.66,0.72]:
           p=dict(rho=rho,Amax=1.2,b0=0.5,bG=bG,eta=0.03,alpha=0.15,kappa=kap,tw=tw,deltab=db,Aext=0.02)
           res=run(p,T=400,dt=0.5,A0=1.2,E=E)
           t,A,B=res['t'],res['A'],res['B'];B0=B[0]
           mask=np.array([(B[i]>B0 and A[i]<A[0]*0.995) for i in range(len(t))])
           idx=np.where(mask)[0]
           if len(idx):
              span=t[idx[-1]]-t[idx[0]]
              if span>best[0] if best else span>0:
                 j=idx[np.argmax(B[idx])]
                 best=(span,dict(p,E=E),t[idx[0]],t[idx[-1]],B[idx].max(),t[j],A[j],A[idx].min())
    if best:
        print("BEST masking: span=%.0f yr window t=[%.0f,%.0f]; peak B=%.3f at t=%.0f while A=%.3f; A_min=%.3f"%(
            best[0],best[2],best[3],best[4],best[5],best[6],best[7]))
        print("  params:",{k:(round(v,2) if isinstance(v,float) else v) for k,v in best[1].items()})
    else:
        print("no masking")
