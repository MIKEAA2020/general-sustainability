#!/usr/bin/env python3
"""Build paper2 v19 from v18: alignment + remaining merited audit items.
Fixes: stale 4.3->4.2 heading; broken 1.2 sentence; 1.2 refinements list;
1.4 organization; graphicspath leftover; conclusion staleness.
Merited additions: finite-horizon case in abstract; 'information structures'
keyword; Witsenhausen bridge (CE trap + reference); Farkas infeasibility margin.
Excluded (documented in verdict): full g(B) margins; cost-min design;
distance-to-viability; algorithm box; A-E taxonomy; Pre_blind; supplementary.
"""
import re

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v18.tex"
src = open(SRC, encoding="utf-8").read()

def w(plain):
    rx = re.escape(plain)
    rx = re.sub(r'\\\s+', r'\\s+', rx)
    return rx

def sub(plain, new, expect=1):
    global src
    rx = w(plain)
    found = len(re.findall(rx, src))
    assert found == expect, f"SUB expect={expect} found={found}: {plain[:70]!r}"
    src = re.sub(rx, lambda m: new, src)

def block(rx, new, expect=1):
    global src
    found = len(re.findall(rx, src, re.DOTALL))
    assert found == expect, f"BLOCK expect={expect} found={found}: {rx[:60]!r}"
    src = re.sub(rx, lambda m: new, src, flags=re.DOTALL)

# ---- 1. remove graphicspath leftover (standalone compile) ----
sub(r"\graphicspath{{../}}", "")

# ---- 2. fix broken 1.2 sentence ----
block(r"itself,\s+The calculus is positioned against",
      r"itself. The calculus is positioned against")

# ---- 3. 1.2 refinements list ----
block(r"The calculus is refined in three further directions: a[\s\S]*?\(Theorem~\\ref\{thm:finite-horizon\}\)\.",
r"""The calculus is organized by a single selector principle (Section 2.4):
observation-based viability is the existence of one response ---
admissible, safe, and recursively viable --- for every compatible state,
and each certificate proves that a specific response correspondence is
empty; the obstructions are nested in a ladder
(Proposition~\ref{prop:ladder}). Four refinements complete the picture:
a comparison-function form sharpens the exit-time bound
(Remark~\ref{rem:comparison}); a uniform-margin condition connects the
instantaneous and tube obstructions
(Proposition~\ref{prop:uniform-margin}); the timing obstruction has a
sharp threshold form (Remark~\ref{rem:sigma}); and backward belief
recursion is sound and complete on any finite horizon in finite systems
(Theorem~\ref{thm:finite-horizon}). The epistemic kernel is monotone in
action sets, disturbances, information, and policy class
(Proposition~\ref{prop:monotone}).""")

# ---- 4. 1.4 organization ----
sub(r"Section 3 develops the obstruction calculus (Theorem~\ref{thm:exit}--\ref{thm:finite-horizon}, Propositions~\ref{prop:emptiness} and \ref{prop:uniform-margin}, and Example~\ref{ex:hidden-mode}).",
r"Section 3 develops the obstruction calculus (Theorem~\ref{thm:exit}--\ref{thm:finite-horizon}, Propositions~\ref{prop:emptiness}--\ref{prop:ladder}, Remarks~\ref{rem:comparison}--\ref{rem:sigma}, and Example~\ref{ex:hidden-mode}): the finite-time exit certificate, the admissibility and common-action obstructions, the delayed-information obstruction with its threshold form, the obstruction ladder, and finite-horizon completeness.")
block(r"Section\n6 discusses the position of the calculus relative to barrier\ncertificates and estimation tubes, and draws the governance\nconsequences\.",
r"""Section
6 discusses the position of the calculus relative to barrier
certificates and estimation tubes, states the monotonicity of the
epistemic kernel (Proposition~\ref{prop:monotone}), and draws the governance
consequences.""")

# ---- 5. 4.3 -> 4.2 heading ----
sub(r"4.3 The certainty-equivalence", r"4.2 The certainty-equivalence")

# ---- 6. abstract: finite-horizon as a finitely checkable case ----
sub(r"polyhedral and finite-fibre cases and closed-form elsewhere.",
r"polyhedral, finite-fibre, and finite-horizon cases and closed-form elsewhere.")

# ---- 7. keyword: information structures ----
block(r"output feedback;\s*sustainability governance",
r"""output feedback;
sustainability governance; information structures""")

# ---- 8. CE trap: Witsenhausen bridge ----
block(r"an uncorrected biased\s*indicator empties the kernel that a corrected one preserves\.",
r"""an uncorrected biased
indicator empties the kernel that a corrected one preserves. The
phenomenon is the viability-theoretic analogue of Witsenhausen's
counterexample in stochastic control (Witsenhausen, 1968): the
information pattern --- not the dynamics and not the constraint ---
defeats the restricted controller class.""")

# ---- 9. references: Witsenhausen ----
block(r"305--317 \(1993\)\s*\\section\*\{Declarations\}",
r"""305--317 (1993)

Witsenhausen, H.S.: A counterexample in stochastic optimum control.
SIAM J. Control \textbf{6}(1), 131--147 (1968)

\section*{Declarations}""")

# ---- 10. Farkas example: infeasibility margin ----
sub(r"\(\lambda^{\top}b=-0.1<0\).",
r"""\(\lambda^{\top}b=-0.1<0\). Under the normalization
\(\|\lambda\|_1=1\), the magnitude \(|\lambda^{\top}b|=0.1\) is the
infeasibility margin of the stacked system, shrinking to zero exactly as
the two safe-action sets come to touch.""")

# ---- 11. Conclusion: selector/ladder/finite-horizon sentence ----
sub(r"and the paper claims no complete characterization.",
r"""and the paper claims no complete characterization. The mechanisms
are organized by one selector principle --- observation-based viability
is the existence of a common recursively safe response --- and are
nested in an obstruction ladder (Proposition~\ref{prop:ladder}); in
finite systems backward belief recursion is sound and complete
(Theorem~\ref{thm:finite-horizon}), so the calculus is exact where it
can be and sound elsewhere.""")

# ---- 12. header bump ----
sub(r"% Amin Abaee. Revision v18 (selector-framework unification: framing paragraph; obstruction ladder; sigma* timing threshold; label-selector bridge; monotonicity; measurable-selection scope clause). Compiles with tectonic, pdflatex, or xelatex.",
r"% Amin Abaee. Revision v19 (alignment pass: 4.2 renumber; 1.2/1.4/conclusion sync; graphicspath removed; abstract finite-horizon case; keywords; Witsenhausen bridge; Farkas margin). Compiles with tectonic, pdflatex, or xelatex.")

open("arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v19.tex", "w", encoding="utf-8").write(src)
print("wrote v19,", len(src), "bytes")

# ---- verification ----
for e in ["theorem","proposition","corollary","remark","example","definition","figure"]:
    b = len(re.findall(r"\\begin\{"+e+r"\}", src)); en = len(re.findall(r"\\end\{"+e+r"\}", src))
    print(f"  {e:12s} begin={b} end={en} {'OK' if b==en else 'MISMATCH'}")
print("graphicspath:", "graphicspath" in src)
print("hardcoded numbered refs:", re.findall(r"(?:Theorem|Proposition|Corollary|Remark|Example|Definition) [0-9]", src) or "NONE")
print("section headings:", [s for s in re.findall(r"\\subsubsection\{([^}]*)\}", src) if s.strip()[0].isdigit()][:20])
m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", src, re.S)
t = re.sub(r"\\(?:emph|textbf|mathrm|mathcal|mathbf|ensuremath)\{[^}]*\}", " ", m.group(1))
t = re.sub(r"\\[a-zA-Z]+", " ", t); t = re.sub(r"[^A-Za-z0-9\-]+", " ", t)
print("abstract words:", len([x for x in t.split() if x]))
print("Witsenhausen mentions:", src.count("Witsenhausen"))
