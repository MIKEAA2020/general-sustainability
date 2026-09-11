"""Close item 3: characterize the high-delay four-state crossings (kappa_A=0.05).
For tau in [130, 500]: rightmost characteristic root and unstable-root count;
classify each crossing (real eigenvalue vs Hopf pair by Im omega at crossing);
simulate from a 2% perturbation in each window to confirm stability and
oscillatory-vs-monotone nature.
"""
import numpy as np
from fourstate_pipeline import (FOUR_PARAMS, equilibrium, jacobian_tau0,
                                char_eq_components, sim_four, Estar)
from verify_kappaA_sweep import (rightmost_root, unstable_root_count,
                                 hopf_thresholds, PQ)

p = FOUR_PARAMS()
p['kappa_A'] = 0.05
Jc, B, st = char_eq_components(p, donor=1)
N, Z, E1, A = equilibrium(p, donor=1) if isinstance(equilibrium(p, donor=1), tuple) else (None,)*4

# get physical-branch equilibrium via the pipeline
from fourstate_pipeline import physical_branch as pb  # may not exist; fall back
try:
    from verification_scripts.verify_kappaA_sweep import physical_branch
    b3 = physical_branch(p, donor=1, kas=np.array([0.05]))[0]
    N3, A3, E1_3 = b3[1], b3[2], b3[3]
except Exception as e:
    print("physical_branch failed:", e)
    # fallback: equilibrium from pipeline
    eq = equilibrium(p, donor=1)
    print("pipeline equilibrium:", eq)
    N3, A3, E1_3 = eq[0], eq[3], eq[2]
Z3 = p['delta']
print(f"equilibrium: N={N3:.6f} Z={Z3:.6f} E={E1_3:.6f} A={A3:.6f}")

Jc, B, _ = char_eq_components(p, donor=1, state=(N3, Z3, E1_3, A3))

print("\n== high-delay crossings (all imaginary-axis crossings beyond tau_+) ==")
thr = hopf_thresholds(Jc, B, w_lo=0.0005, w_hi=1.5, nw=6000, nmax=10)
for tau, w in thr:
    print(f"  tau={tau:10.4f}  omega={w:.6f}  (period {2*np.pi/w:8.2f} yr)")
print("  (manuscript: tau_-=6.982022, tau_+=132.272044, then 270.2/274.5/416.6 observed)")

print("\n== unstable-root count & rightmost root vs tau ==")
taus = [130.0, 132.27, 134.0, 200.0, 260.0, 270.0, 270.5, 273.0, 274.5, 275.5,
        300.0, 400.0, 416.0, 416.6, 417.5, 450.0, 500.0]
print(f"{'tau':>8s} {'#unstable':>9s} {'rightmost Re':>12s} {'Im':>8s}")
for tau in taus:
    nu = unstable_root_count(Jc, B, tau, Omega=12.0, n=9000)
    r = rightmost_root(Jc, B, tau)
    print(f"{tau:8.1f} {nu:9d} {r.real:12.5f} {r.imag:8.4f}")

print("\n== simulate 2% perturbation in each window (20000 yr, tail amp) ==")
for tau in [134.0, 200.0, 270.5, 273.0, 275.5, 300.0, 416.6, 417.5, 450.0]:
    y0 = np.array([N3*1.02, Z3*1.02, E1_3*1.02, A3*1.02])
    try:
        Nf, Zf, Ef, Af, amp = sim_four(*y0, tau, T=20000.0, dt=0.5)
        per = None
        tail = Nf[int(0.5*len(Nf)):]
        mn = tail.mean()
        cr = [j for j in range(1, len(tail)) if tail[j-1] < mn <= tail[j]]
        if len(cr) >= 3:
            per = np.median(np.diff(cr))*0.5
        print(f"  tau={tau:7.1f}: amp(N)={amp:9.3f}  period={per if per is None else round(per,1)}"
              f"  N_end={Nf[-1]:.3f}")
    except Exception as ex:
        print(f"  tau={tau:7.1f}: sim err {str(ex)[:50]}")
