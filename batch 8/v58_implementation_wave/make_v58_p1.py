#!/usr/bin/env python3
"""make_v58_p1.py — build paper1_assessment_separation_v58.tex from v57.

Task 113 / batch 8 / paper 1. The owner's two directives (the two open
items recorded by the v57 round's record, section 5):

  (1) "the earlier waves' in-place limits (5.8 wave-1's, 5.9's)" —
      the two limits stated in place by the sigma-extension (the
      wave-1 block of Section 5.8, v57 lines 1748-1762: the
      off-diagonal log-transcendental comparison decided only on
      proven sufficient and necessary rational conditions, headline
      results diagonal; and interior-theta sigma* bracketed between
      tested rungs, the master root transcendental in general) and
      the common-shock extension's limits paragraph (Section 5.9,
      v57 lines 2243-2267), transcribed into the paper's Limitations
      registry as items (xi) and (xii). The first wave-1 limit's
      standing is transcribed honestly: the off-diagonal closure has
      since closed it (the closure block's own opening, v57 lines
      1764-1766: "The first limit recorded above is no longer open").

  (2) "the continuum slice-minimum itself" — the programme's one
      honestly open mathematical residual (the v57 record's open
      items), given its own registry item (xiii): what the slice
      scans certify (the scanned grid points; the machine-bracketed
      slice-flip total (141/50, 353/125] strictly below 2*sqrt(2)),
      what remains open (the slice-minimum of sigma* over the
      continuum — a transcendental inequality in general; the
      interval character of the accepting windows machine-evidenced,
      not proved), and the total-3 regime boundary's standing
      (elementary at the edges, scan-certified in the interior).

One anchored, position-recorded, purely additive insertion at the end
of the Limitations registry's enumerate (after item (x)); SUPERSEDED
is empty. Standing rules honored: new version only (never overwrite);
NO content removed or condensed; fail-loud anchored edit with the
inverse-reconstruction gate proving the diff is exactly the one
insertion; math-span multiset preserved (v57's spans intact, zero
alterations). Idempotence is enforced by the destination-exists gate.
Exit 0 on success.
"""
import sys
from pathlib import Path
from collections import Counter
import re

HERE = Path(__file__).resolve().parent
LATEX = HERE.parents[1] / "arena agent 1" / "paper rewrites" / "latex"
SRC = LATEX / "paper1_assessment_separation_v57.tex"
DST = LATEX / "paper1_assessment_separation_v58.tex"


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
# The one insertion — three items appended inside the Limitations
# registry's enumerate after item (x) (the off-diagonal closure's own
# residuals, added by v57). Every clause is sourced from the in-place
# paragraphs (see IMPLEMENTATION_RECORD.md section 2 for the
# claim-by-claim source check).
# =====================================================================
ITEM_XI = """\\item
  The \\(\\sigma\\)-extension of Section~\\ref{substitutability-spectrum}
  stated two limits in place. Off the diagonal, the geometric
  member's cover comparison is log-transcendental, and the
  verifier decides it only on proven sufficient and necessary
  rational conditions --- the headline results are diagonal, so
  nothing load-bearing rests on the residual undecided cells;
  a limit the off-diagonal closure has since closed, every cell
  now decided by finite rational proof. And interior-\\(\\theta\\)
  values of \\(\\sigma^*(z)\\) are bracketed between tested rungs
  --- the brackets are exact and strictness-refined; the interior
  value is the master root, transcendental in general."""

ITEM_XII = """\\item
  The common-shock extension of Section~\\ref{common-shock-variant}
  states its limits in place: everything is on the witness datum's
  decomposition (tent events, exact tubes,
  the specific STAGED mechanics, the Section 6.3 arithmetic);
  no claim about other data
  beyond the \\(\\delta\\)-family verified. The two regime-(iii)
  readings (additive/replace) bracket the coupled truth ---
  Theorem CT is reading-conditional, and both are
  stated rather than choosing. Grid verification is
  fail-loud but finite, the closed forms carry proofs
  (affine interval arithmetic; the kink device), and the two
  were cross-checked against each other at every grid point
  --- the standard the \\(\\sigma\\)-extension set. \\(\\kappa^*\\)
  under the common class is adjudicated on a reserve grid of
  step \\(1/40\\) plus closed-form confirmation on the survivors,
  and the infinity verdict on \\(\\{\\min(s) < 3/8\\}\\) is
  proved structurally, not sampled; no stochastic,
  partial-observation, or infinite-horizon claim is made, and
  the disturbance quantifier remains innermost throughout
  (Section 2.3)."""

ITEM_XIII = """\\item
  The continuum slice-minimum itself ---
  the programme's one honestly open mathematical residual. In
  the fixed-sum tolerance structure of
  Section~\\ref{substitutability-spectrum},
  the slice scans certify the scanned grid points only: the
  slice-flip total is machine-bracketed \\((141/50,\\, 353/125]\\),
  strictly below \\(2\\sqrt{2}\\); the slice-minimum of \\(\\sigma^*\\)
  over the continuum --- where a slice's best point lies --- is
  a transcendental inequality in general and remains open, so the
  interior window's ecological content (moderate concentration of
  a deficit is more certifiable than balance) is certified at
  the scanned points, not on the continuum; the interval character
  of the accepting windows is machine-evidenced, not proved; the
  total-\\(3\\) regime boundary is elementary at the edges,
  scan-certified in the interior."""

print("== edit 1: the Limitations items (xi) + (xii) + (xiii) ==")
edit(
    "items (xi)/(xii)/(xiii) appended after item (x) in the Limitations enumerate",
    "machine-evidenced, not proved.\n\\end{enumerate}",
    "machine-evidenced, not proved.\n"
    + ITEM_XI + "\n" + ITEM_XII + "\n" + ITEM_XIII
    + "\n\\end{enumerate}",
)

# ============ verification gates ============
print("== verification gates ==")
if text == orig:
    die("no edits applied")
if DST.exists():
    die(f"destination already exists (never overwrite): {DST}")

# gate 0: the frontmatter (title, abstract, highlights) is untouched —
# the edit lies far beyond it
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
print(f"  ok  math-span multiset preserved (v57: {sum(o.values())} spans all "
      f"intact; v58 adds {sum((n - o).values())} new spans; zero alterations)")

# gate 2 (the strongest no-removal check): inverse-reconstruction.
# Reverting the one enumerated edit at its recorded position must
# reproduce v57 byte-identically.
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
      f"reproduces v57 byte-identically (the diff is exactly the three items)")

# gate 3: the new-content markers, with the expected post-edit counts
# (every expectation = the audited v57 count + the item's contribution;
# phrases the v57 source wraps across lines are pinned only where THIS
# wave's own text keeps them contiguous)
for marker, cnt in [
    # -- item (xi): the sigma-extension's two in-place limits --
    ("The \\(\\sigma\\)-extension of Section~\\ref{substitutability-spectrum}", 1),  # new
    ("stated two limits in place", 1),               # new
    ("log-transcendental", 4),                       # 3 + 1
    ("proven sufficient and necessary", 1),          # new (v57 wraps the phrase)
    ("the headline results are diagonal", 2),        # 1 + 1
    ("the residual undecided cells", 2),             # 1 + 1
    ("a limit the off-diagonal closure has since closed", 1),  # new
    ("finite rational proof", 2),                    # 1 + 1
    ("bracketed between tested rungs", 1),           # new (v57 wraps it)
    ("the brackets are exact and strictness-refined", 2),      # 1 + 1
    ("strictness-refined", 2),                       # 1 + 1
    ("master root", 2),                              # 1 + 1
    ("transcendental in general", 2),                # 1 + 1
    ("interior-\\(\\theta\\)", 2),                   # 1 + 1
    ("\\(\\sigma^*(z)\\)", 7),                       # 6 + 1
    # -- item (xii): the common-shock extension's in-place limits --
    ("The common-shock extension of Section~\\ref{common-shock-variant}", 1),  # new
    ("common-shock extension", 2),                   # 1 + 1
    ("states its limits in place", 1),               # new
    ("witness datum's", 2),                          # 1 + 1
    ("tent events", 2),                              # 1 + 1
    ("the specific STAGED mechanics", 2),            # 1 + 1
    ("the Section 6.3 arithmetic", 2),               # 1 + 1
    ("no claim about other data", 2),                # 1 + 1
    ("\\(\\delta\\)-family", 3),                     # 2 + 1
    ("regime-(iii)", 2),                             # 1 + 1
    ("additive/replace", 2),                         # 1 + 1
    ("bracket the coupled truth", 3),                # 2 + 1
    ("Theorem CT", 5),                               # 4 + 1
    ("Theorem CT is reading-conditional", 1),        # new (v57 wraps it)
    ("reading-conditional", 8),                      # 7 + 1
    ("stated rather than choosing", 2),              # 1 + 1
    ("fail-loud but finite", 2),                     # 1 + 1
    ("affine interval arithmetic", 2),               # 1 + 1
    ("the kink device", 3),                          # 2 + 1
    ("were cross-checked against each other at every grid point", 1),  # new (v57 wraps it)
    ("the standard the \\(\\sigma\\)-extension set", 1),                # new (v57 wraps it)
    ("a reserve grid of", 2),                        # 1 + 1
    ("\\(\\kappa^*\\)", 8),                          # 7 + 1
    ("\\(1/40\\)", 2),                               # 1 + 1
    ("closed-form confirmation on the survivors", 1),  # new (v57 wraps it)
    ("\\(\\{\\min(s) < 3/8\\}\\)", 2),               # 1 + 1
    ("proved structurally, not sampled", 2),         # 1 + 1
    ("partial-observation, or infinite-horizon claim", 2),  # 1 + 1
    ("disturbance quantifier", 4),                   # 3 + 1
    ("innermost throughout", 3),                     # 2 + 1
    ("Section 2.3", 3),                              # 2 + 1
    # -- item (xiii): the continuum slice-minimum itself --
    ("The continuum slice-minimum itself", 1),       # new
    ("the programme's one honestly open mathematical residual", 1),  # new
    ("fixed-sum tolerance structure", 3),            # 2 + 1
    ("the slice scans certify the scanned grid points", 2),  # 1 + 1 (item (x) wraps it)
    ("machine-bracketed", 2),                        # 1 + 1
    ("\\((141/50,\\, 353/125]\\)", 2),               # 1 + 1
    ("strictly below \\(2\\sqrt{2}\\)", 2),          # 1 + 1
    ("the slice-minimum of \\(\\sigma^*\\)", 1),     # new
    ("where a slice's best point lies", 1),          # new (v57 wraps the phrase)
    ("a slice's best point", 1),                     # new
    ("transcendental inequality in general", 1),     # new
    ("remains open", 1),                             # new
    ("moderate concentration of", 2),                # 1 + 1
    ("more certifiable than balance", 3),            # 2 + 1
    ("the scanned points, not on the continuum", 1),  # new
    ("machine-evidenced, not proved", 3),            # 2 + 1
    ("accepting windows", 3),                        # 2 + 1
    ("elementary at the edges", 1),                  # new
    ("scan-certified in the interior", 1),           # new
    ("total-\\(3\\) regime boundary", 1),            # new
    ("continuum slice-minimum", 3),                  # 2 + 1
    ("transcendental", 11),                          # 8 + 3 (log-transcendental + xi + xiii)
]:
    c = text.count(marker)
    if c != cnt:
        die(f"marker {marker!r} found {c}x (expected {cnt})")
print("  ok  all new-content markers present with the expected counts")

# gate 4: the structure around the insertion is intact — the registry's
# enumerate count is unchanged (the items went INSIDE the existing list),
# the flow markers x->xi->xii->xiii->end hold, the contributions
# paragraph is untouched, and the three new item lines begin exactly as
# the registry's items do
for marker, cnt in [
    ("\\subsection{Limitations}\\label{limitations}", 1),
    ("\\begin{enumerate}", 4),                      # unchanged
    ("\\end{enumerate}", 4),                        # unchanged
    ("\\item\n  The", 8),                           # 5 + 3 (the new items)
    ("machine-evidenced, not proved.\n\\item", 1),  # item (x) -> (xi) flow
    ("transcendental in general.\n\\item", 1),      # (xi) -> (xii) flow
    ("(Section 2.3).\n\\item", 1),                  # (xii) -> (xiii) flow
    ("scan-certified in the interior.\n\\end{enumerate}", 1),  # (xiii) -> end
    ("\\ref{substitutability-spectrum}", 6),        # 4 + 1 (xi) + 1 (xiii)
    ("\\ref{common-shock-variant}", 3),             # 2 + 1 (xii)
    ("\\textbf{Contributions.}", 1),                # untouched
    ("\\textbf{Scope.}", 1),                        # untouched
    ("(xii)", 1),                                   # contributions, untouched
    ("(xiii)", 1),                                  # contributions, untouched
    ("\\begin{itemize}", 7),                        # unchanged
    ("\\end{itemize}", 7),                          # unchanged
    ("\\subsection{The common-shock variant of the witness (a", 1),
    ("\\label{common-shock-variant}", 1),
]:
    c = text.count(marker)
    if c != cnt:
        die(f"structure marker {marker!r} found {c}x (expected {cnt})")
print("  ok  structure intact (registry enumerate balanced, the (x)->(xi)->(xii)->(xiii) flow, "
      "contributions paragraph and itemize counts untouched)")

# gate 5: nothing else moved — already proven by the inverse gate;
# record the line delta
print(f"\nv57: {len(orig.splitlines())} lines -> v58: {len(text.splitlines())} lines "
      f"(+{len(text.splitlines()) - len(orig.splitlines())})")
print(f"edits applied: {len(PAIRS)}; superseded strings: {len(SUPERSEDED)} "
      f"(the wave is purely additive — nothing replaced)")

DST.write_text(text, encoding="utf-8")
print(f"\nWROTE {DST}")
