#!/usr/bin/env python3
"""make_v56_p1.py — build paper1_assessment_separation_v56.tex from v55.

Task 111 / batch 8 / paper 1. The owner's directive: "the wave's five
transcription items if merited" — the off-diagonal wave's five
owner-gated transcription items (OFF_DIAGONAL_WAVE.md section 8,
recorded by Task 110 as "five owner-gated transcription items for a
future round"), each adjudicated on the merits this round. All five
adjudicated MERITED (the full adjudication, with grounds and overruled
counters, is recorded in batch 8/v56_implementation_wave/
IMPLEMENTATION_RECORD.md section 1):

  (i)   the exact off-diagonal criterion (A*D <= B*C, derived in full)
        and the r-function/rho-curve with its properties (involution,
        the (sqrt 2, sqrt 2) pivot, the limits) — implemented as
        Theorem G with a machine-anchored proof sketch;
  (ii)  the residual wedge witnesses ((5/4,3/2) rejects, (5/4,7/4)
        accepts — the two rational tests' gap is genuine) and the
        ten-cell completion — implemented as "The residual cells
        decided";
  (iii) the completed 2-D sigma*-landscape sentence (the off-diagonal
        bands mirroring the diagonal ladder) — implemented as "The
        completed two-dimensional landscape";
  (iv)  the four-regime fixed-sum tolerance structure as a labelled
        remark, with the 707/250 report/action pair as the anchor and
        the plan-design (FAST/SLOW trough-report) flip — implemented
        as "Remark (the fixed-sum tolerance structure)" + "The anchor
        decision: distribution versus total";
  (v)   the pointer to the wave's verifier as the datum's companion
        extension, a fifth check list under the family's non-pooling
        policy — implemented as "Verification addendum (a fifth check
        list)".

The edit: ONE anchored, position-recorded insertion — the closure
block appended at the end of Section 5.8 (after its "Verification and
honest limits" paragraph, before the Section 5.9 heading). Every
number is transcribed from the committed wave record and its run log
(off_diagonal_run_log.txt, 50/50 checks), with the four closed forms
hand re-derived during transcription (the A*D <= B*C cross-
multiplication from L <= U; the F-form and its diagonal reduction to
the master equation; r(s) <= 1 iff s^2 >= 2; the 707/500 arithmetic,
the trough products, and the 1707/250 kt total).

Standing rules honored: new version only (never overwrite); NO content
removed or condensed — the wave is purely additive (SUPERSEDED is
empty); fail-loud anchored edit with the inverse-reconstruction gate
proving the diff is exactly the one enumerated edit; math-span multiset
preserved (v55's spans intact, zero alterations). Idempotence is
enforced by the destination-exists gate. Exit 0 on success.
"""
import sys
from pathlib import Path
from collections import Counter
import re

HERE = Path(__file__).resolve().parent
LATEX = HERE.parents[1] / "arena agent 1" / "paper rewrites" / "latex"
SRC = LATEX / "paper1_assessment_separation_v55.tex"
DST = LATEX / "paper1_assessment_separation_v56.tex"


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
# The one edit: the off-diagonal closure block at the end of Section 5.8.
# =====================================================================
PREFIX = "interior value is the master root, transcendental in general."
SUBSEC = "\\subsection{The common-shock variant of the witness (a"

BLOCK = r"""\textbf{The off-diagonal closure.} The first limit recorded above
is no longer open. A third dedicated exact computation in the
same programme --- after the spectrum above and the common-shock
computation of Section~\ref{common-shock-variant}; same datum,
same exactness standard, same delimitations --- has decided every
off-diagonal cell that the rational conditions left undecided,
and with it the complete two-dimensional \(\sigma^*\)-landscape.
The log-transcendental comparison acquires no closed form (it has
none); it is \emph{decided}: every verdict below is a finite
rational proof. The device is the \emph{certified rational
enclosure}: every logarithm is bracketed between two rationals
carrying a checkable certificate (the all-positive-term
\(\operatorname{artanh}\) series for \(\ln\), its tail dominated
geometrically), every fractional power by integer \(k\)-th-root
brackets, and every cover comparison below is multilinear in the
enclosed quantities, so that its extrema over the enclosure box
are attained at the vertices --- a finite rational computation.
The fail-loud discipline (any cell the schedule cannot decide
aborts the run) was never triggered: zero cells remain undecided.

\textbf{Theorem G (the exact off-diagonal criterion).} \emph{On
the viable gap quadrant --- \(x < 1\), both coordinates in
\((1, 2)\) --- the geometric member's cover comparison reduces,
by cross-multiplication of the two plans' weight thresholds, to}
\[
\mathrm{cover} \iff A \cdot D \le B \cdot C,
\]
\emph{with \(A = \ln(s_1 - 1)\), \(B = \ln(s_2 + 1)\),
\(C = \ln(s_1 + 1)\), \(D = \ln(s_2 - 1)\); equivalently}
\[
r(s_1)\, r(s_2) \le 1, \qquad r(s) = \frac{\ln\bigl(1/(s-1)\bigr)}{\ln(s+1)},
\]
\emph{so the acceptance region is \(\{ s_2 \ge \rho(s_1) \}\),
where \(\rho = r^{-1} \circ (1/r)\) is a strictly decreasing
involution with the unique fixed point \(\rho(\sqrt{2}) =
\sqrt{2}\) (exactly: \(r(s) \le 1 \iff s^2 \ge 2\)) and limits
\(\rho(s) \to 2^-\) as \(s \to 1^+\), \(\rho(s) \to 1^+\) as
\(s \to 2^-\). The pivot has two sides: \(\min(s_1, s_2) \ge
\sqrt{2}\) is sufficient for the cover, and the cover forces
\(\max(s_1, s_2) \ge \sqrt{2}\); the residual wedge \(\{\min <
\sqrt{2} < \max\}\) is split by the curve \(\rho\), which is
transcendental --- bracketed at rational columns with certified
endpoints in the verifier. A coordinate \(s_i \ge 2\) accepts
outright --- its own plan's worst tube keeps both coordinates at
or above \(1\) (\(s_i - 1 \ge 1\) and \(s_j + 1 > 1\)), serving
every weight at every rung --- so the residual decision problem
lives on the open quadrant. For the interior rungs \(\theta \in
(0, 1)\) the same cross-multiplication, applied to the four
powers \(A = (s_1 - 1)^\theta\), \(B = (s_2 + 1)^\theta\),
\(C = (s_1 + 1)^\theta\), \(D = (s_2 - 1)^\theta\), gives the
multilinear form \(F = C (B - 1) + A (1 - D) - (B - D) \ge 0\),
which reduces on the diagonal to the master equation of
Table~\ref{tab:sigmaladder}.}

\emph{Proof sketch (machine-anchored).} FAST's per-weight
acceptance set is the downward interval \([0, U]\), SLOW's the
upward interval \([L, 1]\), with \(U = B/(B - A)\) and \(L =
-D/(C - D)\) at the geometric member (both denominators positive
on the quadrant); the cover is \(L \le U\), and the
cross-multiplication is the criterion. The function \(r\) is
strictly decreasing (its numerator decreasing, its denominator
increasing), so \(\rho\) is well defined and strictly decreasing,
and the criterion's symmetry makes it its own inverse. The
enclosure lemmas certify the four quantities --- and the four
powers --- between rationals; the comparison forms are
multilinear, so the vertex ranges decide; every rejection
additionally carries an exhibited rational witness weight served
by neither plan, cross-validated in both directions against the
independent per-weight algebra. \ensuremath{\square}

\textbf{The residual cells decided.} The two wedge witnesses
certify that the residual was genuine: \((5/4,\, 3/2)\) and its
mirror \((3/2,\, 5/4)\) \textbf{reject}, with certified margins
\(\approx 0.218\) and exhibited rational witness weights served
by neither plan, while \((5/4,\, 7/4)\) and its mirror
\textbf{accept}, with margins \(\approx 0.422\) --- no
per-coordinate rational condition separates them; the curve
\(\rho\) does. Together with the six \((5/4,\, \ge 2)\)-family
cells, accepted by the \(s_i \ge 2\) boundary argument, all ten
undecided cells of the 64-state grid are decided with certified
strict verdicts.

\textbf{The completed two-dimensional landscape.} With the
geometric member decidable off the diagonal and the interior
rungs \(\theta = 1/2\) and \(2/3\) given the same treatment, all
13 rungs are decided at all 64 grid states, with zero cells
undecided: the accepted rungs form a prefix at every state
(Theorem S1's nesting, now machine-complete off the diagonal),
the acceptance regions are up-closed in each coordinate ---
\(\sigma^*(z)\) is nonincreasing in \(s_1\) and in \(s_2\)
(increasing either coordinate raises both plans' worst-tube
aggregates) --- and the diagonal closed forms of
Table~\ref{tab:sigmaladder} are reproduced, the \(\theta = 1/2\)
rung's \((5/4,\, 5/4)\) equality state included. The nine
finite-\(\sigma^*\) states of the core \(\{5/4,\, 3/2,\, 7/4\}^2\)
form clean off-diagonal bands mirroring the diagonal ladder:
\((5/4,\, 3/2)\) and its mirror in \((1,\, 2)\); \((5/4,\, 7/4)\)
and its mirror in \((1/2,\, 1)\); \((3/2,\, 7/4)\) and its mirror
in \((1/3,\, 1/2)\); \((7/4,\, 7/4)\) in \((1/4,\, 1/3)\); the
diagonal \((5/4,\, 5/4)\) is \(= 2\) exactly and \((3/2,\, 3/2)
\in (1/2,\, 1)\), both already in Table~\ref{tab:sigmastar}.
Off-grid specials: \((6/5,\, 7/5)\) and \((13/10,\, 3/2)\) lie
in \((1,\, 2)\). The remaining thirteen gap states of the grid
are only-linear (\(\sigma^* = \infty\), the \(\min(s) \le 1\)
boundary states).

\textbf{Remark (the fixed-sum tolerance structure).} Slice the
gap quadrant by total margin \(s_1 + s_2\) (the anti-diagonals).
The elementary anchors: a slice's balanced point accepts exactly
when \(s_1 = s_2 \ge \sqrt{2}\) (the diagonal closed form), and
the \(s = 1\) edge accepts exactly from total \(3\) up (the
boundary argument); below total \(3\) the near-edge rejects
(\(r \to \infty\) at the edge, against a fixed positive
partner). On the scanned grids the slices assemble into four
regimes:

\begin{itemize}
\tightlist
\item
  \textbf{R1} (totals \(\le 141/50\), the canonical \(12/5\)
  among them): every scanned point rejects --- no asymmetry saves
  the total;
\item
  \textbf{R2} (an interior window, \(141/50 <\) total \(<
  2\sqrt{2}\); exemplar \(707/250\)): the balanced point rejects,
  moderate asymmetry accepts, the edges reject;
\item
  \textbf{R3} (an anchored window, \(2\sqrt{2} \le\) total
  \(< 3\); exemplar \(71/25\)): the balanced point accepts, strong
  asymmetry rejects;
\item
  \textbf{R4} (totals \(\ge 3\)): the whole scanned slice
  accepts.
\end{itemize}

The regime boundaries \(2\sqrt{2}\) and \(3\) are elementary;
the slice-flip total --- where a slice's first accepting point
appears --- is transcendental and machine-bracketed: every
scanned point of the \(141/50\) slice rejects, while the
\(353/125\) slice already contains acceptors, so the flip lies
in \((141/50,\, 353/125]\), strictly below \(2\sqrt{2}\). The
ecological content of the interior window: \emph{moderate
concentration of a deficit is more certifiable than balance} ---
below \(2\sqrt{2}\), the balanced point is not the slice's best
point.

\textbf{The anchor decision: distribution versus total.} The
benchmark's asymmetric-allocation licensing choice fixes the
total margin at \(s_1 + s_2 = 707/250\) (total biomass
\(1707/250\) kt at the Section 6.3 floor \(B_{\mathrm{lim}} = 2\)
kt per stock) and asks how the verdict depends on the allocation
of the deficit across the stocks. Both allocations are gap
states, and the LPI-structured composite rejects the balanced
allocation \((707/500,\, 707/500)\) by the diagonal closed form
--- \((707/500)^2 = 499849/250000 < 2\) exactly, by the exact
excess \(151/250000\) --- while accepting the concentrated
allocation \((607/500,\, 807/500)\) by the certified
log-comparison (\(r\)-product \(\approx 0.9847\), margin
\(\approx 1.17 \times 10^{-2}\)). The same total margin, opposite
verdicts: the false certification of the compensatory dashboard
is visibly two-dimensional --- blind to the \emph{distribution}
of the deficit, not only to its total; the linear dashboard
licenses both allocations, reporting literally the same number,
\(707/500 \ge 1\), on every trough of both states. The report
layer carries the same structure: at the concentrated state,
which stock bears the pulse flips the equal-weight geometric
report --- the FAST-trough \(\sqrt{139849/250000} < 1\), a
decline signal, against the SLOW-trough \(\sqrt{339849/250000}
> 1\), certified --- a plan-design decision with certification
content. And the action layer: the balanced allocation triggers
the mandatory closure and rebuilding response (the reserve top-up
\(\kappa^* = 1 - x = 1/2\) financing the staged plan,
Section 5.7); the concentrated allocation is licensed with no
mid-transition response. The allocation --- a design-level
choice --- flips a management action.

\textbf{Verification addendum (a fifth check list).} Every
number in this closure is an exact rational, verified in a
dedicated fail-loud exact-arithmetic verifier (50 checks;
standard-library fractions only; no floats, tolerances, or
randomness; deterministic; with a committed byte-reproducible run
log) --- a fifth check list, separate from and not pooled with
the grid verifier's 25, the software companion's 24, the
\(\sigma\)-extension's 57, and the common-shock extension's 77
(the family's non-pooling policy). Honest limits, in the spirit
of the two recorded above: the curve \(\rho\), the slice-flip
total, and every interior \(\sigma^*\) value are transcendental
--- the closure provides certified rational brackets, not closed
forms; the slice scans certify the scanned grid points, the
continuum slice-minimum remaining an honest open residual (the
interval character of the accepting windows is
machine-evidenced, not proved); and the LPI-identification
caveats above carry over unchanged."""

print("== the off-diagonal closure (five transcription items, all merited) ==")
edit(
    "the closure block after Section 5.8's honest-limits paragraph",
    PREFIX + "\n\n" + SUBSEC,
    PREFIX + "\n\n" + BLOCK + "\n\n" + SUBSEC,
)

# ============ verification gates ============
print("== verification gates ==")
if text == orig:
    die("no edits applied")
if DST.exists():
    die(f"destination already exists (never overwrite): {DST}")

# gate 0: the frontmatter (title, abstract, highlights) is untouched —
# the edit lies in Section 5.8, far beyond it (the Task-108
# sigma-abstract DECLINED ruling stands)
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
print(f"  ok  math-span multiset preserved (v55: {sum(o.values())} spans all "
      f"intact; v56 adds {sum((n - o).values())} new spans; zero alterations)")

# gate 2 (the strongest no-removal check): inverse-reconstruction.
# Reverting the one enumerated edit at its recorded position must
# reproduce v55 byte-identically.
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
      f"reproduces v55 byte-identically (the diff is exactly the closure block)")

# gate 3: the new-content markers, with the expected post-edit counts
# (every expectation = the audited v55 count + the block's contribution)
for marker, cnt in [
    ("Theorem G", 1),
    ("involution", 1),
    ("fifth check list", 2),
    ("off-diagonal", 4),
    ("off the diagonal", 2),
    ("undecided", 5),                       # 1 + 4
    ("707/500", 4),
    ("607/500", 1),
    ("807/500", 1),
    ("499849/250000", 1),
    ("151/250000", 1),
    ("139849/250000", 1),
    ("339849/250000", 1),
    ("707/250", 3),                         # incl. the 1707/250 substring
    ("1707/250", 1),
    ("141/50", 4),
    ("353/125", 2),
    ("71/25", 1),
    ("12/5", 3),                            # 2 + 1
    ("\\ref{tab:sigmaladder}", 3),         # 1 + 2
    ("\\ref{tab:sigmastar}", 2),           # 1 + 1
    ("\\ref{common-shock-variant}", 2),    # 1 + 1
    ("Section 5.7", 8),                     # 7 + 1
    ("Section 6.3", 16),                    # 15 + 1
    ("Section 5.9", 8),                     # unchanged
    ("Section 5.8", 1),                     # unchanged
    ("closure and rebuilding", 2),           # 1 + 1
    ("staged plan", 4),                     # 3 + 1
    ("mid-transition", 5),                  # 4 + 1
    ("only-linear", 3),                     # 2 + 1
    ("Theorem S1", 4),                      # 3 + 1
    ("wedge", 2),
    ("artanh", 1),
    ("64-state grid", 1),
    ("64 grid states", 1),
    ("13 rungs", 1),
    ("\\kappa^* = 1 - x = 1/2", 2),        # 1 + 1
    ("log-transcendental", 2),              # 1 + 1
    ("machine-bracketed", 1),
    ("up-closed", 1),
    ("0.9847", 1),
    ("0.218", 1),
    ("0.422", 1),
]:
    c = text.count(marker)
    if c != cnt:
        die(f"marker {marker!r} found {c}x (expected {cnt})")
print("  ok  all new-content markers present with the expected counts")

# gate 4: the structure around the insertion is intact — the Section 5.8
# honest-limits paragraph unchanged, the Section 5.9 heading exactly
# once, its label exactly once, and one new itemize environment
for marker, cnt in [
    (PREFIX, 1),                                        # the 5.8 closing sentence
    ("\\subsection{The common-shock variant of the witness (a", 1),
    ("\\label{common-shock-variant}", 1),
    ("\\begin{itemize}", orig.count("\\begin{itemize}") + 1),
    ("\\end{itemize}", orig.count("\\end{itemize}") + 1),
    ("\\textbf{Contributions.}", 1),
    ("(xii)", 1),
]:
    c = text.count(marker)
    if c != cnt:
        die(f"structure marker {marker!r} found {c}x (expected {cnt})")
print("  ok  structure intact (5.8 closing sentence, 5.9 heading/label, itemize balanced, contributions untouched)")

# gate 5: nothing else moved — the only difference beyond the inserted
# block is nothing at all (already proven by the inverse gate); record
# the line delta
print(f"\nv55: {len(orig.splitlines())} lines -> v56: {len(text.splitlines())} lines "
      f"(+{len(text.splitlines()) - len(orig.splitlines())})")
print(f"edits applied: {len(PAIRS)}; superseded strings: {len(SUPERSEDED)} "
      f"(the wave is purely additive — nothing replaced)")

DST.write_text(text, encoding="utf-8")
print(f"\nWROTE {DST}")
