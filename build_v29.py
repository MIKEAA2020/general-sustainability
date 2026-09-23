#!/usr/bin/env python3
"""Build paper1_assessment_separation_v29.tex from the v28 base (= p1.txt)."""
import sys

src = open('/home/user/v28_base.tex', encoding='utf-8').read()
edits = []

# 1. Header revision tag
edits.append(("Revision v28 (review build with line numbers)",
              "Revision v29 (review build with line numbers)", "header"))

# 2. Date
edits.append(("\\date{September 10, 2026}", "\\date{September 11, 2026}", "date"))

# 3. Abstract (marker-based)
i = src.find("\\begin{abstract}")
j = src.find("\\end{abstract}")
assert i != -1 and j != -1, "abstract markers not found"
new_abstract = r'''\begin{abstract}

Sustainability assessments routinely boil many different things ---
money, natural resources, clean water, biodiversity --- into a single
index, on the assumption that a shortfall in one can always be made up
by a surplus in another. This paper proves that the assumption fails in
a precise, practical way. An aggregate index can look sound under every
possible weighting and still certify a transition that a floor-by-floor
assessment rejects, because having some plan that works for each
weighting is not the same as having one plan that works for all
weightings at once.

The finding is demonstrated on a small, explicit example: two protected
service floors and a limited reserve, managed over a single review
period. Where the two assessments diverge, the region splits in two:
one part can be rescued by spending a defined amount of reserve; the
rest is impossible under every weighting, no matter how the index is
weighted. Two further results bound the finding. Allowing policies to be
mixed as fractional blends closes the gap exactly where aggregation
permitted it, while merely alternating between policies over time does
not. The gap is therefore a property of the limited menu of options, not
of either sustainability philosophy.

Practical message: where separately-binding floors matter, reporting
them individually is a detection requirement rather than a presentation
preference --- the aggregate alone cannot tell the rescuable from the
impossible. All results are proved analytically and verified by exact
computation.

\end{abstract}'''
src = src[:i] + new_abstract + src[j + len("\\end{abstract}"):]

# 4. Worked example before Figure 1
edits.append((
    r'''\subsubsection{4.7 Figure 1}\label{figure-1}''',
    r'''\textbf{Example (the witness point).} At \((x, s_1, s_2) = (\tfrac12, \tfrac65, \tfrac65)\), the interior witness of Figure 1, Panel A, the typed verdict is rejection: STAGED's \(x\)-tube reaches \(\tfrac12 - 1 = -\tfrac12 < 0\); FAST's worst-case \(s_1\) dips to \(\tfrac65 - 2 = -\tfrac45 < 0\); SLOW's worst-case \(s_2\) dips to \(-\tfrac45 < 0\); NO-SWITCH misses \(G\). Yet \(s_1 + s_2 = \tfrac{12}{5} \ge 2\), so the state is in \(\mathcal{V}_{\mathrm{weak}}\), with thresholds \(\rho_1 = (2 - \tfrac65)/(\tfrac65) = \tfrac23\) and \(\rho_2 = (\tfrac65)/(2 - \tfrac65) = \tfrac32\). FAST is licensed exactly for \(r \ge \tfrac23\) and SLOW exactly for \(r \le \tfrac32\); the intervals overlap, so every weight ratio \(r \ge 0\) licenses at least one action, but the licensed action depends on \(r\): \(r = 2\) (heavy on \(s_2\)) licenses FAST only, \(r = \tfrac12\) licenses SLOW only, \(r = 1\) licenses both. The aggregate thus certifies this state under every weighting while no single plan passes every weighting. By contrast, \((x, s_1, s_2) = (\tfrac12, \tfrac1{10}, \tfrac1{10})\) has \(s_1 + s_2 = \tfrac15 < 2\) and \(x < 1\), so it fails even the weak test while remaining in \(\mathcal{V}_{\mathrm{phys}}\) --- the point that makes the second inclusion strict. At \((x, s_1, s_2) = (1, \tfrac65, \tfrac65)\), \(x \ge 1\) with the same floors, STAGED's \(x\)-tube is \([0, 1]\), the floors grow, and the successor \((1, 0, s + e) \in G\), so the state is typed-accepted, as \(R\) promises.

\subsubsection{4.7 Figure 1}\label{figure-1}''',
    "worked-example"))

# 5. Aubin & Catte in 5.2
edits.append((
    "Tomlin, and Sastry, 1999). Proposition 3(i) is constraint-set",
    r'''Tomlin, and Sastry, 1999); the fixed-point and algebraic character of these objects is developed in Aubin and Catt\'e (2002). Proposition 3(i) is constraint-set''',
    "aubin-catte"))

# 6. Cardaliaguet in 4.10 remark
edits.append((
    "extension closes; this is also the here-and-now versus wait-and-see",
    "extension closes. The two-player reach/avoid formulation of such games is the discriminating kernel of Cardaliaguet (1996), with numerical treatment in Cardaliaguet, Quincampoix, and Saint-Pierre (1999). This is also the here-and-now versus wait-and-see",
    "cardaliaguet"))

# 7. Lade in 5.3
edits.append((
    "collapses into universal rejection. The separation is exhibited for, and scoped to, the specified action-indexed class.",
    "collapses into universal rejection. The separation is exhibited for, and scoped to, the specified action-indexed class; that the coupled regime is not a remote possibility is indicated by evidence that planetary-boundary processes interact and amplify one another (Lade et al., 2020).",
    "lade"))

# 8. O'Neill + Fanning in 5.4 Third
edits.append((
    "index alone cannot distinguish the rescue region from the impossibility\nregion. A minimum report for such an assessment should include:",
    "index alone cannot distinguish the rescue region from the impossibility region. The same separately-checked-floor logic underlies the safe-and-just-space (``doughnut'') literature, which evaluates social thresholds and biophysical ceilings independently, without cross-compensation, and reports that no country satisfies all floors within all ceilings (O'Neill et al., 2018; Fanning et al., 2022). A minimum report for such an assessment should include:",
    "oneill-fanning"))

# 9. Generalized rescue threshold + error-bound remark
edits.append((
    r'''\textbf{Proposition (rescue threshold).} \emph{On the witness datum, for the STAGED action and \(x < 1\), \(\kappa^* = 1 - x\).} \emph{Proof.} STAGED is typed-admissible exactly when its \(x\)-tube stays nonnegative, i.e.\ when \(x + \kappa \ge 1\); the least such increment is \(1 - x\). \ensuremath{\square} The increment converts an impossibility-region state into a typed-transformable one. States of the rescue set \(R\) need no augmentation, since STAGED is typed-admissible there; this is why \(R\) is not part of the acceptance gap.''',
    r'''\textbf{Proposition (rescue threshold).} \emph{On the witness datum, for every \(z \in X_0\),}
\[\kappa^*(z) = (1 - x)_+ \cdot \mathbf{1}[\,x < 1,\; s_1 < 2,\; s_2 < 2\,] = (1 - x) \cdot \mathbf{1}[\,z \notin \mathcal{V}_{\mathrm{typ}}\,].\]
\emph{Proof.} Among the augmented menu, only \(\mathrm{STAGED}_\kappa\) depends on \(\kappa\), and its typed-admissibility is independent of the floors: its \(x\)-tube is \([x + \kappa - 1,\; x + \kappa]\), the floors are nondecreasing (they grow to \(s + e\) with \(e = (\tfrac14, \tfrac14) > 0\)), and the successor \((1, x + \kappa - 1, s + e)\) lies in \(G\) exactly when \(x + \kappa - 1 \ge 0\). Hence \(\mathrm{STAGED}_\kappa \in E_{\mathrm{typ}}(z) \iff x + \kappa \ge 1\), for every \(z\). If \(z \in \mathcal{V}_{\mathrm{typ}}\), some base action of \(\mathcal{A} \subseteq \mathcal{A}_\kappa\) is admissible at \(\kappa = 0\), so \(\kappa^*(z) = 0\). If \(z \notin \mathcal{V}_{\mathrm{typ}}\) --- that is, \(x < 1\) and \(s_1 < 2\) and \(s_2 < 2\) --- then NO-SWITCH, FAST, and SLOW all fail (Theorem 5(1)), the only admissible element of \(\mathcal{A}_\kappa\) is \(\mathrm{STAGED}_\kappa\), and it is admissible exactly for \(\kappa \ge 1 - x\); hence \(\kappa^*(z) = 1 - x\). \ensuremath{\square}

On the impossibility region \(I\), \(\kappa^*(z) = 1 - x > 0\); on the rescue set \(R\), and on all of \(\mathcal{V}_{\mathrm{typ}}\), \(\kappa^*(z) = 0\), matching the observation that states of \(R\) need no augmentation. Because \(\mathrm{STAGED}_\kappa\) is admissible exactly when \(x + \kappa \ge 1\), independently of the floors, the resource route admits every state with \(x < 1\) --- including states outside \(\mathcal{V}_{\mathrm{weak}}\), such as \((\tfrac12, \tfrac1{10}, \tfrac1{10})\) --- at cost \(1 - x\); the impossibility region is exactly the set on which the four-action menu fails yet resource augmentation succeeds at finite cost. The increment converts an impossibility-region state into a typed-transformable one.

\textbf{Remark (error-bound modulus).} Along the resource route the minimal increment is the affine function \(f(z) = (1 - x)_+\), whose error-bound modulus (Fabian et al., 2010) is identically \(1\) on \(\{x < 1\}\); the rescue threshold \(\kappa^*\) therefore coincides with the error-bound modulus along this route. The coincidence reflects the linearity of the route. On data with nonlinear resource dynamics the two quantities diverge, and the error-bound modulus governs only the scaling of distance-to-feasibility under unstructured perturbation, a regime outside the present scope (Section 6.2).''',
    "kappa"))

# 10. References: Aubin & Catte
edits.append((
    r'''Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. (2011). \emph{Viability Theory: New Directions}, 2nd ed.~Birkh\"auser, Boston.''',
    r'''Aubin, J.-P., Bayen, A. M., and Saint-Pierre, P. (2011). \emph{Viability Theory: New Directions}, 2nd ed.~Birkh\"auser, Boston.

Aubin, J.-P., and Catt\'e, F. (2002). Bilateral fixed-points and algebraic properties of viability kernels and capture basins of sets. \emph{Set-Valued Analysis}, 10(4), 379--416.''',
    "ref-aubin-catte"))

# 11. References: Cardaliaguet x2
edits.append((
    r'''Cairns, R. D., and Martinet, V. (2014). An environmental-economic
measure of sustainable development. \emph{European Economic Review}, 69,
4--17.''',
    r'''Cairns, R. D., and Martinet, V. (2014). An environmental-economic
measure of sustainable development. \emph{European Economic Review}, 69,
4--17.

Cardaliaguet, P. (1996). A differential game with two players and one target. \emph{SIAM Journal on Control and Optimization}, 34(4), 1441--1460.

Cardaliaguet, P., Quincampoix, M., and Saint-Pierre, P. (1999). Set-valued numerical analysis for optimal control and differential games. In: \emph{Stochastic and Differential Games: Theory and Numerical Methods}, Annals of the International Society of Dynamic Games, vol.~4, Birkh\"auser, Boston, 177--247.''',
    "ref-cardaliaguet"))

# 12. References: Fabian + Fanning
edits.append((
    "44(2), 165--185.",
    r'''44(2), 165--185.

Fabian, M. J., Henrion, R., Kruger, A. Y., and Outrata, J. V. (2010). Error bounds: necessary and sufficient conditions. \emph{Set-Valued Analysis}, 18(2), 121--149.

Fanning, A. L., O'Neill, D. W., Hickel, J., and Roux, N. (2022). The social shortfall and ecological overshoot of nations. \emph{Nature Sustainability}, 5(1), 26--36.''',
    "ref-fabian-fanning"))

# 13. References: Lade
edits.append((
    "167, 106331.",
    r'''167, 106331.

Lade, S. J., Steffen, W., de Vries, W., Carpenter, S. R., Donges, J. F., Gerten, D., Hoff, H., Newbold, T., Richardson, K., and Rockstr\"om, J. (2020). Human impacts on planetary boundaries amplified by Earth system interactions. \emph{Nature Sustainability}, 3(2), 119--128.''',
    "ref-lade"))

# 14. References: O'Neill
edits.append((
    "4th ed.~Edward Elgar, Cheltenham.",
    r'''4th ed.~Edward Elgar, Cheltenham.

O'Neill, D. W., Fanning, A. L., Lamb, W. F., and Steinberger, J. K. (2018). A good life for all within planetary boundaries. \emph{Nature Sustainability}, 1(2), 88--95.''',
    "ref-oneill"))

# 15. Data availability
edits.append((
    "The proofs are contained in this article. The verification code for the finite rational instance (all 25 checks; deterministic exact-integer arithmetic) is archived in a public repository; a link is provided with the submission.",
    "The verification code for the finite rational instance (all 25 checks; deterministic exact-integer arithmetic) is archived at \\url{https://zenodo.org/records/22545740}.",
    "data-availability"))

failed = False
for old, new, label in edits:
    n = src.count(old)
    if n != 1:
        print(f"FAIL [{label}]: anchor found {n} times (expected 1)")
        failed = True
    else:
        src = src.replace(old, new)
        print(f"ok   [{label}]")

if failed:
    sys.exit(1)

out = '/home/user/paper1_assessment_separation_v29.tex'
open(out, 'w', encoding='utf-8').write(src)
print(f"\nWROTE {out} ({len(src)} bytes)")

a = src.find("\\begin{abstract}"); b = src.find("\\end{abstract}")
ab = src[a:b].replace("\\begin{abstract}", "").replace("---", " ")
print(f"abstract word count: {len(ab.split())}")
