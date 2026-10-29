import numpy as np
rho=1.5; Mmax=1.2; gam=1.0; b0=0.5; ropt=1.0; r=0.02
alpha=0.5; db=0.3; twave=150.0; kappa=0.1
dt=0.5; T=600.0
n=int(T/dt)

def run(e, tau_m, tau_p, tech=False, halfearth=False):
    # history
    Nhist=2000
    t0=-Nhist*dt
    M=np.zeros(n+1); P=np.zeros(n+1); D=0.0; bg=0.0
    history=[]  # store (t, M, P, D)
    # initial condition M=1.0,P=0.1 constant in past
    Mp=Pp=Dp=0.0
    Mstore=np.full(n+Nhist+1, 1.0)
    Pstore=np.full(n+Nhist+1, 0.1)
    Dstore=np.zeros(n+Nhist+1)
    idx0=Nhist
    for k in range(n+1):
        t=k*dt
        ti=idx0+k
        if ti>0:
            Mstore[ti]=Mstore[ti-1]; Pstore[ti]=Pstore[ti-1]; Dstore[ti]=Dstore[ti-1]
    # Actually simpler: store arrays of full length
    Mv=np.full(idx0+n+1, 1.0); Pv=np.full(idx0+n+1, 0.1); Dv=np.zeros(idx0+n+1)
    Mv[idx0]=1.0; Pv[idx0]=0.1; Dv[idx0]=0.0
    # history function for delays
    def hist(arr, t, delay):
        ti = int(round((t-delay)/dt)) + idx0
        ti=max(0,min(len(arr)-1,ti))
        # linear interp
        xf=(t-delay)/dt + idx0
        j=int(np.floor(xf))
        frac=xf-j
        j0=max(0,min(len(arr)-1,j)); j1=max(0,min(len(arr)-1,j+1))
        return arr[j0]*(1-frac)+arr[j1]*frac
    maxom=0.0
    results=[]
    for k in range(n+1):
        t=k*dt
        i=idx0+k
        # current b via D
        if tech:
            Tt = db/(1+np.exp(-kappa*(t-twave)))
        else:
            Tt=0.0
        b = b0*np.exp(-alpha*Dv[i-1 if i>idx0 else idx0]) + Tt
        # note index for D at current: use Dv at current point (previous). Let's use last computed.
        Dcur=Dv[i-1] if i>idx0 else 0.0
        b = b0*np.exp(-alpha*Dcur)+Tt
        B = b*Mv[i-1 if i>idx0 else idx0]
        # For half earth, cap K
        if halfearth:
            K = 0.5*B/ropt
        else:
            K = B/ropt
        Em = e*Pv[i-1 if i>idx0 else idx0]*1.0  # e in gha/cap/yr (ropt=1)
        if i>idx0:
            # integrate with Euler
            Mt = Mv[i-1]; Pt=Pv[i-1]
            Etm = e*hist(Pv, t-dt, tau_m) if tau_m>0 else e*Pt   # E(t-tau_m)=e P(t-tau_m)
            dMdt = rho*Mt*(1-Mt/Mmax) - gam*Etm
            P_tau = hist(Pv, t-dt, tau_p) if tau_p>0 else Pt
            dPdt = r*Pt*(1 - P_tau/K)
            dDdt = max(Em - B, 0.0)
            Mv[i]=max(0.0, Mt+dt*dMdt)
            Pv[i]=max(0.0, Pt+dt*dPdt)
            Dv[i]=Dv[i-1]+dt*dDdt
        else:
            Mv[i]=1.0; Pv[i]=0.1; Dv[i]=0.0
        # compute omega
        bt= b0*np.exp(-alpha*Dv[i])+Tt
        Bt=bt*Mv[i]
        Et=e*Pv[i]
        if Bt>1e-9:
            om=Et/Bt
            maxom=max(maxom, om)
        results.append((t,Mv[i],Pv[i],Dv[i]))
    return np.array(results), maxom

scenA,_=run(1.0,0,0)
scenB,omB=run(1.15,0,0)
scenC,omC=run(1.15,30,0)
scenD,omD=run(1.15,30,25)
scenE,omE=run(1.15,30,25,tech=True)
scenF,omF=run(1.15,30,25,halfearth=True)
for name,s,om in [('A',scenA,None),('B',scenB,omB),('C',scenC,omC),('D',scenD,omD),('E',scenE,omE),('F',scenF,omF)]:
    print(f"{name}: Mfin={s[-1,1]:.3f} Pfin={s[-1,2]:.3f} Dfin={s[-1,3]:.3f} maxOm={om if om else '--'}")
