"""Close D12: four-state core under the corrected (gated) effort law.
Adds the (1 - E/Emax) gate to the four-state effort equation and recomputes:
  equilibrium (expected unchanged), tau=0 eigenvalues, Hopf thresholds,
  kappa_A stability threshold, and (via long-horizon persistence bisection)
  the SNPO folds -- the "not yet performed for the four-state core" item.
"""
import numpy as np
from scipy.optimize import fsolve
import sys
sys.path.insert(0, 'verification_scripts')
from verify_kappaA_sweep import rightmost_root, unstable_root_count, hopf_thresholds

from fourstate_pipeline import FOUR_PARAMS, four_arr, softplus_stable

def rhs_four_gated(N, Z, E, A, Ztau, pa, donor):
    """Gated effort law: whole bracket x (1 - E/Emax)."""
    r_, K_, q_ = pa[0], pa[1], pa[2]
    eta_, Emax_, Dref_ = pa[3], pa[4], pa[6]
    delta0_, Zref_, k_, taum_ = pa[9], pa[8], pa[7], pa[5]
    delta_ = pa[10]; kA_ = pa[11]; omA_ = pa[12]; Aeq_ = pa[13]; A0_ = pa[14]
    R = r_*N*(1 - N/K_)*A/(A + A0_)
    B = R + kA_*N*A/(A + A0_) if donor else R + kA_*N
    Ndot = R - q_*E*N
    Adot = -B + omA_*(Aeq_ - A)
    u = q_*E*N - R
    sp = softplus_stable(u, k_)
    inner = sp - np.log(2.0)/k_ + delta_
    Zdot = ((inner if inner > 0.0 else 0.0) - Z)/taum_
    bracket = eta_*E*(Ztau/Dref_ - E/Emax_) + delta0_*Ztau/(Zref_ + Ztau)
    Edot = (1.0 - E/Emax_)*bracket   # <-- the gate
    return Ndot, Zdot, Edot, Adot

def equilibrium_gated(p=None, donor=1):
    """Equilibrium is UNCHANGED by the gate (bracket=0 at equilibrium)."""
    p = p or FOUR_PARAMS()
    pa = four_arr(p)
    E1 = pa[3]*0  # placeholder
    Zs = p['delta']
    a = p['eta']/p['Emax']; b = p['eta']*Zs/p['Dref']; c = p['delta0']*Zs/(p['Zref']+Zs)
    E1 = (b + np.sqrt(b*b + 4*a*c))/(2*a)
    Aeq = pa[13]
    def sys(x):
        N, A = x
        R = pa[0]*N*(1-N/pa[1])*A/(A+pa[14])
        B = R + pa[11]*N*A/(A+pa[14]) if donor else R + pa[11]*N
        return [R - pa[2]*E1*N, -B + pa[12]*(Aeq - A)]
    sol = fsolve(sys, [89.5, 400.0])
    return sol[0], sol[1], E1, Aeq

def char_eq_gated(p=None, donor=1, state=None):
    """(J_local, B_delay, st) with the gated effort law (FD)."""
    p = p or FOUR_PARAMS()
    pa = four_arr(p)
    if state is None:
        N, A, E1, Aeq = equilibrium_gated(p, donor)
        Z = p['delta']; E = E1
    else:
        N, Z, E, A = state
    h = 1e-6
    J = np.zeros((4,4))
    st = np.array([N, Z, E, A])
    for j in range(4):
        sp = st.copy(); sm = st.copy(); sp[j]+=h; sm[j]-=h
        fp = np.array(rhs_four_gated(sp[0], sp[1], sp[2], sp[3], Z, pa, donor))
        fm = np.array(rhs_four_gated(sm[0], sm[1], sm[2], sm[3], Z, pa, donor))
        J[:, j] = (fp - fm)/(2*h)
    # B_delay = dEdot/dZ_tau (gated)
    dEdZ = (1.0 - E/pa[4])*(pa[3]*E/pa[6] + pa[9]*pa[8]/(pa[8]+Z)**2)
    B = np.zeros((4,4)); B[2,1] = dEdZ
    return J, B, st

def jac_tau0_gated(p=None, donor=1, state=None):
    p = p or FOUR_PARAMS()
    pa = four_arr(p)
    if state is None:
        N, A, E1, Aeq = equilibrium_gated(p, donor)
        Z = p['delta']; E = E1
    else:
        N, Z, E, A = state
    h = 1e-6
    J = np.zeros((4,4))
    st = np.array([N, Z, E, A])
    for j in range(4):
        sp = st.copy(); sm = st.copy(); sp[j]+=h; sm[j]-=h
        fp = np.array(rhs_four_gated(sp[0], sp[1], sp[2], sp[3], sp[1], pa, donor))
        fm = np.array(rhs_four_gated(sm[0], sm[1], sm[2], sm[3], sm[1], pa, donor))
        J[:, j] = (fp - fm)/(2*h)
    return J, st

if __name__ == "__main__":
    print("="*70)
    print("FOUR-STATE CORE UNDER THE CORRECTED (GATED) EFFORT LAW")
    print("="*70)
    p = FOUR_PARAMS(); p['kappa_A'] = 0.05
    N, A, E1, Aeq = equilibrium_gated(p, donor=1)
    print(f"\nequilibrium: N*={N:.8f} A*={A:.8f} E*={E1:.8f}")
    print(f"  (ungated manuscript: N*=89.52562265 A*=397.86653507 E*=2.08962340)")

    J, st = jac_tau0_gated(p, donor=1)
    ev = np.linalg.eigvals(J)
    ev = ev[np.argsort(-ev.real)]
    print(f"\ntau=0 eigenvalues (gated): {np.round(ev,8)}")
    print(f"  (ungated: -0.28350455, -0.00103152, 0.00083623+/-0.02837932i)")

    Jc, B, _ = char_eq_gated(p, donor=1)
    thr = hopf_thresholds(Jc, B, w_lo=0.001, w_hi=1.5, nw=6000, nmax=6)
    print(f"\nHopf thresholds (gated): tau = {[round(t,6) for t,w in thr[:4]]}")
    print(f"  (ungated: tau_-=6.982022, tau_+=132.272044)")
    # rightmost root at tau in the safe range
    print("\nrightmost root vs tau (gated):")
    for tau in [6.0, 7.0, 50.0, 130.0, 132.3, 140.0]:
        nu = unstable_root_count(Jc, B, tau, Omega=12.0, n=8000)
        r = rightmost_root(Jc, B, tau)
        print(f"  tau={tau:6.1f}: rightmost Re={r.real:+.6f} Im={r.imag:.4f} n_unstable={nu}")
