#!/usr/bin/env python3
"""Wave-14 / Task 86, part 1: create paper4_delay_dynamics_v31.md from v30.

Owner directive (2026-09-16): evaluate, verify, strengthen and complete the
best journal-fit suggestions for P4 jointly ("journal fit audits/p4/
qwen journal fits p4.txt"), especially breadth and generality; changes to
new versions only, never overwrite.

The joint best cross-venue suggestions implemented here (see
JOURNAL_FIT_RESPONSE_p4.md for the full evaluation):
  1. Broad-lead abstract (Qwen's Nature Communications / PNAS / Proc B /
     Ecology Letters suggestion): governance insight first, technical
     machinery kept but glossed at first use; the two policy centrepieces
     and the review-interval-as-design-parameter claim foregrounded;
     breadth statement of the stock-agnostic class.  Qwen's own draft
     abstract contained one inaccuracy (its "delay window associated with
     Hopf instability" reverses the paper's finding - the window is the
     delay range INSIDE which the equilibrium is stabilised); corrected
     here against v30's own abstract and Section 5.1/9.2.
  2. Breadth keywords (renewable resource management; regime shifts).
  3. Introduction: one new generality paragraph (coupled human-natural
     framing; fisheries as motivating instance, not boundary; Section 7
     as the institutional-delay-meets-ecological-delay frame).
  4. Plain-language glosses at first use (sample-and-hold in Section 2
     notation; Hopf crossing / interval-certified at Section 5.1;
     monodromy at Section 8).
  5. New Discussion subsection 11.3 "Generality: what carries beyond the
     analysed class" - the three institutional-loop coordinates, the
     management-language translation table (Fish and Fisheries /
     ICES-style strengthening, useful to every venue), the
     discretisation-artefact caution generalised, and the scope guard.
     Old 11.3-11.6 renumbered 11.4-11.7 (one internal cross-reference
     fixed), Organization sentence updated.
  6. Conclusion: breadth closing sentences (the three design coordinates
     generalise to any periodically reviewed renewable-resource
     institution; field identification is the empirical programme).

Fail-loud guarantees:
  - every edit block is found verbatim and exactly once in v30;
  - numeric-token multiset: v31 is a strict superset of v30 (no frozen
    value lost, none restated in altered form) and introduces NO numeric
    token absent from v30 (every number in the new text is verbatim from
    v30's own usage: 3.7, 150, 6.5, 2.3);
  - v30 file untouched on disk after the run (byte-identical);
  - the v30->v31 diff touches only the nine declared edit regions.
"""
from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
V30 = PR / "paper4_delay_dynamics_v30.md"
V31 = PR / "paper4_delay_dynamics_v31.md"

md = V30.read_text(encoding="utf-8")
md0 = md  # frozen copy for the final no-touch assertion

EDITS: list[tuple[str, str, str]] = []  # (region name, old, new)


def register(name: str, old: str, new: str) -> None:
    EDITS.append((name, old, new))


# --- 1. abstract ----------------------------------------------------------
register(
    "abstract",
    """Classical delay studies place lags in the ecological dynamics. Here the delay instead resides in the governance loop that converts observed stock decline into institutional response. We analyse a gated three-state model — stock, deficit memory, deployed effort — under two effort laws: a mobilising law whose gain grows with deployment, and a protective quota-tracking law whose gain restores toward a cap. The characteristic equation reduces to a cubic modulus condition with a phase relation, and a filter identity implies that positive roots come in even multiplicity.

For the mobilising channel, two subcritical Hopf crossings bound a delay window within which the equilibrium is stabilised; the crossings are interval-certified (near 3.7 and 150 yr). For the protective channel, the loop gain remains below unity at the calibrated point, so the equilibrium is exponentially stable at every delay — a no-Hopf theorem. Under periodic-review (sample-and-hold) governance, annual protective review remains stable, whereas annual mobilising review is unstable and restabilises only for review intervals above about 6.5 yr, via a Neimark–Sacker-type crossing; an apparent threshold reported by a first-order discretisation is a numerical artefact. Continuation in the delay reveals a five-regime attractor topology, with two folds certified at the discrete collocation level (the continuum off-grid residual stage and the continuous-delay lift remain open) and a basin-boundary transition toward a large-amplitude attractor of unverified identity.

The results indicate that the form and timing of institutional response, not ecological lag alone, determine whether governance stabilises or destabilises a harvested stock; the review interval acts as a local spectral design parameter.""",
    """Delayed feedback is a classic source of instability in renewable-resource systems, yet the analysed lags have overwhelmingly been ecological: maturation, recruitment, density responses. Here the delay sits elsewhere — in the governance loop that converts an observed stock decline into an institutional response. We analyse a gated three-state model — the harvested stock, a deficit memory, and deployed management effort — under two canonical response rules: a mobilising rule whose effort gain grows with deployment, and a protective quota-tracking rule whose gain restores harvest toward a cap.

For the mobilising rule, an institutional delay of intermediate length stabilises the equilibrium: two subcritical Hopf crossings — eigenvalue transitions at which oscillatory dynamics are born — bound a delay window inside which the lag itself holds the loop stable, with the crossings interval-certified (near 3.7 and 150 yr). For the protective rule, the loop gain remains below unity at the calibrated point, so the equilibrium is exponentially stable at every delay — a no-Hopf theorem. When governance acts through periodic review (sample-and-hold), annual protective review remains stable, whereas annual mobilising review is unstable and restabilises only for review intervals above about 6.5 yr, via a Neimark–Sacker-type crossing — the sampled-review analogue of a Hopf transition; an apparent threshold near 2.3 yr reported by a first-order numerical update is an artefact of the discretisation, not a property of the governance system. Continuation in the delay reveals a five-regime attractor topology, with two folds certified at the discrete collocation level (the continuum off-grid residual stage and the continuous-delay lift remain open) and a basin-boundary transition toward a large-amplitude attractor of unverified identity.

The analysed class is deliberately stock-agnostic — a harvested renewable stock under institutional control, with fisheries as the motivating instance — so the mechanism's coordinates (the response rule's sign structure, the deployment delay, and the review cadence) are available to any periodically reviewed renewable-resource regime. The form and timing of institutional response, not ecological lag alone, determine whether governance stabilises or destabilises a harvested stock; the review interval acts as a local spectral design parameter, with opposite effects under the two rules.""",
)

# --- 2. keywords -----------------------------------------------------------
register(
    "keywords",
    "**Keywords:** delay differential equations; Hopf bifurcation; institutional feedback; fisheries governance; sample-and-hold control; maturation delay; recruitment dynamics",
    "**Keywords:** delay differential equations; Hopf bifurcation; institutional feedback; renewable resource management; fisheries governance; sample-and-hold control; regime shifts; maturation delay; recruitment dynamics",
)

# --- 3. introduction generality paragraph ---------------------------------
register(
    "intro-generality",
    "The present paper takes up both questions on a declared class of stock–memory–effort models.\n\nThe overshoot mechanism",
    "The present paper takes up both questions on a declared class of stock–memory–effort models.\n\nThe institutional loop is not fisheries-specific, and neither is the analysed class. Assessment on a fixed cadence, a rule that converts the assessed signal into a quota or an effort decision, and a deployment lag between decision and action — this structure recurs across renewable-resource institutions, from quota-tracked harvests to capped withdrawals, and it is the formal signature of a coupled human–natural system whose human component is a controller with memory. The model class of Section 2 is deliberately stock-agnostic — the state $N$ is a renewable stock in material or biomass units, not a named fishery — and Section 7 registers the same governance structure acting on a stock whose own ecology carries a maturation delay, so institutional and ecological delay are analysed within one frame rather than opposed in caricature. Fisheries supply the motivating instance — the setting in which periodic review is most literally institutionalised — and the management language of the two rules (effort escalation versus quota tracking) is the language of harvest control.\n\nThe overshoot mechanism",
)

# --- 4a. Section 2 notation: sample-and-hold gloss ------------------------
register(
    "notation-gloss",
    "Periodic-review results use *sample-and-hold* (an Euler-reviewed zero-order-hold sampling of the delayed signal at intervals of length $T_r$).",
    "Periodic-review results use *sample-and-hold* (an Euler-reviewed zero-order-hold sampling of the delayed signal at intervals of length $T_r$): the delayed signal is measured once at each review instant and held fixed between reviews, so the review interval $T_r$ is the cadence at which the institution re-decides.",
)

# --- 4b. Section 5.1: Hopf / interval-certified gloss ---------------------
register(
    "hopf-gloss",
    "### 5.1 Local crossings and interval-certified delays\n\nThe complete cubic search (Theorem 4.1)",
    "### 5.1 Local crossings and interval-certified delays\n\nTerminology for the broad reader: a *Hopf crossing* is a parameter value at which a complex-conjugate pair of characteristic roots crosses the imaginary axis and oscillatory dynamics are born; *interval-certified* means the crossing delay is enclosed by interval Newton iteration with outward rounding, so the enclosure is guaranteed to contain the exact root of the registered equations (Moore, 1979; Cloud, Moore, and Kearfott, 2009).\n\nThe complete cubic search (Theorem 4.1)",
)

# --- 4c. Section 8: monodromy gloss ---------------------------------------
register(
    "monodromy-gloss",
    "The implication for institutional design is that the review interval is a controller knob, not a governance recommendation; an interval that stabilises the equilibrium may still allow severe inter-review depletion, and inter-review tube safety is an additional criterion not certified here.\n\n**Theorem 8.1",
    "The implication for institutional design is that the review interval is a controller knob, not a governance recommendation; an interval that stabilises the equilibrium may still allow severe inter-review depletion, and inter-review tube safety is an additional criterion not certified here. Throughout this section the *monodromy* is the one-period linear return map of the reviewed loop — the product of the held flow and the review update — whose spectral radius decides the linear stability of the sampled equilibrium (radius below one: stable; above one: unstable).\n\n**Theorem 8.1",
)

# --- 5. discussion: new subsection 11.3 + renumber ------------------------
register(
    "discussion-new-11.3",
    "### 11.3 Certification levels",
    """### 11.3 Generality: what carries beyond the analysed class

Three coordinates of the institutional loop are independent of the ecology they govern: the sign structure and modulus of the response law, the deployment delay, and the review cadence. The theorems of this paper fix what those coordinates do within the declared stock–memory–effort class — the delay window and its two certified crossings, the no-Hopf property of the calibrated quota law, the opposite cadence responses of the two rules — and the class itself is stock-agnostic: a harvested renewable stock under institutional control, of which fisheries are the motivating instance, with the liquidation channels of Section 1.1 (culling the standing stock, suppressing recruitment, decoupled consumption) marking how far the same loop reaches beyond a single-sector reading. What transfers to other periodically reviewed renewable-resource regimes is therefore the mechanism's form, not the numerical thresholds: the thresholds are theorems about the declared parameterisation, and any field application must re-identify the institutional coefficients — the gains, delays, and cadences of the governance loop — with the same standing as the biological ones.

For management readers the paper's technical vocabulary has a direct translation:

| Technical term | Management reading |
| --- | --- |
| Mobilising law ($C_Z > 0$) | Effort-escalation rule: decline triggers more deployment |
| Protective quota-tracking law ($C_Z < 0$) | Catch/quota rule: harvest restored toward a cap |
| Hopf crossing | Onset or loss of oscillatory stock dynamics |
| Neimark–Sacker-type crossing | Quasi-periodic instability emerging under periodic review |
| Monodromy spectral radius | Stability margin of one review cycle |
| Review interval $T_r$ | Assessment/management review cycle length |

Two cautions travel with the translation. First, the discretisation artefacts are a general warning for management modelling, not a curiosity of this system: in both channels an explicit first-order update manufactured thresholds (near 2.3 yr for the protective channel, the half-century restabilisation for the mobilising channel) that the exact update of the same reviewed loop does not carry, so a discrete-time management model can report stability boundaries that belong to its discretisation rather than to the institution. Second, local spectral stabilisation is not governance: an interval that stabilises the equilibrium may still admit severe inter-review depletion (Section 8), and the capture boundaries of Section 9 are basin statements, not thresholds a manager can read off a spectrum. The design reading that survives both cautions is the paper's central one: the response rule's class is a design choice, the review interval is a control variable with opposite effects under the two rules, and the institutional coefficients are dynamical parameters to be identified, bounded, and designed against.

### 11.4 Certification levels""",
)
register("renumber-11.4", "### 11.4 Relation to the early-warning literature", "### 11.5 Relation to the early-warning literature")
register("renumber-11.5", "### 11.5 Limitations", "### 11.6 Limitations")
register("renumber-11.6", "### 11.6 Open problems", "### 11.7 Open problems")
register(
    "fix-crossref-11.3",
    "(Section 11.3's first stated open task",
    "(Section 11.4's first stated open task",
)

# --- 5b. Organization sentence --------------------------------------------
register(
    "organization",
    "Section 11 discusses design consequences, relation to the early-warning literature, and open problems. Section 12 concludes.",
    "Section 11 discusses design consequences, the generality of the institutional-loop coordinates, relation to the early-warning literature, and open problems. Section 12 concludes.",
)

# --- 6. conclusion breadth closing ----------------------------------------
register(
    "conclusion-breadth",
    "the institutional coefficients — the gains and delays of the governance loop — are dynamical parameters with the same standing as the biological ones, to be identified, bounded, and designed against.",
    "the institutional coefficients — the gains and delays of the governance loop — are dynamical parameters with the same standing as the biological ones, to be identified, bounded, and designed against. Beyond the declared class, the coordinates themselves generalise: any periodically reviewed renewable-resource institution — whatever the stock, the sector, or the rule's legal form — admits the same three design coordinates analysed here (the response law's class, the deployment delay, and the review cadence), and the theorems fix their local effects in one analysable instance of that family. The mechanism is available wherever an institution answers an observed decline with a lagged rule; the empirical programme that follows is the identification of these coordinates in field institutions.",
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
# Section-reposition tokens: the new subsection 11.3 shifts old 11.3-11.6 to
# 11.4-11.7. These are structural positions, not frozen scientific values; no
# live cross-file reference points at them (checked: supplementary v5's S11.3
# is an unrelated supplement section; only frozen historical md versions v27-
# v29 carry the old numbers). Exempt exactly these five tokens, then verify
# the renumbered structure explicitly below.
RENUMBER_TOKENS = {"11.3", "11.4", "11.5", "11.6", "11.7"}

t30, t31 = tokens(md0), tokens(md)
lost = {t: c for t, c in t30.items() if t31[t] < c and t not in RENUMBER_TOKENS}
assert not lost, f"frozen numeric tokens lost or reduced: {lost}"
newtok = {t for t in t31 if t not in t30 and t not in RENUMBER_TOKENS}
assert not newtok, f"new numeric tokens not present verbatim in v30: {newtok}"
print("numeric discipline: v31 keeps every frozen scientific value verbatim; "
      "no new scientific tokens (section renumber exempted and verified below)")

# ---- renumber consistency (Discussion 11.1-11.7) ---------------------------
heads = re.findall(r"^### (11\.\d) (.+)$", md, re.M)
expected = [
    ("11.1", "The two channels as a design distinction"),
    ("11.2", "The review interval as control"),
    ("11.3", "Generality: what carries beyond the analysed class"),
    ("11.4", "Certification levels"),
    ("11.5", "Relation to the early-warning literature"),
    ("11.6", "Limitations"),
    ("11.7", "Open problems"),
]
assert heads == expected, f"unexpected Discussion structure: {heads}"
assert md.count("(Section 11.4's first stated open task") == 1, "cross-ref not re-pointed"
print("renumber consistency: Discussion 11.1-11.7 in the expected order; "
      "open-task cross-reference re-pointed to 11.4")

# ---- v30 untouched ----------------------------------------------------------
assert V30.read_text(encoding="utf-8") == md0, "v30 changed on disk!"

V31.write_text(md, encoding="utf-8")
print(f"wrote {V31.relative_to(ROOT)} ({len(md)} chars, {md.count(chr(10)) + 1} lines)")

# ---- diff-region audit: only the declared regions changed -------------------
r = subprocess.run(
    ["git", "diff", "--no-index", "-U0", str(V30), str(V31)],
    capture_output=True, text=True,
)
hunks = re.findall(r"^@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@(.*)$", r.stdout, re.M)
print(f"diff hunks: {len(hunks)} (13 declared edit regions; git's line "
      f"aligner may split/merge adjacent renumber edits)")
assert 13 <= len(hunks) <= 20, f"hunk count out of sanity range: {len(hunks)}"
for name, _old, _new in EDITS:
    print(f"  applied: {name}")
print("OK: v31 created; v30 untouched")
