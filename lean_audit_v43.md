# Lean audit — v43

Branch `lean-audit-v4`. Range: `c41bdd1` → (this push).

Build unchanged: **rc = 0, 60 jobs** (54 imported modules), zero
warnings, zero `sorry`, zero axioms.

---

## 1. The remaining papers

v42 covered the EBC paper. This turn covers the other three papers the
mechanized layer bears on — the four slots in the index are P1, P3,
comp and EBC.

| slot | paper | edited |
|---|---|---|
| P1 | `paper1_assessment_separation_v62` | → **v63** |
| comp | `paper2_computational_certification_v18` | → **v19** |
| P3 | `paper2_probabilistic_sufficiency_v12` | → **v13** |

## 2. Two of my own greps were wrong, and how

An initial scan counted `Lean=1, formaliz=9` in P1 and concluded it
"does mention the layer". Both were false positives:

* `Lean` matched the word **"c*lean* off-diagonal bands"** (case-
  insensitive substring match);
* all nine `formaliz` hits were the ordinary mathematical sense —
  *"the operators formalized in…"*, *"The masking formalized here…"* —
  not references to a proof assistant.

Corrected: **P1, comp and P3 all had zero references to the
mechanized layer.** (P3 had one genuine mention, addressed in §4.)

This is the same lesson as the `mathcal{W}^{\mathrm{fb}}` miss in v41:
a substring count is weak evidence, and a negative result on a
pattern one has not checked is weaker still.

## 3. What each paper was missing

**P1 (§Machine verification).** The paper carries a *Claim layer /
What is established / By what* table — the same three-way attribution
structure built for the EBC paper in v42. Its rows were:

| claim layer | by what |
|---|---|
| Continuum statements | Appendices A–C |
| Finite rational instance | Deterministic computation |
| Empirical claims | --- |

The mechanized layer was absent from all three rows. But `P1_AssessmentSeparation_v5`
machine-checks Theorem 5 (1)–(7), Remark 2 with Proposition 3,
Theorem 9 (i),(iii) with Proposition 10, Lemma A (handshake identity
and engine equivalence), Lemma B, the master-equation reductions and
Theorem S2. **v63 adds a third warrant** alongside the appendices and
the grid, and says plainly what each of the three can and cannot do.

**comp (§Verification methods).** Described three scripts and one
package — 51 exact checks, a campaign script, a library self-test, a
master entry point — and nothing else. But `Prelude.farkas_sound`
**proves** the Farkas core on which its exact primal–dual witnesses
rest. **v19 adds a mechanized-layer paragraph**, and states the
limits honestly: only the *soundness* direction is proved (the one the
certificates use); the converse rests on a separation theorem the layer
does not develop; and the value identity, bridge theorem and belief-cell
proposition remain **out of reach by construction**, cited rather than
formalized, because they need `exp`/`ln` or weak-\* compactness.

## 4. P3: a factual staleness, not a gap

P3 did mention formalization — but as **future work**:

> *"…the probe-count asymptotics of the repetition trade-off, the
> general learning-deadline law for additively entering hidden
> parameters, and a proof-assistant formalization of the closed forms
> are the natural next steps"*

The third item is **already done**. v13 rewrites the sentence: two
items remain open, and the third is recorded as complete — support
identity (on the repaired reading of `thm:support`), freeze count and
frozen value, and the rationality of the α-vectors, machine-checked.

It also records the one genuinely open formalization item: the **Sperner
bound** of `prop:antichain` (iii), for which the layer supplies the
binomial machinery needed to *state* it but no proof — cited, not
formalized, by decision.

## 5. Method note

All replacement strings in `patch_papers_remaining.py` are **raw
strings**, so LaTeX backslashes are never interpreted as Python
escapes — the bug class that corrupted `lean_README_v18.md` in v42,
where `\ref` was silently written as `\nef`.

Post-patch integrity for all three files: **brace balance 0**,
**unresolved refs none**.

**Caveat, repeated from v42:** there is no `pdflatex` in this
environment. None of v63, v19 or v13 has been compiled; verification is
by reference resolution, brace balance and inspection.

## 6. Still open

* The glance table's **736** stored antichain vs the abstract's **496**
  maximal sets (EBC) — possibly different measures, not verified.
* Titles and abstracts have not been reviewed against the findings.
* Supplementary material not reviewed.
