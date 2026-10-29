import numpy as np
def run(p, T=400, dt=0.1, A0=1.2, E=0.6):
    n=int(T/dt); t=np.arange(0,n+1)*dt
    A=np.zeros(n+1);D=np.zeros(n+1);B=np.zeros(n+1);b=np.zeros(n+1)
    rho=p['rho'];Amax=p['Amax'];bG=p['bG'];eta=p['eta'];alpha=p['alpha']
    kap=p['kappa'];tw=p['tw'];db=p['deltab'];b0=p['b0'];Aext=p['Aext'];w=p['w']
    def Tb(tv): return db/(1+np.exp(-kap*(tv-tw)))
    def bf(tv,Dd): return (b0+Tb(tv))*np.exp(-alpha*max(Dd,0))
    def Gf(a): a=max(a,0.0); return rho*a*(1-a/Amax)
    def ramp(x): return w*np.log(1+np.exp(x/w))
    A[0]=A0;D[0]=0;b[0]=bf(0,0);B[0]=b[0]*A0+bG*Gf(A0)
    def der(tt,Aa,Dd):
        bv=bf(tt,Dd); Bv=bv*Aa+bG*Gf(Aa)
        return (Gf(Aa)-ramp(E-bv*Aa)/bG, ramp(E-Bv)-eta*Dd)
    for i in range(n):
        tt=t[i]
        k1=der(tt,A[i],D[i]); k2=der(tt+dt/2,A[i]+dt/2*k1[0],D[i]+dt/2*k1[1])
        k3=der(tt+dt/2,A[i]+dt/2*k2[0],D[i]+dt/2*k2[1]); k4=der(tt+dt,A[i]+dt*k3[0],D[i]+dt*k3[1])
        A[i+1]=max(A[i]+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),Aext)
        D[i+1]=max(D[i]+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),0)
        b[i+1]=bf(t[i+1],D[i+1]); B[i+1]=b[i+1]*A[i+1]+bG*Gf(A[i+1])
    return dict(t=t,A=A,D=D,B=B,b=b)
if __name__=="__main__":
    p=dict(rho=0.04,Amax=1.2,b0=0.5,bG=0.2,eta=0.03,alpha=0.15,kappa=0.06,tw=50,deltab=0.9,Aext=0.02,w=0.05)
    # convergence check + masking
    for dt in [0.5,0.1,0.05,0.02]:
        r=run(p,T=250,dt=dt,A0=1.2,E=0.6); t,A,B=r['t'],r['A'],r['B'];B0=B[0]
        mask=np.array([(B[i]>B0 and A[i]<A[0]*0.995) for i in range(len(t))]);idx=np.where(mask)[0]
        if len(idx):
            j=idx[np.argmax(B[idx])]
            print("dt=%.2f: window=[%.0f,%.0f] span=%.0f | B0=%.3f peak B=%.3f @t=%.0f A=%.3f | A_min=%.3f"%(
                dt,t[idx[0]],t[idx[-1]],t[idx[-1]]-t[idx[0]],B0,B[idx].max(),t[j],A[j],A[idx].min()))
        else:
            print("dt=%.2f: no masking | B0=%.3f Bmax=%.3f Amin=%.3f"%(dt,B0,B.max(),A.min()))
