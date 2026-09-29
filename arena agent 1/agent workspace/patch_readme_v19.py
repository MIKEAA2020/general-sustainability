#!/usr/bin/env python3
"""lean_README_v18.md -> lean_README_v19.md

v43: the remaining three papers brought in line with the mechanized
layer. Raw strings throughout, so LaTeX backslashes are never
interpreted as Python escapes.
"""
import io, os

SRC = "/home/user/lean_README_v18.md"
DST = "/home/user/lean_README_v19.md"
BS = chr(92)

SECTION = r"""
### Paper-side status (v43) — the remaining three papers

v42 edited the EBC paper. This turn covers the other three the layer
bears on; the four slots in the index are P1, P3, comp and EBC.

| slot | paper | edit |
|---|---|---|
| P1 | `paper1_assessment_separation_v62` | → **v63** |
| comp | `paper2_computational_certification_v18` | → **v19** |
| P3 | `paper2_probabilistic_sufficiency_v12` | → **v13** |

**Two of my own greps were wrong.** An initial scan counted
`Lean=1, formaliz=9` in P1. Both were false positives: `Lean` matched
the word *"c**lean** off-diagonal bands"*, and every `formaliz` hit was
the ordinary mathematical sense (*"the operators formalized in…"*), not
a proof assistant. **All three papers had zero references to the layer.**
This is the same lesson as the `\label`-notation miss in v41: a
substring count is weak evidence.

**P1** carries a *Claim layer / What is established / By what* table —
the same three-way structure built for EBC in v42 — whose rows were
*Continuum → Appendices A–C*, *Finite rational instance → Deterministic
computation*, *Empirical → ---*. The layer was in none of them, yet
`P1_AssessmentSeparation_v5` machine-checks Theorem 5 (1)–(7), Remark 2
with Proposition 3, Theorem 9 (i),(iii) with Proposition 10, Lemma A,
Lemma B, the master-equation reductions and Theorem S2. v63 adds a
**third warrant**, and says what each of the three can and cannot do.

**comp** described three scripts and nothing else, but
`Prelude.farkas_sound` **proves** the Farkas core its primal–dual
witnesses rest on. v19 adds that, with the limits stated: only the
*soundness* direction is proved (the one the certificates use); the
converse rests on a separation theorem the layer does not develop; and
the value identity, bridge theorem and belief-cell proposition remain
**out of reach by construction** — cited, not formalized, because they
need `exp`/`ln` or weak-* compactness.

**P3** did mention formalization — as **future work**: *"…and a
proof-assistant formalization of the closed forms are the natural next
steps"*. That item is **already done**. v13 rewrites the sentence: two
items stay open, the third is recorded complete (support identity on the
repaired reading, freeze count and frozen value, α-vector rationality),
and the one genuinely open formalization item is named — the **Sperner
bound**, for which the layer supplies the machinery to *state* it and no
proof.

**Method.** All replacement strings are raw strings, so LaTeX
backslashes are never eaten by Python — the bug class that silently
turned `\ref` into `\nef` in v42. Post-patch: brace balance 0,
unresolved refs none, for all three files.

**Caveat, repeated:** no `pdflatex` in this environment; none of v63,
v19, v13 has been compiled.

**Still open:** the EBC glance table's 736 stored antichain vs the
abstract's 496 maximal sets; titles, abstracts and supplementary
material across all papers.
""".replace("\\label", BS + "label")  # keep the literal command intact

def main():
    s = io.open(SRC, encoding="utf-8", newline="").read()
    s = s.replace("### v18 — result-level index",
                  "### v19 — result-level index", 1)
    print("ok   title")
    s = s.rstrip("\n") + "\n" + SECTION
    io.open(DST, "w", encoding="utf-8", newline="").write(s)
    t = io.open(DST, encoding="utf-8", newline="").read()
    print("stray CR:", t.count(chr(13)))
    print(f"wrote {DST}: {len(t.splitlines())} lines, {os.path.getsize(DST)} bytes")

if __name__ == "__main__":
    main()
