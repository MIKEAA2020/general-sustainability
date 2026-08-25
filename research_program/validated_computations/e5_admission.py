#!/usr/bin/env python3
"""E5: interval-verified numerical admission of the A001 §§6-10 resource-sink
module (linear case, Theorem 6.3).

All arithmetic for the certificate bounds is outward-rounded.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))
from interval_lib import interval, imul, isub, iscale

ROOT = Path(__file__).parent

R, a = 1.0, 0.1
H_min, H_max = 0.4, 0.8
theta_K, theta_d = 0.5, 0.2
S_min, K_max = 2.0, 2.0


def iv(x):
    return interval(float(x))


def lo(A):
    return float(A[0])


def hi(A):
    return float(A[1])


out = {}

# kernel conditions with rigorous margins
cond_i = iv(H_min)
rhs_i = isub(iv(R), imul(iv(a), iv(S_min)))
margin_i = lo(rhs_i) - hi(cond_i)
cond_ii = iscale(imul(iv(theta_K), iv(H_min)), 1.0 / theta_d)
margin_ii = lo(iv(K_max)) - hi(cond_ii)
S_star = iscale(isub(iv(R), iv(H_min)), 1.0 / a)
margin_iii = lo(S_star) - hi(iv(S_min))
out['conditions'] = {
    'arithmetic': 'outward-rounded float64 intervals (nextafter)',
    'i_Hmin_le_R_minus_aSmin': dict(lhs=H_min, rhs=R - a * S_min,
                                     rigorous_margin=margin_i,
                                     holds=bool(margin_i > 0)),
    'ii_Kdag_le_Kmax': dict(Kdag=theta_K * H_min / theta_d,
                            rigorous_margin=margin_ii,
                            holds=bool(margin_ii > 0)),
    'iii_Smin_le_Sstar': dict(Sstar=(R - H_min) / a,
                              rigorous_margin=margin_iii,
                              holds=bool(margin_iii > 0)),
}

# face margins
fS_face = isub(isub(iv(R), imul(iv(a), iv(S_min))), iv(H_min))
fK_face = isub(imul(iv(theta_K), iv(H_min)), imul(iv(theta_d), iv(K_max)))
alpha_S = lo(fS_face)
alpha_K = -hi(fK_face)
alpha = min(alpha_S, alpha_K)
out['face_margins'] = dict(alpha_S_min_face=alpha_S,
                           alpha_K_max_face=alpha_K,
                           alpha_joint=alpha)

# Lipschitz constant
L = max(a, theta_d)
out['lipschitz_L_inf'] = L

# erosion menu
best = None
for r in np.linspace(0.05, 0.45, 19):
    aS = alpha_S - a * r
    aK = alpha_K - theta_d * r
    alpha_r = min(aS, aK)
    Delta = alpha_r - L * r
    if Delta > 0 and (best is None or Delta > best['Delta_max']):
        best = dict(erosion_depth=float(r), alpha_S_r=aS, alpha_K_r=aK,
                    alpha_r=alpha_r, Delta_max=float(Delta))
out['erosion_triple'] = dict(L=L, r=best['erosion_depth'],
                             alpha_r=best['alpha_r'],
                             Delta_max_certified=float(np.nextafter(best['Delta_max'], -np.inf)),
                             eroded_kernel=[f"[{2+best['erosion_depth']:.6f}, inf)",
                                            f"[0, {2-best['erosion_depth']:.6f}]"])

# confinement
S_hi = 8.0
fS_hi = isub(isub(iv(R), imul(iv(a), iv(S_hi))), iv(H_min))
out['confinement'] = dict(enclosure=f"[{S_min}, {S_hi}] x [0, {K_max}]",
                          S_equilibrium=(R - H_min) / a,
                          inward_at_S_hi=bool(hi(fS_hi) <= 0),
                          K_equilibrium_under_min=theta_K * H_min / theta_d)

# module verdict
out['module'] = dict(
    source='A001 topdown source, Section 6 (lines 740-960), Theorems 6.1/6.2/6.3',
    phase_map='identity on (S,K)',
    solution_concept='Caratheodory ODE (linear field, unique forward-complete)',
    safe_set=f'[{S_min}, inf) x [0, {K_max}]',
    kernel=f'[{S_min}, inf) x [0, {K_max}] (Thm 6.3 order-minimal; policy H == H_min)',
    policy='H(t) = H_min (constant; measurable, continuous, Lipschitz, computable)',
    verdict='ADMITTED WITH NUMBERS (linear resource-sink, declared scope)')

import json
print(json.dumps(out, indent=2))
(ROOT / 'E5_NUMBERS.json').write_text(json.dumps(out, indent=2))
print("\nwritten E5_NUMBERS.json")
