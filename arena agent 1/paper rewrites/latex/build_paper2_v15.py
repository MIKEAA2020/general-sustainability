#!/usr/bin/env python3
"""Build paper2 v15 from v14 (= v13 + lineno + date): strip change-log residue,
internal dialogue, meta-commentary, chat-history register, and naive
over-hedging; fix typos, the Limitations enumeration, and reference order.
All theorems, proofs, and equations unchanged."""
import re

PATH = "/home/user/paper2_v15/paper2_obstruction_calculus_v15.tex"
src = open(PATH).read()

def block(pattern, replacement, expect=1, flags=re.DOTALL):
    global src
    found = len(re.findall(pattern, src, flags))
    assert found == expect, f"BLOCK expect={expect} found={found}: {pattern[:80]!r}"
    src = re.sub(pattern, lambda m: replacement, src, flags=flags)

def sub(plain, replacement, expect=1):
    global src
    rx = re.escape(plain).replace(r"\ ", r"\s+")
    found = len(re.findall(rx, src))
    assert found == expect, f"SUB expect={expect} found={found}: {plain[:80]!r}"
    src = re.sub(rx, lambda m: replacement, src)

# B1: header provenance -> minimal formal header
block(r"\A% LaTeX source generated.*?\(also compatible with pdflatex/xelatex\)\.\n",
"""% An Obstruction Calculus for Viability under Incomplete Observation
% Amin Abaee. Revision v15 (cleaned revision with line numbers for review). Compiles with tectonic, pdflatex, or xelatex.
""")

# B2: 6.5 Limitations enumeration bug -> five proper items
block(r"\\item\n  The certificates are sufficient conditions for nonviability, not.*?belongs to applied studies\.",
"""\\item
  The certificates are sufficient conditions for nonviability, not necessary-and-sufficient characterizations of the epistemic kernel; the middle ground (neither a Veliov-type condition nor an obstruction certificate) is open.
\\item
  The information-set semantics is set-membership; probabilistic or belief-space formulations require separate statements, although the common-action obstruction transfers mutatis mutandis to any semantics in which the policy must choose a single action per information state.
\\item
  The results are finite-dimensional and time-invariant; the delay-free setting makes the timing bound of Theorem 4 sharp, and delay systems require the retarded extension of the Dini comparison argument (Hale and Verduyn Lunel, 1993).
\\item
  Theorem 1's adversarial-realization step presupposes both the closed-graph regularity of Section 2.1 and the closed-loop existence hypothesis (H1.2) --- \\(D\\) lower semicontinuous or constant, or the convexified reading; without these the certificate remains a heuristic.
\\item
  The institutional consequences of Section 6.4 are design conclusions from the certificates, not empirical findings; their empirical testing belongs to applied studies.""")

# B3: references -> alphabetical (Abaee first), clean companion entry
block(r"Aubin, J\.-P\.: Viability Theory\..*?Companion\nassessment-separation analysis\.",
"""Abaee, A.: The limits of compensatory aggregation: a formal separation of weak and strong sustainability assessment. Zenodo. https://doi.org/10.5281/zenodo.22545740 (2026).

Aubin, J.-P.: Viability Theory. Birkh\\"auser, Boston (1991)

Aubin, J.-P., Bayen, A.M., Saint-Pierre, P.: Viability Theory: New Directions, 2nd edn. Birkh\\"auser, Boston (2011)

Aubin, J.-P., Frankowska, H.: Set-Valued Analysis. Birkh\\"auser, Boston (1990)""")

# B4: double rule before Appendix A -> single
block(r"\\begin\{center\}\\rule\{0\.5\\linewidth\}\{0\.5pt\}\\end\{center\}\s+\\begin\{center\}\\rule\{0\.5\\linewidth\}\{0\.5pt\}\\end\{center\}\s+(?=\\subsection\{Appendix A)",
"\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n")

# ---------------- targeted edits ----------------
sub("and its consequences for monitoring design --- the timing, coarseness, and bias of observation --- are drawn.",
    "and its consequences for monitoring and institutional design --- observation timing, coarseness, aggregation, and bias --- are drawn.")
sub("constrained sustainability", "sustainability governance")
sub("The further four mechanisms cover a finite-time exit certificate",
    "The other four mechanisms cover a finite-time exit certificate")
sub("Such a base can be eroding while measured output is maintained.",
    "Such a base can erode while measured output is maintained.")
sub("address the same underlying ill-posedness rather than competing ones.",
    "address the same underlying indeterminacy rather than competing ones.")
sub("the other bounds the timing uniformly over every policy --- and are reported as such.",
    "the other bounds the timing uniformly over every policy.")
sub("and Example 1 carries the genuine hidden-mode reading.",
    "and Example 1 gives the genuine hidden-mode instance.")
sub("for every policy in the declared class", "for every policy in the prescribed class")
sub("not a failure exhibit.", "not itself an exhibit of failure.")
sub("are cited rather than reproduced, and are marked as such.",
    "are cited in Section 5 rather than reproduced.")
sub("respecting the declared information structure", "respecting the specified information structure")
sub("is retained as a named contrast class only (the a-fortiori caveat of Section 2.3); no theorem of this paper is stated for it.",
    "is defined as a contrast class only (see the a-fortiori caveat in Section 2.3); no theorem of this paper is stated for it.")
sub("applied explicitly to the first two terms, whose native elements are information states",
    "applied to the first two terms, whose elements are information states")
sub("is the institutionally restricted counterpart (Section 6.4), \\textbf{defined in one line} as the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set \\(U_{\\mathcal{J}}(x) \\subseteq U(x)\\) --- a DEFINED-NOT-THEOREM object: the definition fixes the symbol's meaning, and no theorem of this paper is stated for it.",
    "is the institutionally restricted counterpart (Section 6.4), defined as the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set \\(U_{\\mathcal{J}}(x) \\subseteq U(x)\\). This is a definition, not a theorem: it fixes the symbol's meaning, and no theorem of this paper is stated for it.")
sub("B_0 \\subseteq \\mathrm{RViab}(\\mathcal{V})\\).", "B_0 \\subseteq \\mathrm{RViab}(\\mathcal{V})\\).")
sub("while every trajectory is doomed to exit later", "while every trajectory must exit later")
sub("--- the extensions are stated in Section 6.5.)", "--- the extensions are noted as open in Section 6.5.)")
sub("the quantifier order is load-bearing, because", "the quantifier order is essential, because")
sub("is retained as a named contrast class only, for the a-fortiori caveat below; its coupled-record semantics is used by no theorem.",
    "is defined as a contrast class only, for the a-fortiori caveat below; no theorem uses its coupled-record semantics.")
sub("--- the existential contrast class, in one line: there exist", "--- the existential contrast class: there exist")
sub("With this definition, the informal statement of the paper is precise:", "The thesis is now precise:")
sub("We collect the principal symbols used throughout the paper and freeze the two structural symbols:",
    "We collect the principal symbols used throughout the paper and fix the two structural symbols:")
sub("(calligraphic J); and no other letter serves either role.", "(calligraphic J); no other letter serves either role.")
sub("under the convention (explicit from Theorem 2 on) that", "under the convention, used from Theorem 2 on, that")
sub("is retained as a named contrast class only (Section 2.3's a-fortiori caveat; no theorem is stated for it)",
    "is defined as a contrast class only (Section 2.3's a-fortiori caveat; no theorem is stated for it)")
sub("The institutionally restricted kernel is \\(\\mathrm{IRViab}_{\\mathcal{J}}(\\mathcal{V})\\) --- DEFINED-NOT-THEOREM: in one line, the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set \\(U_{\\mathcal{J}}(x) \\subseteq U(x)\\) (Section 6.4).",
    "The institutionally restricted kernel is \\(\\mathrm{IRViab}_{\\mathcal{J}}(\\mathcal{V})\\) (Section 6.4): a definition, not a theorem --- the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set \\(U_{\\mathcal{J}}(x) \\subseteq U(x)\\).")
sub("Local scopes, declared once here to prevent the residual letter collisions:",
    "Some letters carry site-local meanings:")
sub("the locally Lipschitz reading remains a declared extension, not proved here",
    "the locally Lipschitz reading is an extension not proved here")
sub("(Recorded alternative: without (H1.2),", "(Alternatively, without (H1.2),")
sub("are the standard tools for exactly this step", "are the standard tools for this step")
sub("under the completed hypotheses", "under hypotheses", expect=3)
sub("--- exactly hypothesis (H1.2)'s content", "--- exactly the content of (H1.2)")
sub("the locally Lipschitz case is a declared extension, not proved here:",
    "the locally Lipschitz case is an extension not proved here:")
sub("--- and this is exactly what the certificate needs;", "--- which is what the certificate requires;")
sub("and the kernel empties only under the observation structure; their register is stated per mechanism.",
    "and the kernel empties only under the observation structure.")
sub("are the informational register proper, merging states", "are the informational cases proper, merging states")
sub("The register of the mechanism is \\emph{admissibility} rather than a hidden mode:",
    "The mechanism is \\emph{admissibility} rather than a hidden mode:")
sub("at minimal size, manufactured by the control-set primitive rather than by information",
    "at minimal size, produced by the control-set primitive rather than by information")
sub("The construction isolates the mechanism, and its register is admissibility:",
    "The construction isolates an admissibility mechanism:")
sub("is thereby exercised explicitly:", "is used explicitly:")
sub("which is why the construction is not presented as a hidden-mode mechanism.",
    "so the construction is an admissibility mechanism rather than a hidden-mode mechanism.")
sub("be an information set of the declared observation structure", "be an information set of the specified observation structure")
sub("must be replaced by the tube-safety statement of the tube-safety form below",
    "must be replaced by the tube-safety statement below")
sub("the control-space analogue of the material-substitution separation certificates reported in the companion assessment-separation analysis (Author et al., in review).",
    "the control-space analogue of the material-substitution separation certificates in the companion assessment-separation analysis (Abaee, 2026).")
sub("(the reading declared in Section 2.4),", "(the reading specified in Section 2.4),")
sub("--- formally, for every observation-based policy the hypothesis below supplies branches that are",
    "--- formally, there are branches that are")
sub("It is this open-loop form that makes the timing bound (4) load-bearing",
    "It is this open-loop form that gives the timing bound (4) its force")
sub("and is a template in the general case, as the abstract records.",
    "and is a template to be instantiated in the general case.")
sub("--- the cause of the obstruction; read as the design requirement it inverts, the first informative observation must precede the enforced exit time",
    "--- the cause of the obstruction; inverted, it reads as the design requirement that the first informative observation precede the enforced exit time")
sub("the delayed tube-safety obstruction; the two certificates are stated separately;",
    "the delayed tube-safety obstruction. The two certificates are separate;")
sub("Sustainability governance also consumes \\emph{certificates}", "Sustainability governance also uses \\emph{certificates}")
sub("on the safe side of a declared floor.", "on the safe side of a specified floor.")
sub("measurability is the only additional requirement and is stated once here.",
    "measurability is the only additional requirement.")
sub("on opposite sides of a declared floor", "on opposite sides of a specified floor")
sub("The certainly-safe set is the honest relaxation:", "The certainly-safe set is the sound relaxation:")
sub("arrives is one of them, so no separate proposition is stated.", "arrives is one of them.")
sub("\\(\\Pi_{\\mathrm{CE}}\\), defined here in one formal definition: \\(\\Pi_{\\mathrm{CE}}\\) is the class of causal controllers",
    "\\(\\Pi_{\\mathrm{CE}}\\), defined as the class of causal controllers")
sub("the kernel empties exactly when the controller refuses the correction.",
    "the kernel empties exactly when the controller does not apply the correction.")
sub("where a stronger observer or a finer observation structure is the only remedy.",
    "where a stronger observer or a finer observation structure is the natural remedy.")
sub("The exact relationship is the one stated in Section 6.3: correctly carried out under the set-membership semantics, the estimation-space solution propagates the belief under a single control signal, so its controls \\emph{are} common controls and joint admissibility is built into the estimation-space problem's own admissibility. The caveat that the estimation-space policy is a set-valued feedback \\emph{whose pointwise selections, taken without that joint-admissibility check, need not be jointly admissible} concerns the unchecked selection reading, not the reduction itself; the common-action obstruction (Theorem 3) is precisely the certificate that no jointly admissible selection exists at the information state in question.",
    "The exact relationship is stated in Section 6.3: carried out under the set-membership semantics, the estimation-space solution propagates the belief under a single control signal, so its controls \\emph{are} common controls and joint admissibility is built into the estimation-space problem's own admissibility. Pointwise selections taken without that joint-admissibility check need not be jointly admissible; the common-action obstruction (Theorem 3) is precisely the certificate that no jointly admissible selection exists at the information state in question.")
sub("see the buffer constructions of Section 1.3's cited literature",
    "see the buffer constructions in the literature cited in Section 1.3")
sub("must meet a demand vector through declared substitution pathways",
    "must meet a demand vector through specified substitution pathways")
sub("is a certificate that the declared substitution pathways cannot meet demand",
    "is a certificate that the specified substitution pathways cannot meet demand")
sub("the same infeasibility discipline --- exhibit the separating multiplier rather than assert impossibility --- applies to both.",
    "the same infeasibility logic --- exhibit the separating multiplier rather than assert impossibility --- applies to both.")
sub("The six mechanisms form a useful but nonexhaustive taxonomy", "The six mechanisms form a nonexhaustive taxonomy")
sub("in the admissibility register of Section 3.2", "in the admissibility form of Section 3.2")
sub("has no diagnostic force, and no sentence in this paper relies on it.", "has no diagnostic force.")
sub("while observer-based and belief-space barrier constructions exist and certify safety under a specified controller",
    "while observer-based and belief-space barrier constructions have been proposed that certify safety under a specified controller")
sub("and, correctly carried out, its belief-state controls are common controls applicable to all compatible states under the declared semantics.",
    "and its belief-state controls are common controls applicable to all compatible states under the specified semantics.")
sub("which is the same certificate a robustness analysis computes anyway.",
    "which a robustness analysis computes in any case.")
sub("finer observation never hurts (it merges nothing the coarser one did not), though Theorem 3",
    "refinement is never harmful (a finer observation merges nothing the coarser one did not), though Theorem 3")
sub("a formal complement to the thesis, argued verbally since Martinez-Alier",
    "a formal complement to the thesis, argued informally since Martinez-Alier")
sub("the certainly-safe set is the honest domain of an index-based verdict.",
    "the certainly-safe set is the domain in which an index-based verdict is sound.")
sub("and the second is the one governance structures most often omit:",
    "and the second is the one governance structures can omit:")
sub("--- defined in one line at Section 2.1 as the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set \\(U_{\\mathcal{J}}(x) \\subseteq U(x)\\); DEFINED-NOT-THEOREM, no theorem claimed for it --- combines them:",
    "--- defined in Section 2.1 as the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set \\(U_{\\mathcal{J}}(x) \\subseteq U(x)\\), a definition with no theorem claimed for it --- combines them:")
sub("We close the discussion by stating the scope of the results explicitly. The certificates are sound but not complete; several extensions are noted as open.",
    "The certificates are sound but not complete; several extensions are noted as open.")
sub("(Theorem 2's admissibility register);", "(Theorem 2's admissibility form);")
sub("They are stated in full because each carries a scope remark that is itself part of the contribution; none of them is promoted to a theorem of the main text.",
    "They are stated in full with their scope remarks; none of them is stated as a theorem of the main text.")
sub("define the Lyapunov function \\(W = S_1 + S_2\\) (the letter \\(W\\) is used because \\(U\\) is the control-set letter of Section 2.4); then",
    "define the Lyapunov function \\(W = S_1 + S_2\\); then")
sub("and the two are separated deliberately.", "and the two are kept separate.")
sub("None declared.", "None.")
sub("available from the authors on request.", "available from the author on request.")

open(PATH, "w").write(src)
print("OK - all v15 substitutions applied")
