# Joint Synthesis — Paper 2 Generalization Program (v2, complete)
## All audits + sub-audits + my generalization answer folded in, as-is or after correction

**What v2 adds over v1:** v1 merged the two *uploaded* files. v2 additionally folds in, item by item, **(a)** the full readability/humanization audit (Tiers 1–4), **(b)** the quantitative sub-audit numbers, and **(c)** all 8 directions of my earlier generalization answer — including 16 audit items and 4 directions that v1 had only gestured at or dropped. A complete incorporation register is in Part F.

**Sources (all cross-checked against `paper2_obstruction_calculus_v15.tex`):**
1. My readability audit — `paper2_v15_readability_humanization_audit.md` (Tiers 1–4).
2. My sub-audits — line-level grep counts (abstract length, em-dashes, redundancy counts, symbol collisions).
3. My 8-direction generalization answer (previous turn).
4. `uploads/suggested generalizations.txt` (17 proposals).
5. `uploads/qwen p2.txt` — 4 concatenated parts: (i) Qwen referee review; (ii) Qwen critique of an earlier generalizations answer; (iii) "gpt" improved pass; (iv) Qwen gap-filling follow-up.

---

# Part A — Verification results (sub-audit of the two uploaded files)

Each claim was checked against the paper and standard facts. **✓ correct · ✗ wrong · ≈ already in paper · ⚠ judgment/typo.**

| # | Claim (source) | Verdict | Evidence |
|---|---|---|---|
| 1 | "Certificates are sufficient for nonviability, not a complete 'necessity side'" (all) | **✓** | Paper's abstract: "sound sufficient conditions … do not exhaust the complement." §1.1's "necessity side" overclaims. |
| 2 | Thm 5 is a factorization fact (Qwen 3.4/1.5) | **✓** | `C∘O = 1_K` exists iff `1_K` fibre-constant. Elementary; Corollary 6 (certainly-safe set) is the valuable part. |
| 3 | Thm 1's H1.2 is messy (Qwen 3.4/1.2) | **✓** | Three-way alternative (lsc / constant / convexified-relaxed) inside the hypothesis. |
| 4 | H4.2 is heavy / hard to verify (Qwen 3.6/1.4) | **✓** | Quantifies over all blind-window open-loop controls; paper concedes "checkable in special cases." |
| 5 | Timing value `τ* = inf_u sup_{x₀,d} …` (suggested §3) | **✗ quantifier reversed** | Correct form is `σ* = sup_u inf_{x₀,d} τ`. Files contradict each other — gpt §3 and qwen-followup §6 correct it. |
| 6 | Corrected `σ*` form matches paper's H4.2 (gpt §3, qwen-fu §6) | **✓** | Paper's H4.2 is already `sup_u inf` order; value-function form is a *cleaner restatement*, not a logic fix. |
| 7 | Comparison function `D⁺q ≤ −α(q) ⟹ t_exit ≤ ∫ds/α(s)` (suggested §3/§9, gpt §3, qwen-fu §7) | **✓** | Standard; caveat (α(0)=0 with divergent ∫ ⟹ only asymptotic approach) correctly flagged. |
| 8 | Farkas `λ≥0, λᵀA=0, λᵀb<0` (suggested §4/§6, gpt §4, qwen-fu §9) | **≈ in paper** | §3.3 already states it verbatim (Farkas 1902; Gale 1960). Upgrade = normalization + worked example, not the statement. |
| 9 | Multi-floor `R_V(x)` with active set (suggested §4, gpt §4, qwen-fu §8) | **≈ in paper** | §2.2 already defines it for `m` floors. Upgrade = make it the core case + example. |
| 10 | Tube-safe `A_tube(B,Δ)=∅ ⟹ B∉ERViab` (suggested §1, qwen-fu §5) | **≈ in paper** | §2.4 + §3.3 "tube-safety form" already state it. Upgrade = the *uniform-margin lemma* (qwen-fu §5) — new. |
| 11 | Hierarchy `proj IRViab ⊆ proj ERViab ⊆ RViab ⊆ Viab` (suggested §7) | **≈ in paper** | §2.1 states the exact chain. |
| 12 | Refinement monotonicity `K_{I₂} ⊆ K_{I₁}` (suggested §2, gpt §2) | **≈ in paper (informal)** | §6.4 "refinement is never harmful." Theorem form + maximal-kernel caveat = small upgrade. |
| 13 | Greatest fixed point `νZ. Pre_Δ(Z)` (all) | **✓ with caveat** | μ/ν-calculus notation correct. But it is the **cited estimation-tube reduction** in cleaner clothes — a *re-organization*, **not new**. Must not be claimed novel. |
| 14 | Finite-horizon backward recursion sound & **complete**, obstruction tree (suggested §5, gpt §5, qwen-fu §4) | **✓ — the one genuinely new theorem** | Standard backward induction; clears the novelty threshold. |
| 15 | `Post(B,a,y)` (qwen-fu §4.1) | **⚠ typo** | `∃y∈O(x,a,d,x⁺)` should be membership `y ∈ O(x,a,d,x⁺)`. |
| 16 | `W₀ = {B ⊆ V_T}` (suggested §5) | **⚠** | Mixes terminal/safety; qwen-fu §3 corrects to `W₀ = {B ⊆ V}`. Use corrected form. |
| 17 | `T_max(B) = σ*(B)` (qwen-fu §17) | **✓** | Sup of admissible delays = `σ*(B)`. Correct. |
| 18 | Monotonicity is a **partial order**, not a chain (gpt §7, qwen-fu §16) | **✓** | Correct refinement of suggested §7. |
| 19 | "Thm 2 artificial" (Qwen 3.5/1.6) | **⚠ judgment** | Defensible; paper already frames it as "at minimal size." |
| 20 | Rename "epistemic" (Qwen 4.1) | **⚠ journal-conditional** | For SVVA/JOTA/EJC yes; for EMA keep. |
| 21 | "Appendix A off-topic" (Qwen 3.8) | **⚠ judgment** | Relabel/move; do not silently delete. |
| 22 | Abstract ≈309 words; add figures (my audit + Qwen 4.5) | **✓ / ✓** | Figure set (fibre crossing; incompatible safe controls; delayed info; CE trap) is concrete. |

**Sub-audit numbers (my line-level checks, folded here so they survive the merge):** abstract **309 words**; **157 em-dashes**; `IRViab` defined **3×** near-verbatim (L309/L465/L1219); `EViab` "contrast class / no theorem stated" **4×** (L300/L397/L403/L465); "middle ground … open" **4×**; "not proved here" **2×** (Thm 1 statement + proof); "definition, not a theorem" **2×**; `\linenumbers` **on**; "companion assessment-separation analysis" **1×** (L766); word tics: "genuine" **3×**, "exactly" **7×**, "precisely" **1×**.

---

# Part B — Per-source evaluation

**B.1 `suggested generalizations.txt`** — Good *menu*, not prioritized/deduplicated. Contains the quantifier error (§3) and `W₀` semantics mix (§5); several items already in the paper; §16 anti-decorative list is genuinely useful.

**B.2 Qwen (i) referee review** — The sharpest contribution: the **claim reframe** ("necessity side" → "one-sided sufficient nonviability certificates") and the **novelty threshold** (top venues need ≥1 of: general characterization / nontrivial converse / algorithm with guarantees / belief-space tangency theorem / example where existing methods fail). Weaknesses list verified accurate. Slightly under-credits already-present Farkas/tube/multi-floor material. Journal verdicts: reasonable but re-check scopes at submission.

**B.3 "gpt" (iii)** — Most technically disciplined. Fixes the quantifier order; insists the fixed point is a theorem *only after* specifying belief space/update/admissibility/disturbance semantics/topology; promotes finite-horizon completeness; A–E taxonomy by *what they certify*; monotonicity as partial order; non-overclaiming contribution statement.

**B.4 Qwen follow-up (iv)** — Adds the semantic-conventions layer; `Succ(B,a)` + failure symbol `⊥`; the **uniform-margin tangency→tube lemma** (real small theorem); the certificate-checking **algorithm**; the **integrated worked example**. One typo (`Post`); its 10-section architecture would nearly double the paper (trim to fit one revision cycle).

**B.5 My 8-direction answer** — The genuine-vs-decorative filter (unify / quantify / close-declared-gap / theorem-ize-a-consequence) is the right test; the files do not contradict it. Gaps the files exposed in my answer: (a) I under-pushed the claim reframe; (b) I did not hand over the finite-horizon completeness theorem as a provable-now target; (c) I under-specified the semantic conventions; (d) my #3 (σ-algebra), #7 (SOS), #8 (HJI) are covered by neither file — they remain mine, correct, and now explicitly folded into the horizon layer (D.4).

---

# Part C — Conflicts and resolutions

| Conflict | Sources | Resolution |
|---|---|---|
| Timing value-function quantifier order | suggested §3 vs gpt §3 + qwen-fu §6 | **Adopt `σ*(B₀) = sup_u inf_{x₀,d} τ`; obstruct when `σ* < T_obs`.** |
| Is the belief-space kernel new? | suggested implies yes; gpt refuses | **Present as re-formulation of the cited estimation-tube reduction.** Novelty claim limited to: finite-horizon completeness; uniform-margin lemma; obstruction tree; worked Farkas example. |
| Thm 5 status | Qwen: demote; suggested: valuable | **Demote to proposition; keep Corollary 6.** The direction that earns its place is the σ-algebra/approximate upgrade (my #3). |
| Thm 2 status | Qwen: demote | **Agree.** Example 1 (hidden mode) is primary; Thm 2 a named minimal construction. |
| "Epistemic" terminology | Qwen: rename; my audit: fine | **Journal-conditional.** |
| Appendix A | Qwen: remove/move | **Relabel / move to companion; flag to user, do not silently delete.** |
| Probabilistic | all: exclude | **Exclude; one sentence of future work.** |
| Depth vs breadth | 4 items vs 5–6 vs my 8 | **Merge into 3 layers + horizon (Part D).** |

---

# Part D — The merged synthesis (complete)

## D.0 Thesis
> *Do not add domains or mechanisms. Reorganize the paper around one rigorous object — the **belief-space viability kernel** defined by a robust predecessor operator — and present every certificate as an answer to one question: **why does this belief fail to belong to that kernel?** Add the one genuinely new theorem (finite-horizon completeness) and one worked computational exemplar, and reframe the claim from "the necessity side" to "sound, checkable nonviability certificates."*

**Filter (from my answer, kept as the standing test):** a generalization is genuine only if it (a) unifies proved mechanisms, (b) upgrades a qualitative certificate to quantitative, (c) closes a declared §6.5 gap, or (d) turns a §6.4 consequence into a theorem.

## D.1 Layer 1 — Claim reframe + rigor + style (no new math)
1. **Claim reframe.** Replace "necessity side" everywhere with "sound sufficient certificates for nonviability; equivalently, necessary conditions for observation-based viability; not a complete characterization." (Qwen §3.1/§11; audit Tier 2.)
2. **Semantic conventions subsection** (qwen-fu §1): continuous plant + sampled review; observation records (static map as special case); compatibility; policy class (belief-based = record-based under the set-membership sufficient-statistic property — *stated*, not assumed); disturbance semantics (Isaacs/state-feedback); "inadmissible action = failure" convention; strict-violation convention `q<0`.
3. **Demote** Thm 5 → Proposition (keep Corollary 6); Thm 2 → named minimal construction.
4. **Full meta-commentary cut list (audit Tier 1, all nine items, complete):**
   - `IRViab` defined 3× (L309/L465/L1219) → define **once** in §2.1; elsewhere cite §2.1. Delete both "this is a definition, not a theorem" clauses.
   - `EViab` "contrast class / no theorem stated for it" 4× (L300/L397/L403/L465) → state once; delete the other three.
   - §5 heading "**(Cited)**" → remove.
   - §5 "cited, **not reproduced**" → "proofs appear in the cited sources."
   - §1.2 "**not itself an exhibit of failure**" → delete clause.
   - §2.3 "**not re-derived here**" → delete.
   - Appendix A "**none of them is stated as a theorem of the main text**" → delete.
   - Thm 1 "locally Lipschitz … **not proved here**" stated twice (statement + proof) → state once, in the hypothesis only.
   - Header comment "**cleaned revision**" + `\linenumbers` → drop for submission (keep only if the target requires a numbered review copy).
5. **Hedging consolidation (audit Tier 2):** "sound but do not exhaust / middle ground is open" appears 4–5× (abstract L44; §5 L1040/L1067; §6.5 L1235; §7 L1260) → keep **once** in the abstract and **once** in §6.5 Limitations; delete the §5 and §7 repeats. Replace "we do not claim the underlying elementary facts … as new" (§1.3) with a positive statement of what *is* new.
6. **Symbol renames + notation (audit Tier 1 #1 + Tier 3.3 + Qwen §3.3):** delete the "some letters carry site-local meanings" paragraph; apply Qwen's renaming policy (`d`→`δ`/`γ` for patch coupling; `H`→`h` for harvest; `K`→`C`/`S` for safe set; `λ`→`μ` for Farkas multiplier; `ε`→`η`/`e_obs` for estimation error). Optionally replace the bookkeeping prose with a compact symbol table. Keep the useful "𝒥 vs ℐ — no other letter serves either role" disambiguation.
7. **Prose surgery (audit Tier 3):** cut the 157 em-dashes to appositive use only; rewrite the §2.3 a-fortiori run-on into 3 short sentences (text in the audit); break Definition 1's quantifier-order parenthetical into its own sentence; label the §2.2 "two levels of tangency" explicitly as (i) local reading / (ii) kernel reading; trim word tics ("genuine" 3×, "exactly" 7×, "precisely" 1×).
8. **Abstract ≤265 words** (now 309) + compress the §1.1 base/yield essay to one paragraph (Qwen §3.7; audit Tier 3.7).
9. **Housekeeping (audit Tier 4):** drop "companion" from "companion assessment-separation analysis" (L766) → "the assessment-separation analysis of Abaee (2026)"; code-availability: either archive on Zenodo and cite the record (consistent with paper 1) or write "No code was used or produced"; keep the data-availability statement, the brief AI declaration, and the citation style (all verified correct — no change).

## D.2 Layer 2 — The spine (the new theorem)
10. **Define the robust belief predecessor** `Pre_Δ(𝒞)` via `Succ(B,a)` + failure symbol `⊥` (qwen-fu §2): three clean requirements — common admissibility `a ∈ U^B(B)`, tube safety on [0,Δ], every successor belief in 𝒞.
11. **Finite-horizon soundness & completeness theorem** (the provable-now novelty): for finite X, A, D, Y, `B₀` admits an observation-based policy safe for N steps **iff** `B₀ ∈ W_N`; non-membership yields a **finite obstruction tree**. (suggested §5; gpt §5; qwen-fu §4; my #1's statement-level slice.)
12. **Recast every mechanism as a `Pre`-exclusion certificate**, by *what they certify* (gpt §6): **A.** Dynamic (Thm 1); **B.** Belief-action (Thm 3 + tube form); **C.** Timing (Thm 4); **D.** Certification (fibre Prop + certainly-safe set); **E.** Policy-class (CE trap — explicitly *not* an information-loss obstruction).
13. **Fix the timing layer:** `σ*(B₀) = sup_u inf_{x₀,d} τ(x₀,u,d)` (corrected quantifier order); keep constant-ε as computable special case; add the comparison-function extension with the α(0)=0 caveat. (gpt §3; qwen-fu §6–7.)
14. **Uniform-margin lemma** (qwen-fu §5): uniform `∇q_j·f ≤ −η < 0` for every common action ⟹ `A_tube(B,Δ)=∅` for all `0<Δ≤Δ*`. Closes the instantaneous-vs-tube looseness the paper leaves implicit.

## D.3 Layer 3 — Computational + design exemplars
15. **Elevate the Farkas certificate (≈ already in paper):** exact variant, normalization `‖λ‖₁=1`, and **one worked numerical example** (belief; compatible states; per-state polyhedra; stacked `Au≤b`; multiplier λ; interpretation). (qwen-fu §9.)
16. **Quantitative margins (my #2, added now):** define the **common-action gap** `g(B) = inf_{a∈U^B(B)} max_{x∈B} sup_d (−∇q(x)·f(x,a,d))₊`, prove time-to-violation as a function of `g(B)`, and state the **rescue-budget** question (how much constraint/control slack restores `g(B)=0`), with the **Farkas multiplier magnitude** `|λᵀb|/‖λᵀA‖` as the natural margin. This binds papers 1–2 into one method (assessment + obstruction with a shared margin/rescue spine).
17. **Certificate-checking algorithm box** (dynamic → finite recursion → tube → timing → fibre) + **one integrated example** (hidden modes + incompatible safe actions + delayed indicator + Farkas certificate + a refinement that removes the obstruction). (qwen-fu §14–15.)
18. **3–4 figures** (fibre crossing; incompatible safe controls; delayed information; CE trap). (Qwen §4.5.)
19. **Formalize the design layer modestly (my #4 + suggested §2/§8 + qwen-fu §11):** monotonicity as a **partial order**; static exact-certification condition `K = O⁻¹(O(K))`; one-step necessary conditions; **minimal-refinement rule** (an obstructed fibre must be split); and the **cost-minimization design problem** `min_ℐ c(ℐ) s.t. B₀ ∈ K_ℐ^Δ` — stated as a formulation with the necessary conditions, explicitly **not** claimed as a general design theory.
20. **Distance-to-viability diagnostics (my #2 + qwen-fu §17 + suggested §12):** minimal observation refinement; `T_max(B) = σ*(B)`; minimal action expansion; minimal institutional relaxation.

## D.4 Horizon directions (companion papers / outlook — not this paper)
- **Approximate/statistical certification (my #3):** fibre criterion as measurable factorization; optimal misclassification (ROC/Neyman–Pearson) when no exact certifier exists; certainly-safe set as the zero-error region. **Decision point (flag to user):** this was my #2 priority; the merge keeps the paper deterministic/set-membership and puts #3 in horizon — if a second *new theorem* beyond finite-horizon completeness is wanted cheaply, this is the one to pull into the main paper.
- **Policy-class program (my #5, added now):** a separation-failure theorem for Π_CE (for which biases b the uncorrected fixed-law class empties the kernel), landing in the Witsenhausen / non-classical-information-structure literature.
- **SOS certificates (my #7):** polynomial data → Positivstellensatz/sum-of-squares, putting *nonviability* certificates on the same computational footing as barrier certificates.
- **HJI/viscosity unification (my #8 + my #1's hard core):** certificates as viscosity sub-solutions; the "middle ground" is precisely the belief-space game value — the honest statement of the open problem.
- **Institutional multi-agent (my #6 + suggested §13):** distributed observations/commands → protocol obstruction. Only if it becomes the central theme (both files agree).

## D.5 What not to do (anti-decorative list — merged)
Chance-constrained/stochastic version (this paper); **infinite-dimensional/delay systems — explicitly deprioritized: the retarded Dini comparison is a slog, not an idea** (my answer's "least interesting gaps" verdict); general hybrid inclusions; machine-learning indicators; climate application without data/model; decentralized control as a throwaway section; any "extension" without a checkable theorem. Note: the probabilistic extension is subsumed by the σ-algebra path (D.4), so it is not a separate gap to chase.

## D.6 Preserve list (audit "what is already good" — do-not-regress guardrails)
No "In words"/"Takeaway"/"Reader's guide" artifacts (verified); §1.2 contributions list (keep); the humanizing glosses ("In management terms…", the "stock is either recovering or collapsing" skeleton); §6.4 consequences (Timing/Coarseness/Aggregation/Bias/Institutions); §6.5 Limitations (honest); the "𝒥 vs ℐ" disambiguation; full citations with DOIs and no shorthand letters; the brief AI declaration at the end.

## D.7 Merged contribution statement (unchanged from v1 — already non-overclaiming)
> *We formulate robust observation-based viability as a viability problem on a space of information states. The central object is a robust belief predecessor operator; from it we derive sound obstruction certificates for exclusion from the observation-based viability kernel — adverse-drift, common-action, delayed-information, and observation-fibre certificates. In finite-horizon finite systems, backward belief recursion is sound and complete and yields finite obstruction trees; in polyhedral one-step problems, common-action failures admit Farkas certificates. The results translate information constraints into design requirements on observation refinement, review timing, aggregation, and bias correction.*

---

# Part E — Execution plan (versioned, never overwrite)

| Revision | Contents | Sources merged |
|---|---|---|
| **v16** (claim + style) | Claim reframe; Tier-1 cut list; hedging consolidation; symbol renames; prose surgery; abstract ≤265; §1.1 compress; Tier-4 housekeeping (drop "companion"; code availability; `\linenumbers`) | Qwen (i) + audit Tiers 1–4 |
| **v17** (spine) | Semantic conventions; `Pre_Δ` + `Succ`+⊥; finite-horizon completeness + obstruction tree; A–E taxonomy; `σ*` timing + comparison function; uniform-margin lemma | gpt (iii) + qwen-fu (iv) + suggested §1/§3/§5 + my #1 |
| **v18** (computational) | Farkas worked example; **common-action gap g(B) + margins (my #2)**; algorithm box; integrated example; figures; partial-order monotonicity; cost-min design problem; distance-to-viability | qwen-fu §9/§11/§14–17 + suggested §2/§8/§12 + my #2/#4 |
| **Outlook / companion** | σ-algebra + approximate certification; Π_CE/Witsenhausen; SOS; HJI; institutional multi-agent | my #3/#5/#6/#7/#8 + suggested §13 |

**Pre-submission gate (Qwen's mock-referee list):** (1) no "necessity side" claim; (2) no overloaded symbols; (3) Thm 2/Thm 5 correctly positioned; (4) checkable timing condition; (5) explicit belief-space/estimation-tube relation; (6) Appendix A disposition decided.

---

# Part F — Complete incorporation register

## F.1 Readability-audit items → where they landed

| Audit item | Status in v2 |
|---|---|
| T1.1 IRViab 3× | **Added** — D.1.4 |
| T1.2 EViab 4× | **Added** — D.1.4 |
| T1.3 "(Cited)" heading | D.1.4 (was in v1) |
| T1.4 "cited, not reproduced" | D.1.4 (was in v1) |
| T1.5 "not itself an exhibit" | D.1.4 (was in v1) |
| T1.6 "not re-derived here" | D.1.4 (was in v1) |
| T1.7 Appendix A "none … theorem" | D.1.4 (was in v1) |
| T1.8 Lipschitz ×2 | **Added** — D.1.4 |
| T1.9 `\linenumbers`/header | **Added** — D.1.4 |
| T2.1 "middle ground" 4× | **Added** — D.1.5 |
| T2.2 "we do not claim … as new" | **Added** — D.1.5 |
| T2.3 §5 duplicate | D.1.5 (folded with T2.1) |
| T3.1 em-dashes | **Added** — D.1.7 |
| T3.2 §2.3 a-fortiori | **Added** — D.1.7 |
| T3.3 §2.4 site-local | D.1.6 (renames; table option noted) |
| T3.4 Definition 1 parenthetical | **Added** — D.1.7 |
| T3.5 §2.2 tangency labels | **Added** — D.1.7 |
| T3.6 word tics | **Added** — D.1.7 |
| T3.7 §1.1 compress | D.1.8 (was in v1) |
| T4.1 abstract ≤265 | D.1.8 (was in v1) |
| T4.2 drop "companion" | **Added** — D.1.9 |
| T4.3 code availability | **Added** — D.1.9 |
| T4.4–6 data/AI/citations OK | D.6 preserve list |
| "What is already good" | **Added** — D.6 preserve list |

## F.2 My 8 directions → where they landed

| Direction | Status in v2 |
|---|---|
| #1 taxonomy closure | **Corrected into** finite-horizon completeness (D.2.11) + hard-core-as-game-value (D.4) — full HJI characterization stays horizon |
| #2 quantitative margins | **Added (was missing in v1)** — D.3.16 (g(B), time-to-violation, Farkas-margin, rescue budget) |
| #3 σ-algebra/approximate cert | D.4 + decision point (was partially in v1; now explicit) |
| #4 monitoring design optimization | **Expanded** — D.3.19 now includes the cost-minimization design problem |
| #5 policy-class program / Witsenhausen | **Added (was missing)** — D.4 |
| #6 institutions as games | D.4 (was in v1) |
| #7 SOS | D.4 (was in v1) |
| #8 HJI | D.4 (was in v1) |
| "least interesting gaps" verdict | **Added** — D.5 (delays deprioritized; probabilistic subsumed) |
| Top-3 recommendation (#1,#3,#2) | Reconciled: #1→D.2, #2→D.3.16, #3→D.4 + explicit decision point |

## F.3 Sub-audit numbers → where used
309-word abstract (D.1.8); 157 em-dashes (D.1.7); IRViab 3× / EViab 4× / "middle ground" 4× / "not proved here" 2× (D.1.4–D.1.5); `\linenumbers` (D.1.4); "companion" 1× (D.1.9); word tics (D.1.7). All verified against v15; none dropped.

---

**Net answer to the question:** yes — 16 audit items, the sub-audit numbers, and 4 of my directions were missing or only gestured at in v1. All are now folded into v2, **as-is** where they were already correct, and **after correction** in three cases: the timing value-function quantifier order (suggested §3), the `Post` typo (qwen-fu §4.1), and the four "already in the paper" items reclassified from *add* to *elevate* (Farkas, multi-floor, tube-safe, hierarchy/monotonicity).
