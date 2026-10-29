"""Odd-grid Fourier collocation in invariant interior coordinates.
Coordinates u=log(N), z=Z, v=log(E/(Emax-E)) exclude boundary clipping.
This is floating-point continuation, not a continuum existence certificate.
"""
import numpy as np
from scipy.special import expit
from scipy.linalg import solve
from scipy.signal import resample
R,K,Q,ETA,EMAX,D0,TM,KK=.02,100.,.001,.914,30.,.01,5.,10.

def from_physical(Y):
    N,Z,E=Y.T
    if np.any(N<=0)or np.any(E<=0)or np.any(E>=EMAX):raise ValueError('Seed outside interior')
    return np.column_stack([np.log(N),Z,np.log(E/(EMAX-E))])

def physical(X):
    u,z,v=X.T;return np.column_stack([np.exp(u),z,EMAX*expit(v)])

def field(X,zd,jac=False):
    u,z,v=X.T;N=np.exp(u);E=EMAX*expit(v);Ev=E*(1-E/EMAX)
    deficit=N*(Q*E-R+R*N/K);mem=np.logaddexp(0,KK*deficit)/KK
    F=np.column_stack([R*(1-N/K)-Q*E,(mem-z)/TM,ETA*(zd-E/EMAX)+D0*zd/(E*(1+zd))])
    if not jac:return F
    sig=expit(KK*deficit);A=np.zeros((len(X),3,3));B=np.zeros((len(X),3))
    A[:,0,0]=-R*N/K;A[:,0,2]=-Q*Ev
    A[:,1,0]=sig*N*(Q*E-R+2*R*N/K)/TM;A[:,1,1]=-1/TM;A[:,1,2]=sig*Q*N*Ev/TM
    A[:,2,2]=-ETA*Ev/EMAX-D0*zd*Ev/(E*E*(1+zd));B[:,2]=ETA+D0/(E*(1+zd)**2)
    return F,A,B

class Collocation:
    def __init__(self,n):
        if n%2!=1:raise ValueError('Odd node count required: no ambiguous Nyquist mode')
        self.n=n;self.k=np.fft.fftfreq(n,d=1/n);self.eye_fft=np.fft.fft(np.eye(n),axis=0)
        self.D=self.matrix(2j*np.pi*self.k);self.DI=np.kron(self.D,np.eye(3));self.phase=np.sin(2*np.pi*np.arange(n)/n)/n
    def matrix(self,symbol):return np.fft.ifft(symbol[:,None]*self.eye_fft,axis=0).real
    def residual(self,w,tau,jac=True):
        X=w[:-1].reshape(self.n,3);T=w[-1];phi=tau/T;S=self.matrix(np.exp(-2j*np.pi*self.k*phi));zd=S@X[:,1]
        f,A,B=field(X,zd,True);res=np.r_[(self.D@X-T*f).ravel(),self.phase@X[:,0]]
        if not jac:return res
        J=np.zeros((3*self.n+1,3*self.n+1));J[:-1,:-1]=self.DI
        for i in range(self.n):
            J[3*i:3*i+3,3*i:3*i+3]-=T*A[i]
            J[3*i:3*i+3,1:-1:3]-=T*np.outer(B[i],S[i])
        Sp=self.matrix((-2j*np.pi*self.k)*np.exp(-2j*np.pi*self.k*phi))
        zdT=(Sp@X[:,1])*(-phi/T)
        J[:-1,-1]=(-f-T*B*zdT[:,None]).ravel();J[-1,:-1:3]=self.phase
        return res,J
    def newton(self,w,tau,tol=1e-9,maxit=18):
        w=np.asarray(w).copy()
        for it in range(maxit):
            res,J=self.residual(w,tau);err=float(np.max(np.abs(res)))
            if err<tol:return w,True,err,it
            try:step=solve(J,-res,check_finite=False)
            except Exception:return w,False,err,it
            a=1.
            for _ in range(18):
                trial=w+a*step
                if trial[-1]>1 and np.max(np.abs(trial[:-1].reshape(self.n,3)[:,[0,2]]))<200:
                    r=self.residual(trial,tau,False)
                    if np.isfinite(r).all()and np.max(np.abs(r))<err:break
                a*=.5
            else:return w,err<1e-8,err,it
            w=trial
        err=float(np.max(np.abs(self.residual(w,tau,False))));return w,err<1e-8,err,maxit
    def offgrid(self,w,tau,count=2049):
        X=w[:-1].reshape(self.n,3);T=w[-1];coef=np.fft.fft(X,axis=0)/self.n;t=np.arange(count)/count
        basis=np.exp(2j*np.pi*np.outer(t,self.k));values=(basis@coef).real;der=(basis@((2j*np.pi*self.k/T)[:,None]*coef)).real
        shifted=(np.exp(2j*np.pi*np.outer(t-tau/T,self.k))@coef[:,1]).real;f=field(values,shifted)
        Y=physical(values);E=Y[:,2];scale=np.column_stack([Y[:,0],np.ones(count),E*(1-E/EMAX)])
        errs=np.max(np.abs((der-f)*scale),axis=0)
        high=np.abs(coef[np.abs(self.k)>self.n/3]);tail=float(high.max())
        return {'offgrid_abs_residual_N_Z_E':errs.tolist(),'coordinate_fourier_tail':tail,'N_min':float(Y[:,0].min()),'N_max':float(Y[:,0].max()),'E_min':float(E.min()),'E_max':float(E.max()),'period':float(T)}

def resize(w,n):return np.r_[resample(w[:-1].reshape(-1,3),n,axis=0).ravel(),w[-1]]
