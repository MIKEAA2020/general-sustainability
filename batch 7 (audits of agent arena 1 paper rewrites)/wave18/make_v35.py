#!/usr/bin/env python3
"""Wave-18 / Task 91, part 1: author paper4_delay_dynamics_v35.md from
paper4_delay_dynamics_v34.md.

Owner directive (this round, three items):
1. "abstract should stay below 260 words" --- the v34 abstract runs 560
   journal words; v35 replaces it with a 258-word abstract that keeps every
   load-bearing claim, all six numeric tokens (3.7, 150, 2.3, 6.5, 1992,
   2024), both rule definitions, the certification honesty caveats, the
   stock-agnostic breadth statement, the cod timelines with the
   not-a-calibration clause, and the design message.
2. "'it has a plain name' is meta-commentary without scientific,
   pedagogical or expository substance. maintain brevity without
   sacrificing substance." --- the meta-commentary is removed with the
   abstract rewrite (the concept NAME and its definition stay; the
   announcement sentence goes).  The same principle removes two further
   announcement sentences: v33's "The message of the paper is stated
   plainly." (pure meta) and v34's "The regime record is collected in one
   display:" (the table is self-describing).
3. "does the work merit additional genuine, non-decorative,
   non-superficial ecological insights?" --- evaluation verdict: YES, but
   only as a consolidation of the paper's own already-registered records.
   Implemented as the new Discussion subsection 11.7 "The ecological
   reading" (four findings assembled solely from registered sentences:
   the doubly-selected exposed life histories; the two delays' different
   compartments and different cycles; the extraction-form ecology the
   local mathematics cannot see; the growth-coupled-pool scaling limit),
   with the Discussion renumbered 11.7 Limitations -> 11.8 and 11.8 Open
   problems -> 11.9 (zero live cross-references to the old numbers ---
   verified before the edit).  No new computation, archetype, or
   calibration is added; every math span in the subsection is reused
   byte-identically from v34.

FROZEN (byte-identical to v34, machine-checked): every theorem, proof,
number, interval, table row, hypothesis label, reference entry,
declaration, the figure block, and --- outside the three edited regions
--- all prose.

This script is fully reproducible from the repository alone: it applies
five surgical edits (abstract splice; regime-table signpost removal;
Organization sentence insertion; the 11.8/11.9 renumber; the new
subsection insertion), then runs the md-level fail-loud battery.  v34 is
never modified (version discipline).  Re-running is idempotent.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
V34 = PR / "paper4_delay_dynamics_v34.md"
V35 = PR / "paper4_delay_dynamics_v35.md"

MAX_ABSTRACT_WORDS = 259  # "below 260 words"

NEW_ABSTRACT = """Delays destabilise renewable-resource systems; those studied so far are ecological. This paper analyses the delay that sits elsewhere — **governance delay**, the lag from observed decline to institutional response. A three-state model — harvested stock, filtered deficit memory, bounded effort — compares two rules: the **mobilising rule**, effort grows as more effort is deployed; and the **protective rule**, a quota-tracking law restoring harvest toward a cap.

For the mobilising rule, intermediate delay stabilises the equilibrium: two subcritical Hopf crossings, interval-certified near 3.7 and 150 yr, bound the delay window in which the lag itself stabilises the loop. For the protective rule the loop gain stays below one at the calibrated point: the equilibrium is exponentially stable at every delay — a no-Hopf theorem. Under periodic review the two rules respond oppositely: annual protective review remains stable — its apparent 2.3-yr threshold is a discretisation artefact — while annual mobilising review is unstable, restabilising only above 6.5 yr through a Neimark–Sacker-type crossing. The attractor topology is five-regime: two folds certified at the discrete collocation level (continuum stages open), and a basin-boundary transition toward an unverified large-amplitude attractor.

The class is stock-agnostic: its design coordinates — rule sign, deployment delay, review cadence — carry to any periodically reviewed renewable-resource regime. Documented timelines occupy the same scales — northern cod ran from annual assessment with incremental response to the 1992 moratorium, then the 2024 reopening — grounding scales, not coefficients. Institutional form and timing, not ecological lag, decide whether governance stabilises or destabilises the stock; more frequent assessment is not always safer — the review interval is a local spectral design parameter."""

NEW_SUBSECTION = """### 11.7 The ecological reading

(i) **The exposed life histories are doubly selected.** With the maturation delay switched on, the two-crossing structure survives only on the product locus $r\\,g \\approx 1.5$–$1.6$ (Section 7.3): longer maturation delays move the band to slower stocks, down to $g=10$ near $r\\approx0.08$. Selection acts a second time through the institutional delay. The band $\\tau$-windows grow with the maturation lag — $g=1$: $(1.6,3.5)$ yr; $g=2$: $(2.6,7.8)$ yr; $g=5$: $(9.9,20.3)$ yr — and the $g=2$ window is the one that lies inside the documented $2$–$13$ yr governance-lag distribution. Fast-maturing small pelagics are therefore the predicted exposed class, not an illustrative example. At the slow end the question inverts: with recruitment lagged, the slow-$r$ system carries a $358.8$-yr cohort cycle, so the institutional-delay question becomes moot there (Section 7.4).

(ii) **Ecological delay and institutional delay sit in different compartments and produce different cycles.** The maturation delay enters the stock equation and the deficit signal; the institutional delay enters only the effort equation (Section 7.1). Their cycles differ accordingly: cohort cycles whose periods track the life history ($\\sim 20$ yr at $r = 0.5$, $g = 5$; $358.8$ yr at $r = 0.02$, $g = 5$) versus loop cycles whose period tracks the deployed response ($16.96$ yr at $r = 0.3$, $g = 5$, $\\tau = 10$). With both delays present the institutional window survives on top of the ecological one — $\\tau \\approx 10$ carries the $\\sim 17$-yr cycle; $\\tau \\approx 21$ is stable — the stage analogue of the fundamental window of Section 5.1 (Section 7.4).

(iii) **The form of extraction is ecological even where the local mathematics is not.** The two harvest channels of M3-LC — removing standing stock versus suppressing recruitment — leave the equilibrium, the Jacobian, the characteristic equation, and both Hopf points identical (Section 2.3). The collapse dynamics still separate them: at $\\tau = 115$ yr, $\\kappa = 0.5$, long-lived transients reach minimum $N \\approx 33$ under pure stock culling and $N \\approx 10$ under pure recruitment suppression; under fixed demand, culling first hits $N = 0$ near time $158$ while suppression approaches zero asymptotically, reaching $N < 1$ near time $430$ (Section 9.3). Local spectra cannot see the extraction form; the excursion record can.

(iv) **Growth-coupled ecology cannot widen the window.** The Droop nutrient–quota variant leaves the $r$-window unchanged — upper edge $\\le 0.023$ yr$^{-1}$ at $\\eta = 0.914$, and no Hopf crossing at any $r \\ge 0.2$ yr$^{-1}$ — because a growth-coupled pool self-relaxes at exactly $r$ and cannot supply the slow companion variable (Section 9.3). The only $r$-independent slow pool in the registered family is the working core's $\\omega_A$-type exchange: decoupled storage, not growth-coupled ecology, is what can slow the loop.

Each reading consolidates records registered in Sections 2.3, 7, and 9.3; none adds a computation, an archetype, or a calibration, and the limitations of Section 11.8 apply to all four unchanged.
"""

# Discussion renumbering: the new 11.7 inserts before Limitations; the two
# later headings shift.  "11.9" is the only NEW numeric token value (11.7 and
# 11.8 stay count-neutral: one heading each before and after).
RENUMBER_TOKENS = {"11.9"}

# device/content needles at md level (each must appear in v35)
DEVICE_NEEDLES = [
    # abstract sentinels (the compressed abstract)
    "**governance delay**",
    "the lag from observed decline to institutional response",
    "the **mobilising rule**",
    "the **protective rule**",
    "intermediate delay stabilises the equilibrium",
    "two subcritical Hopf crossings",
    "a no-Hopf theorem",
    "its apparent 2.3-yr threshold is a discretisation artefact",
    "restabilising only above 6.5 yr through a Neimark–Sacker-type crossing",
    "The attractor topology is five-regime",
    "(continuum stages open)",
    "an unverified large-amplitude attractor",
    "carry to any periodically reviewed renewable-resource regime",
    "northern cod ran from annual assessment with incremental response",
    "grounding scales, not coefficients",
    "more frequent assessment is not always safer",
    "a local spectral design parameter",
    # v34 devices that survive
    "**review cadence**",
    "The classic results all place the delay inside the ecology itself",
    "Three structural features of (1) carry everything that follows",
    "Its behavioural reading is direct",
    "**What Theorem 8.1 says.**",
    "**What Proposition 8.1 says.**",
    "> **Governance warning.**",
    "> **Management caution.**",
    "| Regime | Delay range | Attractor record |",
    "- **The mobilising law ($C_Z > 0$)**",
    "| Sample-and-hold review |",
    "| Subcritical Hopf crossing |",
    "| Inter-assessment stability margin |",
    "1. **Proved theorems.**",
    "2. **Interval certificates.**",
    "3. **Declared-status numerical results.**",
    "if and only if",
    # the new ecological reading
    "### 11.7 The ecological reading",
    "The exposed life histories are doubly selected",
    "sit in different compartments and produce different cycles",
    "The form of extraction is ecological even where the local mathematics is not",
    "Growth-coupled ecology cannot widen the window",
    "decoupled storage, not growth-coupled ecology, is what can slow the loop",
    "the predicted exposed class, not an illustrative example",
    "the institutional-delay question becomes moot there",
    "the ecological reading of the registered records",
    "### 11.8 Limitations",
    "### 11.9 Open problems",
]

# caveat-presence needles (dropped-caveat regression gates)
CAVEAT_NEEDLES = [
    "A mesh-range caveat is registered with the fine map",
    "they are not a calibration, and no institutional coefficient is "
    "identified from them",
    "other discretisations have different monodromies, and the "
    "continuous-delay and periodic-review recommendations are not "
    "interchangeable",
    "(H5) non-feedback mass compartments stay outside the delay loop",
    "The saddle-node-of-periodic-orbits classification remains",
    "The reversed-gain linearisation has loop gain",
    "The stable arm is not generically reachable near the fold",
]

# rejection list: the Task-89/90 fabrications + this round's bans (the
# meta-commentary and the removed announcement sentences)
BANNED = [
    "performance of alternative assessment frequencies",
    "fisheries management performance: A simulation approach",
    "Evaluation of management strategy performance under variable "
    "assessment intervals",
    "Effects of assessment frequency and harvest control rules",
    "ICES", "Fisheries Research",
    "183, 313", "313–323", "175, 94", "94–105", "42(4),", "843–861",
    "anchoveta", "sardine", "cephalopod", "haddock", "rockfish",
    "orange roughy", "deep-sea teleost", "large sharks",
    "12.1", "4.5, 12.1", "[4.5,", "0.2, 0.8", "[0.2, 0.8]",
    "N_min",
    "Global Stability", "narrow window", "saddle-node of limit cycles",
    "non-autonomous and spatial domains", "pure mobilizing governance",
    "mobilizing", "artifact", "stabilizing", "destabilizing",
    # this round's bans
    "plain name",
    "The message of the paper is stated plainly",
    "is collected in one display",
]

ABSTRACT_DIGIT_TOKENS = ["3.7", "150", "2.3", "6.5", "1992", "2024"]


def tokens(s: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", s))


def journal_words(s: str) -> int:
    return sum(1 for w in re.findall(r"\S+", s) if re.search(r"[A-Za-z0-9]", w))


def block_by_heading(t: str, start: str, end: str | None = None) -> str:
    lines = t.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.strip() == start)
    if end is None:
        return "\n".join(lines[i:]).rstrip("\n")
    j = next(k for k, ln in enumerate(lines) if ln.strip() == end)
    return "\n".join(lines[i:j]).rstrip("\n")


def main() -> int:
    t34 = V34.read_text(encoding="utf-8")
    text = t34

    # --- edit 1: the abstract splice ------------------------------------
    pre, rest = text.split("## Abstract\n\n", 1)
    old_abstract, post = rest.split("\n\n**Keywords:**", 1)
    assert "It has a plain name" in old_abstract, "unexpected v34 abstract"
    assert "Two response rules are compared throughout:" in old_abstract
    assert journal_words(old_abstract) > MAX_ABSTRACT_WORDS, (
        "v34 abstract was already within the cap?"
    )
    text = pre + "## Abstract\n\n" + NEW_ABSTRACT + "\n\n**Keywords:**" + post

    # --- edit 2: regime-table signpost removal ---------------------------
    signpost = "The regime record is collected in one display:\n\n"
    assert text.count(signpost) == 1, "signpost anchor not unique"
    text = text.replace(signpost, "")

    # --- edit 3: Organization sentence insertion -------------------------
    org_old = (
        "the documented institutional timelines that ground the two timing "
        "coordinates, the relation to the early-warning literature, and "
        "open problems."
    )
    org_new = (
        "the documented institutional timelines that ground the two timing "
        "coordinates, the ecological reading of the registered records, the "
        "relation to the early-warning literature, and open problems."
    )
    assert text.count(org_old) == 1, "Organization anchor not unique"
    text = text.replace(org_old, org_new)

    # --- edit 4: renumber Open problems 11.8 -> 11.9 (before inserting) --
    assert text.count("### 11.8 Open problems") == 1
    text = text.replace("### 11.8 Open problems", "### 11.9 Open problems")

    # --- edit 5: insert the ecological reading as the new 11.7 -----------
    assert text.count("### 11.7 Limitations") == 1
    text = text.replace(
        "### 11.7 Limitations",
        NEW_SUBSECTION.rstrip("\n") + "\n\n### 11.8 Limitations",
    )

    # --- fail-loud battery ------------------------------------------------
    # 1. abstract word cap and digit-token preservation
    aw = journal_words(NEW_ABSTRACT)
    assert aw <= MAX_ABSTRACT_WORDS, f"abstract runs {aw} words"
    for tok in ABSTRACT_DIGIT_TOKENS:
        assert tok in NEW_ABSTRACT, f"abstract digit token lost: {tok}"

    # 2. meta-commentary and announcement sentences gone
    for banned in ("plain name", "The message of the paper is stated plainly",
                   "is collected in one display"):
        assert banned not in text, f"banned phrase present: {banned!r}"

    # 3. math spans: every v35 span byte-identical to a v34 span (empty
    #    whitelist) and no v34 span occurrence lost
    s34 = re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", t34, flags=re.S)
    s35 = re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", text, flags=re.S)
    missing = [s for s in s35 if s not in t34]
    assert not missing, f"v35 spans not in v34: {missing[:5]}"
    c34, c35 = Counter(s34), Counter(s35)
    lost_spans = {s: c for s, c in c34.items() if c35[s] < c}
    assert not lost_spans, f"v34 span occurrences lost: {lost_spans}"

    # 4. numeric discipline: superset of v34, no new values except 11.9
    n34, n35 = tokens(t34), tokens(text)
    lost = {t: c for t, c in n34.items() if n35[t] < c and t not in RENUMBER_TOKENS}
    assert not lost, f"v34 numeric tokens lost: {lost}"
    new = {t for t in n35 if t not in n34} - RENUMBER_TOKENS
    assert not new, f"new numeric values in v35: {sorted(new)[:10]}"

    # 5. heading skeleton: v34's headings with the two renumbers and the
    #    one insertion
    h34 = [ln.rstrip() for ln in t34.split("\n") if ln.startswith("#")]
    h35 = [ln.rstrip() for ln in text.split("\n") if ln.startswith("#")]
    exp = []
    for h in h34:
        if h == "### 11.7 Limitations":
            exp.append("### 11.7 The ecological reading")
            exp.append("### 11.8 Limitations")
        elif h == "### 11.8 Open problems":
            exp.append("### 11.9 Open problems")
        else:
            exp.append(h)
    assert h35 == exp, "heading skeleton differs from the expected transform"

    # 6. frozen blocks byte-identical
    assert text.split("\n", 1)[0] == t34.split("\n", 1)[0], "title changed"
    kw34 = [ln for ln in t34.split("\n") if ln.startswith("**Keywords:")][0]
    kw35 = [ln for ln in text.split("\n") if ln.startswith("**Keywords:")][0]
    assert kw34 == kw35, "keywords line changed"
    for start, end in (
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
        ("## References", "## Supplementary material"),
    ):
        b34 = block_by_heading(t34, start, end)
        b35 = block_by_heading(text, start, end)
        assert b34 == b35, f"frozen block changed: {start}"
    assert block_by_heading(t34, "## Supplementary material") == block_by_heading(
        text, "## Supplementary material"
    ), "supplementary block changed"
    fig34 = [ln for ln in t34.split("\n") if ln.startswith("![Figure")][0]
    cap34 = [ln for ln in t34.split("\n") if ln.startswith("**Figure 1.**")][0]
    assert text.count(fig34) == 1 and text.count(cap34) == 1, "figure block changed"

    # 7. device and caveat needles
    flat = re.sub(r"\s+", " ", text)
    for nd in DEVICE_NEEDLES + CAVEAT_NEEDLES:
        assert nd in flat, f"needle missing: {nd!r}"

    # 8. rejection scanner
    hits = [b for b in BANNED if b in text]
    assert not hits, f"rejection-list hits in v35 md: {hits}"

    # 9. 'if and only if' count unchanged
    assert flat.count("if and only if") == 5

    # idempotence + version discipline
    if V35.exists():
        assert V35.read_text(encoding="utf-8") == text, "non-idempotent rebuild"
    V35.write_text(text, encoding="utf-8")
    assert V34.read_text(encoding="utf-8") == t34, "v34 was modified"

    print(
        f"  paper4_delay_dynamics_v35.md: OK  {len(text)} chars "
        f"({len(text.splitlines())} lines); abstract {aw} journal words "
        f"(cap {MAX_ABSTRACT_WORDS}); {len(s35)} math spans (all "
        f"byte-identical to v34, 0 whitelisted; all {len(s34)} v34 "
        f"occurrences survive); numeric superset "
        f"({sum(n35.values())} vs {sum(n34.values())} tokens, only new "
        f"value: 11.9); v34 untouched"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
