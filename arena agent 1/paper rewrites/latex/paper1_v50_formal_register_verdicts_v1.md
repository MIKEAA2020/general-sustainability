# Paper 1 corpus (v50 / suppl v6 / EMS v8 / master v2) — formal-register pass (v1)

**Scope.** Removal of internal dialogue, change-logs, version narration,
and process commentary from all reader-facing artifacts, per the
formal-academic-writing requirement. Domain vocabulary ("audit layer",
"audited snapshots", independent-audit framing of the checker) is
scientific content and was retained. Required declarations
(AI-assistance disclosure in the acknowledgements) were retained.

**Changes.**
- `paper1_assessment_separation_v50.tex`: provenance comment header
  replaced by a neutral header (title, deposit DOI, compile note).
  Rendered text unchanged (verified identical to v49).
- `paper1_supplementary_v6.md`: "(manuscript v7, … submission)" →
  "(Environmental Modelling & Software)"; internal-reference note now
  covers S1–S12; the "Changes from the v3 supplement: …" change-log
  sentence removed (it also carried a stale 58-tests count); S8 citation
  entry "(software description; venue-agnostic master v1; … v7)" →
  "(software description; Environmental Modelling & Software)"; "the
  audit's reference design" → "the reference certificate design";
  "*New in supplementary v5.*" dropped from S12.
- `paper1_safetransition_ems_v8.tex` and
  `paper1_safetransition_master_v2.tex`: lineage/change-log comment
  headers replaced by neutral headers; companion titles cited without
  version numbers. Rendered text unchanged (verified identical to v7/v1).
- Deposit README: "the journal-neutral form implementing the best audit
  suggestions across venues" → neutral phrasing; verdicts reports
  removed from the public deposit (`pkg/manuscripts/`, stage dirs) and
  kept in the internal archive (workspace `latex/`, GitHub repo).
- New: `paper1_ems_cover_letter_v1.txt`;
  `paper1_safetransition_ems_v8_highlights.txt`; stage packages
  `stage/paper1_ems_v8/`, `stage/master_v2/`.

**Verification.** All three PDFs compiled clean (34/16/16 pp.); rendered
text of each is byte-identical to its predecessor; diary-token sweep
(lineage, changelog, revision, joint-audit, grok/gemini, re-assessment)
clean on all rendered texts and on suppl v6.
