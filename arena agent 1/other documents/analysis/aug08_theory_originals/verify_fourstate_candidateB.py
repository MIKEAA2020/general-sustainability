"""Verify the four-state core at Candidate B (eta=2.756, Emax=26):
   equilibrium, tau=0 eigenvalues, Hopf thresholds (ungated law,
   donor-limited equilibrium) -- the manuscript's line-1254 claim
   tau_SNPO,R~76.98, tau_+=99.79 for Candidate B."""
import numpy as np, sys
sys.path.insert(0, 'verification_scripts')
from fourstate_pipeline import FOUR_PARAMS, four_arr, softplus_stable
from verify_kappaA_sweep import hopf_thresholds
from close_d12_fourstate_gated import equilibrium_gated

p = FOUR_PARAMS()
p['eta'] = 2.756; p['Emax'] = 26.0
pa = four_arr(p)
Z = p['delta']
N, A, E1, Aeq = equilibrium_gated(p, donor=1)
print(f"Equilibrium: N*={N:.10f} A*={A:.10f} E*={E1:.10f} Z*={Z:.6f}")

def rhs_ung(N_, Z_, E_, A_, Ztau, pa):
    r_,K_,q_ = pa[0],pa[1],pa[2]
    eta_,Emax_,Dref_ = pa[3],pa[4],pa[6]
    delta0_,Zref_,k_,taum_ = pa[9],pa[8],pa[7],pa[5]
    R = r_*N_*(1-N_/K_)*A_/(A_+pa[14])
    B = R + pa[11]*N_*A_/(A_+pa[14])
    u = q_*E_*N_ - R
    sp = softplus_stable(u, k_)
    inner = sp - np.log(2.0)/k_ + pa[10]
    Zdot = ((inner if inner>0 else 0.0) - Z_)/taum_
    bracket = eta_*E_*(Ztau/Dref_ - E_/Emax_) + delta0_*Ztau/(Zref_+Ztau)
    return np.array([R - q_*E_*N_, Zdot, bracket, -B + pa[12]*(Aeq - A_)])

st = np.array([N, Z, E1, A])
h = 1e-6
J = np.zeros((4,4))
for j in range(4):
    sp_ = st.copy(); sm = st.copy(); sp_[j]+=h; sm[j]-=h
    fp = rhs_ung(sp_[0],sp_[1],sp_[2],sp_[3], Z, pa)   # Ztau fixed at equilibrium Z
    fm = rhs_ung(sm[0],sm[1],sm[2],sm[3], Z, pa)
    J[:,j] = (fp-fm)/(2*h)
dEdZ = pa[3]*E1/pa[6] + pa[9]*pa[8]/(pa[8]+Z)**2      # ungated dEdot/dZ_tau
Bd = np.zeros((4,4)); Bd[2,1] = dEdZ
ev0 = np.linalg.eigvals(J + Bd)
print("tau=0 eigenvalues (J+B):", np.round(ev0, 8))
print("  -> stable at tau=0:", all(ev0.real < 0))

th = hopf_thresholds(J, Bd, w_lo=1e-4, w_hi=3.0, nw=12000, nmax=8)
print("\nHopf thresholds (tau, omega):")
for tau, w in th:
    print(f"  tau = {tau:10.5f}   omega = {w:8.5f}   period = {2*np.pi/w:8.2f} yr")
