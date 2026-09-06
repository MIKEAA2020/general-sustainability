#!/usr/bin/env python3
"""Wave-9 build: paper4_delay_dynamics_v30.md.

Owner directive (LaTeX/PDF pass) surfaced one latent markdown defect: the
'**Status.**' paragraph of Section 9.6 (the scaffold-companion record
statement) is followed directly by a '---' separator line with no blank
line between, so markdown parsers (including pandoc) read the pair as a
setext H2 heading - the entire paragraph renders as a section heading
(and pandoc duplicates it into \\texorpdfstring PDF bookmarks). The fix:
insert one blank line between the paragraph and the separator, so the
paragraph stays a paragraph and the '---' becomes a horizontal rule as
in the other papers. Exactly one blank line inserted; everything else
byte-identical (all table rows and every other line asserted unchanged).
Fail-loud; run twice to pin the MD5.
"""
from __future__ import annotations
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
SRC = PR / "paper4_delay_dynamics_v29.md"
DST = PR / "paper4_delay_dynamics_v30.md"

lines = SRC.read_text(encoding="utf-8").splitlines()

# Locate the accident: a '---' separator directly after a non-blank line.
hits = [
    i
    for i, l in enumerate(lines)
    if l.strip() == "---" and i > 0 and lines[i - 1].strip()
]
assert len(hits) == 1, f"expected exactly one setext accident, found {len(hits)}: {hits}"
idx = hits[0]
status_line = lines[idx - 1]
assert status_line.startswith("**Status.** These are registered, verified numerical records"), (
    f"unexpected paragraph before separator: {status_line[:100]!r}"
)

fixed = lines[:idx] + [""] + lines[idx:]
out = "\n".join(fixed) + "\n"
DST.write_text(out, encoding="utf-8")

# Post-conditions: one line inserted; the Status paragraph and the '---'
# both present; all table rows byte-identical; no other change.
assert len(fixed) == len(lines) + 1
assert fixed[idx - 1] == status_line
assert fixed[idx] == ""
assert fixed[idx + 1] == "---"
table_rows_src = [l for l in lines if l.strip().startswith("|")]
table_rows_dst = [l for l in fixed if l.strip().startswith("|")]
assert table_rows_dst == table_rows_src, "table rows changed"

md5 = hashlib.md5(DST.read_bytes()).hexdigest()
print(f"wrote {DST}")
print(f"lines: {len(fixed)}  (v29: {len(lines)})")
print(f"inserted blank line before separator at line {idx + 1}")
print(f"MD5: {md5}")
sys.exit(0)
