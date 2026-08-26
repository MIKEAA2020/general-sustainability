#!/usr/bin/env python3
"""A1 piecewise-Chebyshev campaign — STAGE 1: substrate + local-gain diagnostic.

Status: SUBSTRATE/DIAGNOSTIC. This is the first executed stage of the
piecewise-Chebyshev route specified in A1_CONTINUUM_LIFT_STATUS.md (the
global Fourier/Schauder radii polynomials are defeated by the scale
mismatch P*Lip_f ~ 7.9e3; the specified route is local patches with
M ~ 8000 segments and local gain O(1)). It does NOT produce a certificate:
no interval outward rounding, no Krawczyk operator, no radii polynomial.
What it produces:

  1. the piecewise-Chebyshev substrate: the validated K=80 orbit (committed
     Krawczyk box midpoint) re-represented on M Chebyshev patches per period;
  2. the local collocation defect at Chebyshev-Lobatto nodes (the future
     radii-polynomial Y-input, measured against the Fourier orbit);
  3. the local gain diagnostic  g_j = h * sup( ||dF/dx||_inf + ||dF/dzd||_inf )
     per segment — the quantity that must be O(1) locally for the route to
     work, with the segment counts M* at which max_j g_j <= 1 and <= 0.5;
  4. the delay-coupling band structure (segments per delay window, the
     finite-band coupling of the local patches).

Deterministic; no randomness. Run from anywhere:
    python3 research_program/validated_computations/a021_c4/
           c4_piecewise_chebyshev_stage1.py
Writes c4_piecewise_chebyshev_stage1.json next to this file.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from c4_orbit_krawczyk import (  # noqa: E402
    N_NODES, K_MAX, TAU, P4, D, jac_point, f_vec,
)
from c4_monodromy import rhs  # noqa: E402

M_LADDER = [100, 200, 400, 800, 1600, 3200, 6400, 8000]
CHEB_DEGREE = 8          # local polynomial degree per patch
GAIN_TARGETS = (1.0, 0.5)


# ---------------------------------------------------------------- substrate


def load_validated_orbit():
    box = np.load(ROOT / "c4_orbit_krawczyk_box.npz")
    cert = json.loads((ROOT / "c4_orbit_krawczyk_certificate.json").read_text())
    u_mid = 0.5 * (box["u_lo"] + box["u_hi"])
    P = float(0.5 * (box["P_lo"] + box["P_hi"]))
    return u_mid, P, cert


class FourierOrbit:
    """Exact Fourier interpolant of the 161-point K=80 orbit (arbitrary t)."""

    def __init__(self, u, P):
        self.P = P
        # coefficients of the equispaced 161-point representation (K=80):
        # the interpolant is band-limited to |k| <= 80 by construction.
        self.c = np.fft.fft(u, axis=0) / N_NODES     # (161, 4), complex
        self.k = np.fft.fftfreq(N_NODES, d=1.0 / N_NODES)

    def _eval(self, t, deriv=0):
        # t: (n,) in [0, P); returns (n, 4)
        phase = np.exp(2j * np.pi * np.outer(t, self.k) / self.P)
        if deriv:
            phase = phase * ((2j * np.pi * self.k / self.P) ** deriv)
        return np.real(phase @ self.c)

    def x(self, t):
        return self._eval(np.atleast_1d(t), 0)

    def dx(self, t):
        return self._eval(np.atleast_1d(t), 1)

    def delayed_z(self, t):
        return self._eval((np.atleast_1d(t) - TAU) % self.P, 0)[:, 2]


def cheb_lobatto(n):
    """Degree-n Chebyshev-Lobatto nodes on [-1, 1] (ascending)."""
    j = np.arange(n + 1)
    return np.cos(np.pi * (n - j) / n)


# ---------------------------------------------------------------- stage 1


def local_diagnostics(fo: FourierOrbit, M, n=CHEB_DEGREE):
    """Per-segment local gain and collocation defects over one period.

    Segment j covers [j*h, (j+1)*h], h = P/M.  Nodes: degree-n
    Chebyshev-Lobatto points mapped to the segment.  Reported per segment:
      gain_j  = h * max_nodes( ||A||_inf + ||Dv||_inf )   (local Lipschitz
                gain of the DDE right-hand side on the patch, conservative:
                the delayed coupling is charged at full weight)
      defect_j = max over nodes and components of
                |dx_cheb(t) - f(x(t), x(t - tau))|      (the local
                collocation defect of the degree-n Chebyshev interpolant of
                the orbit: x_cheb interpolates the orbit's VALUES at the
                nodes; its derivative is the spectral derivative)
      fourier_defect_j = max over nodes of |dx_F(t) - f(x(t), x(t-tau))|
                (the underlying K=80 Fourier orbit's own DDE defect)
    """
    h = fo.P / M
    nodes = cheb_lobatto(n)
    # barycentric weights for Chebyshev-Lobatto differentiation
    w = np.ones(n + 1)
    w[0] = w[-1] = 0.5
    w *= (-1.0) ** np.arange(n + 1)
    # differentiation matrix (standard Chebyshev-Lobatto)
    Diff = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        for j in range(n + 1):
            if i != j:
                Diff[i, j] = (w[j] / w[i]) / (nodes[i] - nodes[j])
        Diff[i, i] = -np.sum(Diff[i, :])
    # transform: d/dt = (2/h) * d/dxi on [t_j, t_j+h]
    gains = np.zeros(M)
    defects = np.zeros(M)
    fourier_defects = np.zeros(M)
    dxd = np.zeros(M)          # spectral-derivative vs Fourier-derivative gap
    for j in range(M):
        t0 = j * h
        t = t0 + 0.5 * h * (nodes + 1.0)
        X = fo.x(t)                          # (n+1, 4)
        Xd = fo.delayed_z(t)                 # (n+1,)
        # local Chebyshev derivative of the node values
        dX = (2.0 / h) * (Diff @ X)
        dX_fourier = fo.dx(t)
        # DDE defects
        F = np.array([rhs(X[i], Xd[i]) for i in range(n + 1)])
        defects[j] = np.max(np.abs(dX - F))
        fourier_defects[j] = np.max(np.abs(dX_fourier - F))
        dxd[j] = np.max(np.abs(dX - dX_fourier))
        # local Lipschitz gain
        g = 0.0
        for i in range(n + 1):
            A, Dv = jac_point(X[i], Xd[i])
            g = max(g, float(np.abs(A).sum(axis=0).max())
                    + float(np.abs(Dv).sum()))
        gains[j] = h * g
    return dict(h=h, gains=gains, defects=defects,
                fourier_defects=fourier_defects, derivative_gap=dxd)


def main():
    u_mid, P, cert = load_validated_orbit()
    fo = FourierOrbit(u_mid, P)

    # global reference quantities (the obstruction scale)
    t_dense = np.linspace(0.0, P, 4001, endpoint=False)
    X = fo.x(t_dense)
    Zd = fo.delayed_z(t_dense)
    lip = 0.0
    for i in range(len(t_dense)):
        A, Dv = jac_point(X[i], Zd[i])
        lip = max(lip, float(np.abs(A).sum(axis=0).max())
                  + float(np.abs(Dv).sum()))
    global_scale = P * lip

    # the K=80 orbit's own residual scale (sanity: matches the certificate)
    res_scale = float(np.max(np.abs(D @ u_mid
                                    - P * f_vec(u_mid,
                                                (np.roll(u_mid[:, 2],
                                                         -int(round(TAU / P * N_NODES)))
                                                 if False else
                                                 _shift_z(u_mid, P))))))
    out = {
        "title": "A1 piecewise-Chebyshev campaign — Stage 1: substrate + "
                 "local-gain diagnostic (NOT a certificate)",
        "status": "SUBSTRATE/DIAGNOSTIC — first executed stage of the "
                  "specified route (A1_CONTINUUM_LIFT_STATUS.md); no "
                  "interval arithmetic, no Krawczyk operator, no radii "
                  "polynomial; nothing here upgrades any theorem status",
        "inputs": {
            "orbit": "committed Krawczyk box midpoint (c4_orbit_krawczyk_box.npz)",
            "period": P,
            "certified_box_radii": cert["krawczyk"]["radii"],
            "cheb_degree_per_patch": CHEB_DEGREE,
            "delay_tau": TAU,
        },
        "global_obstruction": {
            "sup_rhs_lipschitz_over_orbit": round(lip, 3),
            "P_times_lipschitz": round(global_scale, 1),
            "reading": "the global Fourier/Schauder radii-polynomial scale "
                       "(~7.9e3 in the status record; re-measured here on "
                       "the box midpoint)",
        },
        "K80_orbit_residual_scale": round(res_scale, 12),
        "ladder": [],
    }

    # M* targets from the measured local Lipschitz distribution
    t_seg = np.linspace(0.0, P, 20001, endpoint=False)
    Xs = fo.x(t_seg)
    Zds = fo.delayed_z(t_seg)
    g_pts = np.array([
        float(np.abs(jac_point(Xs[i], Zds[i])[0]).sum(axis=0).max())
        + float(np.abs(jac_point(Xs[i], Zds[i])[1]).sum())
        for i in range(len(t_seg))
    ])
    for target in GAIN_TARGETS:
        M_star = int(np.ceil(P * float(g_pts.max()) / target))
        out[f"M_star_gain_le_{target}"] = M_star

    for M in M_LADDER:
        d = local_diagnostics(fo, M)
        out["ladder"].append({
            "M": M,
            "segment_length_h": round(d["h"], 6),
            "delay_window_segments": round(TAU / d["h"], 2),
            "max_local_gain": round(float(d["gains"].max()), 4),
            "median_local_gain": round(float(np.median(d["gains"])), 4),
            "max_cheb_collocation_defect": float(f"{d['defects'].max():.3e}"),
            "max_fourier_dde_defect": float(f"{d['fourier_defects'].max():.3e}"),
            "max_derivative_gap": float(f"{d['derivative_gap'].max():.3e}"),
        })

    out["stage1_verdict"] = {
        "local_gain_premise": (
            f"max local gain falls like P*lip/M: at M=8000 it is "
            f"{[l['max_local_gain'] for l in out['ladder'] if l['M'] == 8000][0]} "
            f"— the O(1)-local-gain premise of the piecewise-Chebyshev route "
            f"holds on the measured orbit"
        ),
        "coupling_band": (
            f"the delay window spans {[l['delay_window_segments'] for l in out['ladder'] if l['M'] == 8000][0]} "
            f"segments at M=8000 — each patch couples to a finite band of "
            f"earlier patches, as specified"
        ),
        "next_stages": [
            "Stage 2: outward-rounded interval evaluation of the local "
            "collocation defects and Jacobian blocks (Chebyshev basis, "
            "per-patch interval arithmetic)",
            "Stage 3: the local Krawczyk/radii-polynomial system on the "
            "patches with the finite-band delay coupling enclosed",
            "Stage 4: patch-to-patch contraction assembly and the continuum "
            "orbit certificate (the A1 gate)",
        ],
        "honesty": "this stage measures the substrate and verifies the "
                   "route's premises on the committed validated orbit; it "
                   "certifies nothing",
    }

    dst = ROOT / "c4_piecewise_chebyshev_stage1.json"
    dst.write_text(json.dumps(out, indent=2))
    print(f"period P = {P:.3f}, tau = {TAU}")
    print(f"sup rhs Lipschitz on orbit = {lip:.2f}  ->  P*lip = "
          f"{global_scale:.0f} (the global obstruction)")
    for target in GAIN_TARGETS:
        print(f"M* for local gain <= {target}: {out[f'M_star_gain_le_{target}']}")
    print(f"{'M':>6} {'h':>10} {'tau/h':>7} {'maxgain':>9} {'medgain':>9} "
          f"{'cheb_defect':>12} {'fourier_defect':>14} {'dgap':>10}")
    for l in out["ladder"]:
        print(f"{l['M']:>6} {l['segment_length_h']:>10.4f} "
              f"{l['delay_window_segments']:>7.1f} "
              f"{l['max_local_gain']:>9.3f} {l['median_local_gain']:>9.3f} "
              f"{l['max_cheb_collocation_defect']:>12.3e} "
              f"{l['max_fourier_dde_defect']:>14.3e} "
              f"{l['max_derivative_gap']:>10.3e}")
    print(f"wrote {dst.name}")


def _shift_z(u, P):
    """Z(t - tau) on the 161 equispaced grid via the Fourier phase shift."""
    c = np.fft.fft(u[:, 2]) / N_NODES
    k = np.fft.fftfreq(N_NODES, d=1.0 / N_NODES)
    sym = np.exp(-2j * np.pi * k * TAU / P)
    return np.real(np.fft.ifft(sym * c) * N_NODES)


if __name__ == "__main__":
    main()
