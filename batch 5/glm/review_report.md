# Line-Level Review: `papers/paper{1..5}_*/manuscript.md`

**Repository:** `MIKEAA2020/general-sustainability`, branch `main`, commit `8a286c4` (Task 58, HEAD at time of review).
**Scope:** All five core-paper manuscripts, read line by line (3,535 lines, ≈69.8k words), plus targeted verification against the committed artifacts (machine-witness runner, concordance CSV, closure report, source articles A002/A010/A012/A013/A014/A018, canonical schema JSON, external review packet) and independent recomputation of every checkable number.
**Focus (per reviewer instruction):** math & logic flaws and internal inconsistencies; every finding carries file + line + verbatim quote + reason + suggested fix.

---

## 1. Executive summary

The corpus is in unusually strong internal shape for its size: all five committed self-checks pass, the Paper 1 machine witness reproduces 25/25, the concordance arithmetic (354 closed + 27 open + 28 rejected = 409) is exact, and a large fraction of the numerical claims I recomputed from scratch — the M3-B linearization coefficients, the Hopf-cubic coefficients `c0/c1/c2`, the protective-channel gains, the cod assessment-table values, the ψ-mechanism table, the incidence-matrix column sums — reproduce to the displayed precision. The flaws that remain are concentrated in (a) one genuine numerical self-contradiction in Paper 4 §6.1, (b) self-containedness failures in Paper 2 (two theorems whose statements omit their defining data), (c) count/label mismatches (family count, source count, "two vs four" scored-forecast papers, four out-of-sequence remark numbers), and (d) a systematic gap between the camera-ready bibliographies and the texts, which cite almost none of them.

**Severity counts: 1 HIGH · 10 MODERATE · 15 MINOR = 26 findings.**

| # | Sev. | Paper | Finding (short) |
|---|------|-------|-----------------|
| F01 | HIGH | 4 §6.1 | Fold bracket [5.574,5.576] contradicts multiplier 0.964 at τ=5.5815 in the same sentence |
| F02 | MOD | 2 §6.4 | Theorem 6.4 labeled "theorem" with no proof (deferred to camera-ready) — violates the paper's own status table |
| F03 | MOD | 2 §10.1 | Cond. Thm 10.1 uses undefined y, A, v₀, H_loc, A_min; hitting event unspecified |
| F04 | MOD | 2 Abstract | "twelve families" vs 10 enumerated (11 family-labelled sections in the body) |
| F05 | MOD | 2 §5/6/8/13 | Four out-of-sequence labels: Remark 5.9, 6.16, 8.15, 13.4 |
| F06 | MOD | 2 §5.2–5.9 | CES specification and μ_A never stated; used in Thm 5.2, Cor 5.3, Remark 5.9 |
| F07 | MOD | 1 §10.2 | "closed 354 rows across twenty sources" — the closures span **19** sources (closure report's own header lists 19; its "thirteen further closures" enumerates 12) |
| F08 | MOD | 1 §2.2 | "Thirteen declared slots" enumerated as 11 differently-named items; canonical form (A002 source, Paper 2 Def 2.3, schema JSON) is a 13-tuple with other names |
| F09 | MOD | cross | "Two scored-forecast papers" (Papers 1, 3, 5) vs "the four Wave E papers" (external review packet §1.2) |
| F10 | MOD | 5 §6.2 | "the Schaefer model is the Allee-factor-1 specialisation" — no parameter value of the displayed family has Allee factor ≡ 1 |
| F11 | MOD | all | Dangling references: 1/14 (P1), 2/4 (P2), 16/18 (P3), ≈21/37 (P4), ≈14/22 (P5) bibliography entries never cited in text |
| F12–F26 | MINOR | — | See §4 (notation slips, citation mismatches, wording, plausibility flags) |

---

## 2. HIGH-severity finding

### F01 — Paper 4 §6.1: the lower fold bracket and the Floquet multiplier trajectory contradict each other

**Location:** `papers/paper4_delay_dynamics/manuscript.md`, line 433.

**Verbatim:**
> "the lower bistable boundary is the disappearance of the stable large cycle at a fold of periodic orbits in $\tau\in[5.574,5.576]$ (amplitude $25.0$ at $\tau=5.574$; adaptive-mesh collocation with variational Floquet tracking resolves the dominant multiplier as a single real eigenvalue — imaginary part identically zero at every measured point — rising monotonically from $0.240$ at $\tau=4.0$ to $0.964$ at $\tau=5.5815$ with orbit residual $\sim10^{-12}$: the signature of a real $+1$ crossing, a saddle-node of periodic orbits, not a Neimark–Sacker or torus event)"

**Problem.** Three mutually inconsistent statements occupy one sentence:
1. The stable large-cycle family *folds* at τ ∈ [5.574, 5.576] — at a saddle-node of periodic orbits the dominant multiplier crosses **+1 exactly at the fold**, and the family does not exist beyond it.
2. Yet the collocation/Floquet tracking reports a measured point of that same branch at **τ = 5.5815 > 5.576** (a τ past the fold), with dominant multiplier **0.964 < 1**.
3. A multiplier still below 1 and "rising monotonically" at 5.5815 places the +1 crossing at some τ > 5.5815, not at 5.574–5.576 — so the "+1 crossing" signature asserted for the 5.574–5.576 event is not what the displayed multiplier data show.

The tension originates in the A018 source (`revised_articles/A018_capital_liquidation_corrected.tex`, line 904), which however contains a reconciling sentence that Paper 4 **dropped**: *"The orbit remains a converged fixed point of the collocation map through τ=5.5815 (residual ~10⁻¹²), while long-horizon simulation shows the basin collapse between τ=5.574 and 5.576; the exact crossing point and the 0.002 yr gap remain to be pinned."* Even in the source, calling the 5.574–5.576 event "a saddle-node of periodic orbits (real +1 crossing)" sits badly with a multiplier of 0.964 at 5.5815 — a **basin collapse** (crisis-like loss of the attracting cycle's basin) is not an SNPO of the cycle itself. Paper 4 omits the caveat and keeps the SNPO classification, sharpening the contradiction. Note §6.1 also reports the *small*-branch fold at ≈5.587 with multipliers 1.0514 → 0.99898 (lines 433, 441) and A.2 reports the rebuilt fold at 5.587236 (line 649), so "5.5815" cannot be reassigned to the small family either (that family is unstable, multiplier > 1).

**Suggested fix.** Restore the source's caveat sentence and re-state the classification honestly, e.g.: "the attracting large cycle loses its basin between τ = 5.574 and 5.576 (long-horizon simulation), while the collocated orbit persists to τ ≥ 5.5815 with dominant multiplier 0.964 still below +1; the exact +1 crossing and the 0.002-yr gap remain to be pinned, so the SNPO classification of this lower boundary is provisional, not a resolved signature." Alternatively correct the τ value (if 5.5815 is a typo) or the multiplier attribution — but as printed the three numbers cannot all be true.

---

## 3. MODERATE findings

### F02 — Paper 2, Theorem 6.4: "theorem" label without a proof contradicts the paper's own status discipline

**Location:** `papers/paper2_theorem_atlas/manuscript.md`, lines 345–353 (statement), 758 (ledger row 24), 846 (§15).

**Verbatim:**
> "**Theorem 6.4 (Instantaneous common-action obstruction) [CC-A001-026 · theorem — mapping: counterexample/limit].** … *Proof status.* The source states the theorem without proof; the row-closure pass registers an explicit one-step proof obligation … The one-step proof will be supplied at camera-ready; …"

**Problem.** §1.3's status table (lines 38–45) defines *Theorem* as "Complete proof under explicit mathematical assumptions," and the paper's first rule is "**No promotion:** a conditional theorem is never stated as a theorem." A statement whose proof does not exist yet — in the source *or* in this manuscript — is labeled a theorem. The ledger (line 758) honestly records "proof omitted in source; one-step proof obligation registered," and §15 (line 846) admits "One proof is omitted in the source (Theorem 6.4)" — so the manuscript contradicts its own labelling in two other places.

**Fix.** Either supply the one-step proof now (it is genuinely one line: any action chosen at B is unsafe for at least one compatible boundary state, by the defining intersection being empty), or relabel as "Theorem (proof obligation registered; supplied at camera-ready)" / demote to conditional status until then.

### F03 — Paper 2, Cond. Thm 10.1: statement not self-contained — y, A, v₀, H_loc all undefined

**Location:** `papers/paper2_theorem_atlas/manuscript.md`, lines 627–633.

**Verbatim:**
> "Suppose $0\le\epsilon<1$ and $y$ is continuously differentiable on $[0,H_*]$ for some $H_*\ge H_{\rm loc}/(1-\epsilon)$, and suppose throughout that interval that $(1-\epsilon)v_0\le-\dot A(t)\le(1+\epsilon)v_0$. Then a first hitting time $T_A\in[0,H_*]$ exists and satisfies $\frac{H_{\rm loc}}{1+\epsilon}\le T_A\le\frac{H_{\rm loc}}{1-\epsilon}$."

**Problem.** The variable **y** is introduced and never used again; the rate condition uses **A**, **v₀**, **H_loc**, which are never defined in the atlas; and the event that T_A is the first hitting time *of* is never stated. The A002 source (`revised_articles/A002_general_theory_corrected.tex`, lines 2176–2190) supplies the dropped preamble: "Let $A(0)>A_{\min}$ and define $y(t)=A(t)-A_{\min}$. If the current net depletion rate is $v_0=-\dot A(0)>0$, the local ratio is $H_{\rm loc}=y(0)/v_0$" (T_A = first time y hits 0, i.e. A hits A_min; the bracket's missing v₀ factors cancel exactly because H_loc = y(0)/v₀). This violates the atlas's own selection rule 5 ("prerequisites can be stated locally without circular dependence", line 29) and its stated aim of making "every assumption explicit." Note the contrast: Paper 3's sibling statement (Thm 5.4, CC-A010-002, lines 418–432) *is* fully self-contained.

**Fix.** Restore the source's two-line preamble before the theorem: define A, A_min, y = A − A_min, v₀ = −Ȧ(0) > 0, H_loc = y(0)/v₀, and state that T_A is the first time A(t) ≤ A_min.

### F04 — Paper 2, Abstract: "twelve families" vs a 10-item list vs 11 family-labelled sections

**Location:** `papers/paper2_theorem_atlas/manuscript.md`, line 9.

**Verbatim:**
> "The atlas spans twelve families: core viability calculus; typed hybrid conservation and positivity; noncompensation and substitution feasibility; observation and epistemic viability; recovery and irreversibility; sampled, hybrid, and information-state kernels; projectability and exact reduction; diagnostics and delay certificates; restricted composition; and institutional implementation."

**Problem.** The enumerated list contains **10** names. The body carries **11** family-labelled sections: F13 (§3), F01 (§4), F02 (§5), F03 (§6), F04 (§7), F05 (§8), F06 (§9), F07 (§10), F10 (§11), F11 (§12), F12 (§13) — the list omits the F12 intergenerational/stochastic family that §13 explicitly carries ("family F12, bounded appendix", line 695). Even counting the unlabeled F00 preliminaries (the budget CSV's "F00 canonical definitions and types") one reaches 12 only by counting a family the list still does not name. Under no reading does "twelve families:" introduce the list that follows.

**Fix.** Either write "eleven families" and add the intergenerational-and-stochastic-bounds family to the list, or state twelve and add both F00 (canonical definitions, §2) and F12 (§13) to the enumeration.

### F05 — Paper 2: four restored remarks break the numbering sequence

**Location:** `papers/paper2_theorem_atlas/manuscript.md` — Remark 5.9 (line 280, between Cor 5.3 at line 276 and Def 5.4 at line 282); Remark 6.16 (line 327, between Thm 6.2 at 323 and Thm 6.3 at 329); Remark 8.15 (line 496, between Thm 8.4 at 492 and Def 8.5 at 517); Remark 13.4 (line 709, before Programme 13.3 at line 711).

**Verbatim (one instance):** "**Remark 6.16 (Certainty-equivalence obstruction) (A001, Remark 4.1).**" — appearing immediately after Theorem 6.2 and before Theorem 6.3.

**Problem.** Appearance orders are §5: [1,2,3,**9**,4,5,6,7,8]; §6: [1,2,**16**,3,…,15]; §8: [1,2,3,4,**15**,5,…,14]; §13: [1,2,**4**,**3**] (verified mechanically). All four are the closure-campaign restored rows (MS-Native-2/3/5/8 in the §14 table), numbered as if appended at the end of their sections but inserted thematically mid-section. Any reader following a cross-reference such as "Remark 6.16" will look for it after 6.15.

**Fix.** Renumber sequentially in order of appearance at camera-ready (the four remarks become 5.4, 6.3, 8.5, 13.3 and downstream items shift), or move the remarks to their numbered positions.

### F06 — Paper 2, Theorem 5.2 / Corollary 5.3 / Remark 5.9: the CES specification and μ_A are never stated

**Location:** `papers/paper2_theorem_atlas/manuscript.md`, lines 266, 276, 280.

**Verbatim:**
> "For fixed $R > 0$, let $c_{\max}(R) = \sup_{A \geq 0} [F(A, R) - \delta_A A]$ in the dimensionally correct CES specification. Then: … (3) if $\sigma > 1$ and $\mu_A < \delta_A$, … The threshold is $\frac{Y_0}{A_0}\,\alpha^{\sigma/(\sigma-1)} \gtreqless \delta_A$ …"

**Problem.** The "dimensionally correct CES specification" is never displayed; σ, μ_A, Y₀, A₀, R₀, α are all used without definition in the atlas. The A001 source (`uploads/topdown.txt`, lines 1175–1200) defines F(A,R) = Y₀[α(A/A₀)^ρ + (1−α)(R/R₀)^ρ]^{1/ρ}, ρ = (σ−1)/σ, and μ_A := lim_{A→∞} F(A,R)/A = (Y₀/A₀)α^{σ/(σ−1)} — without which items (3)–(5) of Theorem 5.2 and the whole of Remark 5.9 are unverifiable from the manuscript. Additionally, Theorem 5.2(5) says "the boundary case $\mu_A = \delta_A$" while the source's item 5 reads "If $\sigma > 1$ and $\mu_A = \delta_A$" — the σ > 1 qualifier (on which μ_A's very definition depends) was dropped.

**Fix.** State the CES specification and the definition of μ_A once (two lines) before Theorem 5.2, and restore "σ > 1 and" in item (5).

### F07 — Paper 1 §10.2 (and the closure report): "twenty sources" is off by one

**Location:** `papers/paper1_general_theory/manuscript.md`, line 337; `research_program/concordance_row_closure_twenty_sources.md` (title and header); echoed by filename in Papers 2–5 provenance sections.

**Verbatim:**
> "its scientific layer — full source reads, per-row verification of kind, proof presence, module, and mapping — has closed 354 rows across twenty sources"

**Problem.** The concordance CSV has exactly **19** sources with `row_verified` rows (A001–A007, A010–A020, A024, A025; 354 rows). The closure report's own header lists 19 source IDs, and its second-campaign sentence says "thirteen further complete closures" while enumerating **12** (A003, A020, A019, A013, A024, A016, A010, A004, A005, A025, A007, A017). 7 + 12 = 19 ≠ 20. (The remaining sources: A008/A009/A015 are `adjudicated_rejected_or_negative_only`, 28 rows; A021–A023 open, 27 rows.)

**Fix.** Change "twenty sources" to "nineteen sources" in Paper 1 §10.2, correct "thirteen" to "twelve" in the closure report (or identify the missing 20th source if one was intended), and re-check the report's title/filename at the next documentation pass.

### F08 — Paper 1 §2.2: the "canonical system" rendering does not match the source, the atlas, or the schema

**Location:** `papers/paper1_general_theory/manuscript.md`, lines 58–60; compare `papers/paper2_theorem_atlas/manuscript.md` lines 77–88 and `research_program/canonical_system_schema_v1_0.json`.

**Verbatim:**
> "The canonical object is a tuple `S` with thirteen declared slots spanning: the typed physical state; the admissible action correspondence; the dynamics (continuous, sampled, hybrid, or delayed as declared per instance); the observation map; the information pattern; the constraint sets (physical, service, liability, obligation, identity, cumulative-harm); the disturbance class; the policy class; the claim-status table; the destination structure; and the declared model map to any other object."

**Problem.** (i) The enumeration lists **11** items for "thirteen declared slots." (ii) The canonical form of the same row CC-A002-003 — displayed verbatim in the A002 source (eq. canonical-tuple) and in Paper 2 Def 2.3 — is the 13-tuple (𝒯, 𝒵, S, B, 𝒱, Γ, 𝒪, 𝒜, 𝒞, ℛ, 𝒟, K, 𝕡): type system, state space, fluxes, boundaries, service possibility, observation, assessment, command, deployment/reset, disturbance, safe-and-just set, policies. None of "claim-status table", "destination structure", or "declared model map" is a component of that tuple, and Γ/𝒜/𝒞/ℛ are absent from Paper 1's list. (iii) The committed schema JSON lists a third variant (state, model, algebraic_constraints, events_resets, actions, uncertainty, observation, assessment, policy, implementation, ledger, services, admissible_set). Paper 1 line 52 says "the canonical forms are stated once here, and the atlas cross-references this paper as the architecture owner" — but the two papers state different objects.

**Fix.** Replace the §2.2 enumeration with the source's 13-tuple (or, if the 11-item prose list is the intended architecture-level gloss, say "spanning (at least)" and reconcile with the atlas's Def 2.3 so the two papers display the same tuple).

### F09 — Cross-document: "two scored-forecast papers" vs "the four Wave E papers"

**Location:** `papers/paper1_general_theory/manuscript.md` lines 46, 333; `papers/paper3_material_ledgers/manuscript.md` line 46; `papers/paper5_sampled_governance/manuscript.md` lines 56, 434; vs `external_review_packet/README.md` §1.2 (lines 23–32).

**Verbatim:**
- Paper 1, line 46: "This is Paper 1 of five assured papers (plus two scored-forecast papers, a conditional Paper 6, …)"
- Packet, line 23: "### 1.2 The four Wave E papers (the scored empirical gate)" — table lists E1–E4 as four separate papers, each with title, path, word count, and status; line 32: "There are exactly four Wave E manuscripts: two scored systems … each with a forecast-ladder leg and an intervention leg."

**Problem.** The packet (the reviewer's declared entry point) counts four scored-forecast papers / nine drafts total; the core manuscripts repeatedly say "two scored-forecast papers exist in the programme." A reviewer reading both will not know whether the programme has two or four scored papers. (If the intent is "two scored *systems*", the core papers' wording should say systems.)

**Fix.** Harmonize: either "four scored-forecast papers (two systems × two legs)" in the core manuscripts, or "two scored-forecast systems (four manuscripts)" in the packet.

### F10 — Paper 5 §6.2: "the Schaefer model is the Allee-factor-1 specialisation" is not true of the displayed equation

**Location:** `papers/paper5_sampled_governance/manuscript.md`, line 328.

**Verbatim:**
> "$$\frac{dS}{dt}=rS\left(1-\frac{S}{K}\right)\frac{S-\mathfrak s}{K-\mathfrak s}-C(t),$$ … and the Schaefer model is the Allee-factor-1 specialisation."

**Problem.** In the displayed family the Allee factor is (S−𝔰)/(K−𝔰). No value of 𝔰 makes it identically 1: 𝔰 = 0 gives S/K (a depensation modification, not Schaefer); the factor tends to 1 only in the degenerate limit 𝔰 → −∞. The Schaefer model is therefore *not* a parameter specialisation of the displayed equation — it is the separate member of the broader family in which the factor is replaced by 1. (The phrase appears only in Paper 5; the A014 source does not make this claim.)

**Fix.** Rephrase, e.g.: "the Schaefer model is the degenerate member of the wider family in which the Allee factor is replaced by 1 (approached only as 𝔰 → −∞ in this parameterisation)."

### F11 — All five papers: camera-ready bibliographies are largely uncited in the texts

**Location:** References sections — P1 lines 404–432; P2 lines 856–864; P3 lines 767–805; P4 lines 774–850; P5 lines 524–568.

**Evidence (surname-occurrence check, body vs reference list):**
- Paper 1: 14 refs, **1** never cited in body (Ekins et al. 2003).
- Paper 2: 4 refs, **2** never cited (Aubin 1991 — the corpus's foundational viability text; Hale 2009).
- Paper 3: 18 refs, **16** never cited (Aubin, Brunner–Rechberger, Chhikara–Folks, Ekins, Eurostat, Feinberg, Fischer-Kowalski, Griebmeier, Guentner, Munda–Nardo, Neumayer, Øksendal, Redner, Ricard, Tapley, U.S. Geological Survey) — including the G3P product papers behind §5.5.1's headline table and the inverse-Gaussian monograph behind §6.3's theorems.
- Paper 4: 37 refs, **≈21** never cited (Åström–Wittenmark, Beretka–Vas, Carpenter, Cloud–Moore–Kearfott, Costantino, Diekmann, Engelborghs, Ezekiel, Gao–Zhang, Guckenheimer–Holmes, Gurney, both Hale entries, Kearfott, Khiyar, Kuznetsov, Ludwig, Moxnes, Ostrom, all three Scheffer entries).
- Paper 5: 22 refs, **≈14** never cited (Ashwin, both Aubin entries, Benjamini–Hochberg, Cadigan — the NCAM model's own paper, Cohen, Costantino, Forssell–Ljung, Gurney, Moxnes, Nešić–Teel, Punt–Donovan, Ricard — the RAM Legacy citation, Tam–Bundy).

**Problem.** The bibliographies were attached in the Task 57 editorial pass, but in-text citation hooks were not. Papers 3–5 in particular cite *no* external source at the points where external data/methods are used (G3P basin table, USGS reserve data, RAM Legacy cohort, NCAM formulation, Lomb–Scargle methodology, multiplicity control), which no journal will accept and which undercuts the "camera-ready" claim in the packet (§1.1 "camera-ready bibliography entry is in place").

**Fix.** Add bracketed citations at the load-bearing points (data sources first: Griebmeier/Guentner at §5.5.1; USGS at §5.5.2–5.5.3; Ricard at §5.3; Cadigan + DFO at §6.2–6.3; Tam–Bundy at §6.4; Statistics Canada at §8.4; method sources: Chhikara–Folks/Redner at §6.3–6.6; Lomb/Scargle/Benjamini–Hochberg at §5.3; Nešić–Teel at §3.2; Forssell–Ljung at §5.4), and remove or justify unused entries.

---

## 4. MINOR findings

### F12 — Paper 1 §4.1: `C = R^n_+ \ {0}` is called "the closed nonnegative cone" — it is not closed
**Location:** `papers/paper1_general_theory/manuscript.md`, lines 144–148.
**Quote:** "be the **closed nonnegative cone** of aggregate weight vectors."
**Problem.** Removing the origin from the closed orthant yields a set that is neither open nor closed (0 is a limit point). Lemma 4.2 is unaffected (e_k ∈ C does the work), but in a paper whose discipline is exact typing, the name contradicts the definition, and "on the closed cone the pointwise aggregate is lossless" (line 148) inherits the misnomer.
**Fix.** Call C "the nonzero nonnegative orthant," or define C = R^n_+ and note that w = 0 is vacuous for the equivalence.

### F13 — Paper 1 §4.3, proof of Theorem A(ii): stray "Succ ⊆ W" and undefined G^w
**Location:** `papers/paper1_general_theory/manuscript.md`, line 174.
**Quote:** "likewise successors lie in `G ⊆ G^w`" … "the same argument over successors gives `Succ ⊆ W`."
**Problem.** W is not defined anywhere in §4 (it is §3.3's recursion notation); the correct conclusion is `Succ ⊆ G`. G^w is used here and in Theorem C (line 217) but never defined (implicitly G^phys ∩ {w·s ≥ 0}, which §4.1 only spells out inline in E_w's definition).
**Fix.** Replace W with G; add "write S^w := S^phys ∩ {w·s ≥ 0} and G^w := G^phys ∩ {w·s ≥ 0}" once in §4.1.

### F14 — Paper 1 §5.2: citation/year mismatches
**Location:** `papers/paper1_general_theory/manuscript.md`, line 235 vs references (lines 414, 430).
**Quote:** "[Das–Dennis 1997/1998]" … "Usubiaga-Liaño et al. 2025".
**Problem.** The reference list contains only Das & Dennis 1997 (no 1998 entry); "Usubiaga-Liaño et al." implies multiple authors but the reference is single-author (Usubiaga-Liaño, A. 2025).
**Fix.** Cite "Das–Dennis 1997" (or add the 1998 NBI paper) and "Usubiaga-Liaño 2025."

### F15 — Paper 3 §3.4/Abstract: "extraction and mining rates" vs an identity that contains only extraction
**Location:** `papers/paper3_material_ledgers/manuscript.md`, line 234 (identity d/dt(N+A^act+A^geo+U) = −qEN), line 248 ("loses mass at precisely the extraction and mining rates, and nothing else"), abstract line 9.
**Problem.** The §2.2 closed block has C^A = 0 (line 102: "Under the registered institutional-failure specialization (μ=ν=ρ=0, C^A=0)"), so no mining term appears in the displayed system; the reading sentence asserts a mining rate that the displayed identity does not contain (it is trivially zero). Theorem 3.11 (line 270) restores mining only "optionally."
**Fix.** "…at precisely the extraction rate (plus the mining rate when optional mining is restored, currently C^A = 0 in the registered specialization)."

### F16 — Paper 4 §6.5: mixed-variant pairing of τ₊ values
**Location:** `papers/paper4_delay_dynamics/manuscript.md`, line 482.
**Quote:** "Candidates A and B share $r=0.02$ and have $\tau_+\approx150$ and $\approx76$ yr respectively."
**Problem.** 150 is Candidate A's **gated** value (150.36; ungated A is 132.37), while 76 is Candidate B's **ungated** value (76.29; gated B is 80.42). The sentence pairs values from different variants of the two systems.
**Fix.** "τ₊ ≈ 132–150 yr (A) and ≈ 76–80 yr (B) across the two effort laws" or name the variant.

### F17 — Paper 4 §7.1: declared symbol clash — g is both the assimilation flux and the memory gain
**Location:** `papers/paper4_delay_dynamics/manuscript.md`, line 496.
**Quote:** "…memory a gain-$g$ filter of $-\mathbf c^\top\dot{\boldsymbol\xi}$ (the symbol $g$ denotes both the assimilation flux and the memory gain, following the source's declared symbol-reuse convention…)"
**Problem.** Within one formula family, g(X,A) is a flux and g = 1/2 or 1 is a loop gain (line 502 uses both). The clash is honestly declared, but it is exactly the kind of notation ambiguity the programme's own notation-registry discipline exists to prevent.
**Fix.** Rename the memory gain (e.g., γ_m) in this section.

### F18 — Paper 4 §8.3: tether threshold α unverifiable from the manuscript
**Location:** `papers/paper4_delay_dynamics/manuscript.md`, line 573.
**Quote:** "a necessary condition for a positive root is $\mu_E<\alpha:=qK\delta_0\delta/(K_0\delta_K(Z_{\rm ref}+\delta))$ ($\approx1.3\times10^{-3}$ at the illustrative parameterisation)".
**Problem.** The "illustrative parameterisation" values of δ_K, c_E, K₀ are never stated in the manuscript (only "δ_K, c_E, K₀, μ_E > 0" at line 573), so α ≈ 1.3×10⁻³ and μ_E^SN ≈ 5.9α cannot be checked or reused. The necessary-condition derivation itself is correct (F(E) ≈ E[α − μ_E] near 0).
**Fix.** Add the illustrative values of δ_K, K₀ (and c_E) in parentheses.

### F19 — Paper 3 §5.5.1–5.5.2: G3P magnitudes warrant the promised verification
**Location:** `papers/paper3_material_ledgers/manuscript.md`, lines 444, 450–457.
**Quote:** "Indo-Gangetic $-49.7$ cm/yr with index $\approx2.7$ yr; … Indo-Gangetic (N. India) | $-49.7$ | $-414$ | $\approx2.7$" (trend cm/yr, 2023 anomaly cm).
**Problem.** Basin-mean trends of ≈50 cm/yr and a basin-mean anomaly of −414 cm are an order of magnitude larger than commonly cited GRACE/G3P basin-mean rates for these basins (Indo-Gangetic basin-mean TWS decline is usually reported at a few cm/yr). The internal arithmetic is consistent (index ≈ anomaly-gap/trend is unit-free), so a systematic unit slip (mm vs cm) in the upstream source would leave the *indices* intact while the absolute magnitudes are wrong by 10×. The manuscript itself flags "the submission-stage supplement (processing files, source extracts, shared references) is pending" (line 444) — this table is the place to spend it.
**Fix.** Attach the processing files and re-verify units (cm vs mm) and basin masks before submission; if the values are as reported, add one sentence noting they are pixel-extreme-adjacent rather than typical basin means.

### F20 — Paper 2, ledger row 64: destination rendering of CC-A001-084 differs across documents
**Location:** `papers/paper2_theorem_atlas/manuscript.md` line 798 vs `papers/paper1_general_theory/manuscript.md` line 373 vs `research_program/canonical_concordance_A001_A025.csv` (row CC-A001-084).
**Quote:** P2 ledger: "Paper 1 (conditional) / Paper 2"; P1 ledger: "Paper 1 §7.3"; CSV: "Paper 1 if independent-result gate; otherwise Paper 2."
**Problem.** Three renderings of the same row's destination; "(conditional)" in Paper 2's ledger is unexplained (the row is a row-verified theorem in both papers) and could be misread as a status qualifier.
**Fix.** Use one canonical rendering (the CSV's) in both ledgers, e.g. "Paper 1 (gate-dependent) / Paper 2."

### F21 — Paper 2 §6: local notational drift R^n_{++} vs R^n_{>0}
**Location:** `papers/paper2_theorem_atlas/manuscript.md`, line 256 (R^n_{++}) vs line 309 (R^n_{>0}).
**Problem.** Both denote the strictly positive orthant; the atlas switches notation between Proposition 5.1 and Proposition 5.8.
**Fix.** Pick one symbol.

### F22 — Paper 1 §1.5/§10.1: "two scored-forecast papers" counted alongside Paper 6/7 gives an ambiguous programme inventory
**Location:** `papers/paper1_general_theory/manuscript.md`, lines 46, 333.
**Problem.** Same root cause as F09; §10.1's inventory sentence ("a five-paper assured core — … — plus two scored-forecast papers, a conditional RFDE extensions paper, and a monograph … A further conditional stage-structured and spatial extensions paper") reads as 5+2+1+1(+monograph) while the packet's inventory is 5+4+2 conditional(+monograph).
**Fix.** Resolve jointly with F09.

### F23 — Paper 5 §6.1: "Bangkok and La Mancha Oriental are the closest cases on the stabilising side" vs the La Mancha description
**Location:** `papers/paper5_sampled_governance/manuscript.md`, line 314 vs 316.
**Problem.** La Mancha Oriental is listed among the closest *stabilising* cases, but its own description says "extraction rose again in 2019–2023 to … ≈312 hm³ yr⁻¹" — a relapse, with attribution confounded. The sentence is defensible ("closest cases" ≠ eligible), but as printed the stabilising-side label and the described relapse pull against each other.
**Fix.** "…the closest cases on the stabilising side (Bangkok durably; La Mancha Oriental before its 2019–2023 relapse)…".

### F24 — Paper 3 §2.3/§3.5: the six-compartment W-row entry `(1−ρ)` vs §2.3's routing table for harvest
**Location:** `papers/paper3_material_ledgers/manuscript.md`, lines 130–141.
**Problem.** None found — the incidence matrix, its column sums, and Theorem 3.7's term-by-term cancellation all verify (checked by hand). Listed here only to record that this error-prone object was explicitly checked and is correct.

### F25 — Paper 4 §2.1/§3.1: E* / N* / Z* consistency — verified, one rounding note
**Location:** `papers/paper4_delay_dynamics/manuscript.md`, line 239.
**Problem.** N* ≈ 89.55, E* ≈ 2.090, Z* = δ ≈ 0.0693 all recompute exactly (E* = 2.08963…, N* = 89.5519…). No flaw; recorded to delimit the check. (Paper 3's companion working point 89.526/397.87 is a *different* system — the four-state working core — and is likewise consistent with Paper 4's 89.5256/397.8665.)

### F26 — Packet §1.1 status wording vs Paper 2's own length note
**Location:** `external_review_packet/README.md` line 21 ("camera-ready bibliography entry is in place") vs `papers/paper2_theorem_atlas/manuscript.md` line 850 ("The measured retained budget is ≈27.2k words at full proof expansion — above many journal main-text limits").
**Problem.** Not a contradiction (the packet does register the venue-format pass as remaining), but the packet's "camera-ready" phrasing combined with F11's uncited bibliographies overstates readiness; flagging so the venue pass addresses citations and length together.
**Fix.** In the packet, append "in-text citation hooks to be completed at the venue-format pass" or complete them now.

---

## 5. What was checked and found consistent (partial list)

So that the findings above are not mistaken for a general reliability problem, the following were verified independently and pass:

- **Paper 1 machine witness** (`research_program/paper1_instantiation/typed_false_positive_instantiation.py`): re-executed, **25/25 checks pass**; grid arithmetic exact (31³ = 29,791 states; FP = 10 × 190 = 1,900); interior witness (½, 6/5, 6/5) arithmetic correct; ρ₁ = (2−s₁)/s₂, ρ₂ = s₁/(2−s₂) and ρ₂ ≥ ρ₁ ⟺ s₁+s₂ ≥ 2 algebra correct; named-weight checks (r = ½ SLOW-only, r = 1 both, r = 2 FAST-only) consistent with the (½, 6/5, 6/5) thresholds 2/3 and 3/2.
- **Paper 4 linearization block** — recomputed from scratch at Candidate A: E* = 2.08962, N* = 89.55188; A_N = −0.017910; mobilising C_E = −0.059522, C_Z = +1.785069 (matches "+1.785"); protective C_E = −0.850336, C_Z = −1.661702 (match to 6 digits); Hopf-cubic coefficients c₂ = 0.763393, c₁ = 0.028946, c₀ = 9.28×10⁻⁶, c₂c₁−c₀ = 0.02209 (match); the even-pairs argument (B_N = −A_N/2τ_m, B_E = −A_E/2τ_m ⟹ cross term ≡ 0; H(0) > 0, cubic ⟹ 0 or 2 positive roots) is mathematically sound; Prop 5.2's phase-shift arithmetic is exact (3.666149 + π/0.0251764 = 128.374; 150.358477 − π/0.0394360 = 70.697); the 47 %/14 % gate-relocation and 3.2 %/0.2 % four-state shifts recompute; ℓ₁'s k-dependence claim (sp_k''(0) = k/4; Hopf points k-invariant at fixed δ) is correct; A.2's fold-rebuild cross-resolution agreement 2.7×10⁻¹¹ matches the printed values.
- **Paper 5** — the dimensionless-identifiability root e* = (a+√(a²+4b))/2 reproduces E* = 2.0896 at Candidate A; forward-invariance proof correct; cod assessment-table values match the A014 source exactly, including the duplicated M = 0.288 (1995 and 2005 — genuine in the source table) and every exp(−M) entry; harp-seal 3.25× and capelin 64 % recompute; T_r^NS = 47.54 consistent with Paper 4's 47.536; the two-operator discipline is applied consistently across §3.6/§6.1.
- **Paper 3** — S(α,ρ) column sums all zero; four-stock balance I_N − Q_P exact; Theorem 3.11's R* = qE*N* ≈ 0.187 recomputes (0.18716); the donor-support flux 4.652133 recomputes as 0.001 × (5050 − 397.87); Σ_reserves ≈ 0.130 yr⁻¹ recomputes (0.13044); T_resource,10% = 0.9G/C = 1,125 yr consistent with the reserves figure; the IG mean/variance and GBM first-passage parameterizations are standard and correctly stated; ψ-table values match the A018 source and the "factor of ≈1.5" trough claim recomputes (33.1/21.9 = 1.51).
- **Paper 2** — Appendix A.1/A.2 arithmetic (φ_i quadratic, coupling-creates-viability 0.31/0.10), Remark 8.15's finite counterexample (Pre_ml not monotone), Theorem 9.5's variance identity, Corollary 6.3's IG CDF at the mean, and the modular arithmetic of the 89-row ledger (63 + 7 + 19) all verify.
- **Cross-paper seams** — the deficit identity (P3 Lemma 4.3 = P4 §9 = P5 Eq. (2) input), the seam declarations (P2 ledger rows 74/75 ↔ P3 §9.1; row 82 ↔ P4 §4.3; row 85 ↔ P4 §8.1; rows 87/88 ↔ P5 §4.4), the model-version identifiers (`DYN-C3-GATED`, `DYN-C4-WORKING`, `DYN-C4-QSS`, `LEDGER-PRIM-CLOSED-v1` — consistent between P3 §8 and P4 §9), and the equilibrium/parameter values shared across Papers 3/4 are all consistent.
- **Bookkeeping** — 409 = 354 + 27 + 28 with the 27 open rows exactly A021/A022/A023; per-paper retained-row counts (21, 89, 52, 68, 57) match both the ledgers and the packet; reference counts (14, 4, 18, 37, 22) match the packet; all five `verify_retained_rows.py` self-checks exit 0.

---

## 6. Suggested fix order

1. **F01** (Paper 4 §6.1) — resolve the fold/multiplier contradiction; it touches a headline numerical claim. 
2. **F03, F06** (Paper 2) — restore the two dropped preambles (Thm 10.1's defining data; the CES specification and μ_A). Both are two-line fixes that make the atlas self-contained as claimed.
3. **F02** (Paper 2 Thm 6.4) — supply the one-line proof or relabel.
4. **F07, F09** (counts) — "nineteen sources"; "two vs four" scored-forecast papers.
5. **F11** (citations) — attach in-text hooks at the data-bearing points; heaviest in Papers 3–5.
6. **F04, F05, F08, F10** and the minors — editorial pass at camera-ready.
