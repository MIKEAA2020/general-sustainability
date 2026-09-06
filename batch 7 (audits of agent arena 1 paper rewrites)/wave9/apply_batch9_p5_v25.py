#!/usr/bin/env python3
"""Wave-9 build: paper5_sampled_governance_v25.md.

Owner directive: P5 Figure 1's legend superimposed on the title; the
regenerated figure is figs_p5/fig1_crossing_record_v25.png (legend moved
above the title; data unchanged - see make_fig_p5_v25.py). This build
creates paper5_sampled_governance_v25.md from v24 with exactly ONE line
changed: the Figure 1 image reference (line 268),
  ![Figure 1](figs_p5/fig1_crossing_record_v24.png)  ->
  ![Figure 1](figs_p5/fig1_crossing_record_v25.png)
Everything else is byte-identical (the Figure 1 caption and all table
rows are asserted unchanged). Fail-loud; run twice to pin the MD5.
"""
from __future__ import annotations
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
SRC = PR / "paper5_sampled_governance_v24.md"
DST = PR / "paper5_sampled_governance_v25.md"

OLD = "![Figure 1](figs_p5/fig1_crossing_record_v24.png)"
NEW = "![Figure 1](figs_p5/fig1_crossing_record_v25.png)"

text = SRC.read_text(encoding="utf-8")
assert text.count(OLD) == 1, f"expected exactly 1 figure reference, found {text.count(OLD)}"
assert NEW not in text, "v25 reference already present in v24?"

# Table rows and caption must survive byte-identically: capture them now.
table_rows = [l for l in text.splitlines() if l.strip().startswith("|")]
caption = [l for l in text.splitlines() if l.startswith("**Figure 1.**")]
assert caption, "Figure 1 caption paragraph not found"

out = text.replace(OLD, NEW)
assert out != text, "no change applied"

# Post-conditions: exactly one line differs.
src_lines = text.splitlines()
out_lines = out.splitlines()
assert len(src_lines) == len(out_lines), "line count changed"
diffs = [(i, a, b) for i, (a, b) in enumerate(zip(src_lines, out_lines)) if a != b]
assert len(diffs) == 1 and diffs[0][1] == OLD and diffs[0][2] == NEW, f"unexpected diff: {diffs}"

out_table_rows = [l for l in out_lines if l.strip().startswith("|")]
assert out_table_rows == table_rows, "table rows changed"
out_caption = [l for l in out_lines if l.startswith("**Figure 1.**")]
assert out_caption == caption, "Figure 1 caption changed"

DST.write_text(out, encoding="utf-8")
md5 = hashlib.md5(DST.read_bytes()).hexdigest()
print(f"wrote {DST}")
print(f"lines: {len(out_lines)}  (v24: {len(src_lines)})")
print(f"changed line {diffs[0][0] + 1}: {OLD} -> {NEW}")
print(f"MD5: {md5}")
sys.exit(0)
