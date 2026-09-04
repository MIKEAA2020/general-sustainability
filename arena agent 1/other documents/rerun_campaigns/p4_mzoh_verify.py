import numpy as np
from numpy.linalg import eigvals, matrix_rank
from scipy.linalg import expm
r,K,q=0.02,100.0,0.001; eta,Emax,dref=0.914,30.0,1.0; d0,tm,Zref=0.01,5.0,1.0
delta=np.log(2)/10.0
a=-eta/Emax;b=eta*delta/dref;c=d0*delta/(Zref+delta)
E=(-b-np.sqrt(b*b-4*a*c))/(2*a); N=K*(1-q*E/r); g=1-E/Emax
A_N=r*(1-2*N/K)-q*E; A_E=-q*N; B_N=-A_N/(2*tm); B_E=-A_E/(2*tm); d=1/tm
CE_m=g*eta*(delta/dref-2*E/Emax); CZ_m=g*(eta*E/dref+d0*Zref/(Zref+delta)**2)
CE_p=-g*eta; E0=E*(Zref+delta)/Zref; Ecap=-E0*Zref/(Zref+delta)**2; CZ_p=g*eta*Ecap
A_hold=np.array([[A_N,0,A_E],[B_N,-d,B_E],[0,0,0]])
J=np.array([[A_N,0,A_E],[B_N,-d,B_E],[0,CZ_m,CE_m]])
def mzoh(T,CE,CZ):
    AZ=J.copy(); AZ[2,1]=0.0
    if abs(np.linalg.det(AZ))>1e-12:
        integ=np.linalg.solve(AZ,expm(AZ*T)-np.eye(3))
    else:
        aug=np.block([[AZ,np.eye(3)],[np.zeros((3,3)),np.zeros((3,3))]])
        integ=expm(aug*T)[0:3,3:6]
    e3=np.zeros((3,1));e3[2,0]=1.0
    e2=np.zeros((1,3));e2[0,1]=1.0
    return expm(AZ*T)+integ@(CZ*e3@e2)
def cross(f,lo=0.2,hi=200.0):
    g_=np.linspace(lo,hi,40000); s=np.sign([abs(eigvals(f(T))).max()-1 for T in g_])
    out=[]
    for i in range(len(g_)-1):
        if s[i]!=0 and s[i]!=s[i+1]:
            l,h=g_[i],g_[i+1]
            for _ in range(60):
                m=.5*(l+h)
                if (abs(eigvals(f(l))).max()-1)*(abs(eigvals(f(m))).max()-1)<0:h=m
                else:l=m
            T=.5*(l+h);k=sorted(eigvals(f(T)),key=lambda x:abs(abs(x)-1))[0]
            out.append((round(T,4),round(k.real,4),round(k.imag,4)))
    return out
# protective ZOH
print("protective M_ZOH crossings [0.2,200]:", cross(lambda T:mzoh(T,CE_p,CZ_p)))
print("protective M_ZOH rho(1):", round(abs(eigvals(mzoh(1.0,CE_p,CZ_p))).max(),6))
# rank-one limit: eigenvalues at large T of M_ZOH
for T in (200,500,2000):
    M=mzoh(T,CE_m,CZ_m)
    print(f"mobilising M_ZOH rho({T})={abs(eigvals(M)).max():.6f}  rank={matrix_rank(M,tol=1e-10)}")
# check AZ invertibility
AZ=J.copy();AZ[2,1]=0.0
print("det AZ =", round(np.linalg.det(AZ),8))
