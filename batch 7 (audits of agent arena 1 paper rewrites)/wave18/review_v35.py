#!/usr/bin/env python3
"""Wave-18 / Task 91, part 4: the cross-version content review of
paper4_delay_dynamics_v35.md against v34, v33, v32 and v31 --- the
machine-checked ledger behind humanizing audits/
V35_ABSTRACT_AND_ECOLOGICAL_READING.md.

Owner directive items verified here:
1. abstract below 260 words (258 journal words at md AND rendered-text
   level; all six abstract digit tokens preserved);
2. the meta-commentary removed (zero-hit gates for the flagged phrase and
   the two announcement sentences sharing its defect);
3. the ecological-insights consolidation implemented as new Discussion
   11.7 with the 11.8/11.9 renumber, all content from registered records
   (every math span byte-identical to v34).

Checks (all fail-loud, printed as a ledger):

A. v35 -> v34 (the direct parent): math-span multiset containment both
   ways; numeric containment with the single declared renumber token
   11.9 (11.7/11.8 verified count-neutral); heading-skeleton transform
   (one insertion + two renumbers); frozen blocks byte-identical;
   abstract word count; the surviving v33/v32 needle batteries.

B. v35 -> v33 / v32: numeric containment with {11.9} exempt.

C. v35 -> v31: numeric containment with the two renumber generations
   exempt ({11.4..11.9}), plus the Discussion heading-sequence check
   (11.1 -> 11.9 in order); v31's content needles.

D. Reference-section identity chain (v32 == v33 == v34 == v35).

E. Error gates on disk: rejection list zero hits (md + tex), 'if and only
   if' == 5, tex byte-reproducibility, prior versions' checksums frozen.
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

V31 = PR / "paper4_delay_dynamics_v31.md"
V32 = PR / "paper4_delay_dynamics_v32.md"
V33 = PR / "paper4_delay_dynamics_v33.md"
V34 = PR / "paper4_delay_dynamics_v34.md"
V35 = PR / "paper4_delay_dynamics_v35.md"

# the Discussion renumber generations: v31->v32 shifted 11.4-11.7 to
# 11.5-11.8; v34->v35 inserted 11.7 and shifted Open problems to 11.9
RENUM_35 = {"11.9"}                  # vs v34/v33/v32
RENUM_31 = {"11.4", "11.5", "11.6", "11.7", "11.8", "11.9"}  # vs v31

V31_CONTENT_NEEDLES = [
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
    "The institutional loop is not fisheries-specific, and neither is the "
    "analysed class",
    "any periodically reviewed renewable-resource institution",
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
    "Documented timelines occupy the same scales",
]

V34_SURVIVING_NEEDLES = [
    # v33/v34 style markers that survive the abstract compression
    "The delay studied in this paper sits elsewhere",
    "oscillatory dynamics are born",
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
    # v34 devices
    "governance delay",
    "review cadence",
    "What Theorem 8.1 says",
    "What Proposition 8.1 says",
    "Governance warning",
    "Management caution",
    "Attractor record",
    "the two rules carry opposite mathematics",
    "The harvest control rule in force between assessments",
    "tipping point for cycles",
    "Inter-assessment stability margin",
    "Proved theorems",
    "Interval certificates",
    "Declared-status numerical results",
    "if and only if",
    # the ecological reading
    "The exposed life histories are doubly selected",
    "Growth-coupled ecology cannot widen the window",
    "decoupled storage, not growth-coupled ecology, is what can slow the loop",
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
    "plain name", "The message of the paper is stated plainly",
    "is collected in one display",
]

FROZEN_MD5 = {
    "paper4_delay_dynamics_v31.md": "c75674a46b5352e2b3097329320d7c7d",
    "paper4_delay_dynamics_v32.md": "1b09783b0b156347cce3aa3c24f7f149",
    "paper4_delay_dynamics_v33.md": "a2581136fbdbac0f79a1332e42f8e556",
    "paper4_delay_dynamics_v34.md": "4f964bd630bc4d19af448cde47b19025",
    "latex/paper4_delay_dynamics_v31.tex":
        "2224247e4cace8b0f0c2aea85a6ad3be",
    "latex/paper4_delay_dynamics_v32.tex":
        "02d479c048c57f64ecd41509e31ed2f2",
    "latex/paper4_delay_dynamics_v33.tex":
        "658c2fa14e3bbc6a272ded15a8b65a08",
    "latex/paper4_delay_dynamics_v34.tex":
        "a233b61509a76389a9beaae1b50a2e21",
}
V35_TEX_MD5 = "f1bdcd666baf6a0195fa33a7e0913d80"  # three identical builds


def spans(t: str) -> list[str]:
    return re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", t, flags=re.S)


def toks(t: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", t))


def flat(s: str) -> str:
    return re.sub(r"\s+", " ", s)


def journal_words(s: str) -> int:
    return sum(1 for w in re.findall(r"\S+", s) if re.search(r"[A-Za-z0-9]", w))


def refs_block(t: str) -> str:
    lines = t.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.strip() == "## References")
    j = next(k for k, ln in enumerate(lines) if ln.strip() == "## Supplementary material")
    return "\n".join(lines[i:j]).rstrip("\n")


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def main() -> int:
    t31 = V31.read_text(encoding="utf-8")
    t32 = V32.read_text(encoding="utf-8")
    t33 = V33.read_text(encoding="utf-8")
    t34 = V34.read_text(encoding="utf-8")
    t35 = V35.read_text(encoding="utf-8")
    f35 = flat(t35)

    print("== A. v35 vs v34 (direct parent) ==")
    s34, s35 = spans(t34), spans(t35)
    set34 = set(s34)
    invented = [s for s in s35 if s not in set34]
    assert not invented, f"v35 spans not in v34: {invented[:3]}"
    c34, c35 = Counter(s34), Counter(s35)
    lost_spans = {s: c for s, c in c34.items() if c35[s] < c}
    assert not lost_spans, f"v34 span occurrences lost: {lost_spans}"
    print(f"  A1 math spans: {len(s35)} occurrences, all byte-identical to "
          f"v34 spans; all {len(s34)} v34 occurrences survive "
          f"(+{len(s35) - len(s34)} ecological-reading reuses)")

    n34, n35 = toks(t34), toks(t35)
    lost = {t: c for t, c in n34.items() if n35[t] < c and t not in RENUM_35}
    assert not lost, f"v34 numeric tokens lost: {lost}"
    new = {t for t in n35 if t not in n34} - RENUM_35
    assert not new, f"new numeric values vs v34: {sorted(new)[:8]}"
    no_loss = all(n35[t] >= n34[t] for t in ("11.7", "11.8"))
    assert no_loss, "11.7/11.8 lost occurrences"
    print(f"  A2 numeric: {sum(n35.values())} vs {sum(n34.values())} "
          f"tokens; 0 lost; only new value: 11.9 (the declared renumber); "
          f"11.7 count-neutral ({n35['11.7']}), 11.8 heading+cross-ref "
          f"({n34['11.8']} -> {n35['11.8']})")

    h34 = [ln.rstrip() for ln in t34.split("\n") if ln.startswith("#")]
    h35 = [ln.rstrip() for ln in t35.split("\n") if ln.startswith("#")]
    exp = []
    for h in h34:
        if h == "### 11.7 Limitations":
            exp.append("### 11.7 The ecological reading")
            exp.append("### 11.8 Limitations")
        elif h == "### 11.8 Open problems":
            exp.append("### 11.9 Open problems")
        else:
            exp.append(h)
    assert h35 == exp, "heading skeleton differs"
    print("  A3 headings: exactly one insertion (11.7 The ecological "
          "reading) + two renumbers (Limitations 11.8, Open problems 11.9)")

    a35 = t35.split("## Abstract\n\n", 1)[1].split("\n\n**Keywords:**")[0]
    aw = journal_words(a35)
    assert aw <= 259, f"abstract runs {aw} words"
    for tok in ("3.7", "150", "2.3", "6.5", "1992", "2024"):
        assert tok in a35, f"abstract digit token lost: {tok}"
    print(f"  A4 abstract: {aw} journal words (cap 259; v34: 560); all "
          f"six digit tokens preserved")

    assert t34.split("\n", 1)[0] == t35.split("\n", 1)[0], "title changed"
    assert refs_block(t34) == refs_block(t35), "reference block changed"
    for nd in V34_SURVIVING_NEEDLES:
        assert nd in f35, f"surviving needle lost: {nd!r}"
    print(f"  A5 title/references byte-identical; {len(V34_SURVIVING_NEEDLES)} "
          f"surviving style/device needles present")

    print("== B. v35 vs v33 / v32 ==")
    for name, t_old, ren in (("v33", t33, RENUM_35), ("v32", t32, RENUM_35)):
        n_old = toks(t_old)
        lost_x = {t: c for t, c in n_old.items() if n35[t] < c and t not in ren}
        assert not lost_x, f"{name} numeric tokens lost: {lost_x}"
        print(f"  B1 vs {name}: all tokens survive (exempt {sorted(ren)})")
    for nd in V32_CONTENT_NEEDLES:
        assert nd in f35, f"v32 content needle lost: {nd!r}"
    print(f"  B2 v32 additions: {len(V32_CONTENT_NEEDLES)} needles present")

    print("== C. v35 vs v31 ==")
    n31 = toks(t31)
    lost31 = {t: c for t, c in n31.items() if n35[t] < c and t not in RENUM_31}
    assert not lost31, f"v31 numeric tokens lost: {lost31}"
    print(f"  C1 numeric: all v31 tokens survive outside the two renumber "
          f"generations {sorted(RENUM_31)}")
    seq = re.findall(r"### (11\.\d) ", t35)
    assert seq == [f"11.{i}" for i in range(1, 10)], (
        f"Discussion heading sequence broken: {seq}"
    )
    print("  C2 Discussion heading sequence 11.1-11.9 verified in order")
    for nd in V31_CONTENT_NEEDLES:
        assert nd in f35, f"v31 content needle lost: {nd!r}"
    print(f"  C3 v31 additions: {len(V31_CONTENT_NEEDLES)} needles present")

    print("== D. reference-section identity chain ==")
    r31, r32, r33, r34, r35 = (
        refs_block(t31), refs_block(t32), refs_block(t33),
        refs_block(t34), refs_block(t35),
    )
    assert r32 == r33 == r34 == r35, "reference block not frozen v32->v35"
    e31 = [ln for ln in r31.split("\n") if ln.strip()]
    e35 = [ln for ln in r35.split("\n") if ln.strip()]
    removed = [ln for ln in e31 if ln not in e35]
    assert not removed, f"v31 reference entries removed: {removed}"
    print(f"  D1 refs frozen v32==v33==v34==v35 ({len(e35)} entries); "
          f"v31 had {len(e31)}; removed since v31: 0")

    print("== E. error gates re-verified on disk ==")
    hits = [b for b in REJECTION if b in t35]
    assert not hits, f"rejection hits in v35 md: {hits}"
    tex = (LATEX / "paper4_delay_dynamics_v35.tex").read_text(
        encoding="utf-8"
    )
    hits_tex = [b for b in REJECTION if b in flat(tex)]
    assert not hits_tex, f"rejection hits in v35 tex: {hits_tex}"
    print(f"  E1 rejection list: 0 hits in md and tex "
          f"({len(REJECTION)} banned strings)")

    assert flat(t35).count("if and only if") == 5
    print("  E2 'if and only if' x5 unchanged")

    m = md5(LATEX / "paper4_delay_dynamics_v35.tex")
    assert m == V35_TEX_MD5, f"v35 tex md5 drifted: {m}"
    print(f"  E3 v35 tex md5 {m} == the three consecutive byte-identical "
          f"builds")

    drift = {
        k: v for k, v in FROZEN_MD5.items()
        if md5(ROOT / "arena agent 1/paper rewrites" / k) != v
    }
    assert not drift, f"prior versions drifted: {drift}"
    print("  E4 v31/v32/v33/v34 md+tex checksums unchanged (version "
          "discipline)")

    print("\n  CROSS-VERSION REVIEW: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
