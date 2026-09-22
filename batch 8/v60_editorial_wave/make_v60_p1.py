#!/usr/bin/env python3
"""make_v60_p1.py — build paper1_assessment_separation_v60.tex from v59.

Task 118 (owner editorial directives on paper 1 v59) / batch 8 / paper 1.
The owner-gated editorial wave, four directives:

  (1) AFFILIATION: "Independent Researcher, Tehran, Iran, ..." in the
      \\address block (matching the family's paper3/paper4 convention);

  (2) CHANGE-LOG / DIARY STRIP: the closure blocks and the Limitations
      registry re-stated findings-first — "is no longer open" /
      "A third (fourth) dedicated exact computation ... has decided" /
      "was never triggered" / "has since closed" / "stated ... in place" /
      "in passing" / "addendum ... in place" / "upgraded to a proof"
      converted to static, formal statements; the common-shock intro's
      "left ... honestly-open verdict" to present-tense "undetermined
      verdict"; "no longer rescues" to "fails to rescue"; the
      Limitations items (xiii)+(xiv) MERGED into one findings-first item
      (the stale "remains open / machine-evidenced, not proved / scan-
      certified in the interior" clauses in items (x) and (xiii)
      superseded by the closure's certified facts); the contributions
      entry (xiii) extended with the continuum slice closure (it was
      the one 5.8 result the list omitted) and its stale "the closing
      block of Section 5.8" locator corrected;

  (3) SELF-PRAISE / INFORMAL TERMS: "honest limits"/"stated honestly"/
      "honestly-open"/"honest open residual"/"one honestly open
      mathematical residual"/"the family's defining honesty" → neutral
      register ("Limits", "undetermined", "open residual", "defining
      property"); "punchline" → "statement" (x2); "seen to bite" →
      "seen to bear on"; "Northern-cod-style" → "after the Northern cod
      case"; "DFO-precautionary-approach-style" → "DFO precautionary-
      approach"; "the domestic language of" → "the language of";
      "The datum, domesticated." → "The datum, in resource terms.";
      "the family's non-pooling policy" → "the programme's non-pooling
      policy" (x4, one unambiguous programme referent);

  (4) PROVENANCE: one header comment line recording the wave.

Standing rules honored: new version only (v60; never overwrite v59);
fail-loud anchored edits with the inverse-reconstruction gate proving
the diff is exactly the recorded operations; math-span multiset
accounted (v59's 1,470 spans: 4 superseded spans removed with the
merged limitations item — the scan bracket \\((141/50,\\, 353/125]\\),
\\(2\\sqrt{2}\\), the free-standing \\(\\sigma^*\\), and item (xiii)'s
edge-clause \\(3\\) — and 4 added by the contributions extension
(\\(\\phi\\), \\(t^{*} = a^{*} + b^{*}\\), \\(3\\), \\(\\sigma^{*}\\));
zero alterations of any other span); marker accounting; idempotence by
the destination-exists gate. Exit 0 on success.

Legitimate scope statements (the "No empirical ..." delimitations, the
metaphor pair photograph/tube, the LPI-identification caveats) are
deliberately NOT touched — the owner's directive removes naive
over-hedging and diary phrasing, not scope discipline.
"""
import sys
from pathlib import Path
from collections import Counter
import re

HERE = Path(__file__).resolve().parent
LATEX = HERE.parents[1] / "arena agent 1" / "paper rewrites" / "latex"
SRC = LATEX / "paper1_assessment_separation_v59.tex"
DST = LATEX / "paper1_assessment_separation_v60.tex"


def die(msg: str):
    print(f"FAIL: {msg}")
    sys.exit(1)


if DST.exists():
    die(f"destination exists (idempotence gate): {DST.name}")

text = SRC.read_text(encoding="utf-8")
orig = text
PAIRS = []   # (name, anchor, repl, count) for every operation


def edit(name: str, anchor: str, repl: str, count: int = 1):
    global text
    n = text.count(anchor)
    if n != count:
        die(f"anchor [{name}] found {n}x (expected {count}):\n---\n{anchor[:240]}\n---")
    text = text.replace(anchor, repl)
    PAIRS.append((name, anchor, repl, count))
    print(f"  ok  {name}")


# =====================================================================
# (1) Affiliation: Tehran, Iran
# =====================================================================
edit(
    "affiliation-tehran",
    "\\address[aff]{Independent Researcher, \\href{https://orcid.org/0000-0002-0019-1842}{ORCID: 0000-0002-0019-1842},",
    "\\address[aff]{Independent Researcher, Tehran, Iran, \\href{https://orcid.org/0000-0002-0019-1842}{ORCID: 0000-0002-0019-1842},",
)

# =====================================================================
# (3a) punchline -> statement (contributions item (xi); Theorem S2 title)
# =====================================================================
edit(
    "contributions-s2-statement",
    "\\(\\sqrt{3}\\)), and two machine-anchored theorems (S1 nesting; S2 the\ntwo-sided Leontief punchline). (xii) A labelled common-shock",
    "\\(\\sqrt{3}\\)), and two machine-anchored theorems (S1 nesting; S2 the\ntwo-sided Leontief statement). (xii) A labelled common-shock",
)
edit(
    "theorem-s2-statement",
    "\\textbf{Theorem S2 (the two-sided Leontief punchline).} \\emph{(i)",
    "\\textbf{Theorem S2 (the two-sided Leontief statement).} \\emph{(i)",
)

# =====================================================================
# (2a) contributions item (xiii): stale locator corrected + the continuum
#      slice closure entry (the one 5.8 result the list omitted)
# =====================================================================
edit(
    "contributions-xiii-continuum",
    """as a fourth check list. (xiii) The off-diagonal closure of the same programme (the
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
machine-verified as a fifth check list.""",
    """as a fourth check list. (xiii) The off-diagonal closure of the same programme
(Section~\\ref{substitutability-spectrum}): the exact
off-diagonal cover criterion (Theorem G) --- the log-transcendental
comparison decided by certified rational enclosures, the acceptance
region bounded by the strictly decreasing involution \\(\\rho\\) with
its exact \\(\\sqrt{2}\\) pivot --- the completed two-dimensional
\\(\\sigma^*\\)-landscape (all 13 rungs decided at all 64 grid states,
zero cells undecided), and the fixed-sum tolerance structure whose
interior window shows moderate concentration of a deficit
more certifiable than balance --- the benchmark's
asymmetric-allocation decision, where the same total margin draws
opposite verdicts and opposite management responses --- together
with the continuum slice closure (the \\(\\phi\\)-reduction deciding
the slice-minimum: the flip total \\(t^{*} = a^{*} + b^{*}\\)
certified to ten places by two independent code paths, the
accepting windows proved to be intervals, the total-\\(3\\) boundary
proved in the interior, the harmonic circle, the
\\(\\sigma^{*}\\)-depth sandwich, and the flip-total ladder) ---
machine-verified as fifth and sixth check lists.""",
)

# =====================================================================
# (3b) Lemma B: "the family's defining honesty" -> "defining property"
# =====================================================================
edit(
    "lemma-b-property",
    """\\(\\theta \\le 0\\) is undefined there; for \\(\\theta \\in (0,1)\\) the
convention is the family's defining honesty. The \\(\\theta = 1\\) member""",
    """\\(\\theta \\le 0\\) is undefined there; for \\(\\theta \\in (0,1)\\) the
convention is the family's defining property. The \\(\\theta = 1\\) member""",
)

# =====================================================================
# (3c) DFO rule phrasing
# =====================================================================
edit(
    "dfo-rule",
    """decision: the benchmark's closure decision at the canonical datum, under
a DFO-precautionary-approach-style limit rule. (2) The report flip: at""",
    """decision: the benchmark's closure decision at the canonical datum, under
a DFO precautionary-approach limit rule. (2) The report flip: at""",
)

# =====================================================================
# (2b) verification headers: "honest limits" -> "limits" (x2, same form)
# =====================================================================
edit(
    "verification-headers",
    "\\textbf{Verification and honest limits.} Every number in this subsection",
    "\\textbf{Verification and limits.} Every number in this subsection",
    count=2,
)

# =====================================================================
# (2c) the off-diagonal closure opener, findings-first
# =====================================================================
edit(
    "offdiagonal-opener",
    """\\textbf{The off-diagonal closure.} The first limit recorded above
is no longer open. A third dedicated exact computation in the
same programme --- after the spectrum above and the common-shock
computation of Section~\\ref{common-shock-variant}; same datum,
same exactness standard, same delimitations --- has decided every
off-diagonal cell that the rational conditions left undecided,
and with it the complete two-dimensional \\(\\sigma^*\\)-landscape.""",
    """\\textbf{The off-diagonal closure.} Every off-diagonal cell that
the rational conditions leave undecided --- and with it the
complete two-dimensional \\(\\sigma^*\\)-landscape --- is decided by
a dedicated exact computation in the same programme (same datum,
same exactness standard, same delimitations).""",
)

edit(
    "closed-form-verb",
    """The log-transcendental comparison acquires no closed form (it has
none); it is \\emph{decided}: every verdict below is a finite""",
    """The log-transcendental comparison admits no closed form (it has
none); it is \\emph{decided}: every verdict below is a finite""",
)

edit(
    "fail-loud-static",
    """The fail-loud discipline (any cell the schedule cannot decide
aborts the run) was never triggered: zero cells remain undecided.""",
    """Under the fail-loud discipline (any cell the schedule cannot decide
aborts the run), zero cells remain undecided.""",
)

# =====================================================================
# (2d) "Verification addendum" header -> "Verification"
# =====================================================================
edit(
    "fifth-checklist-header",
    "\\textbf{Verification addendum (a fifth check list).} Every",
    "\\textbf{Verification (a fifth check list).} Every",
)

# =====================================================================
# (3d) non-pooling policy: one programme referent (x4)
# =====================================================================
edit(
    "nonpooling-programme",
    "(the family's non-pooling policy)",
    "(the programme's non-pooling policy)",
    count=3,
)
edit(
    "nonpooling-programme-wrapped",
    "(the family's non-pooling\npolicy)",
    "(the programme's non-pooling\npolicy)",
)

# =====================================================================
# (2e) off-diagonal limits lead-in + open residual
# =====================================================================
edit(
    "offdiagonal-limits",
    """Honest limits, in the spirit
of the two recorded above: the curve \\(\\rho\\), the slice-flip""",
    """Limits: the curve \\(\\rho\\), the slice-flip""",
)
edit(
    "offdiagonal-open-residual",
    "continuum slice-minimum remaining an honest open residual (the",
    "continuum slice-minimum remaining open (the",
)

# =====================================================================
# (2f) the continuum slice closure opener, findings-first
# =====================================================================
edit(
    "continuum-opener",
    """\\textbf{The continuum slice closure.} The second limit recorded
above is no longer open either. A fourth dedicated exact computation
in the same programme --- same datum, same exactness standard, same
delimitations --- has decided the continuum. The device is the""",
    """\\textbf{The continuum slice closure.} The continuum slice-minimum
--- the open residual recorded above --- is decided: a dedicated
exact computation in the same programme (same datum, same
exactness standard, same delimitations) settles the continuum.
The device is the""",
)

# =====================================================================
# (2g) interval character: "upgraded to a proof" -> "thereby proved"
# =====================================================================
edit(
    "interval-character",
    """  \\textbf{The interval character.} Every accepting window is a
  sublevel interval of one monotone phase of \\(\\phi\\) --- no internal
  holes: the scan evidence of the fixed-sum remark is upgraded to a
  proof.""",
    """  \\textbf{The interval character.} Every accepting window is a
  sublevel interval of one monotone phase of \\(\\phi\\) --- no internal
  holes: the fixed-sum remark's scan-level finding is thereby
  proved.""",
)

# =====================================================================
# (2h) continuum verification limits lead-in
# =====================================================================
edit(
    "continuum-limits",
    """Honest limits, in the
same spirit: the tangent quantities""",
    """Limits: the tangent quantities""",
)

# =====================================================================
# (2i) common-shock intro: present tense, undetermined, no "in passing"
# =====================================================================
edit(
    "commonshock-intro",
    """Section 5.4's disturbance scoping (Table~\\ref{tab:disturbance}) left the
middle cell --- the common biomass shock, one shared disturbance striking
the same floor coordinate of every plan --- as the one honestly-open
verdict: its assertion demanded its own exact computation, a common-shock
variant of the witness. This subsection --- a labelled extension in the
sense of Section 5.8, not a part of the separation theorem --- records
that computation, and in passing sharpens the coupled regime's row-(iii)
assertion into two exact, reading-conditional theorems.""",
    """Section 5.4's disturbance scoping (Table~\\ref{tab:disturbance}) leaves the
middle cell --- the common biomass shock, one shared disturbance striking
the same floor coordinate of every plan --- as the one undetermined
verdict: its assertion demands its own exact computation, a common-shock
variant of the witness. This subsection --- a labelled extension in the
sense of Section 5.8, not a part of the separation theorem --- records
that computation and sharpens the coupled regime's row-(iii)
assertion into two exact, reading-conditional theorems.""",
)

# =====================================================================
# (2j) Theorem M2: "no longer rescues" -> "fails to rescue"
# =====================================================================
edit(
    "m2-qualitative-change",
    "\\emph{The qualitative change: the resource route no longer rescues every",
    "\\emph{The qualitative change: the resource route fails to rescue every",
)

# =====================================================================
# (3e) Northern-cod-style -> after the Northern cod case
# =====================================================================
edit(
    "northern-cod",
    """decision: whether a composite biomass index may certify a
stock-rebuilding transition (Northern-cod-style, the Section 6.3
benchmark) when the assessment's disturbance class is a shared""",
    """decision: whether a composite biomass index may certify a
stock-rebuilding transition (after the Northern cod case, the Section 6.3
benchmark) when the assessment's disturbance class is a shared""",
)

# =====================================================================
# (3f) common-shock verification: "Limits, stated honestly" -> "Limits"
# =====================================================================
edit(
    "commonshock-limits",
    "Limits, stated honestly: everything is on the witness datum's",
    "Limits: everything is on the witness datum's",
)

# =====================================================================
# (2k) Limitations item (x): drop the stale open-residual clause
# =====================================================================
edit(
    "limitations-offdiagonal",
    """  The off-diagonal closure of Section~\\ref{substitutability-spectrum}
  decides every cell of the 64-state grid by finite rational proof,
  not closed form: the curve \\(\\rho\\), the slice-flip total, and
  interior \\(\\sigma^*\\) values are transcendental and carry
  certified rational brackets only, and the slice scans certify the
  scanned grid points --- the continuum slice-minimum remains an
  open residual, the interval character of the accepting windows
  machine-evidenced, not proved.""",
    """  The off-diagonal closure of Section~\\ref{substitutability-spectrum}
  decides every cell of the 64-state grid by finite rational proof,
  not closed form: the curve \\(\\rho\\), the slice-flip total, and
  interior \\(\\sigma^*\\) values are transcendental and carry
  certified rational brackets only.""",
)

# =====================================================================
# (2l) Limitations item (xi): "has since closed" -> findings-first
# =====================================================================
edit(
    "limitations-sigma-extension",
    """  The \\(\\sigma\\)-extension of Section~\\ref{substitutability-spectrum}
  stated two limits in place. Off the diagonal, the geometric
  member's cover comparison is log-transcendental, and the
  verifier decides it only on proven sufficient and necessary
  rational conditions --- the headline results are diagonal, so
  nothing load-bearing rests on the residual undecided cells;
  a limit the off-diagonal closure has since closed, every cell
  now decided by finite rational proof. And interior-\\(\\theta\\)""",
    """  The \\(\\sigma\\)-extension of Section~\\ref{substitutability-spectrum}
  states two limits. Off the diagonal, the geometric
  member's cover comparison is log-transcendental, and the
  verifier decides it only on proven sufficient and necessary
  rational conditions --- the headline results are diagonal, so
  nothing load-bearing rests on the residual undecided cells;
  the off-diagonal closure decides every such cell by finite
  rational proof. And interior-\\(\\theta\\)""",
)

# =====================================================================
# (2m) Limitations common-shock item: "limits in place" -> "limits"
# =====================================================================
edit(
    "limitations-commonshock",
    "  states its limits in place: everything is on the witness datum's",
    "  states its limits: everything is on the witness datum's",
)

# =====================================================================
# (2n) Limitations items (xiii)+(xiv) MERGED into one findings-first item
# =====================================================================
edit(
    "limitations-merge",
    """  The continuum slice-minimum itself ---
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
  scan-certified in the interior.
\\item
  The continuum slice-minimum of item (xiii) is closed by the fourth
  dedicated exact computation (the continuum slice closure addendum
  of Section~\\ref{substitutability-spectrum}, in place): the
  slice-flip total is certified at""",
    """  The continuum slice-minimum of the fixed-sum tolerance structure
  --- where a slice's best point lies --- is closed (the continuum
  slice closure of Section~\\ref{substitutability-spectrum}): the
  slice-flip total is certified at""",
)
edit(
    "limitations-merge-intervals",
    """  a sublevel interval of a monotone phase of \\(\\phi = s +
  \\rho(s)\\)); the total-\\(3\\) regime boundary is proved in the""",
    """  a sublevel interval of a monotone phase of \\(\\phi = s +
  \\rho(s)\\)), so the interior window's ecological content (moderate
  concentration of a deficit is more certifiable than balance) is
  certified on the continuum, not only at the scanned points; the
  total-\\(3\\) regime boundary is proved in the""",
)

# =====================================================================
# (3g) benchmark: "bite" -> "bear on"; "domestic language" -> "language"
# =====================================================================
edit(
    "benchmark-bear-domestic",
    """that the theorems can be seen to bite on a textbook dynamical system rather
than on a discrete datum alone. The instantiation is an exact rational re-reading of the witness
datum in the domestic language of a Schaefer (1954) production model:""",
    """that the theorems can be seen to bear on a textbook dynamical system rather
than on a discrete datum alone. The instantiation is an exact rational re-reading of the witness
datum in the language of a Schaefer (1954) production model:""",
)
edit(
    "benchmark-header",
    "\\textbf{The datum, domesticated.} At the datum's initial state",
    "\\textbf{The datum, in resource terms.} At the datum's initial state",
)

# =====================================================================
# (4) provenance header comment
# =====================================================================
edit(
    "provenance-comment",
    "% Amin Abaee. Companion software: SafeTransition (verification deposit: https://doi.org/10.6084/m9.figshare.33764023). Compiles with tectonic, pdflatex, or xelatex.",
    "% Amin Abaee. Companion software: SafeTransition (verification deposit: https://doi.org/10.6084/m9.figshare.33764023). Compiles with tectonic, pdflatex, or xelatex.\n% v60 (editorial wave, 2025-09-22): Tehran, Iran affiliation; closure blocks and the Limitations registry restated findings-first; informal terms replaced; mathematics unchanged except the recorded span accounting (batch 8/v60_editorial_wave/).",
)

# =====================================================================
# GATE 1 — inverse reconstruction: revert every operation in reverse
# order and require byte-identity with v59.
# =====================================================================
recon = text
for name, anchor, repl, count in reversed(PAIRS):
    if recon.count(repl) < count:
        die(f"inverse gate: replacement of [{name}] found {recon.count(repl)}x, expected {count}")
    recon = recon.replace(repl, anchor, count)
if recon != orig:
    # locate the first divergence for the error report
    k = next((i for i, (a, b) in enumerate(zip(recon, orig)) if a != b), min(len(recon), len(orig)))
    die(f"inverse reconstruction gate: reverted text != v59 (first divergence at offset {k}:\nRECON: ...{recon[max(0,k-80):k+80]!r}\nV59:    ...{orig[max(0,k-80):k+80]!r})")

# =====================================================================
# GATE 2 — math-span multiset accounting.
# v59 spans minus the 3 superseded spans of the merged limitations
# item, plus the 4 spans of the contributions extension; zero
# alterations elsewhere.
# =====================================================================
SPAN = re.compile(r"\\\((?:[^\\]|\\.)*?\\\)|\\\[.*?\\\]", re.S)

def spans(s):
    return Counter(SPAN.findall(s))

s59, s60 = spans(orig), spans(text)
removed = ["\\((141/50,\\, 353/125]\\)", "\\(2\\sqrt{2}\\)", "\\(\\sigma^*\\)", "\\(3\\)"]
added = ["\\(\\phi\\)", "\\(t^{*} = a^{*} + b^{*}\\)", "\\(3\\)", "\\(\\sigma^{*}\\)"]
expected = s59.copy()
for x in removed:
    if expected[x] <= 0:
        die(f"math-span accounting: span not present in v59 as expected: {x}")
    expected[x] -= 1
for x in added:
    expected[x] += 1
if s60 != expected:
    only59 = s59 - s60
    only60 = s60 - s59
    die(f"math-span multiset mismatch.\nspans lost vs expectation: {dict(only59)}\nspans gained: {dict(only60)}")
print(f"  ok  math-span multiset: {sum(s59.values())} -> {sum(s60.values())} (removed {len(removed)}, added {len(added)}, zero alterations)")

# =====================================================================
# GATE 3 — marker accounting: every new marker present, every retired
# marker absent.
# =====================================================================
NEW_MARKERS = [
    "Independent Researcher, Tehran, Iran,",
    "two-sided Leontief statement). (xii)",
    "Theorem S2 (the two-sided Leontief statement)",
    "together\nwith the continuum slice closure",
    "machine-verified as fifth and sixth check lists",
    "the family's defining property",
    "a DFO precautionary-approach limit rule",
    "Verification and limits.} Every number in this subsection",
    "is decided by\na dedicated exact computation in the same programme (same datum,\nsame exactness standard, same delimitations).",
    "admits no closed form",
    "Under the fail-loud discipline",
    "Verification (a fifth check list)",
    "(the programme's non-pooling policy)",
    "Limits: the curve",
    "remaining open (the",
    "the open residual recorded above --- is decided",
    "settles the continuum",
    "scan-level finding is thereby",
    "Limits: the tangent quantities",
    "leaves the\nmiddle cell",
    "the one undetermined\nverdict",
    "that computation and sharpens",
    "fails to rescue every",
    "after the Northern cod case",
    "Limits: everything is on the witness datum's",
    "states two limits. Off the diagonal",
    "decides every such cell by finite",
    "states its limits: everything",
    "of the fixed-sum tolerance structure\n  --- where a slice's best point lies --- is closed (the continuum",
    "certified on the continuum, not only at the scanned points",
    "seen to bear on a textbook",
    "in the language of a Schaefer (1954) production model",
    "The datum, in resource terms.",
    "% v60 (editorial wave, 2025-09-22)",
]
OLD_MARKERS = [
    "Independent Researcher, \\href",
    "punchline",
    "the\nclosing block of Section",
    "machine-verified as a fifth check list.",
    "family's defining honesty",
    "DFO-precautionary-approach-style",
    "Verification and honest limits",
    "is no longer open",
    "A third dedicated exact computation",
    "A fourth dedicated exact computation",
    "acquires no closed form",
    "was never triggered",
    "Verification addendum",
    "the family's non-pooling policy",
    "Honest limits",
    "an honest open residual",
    "honestly-open",
    "honestly open mathematical residual",
    "in passing",
    "no longer rescues",
    "Northern-cod-style",
    "Limits, stated honestly",
    "stated two limits in place",
    "has since closed",
    "limits in place",
    "The continuum slice-minimum itself",
    "of item (xiii) is closed by the fourth",
    "the continuum slice closure addendum",
    ", in place):",
    "remains open",
    "remains an\n  open residual",
    "machine-evidenced, not proved; the\n  total-",
    "scan-certified in the interior",
    "upgraded to a\n  proof",
    "seen to bite",
    "domestic language",
    "domesticated",
]
for m in NEW_MARKERS:
    if m not in text:
        die(f"marker accounting: new marker missing: {m[:90]!r}")
for m in OLD_MARKERS:
    if m in text:
        die(f"marker accounting: retired marker still present: {m[:90]!r}")
print(f"  ok  marker accounting: {len(NEW_MARKERS)} new present, {len(OLD_MARKERS)} retired absent")

# =====================================================================
# GATE 4 — structure pins: environments and section flow unchanged.
# =====================================================================
for env in ("enumerate", "itemize", "figure", "table", "longtable"):
    b, e = text.count(f"\\begin{{{env}}}"), text.count(f"\\end{{{env}}}")
    ob, oe = orig.count(f"\\begin{{{env}}}"), orig.count(f"\\end{{{env}}}")
    if b != e:
        die(f"structure pin: unbalanced {env} ({b} begin / {e} end)")
    if (b, e) != (ob, oe):
        die(f"structure pin: {env} count changed {ob}->{b}")
n_items_delta = text.count("\\item") - orig.count("\\item")
if n_items_delta != -1:
    die(f"structure pin: expected exactly one \\item removed (the limitations merge), got {n_items_delta}")
for heading in ("\\subsection{The common-shock variant", "\\subsection{Limitations}",
                "\\section{Conclusions}", "\\section{Proofs of the general results}"):
    if text.count(heading) != orig.count(heading):
        die(f"structure pin: heading count changed: {heading}")
print("  ok  structure pins: environments balanced and unchanged; exactly one \\item removed (limitations merge)")

# =====================================================================
# GATE 5 — register sweep: no diary/apology/informal residue.
# =====================================================================
BANNED = ["honest", "punchline", "no longer open", "was never triggered",
          "has since closed", "in passing", "addendum", "domesticat",
          "in place:", "stated in place", "upgraded to a"]
for w in BANNED:
    if w.lower() in text.lower():
        i = text.lower().index(w.lower())
        die(f"register sweep: banned residue {w!r} at offset {i}: ...{text[max(0,i-80):i+80]}...")
print(f"  ok  register sweep: {len(BANNED)} banned residues absent")

# =====================================================================
# Write and report.
# =====================================================================
DST.write_text(text, encoding="utf-8")
nlines = text.count("\n") + 1
print(f"\nWROTE {DST.name}: {nlines} lines (v59: {orig.count(chr(10)) + 1})")
print("ALL GATES GREEN")
