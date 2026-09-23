#!/usr/bin/env python3
"""Build paper1_assessment_separation_v33.tex from v32: editorial scan fixes.
Fixes: (1) wrong navigation 'below'; (2) benchmark->witness-datum terminology;
(3) 'displayed proofs of Section 4' -> appendices; (4) §5.2 duplication of §1.3;
(5) §5.1 terminology bridge; (6) hyphenation consistency."""
import sys

src = open('/home/user/paper1_assessment_separation_v32.tex', encoding='utf-8').read()
def rep(old, new, label):
    global src
    n = src.count(old)
    if n != 1:
        print(f"FAIL [{label}]: found {n}, expected 1")
        sys.exit(1)
    src = src.replace(old, new)
    print(f"ok   [{label}]")

# 1. navigation 'below' -> precise wording (orders are above the paragraph)
rep(r"The" + "\n" + r"quantifier orders below make this divergence precise.",
    r"The" + "\n" + r"two quantifier orders make this divergence precise.",
    "nav-below")

# 2. benchmark -> witness datum (terminology consistency)
rep(r"the benchmark assumes separable transition risks",
    r"the witness datum assumes separable transition risks",
    "benchmark-s53")
rep(r"\section{Proofs for the benchmark economy}",
    r"\section{Proofs for the witness datum}",
    "benchmark-appendix")

# 3. proof-location remnants after proofs->appendix move
rep(r"Remark 6, and Theorems 7--8 are established by the displayed proofs.",
    r"Remark 6, and Theorems 7--8 are established by the displayed proofs (Appendices A--C).",
    "proofs-loc-49")
rep(r"the separation results here rest on the displayed proofs of Section 4 and the machine-checked finite instance of Section 4.9",
    r"the separation results here rest on the displayed proofs (Appendices A--C) and the machine-checked finite instance of Section 4.9",
    "proofs-loc-61")

# 4. §5.2 'Proved here' enumeration duplicates §1.3 Contributions; replace with pointer
proved_old = (r"\textbf{Proved here.} (i) The action-set identity \(E_{\mathrm{typ}} = \bigcap_{w \in W_+} E_w\) with the full-cone choice" + "\n"
              r"isolating the separation as purely dynamic (Proposition 3(ii)). (ii) The" + "\n"
              r"general quantifier-separation remark (Remark 1). (iii) The weight-family" + "\n"
              r"monotonicity proposition (Proposition 4). (iv) The explicit exact-tube" + "\n"
              r"witness with a relatively open region of strict separation and the" + "\n"
              r"rescue/impossibility split (Theorem 5). (v) Persistence of the witness" + "\n"
              r"hierarchy under hold-prefix extension (Remark 6). (vi) The explicit" + "\n"
              r"two-stage erasure datum delimiting that persistence (Theorem 7). (vii)" + "\n"
              r"The blend-collapse theorem, under which menu convexification closes the gap exactly at the compensatory region (Theorem" + "\n"
              r"8), while the converse delimitation (Proposition 9) shows that discrete" + "\n"
              r"time-sharing closes it only where both dips are independently subsumed," + "\n"
              r"so the gap survives on the impossibility region.")
proved_new = (r"\textbf{Proved here.} Against this background, the paper proves the results" + "\n"
              r"itemized in Section 1.3; of these, the finite-menu characterization of" + "\n"
              r"Section 4.4 is the general form, of which the witness separation" + "\n"
              r"(Theorem 5) and the blend collapse (Theorem 8) are the instances.")
rep(proved_old, proved_new, "proved-here-dedup")

# 5. §5.1 terminology bridge (typed = coordinate-wise; scalarized = compensatory)
rep(r"operators idealize one aggregation doctrine." + "\n\n" + r"Within this precise scope, Theorem 5 reads as follows.",
    r"operators idealize one aggregation doctrine. The typed operator is the" + "\n"
    r"coordinate-wise criterion --- each floor is required to hold separately ---" + "\n"
    r"and the scalarized family is the compensatory criterion; the two vocabularies" + "\n"
    r"name the same operators, with \emph{typed} denoting the framework object and" + "\n"
    r"\emph{coordinate-wise} its constraint structure." + "\n\n"
    r"Within this precise scope, Theorem 5 reads as follows.",
    "s51-bridge")

# 6. hyphenation consistency
rep(r"exact tube inclusion may be computationally hard",
    r"exact-tube inclusion may be computationally hard",
    "exact-tube-inclusion")
rep(r"which impose separately binding floors.",
    r"which impose separately-binding floors.",
    "abstract-hyphen-1")
rep(r"Practical message: where separately binding floors matter",
    r"Practical message: where separately-binding floors matter",
    "abstract-hyphen-2")

# header rev
rep(r"% Amin Abaee. Revision v32 (JEDC/elsarticle; proofs in appendix). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Revision v33 (JEDC/elsarticle; editorial scan fixes). Compiles with tectonic, pdflatex, or xelatex.",
    "header-rev")

out = '/home/user/paper1_assessment_separation_v33.tex'
open(out, 'w', encoding='utf-8').write(src)
print(f"\nWROTE {out} ({len(src)} bytes)")
