# paper06_assessment_separation — CHANGELOG v70 → v71 (2026-10-15)

## Why this edition exists (lineage note)
* The research-article rewrite pushed on 2026-10-15 as `arena agent 1/paper rewrites/latex/paper1_assessment_separation_v64*` was built on `paper1_assessment_separation_v63.tex`, the newest file **of that name**. The lineage had, however, been renamed and continued as `arena agent 1/agent workspace/papers/paper06_assessment_separation_v64…v70.tex` (branch `e2-v3-source-year`), so the v64 rewrite was based on a stale ancestor and its number collided with paper06 v64.
* v71 re-issues the research-article edition **on the current base**: it keeps the article structure of the rewrite (sections, result numbering, figures, SI S1–S9) and ports every content change of paper06 v64→v70 into it. The earlier `paper1_…_v64*` files are retained in the repository under `paper rewrites/latex/superseded/` (renamed only); they are superseded by this edition.

## Reconciliation with paper06 v70 (all v63→v70 content changes, and where they landed)
| v70 change | v71 landing |
|---|---|
| Title → "Aggregation is a claim, not a presentation: the geometry of the acceptance gap" | Title (subtitle retained: "…between compensatory and noncompensatory transition assessment"); header, README, cover letter |
| Corrected abstract: canonical point (6/5, 6/5), 12/5 ≥ 2 vs 12/5 < 5/2; blends close the action-indexed margin-class gap but not the shared-shock gap; full-depth alternation ≠ blend; fine duty cycling is a different control class; detection requirement with reserve + protocol | Abstract; Contributions (iii)–(iv); §4.4 paragraph after Theorem 3/Proposition 4; Discussion design test 4 and detection paragraph |
| Path-to-margin synchronisation lemma (m_a(w) ≤ w·d_a, equality iff synchronised maxima) | **New Lemma 3** (`lem:sync`) before Theorem 1, with proof and scope paragraph; Contributions (ii); Related work item 1 |
| Fixed-weight countermechanism (w = (1,1), x = 1/2: 12/5 ≥ 2 accepts a primitive plan; no primitive plan meets both floors) | **New Remark 1** (`rem:fixedweight`) after Theorem 1; Contributions (iii); SI S2 numbering map (grid check 12) |
| Theorem S1/S2 restated with strict-interior hypotheses (s_i > 1, s_1+s_2 > 2, positive tube ratios, strict scalarized margin); boundary equalities excluded; zero-ratio boundary states accepted at the linear member only | Theorem 4(i)–(ii) wording; SI S2 proof of Theorem 4(ii) extended (openness below θ = 1 on the strict interior; collapse convention at boundary states) |
| LPI caveat corrected: Protocol 2 can **understate**, not overstate, the single-weight index's false-acceptance exposure; results depend on the normalisation λ_i = 1 + s_i/c | §4.5 closing paragraph; SI S3.5 caveats (b)–(c) |
| Slice-flip bullets: harmonic circle passes through (φ, φ) (not (√2, √2)); θ = 2/3 flip total = 2·√(6√3 − 9) | SI S3.4 bullets (with the one-line derivations) |
| Terminology-map row for region I: "accepted for every weighting under the scalarized protocol; typed rejection is a separate question" (was "robust infeasibility: rejected at every weighting") | SI S6 Table (terminology map) |
| Policy implication "Third": floors + reserve + protocol sufficient; floors alone not; aggregate without reserve and path data does not reconstruct | Discussion §7.3 detection paragraph; SI S6 checklist item "Mandatory reporting" |
| New section "Related work, and what is actually new here" | **New §6 "Related work, and what is claimed as new"** (`parts/04b_related.tex`): scalarization gap (Theorem 1(ii) is not new), adjustable/randomised robust optimisation (Ben-Tal et al. 2004/2009; Bertsimas–Goyal 2010; Wei–Zhang 2024; Delage–Kuhn–Wiesemann 2019 …), Kuhn 1953 vs path-wise worst case and Main–Randour 2024, weak/strong sustainability (Pearce–Atkinson 1993; Beckerman 1994; Daly 1995; Ayres et al. 2001; Dietz–Neumayer 2007; Neumayer 2013), four narrowed claims + explicit non-claims. The intro's "Position in the literature" was shortened to avoid overlap and points to §6. v70's internal inconsistency ("Theorem 9: blends close the gap exactly" in its related-work section vs the corrected abstract) is resolved: v71 uses the class-specific statement everywhere. |
| Author-contributions wording | Declarations: "A.A. conceptualized the entire work, wrote, reviewed and edited the manuscript." |
| Supplementary pointer | `paper06_assessment_separation_v71_supplementary` (.tex/.pdf) |
| Companion references to Zenodo DOIs | Obstruction calculus 10.5281/zenodo.22552616 (already present); ECOMOD companion marked "publication status not independently verified"; delay-dynamics companion (10.5281/zenodo.22554217) cited in SI S9 only |

## Not replicated from v70 (deliberate)
* v70's merged bibliography (entries inherited from the eleven-paper merge, several unrelated or incomplete). v71's bibliography is rebuilt from cited works only: 73 entries (v64: 53; +21 new for §6; −1 uncited after the intro was shortened, Cardaliaguet 1999).
* v70's assembly artefact in which `References` became a `\subsection*` inside "Proof of the rescue threshold".
* v70's unnumbered theorem-style paragraphs: all results are numbered environments here (numbering unchanged from v64: Theorems 1–4, Propositions 1–6, Lemmas 1–3, Remark 1; map to the v62–v70 numbering in SI Table S1).

## Supplementary Information
* S9 now reproduces the framework extensions of the v69 markdown supplement **in full** (extended definitions S9.1 with claim status, typed failure classes and the witness as a specialisation; governance constructors, implementability ladder, management vocabularies and the commons obstruction — Theorem S4 with hypotheses (H1)–(H3); intergenerational extension with the nested-impossibility theorem — Theorem S5 with proof; composition extension with each item's conditional status; planetary-boundaries note; nine declared conjectures with their preregistration discipline). v64's S9 had only a summary.
* S2 numbering map updated (v71 ↔ v62–v70; the SI theorem numbers in the map, S1–S5, now match the environments — v64's map had quoted the planned numbers S3/S6–S7); S3.4/S3.5 corrections as above; S6 terminology/checklist corrections.

## Page counts (tectonic 0.15, elsarticle preprint 11pt, A4)
main 47 pp. (v64: 40), supplementary 39 pp. (v64: 30). No undefined references; no overfull boxes above 8 pt.
