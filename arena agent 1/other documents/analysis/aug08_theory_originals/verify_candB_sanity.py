import numpy as np, sys
sys.path.insert(0, 'verification_scripts')
from fourstate_pipeline import FOUR_PARAMS, four_arr, softplus_stable
from verify_kappaA_sweep import hopf_thresholds
from close_d12_fourstate_gated import equilibrium_gated

def run(cand, donor=1, label=""):
    p = FOUR_PARAMS()
    if cand == 'A': p['eta']=0.914; p['Emax']=30.0
    else:           p['eta']=2.756; p['Emax']=26.0
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
        return np.array([R - pa[2]*E_*N_, Zdot, bracket, -B + pa[12]*(Aeq - A_)])
    st = np.array([N, Z, E1, A])
    h = 1e-6
    J = np.zeros((4,4))
    for j in range(4):
        sp_ = st.copy(); sm = st.copy(); sp_[j]+=h; sm[j]-=h
        J[:,j] = (rhs(sp_[0],sp_[1],sp_[2],sp_[3], Z) - rhs(sm[0],sm[1],sm[2],sm[3], Z))/(2*h)
    dEdZ = pa[3]*E1/pa[6] + pa[9]*pa[8]/(pa[8]+Z)**2
    Bd = np.zeros((4,4)); Bd[2,1] = dEdZ
    ev0 = np.linalg.eigvals(J + Bd)
    th = hopf_thresholds(J, Bd, w_lo=1e-4, w_hi=3.0, nw=12000, nmax=6)
    print(f"\n[{label}] N*={N:.6f} A*={A:.6f} E*={E1:.6f}")
    print(f"  tau=0 eig: {np.round(ev0,6)}")
    print(f"  Hopf tau: {[round(t,4) for t,w in th[:6]]}")
    return th

print("=== sanity: Candidate A, donor-limited (expect tau-=6.982022, tau+=132.272044) ===")
run('A', 1, "Candidate A donor-limited")
print("\n=== Candidate A, old undivided B (expect 6.985285/132.268712?) ===")
run('A', 0, "Candidate A old-B")
print("\n=== Candidate B, donor-limited (the claim: fold 76.98, tau+=99.79) ===")
run('B', 1, "Candidate B donor-limited")
print("\n=== Candidate B, old undivided B ===")
run('B', 0, "Candidate B old-B")
