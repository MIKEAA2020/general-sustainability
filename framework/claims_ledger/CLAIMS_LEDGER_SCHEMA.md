# Claims Ledger — Schema (v1, 2026-09-17)

Purpose: one canonical registry mapping every factual claim that lives in more
than one paper (F1 framework, E1 cod companion, E3 Edwards companion) to a single
owning paper, its printed value, and the archived file that authorizes it.
Kills two verified defect classes: (a) duplication drift (same result restated
with divergent rounding — the 3.22-kt class) and (b) pass-confusion (the
z=1.21-vs-0.99 class). Also enforces the anti-circularity citation rule
structurally.

## File
`framework/claims_ledger/claims_ledger.csv` — one row per claim. Seed rows only;
rows are added (never edited) as papers change; corrections append a replacement
row with a new `claim_version` and a `supersedes` pointer. Frozen artifacts
(data archives) are never modified; this ledger describes them.

## Columns

| column | meaning |
|---|---|
| claim_id | stable key, `CL-<domain>-<topic>` (see namespaces below) |
| claim_version | integer; bump on any change; old row kept with status=superseded |
| claim_type | `domain_fact` / `instrument_property` / `rule_verdict` / `archive_pointer` |
| statement | canonical short text of the claim (≤200 chars, no paper-specific rounding) |
| owning_paper | `E1` / `E3` / `F1` / `ARCHIVE` (archive = not yet a paper claim) |
| owning_location | section/table in the owning paper as of `as_of_version` |
| as_of_version | owning paper version the location refers to |
| value_printed | the value exactly as printed in the owning paper (with its rounding) |
| value_canonical | full-precision value the ledger treats as authoritative (from archive) |
| archive_file | workspace path of the authorizing archived file (may be itself a CSV row) |
| archive_row_key | row/column selector inside the archive file (free text) |
| archive_md5 | md5 of archive_file at seeding (empty if file not archived yet) |
| allowed_citers | semicolon list of papers allowed to cite this claim, per direction rule |
| cross_mention_rule | allowed form in citing papers (default: "one sentence + section/table pointer; never restate numbers") |
| status | `frozen` / `pending_campaign` / `parked` / `superseded` |
| last_verified | date the (printed vs archive) check last passed |
| notes | class of risk it controls, supersession pointers, campaign ids |

## Direction rule (anti-circularity)
- Companions (E1, E3) cite F1 only for `instrument_property` and the unified-rule
  algorithm itself.
- F1 cites companions only for `domain_fact` and `rule_verdict` under-their-own-frozen-protocol.
- FORBIDDEN: a companion citing F1's synthesized verdict as independent support
  for its own verdict. Such rows may not be created.
- `archive_pointer` rows may be cited by anyone but only as data provenance.

## Namespaces
`CL-COD-*` (E1 domain), `CL-EDW-*` (E3 domain), `CL-INST-*` (F1 instrument),
`CL-ARC-*` (archive pointers incl. vintages), `CL-RULE-*` (rule-verdict rows
recording rule-version differences, e.g., E3 point-rule vs unified rule).

## Verification protocol
Each cross-check pass recomputes (printed value) vs (archive value at
archive_row_key, md5 re-verified) and timestamps `last_verified`. A mismatch
opens a flag in COMPANION_CROSSCHECK; fixes follow the new-version rule.
