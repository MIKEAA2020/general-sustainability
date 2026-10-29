# Journal-revision evaluation

Start with [the journal-merit assessment](JOURNAL_CHANGE_ASSESSMENT.md). The [decision register](DECISION_REGISTER.csv) contains 107 evaluations of substantive changes and associated handling decisions across ECOMOD C10–C14 and follow-up F01–F02.

This is an author-facing evaluation, not a revised research article or journal submission. Existing manuscripts, supplements and published packages were not modified or replaced. The assessment distinguishes scientific merit from authorization and acknowledges gaps in the attribution of earlier edits.

## Evidence

- `diffs/`: 13 complete unified differences covering the available manuscript, SI, configuration and code transitions.
- `AUDIT.md`: the preceding factual inventory. Its judgments about retaining production-history statements in journal prose are superseded by `JOURNAL_CHANGE_ASSESSMENT.md`.
- `VERIFIED_COMPARISONS.json`: scoped file-identity checks and the identified T-versus-L mathematical inconsistency.
- `SOURCE_INVENTORY.json`: the inventory of 17 source snapshots used in the local forensic comparison. The inventory's `audit_copy` paths refer to that separate forensic package; full manuscript copies are not republished in this evaluation directory. Reconstructed C12 sources match the hashes in the published C13 provenance and can be reproduced by reversing its source patches.
- `ASSESSMENT_MANIFEST.json`: hashes for the assessment and register.
- `archive_manifest.json`: distributed archive file hashes and sizes, excluding itself.

The previously published C13 package is at `batch 9/agent 2/ecomod_c13_revision/`; C14 is at `batch 9/agent 2/ecomod_c14/`; the follow-up packages are under `batch 9/agent 2/ecomod_empirical_followup/F01/` and `F02/`.

The evaluation does not claim a fresh exhaustive empirical validation, author approval of a final manuscript, complete attribution of all earlier edits, or coverage of unavailable pre-C10 versions and the missing C11 SI.
