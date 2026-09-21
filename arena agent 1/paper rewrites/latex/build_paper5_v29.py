#!/usr/bin/env python3
"""Build paper5 v29 from v28: root-cause resolution of author-blocked items.

Every substitution asserts exactly one match. Still author-blocked (NOT touched):
A3 disclosure policy (full vector values), A5 (archive role; F12), A6 (all
registration materials), A8/A9 (recommend keep/leave), A10 (structure),
A11-AR(1) (checks or F31 clause stands), I5 (code heading needs deposit bits).
Applied: A1/F2 (protective law), A2/F4 (four-state period), A3-facts (F9
positivity scoping, F38 delta alignment + Table 3 consistency), A4 (information
pattern), A7 (effort channel), F27b (Re lambda), I3 (band entry), A11-a(E)
(guard threshold).
"""
import sys

SRC = "/home/user/paper5_v27/paper5_sampled_governance_v27.tex"
SRC = "/home/user/paper5_v28/paper5_sampled_governance_v28.tex"
DST = "/home/user/paper5_v29/paper5_sampled_governance_v29.tex"

r = lambda s: s  # marker: strings below are raw triple-quoted

SUBS = [
("VER-header",
r'''% Periodic Review as Sampled Governance (paper 5, revision v28): audit-response revision with line numbers for review.''',
r'''% Periodic Review as Sampled Governance (paper 5, revision v29): root-cause resolution revision with line numbers for review.'''),

("F27b-Box-sign",
r'''Relation between the three undelayed-limit statements & Reconciled conditional on the companion's undelayed sign (\(\lambda > 0\));''',
r'''Relation between the three undelayed-limit statements & Reconciled conditional on the companion's undelayed sign (\(\mathrm{Re}\,\lambda > 0\));'''),

("F38-notation-delta",
r'''shift \(\delta\) and sharpness \(k\) (the shift is a constant
regularisation offset, distinct from and unrelated to the effort-law
gain \(\delta_0\), as the display below states)''',
r'''shift \(\delta = \log 2/10 \approx 0.069\) and sharpness \(k\) (the shift is the equilibrium memory level, distinct from and unrelated to the effort-law
gain \(\delta_0\), as the display below states)'''),

("F9-positivity",
r'''robustness experiment of Section 3.3 satisfies this by construction. The effort law's rational term is undefined at''',
r'''robustness experiment of Section 3.3 satisfies this by construction. In the executed calibration all parameters entering the effort law are positive (\(r\), \(K\), \(q\), \(E_{\max}\), \(\Delta_{\rm ref}\), \(Z_{\rm ref}\), \(\tau_m > 0\)); because \(Z_{\rm ref} > 0\) and \(\widehat Z_n \ge 0\), the rational term is well defined on the admissible state space. The effort law's rational term is undefined at'''),

("A4-baseline-pattern",
r'''contemporaneous, \(\widehat Z_n = Z(t_n^-)\). The review map is the''',
r'''contemporaneous, \(\widehat Z_n = Z(t_n^-)\): each command uses the just-flowed end-of-period state, indexed by the review that reads it (\(\widehat Z_{n+1}\) in (4)); the exact update holds this same flowed value. The review map is the'''),

("A1-protective-law",
r'''\right],
\]

together with the shifted, floored softplus signal map''',
r'''\right],
\]

The protective comparator is the quota-tracking law

\[
F_B^{\rm prot}(E,Z)=\left(1-\frac{E}{E_{\max}}\right)
\eta_p\bigl(E_{\rm cap}(Z)-E\bigr),
\qquad
E_{\rm cap}(Z)=E_0\frac{Z_{\rm ref}}{Z_{\rm ref}+Z},
\]

with \(\eta_p = \eta\) and \(E_0 = E^*(Z_{\rm ref}+\delta)/Z_{\rm ref}\), calibrated so its unique interior rest coincides with the extractive fixed point; its linearised gains there are \(C_E = -0.850336\), \(C_Z = -1.661702\) (Abaee, 2026, equation~(3)), reviewed through the same projection \(\Pi_{[0,E_{\max}]}\).

together with the shifted, floored softplus signal map'''),

("F38-display-delta",
r'''with shift \(\delta\) a constant regularisation offset (distinct from
and unrelated to the effort-law gain \(\delta_0\)) and sharpness \(k\)''',
r'''with shift \(\delta = \log 2/10 \approx 0.069\), the equilibrium memory level (\(Z^* = \Phi(0) = \delta\); distinct from
and unrelated to the effort-law gain \(\delta_0\)) and sharpness \(k\)'''),

("A1-gloss-wiring",
r'''Three comparators are distinctly specified: the protective controller (the same machinery with the
response to decline entering with the opposite sign), the fixed-plan''',
r'''Three comparators are distinctly specified: the protective controller (the quota-tracking law above, the same machinery with the
response to decline entering with the opposite sign), the fixed-plan'''),

("F4-centuries-number",
r'''governance; the dominant timescales are centuries, beyond the length''',
r'''governance; the dominant timescales are centuries (the archived slow-stock cohort cycle: \(P \approx 250{-}360\) yr), beyond the length'''),

("A11-aE-threshold",
r'''the limit is used when \(|a(E)T_r|\) is small to avoid cancellation''',
r'''the limit branch is used when \(|a(E)| < 10^{-12}\)'''),

("A4-exact-held",
r'''linearised effort law \(\dot e = C_E e + C_Z z\) with the assessment
\(z\) held, where''',
r'''linearised effort law \(\dot e = C_E e + C_Z z\) with the flowed end-of-period assessment
\(z\) held, where'''),

("F27b-Re-sign",
r'''sampled stability follows the sign of the continuous eigenvalue
\(\lambda_j\); and this section records''',
r'''sampled stability follows the sign of \(\mathrm{Re}\,\lambda_j\); and this section records'''),

("F27b-so-Re",
r'''linearisation of the same loop violates the Routh--Hurwitz condition, so
\(\lambda > 0\) --- the direction''',
r'''linearisation of the same loop violates the Routh--Hurwitz condition, so
\(\mathrm{Re}\,\lambda > 0\) --- the direction'''),

("A1-gains-34",
r'''comparator run (sign-reversed response) on the same plant
gives exact-update spectral radius''',
r'''comparator run (sign-reversed response; linearised gains \(C_E = -0.850336\), \(C_Z = -1.661702\)) on the same plant
gives exact-update spectral radius'''),

("A1-stage-pointer",
r'''quota-tracking gains in the linearised review map, the same
convention as the logistic protective record.''',
r'''quota-tracking gains of Section 2.1 in the linearised review map, the same
convention as the logistic protective record.'''),

("A7-effort-channel",
r'''classes, which converge at every \(T_r \in [1,20]\). The slow-stock''',
r'''classes, which converge at every \(T_r \in [1,20]\). In the multiplier-unstable long-horizon band (\(T_r \ge 34\) yr) the faster-class trajectories remain biomass-converged or weak (relative tail standard deviation at most 0.6\%) while effort excursions grow from approximately 7--15\% at band entry to approximately 190\% at \(T_r = 50\): the instability manifests in the effort channel, to which the classifier --- a biomass-tail threshold --- is insensitive. The slow-stock'''),

("I3-entry-34-35",
r'''band, entering at 34--42 yr and extending to the grid's end, which has''',
r'''band, entering at 34--35 yr and extending to the grid's end, which has'''),

("AppA-delta-prose",
r'''logistic-core parameter vector that the text does not list (\(r\), \(K\),
\(E_{\max}\), \(\delta_0\), \(Z_{\rm ref}\), \(\Delta_{\rm ref}\),
\(\delta\), \(\tau_m\)), the linearised fixed point''',
r'''logistic-core parameter vector that the text does not list (\(r\), \(K\),
\(E_{\max}\), \(\delta_0\), \(Z_{\rm ref}\), \(\Delta_{\rm ref}\),
\(\tau_m\); \(\delta = \log 2/10\) is stated in Section 2.1), the linearised fixed point'''),

("Table3-delta-row",
r'''Logistic hold-map core & \(r\), \(K\), \(E_{\max}\), \(\delta_0\),
\(Z_{\rm ref}\), \(\Delta_{\rm ref}\), \(\delta\), \(\tau_m\) & not
listed here & computational record (this
appendix) \\''',
r'''Logistic hold-map core & \(r\), \(K\), \(E_{\max}\), \(\delta_0\),
\(Z_{\rm ref}\), \(\Delta_{\rm ref}\), \(\tau_m\) & not
listed here & computational record (this
appendix) \\
Logistic hold-map core & memory shift \(\delta\) & \(\log 2/10 \approx 0.069\) (equilibrium memory level) & Section 2.1 \\'''),
]

def main():
    import os
    s = open(SRC, encoding="utf-8").read()
    for name, old, new in SUBS:
        n = s.count(old)
        if n != 1:
            print(f"FAIL {name}: count={n}")
            sys.exit(1)
        s = s.replace(old, new)
        print(f"ok {name}")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "w", encoding="utf-8").write(s)
    print("wrote", DST, len(s), "bytes")

if __name__ == "__main__":
    main()
