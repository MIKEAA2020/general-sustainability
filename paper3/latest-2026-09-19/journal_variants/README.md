# Journal-specific submission variants

These are new working surfaces derived from the immutable v49 full-length line. They do not alter `revision/v49/`'s shipped article, package or archive branch.

## Contents

- `paper3_JIE_submission_v1.md` — Journal of Industrial Ecology cut, checked against a 6,000-word body limit. It leads with MFA, typed material stocks/flows, closure, double-counting and application classifications. Proofs are delegated to `technical_supplement_v1.md`.
- `paper3_EE_submission_v1.md` — Ecological Economics cut, checked against an 8,000-word body limit. It leads with weak/strong sustainability, weak comparability, noncompensatory aggregation, natural-capital drawdown and policy meaning. It deliberately does not promote the regime interpretation to a theorem.
- `technical_supplement_v1.md` — technical extracts of the full-length article's proof-bearing sections, copied verbatim from the v49 source, plus a map to the full-length sections.
- `assets/typed_ledger_readout.svg` and `.png` — the new restrained framework/productivity-illusion figure used by both cuts.
- `route_c_prototype/` — a dependency-free, tested core declaration prototype for a possible Environmental Modelling & Software route. It is explicitly not yet a supported package.
- `validate_journal_variants.py` and `journal_variants_validation.json` — word-limit/content/asset gate.

## Count rule

The validator removes inline and display math and counts word-like tokens before `## References`. This is a working gate, not a journal's final copy-editor count. It reports both cuts below their requested ceilings; references, figure captions and supplementary material are separate.

## Full-length deposit route

The authoritative full-length manuscript remains the v49 four-document set under `revision/v7/` and the validated v10 archive. The Figshare-ready deposit should include that full-length set, the full technical supplementary, the target-specific cuts, the figure assets, the code and analysis records under `revision/v7/code/` and `revision/v7/analysis/`, and the metadata/checksum file generated for the deposit. No Figshare upload is attempted here because no Figshare credential or destination record was supplied.
