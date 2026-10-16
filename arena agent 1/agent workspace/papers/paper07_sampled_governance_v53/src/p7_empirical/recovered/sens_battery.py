#!/usr/bin/env python3
"""Sensitivity battery + F-reparameterisation grid for the logistic hold-map core (paper 5, S3.4).

Self-contained monodromy core (same mathematics as the validated
repo_p4_exact_hold_monodromy.py): equilibrium solve -> Jacobian blocks ->
gains -> A_hold -> R(Tr) @ expm(A_hold*Tr) -> multipliers.

Steps:
  1. VALIDATION GATE: reproduce all committed numbers BEFORE extension:
     rho(1) = 1.00035/1.00055/0.9838/0.9967 (max), crossings
     6.501/47.536/79.143/2.306.
  2. Baseline records: crossing angle theta0, continuous (undelayed)
     eigenvalues lambda via FD Jacobian of the ODE, Euler protective crossing.
  3. One-at-a-time battery: r,K,q,Emax,eta,d0,Zref,Dref,taum,delta x{0.9,0.95,1.05,1.1}.
  4. F-grid: q log-scan (F* = q*E*) at fixed remaining vector.
  5. Robustness: scan-density check (20k vs 200k), CE->0 limit check.
  6. Figure: rho(Tr) curves for the 4 update x channel combos + CSV.

Outputs: sens_battery.log, sens_table.csv, fgrid_table.csv, rho_scan_v39.csv,
         fig_rho_scan_v39.png
"""
import csv, math, sys
import numpy as np
from scipy.linalg import expm

LOG = open('/home/user/_openitems/sens_battery.log', 'w')
def log(*a):
    line = ' '.join(str(x) for x in a)
    print(line, flush=True); LOG.write(line + '\n')

BASE = dict(r=0.02, K=100.0, q=0.001, Emax=30.0, eta=0.914, d0=0.01,
            Zref=1.0, Dref=1.0, taum=5.0, delta=math.log(2)/10.0, k=10.0)

def equilibrium(p):
    r, K, q, Emax, eta = p['r'], p['K'], p['q'], p['Emax'], p['eta']
    d0, Zref, Dref, dl = p['d0'], p['Zref'], p['Dref'], p['delta']
    alpha = -eta/Emax; b = eta*dl/Dref; c = d0*dl/(Zref+dl)
    Estar = (-b - math.sqrt(b*b - 4*alpha*c))/(2*alpha)
    Nstar = K*(1 - q*Estar/r)
    return Estar, Nstar, dl

def core(p):
    """Return dict with equilibrium, gains, A_hold. Raises ValueError if inadmissible."""
    r, K, q, Emax, eta = p['r'], p['K'], p['q'], p['Emax'], p['eta']
    d0, Zref, Dref, taum, dl = p['d0'], p['Zref'], p['Dref'], p['taum'], p['delta']
    Estar, Nstar, Zstar = equilibrium(p)
    if not (Estar > 0 and Nstar > 0 and Estar < Emax):
        raise ValueError(f'inadmissible eq: E*={Estar:.4g} N*={Nstar:.4g}')
    A_N = r*(1 - 2*Nstar/K) - q*Estar
    A_E = -q*Nstar
    Sstar = r*Nstar*(1 - Nstar/K)
    Ystar = q*Estar*Nstar
    gate = 1 - Estar/Emax
    dPhidY = 1/(1 + math.exp(-p['k']*(Ystar - Sstar)))
    B_N = dPhidY*(q*Estar - r + 2*r*Nstar/K)/taum
    B_E = dPhidY*q*Nstar/taum
    dZ = -1/taum
    dFBdZ = gate*(eta*Estar/Dref + d0*Zref/(Zref+dl)**2)
    CEm = gate*eta*(dl/Dref - 2*Estar/Emax)  # bracket vanishes at eq (F_B=0 there)
    CEp = -(1 - Estar/Emax)*eta
    CZp = -(1 - Estar/Emax)*eta*Estar/(Zref+dl)
    A_hold = np.array([[A_N, 0.0, A_E],[B_N, dZ, B_E],[0.0,0.0,0.0]])
    return dict(Estar=Estar, Nstar=Nstar, Zstar=Zstar, Fstar=q*Estar,
                CEm=CEm, CZm=dFBdZ, CEp=CEp, CZp=CZp, A_hold=A_hold)

def R_exact(T, CE, CZ):
    x = CE*T
    c = (math.exp(x)-1.0)/CE if abs(CE) > 1e-12 else T*(1.0 + x/2.0)
    R = np.eye(3); R[2,2] = math.exp(x); R[2,1] = c*CZ
    return R

def R_euler(T, CE, CZ):
    R = np.eye(3); R[2,2] = 1.0 + CE*T; R[2,1] = T*CZ
    return R

def multipliers(T, c, CE, CZ, exact):
    R = R_exact(T,CE,CZ) if exact else R_euler(T,CE,CZ)
    return np.linalg.eigvals(R @ expm(c['A_hold']*T))

def rho(T, c, CE, CZ, exact):
    return float(np.max(np.abs(multipliers(T, c, CE, CZ, exact))))

def first_crossing(c, CE, CZ, exact, lo=0.2, hi=120.0, n=20001):
    Ts = np.linspace(lo, hi, n)
    prev = rho(Ts[0], c, CE, CZ, exact) - 1.0
    out = []
    for T in Ts[1:]:
        cur = rho(T, c, CE, CZ, exact) - 1.0
        if prev == 0: out.append((T,)); prev = cur; continue
        if cur*prev < 0:
            a, b = T-(Ts[1]-Ts[0]), T
            fa = rho(a, c, CE, CZ, exact)-1.0
            for _ in range(60):
                m = 0.5*(a+b); fm = rho(m, c, CE, CZ, exact)-1.0
                if fa*fm <= 0: b = m
                else: a = m; fa = fm
            Tc = 0.5*(a+b)
            ev = multipliers(Tc, c, CE, CZ, exact)
            k = int(np.argmax(np.abs(ev))); mu = ev[k]
            kind = 'complex-pair' if abs(mu.imag) > 1e-6 else ('real +1' if mu.real > 0 else 'real -1')
            out.append((Tc, kind, float(mu.real), float(mu.imag),
                        float(np.angle(mu)), rho(0.5*(Tc+hi if len(out)==0 else Tc), c, CE, CZ, exact)))
        prev = cur
    return out

def max_rho(c, CE, CZ, exact, lo=0.2, hi=120.0, n=4001):
    return max(rho(T, c, CE, CZ, exact) for T in np.linspace(lo, hi, n))

print('=== 1. VALIDATION GATE (must reproduce committed numbers) ===', flush=True)
log('=== 1. VALIDATION GATE (must reproduce committed numbers) ===')
c = core(BASE)
log(f"E*={c['Estar']:.5f} N*={c['Nstar']:.5f} F*={c['Fstar']:.6f}")
log(f"gains mob CE={c['CEm']:.6f} CZ={c['CZm']:.6f} | prot CE={c['CEp']:.6f} CZ={c['CZp']:.6f}")
gate = []
def chk(name, got, want, tol):
    ok = abs(got-want) <= tol
    gate.append(ok)
    log(f"  {'OK ' if ok else 'FAIL'} {name}: got {got:.6f} want {want} tol {tol}")
xe = first_crossing(c, c['CEm'], c['CZm'], True)
xu = first_crossing(c, c['CEm'], c['CZm'], False)
xp = first_crossing(c, c['CEp'], c['CZp'], False)
chk('rho_exact_mob(1)', rho(1.0,c,c['CEm'],c['CZm'],True), 1.00035, 1e-5)
chk('rho_euler_mob(1)', rho(1.0,c,c['CEm'],c['CZm'],False), 1.00055, 1e-5)
chk('rho_euler_prot(1)', rho(1.0,c,c['CEp'],c['CZp'],False), 0.9838, 1e-4)
chk('max_rho_exact_prot', max_rho(c,c['CEp'],c['CZp'],True), 0.9967, 1e-4)
chk('Trc_exact', xe[0][0], 6.501, 1e-3)
chk('Trc_euler_1', xu[0][0], 47.536, 1e-3)
chk('Trc_euler_2', xu[1][0], 79.143, 1e-3)
chk('Trc_euler_prot', xp[0][0], 2.306, 1e-3)
log('exact mob kinds:', [(round(t,4),k) for t,k,_,_,_,_ in xe])
log('euler mob kinds:', [(round(t,4),k) for t,k,_,_,_,_ in xu])
log('euler prot kinds:', [(round(t,4),k) for t,k,_,_,_,_ in xp])
if not all(gate):
    log('GATE FAILED - aborting before extension'); sys.exit(1)
log('GATE PASSED - all 8 committed values reproduced.')

print('=== 2. BASELINE RECORDS ===', flush=True)
log('=== 2. BASELINE RECORDS ===')
Tc, kind, re_, im_, th, _ = xe[0]
log(f'theta0 at exact crossing: {th:.6f} rad = {th/math.pi:.6f} pi (|mu|={math.hypot(re_,im_):.8f})')
# continuous (undelayed) eigenvalues: FD Jacobian of the ODE at eq
def rhs(X, p):
    N, Z, E = X
    r,K,q,Emax,eta,d0,Zref,Dref,taum,dl,k = (p['r'],p['K'],p['q'],p['Emax'],p['eta'],p['d0'],p['Zref'],p['Dref'],p['taum'],p['delta'],p['k'])
    S = r*N*(1-N/K); Y = q*E*N
    Phi = max(0.0, math.log1p(math.exp(k*(Y-S)))/k - math.log(2)/k + dl)
    dN = r*N*(1-N/K) - q*E*N
    dZ = (Phi - Z)/taum
    gate = 1 - E/Emax
    dE = gate*(eta*E*(Z/Dref - E/Emax) + d0*Z/(Zref+Z))
    return np.array([dN, dZ, dE])
X0 = np.array([c['Estar'] and c['Nstar'], c['Zstar'], c['Estar']])
h = 1e-7
J = np.zeros((3,3))
for j in range(3):
    d = np.zeros(3); d[j] = h*max(1.0, abs(X0[j]))
    J[:,j] = (rhs(X0+d, BASE)-rhs(X0-d, BASE))/(2*d[j])
lam = np.linalg.eigvals(J)
log('continuous eigenvalues lambda:', [f'{l.real:.6f}{l.imag:+.6f}j' for l in lam])
log('max Re(lambda):', f'{max(l.real for l in lam):.6f}')
# CE -> 0 limit check
for ce in (1e-13, 0.0):
    T = 1.0
    x = ce*T
    cval = (math.exp(x)-1.0)/x if abs(x) > 1e-12 else T*(1.0+x/2.0)
    log(f'CE={ce}: (e^CT-1)/C = {cval:.12f} vs T=1 limit-err {abs(cval-T):.2e}')
# grid-density robustness: 20k vs 200k coarse grids
xe_coarse = first_crossing(c, c['CEm'], c['CZm'], True, n=2001)
xe_fine = first_crossing(c, c['CEm'], c['CZm'], True, n=200001)
log(f"grid check exact Trc: n=2001 -> {xe_coarse[0][0]:.6f}, n=20001 -> {xe[0][0]:.6f}, n=200001 -> {xe_fine[0][0]:.6f}")

print('=== 3. ONE-AT-A-TIME BATTERY ===', flush=True)
log('=== 3. ONE-AT-A-TIME BATTERY ===')
rows = []
hdr = ['param','factor','Estar','Nstar','Fstar','rho_ex_1','rho_eu_1','Trc_exact','theta0','kind','prot_max','flag']
base_row = ['baseline','1.0', f"{c['Estar']:.6f}", f"{c['Nstar']:.6f}", f"{c['Fstar']:.6f}",
    f"{rho(1.0,c,c['CEm'],c['CZm'],True):.6f}", f"{rho(1.0,c,c['CEm'],c['CZm'],False):.6f}",
    f"{xe[0][0]:.4f}", f"{xe[0][4]:.6f}", xe[0][1], f"{max_rho(c,c['CEp'],c['CZp'],True):.6f}", 'ok']
rows.append(base_row)
for par in ['r','K','q','Emax','eta','d0','Zref','Dref','taum','delta']:
    for f in (0.9, 0.95, 1.05, 1.1):
        p = dict(BASE); p[par] *= f
        try:
            cc = core(p)
            r1 = rho(1.0,cc,cc['CEm'],cc['CZm'],True); r2 = rho(1.0,cc,cc['CEm'],cc['CZm'],False)
            xs = first_crossing(cc, cc['CEm'], cc['CZm'], True, n=4001)
            pm = max_rho(cc,cc['CEp'],cc['CZp'],True, n=2001)
            if xs: Trc, th0, kk = f'{xs[0][0]:.4f}', f'{xs[0][4]:.6f}', xs[0][1]
            else: Trc, th0, kk = 'none', '-', '-'
            rows.append([par, str(f), f"{cc['Estar']:.6f}", f"{cc['Nstar']:.6f}", f"{cc['Fstar']:.6f}",
                         f'{r1:.6f}', f'{r2:.6f}', Trc, th0, kk, f'{pm:.6f}', 'ok'])
            log(f'{par} x{f}: E*={cc["Estar"]:.4f} F*={cc["Fstar"]:.5f} rho_ex(1)={r1:.6f} Trc={Trc} protmax={pm:.6f}')
        except ValueError as e:
            rows.append([par, str(f), '-', '-', '-', '-', '-', '-', '-', '-', '-', f'INVALID:{e}'])
            log(f'{par} x{f}: INVALID ({e})')
with open('/home/user/_openitems/sens_table.csv','w',newline='') as f:
    csv.writer(f).writerows([hdr]+rows)

print('=== 4. F-GRID (q log-scan) ===', flush=True)
log('=== 4. F-GRID (q log-scan) ===')
frows = [hdr]
for q in np.logspace(-4, -1, 13):
    p = dict(BASE); p['q'] = float(q)
    try:
        cc = core(p)
        r1 = rho(1.0,cc,cc['CEm'],cc['CZm'],True); r2 = rho(1.0,cc,cc['CEm'],cc['CZm'],False)
        xs = first_crossing(cc, cc['CEm'], cc['CZm'], True, n=4001)
        pm = max_rho(cc,cc['CEp'],cc['CZp'],True, n=2001)
        if xs: Trc, th0, kk = f'{xs[0][0]:.4f}', f'{xs[0][4]:.6f}', xs[0][1]
        else: Trc, th0, kk = 'none', '-', '-'
        frows.append(['q', f'{q:.4g}', f"{cc['Estar']:.6f}", f"{cc['Nstar']:.6f}", f"{cc['Fstar']:.6f}",
                      f'{r1:.6f}', f'{r2:.6f}', Trc, th0, kk, f'{pm:.6f}', 'ok'])
        log(f"q={q:.4g}: E*={cc['Estar']:.4f} F*={cc['Fstar']:.6f} rho_ex(1)={r1:.6f} Trc={Trc}")
    except ValueError as e:
        frows.append(['q', f'{q:.4g}', '-', '-', '-', '-', '-', '-', '-', '-', '-', f'INVALID:{e}'])
        log(f'q={q:.4g}: INVALID ({e})')
with open('/home/user/_openitems/fgrid_table.csv','w',newline='') as f:
    csv.writer(f).writerows(frows)

print('=== 5. RHO-SCAN FIGURE ===', flush=True)
log('=== 5. RHO-SCAN FIGURE ===')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
Ts = np.logspace(math.log10(0.2), math.log10(120), 400)
series = {
  'exact mobilising': [rho(T,c,c['CEm'],c['CZm'],True) for T in Ts],
  'Euler mobilising': [rho(T,c,c['CEm'],c['CZm'],False) for T in Ts],
  'exact protective': [rho(T,c,c['CEp'],c['CZp'],True) for T in Ts],
  'Euler protective': [rho(T,c,c['CEp'],c['CZp'],False) for T in Ts],
}
with open('/home/user/_openitems/rho_scan_v39.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Tr']+list(series.keys()))
    for i,T in enumerate(Ts): w.writerow([f'{T:.6f}']+[f'{series[k][i]:.6f}' for k in series])
fig, ax = plt.subplots(figsize=(7.2, 4.6))
for k, v in series.items():
    ax.semilogx(Ts, v, label=k, linewidth=1.6 if 'exact mob' in k else 1.1,
                linestyle='-' if 'exact' in k else '--')
ax.axhline(1.0, color='k', linewidth=0.8)
for Tc in (6.501, 47.536, 79.143, 2.306): ax.axvline(Tc, color='grey', linewidth=0.6, linestyle=':')
ax.axvline(1.0, color='k', linewidth=0.8, linestyle=':')
ax.set_xlabel('review interval Tr (yr)'); ax.set_ylabel('spectral radius rho(Tr)')
ax.set_title('Multiplier spectral radius vs review interval (baseline vector)')
ax.legend(fontsize=8, loc='best'); ax.set_ylim(0.9, 1.35)
fig.tight_layout(); fig.savefig('/home/user/_openitems/fig_rho_scan_v39.png', dpi=150)
log('wrote fig_rho_scan_v39.png + rho_scan_v39.csv')
log('DONE')
LOG.close()
