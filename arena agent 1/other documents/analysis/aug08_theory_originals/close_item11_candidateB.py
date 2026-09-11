"""Close open item: recompute Candidate B corrected (gated) Hopf thresholds and
the one-at-a-time parameter sweep under the corrected effort equation.
Manuscript: Candidate B (eta=2.756, Emax=26, delta0=0.01, Dref=1, taum=5):
  uncorrected  tau_-=6.2136, tau_+=76.2906
  corrected    tau_-~5.51, tau_+~80.42   (manuscript, Sec effort-saturation-fix)
  + the one-at-a-time parameter sweep over Table ranges "remain to be recomputed
    under the corrected equation" (Sec robustness-corrected).
Method: gated-core Jacobians + tau-free Hopf criterion |v^T(iwI-J0)^-1 u|=1
(reproducing Candidate A's 3.666/150.359 first as validation).
"""
import numpy as np
from corrected_core_common import PARAMS_A, PARAMS_B, equilibrium, softplus

LN2K = np.log(2.0)/10.0

def gated_jacobians(params):
    """J0, J1 (rank-1) for the corrected (gated) three-state core at equilibrium."""
    r_,K_,q_ = params['r'],params['K'],params['q']
    eta_,Emax_,Dref_ = params['eta'],params['Emax'],params['Dref']
    delta0_,Zref_,k_,taum_ = params['delta0'],params['Zref'],params['k'],params['taum']
    N,Z,E = equilibrium(params)
    Zden = Zref_+Z
    Sp = r_*(1-2*N/K_)
    # h = d/dd max(0, softplus(d)-ln2/k+delta) at equilibrium: softplus'(0)=1/2, floor active iff src<0
    h = 0.5
    J0 = np.zeros((3,3))
    J0[0,0]=Sp - q_*E
    J0[0,2]=-q_*N
    J0[1,0]=h*q_*E/taum_
    J0[1,1]=-1.0/taum_
    J0[1,2]=h*q_*N/taum_
    gate = 1 - E/Emax_
    bracket = eta_*E*(Z/Dref_ - E/Emax_) + delta0_*Z/Zden
    J0[2,2] = (-1/Emax_)*bracket + gate*eta_*(Z/Dref_ - 2*E/Emax_)
    J1 = np.zeros((3,3))
    J1[2,1] = gate*(eta_*E/Dref_ + delta0_*Zref_/(Zden*Zden))
    return J0, J1, equilibrium(params)

def hopf_crossings(params, wmin=1e-4, wmax=40.0, nw=20000):
    J0, J1, eq = gated_jacobians(params)
    u = np.array([0,0,1.0]); v = np.array([0.0, J1[2,1], 0.0])
    ws = np.geomspace(wmin, wmax, nw)
    gs = np.empty(nw, dtype=complex)
    for i,w in enumerate(ws):
        M = 1j*w*np.eye(3) - J0
        gs[i] = v @ np.linalg.solve(M, u)
    mag = np.abs(gs)
    sgn = np.sign(mag-1)
    out = []
    for i in range(nw-1):
        if sgn[i]*sgn[i+1] < 0:
            lo,hi = ws[i],ws[i+1]; glo,ghi = gs[i],gs[i+1]
            for _ in range(80):
                mid = np.sqrt(lo*hi)
                M = 1j*mid*np.eye(3)-J0
                gm = v @ np.linalg.solve(M,u)
                if (abs(gm)-1)*(abs(glo)-1) <= 0: hi=mid; ghi=gm
                else: lo=mid; glo=gm
            wc = np.sqrt(lo*hi)
            M = 1j*wc*np.eye(3)-J0
            gc = v @ np.linalg.solve(M,u)
            tau0 = (np.angle(gc) % (2*np.pi))/wc
            out.append((wc, tau0, 2*np.pi/wc))
    out.sort()
    return out, eq

def one_at_a_time(params, ranges):
    """Vary each parameter across its Table range, recompute tau_- (corrected)."""
    base = params.copy()
    results = {}
    for key,(lo,hi,n) in ranges.items():
        vals = np.linspace(lo,hi,n)
        taus = []
        for val in vals:
            pp = base.copy(); pp[key] = val
            cr, _ = hopf_crossings(pp, nw=8000)
            if cr: taus.append(cr[0][1])
        results[key] = (vals, np.array(taus))
    return results

if __name__ == "__main__":
    # 1. validate on Candidate A (must give 3.666 / 150.359)
    crA, eqA = hopf_crossings(PARAMS_A)
    print("Candidate A equilibrium:", np.round(eqA,6))
    print("Candidate A corrected Hopf:", [(round(t,4)) for _,t,_ in crA], " (manuscript 3.666/150.359)")

    # 2. Candidate B corrected thresholds
    crB, eqB = hopf_crossings(PARAMS_B)
    print("\nCandidate B equilibrium:", np.round(eqB,6))
    print("Candidate B corrected Hopf:", [(round(t,4)) for _,t,_ in crB], " (manuscript ~5.51/80.42)")
