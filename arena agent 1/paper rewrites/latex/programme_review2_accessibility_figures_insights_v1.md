# Programme review II — accessibility, visual aids, field insights

**Date:** September 25, 2026. **Scope:** all current editions (P1 v53 + supp v51, ws v14, comp v14, P3 v8, minimax v6, ebc v5, ARV v5, E1 v55). **Method:** figure/table inventories per tex; literature-anchor scans (viability-in-fisheries, barrier/tube/observer, max-plus); opening-section reads; signposting and running-example greps; targeted reads of every section proposed for change. Advisory only — nothing edited or pushed. Items marked ⚑ require literature verification before shipping; no citation below is to be added unverified.

---

## 1. Accessibility without dumbing down

The house style is exact-arithmetic austerity; every device below is **navigational** — it moves no claim, softens no statement, adds no interpretation. That is the non-dumbing-down test, and each proposed device passes it.

### 1.1 What already works (keep, and imitate)

- **Collected-arithmetic subsections** (comp's "Instance arithmetic, collected") — the reader gets one checkpoint where every number of the section is restated as one rational chain. The family's best device; ws's benchmark section and minimax's benchmark are the natural next carriers.
- **Anchor openings** — ebc's "two working disciplines… evaluate exactly where you probe" and P3's "necessity side / sufficiency side" openings state the paper's discipline in two sentences. minimax's opening ("certificates are emptiness statements") is the same species.
- **Falsified-variant displays** (comp's 2719/1250, 2501/1250, 103/50 entries) — showing the wrong policy alongside the right one teaches the mechanism; ARV's Proposition~`prop:discrimination` (the reference point fails to separate the eras) does the same work in words.
- **P3's seven-step map** ("The development proceeds in seven steps. Section \ref{model} states…") — the family's only true roadmap, and the model to copy.
- **Master tables** (ws) and **the coverage audit** (P1 §9): the reader can check every count in one place.

### 1.2 Gaps and devices (ranked; all navigational)

1. **Per-paper notation tables with family collision rows.** The symbol-collision table from Review I stands unexecuted (Γ, λ, μ, K, ρ, β, τ\* all carry paper-local meanings; minimax uses K three ways internally). A short "Shared symbols" block in each paper's notation front matter — including a one-line pointer per symbol that differs across companions — is the single highest-value accessibility item. Content cost: zero.
2. **Named running instance at first mention.** Every theory paper has a de facto running instance (P1/supp: the two-floor conflict; comp + minimax: the three-branch delayed-observation braking system; ws + minimax: the caps-fibre benchmark; ebc: the four-parameter cube; ARV/E1: 2J3KL). One clause at first mention — "the running instance of this paper is X (Section \ref{…})" — lets a reader build one mental model instead of re-deriving orientation at Section 6. Cost: one clause per paper.
3. **Hypothesis lists for the long single-sentence theorems.** comp's bridge theorem states six hypotheses inside one sentence with a heavy parenthetical (the L¹ clause). A hypothesis list environment (H1–H6, same words) would be referee-friendly and screen-readable without touching a word of content. minimax's Theorem `thm:general` setup and ws's master theorem's three-axis hypothesis deserve the same treatment if their current forms drew audit friction (they did not — so this is optional, comp first).
4. **Uniform verification triple.** Every Verification section states script · count · arithmetic, but in varying order and typography. One fixed display (a three-column mini-table or a fixed sentence pattern) family-wide makes the assurance claim scannable and comparable.
5. **minimax: reorder so the theorem leads.** Still pending from Review I (§3.2): the measure-dual theorem is the paper's result but arrives after the candidate-failure narration; §2-first ordering, with the three obstructions as motivation for the dynamic layer, matches the paper's actual logic. Fold into the next minimax edition.
6. **Contribution-list parity.** P1 and comp carry contributions lists; ws, minimax, ebc, P3, ARV, E1 rely on openings alone (P3's map partially covers it). A three-item contribution list per theory paper — same register as comp's — is cheap and helps skimming referees. Optional; openings are already strong.

### 1.3 What NOT to do

No simplified "informal statements" before theorems (the statements are already plain); no expository footnotes explaining undergraduate mathematics (Farkas, Helly, total variation are the audience's vocabulary at the target venues); no intuition boxes that restate proofs in words (the falsified-variant displays already do this with content). The papers' austerity is a feature at Automatica/SCL/TAC/Math-OR/CJFAS; the accessibility wins are all wayfinding.

---

## 2. Figures, tables, visual aids — merits adjudicated per paper

Discipline for any new figure: script-generated with verifier assertions (the ws recompute-then-assert rule), vector PDF, exact rationals annotated at every plotted feature, archived with the paper. A figure that displays only numbers already in tables is decorative and is rejected under that rule; every candidate below carries structure the text cannot show.

| Paper | Current visual inventory | Verdict |
|---|---|---|
| P1 + supp | 3 + 4 figures, 3 + 1 tables (coverage audit, case study) | **Adequate — nothing merited.** |
| ws v14 | 5 figures (kernels, benchmark, duality, census, timing), 6 tables | **Adequate — nothing merited.** The best-equipped paper; fig_kernels already shows the monotonicity structure. |
| comp v14 | **0 figures**, 1 table | **Two figures merited** (below). The most geometric story in the programme — braking trajectories, a hexagon, mesh refinement, a delay hierarchy — with no visual. |
| minimax v6 | **0 figures, 0 tables** | **One table merited, one figure borderline** (below). |
| P3 v8 | 5 figures (staircase, masses, classdiff, deadline, twofloor), 3 tables | **Adequate — nothing merited.** (All five point into `figs_bs2/` — the directory is P3's, not ebc's; correcting Review I's implicit assumption.) |
| ebc v5 | **0 figures, 0 tables** across all editions v1–v5 (checked — no content loss; figure-free by design) | **One table merited** (below); figures would duplicate P3's. |
| ARV v5 | **0 figures**, 3 tables | **One figure merited** (below) — the programme's most visual dataset with no visual. |
| E1 v55 | 6 figures, 2 tables | **Adequate — nothing merited.** |

**comp (both):**
1. *Three-branch trajectory certificate.* The four printed policies (triple blind-window, pairs {1,2}/{2,3}, the falsified variants) as position-vs-time curves on [0, 6/5] with the floor 2, the peaks 93/50, 12345/6250, 2419/1250, 2719/1250, 2501/1250 annotated as exact rationals, and the slacks 31/1250 and 81/1250 marked. Every curve is piecewise-rational with closed forms already in the verifier — the figure is the certificate, drawn; nothing new is claimed.
2. *The delay hierarchy.* Γ(τ) = τ − 7/50 (and the dilated family Γ_a(τ) = τ − 7/50 − (a−1)/2 from `prop:redesign`) against the three rungs τ\* = 7/50, (15−√183)/6, (10−√58)/6 and the singleton unbounded line: the paper's headline structure (authority shifts the intercept, timing shifts the crossing) becomes visible in one panel. All quantities are verified closed forms.
3. Optional third: a *redesign-rates mini-table* (lever × rate: timing 1, post-revelation authority 1/2, shared window 0, velocity budget 0) — three rows restating `prop:redesign`'s ordering sentence; include only if the two figures land without page pressure.

**minimax:** a *theorem-to-check-family table* (six rows G1–G6: family × statement certified × count), giving the paper its first at-a-glance verification map — genuine navigation, zero content. The coupling-selection tree (the two-window instance's product vs comonotone coupling over four atoms, values 0 vs +1) is the one figure candidate: borderline because the object is small, merited because the coupling-selection residue is the paper's central open problem and currently purely verbal. Owner's call; default lean yes.

**ebc:** a *classification summary table* — the paper's census results (16 singleton survivors, exactly the 32 Hamming-adjacent pairs, nothing larger; the ten ladder values; the deadline boundary) as one table. The paper currently makes readers reconstruct its headline structure from prose; the numbers are all script-certified already.

**ARV:** *the certified record figure* — both vintages' readings 1983–2021 against the two thresholds (276, 884.6 kt), the reference and collapse windows shaded, the 1993 breach and the 2015 re-crossing marked, exact kt values annotated at the certified features. Every plotted value is a locked-file integer; the figure would display the paper's own propositions (windows, breach, discrimination, recovery) in one view. Highest visual merit in the programme after comp's.

---

## 3. Ecological, control-theory, systems-theory insights — merits adjudicated

### 3.1 What the scan shows

P1's sufficiency landscape already carries the family's external anchoring: Doyen (7×), De Lara (3×), Martinet (1×), Aubin (14×), Saint-Pierre/Quincampoix (10×), barrier certificates and Prajna (15/6×), tube/MPC (32×), observer/Kalman (3×), Clark (2×). comp carries light but sufficient anchors (Aubin 2×, Saint-Pierre 2×). ws uses "max-plus" as a method name with **no citation to the max-plus literature**; minimax now has a reference list but **no external standard-result citations at all** (LP duality, basic solutions, Helly are invoked by name); ARV cites **no ecological literature whatsoever** (data sources and companions only); E1's ecological content is already carried and correctly scoped (depensation term 𝔰 active/inactive, Shelton & Healey 1999, the explicit "does not estimate an Allee threshold" delimitation).

### 3.2 Merited items (ranked; each small, each verified-before-ship)

1. **minimax standard-result citations (⚑ verify then ship).** The proof-bar constraint ("standard results cited") currently fails in minimax: the finite-reduction/LP-duality/basic-solution route and the Helly-type sparsity bound rest on classical results cited nowhere. Add the standard sources (linear programming duality and basic-solution theory; Helly's theorem; the measure-theoretic minimax anchors already identified in the programme's earlier scans). This is compliance, not decoration.
2. **ws max-plus anchor (⚑).** One citation at first use of "max-plus recursion" (the classical max-plus-algebra reference after edition verification). SCL referees will expect the term anchored.
3. **ARV collapse-recovery context sentence (⚑, owner's call).** The outcome years document a genuine asymmetry — certified removals cannot explain the way up, twenty years below half the reference point — and ARV cites none of the collapse-recovery literature its CJFAS referees know first-hand. One sentence anchoring the asymmetry (Hutchings-type references after verification) is substantive framing, not decoration. Tension to weigh: ARV is standalone-from-birth by design; the sentence touches no result.
4. **comp belief-cell ↔ certified-observer anchor (⚑, candidate).** `prop:beliefcells` is structurally a set-valued observer with a certified error radius; comp currently makes the observer connection only in prose ("adding observers"). One sentence with a verified set-membership-estimation anchor would position the proposition for the control audience. Optional; only after literature verification.
5. **Barrier-certificate correspondence:** P1 already carries the barrier/Prajna treatment (15/6 mentions); comp's dual firing a Farkas contradiction is the finitely-sampled relative. A cross-reference sentence comp→P1's discussion is available but **not recommended now** — comp's certificate is a dual label bound, not a barrier function, and a sentence claiming correspondence would need its own scoped proposition to be honest. Declined under the merit bar.

### 3.3 Verdict on new theorem-grade insights

**None merited at this stage.** The candidates I tested and rejected: formalizing ARV's recovery asymmetry as a two-threshold hysteresis model (the locked files certify comparisons, not the estimation a formal model requires — out of scope by the data-provenance discipline); a general max-plus duality theorem in ws (would re-prove P1's attributed Theorem 1 ground); an ecological viability-kernel section in ARV (P1 owns the viability-application literature; duplicating it would be the duplication hazard again). The family's insight density is already high — ws's factoring and stationary-policy propositions, comp's redesign rates and belief cells, minimax's tower and coupling orthogonality, ebc's Hamming-regime separation are this cycle's new theory. The remaining merited "insights" are anchoring and framing, listed above.

---

## 4. Proposed sequence if executed (owner to adjudicate)

1. **Round 26a — visual round:** comp's two figures + optional rates table (script + verifier assertions + gates), minimax's check-family table, ebc's classification table, ARV's certified-record figure (script reads the locked CSVs, asserts every annotated value). Edition bumps: comp v15, minimax v7, ebc v6, ARV v6; ws/E1 untouched.
2. **Round 26b — anchoring round (⚑ items after literature verification):** minimax standard citations, ws max-plus anchor, ARV context sentence (if owner approves the standalone tension), optional comp observer anchor. Can share the 26a editions if sequenced together.
3. **Presentation items** (notation tables, running-instance clauses, minimax reorder, hypothesis list, verification triple): fold into the same edition bumps or a dedicated pass; zero-risk edits, full gates either way.


---

## Execution outcomes (round 26, September 25, 2026)

Shipped as adjudicated: comp figures (trajectories + hierarchy, script
asserted 10/10) and bridge-hypothesis itemization H1–H6; minimax
check-family table G1–G6 with Chvátal 1983 and Helly 1923; ebc
classification table; ARV certified-record figure (11/11 asserted),
NCAM expansion, Hutchings–Myers 1994 sentence; ws Baccelli et al. 1992
anchor and DP expansion; the flow scan's objective fixes (LP
introduced in comp; NCAM/LRP expanded in E1 v56); Milanese et al. 1996
observer anchor in comp.

Final calls at execution: minimax coupling-tree figure declined
(plots two already-asserted values — decorative); comp rates table
declined (duplicates one exact sentence); E1 expanded rather than
deferred (same objective-fix class as the other papers). Review I's
minimax reorder finding withdrawn after verification against the
shipped tex (§2 already opens with the measure dual).

Gates: all six new editions verifier-green, build-green (zero
overfull, zero unresolved refs), byte-identical pinned rebuilds;
content-loss audit clean; map round-26 rows updated.

### Post-hoc verification appendix (review III, September 26, 2026)

Section 3.3's rationale for declining the general max-plus duality theorem in ws — "would re-prove P1's attributed Theorem 1 ground" — is retracted as mis-premised: P1 v53 contains no max-plus content (zero hits; its eight theorems are soundness/completeness, common-action obstruction, delayed-information, LP instantiation, exit certificate, and three further theorems). The decline stands on verified grounds: no shipped ws claim needs a general theorem (the regime-graph recursion is certified exactly, check P21); ws's scope is certified instances and the general algebra is now cited (Baccelli et al., 1992, ws v15) rather than re-proved; a new general theorem would add a proof burden and an owner question with no claim-level payoff. ws has no conjecture apparatus, so an "extension" would require new section-grade machinery to be honest. Full adjudication: `programme_review3_declined_additions_adjudication_v1.md`. The hysteresis and viability-kernel rationales were verified and stand as recorded.
