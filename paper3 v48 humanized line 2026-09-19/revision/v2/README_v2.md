# `revision/v2/` — Qwen baseline rebuilt as a novelty-first version

**Rule applied (user, 2026-09-14):** *"use qwen's p3 rewrite.txt as baseline. the rule is to emphasize novel contributions with minimal necessary background added."*
**Constraint inherited:** new version, nothing overwritten — `uploads/qwen's p3 rewrite.txt`, `work/paper3.txt`, `humanized/v1/` and every earlier file are untouched.

## Files

| File | Content |
|---|---|
| `paper3_v2_full.md` | the whole version, 171,561 chars · 12,719 words (assembled from the four parts) |
| `part_1_results_and_ledger.md` | §1 **what this paper establishes** (status-labelled results table, the non-claim list, compressed background, the two regimes, organisation + numbering note) · §2 the ledger in minimum form (definitions, (1), (2), the three recharge laws, mechanism typing, scaffold variants, saturation) |
| `part_2_certification_and_closed_ledger.md` | §3 certification layers (Props 1–2, safety set, Lemma 3, Prop 4, Thm 5 + corollary + qualifications + worked envelope, Prop 6, counterexample, Depletion-is-compartmental) · §4 closed ledger (Thms 7–15 with proofs, both incidences, §4.9 cancellation-is-cheap, the portrait) |
| `part_3_services_depletion_discipline.md` | §5 services and the componentwise deficit (Defs 1–2, Remark 16, decline pressure) · §6 depletion arithmetic and all three applications with every table, the quarantine note, the cohort disclosures, Non-example 1, the vintage paragraph · §7 non-compensation + double counting + negative content + limitations (i)–(viii) |
| `part_4_templates_surrogates_interface_conclusion.md` | §8 domain templates · §9 first-passage on declared surrogates (Def 6, Props 18/20, Cor 19, barrier discipline, **seven non-claims**, identifiability wording) · §10 interface + non-reduction theorem with all five reasons and their numbers · §11 conclusion · back matter · **version note** |

## What "baseline" meant here

Qwen's file supplied the **architecture and the compression level**, and its §1 prose (which is genuinely better at stating the inferential point: "same dimension does not imply same measurand"). It could not supply content: verified against the source, it carries **42 of the source's 186 numeric tokens (23%)**, **3 of 50 discipline phrases**, and deletes §2.4–2.6, §4.7–4.9, §6.4, §6.5.2 tables + quarantine, §7.7, §7.8, §8, §10.3, §10.4, References and the supplementary pointer (full audit: `review/ledger_audits_verified_v1.md` §4). So every one of those was restored from `work/paper3.txt`, with `humanized/v1/` used as the already-verified donor for the status-bearing sentences.

**Result of the restoration:** v2 retains **144 of 186 numeric tokens (77%)**; the residual 42 are source section numbers superseded by the re-ordering, DOI/page numbers inside the reference list (which v2 points to rather than duplicates), and one ORCID fragment. Discipline phrases: **31 of 32** tested strings present, with the two flagged near-misses checked by hand and confirmed present in math form.

## The novelty-first structure

Sections **2–6 and 8 keep the source's numbering and every numbered statement** (Definitions 1–6, Theorems 1–15, Propositions, Remarks, Corollary), so all cross-references still resolve against the 40-page original. The re-ordering is in the frame and the tail:

1. **§1 leads with the results table** — object · predicate established · status · where — so the contribution is on page 1 instead of page 4, and the non-claim list is placed immediately after it rather than at the end.
2. **§7 = non-compensation, double counting and limitations**, promoted from the source's §10 to sit directly after the applications that it governs. This is the paper's most citable content and its most quotable risk; adjacency is the fix.
3. **Background compressed to §1.3** (one paragraph per literature) with all citations retained; the elevator, the four-predicate list and the productivity-illusion analysis are reduced to their load-bearing sentences; §2 carries only what the theorems need.
4. **The domain templates and the surrogate section are short by design** — §8 is three paragraphs, §9 keeps every statement and non-claim but drops derivation prose the source itself labels "a standard fact, stated for notation".
5. §9 and §10 swap so that the discipline (§9's non-claims) precedes the interface (which imports §9's numbers).

## Audits adopted (bucket T of `review/ledger_audits_verified_v1.md` §5)

Wording and framing only — **no new theorem is asserted anywhere in v2**:
anti-compensatory rather than anti-scalar, with the min-margin equivalence and the binding component named (§7.1) · aggregates as valid alarms / invalid certificates (§7.1, §6.5.2) · "identifiability" named where the paper already does the work, with the constant-shift argument stated in words and attributed as the reason §6.5.1 classifies as it does (§9.8) · loss of **safety** vs loss of **assurance** (§7.3) · the joint reading of $\Pr[\tau_{\mathrm{exit}}>T]$ made explicit because it is easy to miss (§6.4) · antecedent humility, which all four audits and my own N1/N2 converge on.

Explicitly *not* adopted: the curvature-number theorem, the half-space proof, the Farkas/IIS witness, the review-interval (Nyquist) bound, false-safe volume, and every passport/ratchet/engine/dashboard/pilot item — the first group needs the author's proofs (they are correct where I checked them: `ledger_audits_verified_v1.md` §2, M1–M8), the second addresses objects this article does not contain (0 hits for "passport", "dashboard", "pilot", "engine", "34 modules"), and the audits' illustrative figures ("78% regenerative", "2.8×", "+38% overhang") appear nowhere in the source and were kept out.

## Deliberate limit of this version

v2 optimises **emphasis and completeness**, not sentence length: mean prose length is 32.3 words (source 31.3; v1 is 22.5). That is the consequence of restoring the source's formal statements rather than paraphrasing them. If you want both, the mechanical step is a v3 = v2's structure × v1's sentence programme (split over 45-word sentences, `humanize/style_audit.py` as the gate) — it is a scripted pass over four files, not a rewrite.
