# v36: the batch-8 restructuring round — implementation and machine-checked review

**Task:** Owner-directed (Task 93): the challenge to the Task-92 adjudication ("your previous response was that the majority of points in all 6 audits have already been implemented, are you sure?! even the restructuring?") plus "provide v36".

**Date:** 2026-09-18.

**Baseline:** `arena agent 1/paper rewrites/paper4_delay_dynamics_v35.md` (md5 `e9c99edbcf59cce80f2bd08c2966a74b`; tex md5 `f1bdcd666baf6a0195fa33a7e0913d80`; 44 pp). **Deliverable:** `paper4_delay_dynamics_v36.md` + `latex/paper4_delay_dynamics_v36.tex/.pdf` (tex md5 `258c2424a752897a139725681af99ecb`; 45 pp; three consecutive byte-identical tectonic builds). v35 and all prior versions untouched on disk and in history.

---

## Part 0 — The corrected adjudication (answering the owner's challenge directly)

The owner's challenge has two parts; both get straight answers.

**1. "Are you sure?!" — What the Task-92 assessment actually claimed, re-verified today.**
The claim was never "everything including the restructuring is already implemented." The assessment's Part 0/Part III ledger said: the six audits' *content-level* demands are already in v35. Today that ledger was re-verified with a fresh 30-needle machine spot-check: 30/30 present (the two apparent misses were my paraphrase strings — the paper's own phrasings "Three coordinates of the institutional loop are independent of the ecology they govern" and the certification-tier sentences were located verbatim). The restructuring layer was explicitly adjudicated **NOT implemented, owner-level** (Task-92 Part II, C3/C6/C8/C9). Where the previous round deserves the owner's criticism is in the *deferral*: three audits (sol's primary spine, qwen §14, sol2 §19) converge on the same reorganization, and deferring all of it to "owner-level" was too conservative for a round the owner was always likely to commission. **v36 corrects this by implementing the convergent restructuring.**

**2. "You mean 6 auditors all mistakenly think the paper hasn't implemented their points?!" — No, and the audits themselves say so.** The six texts are upgrade strategies, not defect reports about missing content:
- sol's §2 is literally titled "What is already strong" and explicitly credits the governance-loop framing, the mobilising/protective contrast, the review-interval design variable, and the certification discipline — then proposes to *restructure* the paper around them (sol §3: "the manuscript is trying to be four papers").
- qwen's §2 headings are "Correction: 'positive roots come in even multiplicity'" etc. — its corrections target *gemini's text*, and its one paper-quoting "correction" is verifiably stale: the quoted abstract sentence exists in v30 and in no version since (machine-checked today: 1 hit in v30, 0 in v35) — qwen audited an abstract six major versions old.
- gemini repeats the paper's own §1.2 pointer "(Section 6.2)" for the Euler artefact (machine-checked: the audits file contains that exact stale pointer) — i.e. it echoed the paper's own cross-reference defect, which E1 below repairs, rather than reading §6.4 where the record lives.
- sol's title critique ("contains formatting problems") is stale against the clean v35 title line (machine-checked).
- deepseek's §8 ("the paper is trying to be too general") and sol's §3 agree with each other and with the paper's own §11.3/§11.8 scoping — the disagreement is about emphasis and packaging.
So the overlap is not six errors: it is six prospective proposals, written largely against pre-v31 snapshots and against each other, whose content-level demands a mature delay-dynamics paper inevitably already satisfies (regime windows, hysteresis, subcriticality, artefact labelling, cod discipline, certification tiers), and whose *structure-level* residue was real, unimplemented, and is now implemented.

**What v36 implements** is exactly the convergent spine the three strategic audits share, mapped onto the existing skeleton without destroying a single registered record:

| Audit demand (convergent) | v36 implementation |
|---|---|
| "Periodic review as sampled-data control" immediately after the continuous-delay stability core (sol primary spine item 3; qwen §14 Section 4; sol2 §19 Section 4) | Old §8 (The Review Interval as Control) **promoted to §7**, directly after §5 (mobilising) and §6 (protective) |
| Global regimes next (qwen §14 Section 5; sol2 §19 Section 5) | Old §9 (Global Numerics) **moved to §8** |
| Ecological/comparative material as the late chapter before the Discussion (sol Paper D; qwen §14 Section 8) | Old §7 (Delayed-Recruitment/Maturation-Delay System) **moved to §9** — the applied analogue, not a headline claim |
| A roadmap that maps the argument arc (qwen §14 intro moves; sol2 §20 item 10) | §1.3 Organization rewritten for the new arc (sign separation → cadence as its own control variable → global numerics → ecological analogue → generality), with two content-bearing arc phrases, no new claims |
| State the tier of each result (sol; qwen; sol2) | already implemented (v33–v35); unchanged |
| Safe-cadence/metrics sections (qwen §14 Section 6; sol §7.2; sol2 §10) | **still rejected** — new science requiring its own certification (Task-92 C7) |
| Four-papers split (sol §3); retitle (sol §17, qwen §14, sol2 §22) | **still owner-level** — the companion ecosystem already exists (sampled-governance, flow-balance, two-stage companions are already spun off and cited as such), the title is frozen v31–v35 and sol's premise is stale; a retitle is a submission-level decision the owner can commission as v37 with a named title |
| Move registered records to supplement (sol §13; qwen §14 supplementary) | **still rejected** — the registered-record density is the deliberate product of the owner's v32–v33 rounds |

## Part I — The change ledger (v35 → v36)

**R (the restructuring).** The three-block rotation old-8→new-7, old-9→new-8, old-7→new-9, with:
- every cross-reference renumbered by the bijective token map (7→9, 8→7, 9→8; 7.k→9.k, 9.k→8.k) — 119 Section references in v36 vs 115 in v35 (the map is count-conserving; the +4 are E2/E3's new pointers);
- the promoted section's numbered objects following their host: **Theorem 8.1 → Theorem 7.1 (×11), Proposition 8.1 → Proposition 7.1 (×9), Remark 8.1 → Remark 7.1 (×2), the "Propositions 6.2 and 8.1" list form (×1)** — old §7 and old §9 own no numbered theorem-like objects, so the renumber is collision-free (verified: no "Theorem/Proposition/Remark 7.x" existed anywhere in v35);
- three range/list constructs the token map cannot see, repaired explicitly: "(Sections 5.1 and 9.3)" → "(Sections 5.1 and 8.3)"; "the model of Sections 2–7" → "the model of Sections 2–6 and 9" (the scaffold-companion range, whose endpoint moved); "Sections 2.3, 7, and 9.3" → "Sections 2.3, 9, and 8.3" (the comma-list in §11.7's closing sentence);
- one net `---` separator added (the rotated region's boundaries normalised; 13 → 14 rules document-wide);
- **no sentence inside the moved blocks altered beyond the declared renumbers** — proven by the fragment round-trip gate (renumber is exactly invertible on each of the five fragments pre/post/blocks; `inverse(renumber(f)) == f` for each).

**R2.** §1.3 Organization rewritten to the new arc. New phrasings kept content-bearing per the owner's Task-91 meta-commentary standard: "together they carry the sign separation — opposite local mathematics on the same stock–memory block" (reuses §1.2(4)'s own words); "the review interval is a spectral design parameter in its own right, and the reviewed loop is a hybrid system, not the delay equation sampled at the review interval" (echoes the new §7's opening verbatim-adjacent).

**E1 — the cross-reference repairs** (the paper defect all six audits missed, present since v31): §1.2(4) "(Section 4.2)" → "(Section 5.2)" (both crossings subcritical); "(Section 4.4)" → "(Section 5.4)" (conditional mobilising-weight corollary); §1.2(5) "(Section 6.2)" → "(Sections 6.2 and 6.4)" (the artefact record lives in §6.4). Plus the **permanent cross-reference resolver gate**: every number in every Section construct (prefix, comma-list, and-list, en-dash range) must resolve to an existing `## N.` / `### N.M` heading, at md AND tex AND rendered-text level. This gate would have caught the v31 defect on day one.

**E2 — §11.8(ii) completion** (sol §5.1, sol2 §4, grounded): the single discrete lag named as a reduced compression of the observation, assessment, decision, deployment, and compliance stages; the cod chronology of §11.4 (annual assessment, the 1992 moratorium decision, the 2024 reopening) registered as a record of such stages at management scale; no additivity claim either way (Task-92 C4 adjudication preserved).

**E3 — §11.9 completion** (qwen §5.7/§11.2, sol §7.3): parameter-box certification registered as the third stated open task — the interval enclosures of §5.1 certify the registered decimal parameter vector, the one-at-a-time windows of §8.5 (renumbered from 9.5) are not boxes, and the interval Newton extension to declared parameter boxes is the upgrade from arithmetic precision to the policy robustness §11.5 reserves to a sensitivity layer.

**E4 — §11.8(i) completion** (deepseek §1, grounded): the identification layer — observational equivalence of gain–delay–memory triples, the institutional coordinates as latent structural parameters separable only through exogenous variation or direct process measurement, and functional-form identification as separate from parameter identification. Zero new model claims; a consolidation of the paper's own §11.8(i)/§11.4/§9.5 admissions into the explicit caveat the audits converged on.

## Part II — Verification evidence (the wave19 fail-loud battery)

- `make_v36.py` (idempotent; v35 byte-identical on disk after the run): parent md5 gate; math-span **multiset EXACT equality** (1,473 = 1,473; the rotation moves blocks, changes nothing); content numerics with section refs/headings/labels stripped == v35 + {1992: +1, 2024: +1} and nothing else; the section-reference multiset == the bijective map + the declared E-deltas; label counts (7.1 ×11/×9/×2, zero stale 8.1); heading skeleton == the declared rotation; title/keywords/abstract/references/declarations/figure byte-identical; Data availability + Supplementary identical modulo the map; resolver 0-unresolved; abstract 258 words; rejection list zero-hit; "if and only if" ×5.
- `build_latex_v19.py`: three consecutive byte-identical tectonic builds (tex md5 `258c2424a752897a139725681af99ecb`); pure-ASCII tex; md↔tex numeric and word parity; the full inherited needle battery (v33 style + v32 frozen claims + v34/v35 devices with the label renumber) + 25 rotation/E needles; tex-level resolver; the section-order gate (7 < 8 < 9 in the tex); tex-level stripped-numeric discipline vs the v35 tex (delta == {1992, 2024}); overfull 10 = the inherited count; 45 pages.
- `check_pdf_v36.py` (PyMuPDF): 10 page-1 needles; 13 pages-1-2 needles; 79 body needles (both hyphen-break normalisations); the rendered spine order 5 < 6 < 7 < 8 < 9 verified in the text layer; 2 URI annotations (https orcid before mailto); Figure 1 caption unique; AI declaration last; 0 rejection hits (34 banned strings); rendered abstract 258 words.
- VLM page verification (6 pages, `wave19/logs/vlm_*.json`): page 1 (title/byline/ORCID/email/date/abstract) all OK with no stray markup; the promoted §7 heading with "review cadence" bold and **Theorem 7.1** (not 8.1) rendering; the moved §9 heading with "The two channels of Sections 5 and 6" and subsection 9.1; the ecological reading with clean Greek; the regime table (now inside §8.2) clean; the declarations page with the AI declaration last.
- `review_v36.py` — the cross-version ledger: **ALL CHECKS PASS** (A: v36 vs v35 as above; B: all v32/v33/v34 numeric tokens survive outside the declared exemption generations — 27 tokens; C: v31 containment with the two renumber generations + Discussion sequence 11.1–11.9 + v31 needles; D: references frozen v32==v33==v34==v35==v36, 36 entries, 0 removed since v31; E: rejection zero-hit md+tex, "if and only if" ×5, tex md5 == the triple build, prior versions' md+tex checksums unchanged).

## Part III — Honest residuals

1. **Still owner-level (named, not deferred silently):** the four-papers split (the companion ecosystem already exists around P4 — sampled-governance, flow-balance/scaffold, two-stage companions — and the owner's v32–v33 registered-record design would be destroyed by the deletion sol demands) and the retitle (frozen v31–v35; sol's "formatting problems" premise is stale; any of the audited titles can be commissioned as v37 by naming one).
2. **Still rejected with reasons (unchanged from Task-92):** safe-cadence/viability/metrics computations (new science, own certification required); stochastic/strategic/multi-actor/normative extensions (change the declared model class); uncited economic microfoundations; new figures (the figure block is frozen and the one-figure design deliberate); evidence-status letter codes and ten-level hierarchies (cosmetic relabelling of §11.5 and the caution chain); the audited coinages (Sign Separation Theorem — mathematically false; viability bleed, phase-stabilisation trap, administrative hunting, basin lock-in, the eigenvalue maxims — decorative under the owner's Task-91 standard; all now on the rejection list as banned strings).
3. **The DOI substitution item remains blocked** on the owner-supplied DOI list (standing item since the v32 round; never guess).
4. Pagination moved as expected under the reflow: 44 → 45 pages (same content, reorganised + the E-completions); overfull boxes unchanged at 10.
5. The audits' shared valid core that v36 finally closes at revision scale: the spine order, the arc-bearing roadmap, the resolver-enforced reference hygiene, and the three consolidation completions. What remains of the six audits after v36 is, by the machine evidence, either new science or owner-level naming — not unimplemented paper content.

---

*Artifacts: `batch 7 (audits of agent arena 1 paper rewrites)/wave19/{make_v36.py, build_latex_v19.py, check_pdf_v36.py, review_v36.py, logs/ (tectonic log, 6 rendered pages, 6 VLM records)}`; the joint assessment this round implements and corrects: `humanizing audits/JOINT_P4_PROFOUND_INSIGHTS_ASSESSMENT_AND_PLAN.md` (Task 92).*
