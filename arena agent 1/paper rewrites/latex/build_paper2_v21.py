#!/usr/bin/env python3
"""Build paper2 v21 from v20: honesty-first micro-revision.
D1 abstract polish (soften 'lacked a comparable instrument'; 'closed-form
elsewhere' -> explicit conditional form; necessary-conditions gloss trimmed).
D2 post-observation-recourse limitation item (Sec 6.5).
Aubin--Catte (2002) + Aubin (2001) related-work bridge (Sec 1.3, Sec 3.1, refs).
Small items, root-cause not shallow:
  - injective-observation consistency check (Sec 2.4; the clean form of the
    batch-7 'singleton sanity' concern, stated as a check not a lemma);
  - named standing solution-existence conditions (Sec 2.1) giving the
    'Marchaud-type' phrase at Theorem 1 an antecedent;
  - observer-transfer citation (Sontag 1998) instead of the uncited
    'standard arguments in the observer-based control literature' gesture.
No theorem, proof, equation, or numbering changes.
"""
import re

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v20.tex"
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

# ---- D1a. abstract: soften the overclaim ----
sub(r"has lacked a comparable instrument.",
    r"has received less systematic treatment.")

# ---- D1b. abstract: 'closed-form elsewhere' -> explicit conditional form ----
sub(r"and closed-form elsewhere.",
    r"and analytic drift-and-timing conditions elsewhere.")

# ---- D1c. abstract: necessary-conditions gloss trimmed (recovers 1 word) ----
sub(r"(equivalently, necessary conditions for observation-based viability)",
    r"(equivalently, necessary conditions for viability)")

# ---- D1d. abstract: recover another word (margin under the 265 limit) ----
sub(r"the observation-based counterpart of the viability kernel",
    r"the observation-based counterpart of the kernel")

# ---- D1e. conclusion: same softening ----
sub(r"the failure side lacked a comparable instrument.",
    r"the failure side has received less systematic treatment.")

# ---- Aubin--Catte bridge: Sec 1.3 ----
sub(r"Cardaliaguet, Quincampoix, and Saint-Pierre (2007). In verification,",
    r"""Cardaliaguet, Quincampoix, and Saint-Pierre (2007). The failure side of
the kernel has a set-valued literature of its own: the complement of
the viability kernel --- Poincar\'e's ``shadow'' --- together with the
capture basins is characterized by Aubin (2001), and the
bilateral-fixed-point and discriminating-kernel calculus of Aubin and
Catt\'e (2002) supplies the algebraic form of the Saint-Pierre and
Cardaliaguet algorithms; the certificates of Section 3 are one-sided,
observation-constrained analogues of that programme. In verification,""")

# ---- Aubin--Catte bridge: Sec 3.1 shadow statement ----
sub(r"The base obstruction operates before any observation-theoretic argument.",
    r"""The base obstruction operates before any observation-theoretic argument: it
certifies membership in the full-information ``shadow'' --- the
complement of the viability kernel (Aubin, 2001; Aubin and
Catt\'e, 2002).""")

# ---- small item: injective-observation consistency check (Sec 2.4) ----
sub(r"the existential projection of a collection \(\mathfrak{B}\) of information states.",
    r"""the existential projection of a collection \(\mathfrak{B}\) of information states. Consistency check: when the observation \(O\) is injective the record determines the state, so the epistemic and robust kernels agree, \(\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V}) = \mathrm{RViab}(\mathcal{V})\), the informational certificates of Sections 3.2--3.4 reduce to the no-merge case, and only the dynamic obstruction of Section 3.1 can certify exclusion --- the definitions degenerate to classical robust viability exactly when observation is perfect.""")

# ---- small item: named standing solution-existence conditions (Sec 2.1) ----
sub(r"to be measurable selections. Let \(\mathcal{V} \subseteq X\) be a closed",
    r"""to be measurable selections --- the standing solution-existence conditions:
every selection pair admits a Carath\'eodory solution, and the
convexified relaxed inclusion of Section 3.1 satisfies the Marchaud
conditions of the viability literature (Aubin, 1991). Let \(\mathcal{V} \subseteq X\) be a closed""")

# ---- small item: observer-transfer citation (Sec 5(c)) ----
block(r"standard arguments in the observer-based\s+control literature\)",
      r"the standard separation argument of observer-based control (Sontag, 1998))")

# ---- D2: post-observation-recourse limitation (Sec 6.5, new item (ii)) ----
block(r"backward recursion is exact \(Section 3\.5\)\.\s*\\item",
      r"""backward recursion is exact (Section 3.5).
\item
  The timing obstruction of Theorem~\ref{thm:delayed} (and its threshold form, Remark~\ref{rem:sigma}) certifies failure by exit \emph{before} the first informative observation. It is blind to the complementary mode of nonviability --- \emph{insufficient post-observation recourse} --- in which a common blind-window control keeps every compatible branch safe, yet no observation-adapted control can recover every branch once the distinguishing observation arrives; the finite-horizon recursion (Section 3.5) captures that mode, but no continuous-time certificate for it is supplied here.
\item""")

# ---- references: Aubin 2001 ----
sub(r"Birkh\"auser, Boston (1991)",
    r"""Birkh\"auser, Boston (1991)

Aubin, J.-P.: Viability kernels and capture basins of sets under differential inclusions. SIAM J. Control Optim. \textbf{40}(3), 853--871 (2001)""")

# ---- references: Aubin--Catte 2002 ----
sub(r"2nd edn. Birkh\"auser, Boston (2011)",
    r"""2nd edn. Birkh\"auser, Boston (2011)

Aubin, J.-P., Catt\'e, F.: Bilateral fixed-points and algebraic properties of viability kernels and capture basins of sets. Set-Valued Anal. \textbf{10}, 379--416 (2002)""")

# ---- references: Sontag 1998 ----
sub(r"\textbf{29}, 187--209 (1994)",
    r"""\textbf{29}, 187--209 (1994)

Sontag, E.D.: Mathematical Control Theory: Deterministic Finite Dimensional Systems, 2nd edn. Springer, New York (1998)""")

# ---- header bump ----
sub(r"% Amin Abaee. Revision v20 (expository: certificate summary table; certainty-equivalence figure; one-step obstruction-tree instance; scan fixes). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Revision v21 (honesty pass: abstract softened; Aubin--Catte/Aubin-2001 bridge; post-observation-recourse limitation; injective-observation consistency check; named standing conditions; observer citation). Compiles with tectonic, pdflatex, or xelatex.")

open("arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v21.tex", "w", encoding="utf-8").write(src)
print("wrote v21,", len(src), "bytes")

# ---- verification ----
for e in ["theorem","proposition","corollary","remark","example","definition","figure","table"]:
    b = len(re.findall(r"\\begin\{"+e+r"\}", src)); en = len(re.findall(r"\\end\{"+e+r"\}", src))
    print(f"  {e:12s} begin={b} end={en} {'OK' if b==en else 'MISMATCH'}")
print("hardcoded numbered refs:", re.findall(r"(?:Theorem|Proposition|Corollary|Remark|Example|Definition) [0-9]", src) or "NONE")
print("'lacked a comparable instrument' residual:", src.count("lacked a comparable instrument"))
print("'closed-form elsewhere' residual:", src.count("closed-form elsewhere"))
print("Aubin & Catté mentions:", src.count("Catt"), "| Aubin 2001 refs:", src.count("853--871"))
print("Sontag mentions:", src.count("Sontag"))
print("recourse item present:", "insufficient post-observation recourse" in src)
print("Marchaud mentions:", src.count("Marchaud"))
m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", src, re.S)
t = re.sub(r"\\(?:emph|textbf|mathrm|mathcal|mathbf|ensuremath)\{[^}]*\}", " ", m.group(1))
t = re.sub(r"\\[a-zA-Z]+", " ", t); t = re.sub(r"[^A-Za-z0-9\-]+", " ", t)
print("abstract words:", len([x for x in t.split() if x]), "(limit 265)")
