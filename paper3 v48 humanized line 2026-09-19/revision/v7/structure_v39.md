# Structure record — main text v39 and supplementary v10

Article: `revision/v7/paper3_material_ledgers_v39.{md,tex,pdf}` — 32,900 words, 62 labels, 55 typeset pages.
Supplementary: `revision/v7/paper3_supplementary_v10.md` — 7,813 words (v9 was 5,809).
Builder: `revision/v7/build_v39_kernel.py` · log: `revisions_v39_kernel_log.json` · gate:
`verify_v39_build.py` (**ALL CHECKS PASS**) · structural measurement: `review/split_graph_v1.py` ·
verdict: `review/corpus_and_split_v1.md`.

## Why this version exists

The question was whether v38 should be split into two papers, or have parts demoted to the supplementary. The
answer was measured, not asserted: the label-citation graph of v38 has sections {2,3,4,5,6,7,10} in a single
strongly connected component containing all 61 numbered statements, with 21 of 21 section pairs mutually
reachable — so no clean cut exists. The same measurement found four sections carrying words and no labels, and
one of them (§9) turned out to hold a theorem-shaped claim in prose. v39 therefore demotes what has no results in
it and promotes what does.

## Edits, all logged so v39 → v38 reverses byte-for-byte in md and tex

| id | edit |
|---|---|
| D3 | the §3.7 remark's pointer "the statistical standards recalled in Section 1.5" re-aimed at §1.2, where that paragraph actually sits — a dangling internal reference inherited from v38, and the reason this round added an internal-pointer resolution check to the gate |
| D0 | §6.5.2's dagger note repointed from "the full quarantine record is the paragraph below" to "its full provenance is the supplementary's S5.4" — required by D1, since D1 moves the paragraph it named |
| D1 | §6.5.2 basin-row provenance (149 w) moved verbatim to supplementary **S5.4**; the article keeps the classification sentence, the table, the dagger note and a pointer |
| D2 | §8.1 and §8.2 (198 w) moved verbatim to supplementary **S14**; each condensed in the article to registered status + admitted object + declared gap, with pointers to S2 (the ladders themselves) and S14 (the detail) |
| P1 | §9's exact-projection claim promoted to **Proposition 43** with a two-line proof; the semiconjugacy to the companion's three-state core stays attributed to paper 4 and explicitly not re-proved |
| note | the numbering note's added-label list runs "39–42" → "39–43"; the maxima are now Definition 47 / Proposition 43 |
| manifest | `revision/v7/code/MANIFEST.md` at v2: the relabelling table above, versions, run command, and the scope limits rewritten against v39's loci; the supplementary's S9.3 needed no change because it names files, not versions |
| supp | supplementary **v10** = v9 verbatim + Part III: S10 identifiability table, S11 MEV table, S5.4, S14, S15 (`Typed` row citing Definition 47 and Proposition 42), S16 (S7's discharge column restated against v39) |
| code | exhibit bundle at **v2** (`revision/v7/code/`): same three scripts, printed loci restated against v39 (`Section 7.1` → `Section 10.1 and supplementary S8`; `(S8.1..3)` → `(main text 6.5.1..3)`), fresh `outputs.txt`, and `make_bundle_v2.py` performing and asserting the substitution. The v5 bundle is untouched |

## What deliberately did not change

Nothing was deleted; the demoted text is re-emitted verbatim in the supplementary, with its deictics explained in
the S5.4 preamble rather than silently repaired. The article's component structure is unchanged, the abstract and
§1 are unchanged, and no number in §6.5 moved. The paper did not get shorter (+40 words): the point of the
version is that no load-bearing claim is unlabelled and no unlabelled claim is load-bearing.

## Gate, in summary

`verify_v39_build.py`: five logged edits reverse v39 → v38 exactly in both formats; 62 labels, md and tex
sequences identical, no repeats; maxima as expected; numbering note updated with no stale "39–42" anywhere;
Proposition 43's headline, proof line, one-way clause and deferral sentence present in both formats; the two
demoted blocks verbatim in the supplementary, absent from the body, and verbatim in v38; supplementary v10
contains v9 verbatim plus two Parts' headings; every `Section n.m` pointer in the article resolves (the one
bibliographic exception, the GFN Guidebook's Section 9.1.2, excluded by rule); no "paragraph below" left in
either document; PDF 55 pages, no unresolved references, two underscores as expected (the e-mail address).

## Companions written this round

- `companionA_certification_procedure_v1.{md,tex,pdf}` — methods/software, 4,828 words, 10 pp.: the eight
  obligations as decision procedures (Protocol 3, with cost and exit conditions), the three LPs as solver-ready
  recipes (Protocols 4–6), the report contract (Protocol 7), the three-test vintage protocol (Section 7 +
  Protocol 8), the v2 bundle and its relabelling record, what the tool cannot buy, and the deposition advice.
- `companionB_standards_horizon_v1.{md,tex,pdf}` — commentary, 2,985 words, 6 pp.: B1–B18 on the 2025 SNA
  recording change, the three steps from a rate to a horizon, the τ_agg exhibit and the carbon zero-row
  convention, eligibility and reclassification, citation hygiene with a concrete draft-vs-published numbering
  drift, and the one un-run computation that would make this a full paper.
- Gate for both: `verify_companions_v1.py` — the shipped tex rebuilds byte-identically from the shipped md;
  Protocol 1–8 and B1–B18 gap-free; every cited main-text label and section resolves (in v39 or in supp v10);
  every run-record number quoted is in `code/outputs.txt`; ASCII-only tex, no unescaped `$`, no markdown
  leakage, balanced environments; track claim budget enforced; PDFs clean. **ALL CHECKS PASS.**
