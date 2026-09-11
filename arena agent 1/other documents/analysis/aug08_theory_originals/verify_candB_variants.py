import numpy as np, sys
sys.path.insert(0, 'verification_scripts')
from fourstate_pipeline import FOUR_PARAMS, four_arr, softplus_stable
from verify_kappaA_sweep import hopf_thresholds
from close_d12_fourstate_gated import equilibrium_gated

def run(cand, gated, donor, kA, label=""):
    p = FOUR_PARAMS()
    if cand == 'A': p['eta']=0.914; p['Emax']=30.0
    else:           p['eta']=2.756; p['Emax']=26.0
    p['kappa_A'] = kA
    pa = four_arr(p)
    Z = p['delta']
    N, A, E1, Aeq = equilibrium_gated(p, donor=donor)
    def rhs(N_,Z_,E_,A_,Ztau):
        R = pa[0]*N_*(1-N_/pa[1])*A_/(A_+pa[14])
        B = R + pa[11]*N_*A_/(A_+pa[14]) if donor else R + pa[11]*N_
        u = pa[2]*E_*N_ - R
        sp = softplus_stable(u, pa[7])
        inner = sp - np.log(2.0)/pa[7] + pa[10]
        Zdot = ((inner if inner>0 else 0.0) - Z_)/pa[5]
        bracket = pa[3]*E_*(Ztau/pa[6] - E_/pa[4]) + pa[9]*Ztau/(pa[8]+Ztau)
        if gated: bracket = bracket*(1.0 - E_/pa[4])
        return np.array([R - pa[2]*E_*N_, Zdot, bracket, -B + pa[12]*(Aeq - A_)])
    st = np.array([N, Z, E1, A])
    h = 1e-6
    J = np.zeros((4,4))
    for j in range(4):
        sp_ = st.copy(); sm = st.copy(); sp_[j]+=h; sm[j]-=h
        J[:,j] = (rhs(sp_[0],sp_[1],sp_[2],sp_[3], Z) - rhs(sm[0],sm[1],sm[2],sm[3], Z))/(2*h)
    dEdZ = pa[3]*E1/pa[6] + pa[9]*pa[8]/(pa[8]+Z)**2
    if gated: dEdZ *= (1.0 - E1/pa[4])
    Bd = np.zeros((4,4)); Bd[2,1] = dEdZ
    ev0 = np.linalg.eigvals(J + Bd)
    th = hopf_thresholds(J, Bd, w_lo=1e-4, w_hi=3.0, nw=12000, nmax=4)
    print(f"[{label}] N*={N:.4f} A*={A:.4f} | tau0 eig {np.round(ev0,5)} | Hopf {[round(t,3) for t,w in th[:4]]}")

run('B', False, 1, 0.05,  "B ungated donor kA=0.05 ")
run('B', True,  1, 0.05,  "B gated   donor kA=0.05 ")
run('B', False, 0, 0.05,  "B ungated oldB  kA=0.05 ")
run('B', True,  0, 0.05,  "B gated   oldB  kA=0.05 ")
for kA in [0.0015, 0.01, 0.02, 0.1, 0.3]:
    run('B', False, 1, kA, f"B ungated donor kA={kA}")
