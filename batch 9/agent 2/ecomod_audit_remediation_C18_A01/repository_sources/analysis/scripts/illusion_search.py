import numpy as np
rho=1.5;Mmax=1.2;gam=1.0;b0=0.5;ropt=1.0;r=0.02
dt=0.5;T=400.0;n=int(T/dt);Nhist=2000;idx0=Nhist

def run(e,tau_m,tau_p,alpha,db,twave,kappa,tau_debt=0.0):
    Mv=np.full(idx0+n+1,1.0);Pv=np.full(idx0+n+1,0.1);Dv=np.zeros(idx0+n+1)
    def hist(a,t,d):
        xf=(t-d)/dt+idx0;j=int(np.floor(xf));fr=xf-j
        j0=max(0,min(len(a)-1,j));j1=max(0,min(len(a)-1,j+1));return a[j0]*(1-fr)+a[j1]*fr
    rec=[]
    for k in range(n+1):
        t=k*dt;i=idx0+k
        if i==idx0: continue
        Dc=Dv[i-1]
        Tt=db/(1+np.exp(-kappa*(t-twave)))
        b=b0*np.exp(-alpha*max(0,Dc))+Tt
        B=b*Mv[i-1]
        # apply debt delay to E-B
        if tau_debt>0 and i>idx0+int(tau_debt/dt):
            Em2=e*hist(Pv,t-dt,tau_debt); Bm2=b0*np.exp(-alpha*max(0,hist(Dv,t-dt,tau_debt)))+Tt
            # approximate B(t-tau_debt) using stored
        else:
            Em2=e*Pv[i-1]; Bm2=B
        K=B/ropt
        Etm=e*hist(Pv,t-dt,tau_m) if tau_m>0 else e*Pv[i-1]
        Pt_=hist(Pv,t-dt,tau_p) if tau_p>0 else Pv[i-1]
        dP=r*Pv[i-1]*(1-Pt_/K) if K>0 else 0.0
        dM=rho*Mv[i-1]*(1-Mv[i-1]/Mmax)-gam*Etm
        dD=max(e*Pv[i-1]-B,0.0)
        Mv[i]=max(0,Mv[i-1]+dt*dM);Pv[i]=max(0,Pv[i-1]+dt*dP);Dv[i]=max(0,Dv[i-1]+dt*dD)
        rec.append((t,Mv[i],Pv[i],Dv[i],b,B))
    return np.array(rec)

# Detect "illusion": window where dB/dt>0 while dM/dt<0, and B exceeds initial B
def detect_illusion(rec):
    B=rec[:,5];M=rec[:,1];t=rec[:,0]
    B0=B[0]
    dt_=t[1]-t[0]
    dM=np.gradient(M,dt_);dB=np.gradient(B,dt_)
    for i in range(1,len(t)-1):
        # window of sustained illusion
        if dB[i]>0 and dM[i]<0:
            # check it persists for at least 30 yr
            j=i
            while j<len(t)-1 and dB[j]>0 and dM[j]<0:
                j+=1
            if (t[j]-t[i])>30 and B[i]>B0*1.02:
                return (t[i],t[j],M[i],M[j],B[i],B[j])
    return None

print("Searching for a genuine productivity-illusion scenario (rising B while M falls):")
found=[]
for e in [1.15,1.3,1.0]:
    for alpha in [0.2,0.5]:
        for db in [0.8,1.5,2.5]:
            for twave in [30,60,100,150]:
                for kappa in [0.05,0.1]:
                    rec=run(e,30,25,alpha,db,twave,kappa)
                    res=detect_illusion(rec)
                    if res:
                        found.append((e,alpha,db,twave,kappa,res))
                        print(f"  e={e} alpha={alpha} db={db} tw={twave} k={kappa}: window t={res[0]:.0f}-{res[1]:.0f}, M {res[2]:.2f}->{res[3]:.2f}, B {res[4]:.3f}->{res[5]:.3f}")
print("total illusion scenarios found:", len(found))
