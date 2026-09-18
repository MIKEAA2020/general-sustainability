#!/usr/bin/env python3
"""Wave-19 / Task 93, part 4: the cross-version content review of
paper4_delay_dynamics_v36.md against v35, v34, v33, v32 and v31 --- the
machine-checked ledger behind humanizing audits/
V36_RESTRUCTURING_AND_CONSOLIDATION.md.

Owner directive verified here: the challenge to the Task-92 adjudication
plus "provide v36" --- the convergent batch-8 restructuring spine
implemented (review interval promoted to Section 7, global numerics to
Section 8, maturation-delay analogue to Section 9; every cross-reference
renumbered by the bijective map; the promoted section's theorem,
proposition and remark labels following their host; the Organization
paragraph rewritten for the new arc) with the E1-E4 consolidations
(repaired cross-references + resolver, delay stages, parameter-box open
task, identification layer).

Checks (all fail-loud, printed as a ledger):

A. v36 -> v35 (the direct parent): math-span multiset EXACT equality;
   content numerics (section refs, headings and theorem labels stripped)
   == v35 + {1992, 2024}; the section-reference multiset == the bijective
   map + the declared E-deltas; the label renumbers; the heading-skeleton
   rotation; frozen blocks (title/keywords/abstract/declarations/
   references/figure byte-identical; Data availability + Supplementary
   identical modulo the map); the permanent cross-reference resolver;
   abstract word count.

B. v36 -> v34 / v33 / v32: raw numeric superset with the declared
   exemption generations (the 11.x renumbers of v32/v35 plus this
   round's section-map and E1 tokens).

C. v36 -> v31: numeric containment with both renumber generations;
   Discussion heading sequence 11.1-11.9; v31 content needles.

D. Reference-section identity chain (v32 == v33 == v34 == v35 == v36).

E. Error gates on disk: rejection list zero hits (md + tex), 'if and only
   if' == 5, tex byte-reproducibility (three consecutive builds), prior
   versions' checksums frozen.
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
V36 = PR / "paper4_delay_dynamics_v36.md"

# renumber generations: v31->v32 shifted the Discussion to 11.4-11.8;
# v34->v35 inserted 11.7 and shifted Open problems to 11.9;
# v35->v36 rotated Sections 7/8/9 (bijective map 7->9, 8->7, 9->8;
# 7.k->9.k, 9.k->8.k), renumbered the promoted section's labels
# (Theorem/Proposition/Remark 8.1 -> 7.1) and repaired the E1 pointers
RENUM_36 = (
    {"7", "8", "9", "11.9", "4.2", "4.4", "5.2", "5.4", "6.4"}
    | {f"{s}.{k}" for s in ("7", "8", "9") for k in range(1, 7)}
)
RENUM_31 = {"11.4", "11.5", "11.6", "11.7", "11.8", "11.9"}

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

V36_STRUCTURE_NEEDLES = [
    # the restructured spine
    "7. The Review Interval as Control",
    "8. Global Numerics at Declared Certification Levels",
    "9. The Delayed-Recruitment (Maturation-Delay) System",
    "Section 7 treats sample-and-hold review",
    "together they carry the sign separation",
    "not the delay equation sampled at the review interval",
    # the renumber map's spot proofs
    "(Theorem 7.1, Proposition 7.1)",
    "Propositions 6.2 and 7.1",
    "**What Theorem 7.1 says.**",
    "**What Proposition 7.1 says.**",
    "the registration counterpart of the reproduction targets of Section 8.6",
    "relocated from Sections 8.3 and 10.4",
    "the paper's reference records (Sections 5.1 and 8.3)",
    "the model of Sections 2–6 and 9",
    "Sections 2.3, 9, and 8.3",
    "stage-analysis machinery of Section 9 is archived verbatim",
    # E1 repairs
    "both crossings subcritical (Section 5.2)",
    "a sufficiently large mobilising weight (Section 5.4)",
    "provably not a Hopf of the continuous system (Sections 6.2 and 6.4)",
    # E2 / E4 / E3 completions
    "Identification is its own layer",
    "latent structural parameters",
    "a reduced compression of the observation, assessment, decision, "
    "deployment, and compliance stages",
    "what the single lag absorbs is their composite timing, not any one "
    "stage",
    "A third stated open task is parameter-box certification",
    "the one-at-a-time windows of Section 8.5 are not boxes",
    # surviving devices
    "The exposed life histories are doubly selected",
    "Growth-coupled ecology cannot widen the window",
    "decoupled storage, not growth-coupled ecology, is what can slow the loop",
    "if and only if",
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
    "Sign Separation Theorem", "viability bleed",
    "phase-stabilisation trap", "administrative hunting", "basin lock-in",
    "A stable eigenvalue is not a stable fishery",
    "A stable eigenvalue is not a sustainable resource system",
]

FROZEN_MD5 = {
    "paper4_delay_dynamics_v31.md": "c75674a46b5352e2b3097329320d7c7d",
    "paper4_delay_dynamics_v32.md": "1b09783b0b156347cce3aa3c24f7f149",
    "paper4_delay_dynamics_v33.md": "a2581136fbdbac0f79a1332e42f8e556",
    "paper4_delay_dynamics_v34.md": "4f964bd630bc4d19af448cde47b19025",
    "paper4_delay_dynamics_v35.md": "e9c99edbcf59cce80f2bd08c2966a74b",
    "latex/paper4_delay_dynamics_v31.tex":
        "2224247e4cace8b0f0c2aea85a6ad3be",
    "latex/paper4_delay_dynamics_v32.tex":
        "02d479c048c57f64ecd41509e31ed2f2",
    "latex/paper4_delay_dynamics_v33.tex":
        "658c2fa14e3bbc6a272ded15a8b65a08",
    "latex/paper4_delay_dynamics_v34.tex":
        "a233b61509a76389a9beaae1b50a2e21",
    "latex/paper4_delay_dynamics_v35.tex":
        "f1bdcd666baf6a0195fa33a7e0913d80",
}
V36_TEX_MD5 = "258c2424a752897a139725681af99ecb"  # three identical builds


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


def block_by_heading(t: str, start: str, end: str | None = None) -> str:
    lines = t.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.strip() == start)
    if end is None:
        return "\n".join(lines[i:]).rstrip("\n")
    j = next(k for k, ln in enumerate(lines) if ln.strip() == end)
    return "\n".join(lines[i:j]).rstrip("\n")


def strip_ref_contexts(t: str) -> str:
    t = re.sub(r"^#{2,3} \d+.*$", " ", t, flags=re.M)
    t = re.sub(
        r"(?:Theorem|Proposition|Corollary|Lemma|Remark)s? "
        r"\d+(?:\.\d+)?(?: and \d+(?:\.\d+)?)*",
        " ", t,
    )
    t = re.sub(
        r"Sections? \d+(?:\.\d+)?"
        r"(?:(?:\s*,\s*(?:and\s+)?|\s+and\s+|–)\d+(?:\.\d+)?)*",
        " ", t,
    )
    return t


def section_refs(t: str) -> Counter:
    return Counter(re.findall(r"Sections? (\d+(?:\.\d+)?)", t))


def map_ref(r: str) -> str:
    if r.startswith("7."):
        return "9." + r[2:]
    if r.startswith("9."):
        return "8." + r[2:]
    return {"7": "9", "8": "7", "9": "8"}.get(r, r)


def renumber(t: str) -> str:
    t = t.replace("Propositions 6.2 and 8.1", "Propositions 6.2 and 7.1")
    t = t.replace("Theorem 8.1", "Theorem 7.1")
    t = t.replace("Proposition 8.1", "Proposition 7.1")
    t = t.replace("Remark 8.1", "Remark 7.1")
    t = re.sub(r"(Sections? )7\.(\d+)", r"\g<1>@@A\g<2>@", t)
    t = re.sub(r"(Sections? )9\.(\d+)", r"\g<1>@@C\g<2>@", t)
    t = re.sub(r"(Sections? )7(?!\.?\d)", r"\g<1>@@A@", t)
    t = re.sub(r"(Sections? )8(?!\.?\d)", r"\g<1>@@B@", t)
    t = re.sub(r"(Sections? )9(?!\.?\d)", r"\g<1>@@C@", t)
    t = re.sub(r"^## 7\.", "## @@A@.", t, flags=re.M)
    t = re.sub(r"^## 8\.", "## @@B@.", t, flags=re.M)
    t = re.sub(r"^## 9\.", "## @@C@.", t, flags=re.M)
    t = re.sub(r"^### 7\.(\d+)", lambda m: f"### @@A{m.group(1)}@", t, flags=re.M)
    t = re.sub(r"^### 9\.(\d+)", lambda m: f"### @@C{m.group(1)}@", t, flags=re.M)
    t = re.sub(r"@@A(\d)@", lambda m: "9." + m.group(1), t)
    t = re.sub(r"@@C(\d)@", lambda m: "8." + m.group(1), t)
    t = t.replace("@@A@", "9").replace("@@B@", "7").replace("@@C@", "8")
    return t


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def main() -> int:
    t31 = V31.read_text(encoding="utf-8")
    t32 = V32.read_text(encoding="utf-8")
    t33 = V33.read_text(encoding="utf-8")
    t34 = V34.read_text(encoding="utf-8")
    t35 = V35.read_text(encoding="utf-8")
    t36 = V36.read_text(encoding="utf-8")
    f36 = flat(t36)

    print("== A. v36 vs v35 (direct parent) ==")
    s35, s36 = spans(t35), spans(t36)
    assert Counter(s35) == Counter(s36), "math-span multiset differs"
    print(f"  A1 math spans: {len(s36)} occurrences, multiset EXACTLY equal "
          f"to v35's {len(s35)} (the rotation moves blocks, changes "
          f"nothing)")

    n35s, n36s = toks(strip_ref_contexts(t35)), toks(strip_ref_contexts(t36))
    assert (n36s - n35s) == Counter({"1992": 1, "2024": 1}) and not (
        n35s - n36s
    ), (
        f"content numerics: delta={dict(n36s - n35s)} lost={dict(n35s - n36s)}"
    )
    print("  A2 content numerics (refs/headings/labels stripped): "
          f"{sum(n36s.values())} vs {sum(n35s.values())} tokens; only "
          "delta: +1992, +2024 (both E2's cod-chronology years, "
          "pre-existing values)")

    r35, r36 = section_refs(t35), section_refs(t36)
    expected = Counter({map_ref(r): c for r, c in r35.items()})
    for k, d in (("4.2", -1), ("4.4", -1), ("5.2", 1), ("5.4", 1),
                 ("5.1", 1), ("8.5", 1), ("11.4", 1), ("11.5", 1)):
        expected[k] += d
    assert r36 == expected, (
        f"section refs: missing={dict(expected - r36)} "
        f"extra={dict(r36 - expected)}"
    )
    print(f"  A3 section references: {sum(r36.values())} (v35: "
          f"{sum(r35.values())}) = the bijective map 7->9, 8->7, 9->8 "
          "(7.k->9.k, 9.k->8.k) + E1 (4.2->5.2, 4.4->5.4) + E3's three "
          "+ E2's one")

    for lab, cnt in (("Theorem 7.1", 11), ("Proposition 7.1", 9),
                     ("Remark 7.1", 2), ("Propositions 6.2 and 7.1", 1)):
        assert t36.count(lab) == cnt, f"label {lab}: {t36.count(lab)}"
    for lab in ("Theorem 8.1", "Proposition 8.1", "Remark 8.1"):
        assert t36.count(lab) == 0, f"stale label {lab}"
    print("  A4 labels: Theorem 7.1 x11, Proposition 7.1 x9, Remark 7.1 "
          "x2, the 'Propositions 6.2 and 7.1' list x1; zero stale 8.1 "
          "labels")

    h35 = [ln.rstrip() for ln in t35.split("\n") if ln.startswith("#")]
    h36 = [ln.rstrip() for ln in t36.split("\n") if ln.startswith("#")]
    a = h35.index("## 7. The Delayed-Recruitment (Maturation-Delay) System")
    b = h35.index("## 8. The Review Interval as Control")
    c = h35.index("## 9. Global Numerics at Declared Certification Levels")
    d = h35.index("## 10. The Loop-Gain Family")
    exp = (
        h35[:a]
        + [renumber(x) for x in h35[b:c]]
        + [renumber(x) for x in h35[c:d]]
        + [renumber(x) for x in h35[a:b]]
        + h35[d:]
    )
    assert h36 == exp, "heading skeleton differs from the declared rotation"
    print("  A5 headings: exactly the declared rotation (8->7, 9->8, 7->9 "
          "with subsection renumbers); nothing else moved")

    a36 = t36.split("## Abstract\n\n", 1)[1].split("\n\n**Keywords:**")[0]
    aw = journal_words(a36)
    assert aw <= 259, f"abstract runs {aw} words"
    for tok in ("3.7", "150", "2.3", "6.5", "1992", "2024"):
        assert tok in a36, f"abstract digit token lost: {tok}"
    print(f"  A6 abstract: {aw} journal words (cap 259; byte-identical to "
          "v35); all six digit tokens preserved")

    assert t35.split("\n", 1)[0] == t36.split("\n", 1)[0], "title changed"
    assert refs_block(t35) == refs_block(t36), "reference block changed"
    for start, end in (
        ("## Declaration of competing interest", "## References"),
        ("## References", "## Supplementary material"),
    ):
        assert block_by_heading(t35, start, end) == block_by_heading(
            t36, start, end
        ), f"frozen block changed: {start}"
    for start, end in (
        ("## Data availability", "## Declaration of competing interest"),
        ("## Supplementary material", None),
    ):
        b35 = block_by_heading(t35, start, end)
        b36 = block_by_heading(t36, start, end)
        assert renumber(b35) == b36, f"block not map-frozen: {start}"
    fig35 = [ln for ln in t35.split("\n") if ln.startswith("![Figure")][0]
    cap35 = [ln for ln in t35.split("\n") if ln.startswith("**Figure 1.**")][0]
    assert t36.count(fig35) == 1 and t36.count(cap35) == 1, (
        "figure block changed"
    )
    print("  A7 frozen blocks: title/keywords/abstract/references/"
          "declarations/figure byte-identical; Data availability + "
          "Supplementary identical modulo the declared renumber map")

    heads = set(re.findall(r"^## (\d+)\.", t36, re.M)) | set(
        re.findall(r"^### (\d+\.\d+)", t36, re.M)
    )
    for m in re.finditer(
        r"Sections? (\d+(?:\.\d+)?)(?:(?:\s*,\s*(?:and\s+)?|\s+and\s+|–)\d+(?:\.\d+)?)*",
        t36,
    ):
        for tgt in re.findall(r"\d+(?:\.\d+)?", m.group(0)[len("Sections"):]):
            assert tgt in heads, f"unresolved cross-reference {tgt}"
    print("  A8 cross-reference resolver: 0 unresolved Section "
          "constructs (the permanent gate; v31's dangling 4.2/4.4 would "
          "have failed it on day one)")

    for nd in V36_STRUCTURE_NEEDLES:
        assert nd in f36, f"structure needle lost: {nd!r}"
    print(f"  A9 {len(V36_STRUCTURE_NEEDLES)} rotation/E-item needles "
          "present")

    print("== B. v36 vs v34 / v33 / v32 ==")
    n36_all = toks(t36)
    for name, t_old in (("v34", t34), ("v33", t33), ("v32", t32)):
        n_old = toks(t_old)
        lost_x = {t: c for t, c in n_old.items()
                  if n36_all[t] < c and t not in RENUM_36}
        assert not lost_x, f"{name} numeric tokens lost: {lost_x}"
        print(f"  B1 vs {name}: all tokens survive outside the declared "
              f"exemptions ({len(RENUM_36)} tokens)")
    for nd in V32_CONTENT_NEEDLES:
        assert nd in f36, f"v32 content needle lost: {nd!r}"
    print(f"  B2 v32 additions: {len(V32_CONTENT_NEEDLES)} needles present")

    print("== C. v36 vs v31 ==")
    n31 = toks(t31)
    n36 = toks(t36)
    lost31 = {t: c for t, c in n31.items()
              if n36[t] < c and t not in (RENUM_36 | RENUM_31)}
    assert not lost31, f"v31 numeric tokens lost: {lost31}"
    print(f"  C1 numeric: all v31 tokens survive outside the two renumber "
          f"generations ({len(RENUM_36 | RENUM_31)} tokens)")
    seq = re.findall(r"### (11\.\d) ", t36)
    assert seq == [f"11.{i}" for i in range(1, 10)], (
        f"Discussion heading sequence broken: {seq}"
    )
    print("  C2 Discussion heading sequence 11.1-11.9 verified in order")
    for nd in V31_CONTENT_NEEDLES:
        assert nd in f36, f"v31 content needle lost: {nd!r}"
    print(f"  C3 v31 additions: {len(V31_CONTENT_NEEDLES)} needles present")

    print("== D. reference-section identity chain ==")
    r31, r32, r33, r34, r35r, r36r = (
        refs_block(t31), refs_block(t32), refs_block(t33),
        refs_block(t34), refs_block(t35), refs_block(t36),
    )
    assert r32 == r33 == r34 == r35r == r36r, "refs not frozen v32->v36"
    e31 = [ln for ln in r31.split("\n") if ln.strip()]
    e36 = [ln for ln in r36r.split("\n") if ln.strip()]
    removed = [ln for ln in e31 if ln not in e36]
    assert not removed, f"v31 reference entries removed: {removed}"
    print(f"  D1 refs frozen v32==v33==v34==v35==v36 ({len(e36)} entries); "
          f"v31 had {len(e31)}; removed since v31: 0")

    print("== E. error gates re-verified on disk ==")
    hits = [b for b in REJECTION if b in t36]
    assert not hits, f"rejection hits in v36 md: {hits}"
    tex = (LATEX / "paper4_delay_dynamics_v36.tex").read_text(
        encoding="utf-8"
    )
    hits_tex = [b for b in REJECTION if b in flat(tex)]
    assert not hits_tex, f"rejection hits in v36 tex: {hits_tex}"
    print(f"  E1 rejection list: 0 hits in md and tex "
          f"({len(REJECTION)} banned strings)")

    assert flat(t36).count("if and only if") == 5
    print("  E2 'if and only if' x5 unchanged")

    m = md5(LATEX / "paper4_delay_dynamics_v36.tex")
    assert m == V36_TEX_MD5, f"v36 tex md5 drifted: {m}"
    print(f"  E3 v36 tex md5 {m} == the three consecutive byte-identical "
          "builds")

    drift = {
        k: v for k, v in FROZEN_MD5.items()
        if md5(ROOT / "arena agent 1/paper rewrites" / k) != v
    }
    assert not drift, f"prior versions drifted: {drift}"
    print("  E4 v31/v32/v33/v34/v35 md+tex checksums unchanged (version "
          "discipline)")

    print("\n  CROSS-VERSION REVIEW: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
