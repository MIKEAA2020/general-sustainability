# Workflow Continuity Correction

## Root issue

No workspace process, proof computation, or external dependency was interrupting execution. The affected turns were marked as stopped before completion when a subsequent user message arrived. The assistant also contributed to the appearance of repeated pausing by ending too many turns at intermediate status checkpoints instead of completing the requested bounded batch.

## Correction

1. Treat status reports as turn endings only after the requested bounded deliverable, validation, snapshot, and clean tracker check are complete.
2. When a hard gate is paused, produce the requested self-contained prompt **and** the internal provisional answer in the same bounded workflow when requested.
3. Keep provisional answers separate from manuscript implementation and register them for future joint adjudication.
4. State explicitly what is complete, what is intentionally gated, and what evidence controls each status.
5. Avoid claiming “finished” when only the currently feasible sub-batch is finished.
