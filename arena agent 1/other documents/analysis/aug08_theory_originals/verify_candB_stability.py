import numpy as np, sys
sys.path.insert(0, 'verification_scripts')
from fourstate_pipeline import FOUR_PARAMS, four_arr, softplus_stable
from verify_kappaA_sweep import rightmost_root
from close_d12_fourstate_gated import equilibrium_gated

p = FOUR_PARAMS(); p['eta']=2.756; p['Emax']=26.0
pa = four_arr(p); Z = p['delta']
N,A,E1,Aeq = equilibrium_gated(p, donor=1)
def rhs(N_,Z_,E_,A_,Ztau):
    R = pa[0]*N_*(1-N_/pa[1])*A_/(A_+pa[14])
    B = R + pa[11]*N_*A_/(A_+pa[14])
    u = pa[2]*E_*N_ - R
    sp = softplus_stable(u, pa[7])
    inner = sp - np.log(2.0)/pa[7] + pa[10]
    Zdot = ((inner if inner>0 else 0.0) - Z_)/pa[5]
    bracket = pa[3]*E_*(Ztau/pa[6] - E_/pa[4]) + pa[9]*Ztau/(pa[8]+Ztau)
    return np.array([R - pa[2]*E_*N_, Zdot, bracket, -B + pa[12]*(Aeq - A_)])
st = np.array([N,Z,E1,A]); h=1e-6
J = np.zeros((4,4))
for j in range(4):
    sp_ = st.copy(); sm = st.copy(); sp_[j]+=h; sm[j]-=h
    J[:,j] = (rhs(sp_[0],sp_[1],sp_[2],sp_[3],Z) - rhs(sm[0],sm[1],sm[2],sm[3],Z))/(2*h)
dEdZ = pa[3]*E1/pa[6] + pa[9]*pa[8]/(pa[8]+Z)**2
Bd = np.zeros((4,4)); Bd[2,1]=dEdZ
print("stability windows (rightmost root real part):")
for tau in [0, 3, 6.251, 10, 60, 76.33, 100, 120, 159.3, 180]:
    rr = rightmost_root(J, Bd, tau)
    print(f"  tau={tau:8.3f}  Re(rightmost)={rr.real:+.6f}")
