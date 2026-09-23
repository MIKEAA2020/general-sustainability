#!/usr/bin/env python3
"""Build paper1_assessment_separation_v37.tex from v36: remove self-referential
meta-commentary (statements ABOUT the paper's own apparatus rather than results)."""
import sys

src = open('/home/user/paper1_assessment_separation_v36.tex', encoding='utf-8').read()
def rep(old, new, label, expect=1):
    global src
    n = src.count(old)
    if n != expect:
        print(f"FAIL [{label}]: found {n}, expected {expect}")
        sys.exit(1)
    src = src.replace(old, new)
    print(f"ok   [{label}]")

# 1. Abstract: process description -> delete
rep(r"impossible. All results are proved analytically and verified by exact" + "\n" + r"computation.",
    r"impossible.",
    "abstract-meta")

# 2. §3.1: process description of the typed-endpoint observation -> delete
rep(r" This observation follows by inspection of the action table and is not part of the machine-checked artifact of Section 4.9.",
    r"",
    "s31-inspection")

# 3. §6.1: epistemic-basis description -> keep only the scope statement
rep(r"the separation results here rest on the displayed proofs (Appendices A--C) and the machine-checked finite instance of Section 4.9, and the cited studies are referenced for related work only.",
    r"the cited studies are referenced for related work only.",
    "s61-rest-on")

# 4. §5.2 run-in meta label "Established." -> drop label
rep(r"\textbf{Established.} The backward recursion of Section 3 is",
    r"The backward recursion of Section 3 is",
    "label-established")

# 5. §5.2 run-in meta label "Proved here." + self-reference -> keep the factual generality claim
rep(r"\textbf{Proved here.} Against this background, the paper proves the results" + "\n" +
    r"itemized in Section 1.3; of these, the finite-menu characterization of" + "\n" +
    r"Section 4.4 is the general form, of which the witness separation" + "\n" +
    r"(Theorem 5) and the blend collapse (Theorem 8) are the instances.",
    r"Against this background, the finite-menu characterization of" + "\n" +
    r"Section 4.4 is the general form, of which the witness separation" + "\n" +
    r"(Theorem 5) and the blend collapse (Theorem 8) are the instances.",
    "label-proved-here")

# 6. §5.2 run-in meta label "Novelty qualification." + review-process language -> plain honest scope
rep(r"\textbf{Novelty qualification.} To our knowledge, this paper provides an" + "\n" +
    r"explicit exact-tube witness for this dynamic separation in a" + "\n" +
    r"compensatory/noncompensatory assessment setting. We do not assert" + "\n" +
    r"priority over the elementary quantifier fact" + "\n" +
    r"\(\exists a\, \forall w \neq \forall w\, \exists a_w\), which is" + "\n" +
    r"standard. Whether an equivalent dynamic separation appears in adjacent" + "\n" +
    r"literatures (multi-objective robust control, viability theory," + "\n" +
    r"multi-criteria decision analysis) is a bounded absence in our review," + "\n" +
    r"not an established universal negative.",
    r"To our knowledge, no explicit exact-tube witness for this dynamic" + "\n" +
    r"separation in a compensatory/noncompensatory assessment setting is" + "\n" +
    r"reported in the literature. We do not assert priority over the" + "\n" +
    r"elementary quantifier fact" + "\n" +
    r"\(\exists a\, \forall w \neq \forall w\, \exists a_w\), which is" + "\n" +
    r"standard. Whether an equivalent dynamic separation appears in adjacent" + "\n" +
    r"literatures (multi-objective robust control, viability theory," + "\n" +
    r"multi-criteria decision analysis) is not established either way.",
    "label-novelty")

# 7. §4.9: "displayed proofs" process term -> plain location pointer
rep(r"The continuum statements of Proposition 3, Proposition 4, Theorem 5," + "\n" +
    r"Remark 6, and Theorems 7--8 are established by the displayed proofs (Appendices A--C).",
    r"Proposition 3, Proposition 4, Theorem 5, Remark 6, and Theorems 7--8" + "\n" +
    r"are proved in Appendices A--C.",
    "displayed-proofs-49")

# 8. §1.3: "organizing result" framing -> plain
rep(r"The paper's organizing result is a quantifier noncommutation.",
    r"The central result is a quantifier noncommutation.",
    "organizing-result")

# 9. §1.3: redundant pointer + duplicate novelty statement -> remove (now held fully in §5.2)
rep("\n\n" + r"To our knowledge, this provides an explicit exact-tube witness for this" + "\n" +
    r"dynamic separation in a compensatory/noncompensatory assessment setting;" + "\n" +
    r"the elementary quantifier fact behind it is standard, and Section 5.2" + "\n" +
    r"states the full novelty qualification.",
    "",
    "s13-novelty-dupe")

# 10. §4.9: presentation-talk lead-in -> remove (table header carries it)
rep(r" The verification levels are kept distinct:" + "\n",
    r"",
    "verification-levels-leadin")

# 11. §4.9 table cell: process term -> precise location
rep(r"Continuum statements & Exact identities and inequalities on the witness datum & Displayed proofs \\",
    r"Continuum statements & Exact identities and inequalities on the witness datum & Appendices A--C \\",
    "table-displayed-proofs")

# 12. header rev
rep(r"% Amin Abaee. Revision v36 (JEDC/elsarticle; Figure 2 re-rendered with a single x-axis label). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Revision v37 (JEDC/elsarticle; removed self-referential meta-commentary). Compiles with tectonic, pdflatex, or xelatex.",
    "header-rev")

out = '/home/user/paper1_assessment_separation_v37.tex'
open(out, 'w', encoding='utf-8').write(src)
print(f"\nWROTE {out} ({len(src)} bytes)")
