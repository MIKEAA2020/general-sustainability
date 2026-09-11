"""Full fold hunt: corrected (gated) four-state core -- SNPO fold locations.

Protocol (manuscript-style continuation):
  * converge a limit cycle deep in the large-amplitude regime (constant far-from-
    equilibrium history);
  * step tau toward the fold, seeding each run from the previous run's final state
    and Z-history (near-exact continuation);
  * each decisive step runs 1.5-5e6 yr; a tail amplitude change > threshold means
    the large cycle persists, a tail collapse to N* means the fold is crossed;
  * bisect, then re-verify the boundary from independent far-from-equilibrium
    histories (the manuscript's cross-check standard).

Only Z is delayed, so only the Z-history ring is needed. Fully numba-jitted.

Usage:
  python fourstate_gated_fold_hunt.py converge <tau> <T> <out.npz> [hist0 N0 E0 A0]
  python fourstate_gated_fold_hunt.py step <tau> <T> <in.npz> <out.npz>
  python fourstate_gated_fold_hunt.py run  <tau> <T> <out.npz> [N0 E0 A0]   # constant history
  python fourstate_gated_fold_hunt.py check <npz> [Nstar]

Every run appends a JSON line to fourstate_gated_fold_hunt_log.jsonl.
Verdict thresholds (tail of coarse record, last 20%): N range > 20 -> PERSIST;
max|N-N*| < 2 -> COLLAPSE; else AMBIGUOUS (needs longer horizon).
"""
import numpy as np
import json, sys, os, time
from numba import njit

# ---------------- parameters (Candidate A, donor-limited) ----------------
r, K, q = 0.02, 100.0, 0.001
eta, Emax, Dref = 0.914, 30.0, 1.0
delta0, Zref, taum = 0.01, 1.0, 5.0
k, delta = 10.0, np.log(2.0)/10.0
kA, omA, A_intr, A0 = 0.05, 1e-3, 50.0, 1.0
Aeq = A_intr + kA*K/omA
NSTAR = 89.52562265496681
LOG = "fourstate_gated_fold_hunt_log.jsonl"

@njit(fastmath=True)
def softplus(u):
    if k*u > 30.0:
        return u
    if k*u < -30.0:
        return 0.0
    return np.log1p(np.exp(k*u))/k

@njit(fastmath=True)
def rhs_gated(N, Z, E, A, Ztau):
    R = r*N*(1.0 - N/K)*A/(A + A0)
    B = R + kA*N*A/(A + A0)
    Ndot = R - q*E*N
    Adot = -B + omA*(Aeq - A)
    u = q*E*N - R
    sp = softplus(u)
    inner = sp - np.log(2.0)/k + delta
    if inner < 0.0:
        inner = 0.0
    Zdot = (inner - Z)/taum
    bracket = eta*E*(Ztau/Dref - E/Emax) + delta0*Ztau/(Zref + Ztau)
    Edot = (1.0 - E/Emax)*bracket
    return Ndot, Zdot, Edot, Adot

@njit(fastmath=True)
def integrate(tau, T, dt, zhist, N0, Z0, E0, A0, record_every, tail_years):
    """tau continuous: delayed Z(t-tau) via linear interpolation of the ring.
    zhist[j] = Z at step j-(n_tau+1), j=0..n_tau+1  (i.e. times -(n_tau+1)*dt .. 0);
    zhist[n_tau+1] must equal the current Z0."""
    tau_d = tau/dt
    n_tau = int(tau_d)
    frac = tau_d - n_tau
    L = n_tau + 2
    # ring init: slot (j mod L) = Z_j for j in [-(n_tau+1), 0]:
    #   slot 0 <- Z_0 (= zhist[n_tau+1]); slot k (1..L-1) <- zhist[k-1]
    ring = np.empty(L)
    ring[0] = Z0
    for k in range(1, L):
        ring[k] = zhist[k - 1]
    N, Z, E, A = N0, Z0, E0, A0
    n_tail = int(tail_years/dt)
    tail = np.empty((n_tail, 4))
    tail_idx = 0
    n_rec = int(T/dt)//record_every + 2
    ts = np.empty(n_rec); Ns = np.empty(n_rec); Es = np.empty(n_rec); As = np.empty(n_rec)
    ri = 0
    ts[0] = 0.0; Ns[0] = N; Es[0] = E; As[0] = A
    nsteps = int(T/dt)
    for s in range(1, nsteps+1):
        s1 = (s - n_tau - 1) % L
        s2 = (s - n_tau) % L
        tap = frac*ring[s1] + (1.0 - frac)*ring[s2]
        n1, z1, e1, a1 = rhs_gated(N, Z, E, A, tap)
        n2, z2, e2, a2 = rhs_gated(N+0.5*dt*n1, Z+0.5*dt*z1, E+0.5*dt*e1, A+0.5*dt*a1, tap)
        n3, z3, e3, a3 = rhs_gated(N+0.5*dt*n2, Z+0.5*dt*z2, E+0.5*dt*e2, A+0.5*dt*a2, tap)
        n4, z4, e4, a4 = rhs_gated(N+dt*n3, Z+dt*z3, E+dt*e3, A+dt*a3, tap)
        N += dt/6.0*(n1 + 2.0*n2 + 2.0*n3 + n4)
        Z += dt/6.0*(z1 + 2.0*z2 + 2.0*z3 + z4)
        E += dt/6.0*(e1 + 2.0*e2 + 2.0*e3 + e4)
        A += dt/6.0*(a1 + 2.0*a2 + 2.0*a3 + a4)
        if N < 0.0: N = 0.0
        if E < 0.0: E = 0.0
        if A < 0.0: A = 0.0
        ring[s % L] = Z
        tail[tail_idx % n_tail, 0] = N
        tail[tail_idx % n_tail, 1] = Z
        tail[tail_idx % n_tail, 2] = E
        tail[tail_idx % n_tail, 3] = A
        tail_idx += 1
        if s % record_every == 0:
            ri += 1
            ts[ri] = s*dt; Ns[ri] = N; Es[ri] = E; As[ri] = A
    # reorder tail ring into chronological order
    chron = np.empty_like(tail)
    if tail_idx >= n_tail:
        rot = tail_idx % n_tail
        if rot == 0:
            chron = tail.copy()
        else:
            chron[:-rot] = tail[rot:]
            chron[-rot:] = tail[:rot]
    else:
        chron[:tail_idx] = tail[:tail_idx]
        chron = chron[:tail_idx]
    return (ts[:ri+1], Ns[:ri+1], Es[:ri+1], As[:ri+1], chron, N, Z, E, A)

def period_from(Ns, ts, frac=0.5):
    """Peak-count period over the final frac of the series."""
    n0 = int(len(Ns)*(1.0-frac))
    N = Ns[n0:]; t = ts[n0:]
    if len(N) < 4:
        return float('nan')
    d = np.diff(N)
    peaks = np.where((d[:-1] > 0) & (d[1:] < 0))[0] + 1
    if len(peaks) < 2:
        return float('nan')
    return (t[peaks[-1]] - t[peaks[0]]) / (len(peaks) - 1)

def run_one(tau, T, dt, zhist, N0, Z0, E0, A0, tag, record_every=200, tail_years=200.0):
    t0 = time.time()
    ts, Ns, Es, As, tail, Nf, Zf, Ef, Af = integrate(
        tau, T, dt, zhist, N0, Z0, E0, A0, record_every, tail_years)
    wall = time.time() - t0
    tailN = Ns[-int(len(Ns)*0.2):]
    rng = tailN.max() - tailN.min()
    dev = np.abs(tailN - NSTAR).max()
    if rng > 20.0:
        verdict = "PERSIST"
    elif dev < 2.0:
        verdict = "COLLAPSE"
    else:
        verdict = "AMBIGUOUS"
    per = period_from(Ns, ts)
    rec = dict(tag=tag, tau=tau, T=T, dt=dt, wall_s=round(wall,1),
               tail_N_min=round(float(tailN.min()),4), tail_N_max=round(float(tailN.max()),4),
               tail_range=round(float(rng),4), dev_from_Nstar=round(float(dev),5),
               verdict=verdict, period_yr=round(float(per),3) if per==per else None,
               Nf=round(float(Nf),6), Ef=round(float(Ef),6), Af=round(float(Af),6))
    with open(LOG, "a") as fh:
        fh.write(json.dumps(rec) + "\n")
    print(f"[{tag}] tau={tau:7.2f} T={T:.1e} tail N=[{tailN.min():9.3f},{tailN.max():9.3f}] "
          f"range={rng:7.2f} dev={dev:9.4f} period~{per:8.1f} -> {verdict:9s} ({wall:.0f}s)")
    return rec, tail, (Nf, Zf, Ef, Af), ts, Ns

def main():
    cmd = sys.argv[1]
    dt = 0.05
    tail_years = 200.0
    if cmd == "converge":
        tau, T = float(sys.argv[2]), float(sys.argv[3])
        out = sys.argv[4]
        N0, E0, A0 = (float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7])) if len(sys.argv) > 7 else (95.0, 1.0, 400.0)
        Z0 = delta
        n_tau = int(tau/dt)
        zhist = np.full(n_tau + 2, Z0)
        rec, tail, state, ts, Ns = run_one(tau, T, dt, zhist, N0, Z0, E0, A0, "conv")
        np.savez(out, tau=tau, tail=tail, state=np.array(state), dt=dt, tail_years=tail_years)
        print(f"  saved {out}")
    elif cmd == "run":
        tau, T = float(sys.argv[2]), float(sys.argv[3])
        out = sys.argv[4]
        N0, E0, A0 = (float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7])) if len(sys.argv) > 7 else (95.0, 1.0, 400.0)
        Z0 = delta
        n_tau = int(tau/dt)
        zhist = np.full(n_tau + 2, Z0)
        rec, tail, state, ts, Ns = run_one(tau, T, dt, zhist, N0, Z0, E0, A0, "run")
        np.savez(out, tau=tau, tail=tail, state=np.array(state), dt=dt, tail_years=tail_years)
        print(f"  saved {out}")
    elif cmd == "step":
        tau, T = float(sys.argv[2]), float(sys.argv[3])
        inn, out = sys.argv[4], sys.argv[5]
        npz = np.load(inn)
        tail = npz["tail"]  # chronological
        n_tau = int(tau/dt)
        if len(tail) < n_tau + 2:
            raise SystemExit(f"tail too short: need {n_tau+2}, have {len(tail)}")
        zhist = tail[-n_tau-2:, 1].copy()
        Nf, Zf, Ef, Af = npz["state"]
        rec, tail2, state, ts, Ns = run_one(tau, T, dt, zhist, Nf, Zf, Ef, Af, "step")
        np.savez(out, tau=tau, tail=tail2, state=np.array(state), dt=dt, tail_years=tail_years)
        print(f"  saved {out}")
    elif cmd == "check":
        for p in sys.argv[2:]:
            npz = np.load(p)
            tail = npz["tail"]
            print(f"{p}: tau={npz['tau']:.3f} state={np.round(npz['state'],4)}")
    else:
        print(__doc__)

if __name__ == "__main__":
    main()

# --- quick decay-trend diagnostic on an existing run npz (no new integration) ---
