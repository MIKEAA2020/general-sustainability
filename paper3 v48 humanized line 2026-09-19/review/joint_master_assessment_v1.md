# Joint master assessment — the four responses to the composition-calculus prompt

Responses: **A** (`uploads/p3 prompt response.txt` lines 1–1088), **B** (1090–2365), **C** (2366–3060),
and **M** (mine: the v34 statements 34–39, `revision/v7/paper3_material_ledgers_v34.md`). Every verdict
below was re-derived before any editorial decision, by an independent script
(`repo_audits/verify_joint.py`, sympy + scipy, no response code reused); the responses' own scripts were
also executed (`repo_audits/respA.py`, `respB.py`, `respC.py`).

## Adjudication

| task | A | B | C | independent check | verdict |
|---|---|---|---|---|---|
| 1 lift lemma | "injectivity automatic, surjectivity not" | computational conservation test | rank condition via ker D_J | quotient example: parts' conserved rays dim **2**, composition's dim **1**; moiety {a1,a2} destroyed by merging a2 with b2 | **M is wrong as stated.** Replace with: conserved quantities of the composition are the pairs constant on identification classes; the pullback is injective, not surjective; add the 2→1 witness. All three agree with each other and against M — no cancellation risk |
| 2 algebra | three-part cost non-additive (witnesses: independent 3, coupled 0, identification 4 vs inherited budget 1) | associativity/unit/commutativity established conditional on a global interface declaration | same, plus "order of identifications" | A's third witness is the load one: an admissible trajectory attaining service 4 against the summed parts' budget 1 | **M under-scoped.** The additivity of interface costs fails for ≥3 parts; state the two-part case as the theorem and the n-part case as requiring a declared global interface |
| 3 orientation | π is convention-dependent; "π-positive charge 6, charge after physical reversal 0" | covariant convention (outflow-negative) | "forward cost 6.0, reverse cost 0.0" | derivation: V̇ = λ₁ṁ₁+λ₂ṁ₂ ≤ −y − π f, so the worst case over f∈[0,v̄] is **(−π)⁺v̄T**, not π⁺v̄T; "free" is π **≥** 0 | **M has a sign error**, both in the cost term and in the free-interface condition. Fix: convention-free |π|v̄T as the asserted bound, (−π)⁺v̄T as the refinement under the declared outflow-negative convention |
| 4 tightness | "two completions with the same quoted scalar data", exact optimum 3/10 for every L | "the supplied instance is incomplete": completed LP 9.0 vs stated bound 15.0 (and 24.0, gap 15.0); "the asserted L_max" | reduced aggregate LP 0.3, hidden box → 0.1, gap 0.2 (their assert fails only on float equality: 0.19999999999999998 ≠ 0.2) | my LP check: with λ=(2,1) and λ=(1,2) both bounds hold, so the *bound* is safe; the *iff* and the instance's status as "the" value are not | **Re-scope, do not delete:** Prop 37 stays as a sufficient condition for the chosen multiplier pair; add that the joint programme over the fibre product is the value function, and that the printed scalar data do not determine it uniquely. Do not claim the converse |
| 5 completeness | affine-margin incompleteness; Motzkin polynomial as the non-SOS witness | exact LP completeness for the *terminal affine relaxation*; λ-only minimum 100.0 vs exact 1.0; full dual (λ,ρ)=(0,1) | quadratic/SOS tractability boundary | accepted from B's run (its numbers are reproducible here) | **New content worth adding as a remark:** box rows need their own multiplier ρ; with ρ the same instance is sharpened by two orders of magnitude. State as a scope remark, not a theorem, since the article's theorem already says "its infeasibility is no evidence of safety" |
| 6 interval | — | interval theorem (continuity + connected fibre); "disconnected exit-time sets" | corrected hypothesis, polyhedral endpoint programme | my check: image over the polytope is [0, 3.9120] ✓ = [0, log 50]; my attempt to build a gap in a symmetric two-component fibre **failed** (both branches cover the same range) | **M's hypothesis ("monotone along the fibre") is wrong** — τ is a min of monotone functions. Replace by continuity + connectedness for the interval; say only that with a disconnected declared set the two programmes return the endpoints of the *containing* interval. Do **not** assert a disconnected instance (B claims one; I could not reproduce it, and no claim should rest on it) |
| 7 stochastic | "drift brackets do not give deterministic support brackets"; aggregate need not identify the mean | zero-sum Brownian example (σ=1) | hitting-time bracket | — | **Do not implement** the deterministic-bracket version of the §7 extension. The transfer-noise rule is implementable and survives: process noise on a conserved moiety must be zero-sum across pools or an explicit boundary term; a diffusion that creates mass is a type error |
| 8 dual price = substitutability | "capacity dual prices do not characterize substitution"; finite price not sufficient; π≤0 not necessary; proposes a computational replacement predicate | 8.4 exact computational compensation predicate; 8.5 hypergraph and Definition 21 claim | dual prices and substitution, Def 21 marked | my LP: shared cap 1.0/1.5/2.0 → Λ\* 0.5/0.75/1.0 ✓ (matches M); with side 1's own return capacity at 10⁻⁴, Λ\*=0.0001 — the dual price is finite, yet side 1 cannot close at all | **This kills my Tier-1 row 1** (defining weak/strong by the dual price, "compensation along certified substitution morphisms"). The surviving form is the exact *computational* predicate on the joint polytope. A, B and C all converge; M's proposed edit would have been the wrong one — the reason for doing this jointly |

## Decisions (all implemented in v35, md and tex together)

1. Prop 36 first clause: correct to the constant-on-classes characterization, with the 2→1 witness.
2. Def 35 + Prop 37: convention-free |π| cost term; (−π)⁺ refinement; free iff π ≥ 0; re-verify the
   numerical instance under the corrected sign (λ₁=1, λ₂=2, π=−1, B₁+B₂=9, T=30 ⇒ L_max=0.30 — the same
   numbers, now with the multiplier pair that actually generates a cost).
3. Prop 37: sufficiency only; add the joint-programme value function and the non-uniqueness of the
   printed scalar data.
4. New remark: box-aware multipliers ρ sharpen the λ-only search (B's 100.0 → 1.0, reproduced).
5. Prop 39: continuity + connected fibre; containing-interval statement for non-convex declared sets;
   no disconnected-instance claim.
6. New definition: exact compensation predicate on the joint polytope, plus the verified negative result
   that finiteness of a capacity dual price does not characterize substitutability.
7. One sentence of transfer-noise discipline in §7.1; no deterministic hitting-time bracket claim.
8. n-part additivity stated as two-part-only, with A's identification witness as the reason a global
   interface declaration is required.
9. Carried from the previous turn, still unshipped and now included: the closure capacity re-lettered
   Λ\* (it collided with the certificate multiplier λ — the notation defect the repo's paper-3 audit
   catalogues); Definition 23's invented "readout matrix C" removed (the article's readout is
   Q(θ)v, §5.1) with the residual bound written on ℓᵀd_x directly; and Remark 33's registered absence
   discharged with the premium computed from `batch 7/source_audits/Country_Trends.csv`
   (2022: τ_agg = 213 d, τ_min = 0 d from the zero-biocapacity carbon component, Π_τ = 213 d; on the
   five positive-biocapacity components 538 vs 365 ⇒ 173 d; series 547/346/251/173 for 1961/1980/2000/2022).

## Rejected, with reasons

- Any edit that *narrows* the aggregation or reserve-life claims in response to task 4/5: those claims are
  the author's and already conditional; the responses' objections are about my composition statements, not
  theirs.
- B's "alarm/certificate asymmetry" restatement and the superlevel-set representation of Prop 29 — already
  present in the article (alarm clause in §10.1; Prop 29 is the uniqueness form); implementing B's variant
  would duplicate, not improve.
- The three-part "many-sided residual" as a theorem: A supplies witnesses for failure of additivity but no
  general statement; recorded as an open item for the supplementary, not as a claim.
- C's `assert reduced_value == 0.3 and hidden_gap == 0.2` fails on float equality in their own script; their
  numbers are right, their exactness claim is not — so I quote the values and not the "exact" language.
- Every tier-3 project item from `review/remaining_points_v3_deep_mine.md` (compiler, pilots, retro-audit,
  dashboards) stays out of the article.

## Implementation record (v35, same day)

`revision/v7/build_v35_kernel.py` applied **22 logged edits** to `paper3_material_ledgers_v35.{md,tex}`,
built from v34 as input (v34 untouched). Decisions 1-9 of the table above all shipped, plus the four
register items whose statements needed no new numerics: Definitions 41 (control margin), 42 (affinity,
the fourth admissibility predicate), 43 (circulation time), 44 (governability ratio $G_{\mathcal K,m}
= T_{\mathcal K,m}/(\tau+h)$, with the 3.7 yr / 6.5 yr figures attributed to the companion's own
certified thresholds rather than to the class), Proposition 40 (corridor emptiness with its Farkas
witness and the support-of-y reading that names the conflicting floors), Lemma 4 (baseline covariance
$\operatorname{Var}(Y-B)=\operatorname{Var}Y+\operatorname{Var}B-2\operatorname{Cov}(Y,B)$), and
Remark 33's premium figures computed from `repo_audits/Country_Trends.csv` with the carbon convention
declared rather than chosen.

Two defects inherited from the md->tex port were fixed in the same build, both pre-existing in the shipped
v33/v34 `.tex`:
1. `revisions_v33_tex.py` escaped underscores inside display math (`B\_1`), and `\_` in TeX math mode is a
   *visible underscore*, not a subscript: the shipped v34 PDF renders literal underscores in its display
   equations (extracted text: 11 underscore-in-math sequences; v35: 2, both the e-mail address). v35's
   builder now writes display math verbatim and strips the stale escaping (9 occurrences in regions v35
   did not otherwise rewrite).
2. The v34 `.tex` contains `\Oksendal` in the 7.1 lineage sentence — an undefined control sequence, since
   an uppercase `\O` is a command and not an accent taking an argument. `tectonic paper3_material_ledgers_v34.tex`
   now halts on it; v35 uses `\O{}ksendal` (which is already how the other two occurrences are written) and
   compiles. The v34 `.pdf` on disk was built before that string entered the tex, so the shipped v34 PDF is
   fine; the v34 *source* is not.

## Verification actually run

`python3 revision/v7/verify_v35_build.py` -> **ALL CHECKS PASS**: the 22 logged edits reverse v35 -> v34
byte-exactly modulo whitespace and the deliberate display-underscore change, in *both* formats (md 184,876
vs 184,876 chars; tex 201,002 vs 201,002); 54 statement labels, md set identical to tex set, no repeats;
maxima Definition 44 / Proposition 40 / Theorem 24 / Remark 34 / Lemma 4 / Corollary 19; numbering note
reads 1-44 and lists the added labels in both formats; tex pure ASCII, zero dollar signs; 23 content probes
present in both formats; PDF 51 pages (v34: 48), subscripts rendering, no literal underscores in math.
`tectonic paper3_material_ledgers_v35.tex` exits clean with only overfull/underfull-hbox warnings.
Independent adjudication numbers: `repo_audits/verify_joint.py` (sympy + scipy) reproduces the Prop 36
nullity drop 2 -> 1, the `(-pi)^+` worst case, the interval image [0, log 50], Lambda* = 0.5/0.75/1.0 and
the 1e-4 counterexample that kills the dual-price characterization.

## Register items still open (deliberately not shipped in v35)

| item | why it waits |
|---|---|
| yield inflation as latent-variable non-identifiability | half-shipped: Def 43's closing sentence and §6.6's existing projection sentence carry the content; the full "non-injective readout, section choice" statement needs the §5.1 readout declaration to be quoted, not paraphrased |
| non-displacement / additionality gate as a deficit-monotonicity predicate | needs Definition 22's deficit functional re-read before it can be written as a predicate on the composed ledger |
| supportable-output envelope | needs a numeric anchor or it becomes an untested definition; the anchor is the author's data choice |
| LSIT as statement only | the acronym's definition must be taken from `uploads/p3 profound upgrades.txt` ~line 387 and matched to the article's vocabulary first; its staged numerics stay excluded either way |
| mechanism-design umbrella proposition | its "declared elasticity" clause depends on the reporting protocol of §10, which the D4 wording item also touches — do them together |
| superlevel-set alternate proof of Prop 29 | proof-only, belongs in the supplementary, not the article |
| per-parameter identifiability status field | a table column in the declaration protocol; pairs with MDV's supplementary table — one batch in the supplementary is cleaner than two in the article |
