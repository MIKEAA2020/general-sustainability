import numpy as np
# Well-posed unified stock-flow model (1''') -- method-of-steps DDE (RK4).
# WELL-POSEDNESS (fix for the K->0 / P->inf singularity):
#   * A-extinction floor A_ext>0 so K stays bounded (no P/K blow-up)
#   * K = max(B/e, K_min)
#   * delayed states evaluated at the true delayed time (linear interp in history)
def integrate(p, T=800.0, dt=0.2, A0=1.0, P0=0.5):
    tg=p['tau_g']; tp=p['tau_p']
    n=int(T/dt); t=np.arange(0,n+1)*dt
    A=np.zeros(n+1); P=np.zeros(n+1); D=np.zeros(n+1); B=np.zeros(n+1); b=np.zeros(n+1)
    rho=p['rho']; Amax=p['Amax']; bG=p['bG']; e=p['e']; r=p['r']; eta=p['eta']; alpha=p['alpha']
    sig=p['sig']; kappa=p['kappa']; tw=p['tw']; deltab=p['deltab']; b0=p['b0']; Aext=p['Aext']
    # history arrays (constant for t<=0, appended as we go)
    def hi(arr,i):  # linear-interp delayed value
        if i<=0: return arr[0] if isinstance(arr,np.ndarray) else arr
        k=np.floor(i).astype(int); frac=i-k
        if k>=len(arr): k=len(arr)-1; frac=0.0
        if k+1>=len(arr): return arr[k]
        return arr[k]*(1-frac)+arr[k+1]*frac
    A[0]=A0; P[0]=P0; D[0]=0.0
    off=1  # base offset for history (indices <0 -> initial)
    def histA(i): return A0 if i<=0 else A[i]
    def histP(i): return P0 if i<=0 else P[i]
    def Tb(tv): return deltab/(1+np.exp(-kappa*(tv-tw)))
    def bf(tv,Dd): return (b0+Tb(tv))*np.exp(-alpha*Dd)
    def Gf(a):
        a=max(a,0.0); return rho*a*(1-a/Amax)
    def deriv(tt,Av,Pv,Dv,Ag,Pg):
        Ag=max(Ag,Aext)                  # extinction floor
        bv=bf(tt,Dv); Bv=bv*Av+bG*Gf(Ag) # biocapacity = flow + increment
        E=e*Pv; K=max(Bv/e,1e-4)
        dA=Gf(Ag)-max(E-sig*bv*Av,0)/bG
        dP=r*Pv*(1-Pg/K)
        dD=max(E-Bv,0)-eta*Dv
        return dA,dP,dD
    def delayed(tt,arr,lag):
        return histA(((tt-lag)/dt)) if arr=='A' else histP(((tt-lag)/dt))
    histA_full=A; histP_full=P
    def dAHist(tv):  # A at (t-tg) via direct index/frac
        i=(tv-tg)/dt
        if i<=0: return A0
        k=int(np.floor(i)); fr=i-k
        if k>=n: return A[n]
        if k+1>n: return A[k]
        return A[k]*(1-fr)+ A[k+1] if k+1<n else A[k]
    def dPHist(tv):
        i=(tv-tp)/dt
        if i<=0: return P0
        k=int(np.floor(i)); fr=i-k
        if k+1>n: return P[k]
        return P[k]*(1-fr)+P[k+1] if k+1<n else P[k]
    # note: use arrays A,P as they fill; helper maps tv-> state index
    def Ast(tv):
        i=np.clip((tv)/dt,0,n); return A[int(np.floor(i))]
    for i in range(n):
        tt=t[i]
        # delayed states at the step midpoint using the running history
        Ag=dAHist(tt); Pg=dPHist(tt)
        def fd(tt2,Av,Pv,Dv):
            Ag2=dAHist(tt2); Pg2=dPHist(tt2); return deriv(tt2,Av,Pv,Dv,Ag2,Pg2)
        k1=fd(tt,A[i],P[i],D[i])
        k2=fd(tt+dt/2,A[i]+dt/2*k1[0],P[i]+dt/2*k1[1],D[i]+dt/2*k1[2])
        k3=fd(tt+dt/2,A[i]+dt/2*k2[0],P[i]+dt/2*k2[1],D[i]+dt/2*k2[2])
        k4=fd(tt+dt,A[i]+dt*k3[0],P[i]+dt*k3[1],D[i]+dt*k3[2])
        nA=A[i]+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        nP=P[i]+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        nD=D[i]+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2])
        A[i+1]=max(nA,Aext); P[i+1]=max(nP,0.0); D[i+1]=max(nD,0.0)
        b[i+1]=bf(t[i+1],D[i+1]); B[i+1]=b[i+1]*A[i+1]+bG*Gf(dAHist(t[i+1]))
    B[0]=bf(0,0)*A0+bG*Gf(A0); b[0]=bf(0,0)
    return dict(t=t,A=A,P=P,D=D,B=B,b=b)

if __name__=="__main__":
    p=dict(rho=0.10, Amax=1.2, b0=0.5, bG=0.8, e=0.7, r=0.02, eta=0.02, alpha=0.2,
           sig=1.0, deltab=0.4, kappa=0.05, tw=100, tau_g=15, tau_p=25, Aext=0.02)
    res=integrate(p,T=800.0,dt=0.2,A0=1.0,P0=0.6)
    t,A,P,D,B=res['t'],res['A'],res['P'],res['D'],res['B']
    B0=B[0]; A0v=A[0]
    print("t=0: A=%.3f B=%.3f P=%.3f"%(A0v,B0,P[0]))
    for tt in [40,80,120,160,200,250,300,400,500,600,700,800]:
        i=int(round(tt/0.2)); print("t=%3d: A=%.3f B=%.3f P=%.3f D=%.3f"%(tt,A[i],B[i],P[i],D[i]))
    mask=np.array([(B[i]>B0 and A[i]<A0v*0.99) for i in range(len(t))])
    idx=np.where(mask)[0]
    if len(idx):
        j=idx[np.argmax(B[idx])]
        print("MASKING window t=[%.1f,%.1f], peak B=%.3f at t=%.1f while A=%.3f (A0=%.3f)==> B rises while A falls"%(t[idx[0]],t[idx[-1]],B[idx].max(),t[j],A[j],A0v))
    else:
        print("NO masking window")
