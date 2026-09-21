# Paper-1 v53 — Final-Version Flaw Review (Owner Directive 3) and the σ-Abstract Visibility Ruling (Directive 2)

Task 108 (continued) / batch 8 / paper 1. Owner directives this round: (3) read the
final version of paper1 assessment_seperation for possible flaws; (2) σ-visibility in
the abstract only if merited. The final version is
`arena agent 1/paper rewrites/latex/paper1_assessment_separation_v53.tex` (2,426
lines; the Task-107 deliverable, commit `6ac41b5`, now pushed). Standing rules
honored: v53 was read, not modified; every finding below is recorded for a future
owner-gated v54 — no existing file was touched, no content removed or condensed.

---

## 1. Mandate and method

Full line-by-line read of v53 (all 2,426 lines), with:

- hand re-derivation of every displayed arithmetic constant (the licensing
  thresholds, the blend window, the S2(ii) witnesses, the §6.3 anchoring
  numbers, Theorem 8's erasure datum);
- cross-checks of every witness-level statement against the two independent
  machine waves (the σ-wave's 57 checks and this round's middle-regime wave,
  77 checks — both passing);
- consistency checks of cross-references (rendered §/Table numbers taken from
  the v53 PDF: §4.5 witness datum, §5.4 scope delimitations, Table 5, §5.7
  rescue, §5.8 spectrum, §6.3 benchmark), the abbreviation list, the
  reference list (completeness + alphabetization), and the figure files.

## 2. Verified clean (the inventory)

1. **Theorem 5, all seven parts** — statements, the Appendix-B proof (including
   its boundary handling at s2 = 0, w1 = 0, r → ∞), and the region dictionary
   (Table 4/tab:regions): verified against the middle-regime wave's Part-0
   handshake (checks 0.7–0.11, independent implementation, 676 grid states).
   The ρ1 = 2/3 / ρ2 = 3/2 arithmetic at the canonical datum re-derived by
   hand: (2 − 6/5)/(6/5) = 2/3 ✓, (6/5)/(2 − 6/5) = 3/2 ✓; ρ2 ≥ ρ1 ⟺ sum ≥ 2
   algebra ✓ (line 2063).
2. **Theorem 6 (finite-menu)** — the separation argument (closed convex set
   conv(D) + R^n_+, w ≥ 0 forced by v ranging over the cone, min over conv =
   min over vertices): correct; the witness instantiation D = {(2,0),(0,2)}
   ✓.
3. **Theorem 8 (erasure datum)** — z* = (2/5, 2/5), A1 threshold 3/7 and A2
   threshold 7/3 re-derived by hand: (1−2/5)/(2/5+1) = 3/7 ✓, (2/5+1)/(1−2/5)
   = 7/3 ✓, coverage 3/7 < 7/3 ✓; the boundary weights covered directly ✓.
4. **Theorem 9 (blend collapse)** — window [1 − s2/2, s1/2], nonempty iff
   sum ≥ 2, singleton at equality, the [0,1]-clip inactivity on Q
   (0 < 1 − s2/2 ≤ s1/2 < 1 on Q: verified), and the Appendix-B proof ✓;
   at the canonical datum [2/5, 3/5] ✓ — independently confirmed by the
   middle-regime wave's checks 2.2/2.3.
5. **Proposition 11 (rescue threshold)** — the formula
   κ*(z) = (1−x)·1[z ∉ V_typ] and its Appendix-C proof ✓. (The middle-regime
   wave's Theorem M2 now extends it class-conditionally — a v54 addition, not
   a correction: under the common-shock class κ* gains an ∞ regime.)
6. **§5.8 (the σ-spectrum, the labelled extension)** — the family table, Lemma
   A's handshake, Lemma B's collapse convention, the master equation, the
   ladder (1 < 5/4 < √2 < φ < √3 < … → 2), the σ* landscape, Theorems S1/S2
   with proofs, the LPI identification with both caveats, the relevance
   chain: all match the σ-wave record (57/57 machine checks). The S2(ii)
   witnesses hand-verified numerically: σ=3 at s=6/5 (sum ≈ 2.03 ≥ 2) ✓;
   σ=2 at s=13/10 (≈ 2.065) ✓; σ=1 at s=3/2 (2.25) ✓; σ=1/2 at s=13/8
   (8/5 + 8/21 ≈ 1.981 ≤ 2) ✓; σ=1/4 at s=9/5 (125/64 + 125/2744 ≈ 1.9987 ≤ 2)
   ✓ — the last remarkably tight but exact. The LPI report flip
   √(11/25) < 1 ⟺ 11 < 25 ✓. The 57-check count and the non-pooling policy
   correctly stated ✓.
7. **§6.3 (the benchmark)** — the Schaefer instantiation (σ(16/5) = 1088/125,
   σ(6/5) = 528/125, MSY = rK/4 = 10 kt/yr, the 69/20 staged rebuild, the
   dashboard tube (12/5, 2/5, 12/5)) and the DFO anchoring: 1.6 × 884.6 ≈
   1,415 kt ≈ 1.42 Mt ✓; 0.6 × 884.6 ≈ 531 kt ✓; 33.8% × 884.6 ≈ 299 kt ✓;
   decline ≈ 1.1 Mt ≈ 1.3 LRP units ✓; the unit convention explicit ✓.
8. **Mechanical layers** — all four figure files referenced exist in figs_p1/;
   the abbreviation list (CES, MSY, PROMETHEE) — each used in the body
   (CES ×12, MSY ×2, PROMETHEE ×3) ✓; the reference list complete for every
   in-text citation (Filippov, Warga, Becker, Nardo, Fischer, Doyen et al.
   2012, Gao, De Lara & Doyen, DFO, Lade, Raworth, O'Neill, Fanning all
   present) with the Abaee block alphabetized ✓; the §4.9 proof list complete
   (Prop 3, Prop 4, Thm 5, Thm 6, Remark 7, Thms 8–9, Prop 10 → App A–C;
   Prop 11 → App C) ✓; the Fig-1 caption's x-independence sentence ✓; the
   σ-notation disambiguation clause (§5.8 opening) ✓; the typed-endpoint
   operator paragraph (§3.1) consistent with §5.6's fourth implication ✓.

**No mathematical error was found.** The findings below are typographic
(F1), precision-gloss (F2), pre-registered substantive refinements (F3),
presentational (F4–F5), and the ruling (§4).

## 3. Findings (all deferred to a future owner-gated v54; v53 untouched)

**F1 (typographic; 5 instances).** Missing space after the proof pointer:
"See Appendix A.The separation…" (line 465), "…A.At a fixed…" (473),
"…A.Part (i)…" (487), "…A.Proposition 4…" (499), "…A.On the witness…" (536).
The rendered PDF reads "Appendix A.The" — a missing inter-sentence space after
the period. v54 fix: insert a space or `\ ` after "Appendix A." at the five
sites. Severity: cosmetic; zero mathematical content.

**F2 (precision gloss; 1 instance).** Proposition 10's parenthetical gloss of
the impossibility region (line 927): "on the impossibility region I (where
s1 < 2, s2 < 2, s1 + s2 > 2)" — I is defined (lines 629–635) with
s1 + s2 ≥ 2; the strict gloss excludes the sum = 2 face of I, which is part
of I and part of FP_agg (at sum = 2: weak-accept by Theorem 5(2), typed-reject
by 5(1)). The proposition's assertion itself ("iff s1 ≥ 2 and s2 ≥ 2") is
unaffected. v54 fix: "s1 + s2 ≥ 2" in the gloss.

**F3 (substantive precision; pre-registered — confirmed by this review as a
finding, and now exactly computed).** The §5.4 scope-delimitation item and
Table 5's row (iii) assert, for the coupled all-floor regime: "the principal
actions fail together and the compensatory/noncompensatory divergence
collapses into universal rejection." The middle-regime wave (this round,
`batch 8/middle_regime_wave/`, 77/77 checks) establishes the exact statement:
(i) under the **additive** reading, "universal rejection" is exact **on I at
the datum's full magnitude** (check 3.5) but depth-dependent — the exact
boundary is δ = 5/4 (check 3.7; at heatwave magnitude δ = 1/2, deep-I states
such as (1/2, 19/10, 19/10) survive as gap states, check 3.6) — and the gap
**relocates rather than vanishes** at full magnitude (the coupled(2) gap
{x < 1, 2 ≤ s_i < 7/2, sum ≥ 11/2} is nonempty; (1/2, 3, 3), check 3.8);
(ii) under the **replace** reading, "fail together" is exact (FAST and SLOW
share the weight-independent requirement A(p) ≥ 2, check 3.11) but the
collapse is of the **typed/weak distinction** (V_weak = V_typ, Theorem CT,
checks 3.12–3.13), with acceptance surviving at {s_i ≥ 2} ∪ {x ≥ 1,
s_i ≥ 15/8} — not universal rejection. Read on I both readings support the
sentence; read globally (as the table cell invites) it overstates in two
exact senses. v54 fix (wave record §8 item 4): the reading-conditional
refinement with the 5/4 boundary, the relocation witness, and Theorem CT;
the same round fills Table 5's middle cell (item 1) and adds the κ*
trichotomy (item 2) and the blend-fragility caveat (item 3).

**F4 (presentational harmonization; optional).** §6.3 states the 2015
assessed stock twice: "about a third of the LRP (≈ 295 kt)" (line 1878) and
"33.8% of that LRP … ≈ 299 kt" (line 1889). Both are correct under their
framings (a third = 294.9; 33.8% = 299.0), and the two sentences serve
different purposes (gloss vs. precise statement), but a reader comparing them
sees two numbers for one datum. v54 option: harmonize to one framing
(≈ 299 kt = 33.8%, "about a third") at both sites.

**F5 (modeling-stipulation transparency; 1 clause; not an error).**
Proposition 10 evaluates the class defined by the explicit stipulation "the
set of visited states is the union of the two primitive worst-case tubes"
(line 924–925) — the adversarial full-dip reading of plan-granular
alternation, under which the result is airtight. A literal rate-preserving
fine-grained alternation visits sub-ranges (its visited set is contained in
the stipulated one), so the possibility that some non-worst-case literal
schedule escapes the impossibility on I lies outside the proposition's class
as stated. The paper's own terminological paragraph (lines 944–954) states
the stipulated model honestly. v54 option: one clause noting that the
stipulated visited set is the pointwise worst case over alternation
schedules, scoping the impossibility to the worst-case alternation.

## 4. The σ-abstract visibility ruling (directive 2) — **DECLINED, on merits**

Question: should the abstract gain a sentence (and/or the highlights a sixth
item) advertising the §5.8 substitutability-spectrum labelled extension?

**Merits for** (weighed): the extension is a listed contribution ((xi),
§1.3); the LPI identification is the paper's most venue-aligned single
result (Ecological Indicators); the abstract's final paragraph already
advertises two smaller contributions (the benchmark (ix) and the terminology
guide (x)), creating a coverage asymmetry.

**Merits against** (decisive):
1. **The abstract advertises closed results; §5.8 is explicitly
   programme-opening** — its own first sentence: "begins the programme of
   establishing what can be claimed." S1/S2 are closed theorems, but the
   subsection's framing is deliberately that of a labelled extension beyond
   the paper's advertised arc; an abstract sentence would promote an
   extension the paper itself labels as outside the separation theorem.
2. **Bound-interaction**: the abstract is a finished 249-word arc (252 by the
   Task-107 count — a counting-convention difference; either way at the
   venue's ~250 soft cap). Any addition pushes past the cap without any
   deletion available under the standing rules — the same interaction that
   correctly declined the sixth highlight (Elsevier caps highlights at five;
   v53 has exactly five).
3. **Visibility is already served**: the contribution list (xi), the
   σ-notation disambiguation, §5.8's own relevance chain, and the paper's
   keywords make the material discoverable; the LPI hook is the first thing
   §5.8 names.

**Ruling: not merited for the abstract.** The Task-107 decline is upheld on
an independent merits re-evaluation. Recorded for the owner, should the gate
ever be re-opened (all strictly additive, one-site, no bound interactions
with existing abstract sentences): (a) the ready-to-transcribe clause for the
final abstract paragraph — "a labelled substitutability-spectrum extension
interpolates the two doctrines between the linear and Leontief aggregators,
with the Living Planet Index's functional form as an intermediate member"
(+27 words, abstract → ~276 words — over the soft cap, which is why it is
declined); (b) the zero-cost alternative — one keyword ("substitutability
elasticity" or "CES aggregation"), which adds visibility with no bound
interaction at all. Neither is applied in this round.

## 5. Dispositions

- v53 stands as the final version; **no file was modified** (standing
  never-overwrite rule).
- F1–F5 and the two σ-visibility options are recorded for a future v54
  round, to be batched with the middle-regime wave's five transcription
  items (`batch 8/middle_regime_wave/MIDDLE_REGIME_WAVE.md`, §8) — a natural
  single v54: the Table 5 middle cell + row-(iii) refinement + κ*+
  blend-fragility + the spectrum subsection are one coherent wave, with F1,
  F2, F4, F5 as its mechanical/precision riders.
- The σ-abstract ruling: declined and recorded (§4).

## 6. Reproduction

The review's arithmetic spot-checks are re-derivable from the two committed
verifiers (`batch 8/sigma_spectrum_wave/` and
`batch 8/middle_regime_wave/`, 57 + 77 checks, all passing, byte-reproducible
logs); the section/table numbering was verified against the v53 PDF text
layer; the reference/figure/abbreviation checks are one-line greps against
the tex source.
