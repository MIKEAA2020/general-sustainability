# Preservation recheck: previously unexamined version transitions

2026-10-01 · **Narrow source-preservation review, not a new scientific audit.**
The reviewed live heads remain the intended outputs. The earlier review compared
39 documented seed/predecessor pairs with an 8-word-window detector, but it did
not compare *every intermediate* draft or explicitly trace the four temporary
two-part papers back into both of their subsequent standalone destinations.
This pass reads those gaps, the previously unresolved combined-paper front
matter, and both source lineages for each supplement. A textual match is only
evidence of retention; it does not certify correctness or replace reading.

## Restored: combined paper09 title page and approved contribution

**Origin:** `paper09_cod_certification_v31.tex`, its cod v29 seed,
`paper09b_arv_certification_v2.tex`, and `paper10b_edwards_aquifer_v1.tex`
contain **the same literal** `Amin Abaee` author block, including
Independent Researcher, ORCID `0000-0002-0019-1842` and the source email.
**Loss:** the reviewed combined `paper09_cod_certification_v32.tex` contained
**zero active `\author` blocks**, an unfilled CRediT template, and two active
`\maketitle` commands (the second inside Part II). Its four original abstracts
were present and should not be deleted. The earlier preservation audit had
*noticed* the missing byline, but the repair sequence had not resolved it.
The owner has since expressly approved `Amin Abaee` and the exact sentence
“A.A. conceptualized the entire work, wrote, reviewed and edited the
manuscript.” No additional CRediT roles were inferred.

**Repair:** put the four-way-agreed source author block on the single combined
title page, put its one `\maketitle` before the combined abstract, remove the
second title call, replace the unfilled template with only the approved prose.
The merged work has no source-agreed publication date; `\date{}` prevents a
spurious current date from being printed. All **four** abstracts are bytewise
unchanged. Exact reviewed diff:
`../content_audit/unvisited/paper09_v32_front.patch`; source-anchored replay:
`../content_audit/unvisited/repair09_front.py`. Replaying that script from the
pre-repair snapshot reproduces the revised head byte-for-byte. Source-specific
structural gate: **0 live failing files, 0 live findings**; report-only
continuation detector: **0 live candidate fragments**. These checks do not
prove that every source sentence has been preserved. A TeX compiler was not
available in this workspace, so this edit has **not** been freshly typeset.

## Where the earlier 39 comparisons had not looked

A report-only five-word-window search examined **42 local intermediate
version→current-head pairs** for short disappeared passages, alongside the
existing 22 downloaded seed and supplement ancestors. It surfaced 293
candidate runs (including one-word label changes adjacent to a long math
passage), not 293 lost pieces of content. The current-head test is intentionally
sensitive and has false positives; the source-specific reading below governs.
The raw candidate list and executable method are in
`../content_audit/unvisited/short_loss_candidates.json` and
`short_loss_scan.py`. In particular the large apparent losses in the four
split articles are not prima facie deletions: the missing half was directed
to another paper. Here are the previously untested transfer checks:

| Temporary combined draft | Previously untested part | Destination head | Normalized 8-word-window carry-over of the part | Reading disposition |
|---|---|---|---:|---|
| paper01 v62 | Part II, belief-state sufficiency | paper02 v12 | **99.88%** | No missing long run; leading part/title markup differs. |
| paper03 v15 | Part II, measure-dual certificates | paper04 v16 | **99.74%** | One leading part/title/abstract boundary run; no long lost result. |
| paper05 v15 | Part II, worked-system exact audits | paper11c v2 | **99.79%** | One leading part/title/abstract boundary run; no long lost result. |
| paper06 v66 | Part II, typed ledger | paper10 v53 | **99.87%** | One leading part/title/section boundary run; no long lost result. |

These draft-specific **cross-part introductions and conclusions** do not occur
verbatim in the split standalone papers; they were written to argue *for a
two-part article*, so pasting them into only one standalone paper would falsely
claim both parts are present. Their sources remain preserved in v62/v15/v15/v66.
If grouping is reconsidered later, review those sections then; they are
**conditional reuse material, not omissions from the reviewed standalone
heads**. No paper grouping or theorem was changed in this pass.

Other short-loss candidates were read by source/version and destination:

- Paper02 v10's support-identity converse and selector notation remain in v12
  (for example §“The support identity and exact sufficiency”); short mismatches
  are reformatting/renaming. Paper03 v10's proposed independent certificate
  parser is superseded by v16's shipped `certificate_exchange_v1.py`; do not
  restore a now-obsolete “next step” as though it were still missing.
- Paper05 v10–v13's scaling-forward sentence was superseded by the five-cube
  analysis and qualified six-cube boundary in v16, not dropped accidentally.
  Paper11b v1's transferable-lesson paragraph was rewritten and expanded in
  v2's general finding and replication discussion, not lost; the same
  replication language also appears in combined paper11.
- Paper08 v42/v43 theorem/corollary leads changed numbering and environment
  syntax by v46. The older claim that the 6.50–6.73-year discretisation band
  made the crossing *parameter-robust* was explicitly superseded by the
  sensitivity band, not valid content to restore. Paper07 v49's two erroneous
  sensitivity descriptions likewise remain historical witnesses, not valid
  restoration material; their current copies were corrected in the previous
  pass.
- Five live supplement files were checked against the relevant old/new
  lineages: paper01's routes supplement, paper06's **actual** aggregate-index
  supplement, paper08's delay and both blinded/unblinded governance ancestors,
  and paper10's LaTeX ledger supplement. Long unmatched runs at their starts
  are retitling/“Accompanies” metadata, not missing sections; labels and
  figures transferred. Both paper08 supplements and paper06's supplement
  **exist**. An inventory of DOI tokens from all 15 documented seeds and
  immediate predecessors found **none absent** from their current heads;
  that limited check does not prove every reference entry complete.

## A second overlooked source: Markdown before LaTeX conversion

The earlier preservation scan began with `.tex` seeds, but two of those seeds
were rendered from **Markdown originals**. I fetched and compared the
repository's `paper4_delay_dynamics_v41.md` with its v41 LaTeX seed,
`paper3_material_ledgers_v50.md` with its v50 LaTeX seed, and
`paper3_supplementary_v18.md` with the v18 LaTeX supplement. At five-word
resolution neither of the two main texts has a long missing run; mathematical
markup and escaped identifiers produce many short misses. The supplement's
reproduction and accounting sections, including S9.3 and S17, are present in
both formats even though the TeX conversion inserts many `\allowbreak` tokens
inside code identifiers. Those tokens must not be mistaken for missing
reproducibility records. The older `paper5_sampled_governance_v26.md` was also
inspected against the much later unblinded v46 LaTeX: its 36 headings have
counterparts but substantial wording was rewritten over **20 versions**;
this is **not a demonstrated loss**, and old interpretations are not copied
back without version-specific adjudication.

**Confirmed conversion damage, restored in one place:** in the v18 supplement
Markdown, S16 says plainly that three of S7's “discharged by” pointers name
sections that no longer carry the cited statements, and explains how to read
the four-row table. In the v18 `.tex` seed and current paper10 supplement,
Markdown inline-code parsing swallowed almost the whole sentence into a
mangled `\texttt{discharged b\allowbreak{}y ... }Typed` fragment. The prior
TeX-seed-to-live comparison correctly reported that the two `.tex` files
agreed, but **could not detect corruption that had already entered the seed**.
I restored only this lead-in from the original Markdown; the S16 heading,
all four table rows, and every other section remain unchanged. Exact diff:
`../content_audit/unvisited/paper10_supp_s16.patch`; anchored repair script:
`../content_audit/unvisited/repair10_s16.py`. After this intentional repair,
the old `.tex`-seed-to-live 8-word-window score drops from **100% to 99.32%**:
its sole long mismatch is the **79-word window around S16**, because the bad
seed text was replaced by the older Markdown original. Zero missing headings
or labels. This is legibility/content preservation, **not a new mathematical
result**. The Markdown source itself
contains other pre-existing copyediting blemishes; those are not evidence of
conversion loss and were not silently rewritten.

## Scope limit and next boundary

The two confirmed repairs in this pass are **paper09's inherited byline and
approved contribution** and **paper10 supplementary S16's source-to-LaTeX
conversion damage**. No further *long-form* missing result was identified in
the examined documented lineages and intermediate split halves. This is not
a declaration that every sentence in every historical repository file is
equivalent: older Markdown ancestry (particularly sampled-governance v26 to
v46), brief altered clauses, unlisted drafts, and bibliographic attribution
require separate source-specific adjudication. The paper09 merge producer still does **not** regenerate the reviewed
byline and previous bibliography repairs safely. It now compares its proposed
output with the reviewed v32 **before any write** and fails closed on the
mismatch. An executed negative test returned the intended refusal while the
reviewed head retained SHA-256 `26205a25da4b554c272e911ecf2c96e5e44ef9b50aa8c7fbeca8a1da57b0ffe7`.
This is protection, **not a completed reproducible upstream rebuild**.
No all-paper scientific claim audit was resumed.
