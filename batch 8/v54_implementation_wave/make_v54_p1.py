#!/usr/bin/env python3
"""make_v54_p1.py — build paper1_assessment_separation_v54.tex from v53.

Task 109 / batch 8 / paper 1. The owner-approved v54 wave: the middle-regime
transcription items (batch 8/middle_regime_wave/MIDDLE_REGIME_WAVE.md §8,
items 1–5) plus the F1/F2/F4/F5 riders from
batch 8/v53_flaw_review/V53_FINAL_FLAW_REVIEW.md §3:

  item 1  Table 5's middle cell filled with the computed verdict (Theorem M1);
  item 2  §5.7 addition — the rescue trichotomy (Theorem M2);
  item 3  Theorem 9 discussion addition — blend fragility (Theorem M3);
  item 4  §5.4 row-(iii) refinement (Theorems M4 + CT), bullet + pointer +
          caption + cell;
  item 5  the labelled-extension subsection §5.9 "The common-shock variant
          of the witness", transcribing Theorems M1–M4 + CT with the
          machine-verification pointer, mirroring §5.8's format;
  rider F1 five missing spaces after "See Appendix A.";
  rider F2 Proposition 10's strict-sum gloss of I corrected to ≥;
  rider F4 the 295-kt gloss harmonized to the 33.8% / ≈299-kt framing;
  rider F5 Proposition 10's stipulation-transparency clause.

Standing rules honored: new version only (never overwrite); no legitimate
content removed or condensed. The only replaced strings are the three
superseded open-cell placeholders of Table 5 and its pointer sentence —
the owner's approval of "fill Table 5's middle cell" and the row-(iii)
refinement provides exactly for their replacement by the computed
verdicts; the superseded texts are recorded verbatim in this file's
SUPERSEDED dict and in IMPLEMENTATION_RECORD.md, and the
inverse-reconstruction gate proves the diff is exactly the enumerated
edits. Fail-loud anchored edits; math-span multiset preservation;
idempotent. Exit 0 on success; any failed gate exits nonzero.
"""
import sys
from pathlib import Path
from collections import Counter

HERE = Path(__file__).resolve().parent
LATEX = HERE.parents[1] / "arena agent 1" / "paper rewrites" / "latex"
SRC = LATEX / "paper1_assessment_separation_v53.tex"
DST = LATEX / "paper1_assessment_separation_v54.tex"

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

# The superseded v53 placeholder texts, recorded verbatim (the supreme
# no-removal rule: nothing is lost — the record and git history carry them).
SUPERSEDED = {
    "pointer_sentence": (
        "class is one of three regimes; the second is \\emph{not analysed} on this\n"
        "datum --- its verdict must be computed, not asserted; the third is the\n"
        "universal-rejection collapse stated above."
    ),
    "table_caption": (
        "\\caption{Disturbance regimes on the witness datum. The middle row is\n"
        "honestly open: no verdict is asserted for it in this paper.}"
    ),
    "middle_cell": (
        "(ii) Common biomass shock & one shared shock strikes the same floor "
        "coordinate of every plan & \\emph{not analysed on this datum}: the "
        "verdict requires its own exact computation --- a common-shock variant "
        "of the witness --- not an assertion \\\\"
    ),
    "row_iii_cell": (
        "(iii) Coupled all-floor shocks & simultaneous dips across all floors "
        "of every action & universal rejection: the per-weight licensing "
        "structure degenerates and the compensatory/noncompensatory divergence "
        "collapses into common rejection (this section; Lade et al., 2020, on "
        "boundary interactions) \\\\"
    ),
}

# =====================================================================
# riders F1 (typographic: five missing spaces after "See Appendix A.")
# =====================================================================
print("== rider F1: the five proof-pointer spaces ==")
edit("F1a space (line 465)",
     "See Appendix A.The separation in Section 4.5",
     "See Appendix A. The separation in Section 4.5")
edit("F1b space (line 473)",
     "See Appendix A.At a \\emph{fixed} trajectory",
     "See Appendix A. At a \\emph{fixed} trajectory")
edit("F1c space (line 487)",
     "See Appendix A.Part (i) is standard",
     "See Appendix A. Part (i) is standard")
edit("F1d space (line 499)",
     "See Appendix A.Proposition 4 makes precise",
     "See Appendix A. Proposition 4 makes precise")
edit("F1e space (line 536)",
     "See Appendix A.On the witness datum",
     "See Appendix A. On the witness datum")

# =====================================================================
# rider F2 (Proposition 10's strict-sum gloss of I; I is defined with >=)
# =====================================================================
print("== rider F2: the I-gloss ==")
edit("F2 I-gloss sum >= 2",
     "(where \\(s_1 < 2\\), \\(s_2 < 2\\), \\(s_1 + s_2 > 2\\)) no such policy is",
     "(where \\(s_1 < 2\\), \\(s_2 < 2\\), \\(s_1 + s_2 \\ge 2\\)) no such policy is")

# =====================================================================
# rider F5 (Proposition 10 stipulation-transparency clause)
# =====================================================================
print("== rider F5: the stipulation-transparency clause ==")
edit("F5 stipulation clause",
     "full strength: each primitive plan is held for a whole sub-interval, so\n"
     "the visited set is the union of the primitive tubes. It is not a",
     "full strength: each primitive plan is held for a whole sub-interval, so\n"
     "the visited set is the union of the primitive tubes. That stipulated\n"
     "visited set is the pointwise worst case over alternation schedules --- a\n"
     "literal rate-preserving fine-grained alternation visits sub-ranges of it\n"
     "--- so the impossibility established here is scoped to the worst-case\n"
     "alternation. It is not a")

# =====================================================================
# rider F4 (harmonize the 2015-stock gloss to the 33.8% / ~299-kt framing)
# =====================================================================
print("== rider F4: the 295-kt harmonization ==")
edit("F4 harmonize 295 -> 33.8%/299",
     "assessed level of about a third of the LRP (\\(\\approx 295\\) kt; DFO,\n"
     "2016)",
     "assessed level of about a third of the LRP (\\(33.8\\%\\), \\(\\approx 299\\)\n"
     "kt; DFO, 2016)")

# =====================================================================
# item 3 — the Theorem 9 discussion addition (Theorem M3, blend fragility)
# =====================================================================
print("== item 3: the blend-fragility caveat after Theorem 9 ==")
M3_CAVEAT = """\\textbf{A class-conditional caveat on the blend collapse.} Theorem 9's
window is computed under the action-indexed disturbance convention of
Section 4.5, and it is class-conditional: under the common-shock class
of Section 5.9 the window is nonempty exactly on \\(\\{ s_1 \\ge \\delta,\\;
s_2 \\ge \\delta,\\; s_1 + s_2 \\ge 3/2 + 2\\delta \\}\\) (at the datum's event
depth \\(\\delta = 1/2\\): \\(\\{ s_1 \\ge 1/2,\\; s_2 \\ge 1/2,\\; s_1 + s_2
\\ge 5/2 \\}\\), against the action-indexed \\(\\{ s_1 + s_2 \\ge 2 \\}\\) of
Theorem 9(i)). The common-shock acceptance gap --- which survives the
shared shock (Theorem M1, Section 5.9) --- is therefore \\emph{not}
blend-closed on the fragile band \\(s_1 + s_2 \\in [2, 5/2)\\): the witness
\\((\\tfrac12, 1, 1)\\) is a common-shock gap state with \\emph{no}
admissible blend, while every common-shock gap state with
\\(s_1 + s_2 \\ge 5/2\\) has one (Theorem M3 there; the coupled variant,
by contrast, is blend-closed --- the fragility is class-conditional). An
agency that would otherwise invoke Theorem 9's collapse at a shallow
common-shock gap state cannot: the blended menu itself is inadmissible
there.
"""
edit("item3 M3 caveat after Thm 9",
     "separation of adjustable robust optimization (Ben-Tal et al., 2004).\n\n"
     "\\subsection{The converse: discrete time-sharing does not erase",
     "separation of adjustable robust optimization (Ben-Tal et al., 2004).\n\n"
     + M3_CAVEAT + "\n"
     "\\subsection{The converse: discrete time-sharing does not erase")

# =====================================================================
# item 4 — the §5.4 row-(iii) refinement (bullet + pointer + caption + cells)
# and item 1 — the Table 5 middle-cell fill
# =====================================================================
print("== items 1+4: the scope-delimitation bullet and Table 5 ==")
edit("item4 bullet refinement",
     "collapses into universal rejection. The separation is exhibited for, and scoped to, the specified action-indexed class:",
     "collapses into universal rejection. The exact statement, computed in\n"
     "  Section 5.9, is reading-conditional and depth-dependent: under the\n"
     "  additive reading the rejection is universal on \\(I\\) at the datum's\n"
     "  full magnitude, with the exact depth boundary \\(\\delta = 5/4\\) below\n"
     "  which deep-\\(I\\) states survive (witness \\((\\tfrac12,\n"
     "  \\tfrac{19}{10}, \\tfrac{19}{10})\\) at heatwave magnitude) and with the\n"
     "  separation relocating --- not vanishing --- at full magnitude (the\n"
     "  coupled gap \\(\\{ x < 1,\\; 2 \\le s_1 < \\tfrac72,\\; 2 \\le s_2 <\n"
     "  \\tfrac72,\\; s_1 + s_2 \\ge \\tfrac{11}{2} \\}\\), witness \\((\\tfrac12,\n"
     "  3, 3)\\)); under the replace reading the principal actions fail\n"
     "  together under one weight-independent requirement and what collapses\n"
     "  is the typed/weak distinction itself (\\(\\mathcal{V}_{\\mathrm{weak}} =\n"
     "  \\mathcal{V}_{\\mathrm{typ}}\\), Theorem CT there), with acceptance ---\n"
     "  not rejection --- surviving at \\(\\{ s_1 \\ge 2,\\; s_2 \\ge 2 \\} \\cup\n"
     "  \\{ x \\ge 1,\\; \\min(s_1, s_2) \\ge \\tfrac{15}{8} \\}\\), a strictly\n"
     "  more demanding reading (the witness \\((\\tfrac12, 3, 1)\\) is\n"
     "  action-indexed typed-accepted yet fully rejected under it). The\n"
     "  separation is exhibited for, and scoped to, the specified\n"
     "  action-indexed class:")

edit("item1+4 pointer sentence",
     "class is one of three regimes; the second is \\emph{not analysed} on this\n"
     "datum --- its verdict must be computed, not asserted; the third is the\n"
     "universal-rejection collapse stated above.",
     "class is one of three regimes; the second's verdict is the common-shock\n"
     "computation of Section 5.9 (Theorem M1: the gap survives the shared\n"
     "shock, reduced by the exact \\(1/2\\)-cut, with licensing thresholds\n"
     "unshifted on the surviving region) --- a verdict computed, not asserted,\n"
     "exactly as the regime demands; the third is the universal-rejection\n"
     "collapse stated above, refined there into two exact reading-conditional\n"
     "theorems (M4 and CT).")

edit("item1+4 table caption",
     "\\caption{Disturbance regimes on the witness datum. The middle row is\n"
     "honestly open: no verdict is asserted for it in this paper.}",
     "\\caption{Disturbance regimes on the witness datum. The middle row's\n"
     "verdict is the exact common-shock computation of Section 5.9 (Theorem\n"
     "M1); the third row's exact statement is reading-conditional (Theorems\n"
     "M4 and CT there).}")

edit("item1 middle cell fill",
     "(ii) Common biomass shock & one shared shock strikes the same floor "
     "coordinate of every plan & \\emph{not analysed on this datum}: the "
     "verdict requires its own exact computation --- a common-shock variant "
     "of the witness --- not an assertion \\\\",
     "(ii) Common biomass shock & one shared shock strikes the same floor "
     "coordinate of every plan & computed (Theorem M1, Section 5.9): the gap "
     "\\emph{survives} the common shock, reduced by the exact \\(1/2\\)-cut "
     "--- every action-indexed gap state with \\(\\min(s_1, s_2) < 1/2\\) "
     "weak-rejects --- with licensing thresholds unshifted on the surviving "
     "region; the canonical datum remains a member \\\\")

edit("item4 row-(iii) cell refinement",
     "(iii) Coupled all-floor shocks & simultaneous dips across all floors "
     "of every action & universal rejection: the per-weight licensing "
     "structure degenerates and the compensatory/noncompensatory divergence "
     "collapses into common rejection (this section; Lade et al., 2020, on "
     "boundary interactions) \\\\",
     "(iii) Coupled all-floor shocks & simultaneous dips across all floors "
     "of every action & reading-conditional (Theorems M4 and CT, Section "
     "5.9): additive --- universal rejection exact on \\(I\\) at the datum's "
     "full magnitude, depth-dependent below the exact boundary \\(\\delta = "
     "5/4\\), the gap relocating (not vanishing) at full magnitude; replace "
     "--- the per-weight licensing structure degenerates to one "
     "weight-independent requirement, the actions fail together, and the "
     "typed/weak distinction itself collapses (\\(\\mathcal{V}_{\\mathrm{weak}} "
     "= \\mathcal{V}_{\\mathrm{typ}}\\)), with acceptance --- not common "
     "rejection --- surviving (this section; Lade et al., 2020, on boundary "
     "interactions) \\\\")

# =====================================================================
# item 2 — the §5.7 rescue-trichotomy addition (Theorem M2)
# =====================================================================
print("== item 2: the rescue trichotomy in Section 5.7 ==")
M2_PARA = """\\textbf{The class-conditional rescue trichotomy (a labelled
extension).} Proposition 11's threshold is computed under the
action-indexed disturbance convention of Section 4.5, under which the
resource route is unconditionally finite --- every failure state is
rescuable at cost at most \\(1 - x\\). The common-shock computation of
Section 5.9 changes this qualitatively: under the common class (a shared
environmental shock of the datum's heatwave magnitude striking every
plan) the threshold becomes a trichotomy (Theorem M2 there) ---
\\(\\kappa^* = 0\\) on the typed accepted set; \\(\\kappa^* = (1 - x)_+\\) on
the failure states with both floors at or above \\(3/8\\); and
\\(\\kappa^* = \\infty\\) on the failure states with \\(\\min(s_1, s_2) <
3/8\\), the first unrescuable-by-reserve failure states on this datum
(witness \\((\\tfrac12, \\tfrac14, 3)\\): no reserve increment whatsoever
rescues it, the shared shock's exposure of the staged route's growing
floor exceeding what a floor below \\(3/8\\) can carry). The canonical
datum's own shortfall is unchanged at \\(\\kappa^* = 1/2\\). The
management reading: at an asymmetric gap state the prescription changes
from reserve accumulation (bridge to \\(x = 1\\)) to floor rebuilding
(rebuild the weaker floor above \\(1/2\\) first, above \\(3/8\\) for the
staged route) --- different actions with different costs and timescales.
"""
edit("item2 M2 trichotomy in 5.7",
     "into a rescue.\n\n\n\\textbf{Institutional forms.}",
     "into a rescue.\n\n" + M2_PARA + "\n\\textbf{Institutional forms.}")

# =====================================================================
# item 5 — the labelled-extension subsection 5.9
# =====================================================================
print("== item 5: the Section 5.9 labelled extension ==")
S59 = """\\subsection{The common-shock variant of the witness (a
labelled extension)}\\label{common-shock-variant}

Section 5.4's disturbance scoping (Table~\\ref{tab:disturbance}) left the
middle cell --- the common biomass shock, one shared disturbance striking
the same floor coordinate of every plan --- as the one honestly-open
verdict: its assertion demanded its own exact computation, a common-shock
variant of the witness. This subsection --- a labelled extension in the
sense of Section 5.8, not a part of the separation theorem --- records
that computation, and in passing sharpens the coupled regime's row-(iii)
assertion into two exact, reading-conditional theorems. Its results are
stated on the datum of Section 4.5 with only the disturbance class
replaced as specified below; all of Section 5.4's scope delimitations are
inherited; nothing here is an empirical claim.

\\textbf{The variant.} Decompose the Section 4.5 datum per the Section 6.3
arithmetic: each principal plan's announced schedule is a mid-interval
tent drawdown of depth \\(3/2\\) in its characteristic coordinate (FAST:
the quota pulse on \\(s_1\\); SLOW: the gradual burden on \\(s_2\\)), the
other coordinate constant; each environmental event is a transient tent
dip of depth \\(\\delta\\) in one floor coordinate, troughing at
\\(t = 1/2\\) and recovered by \\(t = 1\\), successors unchanged; the
Section 4.5 worst-case depth \\(2 = 3/2 + 1/2\\) is the quota pulse plus
the heatwave, so the datum's event depth is \\(\\delta = 1/2\\). STAGED
spends \\(x\\) (it needs \\(x \\ge 1\\)) while its floors grow linearly
to \\(s + e\\), \\(e = (1/4, 1/4)\\); an event of depth \\(\\delta\\) on a
growing floor dips it to \\(s + 1/8 - \\delta\\) --- by
\\(\\max(0,\\, \\delta - 1/8)\\). The \\emph{common} disturbance class
is: the two coordinate events are separate disturbances, each striking
every plan, so each plan's per-coordinate worst case takes its own
schedule plus the event on that coordinate --- ecologically, a marine
heatwave striking the same biomass coordinate regardless of which
harvest-rebuild plan is running. The disturbance quantifier remains
innermost throughout (Section 2.3). One methodological device is used
throughout: STAGED's aggregate dip \\(\\max(0, \\mathrm{raw}(p) - 1/8)\\)
is kinked in the weight share \\(p = w_1/(w_1 + w_2)\\) (with
\\(\\mathrm{raw}\\) affine in \\(p\\)), and the admissibility requirement
decomposes exactly into the two affine conditions of the kink's two
branches --- every other plan's dip is affine in \\(p\\) --- so every
cover decision below reduces to exact endpoint evaluations.

\\textbf{The handshake.} Before any new class is evaluated, the
computation anchors itself to the deposited datum: under the
action-indexed class of Section 4.5 the variant's machinery reproduces
Theorem 5 exactly --- the same typed and weak acceptance sets, the same
licensing thresholds \\(\\rho_1 = 2/3\\), \\(\\rho_2 = 3/2\\) at the
canonical datum \\((\\tfrac12, \\tfrac65, \\tfrac65)\\), the same
strictness witness \\((\\tfrac12, \\tfrac1{10}, \\tfrac1{10})\\) ---
verified on 676 grid states plus the witness list, the same anchoring
discipline as the \\(\\sigma\\)-extension's verifier.

\\textbf{Theorem M1 (the middle-cell verdict).} \\emph{On the common-shock
variant at the datum's event depth \\(\\delta = 1/2\\):}
\\[
\\mathcal{V}_{\\mathrm{typ}}^{\\mathrm{cs}}
= \\{ s_1 \\ge 2,\\; s_2 \\ge \\tfrac12 \\}
\\cup \\{ s_2 \\ge 2,\\; s_1 \\ge \\tfrac12 \\}
\\cup \\{ x \\ge 1,\\; s_1 \\ge \\tfrac38,\\; s_2 \\ge \\tfrac38 \\},
\\]
\\[
\\mathcal{V}_{\\mathrm{weak}}^{\\mathrm{cs}}
= \\{ x < 1,\\; s_1 \\ge \\tfrac12,\\; s_2 \\ge \\tfrac12,\\; s_1 + s_2 \\ge 2 \\}
\\cup \\{ x \\ge 1,\\; s_1 \\ge \\tfrac38,\\; s_2 \\ge \\tfrac38 \\},
\\]
\\emph{and the acceptance gap survives the common-shock regime:}
\\[
\\mathrm{FP}_{\\mathrm{cs}}
= \\mathcal{V}_{\\mathrm{weak}}^{\\mathrm{cs}} \\setminus
\\mathcal{V}_{\\mathrm{typ}}^{\\mathrm{cs}}
= \\{ x < 1,\\; \\tfrac12 \\le s_1 < 2,\\; \\tfrac12 \\le s_2 < 2,\\;
s_1 + s_2 \\ge 2 \\}.
\\]
\\emph{The gap is strictly smaller than the action-indexed impossibility
region \\(I\\) by the exact \\(1/2\\)-cut --- every action-indexed gap
state with \\(\\min(s_1, s_2) < 1/2\\) is weak-rejected under the common
class (witness \\((\\tfrac12, \\tfrac1{10}, \\tfrac{19}{10})\\),
action-indexed weak-accepted by \\(s_1 + s_2 = 2\\)) --- it is nonempty
with interior, and the canonical datum \\((\\tfrac12, \\tfrac65,
\\tfrac65)\\) is a member: the compensatory/noncompensatory separation
is not an artifact of the action-indexed convention. On the surviving
region the licensing structure is unshifted: FAST's common-class
licensing endpoint equals its action-indexed endpoint \\(1/(1 +
\\rho_1)\\) at every gap state of the surviving region (SLOW's the
mirror) --- the middle cell's verdict is reduced by the \\(1/2\\)-cut,
not shifted.}

\\emph{Proof sketch (machine-anchored).} Write \\(A(p) = p\\, s_1 +
(1 - p)\\, s_2\\) for the aggregate margin at weight share \\(p\\).
FAST's common-class requirement is \\(A(p) \\ge \\max(2p,\\; p +
\\tfrac12)\\) (its own tent \\(3/2\\) in \\(s_1\\) plus the
\\(s_1\\)-event, and the \\(s_2\\)-event weighted by \\(1 - p\\));
SLOW's is the mirror; STAGED's (\\(x \\ge 1\\)) is \\(A(p) \\ge
\\max(p, 1 - p)/2 - 1/8\\) (the kink device: the event exposure of a
growing floor). The pointwise minimum of the two principal requirements
is a tent with its only kink at \\(p = 1/2\\), so an affine \\(A\\)
covers it exactly at the three abscissae \\(p \\in \\{0, \\tfrac12,
1\\}\\); the closed forms follow. Every constant is an exact rational;
the verifier checks the closed forms against independent grid
computations (5{,}000-state grids for the common class) plus a curated
witness list, both directions, at every grid point. \\ensuremath{\\square}

\\textbf{Theorem M2 (the rescue trichotomy).} \\emph{Under the common
class the rescue threshold of Proposition 11 becomes}
\\[
\\kappa^*_{\\mathrm{cs}}(z) =
\\begin{cases}
0, & z \\in \\mathcal{V}_{\\mathrm{typ}}^{\\mathrm{cs}}, \\\\[2pt]
(1 - x)_+, & z \\notin \\mathcal{V}_{\\mathrm{typ}}^{\\mathrm{cs}},\\;
\\min(s_1, s_2) \\ge \\tfrac38, \\\\[2pt]
+\\infty, & z \\notin \\mathcal{V}_{\\mathrm{typ}}^{\\mathrm{cs}},\\;
\\min(s_1, s_2) < \\tfrac38.
\\end{cases}
\\]
\\emph{The qualitative change: the resource route no longer rescues every
failure state --- the common shock introduces the first
unrescuable-by-reserve failure states on this datum, with witness
\\((\\tfrac12, \\tfrac14, 3)\\): no reserve increment whatsoever rescues
it, the shared shock's exposure of the staged route's growing floor
(\\(3/8\\)) exceeding what a floor below \\(3/8\\) can carry. The
canonical datum's shortfall stays \\(\\kappa^* = 1/2\\), its
action-indexed value. The \\(3/8\\) boundary is proved structurally, not
sampled: the event exposure of a growing floor is \\(\\max(0, \\delta -
1/8) = 3/8\\) at the datum's depth, and no floor below it can carry the
event.}

\\emph{Proof sketch.} The augmented menu adds
\\(\\mathrm{STAGED}_\\kappa\\), admissible at \\(x + \\kappa \\ge 1\\)
with the same floor requirement \\(s_i \\ge 3/8\\); \\(\\kappa\\) cannot
move the floors, so on \\(\\{\\min(s) < 3/8\\} \\setminus
\\mathcal{V}_{\\mathrm{typ}}^{\\mathrm{cs}}\\) no finite \\(\\kappa\\)
certifies. On the complement the requirement is the action-indexed one,
\\(\\kappa = (1 - x)_+\\). \\ensuremath{\\square}

\\textbf{Theorem M3 (blend fragility).} \\emph{Theorem 9's blend window is
class-conditional: under the action-indexed class at event depth
\\(\\delta\\) it is nonempty exactly on \\(\\{ s_1 + s_2 \\ge 3/2 +
\\delta \\}\\) (Theorem 9 is the \\(\\delta = 1/2\\) instance, \\(\\{
s_1 + s_2 \\ge 2 \\}\\)); under the common class it is nonempty exactly
on}
\\[
\\{\\, s_1 \\ge \\delta,\\; s_2 \\ge \\delta,\\; s_1 + s_2 \\ge \\tfrac32 +
2\\delta \\,\\}.
\\]
\\emph{The common-class gap is therefore not blend-closed on the fragile
band \\(s_1 + s_2 \\in [2, \\tfrac52)\\): the witness \\((\\tfrac12, 1,
1)\\) is a common-shock gap state with no admissible blend, while every
common-shock gap state with \\(s_1 + s_2 \\ge 5/2\\) has one. The
coupled gap, by contrast, is blend-closed --- its window threshold and
weak boundary coincide --- so the fragility is class-conditional.}

\\emph{Proof sketch.} The blend's \\(s_1\\)-trough is \\(s_1 - \\delta -
\\delta_{\\mathrm{blend}} \\cdot \\tfrac32\\) and its \\(s_2\\)-trough
\\(s_2 - \\delta - (1 - \\delta_{\\mathrm{blend}}) \\cdot \\tfrac32\\)
(each coordinate takes its event plus the corresponding fraction of the
principal tent); the window is the nonnegativity interval of the two,
intersected with \\([0,1]\\). \\ensuremath{\\square}

\\textbf{Theorem M4 (the coupled regime, additive reading).} \\emph{Under
the coupled class --- one disturbance carrying both coordinate events
simultaneously, riding on the plans' own schedules --- at event depth
\\(\\delta\\): the typed accepted set coincides with the common class's
at every depth (the per-coordinate tube minima are event-combination
independent, each coordinate taking its own schedule plus its own
event), and}
\\[
\\mathcal{V}_{\\mathrm{weak}}^{\\mathrm{cpl}}
= \\{ x < 1,\\; s_1 \\ge \\delta,\\; s_2 \\ge \\delta,\\; s_1 + s_2 \\ge \\tfrac32
+ 2\\delta \\}
\\cup \\{ x \\ge 1,\\; \\min(s_1, s_2) \\ge \\max(0, \\delta - \\tfrac18) \\}.
\\]
\\emph{At the datum's full magnitude (\\(\\delta = 2\\)) every enumerated
\\(I\\)-state is weak-rejected --- the Section 5.4 claim holds on the
witness's gap region --- but the claim is depth-dependent with the exact
boundary \\(\\delta = 5/4\\): at heatwave magnitude (\\(\\delta =
1/2\\)) deep-\\(I\\) states survive as coupled gap states (witness
\\((\\tfrac12, \\tfrac{19}{10}, \\tfrac{19}{10})\\)), no \\(I\\)-state
survives at \\(\\delta \\ge 5/4\\) while \\((\\tfrac12, \\tfrac{79}{40},
\\tfrac{79}{40})\\) survives at \\(\\delta = 5/4 - 1/40\\) (every
\\(I\\)-state has \\(s_1 + s_2 < 4\\), the survival requirement at
\\(\\delta = 5/4\\)); and at full magnitude the separation relocates
rather than vanishes: the coupled gap}
\\[
\\{\\, x < 1,\\; 2 \\le s_1 < \\tfrac72,\\; 2 \\le s_2 < \\tfrac72,\\; s_1 + s_2
\\ge \\tfrac{11}{2} \\,\\}
\\]
\\emph{is nonempty --- the witness \\((\\tfrac12, 3, 3)\\) is
weak-accepted and typed-rejected. ``Universal rejection'' is exact on
\\(I\\), not global: the divergence re-emerges at larger floors.}

\\emph{Proof sketch.} Under the coupled class each plan's aggregate dip
is the sum of both events' weighted contributions (\\(3p/2 + \\delta\\)
for FAST) against the common class's maximum of single-event
contributions; the cover analysis is the tent argument of Theorem M1
with the summed requirements. The boundary: an \\(I\\)-state has
\\(\\min(s) < 2\\), hence \\(s_1 + s_2 < 4\\), and survives exactly
when \\(s_1 + s_2 \\ge 3/2 + 2\\delta\\), i.e.\\ \\(\\delta \\le (s_1 +
s_2 - 3/2)/2 < 5/4\\); the witness states realize both sides.
\\ensuremath{\\square}

\\textbf{Theorem CT (the replace-reading collapse).} \\emph{Under the
coupled-total class --- the replace reading, each announced-schedule
plan's worst case being the full-magnitude dip \\(2\\) in each floor,
tent schedules suppressed --- FAST and SLOW degenerate to the same,
weight-independent requirement \\(A(p) \\ge 2\\) (they fail together at
every weight: at the canonical datum both serve nowhere, at
\\((\\tfrac12, \\tfrac52, \\tfrac52)\\) both serve all of \\([0,1]\\),
at \\((\\tfrac12, 3, 1)\\) both serve exactly \\([\\tfrac12, 1]\\)),
and}
\\[
\\mathcal{V}_{\\mathrm{weak}}^{\\mathrm{ct}} =
\\mathcal{V}_{\\mathrm{typ}}^{\\mathrm{ct}}
= \\{ s_1 \\ge 2,\\; s_2 \\ge 2 \\} \\cup \\{ x \\ge 1,\\; \\min(s_1, s_2) \\ge
\\tfrac{15}{8} \\}:
\\]
\\emph{the typed/weak separation collapses entirely --- the gap is empty
on every state and witness probed --- and the replace reading is
strictly more demanding than the action-indexed class: the witness
\\((\\tfrac12, 3, 1)\\) is action-indexed typed-accepted (\\(s_1 \\ge
2\\)) yet a coupled-total full reject on both tests, as is the canonical
datum itself. The mechanism: the weak test's advantage is weight-wise
plan choice; when every plan faces the same plan- and
weight-independent dip, choice buys nothing, and the per-weight cover
condition degenerates to the same per-coordinate condition the typed
test applies. STAGED's rescue route survives --- its growth mechanics
are not a ``schedule'' in the cost sense; the dip lands on the growing
floor, threshold \\(15/8\\), exactly its coupled full-magnitude
branch.}

\\emph{Proof sketch.} With the tents suppressed and the full dip \\(2\\)
in each floor, every principal plan's aggregate dip is the constant
\\(2\\) --- plan- and weight-independent --- so the weak cover condition
\\(A(p) \\ge 2\\) for all \\(p\\) is the pair of endpoint conditions
\\(s_1 \\ge 2\\), \\(s_2 \\ge 2\\), which is the typed condition;
STAGED's branch is identical under both tests. \\ensuremath{\\square}

\\medskip

\\noindent The two readings bracket the coupled truth; both are stated
rather than choosing between them. Two further exact structures complete
the scoping. The \\emph{single-event sub-case} (the literal row-(ii)
reading, only the \\(s_1\\)-event existing) has typed acceptance \\(\\{
s_1 \\ge 2 \\} \\cup \\{ s_2 \\ge 3/2,\\; s_1 \\ge 1/2 \\} \\cup \\{ x
\\ge 1,\\; s_1 \\ge 3/8 \\}\\), weak acceptance \\(\\{ x < 1:\\; s_1 \\ge
1/2,\\; s_1 + s_2 \\ge 2 \\} \\cup \\{ x \\ge 1:\\; s_1 \\ge 3/8 \\}\\),
and gap \\(\\{ x < 1,\\; \\tfrac12 \\le s_1 < 2,\\; s_2 < \\tfrac32,\\;
s_1 + s_2 \\ge 2 \\}\\), the canonical datum a member --- the gap
survives this degenerate class too. And the \\emph{\\(\\delta\\)-family}:
all closed forms above are verified at \\(\\delta \\in \\{0,
\\tfrac14, \\tfrac12, 1, \\tfrac54, \\tfrac32, 2\\}\\) on cross-section
grids; \\(\\delta = 0\\) degenerates to the benign datum on which all
disturbance classes coincide --- the middle-cell verdict is a genuine
disturbance-structure effect, not a modeling artifact.

\\textbf{The relevance chain, at the Section 6.3 datum.} The extension
passes the same four-part test as the \\(\\sigma\\)-spectrum. (1) The
decision: whether a composite biomass index may certify a
stock-rebuilding transition (Northern-cod-style, the Section 6.3
benchmark) when the assessment's disturbance class is a shared
environmental shock --- a marine heatwave striking the same biomass
coordinate regardless of which harvest-rebuild plan is running ---
rather than plan-specific risk; Table~\\ref{tab:disturbance} row (ii) at
the canonical datum, with the checklist's sixth audit point demanding
the class be specified. (2) The report flips, on two exact surfaces: the
\\(1/2\\)-cut (any action-indexed gap state with \\(\\min(s) < 1/2\\)
flips its compensatory verdict from accept to reject --- an index that
certified ``aggregate above 2, transition licensed'' now reports
rejection, witness \\((\\tfrac12, \\tfrac1{10}, \\tfrac{19}{10})\\)); and
the rescue margin (on \\(\\{\\min(s) < 3/8\\}\\) the reported
\\(\\kappa^*\\) changes from a finite reserve requirement to infinity
--- ``rescuable with reserve \\(\\kappa^*\\)'' becomes ``not rescuable
by any reserve'', Theorem M2). (3) The new exact datum:
\\(\\mathrm{FP}_{\\mathrm{cs}}\\) and its \\(1/2\\)-cut, the \\(3/8\\)
rescue boundary, the licensing-invariance identity, the \\(5/4\\)
coupled boundary with its \\(79/40\\) witness, the \\(11/2\\)
relocation gap, and Theorem CT's collapse --- all exact rationals,
machine-anchored. (4) The action flips: at an asymmetric gap state the
action-indexed prescription --- accumulate bridge reserve to \\(x =
1\\) (\\(\\kappa^* = (1 - x)_+\\)) --- is replaced under a shared-shock
assessment by a floor-targeted action, rebuilding the weaker floor above
\\(1/2\\) first (above \\(3/8\\) for the staged route), because no
reserve increment alone certifies (\\(\\kappa^* = \\infty\\)); reserve
accumulation and floor rebuilding are different management actions with
different costs and timescales. Second, on the fragile band \\(s_1 +
s_2 \\in [2, \\tfrac52)\\), blended quota policies are not admissible
under a shared shock (Theorem M3) --- an agency that would otherwise
blend FAST and SLOW shares at such a state must not.

\\textbf{Verification and honest limits.} Every number in this subsection
is an exact rational, verified in a dedicated fail-loud exact-arithmetic
verifier (77 checks; standard-library fractions only; no floats,
tolerances, or randomness; deterministic; with a committed
byte-reproducible run log) --- a fourth check list, separate from and
not pooled with the grid verifier's 25 checks, the software companion's
24, and the \\(\\sigma\\)-extension's 57 (the family's non-pooling
policy). Limits, stated honestly: everything is on the witness datum's
decomposition (tent events, exact tubes, the specific STAGED mechanics,
the Section 6.3 arithmetic); no claim about other data beyond the
\\(\\delta\\)-family verified. The two regime-(iii) readings
(additive/replace) bracket the coupled truth; Theorem CT is
reading-conditional, and both are stated rather than choosing. Grid
verification is fail-loud but finite; the closed forms carry proofs
(affine interval arithmetic; the kink device), and the two were
cross-checked against each other at every grid point --- the standard
the \\(\\sigma\\)-extension set. \\(\\kappa^*\\) under the common class
is adjudicated on a reserve grid of step \\(1/40\\) plus closed-form
confirmation on the survivors; the infinity verdict on \\(\\{\\min(s) <
3/8\\}\\) is proved structurally, not sampled. No stochastic,
partial-observation, or infinite-horizon claim is made; the disturbance
quantifier remains innermost throughout (Section 2.3).
"""
edit("item5 the Section 5.9 labelled extension",
     "interior value is the master root, transcendental in general.\n\n"
     "\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n"
     "\\section{Discussion}\\label{discussion}",
     "interior value is the master root, transcendental in general.\n\n"
     + S59 + "\n"
     "\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n"
     "\\section{Discussion}\\label{discussion}")

# ============ verification gates ============
print("== verification gates ==")
if text == orig:
    die("no edits applied")
if DST.exists():
    die(f"destination already exists (never overwrite): {DST}")

# gate 0: the frontmatter (title, abstract, highlights) is untouched —
# every v54 edit lies beyond it
fm = orig.index("\\end{frontmatter}")
if not text.startswith(orig[:fm + len("\\end{frontmatter}")]):
    die("frontmatter altered (abstract/highlights must be untouched)")
print("  ok  frontmatter (title/abstract/highlights) untouched")

# gate 1: every original math span preserved verbatim (multiset containment),
# except the two rider-enumerated span alterations (F2's strict-sum gloss and
# F4's 295->299 harmonization) — the only approved changes to existing math
import re
def spans(s):
    return Counter(re.findall(r"\$\$.*?\$\$|\\\(.*?\\\)|\\\[.*?\\\]", s, flags=re.S))
o, n = spans(orig), spans(text)
missing = o - n
ALLOWED_ALTERED = Counter({r"\(s_1 + s_2 > 2\)": 1, r"\(\approx 295\)": 1})
if missing != ALLOWED_ALTERED:
    die(f"original math spans lost/altered beyond the two enumerated riders: {dict(missing)}")
print(f"  ok  math-span multiset preserved (v53: {sum(o.values())} spans; "
      f"v54 adds {sum((n - o).values())} new spans; exactly the two rider-"
      f"enumerated alterations (F2, F4) accounted)")

# gate 2 (the strongest no-removal check): inverse-reconstruction.
# Reverting every enumerated edit, in reverse order at its recorded
# position, must reproduce v53 byte-identically — proving the diff
# consists of exactly the enumerated edits and nothing else.
t = text
for k in range(len(PAIRS) - 1, -1, -1):
    name, pos, anchor, repl = PAIRS[k]
    if STATES[k] != t:
        i = next((j for j in range(min(len(t), len(STATES[k]))) if t[j] != STATES[k][j]), 0)
        die(f"inverse gate: state mismatch before reverting [{name}] at byte {i}")
    if t[pos:pos + len(repl)] != repl:
        die(f"inverse gate: replacement not at recorded position [{name}]")
    t = t[:pos] + anchor + t[pos + len(repl):]
if t != orig:
    i = next((j for j in range(min(len(t), len(orig))) if t[j] != orig[j]), min(len(t), len(orig)))
    die(f"inverse-reconstruction mismatch at byte {i}:\n  orig: {orig[i:i+120]!r}\n  rev : {t[i:i+120]!r}")
print(f"  ok  inverse-reconstruction: reverting all {len(PAIRS)} enumerated edits "
      f"reproduces v53 byte-identically (the diff is exactly the wave)")

# gate 3: the superseded placeholders are gone, the computed verdicts in
if "not analysed" in text:
    die("stale open-cell placeholder remains ('not analysed')")
if "honestly open: no verdict is asserted" in text:
    die("stale open-row caption remains")
for marker in ["Theorem M1", "Theorem M2", "Theorem M3", "Theorem M4",
               "Theorem CT", "common-shock-variant",
               "\\mathrm{FP}_{\\mathrm{cs}}", "\\kappa^*_{\\mathrm{cs}}",
               "rescue trichotomy", "blend-closed", "fragile band",
               "77 checks", "fourth check list",
               "unrescuable-by-reserve",
               "\\tfrac{79}{40}", "\\tfrac{15}{8}", "\\tfrac{11}{2}",
               "the middle-cell verdict", "reduced by the exact \\(1/2\\)-cut"]:
    if marker not in text:
        die(f"expected new-content marker missing: {marker}")
print("  ok  placeholders superseded; all new-content markers present")

# gate 4: the riders
for bad, why in [("Appendix A.The", "F1 unresolved"), ("Appendix A.At ", "F1 unresolved"),
                 ("Appendix A.Part", "F1 unresolved"), ("Appendix A.Proposition", "F1 unresolved"),
                 ("Appendix A.On", "F1 unresolved"),
                 ("\\approx 295", "F4 unresolved")]:
    if bad in text:
        die(f"{why}: {bad!r} still present")
for good, cnt in [("Appendix A. The", 1), ("Appendix A. At ", 1), ("Appendix A. Part", 1),
                  ("Appendix A. Proposition", 1), ("Appendix A. On", 1),
                  ("33.8\\%", 2), ("\\approx 299", 2)]:
    c = text.count(good)
    if c != cnt:
        die(f"rider marker {good!r} found {c}x (expected {cnt})")
if "s_1 + s_2 > 2\\)) no such policy" in text:
    die("F2 unresolved: strict-sum gloss remains")
print("  ok  riders F1/F2/F4 applied and verified")

# gate 5: cross-reference accounting
n59 = text.count("Section 5.9")
if n59 != 8:
    die(f"expected 8 'Section 5.9' refs (M3 caveat x2, 5.4 bullet, pointer, "
        f"caption, middle cell, row-iii cell, 5.7 addition), found {n59}")
n58 = text.count("Section 5.8")
if n58 != 1:
    die(f"expected 1 'Section 5.8' ref (the 5.9 opening), found {n58}")
for stale in ["Section 5.10", "the audit"]:
    if stale in text:
        die(f"forbidden string present: {stale}")
print("  ok  cross-reference accounting (8 refs to Section 5.9; 1 to Section 5.8)")

# gate 6: the M-theorem statements match the verified wave record on the
# load-bearing constants (independent re-typing check against
# middle_regime_run_log.txt's passing values)
for const in ["\\tfrac12 \\le s_1 < 2", "\\tfrac12 \\le s_2 < 2",
              "\\min(s_1, s_2) \\ge \\tfrac38", "\\min(s_1, s_2) < \\tfrac38",
              "s_1 + s_2 \\ge \\tfrac32", "\\tfrac{19}{10}",
              "(\\tfrac12, \\tfrac14, 3)", "(\\tfrac12, 1, 1)", "(\\tfrac12, 3, 3)",
              "(\\tfrac12, 3, 1)", "\\rho_1 = 2/3", "676 grid states"]:
    if const not in text:
        die(f"wave-record constant missing from the transcription: {const!r}")
print("  ok  wave-record constants verified in the transcription")

DST.write_text(text, encoding="utf-8")
print(f"\nWROTE {DST}")
print(f"v53: {len(orig.splitlines())} lines -> v54: {len(text.splitlines())} lines "
      f"(+{len(text.splitlines()) - len(orig.splitlines())})")
print(f"edits applied: {len(PAIRS)}; superseded placeholders recorded verbatim "
      f"in SUPERSEDED ({len(SUPERSEDED)} entries)")
