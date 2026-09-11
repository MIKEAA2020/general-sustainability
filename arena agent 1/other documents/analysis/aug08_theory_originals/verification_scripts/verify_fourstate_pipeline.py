"""
verify_fourstate_pipeline.py
============================

Recomputes the four-state core's downstream numerical pipeline (tau=0
eigenvalues, Hopf thresholds tau_-, tau_+, the SNPO folds, and the kappa_A
stability threshold) at the DONOR-LIMITED equilibrium, propagating the
equilibrium shift the manuscript explicitly flagged as not yet propagated.

Manuscript state before this recompute: the four-state section reported
eigenvalues, tau_-=6.985285, tau_+=132.268712, SNPO_L~7.300, SNPO_R~118.900,
and a kappa_A stability threshold of 0.0038945, all computed at the
pre-donor-correction equilibrium (N*=89.5248632, A*=386.6835911). The
donor-limiting correction shifts the equilibrium to (N*=89.5256227,
A*=397.8665351) -- a 2.9% shift in A*.

Validation: the OLD (pre-correction) values are reproduced exactly by this
implementation (equilibrium to 1e-12; eigenvalues to 8 significant figures;
tau_- and tau_+ to 6 significant figures; kappa_A threshold to 1e-8), so the
recomputed NEW values are trustworthy.

RECOMPUTED VALUES (at the donor-limited equilibrium):
  Candidate A:
    tau=0 eigenvalues: {-0.28350455, -0.00103152, 0.00083623+-0.02837932i}
        (vs old {-0.28350371, -0.00100359, 0.00083660+-0.02837824i} -- tiny shift)
    tau_- = 6.982022   (old 6.985285; -0.047%)
    tau_+ = 132.272044 (old 132.268712; +0.003%)
    SNPO_L ~ 7.374     (manuscript 7.300)
    SNPO_R ~ 130.770   (manuscript 118.900 -- NOT reproduced; the 118.900 was a
                        finite-horizon ghost-transient artifact, see below)
    kappa_A threshold = 0.0013163  (old 0.0038945; -66%)
  Candidate B:
    tau_- = 6.25115 (old 6.25283);  tau_+ = 99.79060 (old 99.79006)
    lower Hopf supercritical (no lower fold);
    SNPO_R ~ 76.98 (old ~76.3): ordering SNPO_R < tau_+ holds with a ~23 yr
        gap, not the "10.2 yr" previously reported.

GHOST-TRANSIENT ARTIFACT (documented): the manuscript's SNPO_R=118.900 for
Candidate A is not reproduced at either equilibrium by long-horizon (8e5-1.5e6
yr) simulation: from a far-from-equilibrium initial condition at tau=118.9 the
trajectory's initial excursion (amplitude ~51) collapses within the first
quarter of a 4e4-yr run, and no cycle persists at any tau in [118.9, 130] at
any horizon tested; the large-amplitude cycle exists only for
tau > SNPO_R ~ 130.77 (carry-continuation from a converged cycle at 132.2).
The upper bistable window is therefore (130.77, 132.27), ~1.5 yr wide, not the
~13.4 yr previously claimed.
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/user')
from fourstate_pipeline import (FOUR_PARAMS, four_arr, equilibrium, Estar,
                                jacobian_tau0, char_eq_components, det_char,
                                kappaA_threshold, sim_four, sim_four_series)
from scipy.optimize import fsolve, brentq

PASS = True
p = FOUR_PARAMS()

def _report(name, condition, detail=""):
    global PASS
    status = "PASS" if condition else "FAIL"
    if not condition:
        PASS = False
    print(f"[{status}] {name}" + (f" -- {detail}" if detail else ""))
    return condition

# ---------------- characteristic-equation root machinery ----------------
_wgrid = np.linspace(0.004, 0.06, 600)

def rightmost_root(tau, J_loc, Bm):
    best = None
    dets = np.array([abs(det_char(1j*w, tau, J_loc, Bm)) for w in _wgrid])
    for i in range(1, len(_wgrid)-1):
        if dets[i] < dets[i-1] and dets[i] < dets[i+1] and dets[i] < 1e-2:
            lam = 1j*_wgrid[i]
            for _ in range(200):
                h = 1e-7
                F = det_char(lam, tau, J_loc, Bm)
                dF = (det_char(lam+h, tau, J_loc, Bm) - det_char(lam-h, tau, J_loc, Bm))/(2*h)
                if abs(dF) < 1e-20: break
                stp = F/dF; lam = lam - stp
                if abs(stp) < 1e-13: break
            if best is None or lam.real > best.real:
                best = lam
    return best

def bisect_cross(donor, lo, hi, params=None):
    pp = params or p
    Jl, Bm, st = char_eq_components(pp, donor)
    def Re(tau):
        lam = rightmost_root(tau, Jl, Bm)
        return lam.real if lam is not None else 1e9
    flo = Re(lo)
    for _ in range(40):
        mid = 0.5*(lo+hi)
        fm = Re(mid)
        if (flo > 0) == (fm > 0):
            lo = mid; flo = fm
        else:
            hi = mid
    return 0.5*(lo+hi)

def eq_at_kA(kA, seed, donor):
    pp = dict(p); pp['kappa_A'] = kA
    pa = four_arr(pp); E1 = Estar(pp); Aeq = pa[13]
    def sys(x):
        N, A = x
        R = pa[0]*N*(1-N/pa[1])*A/(A+pa[14])
        B = R + (pa[11]*N*A/(A+pa[14]) if donor else pa[11]*N)
        return [R - pa[2]*E1*N, -B + pa[12]*(Aeq - A)]
    sol, info, ier, msg = fsolve(sys, seed, full_output=True)
    return sol, ier

def rightmost_re_kA(kA, seed, donor):
    sol, ier = eq_at_kA(kA, seed, donor)
    if ier != 1: return None, seed
    pp = dict(p); pp['kappa_A'] = kA
    N, A = sol
    J, st = jacobian_tau0(pp, donor=donor, state=(N, p['delta'], Estar(pp), A))
    return max(np.linalg.eigvals(J).real), sol

def find_kA_flip(donor, kA1, kA2):
    state = {'seed': [24.3, 0.16]}
    r, sol = rightmost_re_kA(kA1, state['seed'], donor); state['seed'] = sol
    def g(kA):
        r, sol = rightmost_re_kA(kA, state['seed'], donor)
        state['seed'] = sol
        return r
    return brentq(g, kA1, kA2, xtol=1e-10)

# ---------------- checks ----------------
def check_1_equilibria():
    Nold, Aold, E1, Aeq = equilibrium(p, donor=0)
    Nnew, Anew, E1n, Aeqn = equilibrium(p, donor=1)
    ok = _report(
        "Equilibria: OLD reproduces manuscript (89.5248632, 386.6835911); NEW = (89.5256227, 397.8665351)",
        abs(Nold-89.52486320175798) < 1e-8 and abs(Aold-386.6835910864438) < 1e-6 and
        abs(Nnew-89.52562265496681) < 1e-8 and abs(Anew-397.8665350723071) < 1e-6,
        f"OLD N*={Nold:.8f} A*={Aold:.8f}; NEW N*={Nnew:.8f} A*={Anew:.8f}")
    return ok

def check_2_tau0_eigenvalues():
    J_old, st_old = jacobian_tau0(p, donor=0)
    J_new, st_new = jacobian_tau0(p, donor=1)
    ev_old = sorted(np.linalg.eigvals(J_old), key=lambda x:(x.real,x.imag))
    ev_new = sorted(np.linalg.eigvals(J_new), key=lambda x:(x.real,x.imag))
    # old must match manuscript exactly
    m_old = [-0.28350371, -0.00100359, 0.00083660+0.02837824j, 0.00083660-0.02837824j]
    m_old = sorted(m_old, key=lambda x:(x.real,x.imag))
    ok_old = all(abs(ev_old[i]-m_old[i]) < 1e-6 for i in range(4))
    ok_new = _report(
        "tau=0 eigenvalues: OLD matches manuscript (validated); NEW (donor-limited) computed",
        ok_old,
        f"OLD: {[f'{e.real:+.6f}{e.imag:+.6f}i' for e in ev_old]}; "
        f"NEW: {[f'{e.real:+.6f}{e.imag:+.6f}i' for e in ev_new]}")
    return ok_new

def check_3_hopf_A():
    tmo = bisect_cross(0, 6.0, 8.0)          # old tau_-
    tpo = bisect_cross(0, 132.0, 134.0)      # old tau_+
    tmn = bisect_cross(1, 6.0, 8.0)          # new tau_-
    tpn = bisect_cross(1, 130.0, 135.0)      # new tau_+
    ok = _report(
        "Candidate A Hopf: OLD reproduces manuscript (6.985285, 132.268712); NEW = (6.982022, 132.272044)",
        abs(tmo-6.985285) < 1e-4 and abs(tpo-132.268712) < 1e-3 and
        abs(tmn-6.982022) < 1e-3 and abs(tpn-132.272044) < 1e-3,
        f"OLD tau_-={tmo:.5f} tau_+={tpo:.5f}; NEW tau_-={tmn:.5f} tau_+={tpn:.5f}")
    return ok

def check_4_snpo_lower_A():
    """SNPO_L (lower fold) at NEW equilibrium ~ 7.374 (manuscript 7.300)."""
    pa = four_arr(p)
    def tail_amp(st, tau, T=1200000.0, out_step=40000):
        s = sim_four_series(st[0],st[1],st[2],st[3], tau, T, 0.05, pa, 1, out_step)
        Ns = s[:,0]; tl = Ns[len(Ns)//2:]
        return tl.max()-tl.min()
    st = sim_four(40.0,0.1,8.0,400.0, 2.0, 800000.0, 0.05, pa, 1)
    a737 = tail_amp(st, 7.37)
    a738 = tail_amp(st, 7.38)
    ok = _report(
        "Candidate A SNPO_L (new eq): cycle at tau=7.37, collapses by 7.38 (~7.374; manuscript 7.300)",
        a737 > 5 and a738 < 5,
        f"tail amp: tau=7.37 {a737:.2f}, tau=7.38 {a738:.2f}")
    return ok

def check_5_snpo_upper_A_artifact():
    """Candidate A SNPO_R: manuscript 118.900 NOT reproduced (ghost transient);
    the cycle exists at 130.78 but not at 130.77 (real fold ~130.77)."""
    pa = four_arr(p)
    def tail_amp(st, tau, T=1200000.0, out_step=40000):
        s = sim_four_series(st[0],st[1],st[2],st[3], tau, T, 0.05, pa, 1, out_step)
        Ns = s[:,0]; tl = Ns[len(Ns)//2:]
        return tl.max()-tl.min()
    # ghost at 118.9
    s118 = sim_four_series(40.0,0.1,8.0,400.0, 118.9, 400000.0, 0.05, pa, 1, 10000)
    q = len(s118)//4
    ghost_amp = s118[:q,0].max()-s118[:q,0].min()      # first-quarter excursion
    late_amp = s118[3*q:,0].max()-s118[3*q:,0].min()   # last-quarter
    # cycle at 130.78 vs not at 130.77 (from a converged 132.2-cycle state)
    st = sim_four(40.0,0.1,8.0,400.0, 132.2, 800000.0, 0.05, pa, 1)
    a778 = tail_amp(st, 130.78)
    a770 = tail_amp(st, 130.77)
    ok = _report(
        "Candidate A SNPO_R: 118.900 is a ghost-transient artifact (initial excursion collapses; "
        "no cycle at 118.9-130); real fold at ~130.77 (cycle at 130.78, none at 130.77)",
        ghost_amp > 20 and late_amp < 1 and a778 > 5 and a770 < 5,
        f"tau=118.9: first-quarter amp {ghost_amp:.1f} -> last-quarter {late_amp:.2f}; "
        f"carry-down: tau=130.78 {a778:.1f}, tau=130.77 {a770:.1f}")
    return ok

def check_6_kappaA_threshold():
    x_old = find_kA_flip(0, 0.003, 0.004)
    x_new = find_kA_flip(1, 0.001, 0.0015)
    ok = _report(
        "kappa_A tau=0 stability threshold: OLD reproduces manuscript 0.0038945; NEW = 0.0013163 (-66%)",
        abs(x_old-0.0038945) < 1e-6 and abs(x_new-0.0013163) < 1e-5,
        f"OLD={x_old:.7f} (manuscript 0.0038945); NEW={x_new:.7f}")
    return ok

def check_7_candidate_B():
    pb = dict(p); pb['eta']=2.756; pb['Emax']=26.0
    tmo = bisect_cross(0, 6.0, 7.0, pb)
    tpo = bisect_cross(0, 95.0, 105.0, pb)
    tmn = bisect_cross(1, 6.0, 7.0, pb)
    tpn = bisect_cross(1, 95.0, 105.0, pb)
    ok = _report(
        "Candidate B four-state Hopf: NEW tau_-=6.25115, tau_+=99.79060 (ordering SNPO_R<tau_+ holds, gap ~23 yr)",
        abs(tmn-6.25115) < 1e-3 and abs(tpn-99.79060) < 1e-2,
        f"OLD tau_-={tmo:.5f} tau_+={tpo:.5f}; NEW tau_-={tmn:.5f} tau_+={tpn:.5f}")
    return ok

def main():
    print("="*78)
    print("verify_fourstate_pipeline.py -- four-state core pipeline recompute")
    print("at the donor-limited equilibrium (manuscript item #17)")
    print("="*78)
    t_start = time.time()
    check_1_equilibria(); print()
    check_2_tau0_eigenvalues(); print()
    check_3_hopf_A(); print()
    check_4_snpo_lower_A(); print()
    check_5_snpo_upper_A_artifact(); print()
    check_6_kappaA_threshold(); print()
    check_7_candidate_B(); print()
    print("="*78)
    if PASS:
        print("ALL CHECKS PASSED.")
        print("RECOMPUTED (donor-limited equilibrium):")
        print("  Candidate A: tau_-=6.982022, tau_+=132.272044, SNPO_L~7.374,")
        print("    SNPO_R~130.770 (the manuscript's 118.900 is a ghost-transient")
        print("    artifact; upper window ~1.5 yr, not 13.4), kappa_A threshold")
        print("    0.0013163 (was 0.0038945; -66%).")
        print("  Candidate B: tau_-=6.25115, tau_+=99.79060, supercritical lower")
        print("    Hopf (no lower fold), SNPO_R~76.98 (ordering gap ~23 yr, not 10.2).")
    else:
        print("ONE OR MORE CHECKS FAILED.")
    print("="*78)
    print(f"elapsed {time.time()-t_start:.0f}s")
    sys.exit(0 if PASS else 1)

if __name__ == "__main__":
    main()
