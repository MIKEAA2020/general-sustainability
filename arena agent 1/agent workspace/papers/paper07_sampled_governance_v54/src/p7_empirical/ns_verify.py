#!/usr/bin/env python3
"""Neimark-Sacker verification for the exact-update crossing at Tr=6.501 yr (paper 5, S3.4).

Nonlinear sampled (flow-then-update) map with effort held over each review
interval; Euler and exact held-assessment updates. Steps:
  1. GATE: FD Jacobian of the nonlinear map == monodromy R@expm(A_hold*Tr)
     at Tr=1 and Tr=6.5013 (both updates); fixed-point residual ~ 0.
  2. FD Hessian + third derivatives with step-convergence study at Trc.
  3. Kuznetsov NS normal-form coefficient a(0), transversality d|mu|/dTr,
     non-resonance checks (k=1..4).
  4. Invariant-circle hunt: long iteration on both sides of Trc, amplitude
     scaling, rotation number.

Outputs: ns_verify.log, fig_nscircle_v39.png (only if circle evidence found).
"""
import math, sys
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp

LOG = open('/home/user/_openitems/ns_verify.log', 'w')
def log(*a):
    line = ' '.join(str(x) for x in a)
    print(line, flush=True); LOG.write(line + '\n')

P = dict(r=0.02, K=100.0, q=0.001, Emax=30.0, eta=0.914, d0=0.01,
         Zref=1.0, Dref=1.0, taum=5.0, delta=math.log(2)/10.0, k=10.0)

def equilibrium(p):
    r,K,q,Emax,eta,d0,Zref,Dref,dl = (p['r'],p['K'],p['q'],p['Emax'],p['eta'],
        p['d0'],p['Zref'],p['Dref'],p['delta'])
    a = -eta/Emax; b = eta*dl/Dref; c = d0*dl/(Zref+dl)
    Es = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return Es, K*(1-q*Es/r), dl

Es, Ns, Zs = equilibrium(P)
Xstar = np.array([Ns, Zs, Es])
log(f'fixed point: N*={Ns:.6f} Z*={Zs:.6f} E*={Es:.6f} F*={P["q"]*Es:.6f}')

def gains_hold(p, Es, Ns, Zs):
    r,K,q,Emax,eta,d0,Zref,Dref,taum,dl,k = (p['r'],p['K'],p['q'],p['Emax'],p['eta'],
        p['d0'],p['Zref'],p['Dref'],p['taum'],p['delta'],p['k'])
    gate = 1-Es/Emax
    dY = q*Es; dS = r-2*r*Ns/K
    dPhi = 1/(1+math.exp(-k*(dY*Ns-(r*Ns*(1-Ns/K)))))
    A_N = r*(1-2*Ns/K)-q*Es; A_E = -q*Ns
    B_N = dPhi*(q*Es-r+2*r*Ns/K)/taum; B_E = dPhi*q*Ns/taum; dZ = -1/taum
    CEm = gate*eta*(dl/Dref-2*Es/Emax)  # bracket vanishes at eq (F_B=0 there)
    CZm = gate*(eta*Es/Dref+d0*Zref/(Zref+dl)**2)
    A = np.array([[A_N,0,A_E],[B_N,dZ,B_E],[0,0,0]])
    return CEm, CZm, A

CEm, CZm, A_hold = gains_hold(P, Es, Ns, Zs)
log(f'mobilising gains: CE={CEm:.6f} CZ={CZm:.6f}')

def FB(E, Z):
    gate = 1-E/P['Emax']
    return gate*(P['eta']*E*(Z/P['Dref']-E/P['Emax'])+P['d0']*Z/(P['Zref']+Z))

def flow_NZ(t, Y, E):
    N, Z = Y
    S = P['r']*N*(1-N/P['K']); Yh = P['q']*E*N
    Phi = max(0.0, math.log1p(math.exp(P['k']*(Yh-S)))/P['k']-math.log(2)/P['k']+P['delta'])
    return [P['r']*N*(1-N/P['K'])-P['q']*E*N, (Phi-Z)/P['taum']]

def smap(X, Tr, exact):
    sol = solve_ivp(flow_NZ, (0, Tr), X[:2], args=(X[2],), method='RK45',
                    rtol=1e-11, atol=1e-13)
    Nf, Zf = sol.y[:, -1]
    if exact:
        x = CEm*Tr
        c = (math.exp(x)-1.0)/CEm if abs(CEm) > 1e-12 else Tr
        Ep = Es + math.exp(x)*(X[2]-Es) + c*CZm*(Zf-Zs)
    else:
        Ep = X[2] + Tr*FB(X[2], Zf)
    lo, hi = 0.0, P['Emax']
    return np.array([Nf, Zf, min(hi, max(lo, Ep))])

def monodromy(Tr, exact):
    if exact:
        x = CEm*Tr
        c = (math.exp(x)-1.0)/CEm if abs(CEm) > 1e-12 else Tr
        R = np.eye(3); R[2,2] = math.exp(x); R[2,1] = c*CZm
    else:
        R = np.eye(3); R[2,2] = 1+CEm*Tr; R[2,1] = Tr*CZm
    return R @ expm(A_hold*Tr)

def fd_jac(fun, X, h):
    n = len(X); J = np.zeros((n, n))
    hh = h*np.maximum(1.0, np.abs(X))
    for j in range(n):
        d = np.zeros(n); d[j] = hh[j]
        J[:, j] = (fun(X+d)-fun(X-d))/(2*hh[j])
    return J

print('=== 1. GATES: FD Jacobian vs monodromy; fixed-point residual ===', flush=True)
log('=== 1. GATES: FD Jacobian vs monodromy; fixed-point residual ===')
gates = []
for Tr in (1.0, 6.5013):
    for exact in (False, True):
        M = monodromy(Tr, exact)
        errs = {}
        for h in (1e-6, 1e-7, 1e-8):
            J = fd_jac(lambda X: smap(X, Tr, exact), Xstar, h)
            errs[h] = float(np.max(np.abs(J-M)))
        err = errs[1e-7]
        tol = 1e-6 if Tr == 1.0 else 1e-4  # longer horizon accumulates solver/FD noise
        ok = err < tol
        gates.append(ok)
        log(f"  {'OK ' if ok else 'FAIL'} Tr={Tr} {'exact' if exact else 'Euler'}: max|J_fd-M|={err:.2e} "
            f"(step study {[(k, f'{v:.1e}') for k, v in errs.items()]}, max|M|={float(np.max(np.abs(M))):.3f})")
        res = float(np.max(np.abs(smap(Xstar, Tr, exact)-Xstar)))
        ok2 = res < 1e-8
        gates.append(ok2)
        log(f"  {'OK ' if ok2 else 'FAIL'} Tr={Tr} {'exact' if exact else 'Euler'}: |P(X*)-X*|={res:.2e}")
if not all(gates):
    log('GATE FAILED - aborting'); sys.exit(1)
log('GATES PASSED - nonlinear map matches monodromy; X* is a fixed point.')

# refine Trc on the nonlinear map's FD spectral radius (consistency with 6.501)
def rho_fd(Tr):
    J = fd_jac(lambda X: smap(X, Tr, True), Xstar, 1e-7)
    return float(np.max(np.abs(np.linalg.eigvals(J))))
a, b = 6.0, 7.0
fa = rho_fd(a)-1.0
for _ in range(40):
    m = 0.5*(a+b); fm = rho_fd(m)-1.0
    if fa*fm <= 0: b = m
    else: a = m; fa = fm
Trc_nl = 0.5*(a+b)
log(f'nonlinear-map FD crossing: Trc_nl={Trc_nl:.6f} (monodromy record 6.5013)')

print('=== 2/3. FD DERIVATIVES + KUZNETSOV a(0) AT Trc ===', flush=True)
log('=== 2/3. FD DERIVATIVES + KUZNETSOV a(0) AT Trc ===')
Trc = 6.5013
M = monodromy(Trc, True)
ev, V = np.linalg.eig(M)
k = int(np.argmax(np.abs(ev)))
mu = ev[k]
th0 = float(np.angle(mu))
log(f'mu={mu:.8f} |mu|={abs(mu):.8f} theta0={th0:.8f} rad = {th0/math.pi:.8f} pi')
for kk in (1, 2, 3, 4):
    log(f'  resonance k={kk}: |e^(ik th)-1| = {abs(np.exp(1j*kk*th0)-1):.6f}')
dT = 1e-3
Mp = monodromy(Trc+dT, True); Mm = monodromy(Trc-dT, True)
dr = (float(np.max(np.abs(np.linalg.eigvals(Mp))))-float(np.max(np.abs(np.linalg.eigvals(Mm)))))/(2*dT)
log(f'transversality d|mu|/dTr = {dr:.6f} (nonzero => crosses transversally)')
log(f'side check: rho(6.4)={float(np.max(np.abs(np.linalg.eigvals(monodromy(6.4,True))))):.6f}, '
    f'rho(6.6)={float(np.max(np.abs(np.linalg.eigvals(monodromy(6.6,True))))):.6f}')

def derivs(h):
    """Central-FD B (2nd) and C (3rd) tensors of the exact-update map at X*."""
    n = 3
    hh = h*np.maximum(1.0, np.abs(Xstar))
    f = lambda X: smap(X, Trc, True)
    B = np.zeros((n, n, n)); C = np.zeros((n, n, n, n))
    from itertools import product
    for i in range(n):
        for j, kk_ in product(range(n), repeat=2):
            dj = np.zeros(n); dj[j] = hh[j]; dk = np.zeros(n); dk[kk_] = hh[kk_]
            B[i,j,kk_] = (f(Xstar+dj+dk)[i]-f(Xstar+dj-dk)[i]-f(Xstar-dj+dk)[i]+f(Xstar-dj-dk)[i])/(4*hh[j]*hh[kk_])
        for j, kk_, l in product(range(n), repeat=3):
            dj = np.zeros(n); dj[j] = hh[j]; dk = np.zeros(n); dk[kk_] = hh[kk_]; dl = np.zeros(n); dl[l] = hh[l]
            s = 0.0
            for sj, sk, sl in product((1,-1), repeat=3):
                s += sj*sk*sl*f(Xstar+sj*dj+sk*dk+sl*dl)[i]
            C[i,j,kk_,l] = s/(8*hh[j]*hh[kk_]*hh[l])
    return B, C

def Bm(B, x, y):
    return np.einsum('ijk,j,k->i', B, x, y)
def Cm(C, x, y, z):
    return np.einsum('ijkl,j,k,l->i', C, x, y, z)

def ns_coeff(B, C):
    q = V[:, k]
    evT, VT = np.linalg.eig(M.T)
    kp = int(np.argmin(np.abs(evT-np.conj(mu))))
    p = VT[:, kp]
    p = p/np.conj(np.vdot(p, q))  # <p,q>=1 (vdot conjugates its first arg)
    assert abs(np.vdot(p, q)-1) < 1e-8
    Bqq = Bm(B, q, q); Bqqb = Bm(B, q, np.conj(q))
    Cqqqb = Cm(C, q, q, np.conj(q))
    I = np.eye(3)
    t1 = np.vdot(p, Cqqqb)
    t2 = 2*np.vdot(p, Bm(B, q, np.linalg.solve(I-M, Bqqb)))
    t3 = np.vdot(p, Bm(B, np.conj(q), np.linalg.solve(np.exp(2j*th0)*I-M, Bqq)))
    a0 = float(np.real(np.exp(-1j*th0)*(t1+t2+t3)/2))
    return a0, float(abs(t1)), float(abs(t2)), float(abs(t3))

for h in (2e-3, 1e-3, 5e-4, 3e-4):
    B, C = derivs(h)
    a0, t1, t2, t3 = ns_coeff(B, C)
    log(f'h={h:g}: a(0)={a0:.6f} (|t1|={t1:.4g} |t2|={t2:.4g} |t3|={t3:.4g}) '
        f'=> {"SUPERCRITICAL (stable circle)" if a0 < 0 else "SUBCRITICAL (unstable circle)"} '
        f'(crossing unstable->stable)')
    if h == 3e-4:
        Bstar, Cstar = B, C
a0s, _, _, _ = ns_coeff(Bstar, Cstar)

print('=== 4. CIRCLE HUNT ===', flush=True)
log('=== 4. CIRCLE HUNT ===')
def hunt(Tr, n_it=4000, n_rec=1200):
    X = Xstar + np.array([0.5, 0.01, 0.05])
    for _ in range(n_it-n_rec):
        X = smap(X, Tr, True)
        if not np.all(np.isfinite(X)): return ('blowup',)+ (None,)*4
    rec = np.zeros((n_rec, 3))
    for i in range(n_rec):
        X = smap(X, Tr, True)
        if not np.all(np.isfinite(X)): return ('blowup',)+(None,)*4
        rec[i] = X
    amp = float(np.max(rec[:, 0])-np.min(rec[:, 0]))
    # rotation number: angle of (N,Z)-centered projection increments
    Y = rec[:, :2]-np.mean(rec[:, :2], axis=0)
    ang = np.unwrap(np.arctan2(Y[:, 1]/(np.std(rec[:, 1])+1e-300), Y[:, 0]/(np.std(rec[:, 0])+1e-300)))
    rot = float(np.mean(np.diff(ang))/(2*math.pi))
    # quasiperiodicity: FFT of N - dominant peak sharpness
    sp = np.abs(np.fft.rfft(rec[:, 0]-np.mean(rec[:, 0])))**2
    dom = float(np.argmax(sp[1:])+1)/n_rec
    return ('bounded', amp, rot, dom, rec)

results = {}
for frac in (-0.03, -0.01, 0.01, 0.03):
    Tr = Trc*(1+frac)
    st, amp, rot, dom, rec = hunt(Tr)
    results[frac] = (st, amp, rot, dom)
    log(f'Tr={Tr:.4f} (frac {frac:+.2f}): {st} amp_N={amp} rot={rot} domfreq={dom}')
    if rec is not None and frac == -0.01:
        rec_save = rec; Tr_save = Tr
bounded = [(f, v) for f, v in results.items() if v[0] == 'bounded']
small = [(f, v) for f, v in bounded if v[1] is not None and v[1] < 5.0]
if len(small) >= 1:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
    ax[0].plot(rec_save[:, 0], rec_save[:, 2], '.', ms=1.5)
    ax[0].set_xlabel('N'); ax[0].set_ylabel('E')
    ax[0].set_title(f'map iterates (N,E), Tr={Tr_save:.4f}')
    ax[1].plot(rec_save[:, 0])
    ax[1].set_xlabel('iterate'); ax[1].set_ylabel('N')
    ax[1].set_title('N trajectory (last 1200 iterates)')
    fig.tight_layout(); fig.savefig('/home/user/_openitems/fig_nscircle_v39.png', dpi=150)
    log('circle-candidate figure written: fig_nscircle_v39.png')
else:
    log('no small-amplitude bounded circle candidate found on the tested sides')
log(f'FINAL: a(0)={a0s:.6f}')
log('DONE')
LOG.close()
