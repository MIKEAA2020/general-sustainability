# v37: the alignment audit, the humanizing-pass error audit, and the journal-fit assessment

- **Round:** Task 95, 2026-09-18. Owner directives: (1) *do abstract, title, keywords, individual sections and supplementary file all align with latest version?* (2) *ensure no errors introduced or content lost from the several humanizing passes, including both numerical/mathematical errors and prose errors*; (3) *best journal fits?*
- **Baseline at round start:** `paper4_delay_dynamics_v36.md` (md5 `06af59363a0301b61eae237d7a4f3ea2`), tex md5 `258c2424a752897a139725681af99ecb`, the accompanying file `paper4_supplementary_v5.md` (md5 `8b0170811a31e673cefcc12e59b18895`, last authored in the v29 era, Task 78, 2026-09-06).
- **Round outcome:** items 1 and 2 audited with machine evidence; one genuine defect found (the supplementary file's three stale main-paper section references — an alignment error introduced by the v36 restructuring's renumber map never reaching the accompanying file) and repaired in this round as **paper4_delay_dynamics_v37.md + paper4_supplementary_v6.md** (wave-20 pipeline, all gates green); item 3 answered in Part IV.

## Part I — the alignment audit (directive 1)

### I.1 Title — ALIGNED

"Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective Channels of Institutional Feedback, and the Review Interval as Control." Each clause names a load-bearing part of the v36 structure: the five-regime attractor topology (§8.2), the two channels (§5, §6), and the promoted §7 — whose heading "The Review Interval as Control" matches the title's final clause verbatim. Byte-identical v32→v37 (gates A6, C-chain).

### I.2 Keywords — ALIGNED

All nine keywords map to named body content: *delay differential equations* (§2–§4); *Hopf bifurcation* (§4–§5, Theorem 4.1); *institutional feedback* (§1.1, §2.1); *renewable resource management* (§11.3's translation table); *fisheries governance* (§1.1, §11.4); *sample-and-hold control* (§6.4, §7, Åström and Wittenmark 1997); *regime shifts* (§8.2's five-regime topology); *maturation delay* (§9); *recruitment dynamics* (§9.1–§9.4). Byte-identical v32→v37.

### I.3 Abstract — ALIGNED (258 journal words, re-verified at three levels)

Every digit token has body support (re-checked by grep this round): 3.7 → §5.1's τ₋ = 3.67/3.666 enclosures; 150 → τ₊ = 150.36/150.358; 2.3 → §6.4/§7's Euler artefact (2.306); 6.5 → §7's T_r = 6.50 (Proposition 7.1); 1992/2024 → §11.4's cod moratorium (2 July 1992) and reopening (26 June 2024). Every load-bearing claim phrase re-located in the body: "two subcritical Hopf crossings" (§5.2's ℓ₁ records), "no-Hopf theorem" (Theorem 6.1), "discretisation artefact" (§6.4), "Neimark–Sacker-type crossing" (§7), "continuum stages open" and "unverified large-amplitude attractor" (§8.2/§11.5), "stock-agnostic" (§11.3 breadth statements), "grounding scales, not coefficients" (§11.4), "more frequent assessment is not always safer — a local spectral design parameter" (§7's opening and §11.2's practical reading). Word count 258 verified at md, tex-abstract-environment, and rendered-text level (check_pdf_v37: "rendered abstract: 258 journal words (cap 259)"). Byte-identical v35→v36→v37.

### I.4 Individual sections — ALIGNED

- **The Organization paragraph (§1.3)** lists every section in the v36 order with content descriptions that match the actual headings (§7 "treats sample-and-hold review", §8 "reports the global numerics and their certification levels", §9 "registers the maturation-delayed recruitment system", §11 lists the six Discussion themes including the ecological reading). Rewritten in v36 for the rotation; verified against the skeleton this round.
- **The repaired §1.2 pointers are semantically correct** (re-verified by context reads): "subcritical (Section 5.2)" → §5.2 Lyapunov coefficients and criticality; "mobilising weight (Section 5.4)" → §5.4's conditional mobilising-weight corollary; "the flow-then-update … convention of Section 7" → §7; "(Sections 6.2 and 6.4)" → the no-Hopf theorem plus the discretisation-crossing record; "(Proposition 7.1)" → the exact held-measurement monodromy with the 6.50-yr crossing.
- **The cross-reference resolver** (the permanent gate, md + tex + rendered): 0 unresolved Section constructs (review_v37 A8).
- **The rotation seams are clean** (the highest prose risk in v36): §6.5 closes with a self-contained chapter ending; §7, §9, and §10 each open with self-contained paragraphs whose only section pointers are explicit and correctly renumbered (§9's opening points at "Sections 5 and 6" and "Section 8.6" — the latter correctly mapped from old 9.6); §8's adjacency to §7 is the v35 adjacency preserved. No "next section"/"previous section" relative pointers exist anywhere in the paper (full scan this round: every hit is a safe self-reference).
- **Data availability** uses the v36 numbering throughout ("the five-regime continuation records of Section 8.2", "the recovered stage-analysis machinery of Section 9", "Supplementary S9").

### I.5 The supplementary file — WAS MISALIGNED; NOW ALIGNED (v6)

**The finding.** `paper4_supplementary_v5.md` was authored against the v29 structure (Task 78) and never touched by v31–v36. Its three references to the main paper's rotated sections were correct for v29–v35 and stale under v36:

| Supplement site | v5 text (v29/v35 referents) | v36 reality | Repair in v6 |
|---|---|---|---|
| S9 intro | "All records of **Section 7** of the main paper" (§7 = Delayed-Recruitment) | §7 = The Review Interval as Control; Delayed-Recruitment is §9 | → "Section 9" |
| S11 intro | "relocated from the main article's **Section 9.3** (the MPF paragraph)" (§9.3 = registered numerical families) | that content is §8.3 | → "Section 8.3" |
| S12 status note | "(main text, Sections 5.1 and **9.2**; …)" (§9.2 = attractor topology / fold records) | that content is §8.2 | → "Sections 5.1 and 8.2" |

The paper's own statements already used the v36 numbering (Data availability: "the Section 9 records … Supplementary S9"; the in-paper Supplementary paragraph: "relocated from Sections 8.3 and 10.4") — so the supplement was contradicting the paper it accompanies. The v36 renumber map was applied to the paper's md/tex/rendered text only; the accompanying file was outside every gate's scope. This is the error class the owner's directive 2 targets: an error introduced *by* the restructuring pass, in the cross-file layer.

**The repair (version discipline: new files only).** `paper4_supplementary_v6.md` — byte-identical to v5 except exactly three lines (the remapped references; internal S1–S12 structure and object-label inventory unchanged; every one of the eight supplement→main-paper references now resolves against v37's headings). `paper4_delay_dynamics_v37.md` — byte-identical to v36 except exactly one line (the accompanying-file pointer `paper4_supplementary_v5.md` → `paper4_supplementary_v6.md`). Nothing else changed anywhere: all 1,473 math spans multiset-equal to v36; content numerics == v36 + the filename version digit only; section-reference multiset identical; heading skeleton identical; references (36 entries frozen v32==…==v37)/declarations/figure byte-identical; abstract 258 words byte-identical; 'if and only if' ×5; rejection list 0 hits (35 banned strings, md and tex).

**The verification battery (wave20, all fail-loud):** `make_v37.py` (anchor counts == 1; line-diff gates; supplement-alignment gates; idempotent; v36/v5 untouched) → `build_latex_v20.py` (the wave19 battery inherited + the v6-pointer gates at md and tex level + the numeric discipline vs the v36 tex == the filename digit; three consecutive byte-identical tectonic builds, tex md5 `28f6eee027ba9e5449b9a712bd35a54f`; 45 pages; overfull 10 = the inherited count) → `check_pdf_v37.py` (10 page-1 + 79 body needles; rendered spine order 5<6<7<8<9; 2 URI annotations; 0 rejection hits; the v6 pointer rendered on pdf page 44 with the stale v5 pointer absent from the rendered text; AI declaration last) → `review_v37.py` (the A/B/C/D ledger, ALL CHECKS PASS, prior gates review_v34/v35/v36 re-run ALL PASS) → VLM page verification (page 1: 5/5; the supplementary-pointer page: 5/5 — the v6 filename renders in typewriter font with no v5 anywhere; the declarations page: 3/3 with the AI declaration last; §7's opening with Theorem 7.1; the Governance-warning statement beginning on pdf page 21 with its continuation on page 22 — all phrases confirmed in the text layer).

## Part II — the humanizing-pass error audit (directive 2)

**The passes:** v33→v34 (the humanizing pass, 37 anchored edits), v34→v35 (abstract compression 560→258 words + the ecological-reading consolidation), v35→v36 (the restructuring + E1–E4 consolidations).

**Numerical/mathematical integrity — machine-verified intact:**
- `review_v34.py` re-run: ALL CHECKS PASS (math spans vs v33; numerics; references frozen 36; 'if and only if' ×5; prior checksums unchanged).
- `review_v35.py` re-run: ALL CHECKS PASS (the 11.7 insertion and 11.8/11.9 renumbers; Discussion sequence 11.1–11.9; references frozen; prior checksums unchanged).
- `review_v36.py` re-run (twice this session — before and after v37): ALL CHECKS PASS (the bijective rotation map; the E-deltas; references frozen; prior checksums unchanged).
- `review_v37.py` (new): ALL CHECKS PASS (see Part I.5). The chain is green end-to-end v31→v37: zero numeric losses outside the declared renumber generations, zero math-span changes outside the declared empty whitelists, references frozen at 36 entries since v32, every prior version's md+tex checksum unchanged on disk and in history.
- The v35 abstract compression's six cut items were substance-checked at compression time (the wave18 cut ledger) and the survivors re-located this round: every digit token and every load-bearing claim phrase of the compressed abstract has body support (Part I.3).

**Prose integrity — scanned and read at the high-risk sites:**
- Doubled-word scan (20 function-word classes): 0 hits. Artifact-punctuation scan (",,", "..", "; ", stray hyphens): 0 real hits (all flags are markdown `---` separators or false positives, each read and cleared).
- The rotation seams (§6→§7, §8→§9, §9→§10): all self-contained, no orphaned relative pointers (full "next/previous/preceding/following section" scan: clean).
- The one v35-era edit-seam risk class — the E1-repaired contribution pointers — re-read in context: semantically correct (Part I.4).
- The supplement's S11 claim that "every value below is reproduced verbatim from the main text; nothing is recomputed, and the main text retains one-sentence pointers carrying the key numbers" — re-verified: η_crit ≈ 2.337, CV 1.58, r = −0.47, and the >300-parameterisation screen all appear in §8.3's MPF paragraph with the S11 relocation pointer; the sign-flip values 128.374/70.697 and loop gain 1.016 render in §6.3.
- **The one genuine error found in this audit is the cross-file misalignment of Part I.5** — introduced by the v36 restructuring pass, outside the md/tex gates' scope, now repaired in v37 + supplement v6.

## Part III — what v37 is and is not

v37 is an accuracy-only alignment round: one line in the paper (the supplementary pointer), three lines in the supplement (the remapped references). No scientific content, no number, no claim, no reference, no heading, no math span changed. It is not the retitle (owner-level; name a title → v38), not the DOI substitution (blocked on the owner-supplied DOI list since v32; never guessed), and not any of the Task-94 adjudicated commission items.

## Part IV — best journal fits (directive 3)

The paper's profile that drives the fit: DDE bifurcation theory (Hopf cubic, even-pairs algebra, Lyapunov coefficients) + certified computation (interval Newton, Krawczyk, Moore–Spence) + sampled-data/hybrid monodromy analysis + global attractor numerics + a stylized fisheries-governance application with a documented case record; 45 pages with a separate supplementary file; theorem-proof density with management translation tables. Ranked:

1. **Journal of Mathematical Biology** (Springer) — the primary recommendation. Mathematical models of biological/resource systems with substantial analysis is its core scope; the certification discipline matches its rigor culture; long papers with electronic supplements are normal; the ecological comparison (§9) and the life-history selection (§11.7) give it the biology anchor. The mathematics-first presentation lands as-is.
2. **Natural Resource Modeling** (Wiley) — the strongest subject-community fit: mathematical modeling of renewable-resource management is the journal's literal scope, and the governance/message layer (§11.2–§11.4, the translation table) is exactly its audience. Verify by recent issues whether the interval-certification density suits its norm before committing; the paper may need no change, but the expected referee pool differs (resource modelers rather than dynamicists).
3. **Mathematical Biosciences** (Elsevier) — the solid alternate to JMB; same scope class, marginally different culture.
4. **Journal of Dynamics and Differential Equations** (Springer) — if the DDE-theory community is the target audience: the Hopf-cubic/even-pairs/characteristic-equation core is their material; the application reads as motivation. The certification content is a plus.
5. **SIAM Journal on Applied Dynamical Systems** — if the sampled-data/hybrid monodromy and the certified global numerics should lead; computational dynamics with validation is respected there; the governance framing is off-center but admissible.

Deliberately not recommended: fisheries-science venues (the paper's not-a-calibration stance and stylized model would be misread there; note "Fisheries Research" and "ICES" are already banned strings in the rejection scanner); control-theory venues (paper2, the companion, already occupies the Automatica routes — the portfolio should diversify); ecology-letter venues (wrong density); and the pure-mathematics DDE journals beyond JDDE (the application would be trimmed to a remark).

Strategic note: the companion ecosystem already spans audiences (paper2 → Automatica routes; paper5 → the Nature-Sustainability family; paperE1 → the empirical cod ladder), so paper4's best position is the applied-mathematics-in-biology venue (1 or 3) with the resource-modeling venue (2) as the subject-first alternative. Caveats: verify each venue's current author guidelines (length policy, citation style, supplementary policy) at submission time; impact factors are deliberately not quoted here; and the pending owner-level retitle could sharpen the fit either way (a governance-leaning title → NRM; a DDE-leaning title → JMB/JDDE).

## Part V — honest residuals

1. The supplement's *content* (its records, its S3 status note, its S12 label mapping) is now aligned with v37's structure, but the supplement remains a v29-era document in scope: it has never been re-verified line-by-line against the current paper the way the paper itself is gated version-to-version. The alignment repaired here is the reference layer. A full supplement-content audit (value-by-value against the current records) would be its own round if the owner wants it.
2. The v37 pdf's page count stays 45 (the pointer change does not reflow); overfull count 10 = inherited.
3. The retitle and the DOI substitution remain the standing owner-level items; the Task-94 commission paths (parameter-box campaign, economics reading list) remain open.
4. No PAT was supplied in this round's message: the round is committed locally and the push awaits the owner's PAT (in-memory only when supplied; rotation advised — the previously pasted PAT should be revoked regardless).

*Verification artifacts of this round: wave20/{make_v37.py, build_latex_v20.py, check_pdf_v37.py, review_v37.py, logs/ (7 rendered pages + 5 VLM records)}; the re-run review_v34/v35/v36 gates; the grep line anchors cited inline; the diffs shown above (one paper line, three supplement lines).*
