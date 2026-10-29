import numpy as np
def integrate(p, T=900.0, dt=0.1, A0=1.0, P0=0.5, w=0.02):
    n=int(T/dt); t=np.arange(0,n+1)*dt
    A=np.zeros(n+1); P=np.zeros(n+1); D=np.zeros(n+1); B=np.zeros(n+1); b=np.zeros(n+1)
    rho=p['rho']; Amax=p['Amax']; bG=p['bG']; e=p['e']; r=p['r']; eta=p['eta']; alpha=p['alpha']
    sig=p['sig']; kappa=p['kappa']; tw=p['tw']; deltab=p['deltab']; b0=p['b0']; Aext=p['Aext']
    def Tb(tv): return deltab/(1+np.exp(-kappa*(tv-tw)))
    def bf(tv,Dd): return (b0+Tb(tv))*np.exp(-alpha*max(Dd,0))
    def Gf(a):
        a=max(a,0.0); return rho*a*(1-a/Amax)
    def ramp(x):   # smooth ramp approximating x_+ 
        if w<=0: return max(x,0)
        return w*np.log(1+np.exp(x/w))
    A[0]=A0; P[0]=P0; D[0]=0.0
    def dAHist(tv):
        i=(tv-p['tau_g'])/dt
        if i<=0: return A0
        k=int(np.floor(i)); fr=i-k
        return A[k] if k+1>n else A[k]*(1-fr)+A[min(k+1,n)]*fr
    def dPHist(tv):
        i=(tv-p['tau_p'])/dt
        if i<=0: return P0
        k=int(np.floor(i)); fr=i-k
        return P[k] if k+1>n else P[k]*(1-fr)+P[min(k+1,n)]*fr
    def deriv(tt,Av,Pv,Dv):
        Ag=max(dAHist(tt),Aext); Pg=dPHist(tt)
        bv=bf(tt,Dv); Bv=bv*Av+bG*Gf(Ag); E=e*Pv; K=max(Bv/e,1e-4)
        dA=Gf(Ag)-ramp(E-sig*bv*Av)/bG
        dP=r*Pv*(1-Pg/K); dD=ramp(E-Bv)-eta*Dv
        return dA,dP,dD
    b[0]=bf(0,0); B[0]=b[0]*A0+bG*Gf(A0)
    for i in range(n):
        tt=t[i]
        k1=deriv(tt,A[i],P[i],D[i])
        k2=deriv(tt+dt/2,A[i]+dt/2*k1[0],P[i]+dt/2*k1[1],D[i]+dt/2*k1[2])
        k3=deriv(tt+dt/2,A[i]+dt/2*k2[0],P[i]+dt/2*k2[1],D[i]+dt/2*k2[2])
        k4=deriv(tt+dt,A[i]+dt*k3[0],P[i]+dt*k3[1],D[i]+dt*k3[2])
        A[i+1]=max(A[i]+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),Aext)
        P[i+1]=max(P[i]+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]),0.0)
        D[i+1]=max(D[i]+dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2]),0.0)
        b[i+1]=bf(t[i+1],D[i+1]); B[i+1]=b[i+1]*A[i+1]+bG*Gf(dAHist(t[i+1]))
    return dict(t=t,A=A,P=P,D=D,B=B,b=b)

if __name__=="__main__":
    p=dict(rho=0.08, Amax=1.2, b0=0.5, bG=0.6, e=0.55, r=0.02, eta=0.03, alpha=0.2,
           sig=1.0, deltab=0.5, kappa=0.04, tw=120, tau_g=15, tau_p=25, Aext=0.02)
    res=integrate(p,T=900.0,dt=0.1,A0=1.0,P0=0.45)
    t,A,P,D,B=res['t'],res['A'],res['P'],res['D'],res['B']
    B0=B[0]; A0v=A[0]; print("t=0: A=%.3f B=%.3f P=%.3f D=%.3f"%(A0v,B0,P[0],D[0]))
    for tt in [25,50,75,100,125,150,200,250,300,400,500,600,700,800,900]:
        i=int(round(tt/0.1)); print("t=%3d: A=%.3f B=%.3f P=%.3f D=%.3f"%(tt,A[i],B[i],P[i],D[i]))
    mask=np.array([(B[i]>B0 and A[i]<A0v*0.99) for i in range(len(t))])
    idx=np.where(mask)[0]
    if len(idx):
        j=idx[np.argmax(B[idx])]
        print("MASKING: t=[%.0f,%.0f], peak B=%.3f at t=%.0f, A=%.3f (A0=%.3f) -> B rises while A falls"%(
            t[idx[0]],t[idx[-1]],B[idx].max(),t[j],A[j],A0v))
    else:
        print("NO masking window")
    # collapse check
    print("final A=%.3f B=%.3f P=%.3f D=%.3f"%(A[-1],B[-1],P[-1],D[-1]))

try:
    # Scenario: overshoot (P>K) + strong early tech wave -> masking (B up, A down), then collapse
    p2=dict(rho=0.05, Amax=1.2, b0=0.5, bG=0.4, e=0.8, r=0.02, eta=0.03, alpha=0.2,
           sig=1.0, deltab=0.6, kappa=0.04, tw=100, tau_g=15, tau_p=25, Aext=0.02)
    res=integrate(p2,T=900.0,dt=0.1,A0=1.2,P0=0.95)
    t,A,P,D,B=res['t'],res['A'],res['P'],res['D'],res['B']
    B0=B[0];A0v=A[0]
    print("t=0: A=%.3f B=%.3f P=%.3f D=%.3f"%(A0v,B0,P[0],D[0]))
    for tt in [25,50,75,100,125,150,175,200,250,300,400,600,900]:
        i=int(round(tt/0.1)); print("t=%3d: A=%.3f B=%.3f P=%.3f D=%.3f"%(tt,A[i],B[i],P[i],D[i]))
    mask=np.array([(B[i]>B0 and A[i]<A0v*0.995) for i in range(len(t))])
    idx=np.where(mask)[0]
    if len(idx):
        j=idx[np.argmax(B[idx])]
        print("MAKING WINDOW t=[%.0f,%.0f], peak B=%.3f at t=%.0f, A=%.3f (A0=%.3f)  ==> B rises while A falls"%(t[idx[0]],t[idx[-1]],B[idx].max(),t[j],A[j],A0v))
        Apeak=A[idx].min(); 
        print("   in window A min =%.3f, B max=%.3f"%(A[idx].min(),B[idx].max()))
    else:
        print("NO masking window")
    print("final A=%.3f B=%.3f P=%.3f D=%.3f"%(A[-1],B[-1],P[-1],D[-1]))
except Exception as ex:
    print("ERR",ex)
