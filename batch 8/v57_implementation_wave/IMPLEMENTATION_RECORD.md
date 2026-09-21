# Task 112 / batch 8 / paper 1 — v57 implementation record

**Owner directives (two, English-only rule standing):** (1) "the optional
§1.3 contributions item for the closure itself"; (2) "the wave's own honest
residuals (transcendental brackets; the continuum slice-minimum) transcribed
as limits." Plus the standing push rule (PAT re-supplied).

**Deliverable:** `latex/paper1_assessment_separation_v57.tex` + `.pdf`
(v56 3,010 → v57 3,031 lines; 49 → 50 pp) — TWO anchored, position-recorded,
purely additive edits; built by `make_v57_p1.py` with the full gate battery.

---

## 1. The adjudication (each item on the merits)

### Item 1 — the §1.3 contributions item for the closure itself: **MERITED**

Grounds:
1. **The recorded option.** The v56 round's own counters section recorded
   exactly this as an option deferred to a future owner-gated round: "a §1.3
   contributions item for this closure (NOT added — out of this round's
   five-item scope; recorded as an option for a future owner-gated round,
   since (xi)/(xii) already advertise the programme and item (xii) covers
   §5.9 only)." The owner now exercises that option.
2. **Main-text load parity.** The closure block is 193 lines of main text
   inside Section 5.8 (v56 lines 1750–1942) — comparable to Section 5.9's
   load, which item (xii) advertises. Item (xi) was written in v53 (before
   the closure existed) and describes only the wave-1 content: the CES
   family, the critical-floor ladder, S1/S2. A reader of §1.3 alone learns
   of the programme's opening but not its closure.
3. **Contribution substance.** The closure's headline — every cell of the
   2-D σ\*-landscape decided, the two-dimensional false certification —
   completes what (xi) opens; it is arguably the programme's strongest
   single result.
4. **The owner's delegated call** (the standing "if merited" pattern;
   Task-110 precedent: the owner's direction is itself a ground).

Counters weighed and overruled:
- *The contributions paragraph is already long (items i–xii).* — The
  additive-only discipline means length alone cannot veto a merited item;
  (xiii) is one sentence at the list's established density.
- *(xi) already cites the same section.* — (xi) covers wave-1 content only;
  none of the closure's objects (Theorem G, the ρ-involution, the completed
  landscape, the fixed-sum structure, the allocation flip) appears in it.
- *The Task-108 abstract-visibility DECLINED ruling.* — That ruling
  concerned the abstract's closed-results convention and word caps; the
  contributions list already advertises programme-opening extensions via
  (xi)/(xii), so no convention is violated.

**Implementation:** item (xiii) appended after item (xii)'s final sentence
("…machine-verified as a fourth check list."), continuing the contributions
paragraph; cites Section 5.8 by its label; closes "machine-verified as a
fifth check list," mirroring (xii)'s close.

### Item 2 — the wave's own honest residuals as limits: **MERITED**

Grounds:
1. **The paper-level registry locus.** The Discussion's `Limitations`
   subsection (items (i)–(ix) until now) is the paper's canonical registry
   of limits. The three waves' labelled extensions state their honest
   limits in place (5.8's paragraph, the closure's verification addendum,
   5.9's addendum), but the registry carries none of them. The owner
   directs the closure's residuals there.
2. **The residuals are real and precisely statable** — both named by the
   owner are in the closure block's own honest-limits paragraph (v56 lines
   1934–1942): the transcendental brackets (the curve ρ, the slice-flip
   total, interior σ\* values — certified rational brackets, not closed
   forms) and the continuum slice-minimum (the slice scans certify scanned
   grid points; the interval character of the accepting windows
   machine-evidenced, not proved).
3. **Faithfulness.** The registry entry mirrors the closure's paragraph
   clause-by-clause — no new claim, no softening, no strengthening.

Counter weighed and overruled: *duplication with the in-place limits* — the
registry items already function as pointers (items (iv)/(v)/(vi) likewise
reference sections); the never-remove rule keeps both statements.

**Implementation:** the new item (x) inside the existing enumerate, after
item (ix) (tractability).

---

## 2. The two edits and their claim-by-claim sources

**Edit 1 — item (xiii)** (anchor: the contributions paragraph's close
"as a fourth check list." + the Scope heading; position-recorded):

> (xiii) The off-diagonal closure of the same programme (the closing block
> of Section 5.8): the exact off-diagonal cover criterion (Theorem G) — the
> log-transcendental comparison decided by certified rational enclosures,
> the acceptance region bounded by the strictly decreasing involution ρ
> with its exact √2 pivot — the completed two-dimensional σ\*-landscape
> (all 13 rungs decided at all 64 grid states, zero cells undecided), and
> the fixed-sum tolerance structure whose interior window shows moderate
> concentration of a deficit more certifiable than balance — the benchmark's
> asymmetric-allocation decision, where the same total margin draws
> opposite verdicts and opposite management responses — machine-verified
> as a fifth check list.

Every clause sourced from the closure block: "The off-diagonal closure" +
"in the same programme" (block opening); the criterion and enclosure device
(Theorem G + the enclosure paragraph); the involution with the √2 pivot
(Theorem G, incl. "the pivot has two sides"); "all 13 rungs are decided at
all 64 grid states, with zero cells undecided" (the landscape paragraph);
"the fixed-sum tolerance structure" + "moderate concentration of a deficit
is more certifiable than balance" (the Remark); "the benchmark's
asymmetric-allocation licensing choice" + "The same total margin, opposite
verdicts" + the action flip (the anchor-decision paragraph); the fifth
check list (the verification addendum).

**Edit 2 — Limitations item (x)** (anchor: item (ix)'s close + the
enumerate's end; position-recorded):

> (x) The off-diagonal closure of Section 5.8 decides every cell of the
> 64-state grid by finite rational proof, not closed form: the curve ρ,
> the slice-flip total, and interior σ\* values are transcendental and
> carry certified rational brackets only, and the slice scans certify the
> scanned grid points — the continuum slice-minimum remains an open
> residual, the interval character of the accepting windows
> machine-evidenced, not proved.

Every clause mirrors the closure block's honest-limits paragraph
verbatim in substance: "every verdict below is a finite rational proof" /
"acquires no closed form"; "the curve ρ, the slice-flip total, and every
interior σ\* value are transcendental — the closure provides certified
rational brackets, not closed forms"; "the slice scans certify the scanned
grid points, the continuum slice-minimum remaining an honest open
residual"; "the interval character of the accepting windows is
machine-evidenced, not proved."

---

## 3. The gates (make_v57_p1.py, fail-loud, exit 0)

- **Frontmatter untouched** (both edits far beyond `\end{frontmatter}`;
  the Task-108 sigma-abstract DECLINED ruling stands).
- **Math-span multiset:** v56's 1,362 spans ALL intact; v57 adds 5 new
  (ρ, √2, σ\* in (xiii); ρ, σ\* in item (x)); ZERO alterations.
- **Inverse-reconstruction (the strongest no-removal proof):** reverting
  the two enumerated edits at their recorded positions reproduces v56
  byte-identically — the diff is exactly the two items.
- **Content markers:** 30 asserted counts, all green (each = the audited
  v56 count + the item's contribution; three builder-run corrections were
  needed where v56 wraps a phrase across lines — "the same programme",
  "finite rational proof" — or where my own first draft wrapped a marker
  "fifth check / list", "more / certifiable": the gate caught both
  wrap-trap classes and the build failed loud before any write; fixed and
  re-run).
- **Structure:** contributions flow ("as a fourth check list. (xiii)"),
  `\textbf{Scope.}` follows, the Limitations enumerate count unchanged
  (4/4 — the item went INSIDE the existing list), `\item` + 2-space
  indentation matching the registry's style, 5.9 heading/label intact,
  itemize counts unchanged (7/7).

## 4. The verification battery

- **Diff review:** full hunk-by-hunk — exactly the two insertions, nothing
  else moved.
- **Tectonic (in place):** exit 0; **50 pp** (v56: 49 — the +21 lines cross
  a page boundary in the Limitations/figure neighbourhood); **114 warnings
  — EXACTLY v56's 114** (verified by recompiling v56 in a controlled
  comparison run); the only overfull the pre-existing 2.43091pt header
  box; zero undefined references; the two new `\ref{substitutability-
  spectrum}` instances resolve (5 rendered "Section 5.8" strings in the
  text layer).
- **Flat compile (tex + figs_p1 alone, clean dir):** exit 0; 50 pp; 114
  warnings.
- **PDF text layer:** item (xiii) renders complete (once); item renders as
  "(x)" in the roman-numeral registry; both items' full clauses verified
  in the extracted text; no stale markers; (xii), item (ix), the Scope
  sentence, and the closure's own addendum all intact.
- **Visual (VLM raster, pages 6 and 39):** PASS both — no garbled,
  clipped, or overlapping text; the radical, ρ, and σ\* render correctly;
  clean justified body text and list indentation.
- **Never-overwrite honored:** the git tree shows ONLY new files
  (v57.tex, v57.pdf, the wave folder) plus the append-only worklog. The
  v56 warning-comparison recompile touched the shipped v56.pdf; it was
  **restored byte-exact from git immediately** (the same slip-and-restore
  pattern as Tasks 107/109, caught by git status).

## 5. Open items recorded (no action this round, per scope discipline)

- The earlier waves' in-place honest limits (5.8 wave-1's two limits; 5.9's
  limits paragraph) remain in place but are NOT in the Limitations registry
  — the owner's enumeration covered the off-diagonal wave's residuals only;
  adding the others is an option for a future round.
- The continuum slice-minimum itself remains the programme's one honestly
  open mathematical residual (now advertised as such in the registry).
- The Zenodo deposit refresh (owner-side).
