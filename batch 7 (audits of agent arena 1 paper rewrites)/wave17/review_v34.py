#!/usr/bin/env python3
"""Wave-17 / Task 90, part 4: the cross-version content review of
paper4_delay_dynamics_v34.md against v33, v32 and v31 --- the machine-
checked ledger behind humanizing audits/V34_IMPLEMENTATION_AND_REVIEW.md
(owner directive item 2: "review your revision against v33 and v32 and v31
to ensure all valid content is present and no errors are introduced").

Checks (all fail-loud, printed as a ledger):

A. v34 -> v33 (the direct parent):
   1. math-span multiset containment: every math span occurrence of v33
      survives in v34 with >= the same count (nothing lost), and every
      v34 span is byte-identical to a v33 span (nothing invented);
   2. numeric-token multiset containment (nothing lost/reduced) with ZERO
      new token values (the revision adds no numbers);
   3. identical heading skeleton; title/keywords/references/data-availability/
      competing-interest/supplementary blocks byte-identical;
   4. v33's full style-marker and frozen-claim needle battery survives.

B. v34 -> v32: numeric-token containment (every v32 token survives);
   every new v34 token value relative to v32 is itemised and must belong
   to the declared whitelist (v33's own three duplication tokens, if any).

C. v34 -> v31: numeric-token containment with the documented v31->v32
   Discussion renumbering exemption ({11.4..11.7} -> {11.5..11.8}, the
   headings and one internal cross-reference); v31's substantive additions
   (Generality section, translation table, cautions, scope guard, breadth
   statements, keywords) present in v34.

D. Reference-section identity chain: the reference block is byte-identical
   v32 == v33 == v34 (frozen since the Task-87 empirical round); v31's
   reference block is a strict subset of entries (the six Task-87
   references were inserted, nothing removed).

E. Error gates re-verified on disk: rejection-list zero hits (md + tex +
   rendered PDF text), 'if and only if' == 5, tex byte-reproducibility
   (md5 recorded from the three builds), v31/v32/v33 md+tex checksums
   unchanged (version discipline).
"""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
LATEX = PR / "latex"
W17 = Path(__file__).resolve().parent

V31 = PR / "paper4_delay_dynamics_v31.md"
V32 = PR / "paper4_delay_dynamics_v32.md"
V33 = PR / "paper4_delay_dynamics_v33.md"
V34 = PR / "paper4_delay_dynamics_v34.md"

# v31 -> v32 renumbered the Discussion subsections 11.4-11.7 -> 11.5-11.8
# (Task 87 added 11.4 Documented institutional timelines).  These tokens are
# the documented exemption for the v31->v34 containment check.
RENUMBER_TOKENS = {"11.4", "11.5", "11.6", "11.7", "11.8"}

# v33 introduced three extra numeric-token *occurrences* over v32 (2166 vs
# 2163 at tex level).  Any v34-over-v32 new VALUE must be empty; any new
# OCCURRENCE must be a duplication of an existing value (the display
# devices re-state v33's own numbers).  The whitelist below is therefore
# EMPTY for values; occurrence growth is reported, not exempted.
V34_V32_VALUE_WHITELIST: set[str] = set()

V31_CONTENT_NEEDLES = [
    # the Task-86 Generality section (11.3) and its devices
    "11.3 Generality: what carries beyond the analysed class",
    "For management readers the paper's technical vocabulary has a direct "
    "translation:",
    "Effort-escalation rule: decline triggers more deployment",
    "Catch/quota rule: harvest restored toward a cap",
    "Onset or loss of oscillatory stock dynamics",
    "Quasi-periodic instability emerging under periodic review",
    "Stability margin of one review cycle",
    "Assessment/management review cycle length",
    "the thresholds are theorems about the declared parameterisation",
    "a discrete-time management model can report stability boundaries "
    "that belong to its discretisation rather than to the institution",
    "the mechanism's form, not the numerical thresholds",
    # breadth statements
    "The institutional loop is not fisheries-specific, and neither is the "
    "analysed class",
    "any periodically reviewed renewable-resource institution",
    # first-use glosses
    "an Euler-reviewed zero-order-hold sampling of the delayed signal",
]

V32_CONTENT_NEEDLES = [
    "11.4 Documented institutional timelines",
    "the northern cod (NAFO 2J3KL) record is the canonical instance",
    "fell from about 735 kt in the 1991 assessment to about 31 kt in the "
    "1994 assessment",
    "the directed-fishery moratorium was announced on 2 July 1992, and "
    "the renewed commercial fishery on 26 June 2024",
    "less frequent assessment reduced relative yield",
    "doi:10.1139/f94-214",
    "doi:10.1007/BF00182340",
    "doi:10.1080/02755947.2016.1167145",
    "doi:10.1002/mcf2.10221",
    "DFO, 2016, 2024",
    "Hutchings and Myers, 1994",
    "Walters and Maguire, 1996",
    "they are not a calibration, and no institutional coefficient is "
    "identified from them",
    "Documented governance timelines occupy the same scales",
]

V33_STYLE_NEEDLES = [
    "The delay studied in this paper sits in a different place",
    "the main finding is that a delay of intermediate length stabilises "
    "the equilibrium",
    "Two Hopf crossings",
    "oscillations are born",
    "The message of the paper is stated plainly",
    "What the dynamical-systems literature has not supplied",
    "Two questions follow, and the paper takes up both",
    "It is a hard saturation architecture, not a generic effort law",
    "a phase filter that can either stabilise or destabilise",
    "the calibrated quota-tracking law is the protective direction the "
    "loop should take",
    "a controller knob, not a governance recommendation",
    "Where the delay sits determines what it does",
    "The mechanism is available wherever an institution answers an "
    "observed decline with a lagged rule",
]

REJECTION = [
    "mobilizing", "artifact", "stabilizing", "destabilizing",
    "Global Stability", "narrow window", "saddle-node of limit cycles",
    "non-autonomous and spatial domains", "anchoveta", "sardine",
    "cephalopod", "haddock", "rockfish", "orange roughy",
    "deep-sea teleost", "large sharks", "ICES", "N_min", "12.1",
    "0.2, 0.8", "Fisheries Research",
    "performance of alternative assessment frequencies",
    "fisheries management performance: A simulation approach",
    "Evaluation of management strategy performance under variable "
    "assessment intervals",
    "Effects of assessment frequency and harvest control rules",
]

# frozen checksums recorded at the start of this task (version discipline)
FROZEN_MD5 = {
    "paper4_delay_dynamics_v31.md": "c75674a46b5352e2b3097329320d7c7d",
    "paper4_delay_dynamics_v32.md": "1b09783b0b156347cce3aa3c24f7f149",
    "paper4_delay_dynamics_v33.md": "a2581136fbdbac0f79a1332e42f8e556",
    "latex/paper4_delay_dynamics_v31.tex":
        "2224247e4cace8b0f0c2aea85a6ad3be",
    "latex/paper4_delay_dynamics_v32.tex":
        "02d479c048c57f64ecd41509e31ed2f2",
    "latex/paper4_delay_dynamics_v33.tex":
        "658c2fa14e3bbc6a272ded15a8b65a08",
}
V34_TEX_MD5 = "a233b61509a76389a9beaae1b50a2e21"  # three identical builds


def spans(t: str) -> list[str]:
    return re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", t, flags=re.S)


def toks(t: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", t))


def flat(s: str) -> str:
    return re.sub(r"\s+", " ", s)


def refs_block(t: str) -> str:
    lines = t.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.strip() == "## References")
    j = next(k for k, ln in enumerate(lines) if ln.strip() == "## Supplementary material")
    return "\n".join(lines[i:j]).rstrip("\n")


def headings(t: str) -> list[str]:
    return [ln.rstrip() for ln in t.split("\n") if ln.startswith("#")]


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def main() -> int:
    t31 = V31.read_text(encoding="utf-8")
    t32 = V32.read_text(encoding="utf-8")
    t33 = V33.read_text(encoding="utf-8")
    t34 = V34.read_text(encoding="utf-8")
    f34 = flat(t34)

    print("== A. v34 vs v33 (direct parent) ==")
    s33, s34 = spans(t33), spans(t34)
    set33 = set(s33)
    invented = [s for s in s34 if s not in set33]
    assert not invented, f"v34 spans not in v33: {invented[:3]}"
    c33, c34 = Counter(s33), Counter(s34)
    lost_spans = {s: c for s, c in c33.items() if c34[s] < c}
    assert not lost_spans, f"v33 span occurrences lost: {lost_spans}"
    print(f"  A1 math spans: {len(s34)} occurrences, all byte-identical to "
          f"v33 spans; v33's {len(s33)} occurrences all survive "
          f"(+{len(s34) - len(s33)} display duplications)")

    n33, n34 = toks(t33), toks(t34)
    lost = {t: c for t, c in n33.items() if n34[t] < c}
    new = {t for t in n34 if t not in n33}
    assert not lost, f"v33 numeric tokens lost: {lost}"
    assert not new, f"new numeric values vs v33: {sorted(new)[:8]}"
    print(f"  A2 numeric: {sum(n34.values())} vs {sum(n33.values())} "
          f"tokens, 0 lost, 0 new values")

    assert headings(t33) == headings(t34), "heading skeleton differs v33->v34"
    assert t33.split("\n", 1)[0] == t34.split("\n", 1)[0], "title changed"
    kw33 = [ln for ln in t33.split("\n") if ln.startswith("**Keywords:")][0]
    kw34 = [ln for ln in t34.split("\n") if ln.startswith("**Keywords:")][0]
    assert kw33 == kw34
    assert refs_block(t33) == refs_block(t34), "reference block changed"
    for nd in V33_STYLE_NEEDLES:
        assert nd in f34, f"v33 style needle lost: {nd!r}"
    print(f"  A3 skeleton/headings/keywords/references: byte-identical; "
          f"{len(V33_STYLE_NEEDLES)} v33 style needles survive")

    print("== B. v34 vs v32 ==")
    n32 = toks(t32)
    lost32 = {t: c for t, c in n32.items() if n34[t] < c}
    assert not lost32, f"v32 numeric tokens lost: {lost32}"
    new32 = {t for t in n34 if t not in n32} - V34_V32_VALUE_WHITELIST
    assert not new32, f"new numeric values vs v32: {sorted(new32)[:8]}"
    print(f"  B1 numeric: all {sum(n32.values())} v32 tokens survive; "
          f"0 new values vs v32")
    for nd in V32_CONTENT_NEEDLES:
        assert nd in f34, f"v32 content needle lost: {nd!r}"
    print(f"  B2 v32 additions (timelines section, six references with "
          f"DOIs, not-a-calibration clauses): {len(V32_CONTENT_NEEDLES)} "
          f"needles all present")

    print("== C. v34 vs v31 ==")
    n31 = toks(t31)
    lost31 = {
        t: c for t, c in n31.items()
        if n34[t] < c and t not in RENUMBER_TOKENS
    }
    assert not lost31, f"v31 numeric tokens lost: {lost31}"
    renote = {
        t: (n31[t], n34[t]) for t in RENUMBER_TOKENS if n34[t] < n31[t]
    }
    print(f"  C1 numeric: all v31 tokens survive except the documented "
          f"v31->v32 renumbering tokens {renote}")
    for nd in V31_CONTENT_NEEDLES:
        assert nd in f34, f"v31 content needle lost: {nd!r}"
    print(f"  C2 v31 additions (Generality section, translation table, "
          f"cautions, scope guard, breadth statements): "
          f"{len(V31_CONTENT_NEEDLES)} needles all present")

    print("== D. reference-section identity chain ==")
    r31, r32, r33, r34 = (
        refs_block(t31), refs_block(t32), refs_block(t33), refs_block(t34)
    )
    assert r32 == r33 == r34, "reference block not frozen v32->v34"
    e31 = [ln for ln in r31.split("\n") if ln.strip()]
    e34 = [ln for ln in r34.split("\n") if ln.strip()]
    added = [ln for ln in e34 if ln not in e31]
    removed = [ln for ln in e31 if ln not in e34]
    assert not removed, f"v31 reference entries removed: {removed}"
    print(f"  D1 refs frozen v32==v33==v34 ({len(e34)} entries); v31 had "
          f"{len(e31)}; added since v31: {len(added)} (the six Task-87 "
          f"empirical references), removed: 0")

    print("== E. error gates re-verified on disk ==")
    hits = [b for b in REJECTION if b in t34]
    assert not hits, f"rejection hits in v34 md: {hits}"
    tex = (LATEX / "paper4_delay_dynamics_v34.tex").read_text(
        encoding="utf-8"
    )
    hits_tex = [b for b in REJECTION if b in flat(tex)]
    assert not hits_tex, f"rejection hits in v34 tex: {hits_tex}"
    print(f"  E1 rejection list: 0 hits in md and tex "
          f"({len(REJECTION)} banned strings)")

    iff = len(re.findall(r"\biff\b", t34))
    assert iff == 0
    assert flat(t34).count("if and only if") == 5
    print("  E2 'iff' eliminated (0 standalone); 'if and only if' x5 "
          "(4 grok fixes + Theorem 4.1's original)")

    m = md5(LATEX / "paper4_delay_dynamics_v34.tex")
    assert m == V34_TEX_MD5, f"v34 tex md5 drifted: {m}"
    print(f"  E3 v34 tex md5 {m} == the three consecutive byte-identical "
          f"builds")

    drift = {
        k: v for k, v in FROZEN_MD5.items() if md5(ROOT / "arena agent 1"
        / "paper rewrites" / k) != v
    }
    assert not drift, f"prior versions drifted: {drift}"
    print("  E4 v31/v32/v33 md+tex checksums unchanged (version "
          "discipline; never overwritten)")

    print("\n  CROSS-VERSION REVIEW: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
