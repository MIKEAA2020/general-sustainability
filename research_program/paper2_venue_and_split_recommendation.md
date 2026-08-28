# Paper 2 Venue and Split Recommendation

**Status:** Decision memo (internal planning document; not a manuscript). Resolves the open item "Paper 2 venue/split decision" (worklog Task 56 next-candidates; `remaining_obstacles_to_general_theory.md` priority item 7's open clause; the B-1 routing in `pending_separate_publications_register.md`).
**Subject:** `papers/paper2_theorem_atlas/manuscript.md` — the theorem atlas, Paper 2 of the five-paper architecture.
**Decision owner:** programme owner. **Prepared:** 2026-08-28. No theorem status is created, promoted, or demoted by anything in this memo.

---

## 1. The decision to be made

Two coupled decisions, both recorded as open:

1. **Venue.** Which journal receives the theorem atlas. The manuscript's own length constraint (§15) defers this to "venue-policy check, not now"; the content budget (`paper2_theorem_atlas_content_budget.md`, "Quantitative gate") requires recording the target venue's word/page policy and evaluating `L_total ≤ L_target` with a ≥10% revision buffer.
2. **Split or not.** Whether the atlas is submitted as one paper or split into the pre-authorized **2A/2B** pair ("Authorized split trigger" in the content budget). The split decision carries the **B-1 routing**: the delegated F08/F10 families in `pending_separate_publications_register.md` (Class B) are "the natural 2B core" if the split opens, and stay monograph-carried if the single-paper venue holds.

## 2. What the atlas is

**Section map** (all claims verifiable in the manuscript):

- **§1 Introduction** — the atlas question (§1.1), the six selection rules (§1.2), the claim-status hierarchy with the no-promotion/no-silent-transfer rules (§1.3), provenance (§1.4), the five-paper relationship (§1.5: the monograph "reintegrates everything at full length").
- **§2 Preliminaries** — the typed canonical framework: six definitions (type system, hybrid specialization, canonical tuple, uncertainty levels, diagnostic types, threshold/intergenerational types), notation bridges, and the informational hierarchy IRViab ⊆ K_I ⊆ RViab ⊆ Viab (§2.7).
- **§3 Core viability and obstruction calculus (F13)** — monotonicity, product structure, face- vs kernel-necessity, the finite-time exit certificate ("the obstruction engine of the whole atlas"), stability ≠ safety.
- **§4 Typed conservation and physical admissibility (F01)** — hybrid conservation, positive-moiety bound, non-negative invariance across ordinary/hybrid/RFDE modes, donor limitation, the conditional BIBS criterion, geological noninvariance.
- **§5 Noncompensation and substitution feasibility (F02)** — domain-qualified noncompensation, CES substitution thresholds, essentiality, support gaps, the Farkas alternative, three witness/no-scalar families.
- **§6 Observation and epistemic viability (F03)** — the central negative results: epistemic emptiness, observer transfer, the strong-invariance certificate, common-action/delayed-information obstructions, observation-fibre certifiers, aliasing, safe learning (15 rows, second-largest family).
- **§7 Recovery and irreversibility (F04)** — capture-basin identity, vanishing recovery resilience, envelope-relative recovery, robust informational capture basins, typed irreversibility.
- **§8 Sampled, hybrid, and information-state kernels (F05)** — the largest family (14 rows): sampled robust kernels, finite-clopen observation kernels, held-control tubes, inter-sample safety, the two RFDE kernels (destined to Paper 4), information-state kernels, sample-and-hold convergence, the selector ladder, the memoryless counterexample.
- **§9 Projectability and exact reduction (F06)** — four model maps, the semiconjugacy criterion, fibre obstruction, logistic reductions, variance correction, the five-state reduction conjecture.
- **§10 Diagnostics and delay certificates (F07)** — local-horizon bracket, small-gain delay-independent stability (destined to Paper 4), the two audit-template algebra rows.
- **§11 Restricted composition and coupling (F10)** — the compositional viability theorem (one row).
- **§12 Institutional implementation (F11)** — institutional equivalence and viability condition, the H3 hypothesis object, the epistemic-institutional kernel recursion, the solvency-index negative record.
- **§13 Intergenerational and stochastic bounds (F12)** — nested-constraint impossibility, finite-horizon small-noise viability, the stochastic horizon split, the justice/multiscale programme.
- **Appendix A** — the two coupling constructions (MSY emptiness; coupling creates viability) and three scope remarks.
- **§14 Status ledger; §15 Provenance, reproducibility, and limits; References.**

**Ledger composition (§14).** 89 concordance rows: 70 budgeted (63 main + 7 bounded-appendix) plus 19 closure-campaign seam rows, every one `row_verified` across nine closed sources (A001, A002 primary; A003, A005, A006, A007, A010, A013, A018 seams; §15 "Sources"). Claim statuses: 31 theorems, 18 definitions, 8 conditional theorems; the remainder propositions/lemmas/examples/counterexamples/remarks, one conjecture (Conj 9.6), one open research programme (Prog 13.3) — each at its source-declared status. Eight further manuscript-native entries (MS-Native-1..8) carry no concordance row; several of rows 71–89 are seam-annotated to Papers 3/4/5.

**Length and proof density.** The manuscript as drafted measures ≈15.4k words, with proofs *reproduced* where short (§3's four theorems, Prop 7.7, Thm 11.1) and *verified present; summary* otherwise; one proof is omitted in the source with a registered one-step proof obligation (Thm 6.4; §15 "Proof handling"). The §15 length constraint states the measured retained budget: **≈27.2k words at full proof expansion** (camera-ready reproduces every proof verbatim). The programme's planning default for ordinary mathematics articles is ≈8–15k words main text, with proofs routinely moved to electronic supplementary material (`content_retention_and_length_budget_A001_A025.md` §4).

**The B-1 pending families.** Class B item B-1 routes twelve `row_verified` concordance rows currently tier `delegated` in `paper2_retained_row_budget.csv`: the scalar resource–sink and Allee kernel families (CC-A001-037/-038/-039/-040/-041/-043), the patch-algebra family including the corrected non-polyhedrality conjecture with its proved local-curvature certificate (CC-A001-057/-058/-059), and the cascade-containment family with the spectral-radius antitheorem (CC-A001-061/-064/-065). All are monograph-carried at compressed forms (monograph §15A). At the budget's measured per-row economics (20,146 located source words for 70 rows, plus the 35% connective allowance), absorbing these theorem-dense families adds roughly 6–9k words — an estimated ≈**33–35k words** at full proof expansion.

## 3. Venue analysis

Norms below are planning-typical; the operative step remains the per-venue policy check the content budget mandates at submission time.

| Venue | Scope fit (viability + typed applications) | Length accommodation | Audience | Assessment |
|---|---|---|---|---|
| **Set-Valued and Variational Analysis (SVVA)** | Core. Kernels, tangency/Nagumo conditions, capture basins, differential inclusions, invariance under uncertainty are the journal's home territory; typed sustainability applications fit its applications scope | No hard page cap; extended articles routine; Springer ESM allowed. Main text ≈14–16k words with proofs in ESM is comfortable | The viability/set-valued community — the domain experts for this proof corpus | **Primary candidate** |
| **J. Mathematical Analysis and Applications (JMAA)** | Good. Control theory, differential inclusions, applied analysis appear; viability less central than at SVVA | No explicit page limit; long articles routine; supplementary accepted | Broad analysts | **Alternate single-paper venue** |
| **J. Optimization Theory and Applications (JOTA)** | Moderate: invariance/capturability has appeared historically; the atlas is not optimization-shaped | Longer articles acceptable | Optimizers/control | Backup; scope framing would need rework |
| **Systems & Control Letters** | Good (invariance, constrained control, sampled systems) | Poor: short-paper format (typically ≈8–12 typeset pages) | Control theorists | Not feasible: even a split half exceeds the format; would force destructive condensation |
| **Automatica** | Partial: sampled-data and delay families (F05/F07) fit; the ledger/status apparatus and typed framing are off-register | Poor: nominal ≈10-page regular-paper limit | Control engineers/theorists | Not feasible for the atlas; marginal even for a split half |
| **IEEE Trans. Automatic Control** | Partial: invariance-adjacent, but viability corpus rare and sustainability register foreign | Poor: ≈16-page submission ceiling for full papers | Control theorists | Not feasible |
| **Mathematical Methods in the Applied Sciences** | Good: applied ODE/control/methods with applications | Flexible; 20–45-page papers common; supporting information allowed | Applied mathematicians | Viable fallback, especially for an applications-flavoured 2B |
| **Ecological Modelling** | Poor: referee expertise is ecological modelling, not viability proofs; the atlas's ecological content is definitional (the domain applications are owned by Papers 3–5) | ≈6–10k words | Ecologists | Not feasible: proof corpus would not be competently refereed |
| **Theoretical Ecology** | Poor: same mismatch; expects ecological theory with models/results | Short-to-medium | Ecologists | Not feasible |
| **American Mathematical Monthly** | Not suitable: (i) an expository journal for the general mathematical community, not a primary-research venue for a specialized 89-row proof corpus; (ii) length norms (most articles under ~15 pages) and an undergraduate-accessible register cannot host dense viability/RFDE material plus a provenance ledger; (iii) generalist referees defeat the domain-expert requirement | n/a | General mathematical readership | Excluded |
| **Monograph route (Birkhäuser Systems & Control series / Springer LNM)** | Excellent (Aubin's *Viability Theory* itself is Birkhäuser SCFA); a 33–35k-word full-proof atlas + B-1 is a legitimate compact research monograph | No limit | Research specialists | **Not now**: it would invert the sequencing rule (journal-level external scrutiny precedes the monograph — priority item 8), duplicate the definitive monograph's retention role, and remove the corpus from journal review. Last resort only |

## 4. Split analysis

**Available seams.** A theory-vs-applications seam does not exist: the atlas has no applications section — the domain applications are owned by Papers 3–5, and the atlas's rows carry primary-destination cross-references instead (§1.2). Two candidate cuts remain:

**(a) Static/structural vs dynamic/stochastic.** Rejected. It cuts *through* family F03 (§6 mixes static certifier results — Def 6.9, Thm 6.10, Cor 6.11, Lem 6.14 — with dynamic obstruction theorems 6.1–6.8), and it severs the §6 → §8 → §12 arc (epistemic kernels → information-state kernels → institutional kernels) along which the informational hierarchy of §2.7 is read.

**(b) The pre-authorized question seam (content budget, "Authorized split trigger").** Viable, and the only coherent cut:

- **2A — Typed viability under observation and implementation** (§2 preliminaries, §3 calculus minus the product-structure cluster, §4 conservation, §6 observation/epistemic, §7 recovery, §8 sampled kernels, §12 institutional implementation, §13.2 + Remark 13.4, App A.3/A.5): **62 of the 89 rows** (6+4+6+15+8+14+6+1+2). MS-Native-1, -3, -4, -5, -6, -7, -8 accompany it.
- **2B — Projectability, noncompensation, substitution, and composition limits** (the Thm 3.2 product-structure cluster, §5, §9, §10, §11, §13.1 + Prog 13.3, App A.1/A.2/A.4): **27 rows** (1+8+8+4+1+2+3), with MS-Native-2 — the content budget itself assigns 2B the "coupling destruction/rescue and limit counterexamples," so the Thm 3.2 + A.1/A.2 cluster travels intact within 2B (it is referenced from Thm 3.2's own statement and §11's closing text, both in 2B).

Both halves are self-contained on the atlas's own criteria: each has its own question, complete assumptions, and per-row proofs. The one qualification is the preliminaries block, quantified next.

**Cross-reference burden.** The genuinely shared rows are the preliminaries block: 2B needs Def 2.1 (type system), Def 2.5 (diagnostic types), and Def 2.6 (threshold types) for its §10 — **3 of the 89 rows**, rising toward 9 if 2B restates the whole §2/§2.7 apparatus. Under the exactly-once ledger rule these stay in 2A's ledger; 2B either (i) restates the definitions it needs as a Minimal Working Realization without CC identifiers — the established Papers 3–5 pattern, consistent with the architecture's citation-closure rule — or (ii) cites 2A's published versions as stably available results, which imposes a **submission-order constraint**: 2B cannot precede 2A's acceptance. No later section invokes Thm 3.4 by number (the §3 "obstruction engine" sentence is framing prose), and the Thm 3.2 + A.1/A.2 cluster sits wholly in 2B, so neither half needs the other's theorems as load-bearing inputs.

**B-1 routing consequence.** Under the split, B-1's twelve F08/F10 rows enter 2B (the register names them "the natural 2B core"): 2B becomes ≈39 rows; at the budget's ≈300 words/row economics, each half lands in the ≈14–19k range (2A ≈62 rows; 2B ≈27 + 12 B-1 rows, the B-1 families proof-dense). Both sit inside single-article norms for SVVA/JMAA/MMAS with ESM proofs. All twelve rows are `row_verified`; CC-A001-057 enters at its corrected conditional/conjecture status — the split creates no status change.

**Risks of the split.** (i) Three to nine preliminaries rows are duplicated or cross-cited, weakening the "stated once" principle (§1.1: the atlas exists because "duplicate statements mask genuine differences in assumptions"). (ii) The unified framing is lost: §3 presents its four results as "the calculus every later family uses," a claim only the single paper can make literally. (iii) Two referee processes instead of one unified external review before the monograph. (iv) Register churn: per-paper budgets and self-checks must be created. Against these, the split buys ~10k words of headroom and journal publication of B-1 — headroom needed only if both single-paper venues fail their policy check.

## 5. Recommendation

**Primary recommendation — no split; submit the full atlas to Set-Valued and Variational Analysis, with JMAA as the immediate alternate if SVVA declines on scope or length.**

(i) **Venue and submission order.** One submission, SVVA first: its scope is the corpus's home territory (F13, F03, F05, F04, F10 — the viability/set-valued core), and its referee pool is the domain-expert readership the owner requires; the typed sustainability applications fit its applications scope. If SVVA's policy check or editorial response fails, JMAA takes the same package unchanged.

(ii) **Where F08/F10 land.** B-1 stays **monograph-carried**, per the register's own conditional: "If the single-paper venue holds, they stay monograph-carried." The twelve rows remain tier `delegated` with their monograph-chapter destinations; nothing is lost (non-loss rule), and the definitive monograph restates them at full length.

(iii) **The 89-row ledger.** Unchanged: one paper, one ledger, `verify_retained_rows.py` runs as-is (89 cited = retained exactly, ledger complete, exit 0). No per-paper budget is needed.

(iv) **Length handling.** Main text carries statements, the claim-status discipline, the reproduced short proofs, the ledger, and §15 — ≈14–16k words; the camera-ready verbatim proof reproductions (the ≈27.2k-word full expansion) go to **electronic supplementary material**, which SVVA (Springer ESM) and JMAA both allow; the full-length version additionally lives permanently as the repository/preprint copy, per the length budget's preprint layer. The content budget's quantitative gate then reads: L_total(main text) ≈ 14–16k ≤ L_target(SVVA long-article norm ≈ 20k+) with the ≥10% revision buffer intact — the gate passes and the split trigger is not fired.

**Fallback (only if both SVVA and JMAA fail the policy check or reject on length):** execute the pre-authorized 2A/2B split. Submit **2A first** (SVVA or JMAA) — it owns the preliminaries; after 2A's acceptance, submit **2B** (JMAA or MMAS) with B-1's twelve rows absorbed into its budget (re-tiered from `delegated` to `main` at their verified statuses; CC-A001-057 stays at its corrected conjecture status — no promotion), carrying a Minimal Working Realization of Def 2.1/2.5/2.6 and citing 2A's published versions as stably available results. The 89 rows partition 62/27 (each row cited exactly once across the two ledgers), MS-Native-1..8 split 7/1, and `verify_retained_rows.py` is instantiated per paper against per-paper budget files (`paper2a_…`/`paper2b_…`) with the B-1 IDs added to 2B's retained set.

**Rationale for the primary.** (1) The architecture's objective is "minimize fragmentation subject to complete substantive retention"; the split trigger is conditional on a length failure, and SVVA/JMAA accommodate the atlas. (2) The atlas's identity is "in one refereable unit" (Abstract) — the split duplicates the preliminaries block and forfeits the unified framing for headroom that is not needed. (3) One unified external review of the whole proof corpus is the best preparation for the monograph, which reabsorbs everything at full length regardless of route. (4) All non-negotiables hold without change: no theorem-status promotion (statuses travel verbatim), the monograph's reabsorption is untouched, external scrutiny precedes the monograph, and the domain-expert reader requirement is met precisely at SVVA.

## 6. Consequences register (if the primary recommendation is adopted)

1. **`pending_separate_publications_register.md` — B-1 closed:** the routing decision resolves to "single-paper venue holds; F08/F10 stay monograph-carried"; the entry is marked resolved with the corrected-forms status-discipline note retained (the non-polyhedrality conjecture status, the H_safe-dependent restatements).
2. **`remaining_obstacles_to_general_theory.md` — priority item 7:** the open clause "the venue decision and the 2A/2B split trigger remain open at the length gate" resolves to: venue SVVA (alternate JMAA), no split, B-1 monograph-carried. The **camera-ready references** were completed for all five core papers in the 2026-08-28 editorial pass; item 8 (monograph after external scrutiny) is unchanged — the SVVA submission *is* the scrutiny step for this corpus.
3. **`revised_optimal_publication_architecture_A001_A025.md`:** Paper 2's entry gains the venue decision; the Wave 1 release protocol (release/submit Paper 2 passing its own gate) executes; the assured count stays five (no sixth paper created).
4. **`paper2_theorem_atlas_content_budget.md`:** the quantitative gate is evaluated against the recorded SVVA policy — PASS with ESM proofs and the revision buffer; the "Current conclusion" paragraph is updated with a dated decision note (split trigger not fired).
5. **`paper2_retained_row_budget.csv` / `verify_retained_rows.py`:** unchanged (89-row retained set intact; B-1 rows remain `delegated`).
6. **Manuscript work implied (not authorized by this memo):** the venue-format pass (SVVA template, ESM packaging of the camera-ready proofs, the registered Thm 6.4 one-step proof obligation). The camera-ready reference list was completed in the 2026-08-28 editorial pass.
