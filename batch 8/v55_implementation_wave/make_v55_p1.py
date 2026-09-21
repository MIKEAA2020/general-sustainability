#!/usr/bin/env python3
"""make_v55_p1.py — build paper1_assessment_separation_v55.tex from v54.

Task 110 / batch 8 / paper 1. The owner's second directive this round:
"an optional Section 1.3 contributions item for Section 5.9 if
genuinely merited." The adjudication (recorded in
batch 8/v55_implementation_wave/IMPLEMENTATION_RECORD.md section 1):
MERITED, on four grounds —

  (a) parity precedent: Section 1.3's item (xi) already covers the
      Section 5.8 labelled extension (added in v53); Section 5.9 is the
      same format (a labelled extension with machine-verified theorems)
      and omitting it leaves the contributions list asymmetric between
      the paper's two labelled extensions;
  (b) main-text load: Section 5.9's results are load-bearing in the
      main text — Table 5's middle cell and row (iii) carry its
      computed verdicts (Section 5.4), Section 5.7 carries the
      kappa* trichotomy with a prescription change, Section 4.10
      carries the blend-fragility caveat — a list that enumerates (xi)
      but not the extension that filled a main-text table understates
      the paper;
  (c) the v54 implementation record itself recorded the additive item
      as "a one-line option" (its section 4);
  (d) the owner delegated the merit call ("if genuinely merited").

The edit: ONE anchored, position-recorded insertion — the new item
(xii) appended to the contributions paragraph after item (xi), citing
Section 5.9 by its label (mirroring (xi)'s citation style for 5.8) and
claiming ONLY what Section 5.9, Table 5, Section 5.7 and Section 4.10
already state (Theorems M1-M4 + CT, the 1/2-cut, the rescue trichotomy
with the v54 notation, the class-conditional blend caveat, the
reading-conditional coupled theorems, the fourth-check-list
verification). No new claims, no new numbers.

Standing rules honored: new version only (never overwrite); NO content
removed or condensed — the wave is purely additive (SUPERSEDED is
empty); fail-loud anchored edit with the inverse-reconstruction gate
proving the diff is exactly the one enumerated edit; math-span multiset
preserved (v54's spans intact, zero alterations). Idempotence is
enforced by the destination-exists gate. Exit 0 on success.
"""
import sys
from pathlib import Path
from collections import Counter
import re

HERE = Path(__file__).resolve().parent
LATEX = HERE.parents[1] / "arena agent 1" / "paper rewrites" / "latex"
SRC = LATEX / "paper1_assessment_separation_v54.tex"
DST = LATEX / "paper1_assessment_separation_v55.tex"


def die(msg: str):
    print(f"FAIL: {msg}")
    sys.exit(1)


text = SRC.read_text(encoding="utf-8")
orig = text
PAIRS = []   # (name, pos, anchor, repl) for every operation
STATES = []  # the full text after each edit (drives the inverse gate)


def edit(name: str, anchor: str, repl: str, count: int = 1):
    global text
    n = text.count(anchor)
    if n != count:
        die(f"anchor [{name}] found {n}x (expected {count}):\n---\n{anchor[:200]}\n---")
    pos = text.index(anchor)
    text = text[:pos] + repl + text[pos + len(anchor):]
    PAIRS.append((name, pos, anchor, repl))
    STATES.append(text)
    print(f"  ok  {name}")


# Nothing is superseded in this wave (purely additive; the supreme rule).
SUPERSEDED = {}

# =====================================================================
# The one edit: item (xii) appended to the contributions paragraph.
# =====================================================================
print("== the Section 1.3 contributions item (xii) for Section 5.9 ==")
edit(
    "item (xii) after item (xi)",
    "and two machine-anchored theorems (S1 nesting; S2 the\ntwo-sided Leontief punchline).\n",
    "and two machine-anchored theorems (S1 nesting; S2 the\ntwo-sided Leontief punchline). (xii) A labelled common-shock\n"
    "extension of the witness datum\n"
    "(Section~\\ref{common-shock-variant}): the middle-regime disturbance\n"
    "verdict of Table~\\ref{tab:disturbance} computed exactly (the\n"
    "acceptance gap survives the common shock,\n"
    "reduced by the exact \\(1/2\\)-cut, licensing thresholds unshifted\n"
    "on the surviving region), the class-conditional rescue trichotomy\n"
    "(\\(\\kappa^* = 0\\),\n"
    "\\((1 - x)_+\\), or \\(\\infty\\), with the first\n"
    "unrescuable-by-reserve failure states on this datum), the\n"
    "class-conditional caveat on the blend collapse (Theorem 9's window,\n"
    "not blend-closed on the fragile band), and two exact\n"
    "reading-conditional theorems for the coupled regime (the additive\n"
    "gap relocating rather than vanishing; the replace reading\n"
    "collapsing the typed/weak distinction itself) --- machine-verified\n"
    "as a fourth check list.\n",
)

# ============ verification gates ============
print("== verification gates ==")
if text == orig:
    die("no edits applied")
if DST.exists():
    die(f"destination already exists (never overwrite): {DST}")

# gate 0: the frontmatter (title, abstract, highlights) is untouched —
# the edit lies in Section 1.3, far beyond it
fm = orig.index("\\end{frontmatter}")
if not text.startswith(orig[:fm + len("\\end{frontmatter}")]):
    die("frontmatter altered (abstract/highlights must be untouched)")
print("  ok  frontmatter (title/abstract/highlights) untouched")

# gate 1: every original math span preserved verbatim (multiset
# containment), with ZERO alterations (the wave is purely additive)
def spans(s):
    return Counter(re.findall(r"\$\$.*?\$\$|\\\(.*?\\\)|\\\[.*?\\\]", s, flags=re.S))


o, n = spans(orig), spans(text)
missing = o - n
if missing:
    die(f"original math spans lost/altered (none allowed this wave): {dict(missing)}")
print(f"  ok  math-span multiset preserved (v54: {sum(o.values())} spans all "
      f"intact; v55 adds {sum((n - o).values())} new spans; zero alterations)")

# gate 2 (the strongest no-removal check): inverse-reconstruction.
# Reverting the one enumerated edit at its recorded position must
# reproduce v54 byte-identically.
t = text
for k in range(len(PAIRS) - 1, -1, -1):
    name, pos, anchor, repl = PAIRS[k]
    if STATES[k] != t:
        die(f"inverse gate: state mismatch before reverting [{name}]")
    if t[pos:pos + len(repl)] != repl:
        die(f"inverse gate: replacement not at recorded position [{name}]")
    t = t[:pos] + anchor + t[pos + len(repl):]
if t != orig:
    i = next((j for j in range(min(len(t), len(orig))) if t[j] != orig[j]), min(len(t), len(orig)))
    die(f"inverse-reconstruction mismatch at byte {i}:\n  orig: {orig[i:i+120]!r}\n  rev : {t[i:i+120]!r}")
print(f"  ok  inverse-reconstruction: reverting the {len(PAIRS)} enumerated edit "
      f"reproduces v54 byte-identically (the diff is exactly the item)")

# gate 3: the new-content markers, with the expected post-edit counts
# (every expectation = the audited v54 count + 1, or unchanged)
for marker, cnt in [
    ("(xii)", 1),
    ("\\ref{common-shock-variant}", 1),      # the new label reference
    ("fourth check list", 2),                # 5.9's own + the item
    ("unrescuable-by-reserve", 3),           # 5.7 x2 + the item
    ("rescue trichotomy", 3),                # 5.7 x2 + the item
    ("not blend-closed on the fragile band", 1),
    ("blend-closed", 5),                     # 4 + the item
    ("fragile band", 3),                     # 2 + the item
    ("reading-conditional", 7),              # 6 + the item
    ("class-conditional", 8),                # 6 + the item x2 (trichotomy, caveat)
    ("reduced by the exact \\(1/2\\)-cut", 3),  # 2 + the item
    ("Section 5.9", 8),                      # hardcoded refs unchanged
    ("Section 5.8", 1),                      # unchanged
]:
    c = text.count(marker)
    if c != cnt:
        die(f"marker {marker!r} found {c}x (expected {cnt})")
print("  ok  all new-content markers present with the expected counts")

# gate 4: the scope paragraph after the contributions is intact and the
# paragraph structure is unchanged (one paragraph, items (i)-(xii))
if "\\textbf{Scope.} No universal ranking" not in text:
    die("the Scope paragraph after the contributions list is missing/changed")
if text.count("\\textbf{Contributions.}") != 1:
    die("the contributions paragraph header count changed")
print("  ok  contributions paragraph structure intact (items (i)-(xii); Scope unchanged)")

# gate 5: nothing else moved — the only difference beyond the inserted
# item is nothing at all (already proven by the inverse gate); record
# the line delta
print(f"\nv54: {len(orig.splitlines())} lines -> v55: {len(text.splitlines())} lines "
      f"(+{len(text.splitlines()) - len(orig.splitlines())})")
print(f"edits applied: {len(PAIRS)}; superseded strings: {len(SUPERSEDED)} "
      f"(the wave is purely additive — nothing replaced)")

DST.write_text(text, encoding="utf-8")
print(f"\nWROTE {DST}")
