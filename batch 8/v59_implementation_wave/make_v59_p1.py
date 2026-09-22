#!/usr/bin/env python3
"""make_v59_p1.py — build paper1_assessment_separation_v59.tex from v58.

Task 115 (re-executing the transcription of the lost Task-114 round) /
batch 8 / paper 1. The owner-gated transcription of the fourth exact
wave (batch 8/slice_minimum_wave/ — the continuum slice-minimum
closure; SLICE_MINIMUM_WAVE.md):

  (1) the continuum-slice closure addendum at the end of Section 5.8's
      off-diagonal closure block — the phi-reduction, the tangency
      identity and the four-phase shape, t* with the tangent pair (two
      code paths), the harmonic circle, the m-side flip total exactly
      3, the total-3 interior proof, the interval character, the
      sigma-depth sandwich with the anchor brackets, the corner cusps
      (inf sigma* = 0 beyond 3), the flip-total ladder, and the sixth
      check list under the family's non-pooling policy;

  (2) the Limitations registry item (xiv) recording the closure of
      item (xiii)'s residual (the programme's one honestly open
      mathematical residual, now closed).

Two anchored, position-recorded, purely additive edits; SUPERSEDED is
empty. Standing rules honored: new version only (never overwrite); NO
content removed or condensed; fail-loud anchored edits with the
inverse-reconstruction gate proving the diff is exactly the two
insertions; math-span multiset preserved (v58's spans intact, zero
alterations). Idempotence is enforced by the destination-exists gate.
Exit 0 on success.

Provenance: the original Task-114 round's v59 was committed locally
but never pushed and was lost with its sandbox; this rebuild carries
the same two anchored additive edits, with the certified numbers of
the re-executed verifier (slice_minimum_verify.py, 44/44 checks).
"""
import sys
from pathlib import Path
from collections import Counter
import re

HERE = Path(__file__).resolve().parent
LATEX = HERE.parents[1] / "arena agent 1" / "paper rewrites" / "latex"
SRC = LATEX / "paper1_assessment_separation_v58.tex"
DST = LATEX / "paper1_assessment_separation_v59.tex"


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
# Edit 1 — the continuum-slice closure addendum, appended at the end of
# Section 5.8's off-diagonal closure block (after the fifth-check-list
# paragraph's closing sentence, before the Section 5.9 heading). Every
# claim is sourced from SLICE_MINIMUM_WAVE.md (the wave record) and the
# committed run log (44/44 checks).
# =====================================================================

ADDENDUM = r"""\textbf{The continuum slice closure.} The second limit recorded
above is no longer open either. A fourth dedicated exact computation
in the same programme --- same datum, same exactness standard, same
delimitations --- has decided the continuum. The device is the
\emph{\(\phi\)-reduction}: a point \((s, t-s)\) of the total-\(t\)
slice accepts at the geometric member iff
\(\phi(s) := s + \rho(s) \le t\), so the fixed-sum programme is the
sublevel-set programme of one explicit scalar function on
\((1,2)\), with \(\phi(1^+) = \phi(2^-) = 3\) and
\(\phi(\sqrt{2}) = 2\sqrt{2}\). The tangency identity
\(\rho'(s) = -h(s)/h(\rho(s))\), with \(h = r'/r\), makes the
stationary points of \(\phi\) the zeros of
\(D(s) = h(s) - h(\rho(s))\); there are exactly three --- the
elementary fixed point \(\sqrt{2}\), and a tangent pair
\(a^{*} < \sqrt{2} < b^{*}\) with \(\rho(a^{*}) = b^{*}\) and
\(\rho'(a^{*}) = -1\) --- giving the certified four-phase shape of
\(\phi\): descending from the limit \(3\) to its minimum at
\(a^{*}\), rising through \(2\sqrt{2}\), descending to the equal
minimum at \(b^{*}\), climbing back to \(3\). The consequences, each
a certified rational proof:

\begin{itemize}
\tightlist
\item
  \textbf{The slice-flip total.} \(t^{*} = \min_{s\in(1,2)}\phi =
  a^{*} + b^{*} \in (2.82256976476,\, 2.82256976491)\), certified to
  ten places by two independent code paths (the tangency bisection
  on \(D\); the direct slice bisection) --- five orders inside the
  scan bracket \((141/50,\, 353/125]\) and strictly below
  \(2\sqrt{2}\). The flip is attained at the tangent pair, where the
  curve \(\rho\) touches the anti-diagonal:
  \(a^{*} \in (1.14796785390,\, 1.14796785398)\),
  \(b^{*} \in (1.67460191085,\, 1.67460191093)\).
\item
  \textbf{The interval character.} Every accepting window is a
  sublevel interval of one monotone phase of \(\phi\) --- no internal
  holes: the scan evidence of the fixed-sum remark is upgraded to a
  proof.
\item
  \textbf{The total-\(3\) boundary proved in the interior.}
  \(\phi < 3\) on \((1,2)\) --- every interior point of every
  total-\(3\) slice accepts --- and with it the R4 regime wholesale:
  \(\phi(s) < 3 \le t\) for every point of every total-\(t \ge 3\)
  slice.
\item
  \textbf{The harmonic circle.} The \(\theta = -1\) member's
  off-diagonal acceptance region is exactly the exterior of
  \((2s_1-1)^2 + (2s_2-1)^2 = 10\) --- a polynomial identity; the
  circle passes through \((1,2)\), \((\sqrt{2},\sqrt{2})\), and
  \((2,1)\). So nothing at or below \(\theta = -1\) covers anything
  below total \(3\), and the m-side flip total is exactly \(3\),
  attained at the corners --- which every rung accepts.
\item
  \textbf{The \(\sigma^{*}\)-depth sandwich.} Writing
  \(\sigma_{\min}(t)\) for the slice-minimum of the critical
  elasticity, \(\sigma_{\min}(t) \in (1/2,\, 1]\) on
  \((t^{*},\, 3)\) (the circle's strict interior below, the
  \(\phi\)-minimum above); at the anchor total \(707/250\),
  \(\sigma_{\min} \in [12/13,\, 1]\) --- the interior window's best
  point needs nearly full substitutability and lies near the tangent
  branch, sliding toward the corners as \(t\) climbs to \(3\).
  Beyond total \(3\) the corner cusps
  (\(\delta \sim \varepsilon^{m}/m\)) give \(\inf \sigma^{*} = 0\):
  certified rational witnesses at every tested depth \(m\).
\item
  \textbf{The flip-total ladder.} The linear member exactly \(2\)
  (the dashboard identity: cover iff \(s_1 + s_2 \ge 2\));
  \(\theta = 2/3\) exactly \(2\times\)the cubic master root;
  \(\theta = 1/2\) exactly \(5/2\) (the rung's own equality state
  \((5/4, 5/4)\)); \(\theta = 0\) the transcendental \(t^{*}\) ---
  moderate concentration beats balance from the geometric member
  down; every \(\theta = -m\) and the Leontief member exactly \(3\)
  (the circle; the corners). Strictly increasing in depth,
  nesting-consistent.
\end{itemize}

Every number above is an exact rational, verified in a dedicated
fail-loud exact-arithmetic verifier (44 checks; standard-library
fractions only; deterministic; with a committed byte-reproducible run
log) --- a sixth check list, separate from and not pooled with the
five above (the family's non-pooling policy). Honest limits, in the
same spirit: the tangent quantities (\(a^{*}\), \(b^{*}\), \(t^{*}\),
every interior \(\sigma^{*}\)) are transcendental and carry certified
rational brackets only; the four-phase certificate's end segments
rest on value anchors and the elementary asymptotics of \(h\) at the
ends of \((1,2)\), where \(h\) diverges."""

# =====================================================================
# Edit 2 — the Limitations registry item (xiv): the closure of item
# (xiii)'s residual. Every clause sourced from the addendum and the
# wave record.
# =====================================================================

ITEM_XIV = r"""\item
  The continuum slice-minimum of item (xiii) is closed by the fourth
  dedicated exact computation (the continuum slice closure addendum
  of Section~\ref{substitutability-spectrum}, in place): the
  slice-flip total is certified at \(t^{*} = a^{*} + b^{*}\) --- the
  tangent pair of the boundary involution --- to ten places, by two
  independent code paths; the accepting windows are intervals (each
  a sublevel interval of a monotone phase of \(\phi = s +
  \rho(s)\)); the total-\(3\) regime boundary is proved in the
  interior (\(\phi < 3\)); the harmonic member's region is exactly
  the circle \((2s_1-1)^2 + (2s_2-1)^2 \ge 10\), so nothing at or
  below \(\theta = -1\) covers below total \(3\) and the m-side flip
  total is exactly \(3\); \(\sigma_{\min}(t) \in (1/2,\, 1]\) on
  \((t^{*},\, 3)\), with \(\sigma_{\min}(707/250) \in [12/13,\, 1]\)
  and \(\inf \sigma^{*} = 0\) beyond total \(3\) (corner cusps). The
  transcendental quantities (\(a^{*}\), \(b^{*}\), \(t^{*}\), the
  interior \(\sigma^{*}\) values) carry certified rational brackets
  only."""

print("== edit 1: the continuum slice closure addendum (end of the "
      "Section 5.8 off-diagonal closure block) ==")
edit(
    "the addendum after the fifth-check-list paragraph",
    "caveats above carry over unchanged.\n\n\\subsection{The common-shock "
    "variant of the witness (a",
    "caveats above carry over unchanged.\n\n" + ADDENDUM
    + "\n\n\\subsection{The common-shock variant of the witness (a",
)

print("== edit 2: the Limitations registry item (xiv) ==")
edit(
    "item (xiv) appended after item (xiii) in the Limitations enumerate",
    "  scan-certified in the interior.\n\\end{enumerate}",
    "  scan-certified in the interior.\n" + ITEM_XIV + "\n\\end{enumerate}",
)

# ============ verification gates ============
print("== verification gates ==")
if text == orig:
    die("no edits applied")
if DST.exists():
    die(f"destination already exists (never overwrite): {DST}")

# gate 0: the frontmatter (title, abstract, highlights) is untouched
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
print(f"  ok  math-span multiset preserved (v58: {sum(o.values())} spans all "
      f"intact; v59 adds {sum((n - o).values())} new spans; zero alterations)")

# gate 2 (the strongest no-removal check): inverse-reconstruction.
# Reverting the two enumerated edits at their recorded positions must
# reproduce v58 byte-identically.
t = text
for k in range(len(PAIRS) - 1, -1, -1):
    name, pos, anchor, repl = PAIRS[k]
    if STATES[k] != t:
        die(f"inverse gate: state mismatch before reverting [{name}]")
    if t[pos:pos + len(repl)] != repl:
        die(f"inverse gate: replacement not at recorded position [{name}]")
    t = t[:pos] + anchor + t[pos + len(repl):]
if t != orig:
    i = next((j for j in range(min(len(t), len(orig))) if t[j] != orig[j]),
             min(len(t), len(orig)))
    die(f"inverse-reconstruction mismatch at byte {i}:\n"
        f"  orig: {orig[i:i+120]!r}\n  rev : {t[i:i+120]!r}")
print(f"  ok  inverse-reconstruction: reverting the {len(PAIRS)} enumerated "
      f"edits reproduces v58 byte-identically (the diff is exactly the two "
      f"insertions)")

# gate 3: marker accounting — for every curated marker, the v59 count
# must equal the v58 count plus the inserted texts' own contribution
# (computed from the REPL/anchor strings themselves), and a set of
# absolute structural pins must hold.
def cnt(s, m):
    return s.count(m)

inserted = "".join(repl for (_, _, _, repl) in PAIRS)
removed = "".join(anchor for (_, _, anchor, _) in PAIRS)

marker_pins = [
    "The continuum slice closure",
    "tangent pair",
    "slice-flip",
    "(2s_1-1)^2",
    "\\sigma_{\\min}",
    "non-pooling",
    "sixth check list",
    "44 checks",
    "(xiii)",
    "(xiv)",
    "substitutability-spectrum",
    "moderate concentration",
    "t^{*}",
    "a^{*}",
    "b^{*}",
    "corner cusps",
    "two independent code paths",
    "byte-reproducible",
]
bad = []
for m in marker_pins:
    contrib = cnt(inserted, m) - cnt(removed, m)
    expect = cnt(orig, m) + contrib
    got = cnt(text, m)
    if got != expect:
        bad.append((m, cnt(orig, m), contrib, got))
    else:
        print(f"  ok  marker [{m}]: v58 {cnt(orig, m)} + {contrib} = {got}")
if bad:
    die("marker accounting failed: " + str(bad))

# absolute structural pins
for m, c in [
    ("\\begin{enumerate}", 4),        # the registry items go INSIDE the list
    ("\\end{enumerate}", 4),
    ("\\begin{itemize}", 8),          # 7 + the addendum's one
    ("\\end{itemize}", 8),
    ("\\subsection{The common-shock variant", 1),   # the Section 5.9 heading intact
    ("\\label{common-shock-variant}", 1),
    ("\\begin{document}", 1),
]:
    if cnt(text, m) != c:
        die(f"structure pin [{m}]: expected {c}, got {cnt(text, m)}")
print("  ok  structure pins (enumerate 4/4, itemize 8/8, the 5.9 "
      "heading/label intact)")

# gate 4: the registry flow — item (xiv) sits inside the enumerate,
# after item (xiii), and the addendum sits before the Section 5.9
# heading
if "scan-certified in the interior.\n\\item\n  The continuum slice-minimum " \
   "of item (xiii) is closed" not in text:
    die("registry flow: item (xiv) not directly after item (xiii)")
if "where \\(h\\) diverges.\n\n\\subsection{The common-shock variant" not in text:
    die("addendum flow: the addendum does not end right before the 5.9 heading")
print("  ok  flow gates ((xiii) -> (xiv) -> end; addendum -> 5.9 heading)")

DST.write_text(text, encoding="utf-8")
print(f"\nwrote {DST} ({len(text.splitlines())} lines; v58 had "
      f"{len(orig.splitlines())})")
print("ALL GATES PASS")
