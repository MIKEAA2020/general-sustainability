"""Item 11 closure: Candidate B corrected thresholds (done) + one-at-a-time
parameter sweep under the corrected equation (the open item).
Ranges from Table tab:params for the core parameters.
"""
import numpy as np
from corrected_core_common import PARAMS_B, equilibrium, rhs_corrected

def fd_jacobians(params, h=1e-7):
    eq = np.array(equilibrium(params), float)
    def f(y, yd):
        return np.array(rhs_corrected(y[0], y[1], yd[1], y[2], params), float)
    J0 = np.zeros((3,3)); J1 = np.zeros((3,3))
    for j in range(3):
        ep = eq.copy(); em = eq.copy(); ep[j]+=h; em[j]-=h
        J0[:,j] = (f(ep,eq)-f(em,eq))/(2*h)
        ep2 = eq.copy(); em2 = eq.copy(); ep2[j]+=h; em2[j]-=h
        J1[:,j] = (f(eq,ep2)-f(eq,em2))/(2*h)
    return J0, J1, eq

def hopf_taus(params, wmin=1e-4, wmax=60.0, nw=25000, nmax=3):
    J0,J1,eq = fd_jacobians(params)
    nz = np.argwhere(np.abs(J1)>1e-12)
    if len(nz)==0: return []
    i,j = nz[0]; c = J1[i,j]
    u = np.zeros(3); u[i]=1.0
    v = np.zeros(3); v[j]=c
    ws = np.geomspace(wmin,wmax,nw)
    gs = np.empty(nw,complex)
    for k,w in enumerate(ws):
        M = 1j*w*np.eye(3)-J0
        gs[k] = v @ np.linalg.solve(M,u)
    mag = np.abs(gs); sgn = np.sign(mag-1)
    out = []
    for k in range(nw-1):
        if sgn[k]*sgn[k+1]<0:
            lo,hi = ws[k],ws[k+1]; glo,ghi = gs[k],gs[k+1]
            for _ in range(80):
                mid = np.sqrt(lo*hi)
                M = 1j*mid*np.eye(3)-J0
                gm = v@np.linalg.solve(M,u)
                if (abs(gm)-1)*(abs(glo)-1)<=0: hi=mid; ghi=gm
                else: lo=mid; glo=gm
            wc = np.sqrt(lo*hi)
            M = 1j*wc*np.eye(3)-J0
            gc = v@np.linalg.solve(M,u)
            out.append((np.angle(gc)%(2*np.pi))/wc)
    out.sort()
    return out[:nmax]

if __name__ == "__main__":
    print("Candidate B baseline corrected Hopf:", [round(t,4) for t in hopf_taus(PARAMS_B)])
    # one-at-a-time sweep: vary each core parameter across its Table range
    ranges = {
        'r':       (0.01, 0.05, 9),
        'eta':     (0.5, 3.0, 9),
        'Emax':    (15.0, 50.0, 8),
        'Dref':    (0.5, 5.0, 9),
        'delta0':  (0.005, 0.05, 9),
        'taum':    (2.0, 15.0, 9),
        'Zref':    (0.5, 5.0, 9),
        'k':       (5.0, 50.0, 8),
    }
    print("\none-at-a-time sweep under CORRECTED equation (Candidate B):")
    print(f"{'param':>7s} {'range':>14s} {'tau_- min':>9s} {'tau_- max':>9s} {'tau_+ min':>9s} {'tau_+ max':>9s} {'safe-window':>12s}")
    for key,(lo,hi,n) in ranges.items():
        taus_m, taus_p = [], []
        for val in np.linspace(lo,hi,n):
            pp = PARAMS_B.copy(); pp[key]=val
            cr = hopf_taus(pp, nw=15000)
            if len(cr)>=2:
                taus_m.append(cr[0]); taus_p.append(cr[1])
            elif len(cr)==1:
                taus_m.append(cr[0])
        if taus_m and taus_p:
            w = min(taus_p)-max(taus_m)
            print(f"{key:>7s} [{lo:6.2g},{hi:6.2g}] {min(taus_m):9.3f} {max(taus_m):9.3f} "
                  f"{min(taus_p):9.3f} {max(taus_p):9.3f} {w:12.2f}")
        else:
            print(f"{key:>7s} [{lo:6.2g},{hi:6.2g}]  (no full pair at some points)")
