# Reader-draft phase changelog (2026-09-17)

Scope: Q4 directive — landmark-grounded, plain-prose re-expression of the three
papers as NEW versions (no frozen file touched).

Landmarks consulted (conventions extracted, abstracts re-read via web):
- Hutchings & Myers 1994 (CJFAS 51:2126): question-as-title; abstract = question
  -> evidence -> conclusion; plain causal sentences.
- Hyndman & Koehler 2006 (IJF 22:679): direct proposal voice ("we propose that
  the mean absolute scaled error become the standard measure"); scaled-error
  vocabulary that E1/F1 already use.
- USGS Edwards water-budget literature (SIR 2004-5277 conceptualization; Barton
  Springs water-balance studies): accounting-first framing, sources/sinks in
  percent, sensitivity listed flatly.
Style rules applied across all three drafts: define terms at first use; one
idea per paragraph; no chained clauses; every number with units; limits stated
with the same prominence as findings; no jargon beyond the frozen vocabulary
needed for referees (RMSE, tie band, comparator, vintage, conditional hindcast —
each defined on first use).

New files (nothing overwritten):
- e1/paperE1_cod_forecast_ladder_v51_reader_draft.md  (re-expresses frozen v50;
  numbers mirror claims-ledger canonical values)
- e3/paperE3_edwards_forecast_ladder_v17_reader_draft.md (re-expresses frozen v16)
- framework/paperF1_retention_framework_v27_reader_draft.md (re-expresses v26)
- arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v50.tex (staged
  copy of the frozen v50 tex for submission packaging; arena latex folder
  previously held no current E1 tex)

Not done / deferred (owner-visible):
- Drafts mark `[carried]` sections (data, model equations, tables, refs) to be
  transplanted verbatim at typesetting; full line-by-line plain rewrite of every
  carried section is a multi-turn job if the owner wants it.
- No PDFs built (no LaTeX toolchain in sandbox).
- Compliance note: prose re-ordering only; every numeric claim in the drafts
  traces to a frozen ledger row (claims_ledger.csv) — no restated numbers
  outside ledger precision.
