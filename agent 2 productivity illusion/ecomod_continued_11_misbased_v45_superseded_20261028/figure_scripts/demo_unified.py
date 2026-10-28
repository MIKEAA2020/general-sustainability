"""Numerical core for the one-stock comparator figure in ECOMOD v43.

Annual NFA account quantities B and E are in gha; P and K are in cap; A and
Amax use comparator-specific stock units; G(A) is stock-unit yr^-1. The yield
coefficients b, b0, Tb and Delta-b are gha per stock unit; bG is gha yr per
stock unit; e is gha cap^-1. Time and delays are yr; rho, r, eta and the
logistic-wave steepness kappa are yr^-1; sigma is dimensionless. The leaky
state D is gha yr, so alpha is gha^-1 yr^-1 and dot-D and eta D are gha. The
ramp width w is in gha and Aext is in stock units. Numeric values and
trajectory equations are unchanged from the v42 comparator figure.
"""
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
