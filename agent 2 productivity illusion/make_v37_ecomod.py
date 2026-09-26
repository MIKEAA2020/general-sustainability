#!/usr/bin/env python3
"""make_v37_ecomod.py — ECOMOD v36 -> v37 editorial alignment round.

Executes the Task-117 audit flags + cross-strengthening anchors as anchored,
exact-match operations (family discipline: every op asserted to occur exactly
once; the builder fails loudly rather than guessing).

Ops:
  E1  header author line + v37 provenance note
  E2  author block: Tehran affiliation (superscript, P4-v41 / JIE-v3 style)
  E3  date bump
  E4  elevator image attributed (ledger study's image)
  E5  line-71 productivity-illusion gloss made precise (P3's actual definition)
  E6  mobilising/protective taxonomy inline cite (2026a)
  E7  exact-tube semantics attributed (2026b vocabulary)
  E8  strong-sustainability doctrine sentence quotation-marked (exact quote,
      'either' restored) + the two sub-threshold phrasings paraphrased
  E9  weak-sustainability index anchored to Lemma A (2026b)
  E10 mask claim anchored to Theorem S2(ii) (2026b)

No mathematical content is touched; bibliography unchanged (2026a/b/c already
present and DOI-resolved).
"""
import sys, difflib

SRC = "manuscript_ECOMOD_v36.tex"
DST = "manuscript_ECOMOD_v37.tex"

OPS = [
# E1 — header author line + provenance
("E1a header author",
r"""% Author: Amin Abaee (Independent Researcher)
% Compiled with LuaLaTeX (fontspec + unicode-math).""",
r"""% Author: Amin Abaee (Independent Researcher, Tehran, Iran)
% Compiled with LuaLaTeX (fontspec + unicode-math).
% v37 (2026-09-26): editorial alignment round per the family audit --- doctrine
% borrowing quotation-marked and attributed; elevator image attributed; the
% productivity-illusion gloss made precise; the mobilising/protective taxonomy
% and exact-tube vocabulary given inline citations; the weak-sustainability
% index and structural mask claims anchored to Lemma A and Theorem S2(ii) of
% the assessment companion; Tehran affiliation added. No mathematical change."""),
# E2 — author block affiliation
("E2 author block",
r"""\author{
  \textbf{Amin Abaee}\\
  \textit{Independent Researcher}\\
  \href{mailto:amin_abaee@ut.ac.ir}{amin\_abaee@ut.ac.ir}\\
  \href{https://orcid.org/0000-0002-0019-1842}{ORCID: 0000-0002-0019-1842}
}""",
r"""\author{
  \textbf{Amin Abaee}\textsuperscript{1}\\
  \textsuperscript{1}\,\textit{Independent Researcher, Tehran, Iran}\\
  \href{mailto:amin_abaee@ut.ac.ir}{amin\_abaee@ut.ac.ir}\\
  \href{https://orcid.org/0000-0002-0019-1842}{ORCID: 0000-0002-0019-1842}
}"""),
# E3 — date
("E3 date",
r"\date{September 7, 2026}",
r"\date{September 26, 2026}"),
# E4 — elevator image attribution
("E4 elevator attribution",
r"""The orchard has an everyday analogue. A system can bear overload for a while""",
r"""The orchard has an everyday analogue, in the ledger study's own image (Abaee, 2026c): a system can bear overload for a while"""),
# E5 — productivity-illusion gloss precision
("E5 gloss precision",
r"""the aggregate rises \emph{not} merely because technology outpaces degradation (the productivity illusion as Abaee, 2026c, defines it), but because the two books are re-weighted""",
r"""the aggregate rises \emph{not} merely because technology outpaces degradation (one channel of the productivity illusion of Abaee, 2026c: the appearance of adequate delivery while the base that sustains it is being reduced), but because the two books are re-weighted"""),
# E6 — taxonomy cite
("E6 taxonomy cite",
r"""\item \textbf{The stabilising institutional signature is the protective one.} Freeze-conversion protects the capital book;""",
r"""\item \textbf{The stabilising institutional signature is the protective one} (the mobilising/protective taxonomy of the delay companion, Abaee, 2026a). Freeze-conversion protects the capital book;"""),
# E7 — exact-tube attribution
("E7 exact-tube attribution",
r"""(b) Under \emph{exact-tube} semantics (a transition is safe only if every state along it, not merely the endpoint, satisfies the constraints), the intermediate passage""",
r"""(b) Under \emph{exact-tube} semantics (in the assessment companion's vocabulary, Abaee, 2026b: a transition is safe only if every state along it, not merely the endpoint, satisfies the constraints), the intermediate passage"""),
# E8a — doctrine sentence quotation-marked (exact quote, 'either' restored)
("E8a doctrine quotation",
r"""Strong sustainability is the regime in which that closure fails --- because no identified physical pathway re-routes the extracted matter, or because depletion outruns the rate at which such a pathway could be deployed --- so a separately-binding floor on a critical stock binds.""",
r"""Strong sustainability, in the ledger study's words, is ``the regime in which that closure fails --- either because no identified physical pathway re-routes the extracted matter, or because depletion outruns the rate at which such a pathway could be deployed'' (Abaee, 2026c), so a separately-binding floor on a critical stock binds."""),
# E8b — sub-threshold phrasings paraphrased
("E8b waste phrasing",
r"""the by-products of use are returned to use in time and are therefore not waste (waste is a relational status, not an intrinsic property of any material);""",
r"""the by-products of use come back into service soon enough not to count as waste (in that reading, waste is relational --- a status of the use it enters, not an intrinsic property of the material);"""),
# E9 — Lemma A anchor
("E9 Lemma A anchor",
r"""The weighted composite $B$ is the weak-sustainability index: it satisfies its aggregate floor while the \emph{typed} floor on ecological capital $A_c$ is violated.""",
r"""The weighted composite $B$ is the weak-sustainability index --- the linear, perfectly-substitutable member of the assessment companion's aggregator family, its attained weak extreme (Lemma A of Abaee, 2026b): it satisfies its aggregate floor while the \emph{typed} floor on ecological capital $A_c$ is violated."""),
# E10 — Theorem S2(ii) anchor
("E10 S2(ii) anchor",
r"""(a) The mask is a structural failure of any aggregate that compensates a falling capital book with a rising yield, not an accident of one parameter set.""",
r"""(a) The mask is a structural failure of any aggregate that compensates a falling capital book with a rising yield, not an accident of one parameter set: in the assessment companion's family no positive-elasticity aggregator is uniformly safe, and the only uniformly safe aggregator is the typed, non-compensating one (Theorem S2(ii) of Abaee, 2026b)."""),
]

def main():
    src = open(SRC, encoding="utf-8").read()
    out = src
    applied = []
    for name, old, new in OPS:
        n = out.count(old)
        if n != 1:
            print(f"FATAL: op {name!r} matched {n} times (need exactly 1)")
            sys.exit(1)
        out = out.replace(old, new)
        applied.append(name)
    # sanity: no v36 date residue, provenance present, no math env touched
    assert "September 7, 2026" not in out, "old date residue"
    assert out.count("Abaee, 2026b") >= src.count("Abaee, 2026b"), "2026b cites must not decrease"
    assert out.count("Abaee, 2026a") >= src.count("Abaee, 2026a"), "2026a cites must not decrease"
    # equation environments unchanged
    import re
    def mathenvs(t):
        return re.findall(r"\\begin\{(equation|align|gather|eqnarray)\*?\}.*?\\end\{\1\*?\}", t, re.S)
    assert mathenvs(out) == mathenvs(src), "math environments changed"
    open(DST, "w", encoding="utf-8").write(out)
    print(f"OK: {len(applied)} ops applied -> {DST}")
    for a in applied:
        print("  -", a)
    # unified summary of changed lines
    diff = list(difflib.unified_diff(src.splitlines(), out.splitlines(), lineterm=""))
    changed = [l for l in diff if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
    print(f"changed lines: +{sum(1 for l in changed if l.startswith('+'))} / -{sum(1 for l in changed if l.startswith('-'))}")

if __name__ == "__main__":
    main()
