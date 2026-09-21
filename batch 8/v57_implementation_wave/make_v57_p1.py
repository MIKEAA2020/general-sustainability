#!/usr/bin/env python3
"""make_v57_p1.py — build paper1_assessment_separation_v57.tex from v56.

Task 112 / batch 8 / paper 1. The owner's two directives, each adjudicated
on the merits this round (the full adjudication, with grounds and overruled
counters, is recorded in batch 8/v57_implementation_wave/
IMPLEMENTATION_RECORD.md section 1):

  (1) "the optional Section 1.3 contributions item for the closure
       itself" — the option recorded by the v56 round (Task 111's
       counters section: "a Section 1.3 contributions item for this
       closure (NOT added — out of this round's five-item scope;
       recorded as an option for a future owner-gated round, since
       (xi)/(xii) already advertise the programme and item (xii)
       covers 5.9 only)"). Adjudicated MERITED → item (xiii), appended
       after item (xii) in the contributions paragraph, citing
       Section 5.8 by its label and claiming only what the closure
       block (v56 lines 1750-1942) already states.

  (2) "the wave's own honest residuals (transcendental brackets; the
       continuum slice-minimum) transcribed as limits" — the
       off-diagonal wave's honest residuals transcribed into the
       paper's Limitations registry (the Discussion subsection's
       enumerated list, items (i)-(ix) until now), as its new item
       (x). Adjudicated MERITED → the registry entry, mirroring the
       closure block's own honest-limits paragraph verbatim in
       substance: the curve rho, the slice-flip total, and interior
       sigma* values transcendental — certified rational brackets,
       not closed forms; the slice scans certify the scanned grid
       points; the continuum slice-minimum an open residual; the
       interval character of the accepting windows machine-evidenced,
       not proved.

Both edits are purely additive (SUPERSEDED is empty). Standing rules
honored: new version only (never overwrite); NO content removed or
condensed; fail-loud anchored edits with the inverse-reconstruction
gate proving the diff is exactly the two enumerated edits; math-span
multiset preserved (v56's spans intact, zero alterations). Idempotence
is enforced by the destination-exists gate. Exit 0 on success.
"""
import sys
from pathlib import Path
from collections import Counter
import re

HERE = Path(__file__).resolve().parent
LATEX = HERE.parents[1] / "arena agent 1" / "paper rewrites" / "latex"
SRC = LATEX / "paper1_assessment_separation_v56.tex"
DST = LATEX / "paper1_assessment_separation_v57.tex"


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
# Edit 1 — item (xiii) of the contributions paragraph (Section 1.3):
# the off-diagonal closure of the same programme. Appended inline after
# item (xii)'s final sentence, continuing the paragraph. Every clause
# is sourced from the closure block (see IMPLEMENTATION_RECORD.md
# section 2 for the claim-by-claim source check).
# =====================================================================
ITEM_XIII = """(xiii) The off-diagonal closure of the same programme (the
closing block of Section~\\ref{substitutability-spectrum}): the exact
off-diagonal cover criterion (Theorem G) --- the log-transcendental
comparison decided by certified rational enclosures, the acceptance
region bounded by the strictly decreasing involution \\(\\rho\\) with
its exact \\(\\sqrt{2}\\) pivot --- the completed two-dimensional
\\(\\sigma^*\\)-landscape (all 13 rungs decided at all 64 grid states,
zero cells undecided), and the fixed-sum tolerance structure whose
interior window shows moderate concentration of a deficit
more certifiable than balance --- the benchmark's
asymmetric-allocation decision, where the same total margin draws
opposite verdicts and opposite management responses ---
machine-verified as a fifth check list."""

print("== edit 1: the Section 1.3 contributions item (xiii) ==")
edit(
    "item (xiii) appended after item (xii) in the contributions paragraph",
    "as a fourth check list.\n\n\\textbf{Scope.}",
    "as a fourth check list. " + ITEM_XIII + "\n\n\\textbf{Scope.}",
)

# =====================================================================
# Edit 2 — item (x) of the Limitations registry (Discussion): the
# off-diagonal wave's own honest residuals as a stated limit. Appended
# inside the existing enumerate after item (ix) (tractability). Every
# clause mirrors the closure block's honest-limits paragraph.
# =====================================================================
ITEM_X = """\\item
  The off-diagonal closure of Section~\\ref{substitutability-spectrum}
  decides every cell of the 64-state grid by finite rational proof,
  not closed form: the curve \\(\\rho\\), the slice-flip total, and
  interior \\(\\sigma^*\\) values are transcendental and carry
  certified rational brackets only, and the slice scans certify the
  scanned grid points --- the continuum slice-minimum remains an
  open residual, the interval character of the accepting windows
  machine-evidenced, not proved."""

print("== edit 2: the Limitations item (x) (the wave's honest residuals) ==")
edit(
    "item (x) appended after item (ix) in the Limitations enumerate",
    "small, finite, and rational.\n\\end{enumerate}",
    "small, finite, and rational.\n" + ITEM_X + "\n\\end{enumerate}",
)

# ============ verification gates ============
print("== verification gates ==")
if text == orig:
    die("no edits applied")
if DST.exists():
    die(f"destination already exists (never overwrite): {DST}")

# gate 0: the frontmatter (title, abstract, highlights) is untouched —
# both edits lie far beyond it (the Task-108 sigma-abstract DECLINED
# ruling stands)
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
print(f"  ok  math-span multiset preserved (v56: {sum(o.values())} spans all "
      f"intact; v57 adds {sum((n - o).values())} new spans; zero alterations)")

# gate 2 (the strongest no-removal check): inverse-reconstruction.
# Reverting the two enumerated edits at their recorded positions must
# reproduce v56 byte-identically.
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
print(f"  ok  inverse-reconstruction: reverting the {len(PAIRS)} enumerated edits "
      f"reproduces v56 byte-identically (the diff is exactly the two items)")

# gate 3: the new-content markers, with the expected post-edit counts
# (every expectation = the audited v56 count + the item's contribution)
for marker, cnt in [
    ("(xiii)", 1),                                  # new
    ("(xii)", 1),                                   # unchanged
    ("as a fourth check list. (xiii)", 1),          # the appended flow
    ("\\ref{substitutability-spectrum}", 4),        # 2 + 1 (xiii) + 1 (item x)
    ("fifth check list", 3),                        # 2 + 1 (xiii)
    ("machine-verified as a fifth check list", 1),  # new (xiii's close)
    ("machine-verified", 3),                        # 2 + 1
    ("involution", 2),                              # 1 + 1 (xiii)
    ("off-diagonal", 7),                            # 4 + 2 (xiii) + 1 (item x)
    ("Theorem G", 2),                               # 1 + 1 (xiii)
    ("13 rungs", 2),                                # 1 + 1 (xiii)
    ("64 grid states", 2),                          # 1 + 1 (xiii)
    ("64-state grid", 2),                           # 1 + 1 (item x)
    ("zero cells undecided", 1),                    # new in (xiii)
    ("more certifiable than balance", 2),           # 1 + 1 (xiii)
    ("interior window", 3),                         # 2 + 1 (xiii)
    ("asymmetric-allocation", 2),                   # 1 + 1 (xiii)
    ("opposite verdicts", 1),                       # new in (xiii)
    ("management responses", 1),                    # new in (xiii)
    ("the same programme", 1),                      # new in (xiii) (v56 wraps it)
    ("closing block", 1),                           # new in (xiii)
    ("certified rational brackets", 2),             # 1 + 1 (item x)
    ("continuum slice-minimum", 2),                 # 1 + 1 (item x)
    ("machine-evidenced", 2),                       # 1 + 1 (item x)
    ("slice-flip total", 2),                        # 1 + 1 (item x)
    ("the curve \\(\\rho\\)", 3),                   # 2 + 1 (item x)
    ("finite rational proof", 1),                   # new in (item x) (v56 wraps it)
    ("honest open residual", 1),                    # unchanged (5.8's phrasing)
    ("open residual", 2),                           # 1 + 1 (item x)
    ("moderate", 3),                                # 2 + 1 (xiii)
]:
    c = text.count(marker)
    if c != cnt:
        die(f"marker {marker!r} found {c}x (expected {cnt})")
print("  ok  all new-content markers present with the expected counts")

# gate 4: the structure around the two insertions is intact — the
# contributions paragraph's Scope sentence follows, the Limitations
# enumerate count is unchanged (the item went INSIDE the existing list),
# and one new item line begins exactly as the registry's items do
for marker, cnt in [
    ("\\textbf{Contributions.}", 1),
    ("\\textbf{Scope.}", 1),
    ("\\subsection{Limitations}\\label{limitations}", 1),
    ("\\begin{enumerate}", 4),                      # unchanged
    ("\\end{enumerate}", 4),                        # unchanged
    ("\\item\n  The", 5),                           # 4 + 1 (the new item x)
    ("small, finite, and rational.\n\\item", 1),    # item (ix) -> item (x) flow
    ("\\subsection{The common-shock variant of the witness (a", 1),
    ("\\label{common-shock-variant}", 1),
    ("\\begin{itemize}", 7),                        # unchanged
    ("\\end{itemize}", 7),                          # unchanged
]:
    c = text.count(marker)
    if c != cnt:
        die(f"structure marker {marker!r} found {c}x (expected {cnt})")
print("  ok  structure intact (contributions flow, Limitations enumerate balanced, 5.9 heading/label)")

# gate 5: nothing else moved — already proven by the inverse gate;
# record the line delta
print(f"\nv56: {len(orig.splitlines())} lines -> v57: {len(text.splitlines())} lines "
      f"(+{len(text.splitlines()) - len(orig.splitlines())})")
print(f"edits applied: {len(PAIRS)}; superseded strings: {len(SUPERSEDED)} "
      f"(the wave is purely additive — nothing replaced)")

DST.write_text(text, encoding="utf-8")
print(f"\nWROTE {DST}")
