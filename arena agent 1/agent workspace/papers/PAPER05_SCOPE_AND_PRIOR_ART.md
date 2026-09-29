# Paper 5 — scope decision resolved, prior art added, 2026-09-29

## 1. `ebc` identification — CONFIRMED, upgraded moderate → high

Sixteen Lean modules named `EBC_*` exist in `lean/Formalizations/`, in namespace
`Formalizations.EBC`, carrying **134 theorem/lemma declarations with zero `sorry`/`admit`**:

| module | thm/lem | maps to paper 5 section |
|---|---|---|
| EBC_Hamming | 6 | § The pairwise-Hamming classification (`lem:pairsum`, `cor:hamming`) |
| EBC_Bands | 5 | the exact bands (`prop:bands`) |
| EBC_Ladder (+v2) | 12 | § The observation ladder doubles (`prop:ladder`) |
| EBC_ExactBelief (v1–v3) | 23 | § Exact point-based evaluation (`prop:pbvi`) |
| EBC_Deadline | 17 | § A deadline instance (`prop:deadline`) |
| EBC_Pairs (v1–v3) | 23 | pairwise structure |
| EBC_Dynamics | 26 | supporting dynamics |
| EBC_Classification (v1–v3) | 18 | classification |

`EBC` = **E**xact **B**elief **C**omputation. The module names map onto this paper's own
section labels. Manifest updated.

## 2. Scope decision — EXPAND, DO NOT FOLD INTO PAPER 3

Decided on evidence, not taste:

- **Paper 3 cites paper 5** as "the exact-computation companion" in both its body text and
  its bibliography. Folding would make paper 3 cite itself.
- Folding would join two different mathematical cores — paper 3's continuous-to-finite
  bridge versus paper 5's exact enumeration at scale — which is the failure the manifest
  itself names: "two mathematical cores in one paper is the signature of two papers."
- It would bury paper 5's own 16-module formalization.
- LENGTH IS NOT A CONSTRAINT (preprints.org), so thinness is a reason to develop, not merge.
- The standing constraint that none of the eight venue-assigned papers may be silently
  dropped by a reorganisation also rules folding out.

## 3. The orphaned "Scale II" — RESOLVED

Paper 5 is titled "at Scale II" and calls itself "a computational companion to the
belief-state safety-value theory", but no "Scale I" appeared among the eleven. Located:
`arena agent 1/paper rewrites/latex/paper2_belief_state_v2.tex`, titled *"Belief-State
Safety Values for Viability under Incomplete Observation"* (4,217 words).

That is **paper 2 of this set in its earlier form**: 32.6% of its sentences appear verbatim
in `paper02_probabilistic_sufficiency_v11.tex` (12,753 words), and both develop `V_k(b)`
and the support identity. So the companion relation is intact and points inward at paper 2.
Now stated explicitly in paper 5's text.

## 4. Papers 2 and 5 are NOT duplicates

Sentence-level overlap is **4.3%** (5 of 117 sentences), and all five are boilerplate
(cross-cite comments, AI declaration, author statement, one bibliography line). They are
complementary: paper 2 uses the antichain structure *theoretically* (α-vectors as the
indicators of maximal jointly survivable subsets — an antichain, Sperner-bounded,
`prop:antichain`), while paper 5 performs the *computational census* at scale.

## 5. Prior art added (§ priorart)

Concedes, in as many words:
- **Sperner (1927)**, **Dedekind's problem**, **Kleitman's** asymptotic antichain count —
  classical; Stanley and Engel are the standard treatments.
- **Hamming adjacency** — classical coding theory.
- **"This paper proves no new theorem about antichains."** The census (1,048,576 → 496) is
  an output of a computation on one instance; the classical results are the scaffold.
- **PBVI** (Pineau, Gordon & Thrun 2003; Shani, Pineau & Kaplow 2013) — the distinction is
  exact rational arithmetic, not the idea of a point set.
- **Qualitative objectives** (Chatterjee, Doyen & Henzinger 2009) — positioned in paper 2;
  paper 5 adds nothing.

Claim narrowed to four items: complete exact classification of the cube instance; the cost
figures for exactness at this size; the pairwise-Hamming restrictions *as applied here*;
and the machine-checked layer.

## 6. Mechanized verification added (§ mech)

16 EBC modules, 134 declarations, project builds 60/60 under Lean 4.14.0, no `sorryAx`,
no `sorry`/`admit`/`axiom` anywhere in the layer.

**Honest scope note included**: what is machine-checked is the discrete combinatorial core
— the structure the enumeration walks. The enumeration itself, including the census, is
performed by the deposited scripts and is **not** formalized.

## 7. Bibliography

Seven works added. Chatterjee/Doyen/Henzinger copied verbatim from paper 2's bibliography
so it is consistent across the set. Four flagged in the `.tex` as needing publisher
verification (pagination/venue not confirmed): Sperner 1927, Kleitman 1969, Pineau et al.
2003, Shani et al. 2013.

## Result

paper05_exact_belief_computation_v12.tex: 4,241 → 5,474 words.

## Residual risk

Paper 5 remains the thinnest of the eleven. It is honest about being a companion, its claim
is narrowed to four items, and it carries a 134-declaration formalization. But a companion
paper whose combinatorics is classical and whose scale is a four-parameter cube may not
clear the bar on novelty no matter how carefully framed. **The strongest available move, not
taken here, would be to extend the census to a larger instance** (five or six parameters),
where the cost figures would say something new about the feasibility frontier of exact
computation. That is a research task, not an editing one, and it is the right next step if
paper 5 is to clear the bar.
