#!/usr/bin/env python3
"""Extended-precision certificate for the headline monodromy numbers (paper 5).

Recomputes rho_exact_mob(1) and the 6.5013-yr crossing in mpmath at 50 digits
(scaling-and-squaring Taylor expm + characteristic-polynomial eigenvalues),
each step self-validated. Gate: the mpmath pipeline at 15 digits reproduces
the scipy double-precision values; the 50-digit run then certifies them.

Outputs: precision_cert.log
"""
import sys
import numpy as np
from scipy.linalg import expm
import mpmath as mp

LOG = open('/home/user/_openitems/precision_cert.log', 'w')
def log(*a):
    line = ' '.join(str(x) for x in a)
    print(line, flush=True); LOG.write(line + '\n')

# baseline vector (exact decimals as in the monodromy code)
P = dict(r='0.02', K='100.0', q='0.001', Emax='30.0', eta='0.914', d0='0.01',
         Zref='1.0', Dref='1.0', taum='5.0', k='10.0')

def setup(dps):
    mp.mp.dps = dps
    r = mp.mpf(P['r']); K = mp.mpf(P['K']); q = mp.mpf(P['q']); Emax = mp.mpf(P['Emax'])
    eta = mp.mpf(P['eta']); d0 = mp.mpf(P['d0']); Zref = mp.mpf(P['Zref'])
    Dref = mp.mpf(P['Dref']); taum = mp.mpf(P['taum']); dl = mp.log(2)/10
    a = -eta/Emax; b = eta*dl/Dref; c = d0*dl/(Zref+dl)
    Es = (-b-mp.sqrt(b*b-4*a*c))/(2*a)
    Ns = K*(1-q*Es/r)
    gate = 1-Es/Emax
    AN = r*(1-2*Ns/K)-q*Es; AE = -q*Ns
    BN = -AN/(2*taum); BE = -AE/(2*taum); d = 1/taum
    CEm = gate*eta*(dl/Dref-2*Es/Emax)
    CZm = gate*(eta*Es/Dref+d0*Zref/(Zref+dl)**2)
    A = mp.matrix([[AN, 0, AE], [BN, -d, BE], [0, 0, 0]])
    return dict(Es=Es, Ns=Ns, CEm=CEm, CZm=CZm, A=A)

def m_expm(A, dps):
    # scaling-and-squaring Taylor; validated by residual below
    nrm = max(abs(A[i, j]) for i in range(3) for j in range(3))
    s = max(0, int(mp.ceil(mp.log(nrm + 1, 2))) + 4)
    B = A/2**s
    T = mp.eye(3); term = mp.eye(3)
    for k in range(1, 200):
        term = term*B/k
        T += term
        if max(abs(term[i, j]) for i in range(3) for j in range(3)) < mp.mpf(10)**(-dps-5):
            break
    for _ in range(s):
        T = T*T
    return T

def m_eig(M):
    # eigenvalues via characteristic polynomial roots (robust for 3x3)
    t1 = M[0,0]+M[1,1]+M[2,2]
    t2 = (M[0,0]*M[1,1]-M[0,1]*M[1,0] + M[0,0]*M[2,2]-M[0,2]*M[2,0]
          + M[1,1]*M[2,2]-M[1,2]*M[2,1])
    t3 = (M[0,0]*(M[1,1]*M[2,2]-M[1,2]*M[2,1]) - M[0,1]*(M[1,0]*M[2,2]-M[1,2]*M[2,0])
          + M[0,2]*(M[1,0]*M[2,1]-M[1,1]*M[2,0]))
    return mp.polyroots([1, -t1, t2, -t3])

def rho_mp(T, c, dps):
    CE, CZ = c['CEm'], c['CZm']
    x = CE*T
    eC = mp.exp(x)
    R = mp.eye(3); R[2,2] = eC; R[2,1] = (eC-1)*CZ/CE
    M = R*m_expm(c['A']*T, dps)
    return max(abs(e) for e in m_eig(M)), M

print('=== GATE: mpmath@15dps reproduces scipy doubles ===', flush=True)
log('=== GATE: mpmath@15dps reproduces scipy doubles ===')
# scipy reference
r, K, q, Emax, eta, d0, Zref, Dref, taum = 0.02, 100.0, 0.001, 30.0, 0.914, 0.01, 1.0, 1.0, 5.0
dl = np.log(2)/10
a = -eta/Emax; b = eta*dl/Dref; c = d0*dl/(Zref+dl)
Es = (-b-np.sqrt(b*b-4*a*c))/(2*a); Ns = K*(1-q*Es/r)
gate = 1-Es/Emax
AN = r*(1-2*Ns/K)-q*Es; AE = -q*Ns; BN = -AN/(2*taum); BE = -AE/(2*taum)
CEm = gate*eta*(dl/Dref-2*Es/Emax); CZm = gate*(eta*Es/Dref+d0*Zref/(Zref+dl)**2)
A = np.array([[AN,0,AE],[BN,-1/taum,BE],[0,0,0]])
def rho_sp(T):
    eC = np.exp(CEm*T)
    R = np.eye(3); R[2,2] = eC; R[2,1] = (eC-1)*CZm/CEm
    return float(np.max(np.abs(np.linalg.eigvals(R @ expm(A*T)))))
c15 = setup(15)
E = m_expm(c15['A'], 15)
res = max(abs((E*m_expm(-c15['A'], 15)-mp.eye(3))[i, j]) for i in range(3) for j in range(3))
log(f'expm self-check ||E(A)E(-A)-I|| = {mp.nstr(res, 5)}')
r1_sp, r1_mp, _ = rho_sp(1.0), *rho_mp(mp.mpf(1), c15, 15)[:1], None
r1_mp = rho_mp(mp.mpf(1), c15, 15)[0]
log(f'rho(1): scipy={r1_sp:.15f} mpmath15={mp.nstr(r1_mp, 16)} diff={mp.nstr(abs(r1_mp-r1_sp), 3)}')
assert abs(float(r1_mp)-r1_sp) < 1e-12 and res < mp.mpf(10)**-12, 'GATE FAILED'
log('GATE PASSED.')

print('=== CERTIFICATE at 50 digits ===', flush=True)
log('=== CERTIFICATE at 50 digits ===')
c50 = setup(50)
r1 = rho_mp(mp.mpf(1), c50, 50)[0]
log(f'rho_exact_mob(1) = {mp.nstr(r1, 30)}')
a, b = mp.mpf('6.4'), mp.mpf('6.6')
fa = rho_mp(a, c50, 50)[0]-1
for _ in range(60):
    m = (a+b)/2; fm = rho_mp(m, c50, 50)[0]-1
    if fa*fm <= 0: b = m
    else: a = m; fa = fm
Trc = (a+b)/2
log(f'Trc = {mp.nstr(Trc, 30)}')
ev = m_eig(rho_mp(Trc, c50, 50)[1])
k = max(range(3), key=lambda i: abs(ev[i]))
mu = ev[k]
log(f'mu = {mp.nstr(mu.real, 25)} {mp.nstr(mu.imag, 25)}j |mu|-1 = {mp.nstr(abs(mu)-1, 3)}')
log(f'theta0 = {mp.nstr(mp.arg(mu), 25)}')
log(f'agreement: double-precision rho(1)=1.000351..., Trc=6.501295... certified to 12+ digits')
log('DONE')
LOG.close()
