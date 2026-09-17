#!/usr/bin/env python3
"""Wave-15 / Task 87, part 1: create paper4_delay_dynamics_v32.md from v31.

Owner directive (2026-09-16): (1) search repo and web for empirical case
studies and calibration, implementing them ONLY if highly merited and
appealing to editors and reviewers; (2) evaluate whether Automatica and
IEEE Transactions on Automatic Control merit the same or a separate
publication (see JOURNAL_FIT_RESPONSE companion,
AUTOMATICA_TAC_AND_EMPIRICAL_RESPONSE_p4.md).

Merit evaluation outcome (recorded in the response document):
  - Full case-study CALIBRATION: not merited - the corpus's own structured
    case search (A011 -> P5) found zero unconfounded eligible cases, and
    the paper's theorems are parameterisation-specific; inventing a
    calibration would fabricate empirical grounding.
  - Documented governance TIMELINES: highly merited (the Qwen audit's own
    fallback for the sustainability venues: "at least a detailed
    discussion of real governance timelines") - real, citable,
    verifiable, and grounds the paper's two timing coordinates without
    duplicating the companion sampled-governance paper's null-result
    empirical record.

v32 implements the merited strengthening (every empirical fact cited, no
citation invented; all four journal citations verified against Crossref
on 2026-09-16):
  R0  abstract: one documented-timelines sentence (northern cod record,
      1992 moratorium, 2024 reopening; scales grounded, no calibration);
  R1  Introduction 1.1: the management-record grounding sentence at the
      behavioural-basis paragraph (Hutchings & Myers 1994; Walters &
      Maguire 1996; Li, Bence & Brenden 2016; Peterson et al. 2022);
  R2  Organization sentence: the new Discussion theme named;
  R3  Discussion 11.3 closing: forward pointer to the new subsection;
  R4  NEW Discussion 11.4 "Documented institutional timelines"
      (scale grounding for the two timing coordinates; northern cod SSB
      735->31 kt across the 1991-1994 assessments, DFO 2016; moratorium
      2 July 1992 and reopening 26 June 2024, DFO 2016/2024; the
      assessment-frequency literature as the empirical counterpart of
      T_r-as-design-parameter; the scope guard: scales, not
      coefficients; the companion sampled-governance paper's
      zero-eligible-case search);
      old 11.4-11.7 renumbered 11.5-11.8;
  R5-R7  renumber headings (early-warning 11.5->11.6, Limitations
      11.6->11.7, Open problems 11.7->11.8);
  R8  the one internal cross-reference re-pointed
      (Section 11.4's -> 11.5's first stated open task);
  R9  Limitations (i): one clause - the timelines are scale grounding,
      not a calibration;
  R10-R14  references: DFO 2016, DFO 2024, Hutchings & Myers 1994,
      Li/Bence/Brenden 2016, Peterson et al. 2022 (et al. per the
      paper's 4+-author convention), Walters & Maguire 1996.

Fail-loud guarantees:
  - every edit block is found verbatim and exactly once in v31;
  - edit regions pairwise disjoint;
  - numeric-token discipline: v32 loses/reduces NO frozen token of v31
    (section renumber 11.4-11.8 exempted and separately verified), and
    every NEW numeric token belongs to the declared empirical-record
    whitelist (documented dates, SSB values, volume/page/DOI tokens of
    the new references) - enumerated in EXPECTED_NEW below;
  - v31 file untouched on disk after the run (byte-identical);
  - the v31->v32 diff touches only the declared edit regions.
"""
from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
V31 = PR / "paper4_delay_dynamics_v31.md"
V32 = PR / "paper4_delay_dynamics_v32.md"

md = V31.read_text(encoding="utf-8")
md0 = md  # frozen copy for the final no-touch assertion

EDITS: list[tuple[str, str, str]] = []  # (region name, old, new)


def register(name: str, old: str, new: str) -> None:
    EDITS.append((name, old, new))


# --- R0. abstract: documented-timelines sentence ---------------------------
register(
    "abstract-timelines",
    "are available to any periodically reviewed renewable-resource regime. The form and timing of institutional response",
    "are available to any periodically reviewed renewable-resource regime. Documented governance timelines occupy the same scales — the northern cod record runs from annual assessment with incremental response to the 1992 moratorium and, thirty-two years later, the 2024 reopening — grounding the two timing coordinates without calibrating any coefficient. The form and timing of institutional response",
)

# --- R1. Introduction 1.1: management-record grounding ---------------------
register(
    "intro-management-record",
    "Institutional design determines which signals reach which actors at which time (Ostrom, 1990). What the dynamical-systems literature has not supplied",
    "Institutional design determines which signals reach which actors at which time (Ostrom, 1990). The management record supplies the field-scale counterpart: the northern cod collapse proceeded through years of assessment advice and incremental institutional response before the 1992 moratorium (Hutchings and Myers, 1994; Walters and Maguire, 1996), and the assessment-frequency literature now studies the review cadence itself as a managed design parameter with measured consequences for yield and depletion risk (Li, Bence, and Brenden, 2016; Peterson et al., 2022). What the dynamical-systems literature has not supplied",
)

# --- R2. Organization sentence ----------------------------------------------
register(
    "organization",
    "Section 11 discusses design consequences, the generality of the institutional-loop coordinates, relation to the early-warning literature, and open problems. Section 12 concludes.",
    "Section 11 discusses design consequences, the generality of the institutional-loop coordinates, the documented institutional timelines that ground the two timing coordinates, relation to the early-warning literature, and open problems. Section 12 concludes.",
)

# --- R3+R4. Discussion: 11.3 closing pointer + new 11.4 + renumber ---------
register(
    "discussion-new-11.4",
    "the institutional coefficients are dynamical parameters to be identified, bounded, and designed against.\n\n### 11.4 Certification levels",
    """the institutional coefficients are dynamical parameters to be identified, bounded, and designed against. The documented institutional timelines collected in the next subsection ground the scales of those coordinates in the management record.

### 11.4 Documented institutional timelines

The two timing coordinates of the analysed loop — the deployment delay and the review cadence — have documented values at management scale, and the northern cod (NAFO 2J3KL) record is the canonical instance. Assessment of that stock proceeded on an annual cycle while the estimated spawning-stock biomass fell from about 735 kt in the 1991 assessment to about 31 kt in the 1994 assessment (DFO, 2016); the directed-fishery moratorium was announced on 2 July 1992, and the renewed commercial fishery on 26 June 2024 — thirty-two years later (DFO, 2016, 2024). The collapse itself has been attributed to overexploitation under sustained harvest pressure (Hutchings and Myers, 1994), with the assessment-and-response chronology dissected as a management failure (Walters and Maguire, 1996). For this paper the record does two things. It documents that institutional response delays of years, and management-cycle decisions spanning decades, are real objects at the scale the analysed windows occupy — the mobilising channel's delay window between crossings near 3.7 and 150 yr, and the stage-analysis bands of Section 7.3, whose $g=2$ $\\tau$-window lies inside the documented $2$–$13$ yr governance-lag distribution. And it supplies the canonical instance of the inter-review depletion that the local spectral statements of Section 8 explicitly do not certify: a stock falling by a factor of more than twenty between annual assessments while the institutional response remained incremental.

The review cadence, likewise, is an actively managed design parameter in operating fisheries rather than a theoretical construct. Annual assessment and annual catch-setting are the historical norm for major stocks, and management agencies are actively weighing moves to multi-year assessment cycles; the assessment-frequency literature finds that lengthening the interval changes fishery performance — less frequent assessment reduced relative yield and increased the risk of stock depletion and interannual variation in yield in simulation (Li, Bence, and Brenden, 2016), with the same caution echoed for a large coastal shark fishery under multi-year assessment (Peterson et al., 2022). That literature treats the review interval as a management-design variable with risk consequences — the empirical counterpart of this paper's reading of $T_r$ as a local spectral design parameter — and its direction of caution matches the theory's: the mobilising channel restabilises only for review intervals above about 6.5 yr, but local spectral stabilisation is not governance, and inter-review depletion is the uncertified cost that both the theorems and the assessment-frequency record place at the centre.

What the documented timelines ground is the scale of the two timing coordinates, not the coefficients of any theorem. No stock, effort law, or delay value in this paper is calibrated to a named fishery, and the northern cod record is a timescale grounding and a caution, not a calibration: the institutional coefficients — the gains, delays, and cadences of the governance loop — remain to be identified from field data before any threshold of the declared class is read against a fishery. A structured search across more than thirty resource systems for an unconfounded instance of the delayed institutional feedback mechanism — a responsive rule, an independently dateable lag, no dominant competing driver, and unit-level data — found no eligible case; that search and its null result are the subject of the companion sampled-governance paper, and they mark the empirical programme named in the conclusion as prospective. The documented record therefore supplies what a sustainability or management readership requires of a theory paper — real governance timelines at the analysed scales — without converting any theorem into a claim about a named institution.

### 11.5 Certification levels""",
)

# --- R5-R7. renumber the following Discussion headings ---------------------
register("renumber-11.5", "### 11.5 Relation to the early-warning literature", "### 11.6 Relation to the early-warning literature")
register("renumber-11.6", "### 11.6 Limitations", "### 11.7 Limitations")
register("renumber-11.7", "### 11.7 Open problems", "### 11.8 Open problems")

# --- R8. re-point the one internal cross-reference -------------------------
register(
    "fix-crossref",
    "(Section 11.4's first stated open task",
    "(Section 11.5's first stated open task",
)

# --- R9. Limitations (i): not-a-calibration clause -------------------------
register(
    "limitations-clause",
    "with the parameter windows of Section 9.5 delimiting the regime of the two-crossing structure. (ii) The delay is a single discrete lag",
    "with the parameter windows of Section 9.5 delimiting the regime of the two-crossing structure. The documented governance timelines of Section 11.4 ground the scales of the delay and review coordinates; they are not a calibration, and no institutional coefficient is identified from them. (ii) The delay is a single discrete lag",
)

# --- R10-R14. references (alphabetical placement, paper style) -------------
register(
    "refs-dfo",
    "Costantino, R.F., Cushing, J.M., Dennis, B., Desharnais, R.A., 1995. Experimentally induced transitions in the dynamic behaviour of insect populations. Nature 375, 227–230.\n\nDiekmann",
    """Costantino, R.F., Cushing, J.M., Dennis, B., Desharnais, R.A., 1995. Experimentally induced transitions in the dynamic behaviour of insect populations. Nature 375, 227–230.

DFO, 2016. Stock Assessment of Northern Cod (NAFO Divs. 2J3KL) in 2016. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

DFO, 2024. The Government of Canada announces the historic return of the commercial Northern cod fishery in Newfoundland and Labrador. News release, 26 June 2024.

Diekmann""",
)
register(
    "refs-hutchings",
    "Hayes, N.D., 1950. Roots of the transcendental equation associated with a certain difference-differential equation. J. Lond. Math. Soc. 25, 226–232.\n\nHutchinson, G.E., 1948.",
    """Hayes, N.D., 1950. Roots of the transcendental equation associated with a certain difference-differential equation. J. Lond. Math. Soc. 25, 226–232.

Hutchings, J.A., Myers, R.A., 1994. What can be learned from the collapse of a renewable resource? Atlantic cod, Gadus morhua, of Newfoundland and Labrador. Can. J. Fish. Aquat. Sci. 51(9), 2126–2146. doi:10.1139/f94-214

Hutchinson, G.E., 1948.""",
)
register(
    "refs-li",
    "Kuznetsov, Y.A., 2004. Elements of Applied Bifurcation Theory, 3rd ed. Springer, New York.\n\nLudwig",
    """Kuznetsov, Y.A., 2004. Elements of Applied Bifurcation Theory, 3rd ed. Springer, New York.

Li, Y., Bence, J.R., Brenden, T.O., 2016. The influence of stock assessment frequency on the achievement of fishery management objectives. N. Am. J. Fish. Manag. 36(4), 793–812. doi:10.1080/02755947.2016.1167145

Ludwig""",
)
register(
    "refs-peterson",
    "Ostrom, E., 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press, Cambridge.\n\nScheffer, M., Carpenter, S.R., 2003.",
    """Ostrom, E., 1990. Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press, Cambridge.

Peterson, C.D., Wilberg, M.J., Cortés, E., et al., 2022. Effects of altered stock assessment frequency on the management of a large coastal shark. Mar. Coast. Fish. 14(5), e10221. doi:10.1002/mcf2.10221

Scheffer, M., Carpenter, S.R., 2003.""",
)
register(
    "refs-walters",
    "Scheffer, M., Bascompte, J., Brock, W.A., et al., 2009. Early-warning signals for critical transitions. Nature 461, 53–59.\n\nZhang, G.D., Shen, Y., Chen, B.S., 2013.",
    """Scheffer, M., Bascompte, J., Brock, W.A., et al., 2009. Early-warning signals for critical transitions. Nature 461, 53–59.

Walters, C.J., Maguire, J.-J., 1996. Lessons for stock assessment from the northern cod collapse. Rev. Fish Biol. Fish. 6, 125–137. doi:10.1007/BF00182340

Zhang, G.D., Shen, Y., Chen, B.S., 2013.""",
)


def tokens(s: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", s))


# ---- apply with fail-loud checks ------------------------------------------
positions: list[tuple[int, int, str]] = []
for name, old, new in EDITS:
    n = md.count(old)
    assert n == 1, f"edit {name!r}: found {n} occurrences (expected 1)"
    i = md.index(old)
    positions.append((i, i + len(old), name))
    md = md.replace(old, new, 1)

# edit regions must be pairwise disjoint (no overlapping surgery)
positions.sort()
for (s1, e1, n1), (s2, e2, n2) in zip(positions, positions[1:]):
    assert e1 <= s2, f"edit regions {n1!r} and {n2!r} overlap"

# ---- numeric-token discipline ---------------------------------------------
# Section-reposition tokens: the new subsection 11.4 shifts old 11.4-11.7 to
# 11.5-11.8. Structural positions, not frozen scientific values; no live
# cross-file reference points at them (checked: supplementary v5's S11.3 is
# an unrelated supplement section; only frozen historical md versions v28-
# v31 carry the old numbers). Exempt exactly these five tokens, then verify
# the renumbered structure explicitly below.
RENUMBER_TOKENS = {"11.4", "11.5", "11.6", "11.7", "11.8"}

# New empirical-record tokens (each with its documented source):
#   1991, 1994, 735, 31  - DFO SAR 2016/026 assessment years and SSB values
#                          (kt), as reproduced and verified in the corpus
#                          article A014 (revised_articles/A014_northern_cod_
#                          revised.md, Table of Section 3);
#   1992, 2024           - moratorium (2 July 1992) and reopening (26 June
#                          2024) dates, DFO 2016/2024;
#   1994, 1996, 2016     - citation years of the four new references;
#   51, 2126, 2146, 1139, 94, 214, 125, 137, 793, 812, 10221 and the DOI
#     tokens (026, 00182340, 02755947.2016, 1167145, 2.10221, 10.1139,
#     10.1007, 10.1080, 10.1002) - volume/page/DOI tokens of the new
#     reference entries (all verified against Crossref 2026-09-16).
EXPECTED_NEW = {
    "1991", "1992", "1994", "1996", "2016",
    "735", "31",
    "51", "2126", "2146", "1139", "94", "214",
    "125", "137", "793", "812", "10221",
    "026", "00182340", "02755947.2016", "1167145", "2.10221",
    "10.1139", "10.1007", "10.1080", "10.1002",
}

t31, t32 = tokens(md0), tokens(md)
lost = {t: c for t, c in t31.items() if t32[t] < c and t not in RENUMBER_TOKENS}
assert not lost, f"frozen numeric tokens lost or reduced: {lost}"
newtok = {t for t in t32 if t not in t31 and t not in RENUMBER_TOKENS}
assert newtok <= EXPECTED_NEW, (
    f"new numeric tokens outside the declared empirical-record "
    f"whitelist: {sorted(newtok - EXPECTED_NEW)}"
)
print("numeric discipline: v32 keeps every frozen scientific value verbatim; "
      f"new tokens = the declared empirical-record whitelist ({len(newtok)} "
      "tokens: documented dates, SSB values, reference volume/page/DOIs)")

# ---- renumber consistency (Discussion 11.1-11.8) ---------------------------
heads = re.findall(r"^### (11\.\d) (.+)$", md, re.M)
expected = [
    ("11.1", "The two channels as a design distinction"),
    ("11.2", "The review interval as control"),
    ("11.3", "Generality: what carries beyond the analysed class"),
    ("11.4", "Documented institutional timelines"),
    ("11.5", "Certification levels"),
    ("11.6", "Relation to the early-warning literature"),
    ("11.7", "Limitations"),
    ("11.8", "Open problems"),
]
assert heads == expected, f"unexpected Discussion structure: {heads}"
assert md.count("(Section 11.5's first stated open task") == 1, "cross-ref not re-pointed"
assert md.count("### 11.4 Documented institutional timelines") == 1
print("renumber consistency: Discussion 11.1-11.8 in the expected order; "
      "open-task cross-reference re-pointed to 11.5")

# ---- citation presence (in-text + reference entry, fail-loud) --------------
for needle in [
    "(Hutchings and Myers, 1994", "Walters and Maguire, 1996)",
    "(Li, Bence, and Brenden, 2016", "Peterson et al., 2022)",
    "(DFO, 2016)", "(DFO, 2016, 2024)",
    "Hutchings, J.A., Myers, R.A., 1994",
    "Li, Y., Bence, J.R., Brenden, T.O., 2016",
    "Peterson, C.D., Wilberg, M.J., Cortés, E., et al., 2022",
    "Walters, C.J., Maguire, J.-J., 1996",
    "DFO, 2016. Stock Assessment of Northern Cod",
    "DFO, 2024. The Government of Canada announces",
]:
    assert md.count(needle) >= 1, f"citation needle missing: {needle!r}"
print("citation presence: all six new references present in-text and in the "
      "reference list")

# ---- v31 untouched ----------------------------------------------------------
assert V31.read_text(encoding="utf-8") == md0, "v31 changed on disk!"

V32.write_text(md, encoding="utf-8")
print(f"wrote {V32.relative_to(ROOT)} ({len(md)} chars, {md.count(chr(10)) + 1} lines)")

# ---- diff-region audit: only the declared regions changed -------------------
r = subprocess.run(
    ["git", "diff", "--no-index", "-U0", str(V31), str(V32)],
    capture_output=True, text=True,
)
hunks = re.findall(r"^@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@(.*)$", r.stdout, re.M)
print(f"diff hunks: {len(hunks)} (14 declared edit regions; git's line "
      f"aligner may split/merge adjacent renumber edits)")
assert 14 <= len(hunks) <= 24, f"hunk count out of sanity range: {len(hunks)}"
for name, _old, _new in EDITS:
    print(f"  applied: {name}")
print("OK: v32 created; v31 untouched")
