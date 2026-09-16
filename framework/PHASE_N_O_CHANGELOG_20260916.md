# Phase N + O changelog — adoption-layer artifacts, literature, and the two decisions (2026-09-16)

Merit test applied: only items that are genuinely useful to a working analyst,
appealing to an editor/reviewer, and honest to the archive. Everything below
passes; each artifact is standalone-usable and zero-risk to the frozen numbers.
Main text untouched (v26); one sequence edit to the prospective Edwards DRAFT.

## Phase N — the adoption layer (S3 + schema)

- **O28 fillable information-set audit** → **S3.1**: the Section 3 columns as an
  empty form, with the three-way classification (available / supplied / revised)
  and the reading rules (supplied driver ⇒ conditional hindcast; revised row ⇒
  certificate expiry).
- **O26 machine-readable negative certificate** → **S3.2 + S3.3**:
  S3.2 is the human-fillable record (predictand, vintage, ladder, rule, band +
  basis, margins, gate decomposition, OC, N-level, expiry, archives);
  S3.3 is the companion script `certificate_schema_S3.py` — stdlib-only JSON
  validator enforcing the frozen verdict vocabulary, the N0–N3 levels, the
  band-basis vocabulary, and the rule that a declined module carries its
  class-grounds reason. Tested: blank template validates; bad verdict, missing
  reason, bad level all reject.
- Both commands/fields cross-referenced at Phase L's §2.2/S2, Phase M's S1.5,
  and §3a — one coherent stack.

## Phase O — literature positioning (S4)

- **O23** → **S4**: a comparison table + reading + 7 verified references, all
  checked against publisher records this session (White 2000; Hansen 2005;
  Hansen–Lunde–Nason 2011; Giacomini–White 2006; Clark–West 2007; Wellek 2010;
  Hyndman–Koehler 2006 — exact volumes/pages/DOIs/ISBN recorded). Descriptive,
  non-adversarial; states plainly that the three obligations are the article's
  only novelty claim and that a wide model search pairs with a reality-check /
  model-confidence-set correction.

## Governance decisions (root-cause, in-sheet)

- **O19 prospective class-grounds criterion** → DRAFT §3a (3-step: as-implemented
  reduction / s → 0 boundary / declaration-before-generation; approximate collapse
  is an OC question, not a veto).
- **Edwards E2m convention** → DRAFT §4, DECIDED **with-decline** (mirror the
  frozen protocol): the class-grounds decline is an analytical reduction, so a
  without-decline headline would measure a cell the protocol can never produce;
  the counterfactual is kept visible as sensitivity, never the adequacy target.
  Status line now finalisation-gated (2026-09-16); no open design element.

## What was deliberately NOT done

- Companion-side edits (E1/E3): owner-gated, untouched.
- Any re-simulation, band, OC, or verdict change: not in scope; frozen elements
  stand.
- A full reference implementation (O35) and third-party pilot (O34): recorded
  long-term, not run.

Scanners: all four green on the supplement; v26 + companion files untouched.
