# Loss Audit — v35 vs. the full lineage (one-stock negative results, expository, scientific)

**Scope:** Did `manuscript_ECOMOD_v35.tex` (the submission version) lose any *one-stock
negative-result phrasing*, *expository* content, or *scientific* content relative to the prior
versions (v30–v34) and the one-stock revision lineage (v18+, now retained in the SI as the
one-stock comparator)?

**Method:** structure (section/subsection/table/figure/label) counts, word-level
`difflib` diff (v34→v35), targeted grep of the manuscript + `supplementary/SUPPLEMENTARY_information_v2.md`
for every one-stock negative result, reference-list ↔ in-text citation cross-check, and reads of the
Conclusions and the existing `audits/` content-loss reports.

---

## Headline verdict

**No substantive content loss.** v35 is a strict superset of v34 in *content*; it intentionally
replaces the title, rewrites the abstract, and *adds* the v13 recommendations (recursive
identifiability, corrected scalar-projection anchor, §1 indicator paragraph, operationalised policy
rule, endpoint/path fix). The one-stock negative results, the expository motifs, and all scientific
results are retained — the one-stock material is deliberately kept in the SI as a *comparator/limit*,
exactly as the paper states.

---

## 1. One-stock negative-result phrasing

| One-stock result (v18/v19) | In v35 (main) or SI? | Where |
|---|---|---|
| No Hopf / no imaginary-axis crossing | ✅ | SI §S (line 169): "monotone positive-real eigenvalue with no imaginary-axis crossing… no Hopf" |
| Monotone positive-real leading eigenvalue (+0.625 / +0.62) | ✅ | SI (line 169, 203): "leading Re λ = 0.608–0.625 … 0.625 (constant)"; main title footnote |
| No critical slowing down | ✅ | Main §Results (line 268) + SI (line 280): "no critical slowing down" |
| No sustained limit cycle | ✅ | SI (line 728): "no-Hopf, no-limit-cycle"; (line 735) |
| No Allee rescue threshold (no rescue zone) | ✅ | SI §negative-results table (line 755) |
| No hysteresis (no bistability per fixed E, no path dependence) | ✅ | SI negative-results table |
| Neutral continuum / one-parameter equilibrium family `P=B(A)/e` | ✅ | SI (line 150): "one-parameter family of equilibria … a neutral continuum" |
| Basin recover-fraction collapse 39.9% → 5.3% (τ_g ≈ 20 yr cliff) | ✅ | SI (line 205) recover-fraction table: `0.399 → 0.394 → 0.240 → 0.0529` (same numbers, fraction form) |
| τ_g cliff is an ≈18–20 yr band, not a single edge | ✅ | SI (line 207) |
| Rate/lag decoupling (ρ sets *how long*, τ_g sets *whether*) | ✅ | SI §S5.3a (-lines 314–316) + main regeneration-timescale paragraph (line 537) |

No one-stock negative-result phrasing was lost. The only phrasings not present verbatim are the
basin fractions written as percentages (`39.9%`, `94.7%`) — they appear in the SI as fractions
(`0.399`, `0.0529`), which carry identical information.

---

## 2. Expository content

- **Orchard/ground, fast-vs-ecological-capital analogy:** retained (7 "orchard" instances).
- **Elevator/cable everyday analogue:** retained (2 instances).
- **"two kinds of ground," "fruit vs. trees," "kill hens," "cut branches":** retained in the
  Introduction.
- **Falsifiable-predictions framing and the "not a forecast"/"two registers" statements:** retained.
- **NFA-limitation and information-layer paragraphs:** retained (main §Limitations + SI).
- **Symbol table before equations, assumption-before-equation (§3):** retained.

---

## 3. Scientific content

- **Structure counts identical v34 ↔ v35:** 16 `\section`, 13 `\subsection`, 5 `\label{tab:}`,
  1 `\label{fig:}`, 6 `\begin{table}`, 1 `\begin{figure}`.
- **Word-level diff v34 → v35:** the **only** v34 span not present in v35 is the old title string
  ("Composition Illusion: Two-Land Conversion…") — an intentional replacement. v35 *adds* 6
  insertion-spans (abstract rewrite + the v13 insertions). No equation, table row, label, citation,
  or numeric result was deleted.
- **Distinctive numeric quantities present in v35:** `2.85, 1.17, 2.43, 1.008, 1.024, 0.207, 0.219,
  +23.0%, +24.5%, 0.718, 1.782, 1971, +464%, −364%, 1.138, 0.0537, 0.08, 1.110, 0.626, 0.385, 0.143,
  0.070, 2.41, 2.70, 2.98, 3.14, 1.21, 5.39, 0.128`.
- **Reference integrity:** every in-text citation has a reference entry, and every reference is cited
  (the few "orphan-looking" surnames — `Ausubel, Grazi, Rees, Saltelli, van` — are second authors in
  `Meyer & Ausubel`, `van den Bergh & Grazi`, `Wackernagel & Rees`, `Giampietro & Saltelli`,
  `van den Bergh`; `United Nations`/`Land Use Harmonization` are dataset/institution names).

---

## 4. Places checked that prior audits may not have

- **v34 → v35:** new word-level diff (above) — clean.
- **Existing `audits/v33_vs_v34_CONTENT_LOSS_AUDIT.md`:** verdict was already "no accidental content
  loss" (the v34→v33 cleanup removed only change-log / self-referential / informal-chat language).
- **Reference ↔ citation consistency:** verified (above).
- **Conclusions:** verify it states the three departures, the identifiability result, the empirically
  anchored cropland book (2.85× / 1.17× / 2.43×), the endpoint vs. intra-period distinction, and
  retains the "orchard quietly shrinks" closing metaphor — all confirmed.
- **Figure dependency:** v35 references exactly one figure
  (`real_series_aggregation_face.png`); the SI figures (S1–S15) are separate and not `\includegraphics`'d
  in the main `.tex` (referenced only as a package). No dangling `\includegraphics` path.

---

## Residual note (intentional, not a loss)

The one-stock model itself is **not** in the main body — it is deliberately retained in the SI as a
*comparator/limit* (the paper states this explicitly). This is the intended design of the two-land
manuscript, not an accidental removal. If you ever want any one-stock result promoted into the main
body (e.g., the recover-fraction table or the +0.625 eigenvalue), that would be an *addition*, not a
recovery of lost content.
