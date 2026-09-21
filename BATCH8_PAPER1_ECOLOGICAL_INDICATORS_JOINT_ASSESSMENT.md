# Batch 8 — Paper 1 (Ecological Indicators) Joint Assessment of the Self-Correcting Audit Streams

**Date:** 2026-09-19. **Audited state:** commit `5163f7d` (the batch-8 upload on top of Paper 1 v52 at `bbbf588`); all verification performed against the current manuscript `arena agent 1/paper rewrites/latex/paper1_assessment_separation_v52.tex` (1,817 lines, md5 `2f43e2cadf94856fd20c2437f024ce6b`). The audit file: `batch 8/paper 1 ecological indicators.txt` (1,291 lines, md5 `fc202ec9db2783c952dd71e6fa0f3abc`), read in full at line level.

**Owner standing rule for this assessment (recorded verbatim in substance):** *no legitimate content from the audit or the manuscript it refers to may be removed or condensed; this rule overruns any recommendation on removing or shortening valid manuscript content.* Every removal/shortening recommendation in the streams is therefore recorded below as **OVERRIDDEN**, with its legitimate intent preserved in additive form where one exists. No other repository file was modified in this round; this assessment is the round's only creation.

**The streams (the file's internal evolution — "the audits evolve and correct themselves"):**

| Stream | Lines | Role in the evolution |
|---|---|---|
| deepseek | 1–110 | Seven enhancement proposals for *Ecological Indicators* (indication-theoretic reframing; EBFM grounding; non-compensatory aggregation as a contribution; benchmark realism; positioning; a design checklist; an abstract draft) |
| gpt | 111–819 | The critical audit: corrects deepseek's overclaims, adds the protocol-level precision, the fishery-benchmark honesty demands, and its own restructuring/shortening recommendations (the latter now overridden) |
| qwen | 820–1023 | Ten line-level observations (all verified below) + a synthesis endorsing gpt's corrections + proposed LaTeX for the pivot points (one draft numerically defective — §3.4 below) |
| the generalization stream (unlabelled continuation) | 1025–1291 | The substitutability-elasticity (σ) reframing, six generalization pathways A–F, the persistence taxonomy, the owner's Liebig correction accepted and integrated into the "Idealized Regime vs Practical Reality" synthesis, and a Theorem 11 sketch |

---

## 1. Verification performed before adjudication (all against v52)

Every checkable claim was re-verified against the manuscript before acceptance. Line numbers are v52's.

### 1.1 qwen's ten line-level observations — 10/10 CONFIRMED

| # | Claim | Verdict on v52 |
|---|---|---|
| 1 | Thm 6 (§4.4) precedes Thm 5 (§4.6); numbering non-sequential in presentation order | **Confirmed** — Thm 6 at line 424 (§4.4 "Weight-family…"), Thm 5 at line 528 (§4.6 "Witnessed separation") |
| 2 | "Filippov; Warga" (§4.11) have no reference entries; De Lara & Doyen (2008), Rockström et al. (2009), Raworth (2012) in References but never cited in text | **Confirmed** — Filippov/Warga cited at ~843; the References block (1648–1793) contains neither entry. "De Lara" has zero body hits; Rockström and Raworth appear only in the reference list. (Care: *Doyen and Gajardo (2020)* IS cited — at 103, 869, 927; the uncited entry is the De Lara & Doyen 2008 book. Rockström also appears as co-author of the cited Lade et al. 2020) |
| 3 | MSY and PROMETHEE listed but never used in the body | **Confirmed** — MSY only at the abbreviation item (1365); PROMETHEE at the abbreviation item (1366) and inside the Schär et al. reference title (1759). (CES, by contrast, IS used — "CES-type substitutability" in §5.1) |
| 4 | Reference-ordering slips | **Confirmed** — De Lara & Doyen (2008) before Dasgupta & Mäler (2000); Rockström et al. (2009) before O'Neill et al. (2018); Schaefer (1954) before Saint-Pierre (1994); Schär et al. (2025) after Saint-Pierre. Alphabetical order requires: Dasgupta, De Lara; O'Neill, Rockström; Saint-Pierre, Schaefer, Schär |
| 5 | `\emergencystretch` set twice (2.5em then 3em); `longtable` loaded + hooked but never used | **Confirmed** — lines 4 and 16; `\begin{longtable}` count = 0 |
| 6 | Escaped underscore in the mailto target | **Confirmed** — line 24 (`mailto:amin\_abaee@ut.ac.ir`) |
| 7 | Fig 1 caption reserve bar x = 0 vs canonical witness x = ½ elsewhere | **Confirmed** — Fig 1 caption (636): "the reserve bars show the bridge stock x against the rescue cost c = 1 (Panel A: x = 0; Panel B: x = 1)"; Fig 2 caption (642): "at the witness point (x, s₁, s₂) = (1/2, 6/5, 6/5)". The dip arrows are indeed x-independent (the floor-plane panels do not depend on x), so this is a caption-consistency point, exactly as qwen says |
| 8 | §6.3 trough "0.6 LRP units" vs critical zone "about a third of the LRP in 2015" — 0.6 > ≈0.33, "inside the critical zone" is loose | **Confirmed** — the trough is "(B = 6/5 kt, 0.6 LRP units ≈ 531 kt)" and the zone is "about a third of the LRP in 2015 (DFO, 2016)" (~295 kt). 531 kt is below the LRP but *above* the 2015 level; the phrase needs the explicit comparison |
| 9 | §4.9 proof-location sentence omits Thm 6 (App A), Prop 10 (App B), Prop 11 (App C) | **Confirmed** — line 724 lists "Proposition 3, Proposition 4, Theorem 5, Remark 7, and Theorems 8–9"; the appendix proofs at 1376–1645 additionally cover "the finite-menu theorem (Section 4.4)" (= Thm 6), "Proposition 10 (Section 4.11)", and "the rescue threshold (Section 5.6)" (= Prop 11) |
| 10 | Qed inside the last enumerate item in the Proof of Theorem 9; typed-endpoint operator introduced after the four-operator chain despite the "five operators" count | **Confirmed** — `\ensuremath{\square}` sits inside item (iii) of the enumerate at 1612–1629; §3.1 introduces four operators with the inclusion chain (319–344) and only then the "Definition (typed-endpoint operator)" at 346 |

### 1.2 gpt's quoted phrases and claims — confirmed with three paraphrases mapped

All of gpt's verbatim quotes were located in v52 (several across line breaks): the title (line 20); "mixing plans as fractional blends closes every aggregate-certified state exactly" (abstract, ~40); "the aggregate alone cannot tell the rescuable from the impossible" (~48); "This paper addresses a question that the indicator literature has left comparatively open" (138–139); "no choice of weights repairs the difficulty" (151); "The endpoint operator represents aggregated accounting evaluated on audited snapshots" (339); FP_agg notation (550); "impossibility region" (548); "pure-versus-mixed strategies" (801); "the reviewer checks the dashboard, not the floors" (1223); "conservative for the nonlinear realization" (1199–1200); "cannot certify noncompensatory transition safety" (1070); "mid-1980s" (1303); LRP 884.6 kt (1297, 1302); "about a third of the LRP" (1307); "the order of the stock's swing" (~1310). Three quotes are paraphrases that map to v52 wording: "the dashboard remains certified while the biomass floor is breached" → "the transition is certified at every weighting… the aggregate dashboard certifies a transition that violates the biomass limit on both branches — with the strike and without it" (the qualification gpt asks for is *partially already present*); "This section realizes the same datum as a standard biomass–yield resource model" → present verbatim at 1192–1193; "opening stock (1.6 LRP units)" and "0.6 LRP units" → present at ~1305 and ~1306. `B_lim = 2` kt, `K = 10`, `r = 4` confirmed (1206–1207); FAST/SLOW/STAGED/NO-SWITCH and the heatwave convention confirmed (1213–1231); "index green" occurs exactly once (993, the translation-table row) with no traffic-light classification defined anywhere; Table 2 = the terminology map (`tab:translation`, 958–960) and Table 3 = "Policy instruments acting on the acceptance gap" (`tab:instruments`, 1112–1113), both exactly as deepseek names them; Becker et al. (2017) is absent from v52; Gao et al. (2023) is present and cited in the introduction (151–152, added in v52 itself).

### 1.3 The two "math error" claims — adjudicated (one partially defective)

**(a) The Northern cod anchoring (gpt 2.3, qwen's draft).** The manuscript's convention is internally consistent and correct: `s₁ = B − B_lim` is a **kt margin** ("a stock B = B_lim + 6/5 = 16/5 kt (6/5 kt = 1.2 above the limit)", line ~1229), so `B(0) = 16/5 kt = 1.6 × B_lim = 1.6 LRP units ≈ 1.42 Mt` ✓, and the trough `B = 6/5 kt = 0.6 LRP units ≈ 531 kt` ✓. The abstract datum's `s₁ = 6/5` is a kt margin, not a biomass ratio — and the manuscript already states the explicit chain. gpt's surviving, correct core: **one explicitness sentence at the anchor** (the kt-vs-ratio distinction, with the normalized reading `b(0) = B(0)/B_lim = 8/5 = 1.6` stated). **qwen's proposed §6.3 LaTeX is defective as written:** by silently re-reading `s₁ = 6/5` as *normalized* (`s₁ = b − 1`), it computes `b(0) = 11/5 = 2.2 B_lim` and a trough `b = 0.2 B_lim` — contradicting the manuscript's deposited exact-arithmetic witness (the tube tables' dip-2 arithmetic is in kt, verified by the benchmark script) and breaking the historical anchor (2.2 LRP units ≈ 1.95 Mt is *not* "the neighbourhood of the assessed mid-1980s biomass"; 1.6 LRP units ≈ 1.42 Mt is). The corrected variant (keep the kt convention; add the explicitness sentence) achieves gpt's intent without touching a single verified number.

**(b) Theorem 6's scope (gpt 1.4).** The body theorem **already carries the margin-class hypothesis** — "suppose each plan's coordinate-wise admissibility is governed by a required-margin vector d_a… (Plans outside this margin class — reserve-financed or destination-failing plans — are handled separately, as in Section 4.5.)" (424–431) — so gpt's proposed restatement is already the theorem's content; what remains genuinely unqualified is the **abstract's** "a general geometric result characterizes the gap for any finite menu of plans" (~43). The surviving fix is the abstract qualifier ("any finite menu of margin-reducible plans") plus optionally the retitle gpt/qwen propose ("finite-menu characterization for margin-reducible plans"). gpt's claim that the current wording is "too broad" is correct for the abstract and already repaired in the body.

### 1.4 What v52 already contains (the streams under-credit the manuscript)

A material fraction of gpt's "softening" asks already exists in substance:

- **§5.5 Scope delimitations (1009–1065)** already carries: "No absolute impossibility. The impossibility region is a negative certificate **relative to the specified four-action menu**; with a larger menu it can shrink or vanish" (= gpt's "menu-relative impossibility region" in substance); "No separation under coupled all-floor shocks… The separation is exhibited for, and scoped to, the specified action-indexed class… (Lade et al., 2020)" (= gpt 2.2's structural-assumption demand, plus the citation the generalization stream's pathway C leans on); the weight-family scoping; "No welfare claim about prices"; "No empirical transfer"; "No claim that V_weak is the genuine-savings criterion"; "No universal doctrinal ranking".
- **§5.1 The doctrinal reading (852–910)** already contains the information/commitment reading the generalization stream's pathway E proposes as a contribution: "∃a∀w is a commitment made before the weight is known — the strong doctrine's robustness demand — while ∀w∃a_w lets the action be chosen after the weight is observed. On the witness, the acceptance gap… measures the value of information about the assessment weight. Theorem 9 qualifies this reading… Proposition 10 sharpens the point: the value of information is removed by convexifying the action space, not by sharing actions in time." **Pathway E is therefore largely pre-implemented**; what survives from it is only the explicit adaptive-management/MSE literature anchor (Holling/Walters; Management Strategy Evaluation).
- **§5.1's closing paragraph** explicitly disclaims the nonlinear territory: "Nonlinear aggregate indices — CES-type substitutability or endogenous, state-dependent weighting… are different assessment operators, **and the theorems claim nothing for them**." This is precisely the gap the σ-spectrum extension (pathway A) would fill — the manuscript itself marks it as open, which strengthens pathway A's first-priority status.
- §5.1 already distinguishes "the scalarized aggregate doctrine as formalized here" from "weak sustainability simpliciter" — the care the final regime-mismatch framing needs in order to be integrated without overclaiming.

### 1.5 Theorem 11 sketch (the final stream) — adjudicated

Part (1) (the gap is maximal at the linear/σ→∞ limit, yielding the Thm 5 region) restates Theorem 5 and is fine. Part (3) (Leontief/σ→0: the gap vanishes identically because the aggregator is weight-independent — `min_i(s_i/w_i) ≥ 0 ⟺ s ≥ 0`, so per-weight acceptance degenerates to common-plan acceptance) is elementary and correct. Part (2) (**monotonicity**: the gap shrinks monotonically as σ→0) is a **conjecture** — the stream itself says "Conjecture, to be proved on a witness" — and cannot enter the manuscript as a theorem without its own exact rational witness and machine verification under the house discipline. The "Living Planet Index = σ = 1" identification is a heuristic reading (the LPI is a geometric mean of *relative abundance indices*, not of floor margins) and needs a precise, citation-backed statement before inclusion. The regime-mismatch framing ("Idealized Regime" vs "Practical Biophysical Reality") survives as an interpretive frame, provided §5.1's existing guard ("not weak sustainability simpliciter") is retained alongside it — the frame *explains* why the idealized regime's protocols fail on practical-regime systems; it must not collapse the distinction between the formalized operator and the whole doctrine.

---

## 2. The evolution's correction chain (what the streams corrected in each other)

1. **Normative → conditional.** deepseek: the typed operator is "the indication-theoretically correct choice." gpt: too strong — it is correct **if the floors are genuinely separately binding**, with a criteria list (legal/regulatory binding; irreversibility; threshold behavior; unverified substitutability; asymmetric loss; inability to compensate after breach; stakeholder constraint-vs-preference agreement). **The conditional form survives.**
2. **Realization → stylized embedding.** deepseek: ground the benchmark in EBFM indicator literature and use the cod anchoring more substantively. gpt: the income floor and reserve have no ODEs — the section is partly relabeling; call it a stylized embedding (or add the missing equations); do not suggest the trajectory reproduces cod history. **The stylized-embedding label + the motivation-paragraph-with-exact-DFO-values form survives; the "remove the historical statements" branch is overridden (§3.D).**
3. **Convexification trust → feasibility qualification.** deepseek: blend-collapse means a composite index can be made sound if the policy space includes convexified actions. gpt: only when the blended control is physically feasible, institutionally implementable, and dynamically validated; Thm 9 is about menu convexification on the witness datum, not general "mixing plans." **Survives qualified; the manuscript's Thm 9 is already witness-scoped, so the surviving addition is the prominent limitation paragraph (affine-map/relaxed-control assumptions) before Thm 9 plus the institutional-feasibility qualifiers in the policy reading.**
4. **gpt's own overreaches.** The "1.6 math error" reading is partially defective (§1.3a — the manuscript is consistent; only an explicitness sentence is needed); the "reduce by one-third", "move to supplementary", and "shorten" recommendations are overridden by the standing rule (§3.D); the four-protocol table and the semantics table are genuinely missing and survive.
5. **qwen's synthesis** endorses gpt's corrections and drafts the LaTeX — with one numerically defective draft (§1.3a) — and its ten line-level observations all verify.
6. **The final stream** accepts the owner's Liebig correction ("weak sustainability is the idealized mathematical fiction; strong sustainability the physical baseline"), integrates it into the regime-mismatch synthesis, and orders the generalization program (pathway A first). Its pathway E was found pre-implemented (§1.4); its Theorem 11 part (2) is a conjecture (§1.5).

---

## 3. The consolidated surviving points

### 3.A Additions (new content — survives in full under the standing rule)

1. **The four-protocol table** (fixed-weight `E_w(z)`; weight-robust `∀w∃a_w`; common-plan `∃a∀w`; coordinate-wise `∃a ∈ E_typ(z)`), placed early (gpt 1.2; qwen's draft at 882–897) — prevents the reading that the paper attacks composite indices indiscriminately; the separation is specifically Protocol 2 vs Protocol 4.
2. **The evaluation-semantics table** (physical vs typed floors × tube vs endpoint; gpt's §3 note; qwen's draft at 911–925) — organizes the five existing operators without removing any of the prose.
3. **A "Remark 2 / Proposition 3 interpretation box"** promoted into §1/§5: *static scalarization is not the source of the counterexample — the full cone detects every component violation on a fixed trajectory; the failure appears because different weights may select different trajectories* (gpt's line-level note; both audits call this the paper's differentiator).
4. **The indicator-validity section with four design tests** (static losslessness; protocol quantifiers; path-wise observability; menu completeness and convexity) before the policy implications (gpt #5; qwen's draft at 960–970).
5. **The practitioner audit checklist** — the consolidated 10-point list (gpt #6 + qwen's draft 975–986, which subsumes deepseek's 6-point version).
6. **The disturbance-sensitivity treatment across three regimes** (gpt 2.2 + pathway C + the persistence taxonomy): (i) action-indexed separable — the witness, proven; (ii) common biomass shock — **honestly marked as not yet analyzed** (qwen's "Reduced/Shifted" cell is speculative and must be computed, not asserted); (iii) coupled multi-floor — universal rejection, already stated in §5.5, with the exact conditions made explicit in the table. The persistence-taxonomy table (grow/vanish/persist per generalization) is itself a contribution (the final stream, §5 of its framework).
7. **Positioning additions** (deepseek #2/#5 + gpt's "organize by problem"): Becker et al. (2017, *Ecological Indicators* 80, 12–22) on weights vs importance — the paper's result is orthogonal ("even if weights perfectly reflect importance, the quantifier order can still produce the gap"); the fisheries EBFM indicator-performance literature (specificity/sensitivity/threshold response) for the dashboard reading; viability-in-fisheries work for the backward recursion; a fisheries-specific column for the typed-floors translation (LRP/Blim, FMSY/Flim, fleet income/quota value, buy-back/adjustment fund) extending Table 2. Gao et al. (2023) is already in v52 and belongs in this cluster.
8. **The substitutability-elasticity (σ) framework as a labelled extension program** (pathway A first, per the final stream's ordering): the Leontief identification (E_typ as the σ→0 member of the aggregate family — dissolving the weak/strong dichotomy into a continuum); the regime-mismatch framing (Idealized vs Practical); Theorem 11 parts (1)/(3) as an elementary proposition with part (2) as a stated conjecture; each generalization shipping its own small exact witness per the relevance discipline ("generalize the datum, not just the theorem"; every result anchored to a named indicator and a verifiable exact datum). All additive — the manuscript's existing doctrinal-care paragraphs (§1.4 above) stay in full.
9. **Reserve-stock institutional forms** (license buy-backs, transition assistance, quota banking) mapping κ* = 1 − x onto real institutional quantities (deepseek #4).
10. **Conservatism-invalidation caveats** for the certified tubes (depensation in the stock-recruitment relationship; nonlinearly amplified heatwave mortality at low stock) (deepseek #4).
11. **The dashboard-only architecture as a stated assumption**: "To isolate the assessment-operator issue, the benchmark assumes certification is based on the aggregate dashboard… a deliberately adverse reporting architecture, not a claim about current fisheries assessment practice" (gpt 2.4) — one sentence, additive; §6.3's current sentence states the convention but not the not-a-claim-about-practice disclaimer.
12. **Reference entries for Filippov and Warga** (qwen #2) — add the entries; the in-text citations stay.
13. **In-text citations for the currently uncited entries** — De Lara & Doyen (2008) at the viability positioning (§5.2), Rockström et al. (2009) and Raworth (2012) at the safe-operating-space/critical-natural-capital statements (§5.1) — additive; the entries stay.
14. **Exact DFO values** for the mid-1980s neighbourhood and the swing statements (gpt 2.3's "motivation paragraph with exact DFO values" branch) — the statements stay, strengthened with the assessed numbers and labels.
15. **A limitation paragraph before Theorem 9** (gpt 1.5): the blend-collapse result is a theorem about the abstract witness datum and its explicitly defined convexified control map; convexification must be demonstrated from the model equations or treated as a management assumption; blended controls require physical and institutional implementability (fractional effort/quota/seasonal resolution; monitoring and enforcement).

### 3.B Precision rewordings (content preserved; scope made explicit)

16. Abstract, Thm 6 sentence: "any finite menu of plans" → "any finite menu of **margin-reducible** plans" (§1.3b); optionally retitle Thm 6 "…for margin-reducible plans".
17. "no choice of weights repairs the difficulty" (151) → append "under the per-weight, weight-adaptive certification protocol" (gpt #7).
18. "the aggregate alone cannot tell the rescuable from the impossible" (abstract ~48) → append "without separately checking the floors or verifying a common implementable plan" (gpt's abstract note).
19. "left comparatively open" (138) → the softened literature-priority phrasing ("a dynamic question that is less explicit in much of the composite-indicator literature"), retaining the claim (gpt's intro note; §5.2's existing honest novelty paragraph at 937–944 stays).
20. "index green" (993, translation table) → "index nonnegative" (or define the traffic-light classification) — single occurrence (gpt 3.4).
21. "The endpoint operator represents aggregated accounting evaluated on audited snapshots" (339) → "any assessment architecture that evaluates constraints only at sampled or audited endpoints" — a generalization, additive in meaning (gpt's §3 note).
22. First-use qualifiers at Theorem 5: define FP_agg as "relative to the typed criterion and the specified menu" at first use (gpt's Thm 5 note; the Gap_agg|typ rename is optional with FP_agg kept as an alias — no notation is deleted).
23. The unit-convention explicitness sentence at the cod anchor (§1.3a's corrected variant): s₁ is a kt margin above B_lim; the normalized stock is b(0) = B(0)/B_lim = 8/5 = 1.6; the abstract margin 6/5 (kt) is not itself a biomass ratio.
24. The critical-zone precision (qwen #8): the trough at 0.6 LRP units (~531 kt) is below the LRP and above the ~⅓-LRP 2015 level (~295 kt) — state both comparisons explicitly.

### 3.C Mechanical and cosmetic fixes (no content change)

25. Reference-order corrections: Dasgupta & Mäler before De Lara & Doyen; O'Neill et al. before Rockström et al.; Saint-Pierre before Schaefer before Schär (qwen #4).
26. §4.9 proof-location sentence completed: add Thm 6 (Appendix A), Prop 10 (Appendix B), Prop 11 (Appendix C) (qwen #9).
27. Theorem 9's qed symbol moved outside the final enumerate item (qwen #10).
28. Preamble hygiene: one `\emergencystretch` (keep the operative 3em); the mailto underscore unescaped in the URL argument; the unused `longtable` load noted (harmless; leaving it is also acceptable).
29. Unused abbreviations (MSY, PROMETHEE) given natural body uses rather than removed — MSY at the sustained-yield quota discussion (§6.3), PROMETHEE at the MCDA compensability discussion (§5.2's Cinelli/Schär sentence) — keeping the abbreviation entries per the standing rule.
30. Fig 1 caption consistency sentence: Panel A's reserve bar is drawn at x = 0 (the impossibility-slice representative) while the dip arrows are x-independent and the canonical witness point is x = ½ (qwen #7).
31. Theorem presentation order (Thm 6 before Thm 5): a presentation note, or a renumbering — the latter touches cross-references and ledger rows, so it must ride a fail-loud implementation round if chosen (qwen #1).

### 3.D OVERRIDDEN by the owner's standing rule (recorded; not to be implemented as removals or condensations)

32. gpt's "Reduce that material [the weak/strong sustainability introduction] by approximately one-third" — **OVERRIDDEN**. The introduction stays in full; the protocol table and the indicator-validity framing may augment it.
33. gpt's "move some game-theoretic discussion to supplementary material… the paragraph… should be shortened" (Thm 9/Prop 10 correspondence) — **OVERRIDDEN**. The correspondence passages stay; a supplementary *pointer* may be added.
34. gpt's restructuring demand to "move peripheral framework extensions to supplementary material" / "parallel framing systems… weaken the submission" — **OVERRIDDEN** for anything in the main text (the Supplementary Material already exists as a separate document; no main-text content moves out). Reordering and the orienting tables survive (§3.A).
35. gpt's "Remove them or place them in a clearly labeled motivation paragraph" (the mid-1980s/swing statements) — the removal branch **OVERRIDDEN**; the labeled-motivation-paragraph-with-exact-DFO-values branch survives (§3.A point 14).
36. The wholesale abstract/intro rewrites (deepseek #7's abstract; gpt's suggested abstract) — **OVERRIDDEN as replacements** (they drop existing sentences' content). Their *additions* survive: the protocol framing can enter the existing abstract only with every existing claim preserved; where journal abstract-length bounds conflict with the rule, the rule overruns and the bound question goes to the owner.
37. Title-change proposals (gpt's two titles) — recorded as owner-gated framing choices, not content removals; the option of keeping the current title and carrying the indicator-theoretic framing in the abstract/intro stands.

### 3.E Rejected auditor materials (defective as written)

38. qwen's §6.3 normalized-biomass LaTeX draft (b(0) = 11/5 = 2.2 B_lim; trough b = 0.2 B_lim) — internally consistent under a *changed* convention but numerically inconsistent with the manuscript's kt convention, the deposited exact-arithmetic witness, and the historical anchor (§1.3a). The corrected variant is §3.B point 23.
39. gpt's normalization as a wholesale convention change — same defect; the explicitness sentence achieves the goal without breaking the verified numbers.
40. Theorem 11 part (2) (monotonicity of the gap in σ) as a theorem — it is a conjecture (§1.5); enter as a stated conjecture with its own exact witness when pursued.
41. The "Living Planet Index = σ = 1" identification without a precise statement (§1.5).
42. qwen's sensitivity-table cell "Common biomass shock → Reduced/Shifted" — asserted, not computed (§3.A point 6); the middle regime must be analyzed before any cell is filled.

---

## 4. Honest residuals and open items

- **Version target of the audits:** the streams were evidently written against a v51/v52-era state and do not reference v52's own Gao et al. (2023) addition, §5.5's scope delimitations, or §5.1's information reading (all of which pre-answer several asks). Any future implementation round must re-verify each point against the then-current version — several may already be closed.
- **Nothing was implemented this round** (the owner's directive: assessment and consolidation only; no other repo files modified). The consolidated points in §3 are the working queue for the implementation round(s), under the standing rule and the house discipline (new file versions, never overwrite — per the owner's separate standing directive this round).
- **The σ-spectrum program (§3.A point 8) is a research addition**, not an edit: it needs its own wave with exact rational witnesses, machine verification, and the relevance test (named ecological decision; changes what an actual indicator reports; new exact witness datum; alters at least one management action).
- **Owner-gated framing decisions:** the title options (§3.D point 37); abstract-length bounds vs the standing rule (point 36); whether to renumber Thm 5/6 (point 31).
- The PAT supplied this round again carried the stray `.1` suffix (sixth occurrence); the corrected form was verified and used in-memory only (see the worklog push record); rotation remains advised.

---

## 5. Implementation record

- This file is the round's only creation: `BATCH8_PAPER1_ECOLOGICAL_INDICATORS_JOINT_ASSESSMENT.md` (repo root, beside the batch-5 precedent).
- No manuscript, supplementary, tex, pdf, audit, or any other repository file was modified (verified: the working tree shows only this new file plus the worklog append).
- Verification artifacts: the line-level checks of §1 were performed directly against `paper1_assessment_separation_v52.tex` at commit `5163f7d`; the audit file `batch 8/paper 1 ecological indicators.txt` was read in full (1,291 lines).
- Repo worklog Task 104 records the round; both committed and pushed with the owner's PAT (corrected form; in-memory only; zero residue; rotation advised).
