#!/usr/bin/env python3
"""Build paper5 v28 from v27: joint-audit response (editor-safe fixes).

Every substitution asserts exactly one match. Author-blocked items are NOT
touched here: F2/A1 (protective), F4/A2 (four-state period), A3 (parameter
vector, delta, Zref; F9, F38), A4 (indexing), F27b (lambda hedge), F12
(archive quarantine), A5-A7, I3 (band entry), I5 (code heading).
"""
import os

SRC = "/home/user/paper5_v27/paper5_sampled_governance_v27.tex"
DST = "/home/user/paper5_v28/paper5_sampled_governance_v28.tex"

r = lambda s: s  # marker: strings below are raw triple-quoted

SUBS = [
("L1-version",
r'''% Periodic Review as Sampled Governance (paper 5, revision v27): cleaned revision with line numbers for review.''',
r'''% Periodic Review as Sampled Governance (paper 5, revision v28): audit-response revision with line numbers for review.'''),

("F33-hyperref-order",
r'''\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}
\usepackage[font=small,labelfont=bf]{caption}''',
r'''\usepackage[font=small,labelfont=bf]{caption}
\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}'''),

("date-sep11",
r'''\date{September 10, 2026}''',
r'''\date{September 11, 2026}'''),

("P-L106-band",
r'''stable band {[}47.54, 79.14{]} yr & Closed-form monodromy, 200,001-point''',
r'''stable band {[}47.536, 79.143{]} yr & Closed-form monodromy, 200,001-point'''),

("P-L110-band",
r'''{[}0.2, 2.31{]} yr & Same record; artefact band''',
r'''{[}0.2, 2.306{]} yr & Same record; artefact band'''),

("F34-Box-map",
r'''Exact held-assessment map: single complex crossing at 6.501 yr (unstable''',
r'''Exact map: single complex crossing at 6.501 yr (unstable'''),

("F5-SN-pointer",
r'''surplus production --- \(S(N)\) on the logistic plant (equation (2)) and''',
r'''surplus production --- \(S(N)\) on the logistic plant (defined after equation (2)) and'''),

("F15-H4-clarifier",
r'''(H4) Any between-review deployment interpolation remains in the convex
interval joining consecutive commands.

Then''',
r'''(H4) Any between-review deployment interpolation remains in the convex
interval joining consecutive commands. The main model takes \(E(t)=E_n\), which satisfies (H4) trivially; the proposition is stated for the hold-or-interpolate class.

Then'''),

("F27a-Re-lambda",
r'''the multipliers satisfy \(\mu_j(T_r) = 1 + T_r\lambda_j(A) + O(T_r^2)\)
and local stability persists for all sufficiently small positive review
intervals. The finite-horizon''',
r'''the multipliers satisfy \(\mu_j(T_r) = 1 + T_r\lambda_j(A) + O(T_r^2)\),
so local stability persists for all sufficiently small positive review intervals provided every continuous eigenvalue satisfies \(\Re\lambda_j<0\); if any \(\Re\lambda_j>0\), the sampled equilibrium inherits instability for sufficiently small \(T_r\). The finite-horizon'''),

("F19-F34-L471",
r'''operator. The 3--4 yr windows and the 6.5 yr exact-hold crossing below
are therefore reported as a comparison across plants and operators, and
the operator effect is not claimed to be isolated by it. Changing the''',
r'''operator. The 3--4 yr windows and the \(\approx 6.5\) yr exact-update crossing below
are therefore reported as a comparison across plants and operators, which does not isolate the operator effect; the one-plant operator contrast in Section 3.4 isolates the operator for the logistic plant. Changing the'''),

("F30-degenerate",
r'''The Schaefer model is the
degenerate member of this family in which the factor''',
r'''The Schaefer model is the
formal limit of this family (\(\mathfrak s\to-\infty\)) in which the factor'''),

("F29-lemma-C0",
r'''all conditional on the solutions existing, i.e.~on \(C\) being below the
production maximum.

\begin{enumerate}
\def\labelenumi{(\roman{enumi})}''',
r'''all conditional on the solutions existing, i.e.~on \(C\) being below the
production maximum. For \(C=0\) the smaller positive equilibrium is \(\mathfrak s\); the strict rightward shift holds for \(C>0\).

\begin{enumerate}
\def\labelenumi{(\roman{enumi})}'''),

("F36-closed-form",
r'''The logistic hold-map core gives the computation objects in
closed form. With effort held''',
r'''The logistic hold-map core permits a closed-form expression for the held logistic flow; the linearised review map is then constructed from this flow, the signal dynamics, and the update derivatives. With effort held'''),

("F28-aE-caution",
r'''\(a(E) = 0\). The signal flow enters''',
r'''\(a(E) = 0\). In computations, the limit is used when \(|a(E)T_r|\) is small to avoid cancellation. The signal flow enters'''),

("F7-F16-F34def-exactblock",
r'''held-assessment controller --- the separating comparator that isolates
the Euler step --- is the exponential update
\(e_{n+1} = e^{C_E T_r}e_n + \tfrac{e^{C_E T_r}-1}{C_E}C_Z z_n\) for
\(C_E \ne 0\) --- the exact solution, over one review interval, of the''',
r'''held-assessment controller --- the separating comparator that isolates
the Euler step --- is the exponential update (the exact update)
\(e_{n+1} = e^{C_E T_r}e_n + \tfrac{e^{C_E T_r}-1}{C_E}C_Z z_n\) for
\(C_E \ne 0\), and \(e_{n+1} = e_n + T_r C_Z z_n\) for \(C_E = 0\), with
\(e_n = E_n - E^*\) and \(z_n = Z_n - Z^*\) the deviations from the compared fixed point --- the exact solution, over one review interval, of the'''),

("F17-analytical",
r'''discretisation of the same linear object. Comparing its monodromy with''',
r'''discretisation of the same linear object. This comparator is analytical, not a proposed institutional rule. Comparing its monodromy with'''),

("P-L911",
r'''forward-Euler monodromy reproducing the 47.54 yr crossing reported''',
r'''forward-Euler monodromy reproducing the 47.536 yr crossing reported'''),

("F14a-F6-L913",
r'''(Euler 1.00055); the 47.5 yr and 79.1 yr crossings are command-step
artefacts; the exact map's''',
r'''(Euler 1.00055); the 47.536 yr and 79.143 yr crossings are command-step artefacts of the forward-Euler update;
the exact map's'''),

("P-L921",
r'''at \(T_r^{\rm UC}=47.54\) yr under the''',
r'''at \(T_r^{\rm UC}=47.536\) yr under the'''),

("F14b-F6-L923",
r'''held-assessment update, with the same restabilising direction. The 47.54
yr crossing and its \(-1\) multiplier at 79.1 yr are command-step
artefacts, not a review-cadence property (Section 4.1).''',
r'''held-assessment update, with the same restabilising direction. The 47.536
yr crossing and its \(-1\) multiplier at 79.143 yr are command-step
artefacts, not a review-cadence property (Section 4.1). For an institution implementing the incremental Euler rule these crossings are dynamically real; they are artefacts only relative to the exact update.'''),

("F34-L912",
r'''the exact-hold annual spectral radius is''',
r'''the exact-update annual spectral radius is'''),

("P-L935-band",
r'''\([47.54, 79.14]\) yr --- and once on the protective channel''',
r'''\([47.536, 79.143]\) yr --- and once on the protective channel'''),

("P-F34-L937",
r'''\([0.2, 2.31]\) yr. The exact held-assessment update crosses once on the''',
r'''\([0.2, 2.306]\) yr. The exact update crosses once on the'''),

("P-L939-band",
r'''stable), stable on \([6.50, 200]\) yr --- and never''',
r'''stable), stable on \([6.501, 200]\) yr --- and never'''),

("P-L943",
r'''and the Euler protective instability beyond 2.31 yr is''',
r'''and the Euler protective instability beyond 2.306 yr is'''),

("F34-L948",
r'''are part of the record. The exact held-assessment update's annual''',
r'''are part of the record. The exact update's annual'''),

("F21-margins-47536",
r'''Neimark--Sacker signature), real \(-1\) multipliers at the Euler''',
r'''Neimark--Sacker signature) and at the Euler extractive crossing (47.536 yr), and real \(-1\) multipliers at the Euler'''),

("F13-caption",
r'''Annual review is unstable on both extractive updates;''',
r'''Annual review is nominally unstable on both extractive updates (\(\rho=1.00035\) exact, \(1.00055\) Euler; protective \(0.9838\)), conditional on the numerical construction and parameter vector (Spectral margins paragraph);'''),

("P-L979",
r'''at 6.50 yr. The companion's''',
r'''at 6.501 yr. The companion's'''),

("F13-claim",
r'''for \(0 < \tau < \tau_-\) (Abaee, 2026). Annual review is
unstable under sampling (\(\rho = 1.00035\)), and the same loop under''',
r'''for \(0 < \tau < \tau_-\) (Abaee, 2026). Annual review is
nominally unstable under sampling (\(\rho = 1.00035\), conditional on the numerical construction and parameter vector as stated above), and the same loop under'''),

("P-L987",
r'''6.50-yr crossing, the continuous loop inside''',
r'''6.501-yr crossing, the continuous loop inside'''),

("P-L989",
r'''operator's restabilising crossing (6.50 yr) sits above''',
r'''operator's restabilising crossing (6.501 yr) sits above'''),

("F35-zero-crossings",
r'''crossing (zero crossings lie strictly between \(0\) and \(\tau_-\), an
even count, as the stability-switch principle requires) --- no''',
r'''crossing (there are no crossings in \((0,\tau_-)\); this even count is consistent with the stability-switch principle because the stability state does not change between zero delay and the first crossing) --- no'''),

("F10-differ-only",
r'''additional crossings are required. The two operators then differ only in''',
r'''additional crossings are required. On this plant, the two operators differ only in'''),

("F11-lambda-gloss",
r'''shows. The eigenvalue \(\lambda\) is not listed here
(the spectral-margins record above; Appendix A); its sign is read from''',
r'''shows. The eigenvalue \(\lambda\) is not listed here
(the spectral-margins record above; Appendix A); it is a derived eigenvalue, not a parameter, and its sign is read from'''),

("F34-L1027",
r'''gives exact-hold spectral radius 0.9838''',
r'''gives exact-update spectral radius 0.9838'''),

("F23-fixed-plan",
r'''the artefact operating at the trajectory level; the fixed plan is
the equilibrium rest point (zero deviation).''',
r'''the artefact operating at the trajectory level; in the deterministic baseline with fixed effort set at the equilibrium value, the fixed plan remains at equilibrium --- a baseline rest point, not a robust performance result.'''),

("F20-status-sentence",
r'''criteria fixed in the plan), and its complete multiplier and trajectory
records are reported here. The reconstruction is a newly specified object:''',
r'''criteria fixed in the plan), and its complete multiplier and trajectory
records are reported here. The archived stage-output records are trajectory-classified only (Section 2.2). The reconstruction is a newly specified object:'''),

("F8-I1-controller-eqs",
r'''The controller of Section 2.1 is unchanged: equations (1)--(4) in annual discrete form, softplus''',
r'''The controller of Section 2.1 is unchanged: equations (3)--(4) in discrete form with \(T_r\) varied over \(\{1,\ldots,50\}\) yr at annual internal steps, softplus'''),

("F22-not-inferential",
r'''and the cell is reported as a disagreement between the
reconstruction's two records, not as an agreement.''',
r'''and the cell is reported as a disagreement between the
reconstruction's two records, not as an agreement, and is not used inferentially.'''),

("F3-three-groups",
r'''Supplementary material (S4); three illustrate the screening logic.''',
r'''Supplementary material (S4); three groups illustrate the screening logic.'''),

("F32-BH-family",
r'''no other index is. Bivariate Granger tests''',
r'''no other index is. The ninety index--lag cells define the Benjamini--Hochberg multiplicity family; the Granger and split-half tests are confirmatory and outside that family. Bivariate Granger tests'''),

("F25-review-interval-region",
r'''anchovy-class response region, so the unclassified controller prevents''',
r'''anchovy-class review-interval response region, so the unclassified controller prevents'''),

("F18-repro-targets",
r'''\(3.7\) kt yr\(^{-1}\)) are unreproduced: they are reproduction targets
requiring equations''',
r'''\(3.7\) kt yr\(^{-1}\)) are unreproduced: they are targets for future reproduction
requiring equations'''),

("F24-not-rejection",
r'''assessment table). The phase-line obstruction of Section 2.7 applies as
a model-class diagnostic: an error-free trajectory''',
r'''assessment table). The phase-line obstruction of Section 2.7 applies as
a model-class diagnostic (not an empirical rejection of scalar autonomous models for northern cod): an error-free trajectory'''),

("F14c-L1484",
r'''the Euler-reported 47.5 yr crossing being a
command-step artefact --- under the logistic hold map.''',
r'''the Euler-reported crossing near 47.5 yr being a
command-step artefact relative to the exact update --- under the logistic hold map.'''),

("P-L1496",
r'''exactly one crossing (extractive, 6.50
yr) and none''',
r'''exactly one crossing (extractive, 6.501
yr) and none'''),

("F31-AR1-limitation",
r'''adjudicates nothing about controller sign.
\item The zero-count''',
r'''adjudicates nothing about controller sign; the AR(1) null may understate low-frequency power.
\item The zero-count'''),

("F1-appendix-opener",
r'''requirements stated in Sections 2.2, 2.4, and 2.5. The convention''',
r'''requirements stated in Sections 2.2, 2.4, 2.5, 3.3, and 3.4. The convention'''),

("F26-T3-qrow",
r'''Logistic hold-map core & catchability \(q\) & 0.001 & Section 3.4 (Plant
paragraph) \\''',
r'''Logistic hold-map core & catchability \(q\) & 0.001 & Section 3.4 (stage Plant paragraph, as the hold-map core's value) \\'''),

("F34-L2056",
r'''exact-hold comparison''',
r'''exact-update comparison'''),

("F34-L2072",
r'''exact-hold assessed-controller comparison of Section 3.4''',
r'''exact-update comparison of Section 3.4'''),

("F37-deposit",
r'''fully specified and deposited with the article: the dated''',
r'''fully specified and will be deposited with the article: the dated'''),

("F34-L378-define",
r'''separating computation is the exact held-assessment update, reported in''',
r'''separating computation is the exact held-assessment update (the exact update), reported in'''),

("F34-L922-xline",
r'''at \(\approx 6.5\) yr under the exact
held-assessment update, with the same restabilising direction.''',
r'''at \(\approx 6.5\) yr under the exact update, with the same restabilising direction.'''),

("F34-L1483-xline",
r'''near 6.5 yr under the exact
held-assessment update --- the Euler-reported''',
r'''near 6.5 yr under the exact update --- the Euler-reported'''),
]

def main():
    s = open(SRC, encoding="utf-8").read()
    n0 = len(s)
    for name, old, new in SUBS:
        c = s.count(old)
        assert c == 1, f"{name}: count={c}"
        s = s.replace(old, new, 1)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "w", encoding="utf-8").write(s)
    print(f"OK - all v28 substitutions applied ({n0} -> {len(s)} bytes, {len(SUBS)} subs)")

if __name__ == "__main__":
    main()
