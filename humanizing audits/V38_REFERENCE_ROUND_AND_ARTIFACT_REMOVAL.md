# v38: the reference round + the artifact-class removal

- **Round:** Task 97, 2026-09-18. Owner directive: *"1- v38 reference round, the retitle, the DOI list. 2- check for and remove change-long diary, meta-commentary, self-referential, internal dialogue, informal chat artifacts, etc."*
- **Baseline:** `paper4_delay_dynamics_v37.md` (md5 `f32ef08f15fc3fdfacdc041d6d15a51b`), 45 pp, 1 figure, 36 references (frozen v32==…==v37), abstract 258 journal words, supplementary `paper4_supplementary_v6.md`.
- **Deliverables this round:** `paper4_delay_dynamics_v38.md` (+ tex/pdf), `paper4_supplementary_v7.md`, the refreshed package `submission_zips/paper4_supplementary_v7.zip`, and this record. New files only; v37 and every prior version untouched on disk and in history.

---

## Part I — directive 1: the v38 reference round

The Task-96 recommendation (`V37_JOURNAL_FIT_EVALUATION.md`, Part V) is now commissioned and executed exactly as specified:

1. **Adamson & Hilker (2020) added at §1.1's lineage paragraph** — the missing delayed-knowledge modelling link between Moxnes (1998) and Ostrom (1990):
   > "The modelling counterpart treats the delay as one of knowledge: delayed knowledge of the harvested population state destabilises bioeconomic equilibria and induces resource-harvester cycles, which harvester forecasting can dampen (Adamson and Hilker, 2020)."

   The sentence uses their own title terms ("delayed knowledge of the harvested population state"; "harvester forecasting"; "can dampen" — the modal from their title) and claims exactly what their paper shows. The one **echo** Task 96 marked optional is added at §11.2, appended to the existing echo sentence (Åström–Wittenmark / Ostrom):
   > "Where harvester forecasting can dampen the cycles induced by delayed knowledge of the harvested population state (Adamson and Hilker, 2020), the review interval is the design variable analysed here."

   This is the knowledge-delay/governance-delay pairing that Task 96 identified as "the exact novelty boundary of the paper" — their forecasting-damping versus this paper's cadence control — placed where the design message lives. Non-decorative: it positions the contribution against the closest precedent in the paper's own terms.

2. **Hocherman, Trop & Ghermandi (2025) added and cited at the three "documented 2–13 yr governance-lag distribution" sites** (§9.3, §11.4, §11.7), resolving the dangling source found in Task 96 (the supplement's S4 cited "the Hocherman (2025) synthesis of 101 studies" while the main reference list had no Hocherman entry and no supplementary reference section existed).

   **The full record, pinned this round by web search** (2026-09-18; independent corroboration — Springer's article page `link.springer.com/article/10.1007/s13280-025-02211-y`, PubMed `40610782` ("Ambio. 2025 Dec;54(12):2042-2059. doi: 10.1007/s13280-025-02211-y. Epub 2025 Jul 3"), PMC `PMC12569336`, the University of Haifa release naming all three authors, Semantic Scholar):
   > Hocherman, T., Trop, T., Ghermandi, A., 2025. Time lags in environmental governance: a critical review. Ambio 54(12), 2042–2059. doi:10.1007/s13280-025-02211-y

   **Three authors, not one.** The supplement's S4 citation form was corrected to the house style ("the Hocherman, Trop, and Ghermandi (2025) synthesis") to match the new reference entry — the paper's own convention being full listing for three authors (Li, Bence, and Brenden, 2016) and *et al.* only for four or more.

   The Adamson & Hilker entry is byte-stable from the Task-96 verification (five independent sources): Theoretical Ecology **13**, 425–434, doi:10.1007/s12080-020-00462-x.

3. **References 36 → 38**; the frozen-reference gates re-baselined (v38 == v37 + the two declared insertions; v32==…==v37 remains frozen at 36). The insertion points follow the list's own ordering (Adamson after Åström and before Aiello — the list's convention keeps Åström first; Hocherman after Hayes and before Hutchings). While the block was open, its one formatting blemish was repaired: the Åström and Aiello entries shared a single paragraph (one newline) while every other entry was paragraph-separated, and a double blank line sat between Aiello and Beretka — both normalised to the uniform entry/blank/entry form. No entry other than the two insertions was touched.

4. **The retitle and the DOI list remain blocked owner-level items.** The commission message names them but supplies neither a title nor a list, and the standing rules bind: the owner must name the retitle; the DOI pass is the owner-supplied list (never guessed). What this round does supply: both NEW entries carry verified DOIs (the class of verification the DOI pass would extend to the other 36 entries if the owner supplies or commissions a list).

---

## Part II — directive 2: the artifact-class scan and removal

**Method.** A machine scan over the paper and the supplement across six artifact classes — changelog-diary/editing history, meta-commentary announcements, self-referential process references, internal dialogue, informal chat artifacts, and process date stamps — with per-hit manual adjudication (the classes overlap and the paper's certification-honesty register deliberately uses words like "registered", "recorded", "recovered", "re-execution-verified" that a naive scan would flag).

**What was found and removed (paper, 14 anchored edits):**

| Site | Artifact | Class |
|---|---|---|
| §7 opening | "One point is stated once, at the outset." | meta-commentary (the writing announcing itself; the following sentence carries the content unchanged) |
| §8.3 | "are relocated to the supplement (S11)" | editing history → the paper's own deposit register ("deposited") |
| §10.4 | "the relocated MPF sweep" | editing history |
| Supplementary ¶ | "the relocated MPF material of S11 (…; relocated from Sections 8.3 and 10.4)" | editing history (narrates the document's restructuring past) |
| Remark 5.1 (H1) | "is now established" | change-of-state diary ("previously open, NOW established") |
| §11.5 | "now registered" | change-of-state diary |

**What was found and removed (supplement, 11 anchored edits on 10 lines):**

| Site | Artifact | Class |
|---|---|---|
| S1.2 | "the committed pipeline implements…" | repository-speak → "the deposited pipeline" |
| S4 | "the Hocherman (2025) synthesis" | single-author form for a three-author paper (corrected, not removed) |
| S5 | "carried over from the audit document" | self-referential pointer to an internal file **not deposited in the package** |
| S5 | "(verified 2026-09-03; audit `audits/tikhonov_unh_verification.md`)" + "is stated in full in the audit document" | process date stamp + dangling internal pointer |
| S5, S7 | "now established" ×2, "is now verified" | change-of-state diary |
| S8 | "At the committed gated Candidate A coefficients", "the committed fundamental pair" | repository-speak (dropped / "registered") |
| S9.5 | "reproduces the committed P4 certificates" | repository-speak → "the registered P4 certificates" |
| S11 | heading "Relocated MPF Material"; "Material relocated from the main article's Section 8.3"; "stated where it belongs… with the relocated material" | editing history + placement meta-commentary → heading retitled "MPF Material" (the main text's own phrase), clauses removed |

**What was deliberately KEPT (adjudicated, not artifacts):**
- the certification-honesty register throughout ("registered", "recorded", "recovered", "re-execution-verified", "declared status", "reproduced byte-identical") — this is the paper's epistemic discipline, not process leakage;
- "threshold relocation" / "relocates the local thresholds" (§3.2, §5.1) — dynamical-systems terminology (bifurcation thresholds moving between model variants), unrelated to editing history; the regression gate therefore bans "relocated", which cannot match "relocation"/"relocates";
- the two surviving "now"s — "the assessment-frequency literature now studies the review cadence" (the literature's current state) and "*now with the mobilising gains*" (mathematical prose for the present case);
- "The mathematics of this section says two things" / "the record does two things" — ordinary enumeration, not chat;
- "effort is restored toward a cap" — the quota law's description;
- the table-honesty sentence "Every entry below is a record already stated in this section…, collected in one table; the mobilising native-ZOH row's annual radius is not a recorded quantity of this paper" — carries the load-bearing no-new-content + not-a-recorded-quantity caveats; only the pure signposts ("The message of the paper is stated plainly", "is collected in one display", "It has a plain name") were the v35 removals;
- the AI declaration in the back matter — required transparency, not an artifact.

**Permanent regression gates added:** the removed phrases are now banned strings in every scanner ("One point is stated once", "stated once, at the outset", "relocated", "the committed", "audit document", "is now established", "now registered", "2026-09-03", "where it belongs" — 44 banned strings total at md and tex level; 43 in the rendered-text scan) so the artifact classes cannot silently return.

---

## Part III — the abstract exactness re-check (the flagged owner decision)

Task 96 flagged the opening phrase *"those studied so far are ecological"* for re-check once Adamson & Hilker is cited, suggesting *"ecological or informational"* as the repair and explicitly reserving the decision to the owner at commission time. **The re-check was performed; the abstract is deliberately byte-identical in v38.** The record:

1. **The sentence remains defensible.** It compresses §12's "Delays in the ecological dynamics of harvested stocks are the classical subject of delayed-logistic and delayed-recruitment analysis" — the ecological-dynamics tradition the paper positions against. The delayed-knowledge line (Ezekiel's price-signal lag; A&H's knowledge delay) is presented in §1.1 as the *modelling counterpart* on the institutional side of that contrast, not as part of the ecological tradition the clause compresses.
2. **The suggested repair breaches a hard bound.** "…are ecological or informational" adds two journal words: 258 → 260, violating the standing below-260 abstract bound (Task 91's owner directive). A net-zero rephrasing exists (e.g. restructuring the opener around "Delays — ecological or informational delays so far — destabilise…") but degrades the classic-declarative opening; a compensating trim elsewhere in the abstract would be a further content decision.
3. **The decision stays with the owner.** Say the word and it is a one-line v39 with either the +2-word repair (accepting 260 or a compensating trim) or the net-zero restructure.

---

## Part IV — machine verification (wave21, all fail-loud)

- **`make_v38.py` — ALL CHECKS PASS.** 14 anchored paper edits + 11 anchored supplement edits, every anchor unique; math-span multiset EXACTLY equal to v37's (1,473 occurrences); headings identical; content numerics == the declared deltas only (the two reference entries with DOIs, the five in-text citations, the v7 filename digit; nothing else, verified raw and stripped); word tokens == the declared edit delta (adamson+3, hilker+3, hocherman/trop/ghermandi+4 each, relocated 4→0 in the paper and 3→0 in the supplement, committed 4→0, "now" 4→2); the section-reference multiset loses only the removed "Sections 8.3 and 10.4" construct; frozen blocks byte-identical (title, abstract at 258 journal words, keywords, declarations, Data availability, figure); the References block == the declared construction (38 entries, uniform paragraph separation); the Supplementary block == the declared construction; the cross-reference resolver 0 unresolved; all eight supplement→main-paper references resolve; the supplement's S1–S12 structure unchanged except the declared S11 retitle; the supplement's numerics lose only the removed date stamp. Idempotent; v37/supp-v6 untouched on disk.
- **`build_latex_v21.py` — three consecutive byte-identical tectonic builds.** tex md5 `b9e23ee40f96852f5b3877aae9858f1d`; 45 pages; overfull 10 = the inherited count; the wave19/20 battery inherited (md-level gates, the 90-needle battery incl. the new reference/citation needles, the 44-string rejection scanner at md and tex level, 'if and only if' ×5, the tex-level resolver, the section-order gate 7<8<9, the tex-level stripped-numeric discipline vs the v37 tex == the declared tokens, the v7 pointer at md and tex level with the stale v6 pointer absent).
- **`check_pdf_v38.py` — ALL PDF CHECKS PASS.** 10 page-1 + 90 body needles; spine order 5<6<7<9 verified; 2 URI annotations; 0 rejection hits over 43 banned strings in the rendered text; the rendered abstract 258 journal words (cap 259); the v7 pointer rendered on pdf page 45 with the stale v6 pointer absent; the A&H lineage sentence on pdf page 2; the Adamson entry on pdf page 43 and the Hocherman entry on pdf page 44; the AI declaration last. (One pagination note: the v38 layout shifts one needle across the pdf 3→4 boundary — the checker now strips footer page numbers when joining pages.)
- **`review_v38.py` — the A/B/C/D ledger, ALL CHECKS PASS.** A: the reconstruction gate (v38 == v37 + exactly the 14 declared edits, byte-for-byte; ditto supp v7 == v6 + 11); math spans 1,473 multiset-equal; numerics/section-refs/headings/frozen blocks/label counts as above; the artifact-class regression gates green (the removed phrases absent; the two surviving "now"s the legitimate ones). B: the supplement ledger (structure, numerics, resolver, artifact gates, mirror consistency, the three-author Hocherman form). C: references frozen v32==…==v37 at 36 entries with v38 == v37 + the two declared insertions (38 entries); prior checksums unchanged — v31…v37 md+tex, supp v5, supp v6. D: rejection 0/44 at md and tex; 'if and only if' ×5; the v38 tex md5 == the three builds.
- **VLM page verification (glm-5v):** page 1 — 5/5 (title, byline with clickable ORCID/email, date, the abstract's opening, keywords); the §1.1 lineage page — 4/4 (the A&H sentence renders with its citation, positioned between Moxnes and Ostrom, no rendering defects); the §7 opening — the meta-sentence confirmed absent with continuous flow (Theorem 7.1 itself now begins one page later — a pagination shift verified in the text layer by the needle battery); the references pages — the Adamson entry (3/3) and the Hocherman entry (2/2 relevant) rendered verbatim with correct alphabetical placement and uniform paragraph separation; the final page — 3/3 (the v7 pointer in typewriter font, no v6 anywhere, the AI declaration last).

---

## Part V — the supplementary package refresh

`submission_zips/paper4_supplementary_v7.zip` (built this round, replacing v6 as the deposit behind the Data availability statement): the **supplementary v7 document**; the code-and-records payload (`code_and_records/`, `figure/`) **byte-identical to the v6 package's payload** (verified file-by-file against the v6 zip); an updated `README.md` (the v38 manuscript checksums, the v7 supplement, this round's description); a regenerated `MANIFEST.sha256`; and the verification records. The packaging-time re-execution record of 2026-09-18 stands for the code (unchanged bytes — the interval-Hopf JSON byte-identity, the 21/21 registration gates, the exact-hold T_r = 6.5013 yr record were re-execution-verified at v6 packaging time and the payload has not changed); the v7 note documents the document-only refresh.

---

## Part VI — honest residuals

1. The retitle and the owner-supplied DOI list remain the standing blocked items (Part I.4); the abstract's opening phrase remains the flagged owner decision (Part III).
2. The supplement's CONTENT is still v29-era in scope beyond the artifact classes removed here; a full value-by-value supplement-content audit remains its own round if commissioned (the Task-95 residual, unchanged).
3. The two new references' DOIs are web-search-verified against publisher records (Springer/PubMed/PMC); the remaining 36 entries carry the DOIs they carried since v32 — the DOI pass over them is the owner-level item.
4. The §7 VLM check records a pagination shift (Theorem 7.1's statement now begins on the page after the §7 opening) — a layout consequence of the round's net +4 lines, not a defect; the full needle battery verifies the theorem's presence and label counts in the rendered text.
