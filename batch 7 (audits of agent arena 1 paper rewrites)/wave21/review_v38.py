#!/usr/bin/env python3
"""Wave-21 / Task 97, part 4: the cross-version content review of
paper4_delay_dynamics_v38.md against v37 (and the whole chain back to
v31), plus the supplementary-file artifact ledger --- the machine-checked
record behind humanizing audits/V38_REFERENCE_ROUND_AND_ARTIFACT_REMOVAL.md.

Owner directive verified here: "1- v38 reference round ... 2- check for
and remove change-long diary, meta-commentary, self-referential, internal
dialogue, informal chat artifacts, etc."

Checks (all fail-loud, printed as a ledger):

A. v38 -> v37 (the direct parent): the on-disk v38 is EXACTLY v37 plus
   the 14 declared anchored edits (reconstruction gate); math-span
   multiset EXACT equality (all 1,473 spans); content numerics == v37 +
   the declared reference-entry/citation tokens + the filename version
   digit (+7, -6; the raw comparison additionally loses the removed
   'Sections 8.3 and 10.4' construct); the section-reference multiset
   == v37 minus that one construct; the heading skeleton identical;
   frozen blocks byte-identical (title/abstract 258 words/declarations/
   Data availability/figure); the References block == the declared
   construction (36 -> 38 entries, uniform paragraph separation); the
   Supplementary block == the declared construction (pointer v6 -> v7
   with the editing-history clauses removed); the cross-reference
   resolver (0 unresolved); the label counts; the artifact-class
   regression gates (the removed phrases absent).

B. Supplement v7 vs v6: the on-disk v7 is EXACTLY v6 plus the 11
   declared anchored edits (10 lines); the S1-S12 structure unchanged
   except the declared S11 retitle ('Relocated MPF Material' ->
   'MPF Material'); the object-label inventory unchanged; the numerics
   lose only the removed (verified 2026-09-03) date stamp; every
   supplement -> main-paper section reference resolves against v38's
   headings; the artifact-class gates (committed / audit document /
   relocated / now-established / where-it-belongs / 2026-09-03 all
   0-hit); the mirror consistency with the main text's own statements.

C. The chain: references frozen v32==v33==v34==v35==v36==v37 (36
   entries) with v38 == v37 + the two declared insertions (38 entries);
   prior versions' md+tex checksums unchanged (version discipline),
   including v37 and the v5/v6 supplements.

D. Error gates on disk: rejection list zero hits (md + tex, 44 banned
   strings including the 9 artifact-class regression gates); 'if and
   only if' == 5; v38 tex md5 == the three consecutive byte-identical
   builds.
"""
from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_v38 import (  # noqa: E402
    PAPER_EDITS,
    PAPER_NUM_ADD,
    PAPER_NUM_LOST,
    PAPER_NUM_LOST_RAW,
    SUPP_EDITS,
    SUPP_NUM_LOST,
)

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"
LATEX = PR / "latex"

V31 = PR / "paper4_delay_dynamics_v31.md"
V32 = PR / "paper4_delay_dynamics_v32.md"
V33 = PR / "paper4_delay_dynamics_v33.md"
V34 = PR / "paper4_delay_dynamics_v34.md"
V35 = PR / "paper4_delay_dynamics_v35.md"
V36 = PR / "paper4_delay_dynamics_v36.md"
V37 = PR / "paper4_delay_dynamics_v37.md"
V38 = PR / "paper4_delay_dynamics_v38.md"
SUPP5 = PR / "paper4_supplementary_v5.md"
SUPP6 = PR / "paper4_supplementary_v6.md"
SUPP7 = PR / "paper4_supplementary_v7.md"

FROZEN_MD5 = {
    "paper4_delay_dynamics_v31.md": "c75674a46b5352e2b3097329320d7c7d",
    "paper4_delay_dynamics_v32.md": "1b09783b0b156347cce3aa3c24f7f149",
    "paper4_delay_dynamics_v33.md": "a2581136fbdbac0f79a1332e42f8e556",
    "paper4_delay_dynamics_v34.md": "4f964bd630bc4d19af448cde47b19025",
    "paper4_delay_dynamics_v35.md": "e9c99edbcf59cce80f2bd08c2966a74b",
    "paper4_delay_dynamics_v36.md": "06af59363a0301b61eae237d7a4f3ea2",
    "paper4_delay_dynamics_v37.md": "f32ef08f15fc3fdfacdc041d6d15a51b",
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
    "latex/paper4_delay_dynamics_v36.tex":
        "258c2424a752897a139725681af99ecb",
    "latex/paper4_delay_dynamics_v37.tex":
        "28f6eee027ba9e5449b9a712bd35a54f",
    "paper4_supplementary_v5.md":
        "8b0170811a31e673cefcc12e59b18895",
    "paper4_supplementary_v6.md":
        "c6da3cfabbfa1b8b6b78d83a957f383a",
}
V38_TEX_MD5 = "b9e23ee40f96852f5b3877aae9858f1d"  # three identical builds

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
    # wave-21 artifact-class regression gates
    "One point is stated once", "stated once, at the outset",
    "relocated", "the committed", "audit document", "is now established",
    "now registered", "2026-09-03", "where it belongs",
]


def md5(p: Path) -> str:
    return hashlib.md5(p.read_bytes()).hexdigest()


def flat(s: str) -> str:
    return re.sub(r"\s+", " ", s)


def spans(t: str) -> list[str]:
    return re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", t, flags=re.S)


def toks(t: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", t))


def strip_ref_contexts(t: str) -> str:
    t = re.sub(
        r"Sections? (\d+(?:\.\d+)?)"
        r"(?:(?:\s*,\s*(?:and\s+)?|\s+and\s+|--|–)\d+(?:\.\d+)?)*",
        " ", t)
    t = re.sub(r"^#{2,3} \d+(?:\.\d+)?[^\n]*$", " ", t, flags=re.M)
    t = re.sub(
        r"\*\*(?:Theorem|Proposition|Lemma|Corollary|Remark|Definition) "
        r"\d+(?:\.\d+)?\*\*", " ", t)
    return t


def headings(t: str) -> list[str]:
    return re.findall(r"^#{2,3} .*$", t, flags=re.M)


def section_refs(t: str) -> Counter:
    c: Counter = Counter()
    for m in re.finditer(
        r"Sections?((?:\s+\d+(?:\.\d+)?)(?:(?:\s*,\s*(?:and\s+)?"
        r"|\s+and\s+|--|–)\d+(?:\.\d+)?)*)",
        flat(t),
    ):
        for r in re.findall(r"\d+(?:\.\d+)?", m.group(1)):
            c[r] += 1
    return c


def refs_block(t: str) -> str:
    lines = t.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.strip() == "## References")
    j = next(
        k for k, ln in enumerate(lines)
        if ln.strip() == "## Supplementary material"
    )
    return "\n".join(lines[i:j]).rstrip("\n")


def journal_words(t: str) -> int:
    a = t.split("## Abstract\n\n", 1)[1].split("\n\n**Keywords:**")[0]
    return sum(
        1 for w in re.findall(r"\S+", a)
        if re.search(r"[A-Za-z0-9]", w)
    )


def supp_section_refs(t: str) -> set[str]:
    refs: set[str] = set()
    for m in re.finditer(
        r"Section[s]?((?:\s+\d+(?:\.\d+)?)(?:(?:\s*,\s*(?:and\s+)?"
        r"|\s+and\s+|--|–)\d+(?:\.\d+)?)*)",
        flat(t),
    ):
        refs |= set(re.findall(r"\d+(?:\.\d+)?", m.group(1)))
    return refs


def supp_s_headings(t: str) -> list[str]:
    return re.findall(r"^#{2,3} S[\d.]+.*$", t, flags=re.M)


def supp_object_labels(t: str) -> list[str]:
    return re.findall(
        r"\*\*(?:Definition|Proposition|Theorem|Remark|Corollary|Lemma) "
        r"S[\d.]+", t,
    )


def main() -> int:
    t37 = V37.read_text(encoding="utf-8")
    t38 = V38.read_text(encoding="utf-8")
    s6 = SUPP6.read_text(encoding="utf-8")
    s7 = SUPP7.read_text(encoding="utf-8")

    print("== A. v38 vs v37 (the direct parent) ==")
    # A1. the reconstruction gate: v38 is exactly v37 + the declared edits
    assert len(PAPER_EDITS) == 14 and len(SUPP_EDITS) == 11
    recon = t37
    for old, new, _tag in PAPER_EDITS:
        assert recon.count(old) == 1
        recon = recon.replace(old, new)
    assert recon == t38, "v38 != v37 + the 14 declared edits"
    l37, l38 = t37.splitlines(), t38.splitlines()
    changed = sum(1 for a, b in zip(l37, l38) if a != b)
    print(f"  A1 reconstruction: v38 == v37 + exactly the 14 declared "
          f"anchored edits ({changed} in-place lines modified, "
          f"{len(l38) - len(l37)} lines net: the two reference entries "
          "with separators minus the normalised double blank)")

    # A2. math spans multiset EXACT equality
    assert Counter(spans(t38)) == Counter(spans(t37))
    print(f"  A2 math spans: {len(spans(t38))} occurrences, multiset "
          "EXACTLY equal to v37's (nothing moved, nothing changed)")

    # A3. content numerics: the declared deltas
    n37 = toks(strip_ref_contexts(t37))
    n38 = toks(strip_ref_contexts(t38))
    assert (n38 - n37) == PAPER_NUM_ADD, dict(n38 - n37)
    assert (n37 - n38) == PAPER_NUM_LOST, dict(n37 - n38)
    r37, r38 = toks(t37), toks(t38)
    assert (r38 - r37) == PAPER_NUM_ADD, "raw numeric delta drifted"
    assert (r37 - r38) == PAPER_NUM_LOST_RAW, "raw numeric loss drifted"
    print("  A3 content numerics (refs/headings/labels stripped): v37 + "
          "the declared tokens only (the two reference entries with "
          "DOIs, the five in-text citations, the v7 filename digit; "
          "nothing else)")

    # A4. section-reference multiset
    sr38, sr37 = section_refs(t38), section_refs(t37)
    assert sr38 == sr37 - Counter({"8.3": 1, "10.4": 1}), (
        f"section-ref delta: {dict((sr37 - sr38) + (sr38 - sr37))}"
    )
    print(f"  A4 section references: {sum(sr38.values())} references = "
          "v37's minus the one removed 'Sections 8.3 and 10.4' construct")

    # A5. heading skeleton identical
    assert headings(t38) == headings(t37)
    print("  A5 headings: identical to v37's")

    # A6. abstract 258 words; title/keywords byte-identical
    assert journal_words(t38) == 258
    assert t38.split("\n", 1)[0] == t37.split("\n", 1)[0]
    kw38 = t38.split("**Keywords:**")[1].split("\n", 1)[0]
    kw37 = t37.split("**Keywords:**")[1].split("\n", 1)[0]
    assert kw38 == kw37
    assert t38.split("## Abstract", 1)[1].split("## 1. Introduction")[0] \
        == t37.split("## Abstract", 1)[1].split("## 1. Introduction")[0]
    print("  A6 abstract: 258 journal words, byte-identical (the "
          "exactness re-check recorded in the round deliverable; the "
          "repair's 2-word cost breaches the below-260 bound --- the "
          "owner decision stands); title and keywords byte-identical")

    # A7. frozen blocks + the declared constructions
    for start, end in (
        ("## Data availability", "## Declaration of competing interest"),
        ("## Declaration of competing interest", "## References"),
    ):
        b37 = t37[t37.find(start):t37.find(end)]
        b38 = t38[t38.find(start):t38.find(end)]
        assert b38 == b37, f"frozen block changed: {start}"
    fig37 = re.search(r"!\[Figure 1\].*?\n\n", t37, flags=re.S).group(0)
    fig38 = re.search(r"!\[Figure 1\].*?\n\n", t38, flags=re.S).group(0)
    assert fig38 == fig37
    # the references block: the declared construction, 38 entries
    rb37, rb38 = refs_block(t37), refs_block(t38)
    expected_rb = rb37
    for old, new, _tag in PAPER_EDITS[10:13]:
        expected_rb = expected_rb.replace(old, new)
    assert rb38 == expected_rb, "references block drifted"
    n_entries = sum(1 for ln in rb38.splitlines() if ln.strip())
    assert n_entries == 38
    body = rb38.split("## References", 1)[1]
    assert "\n\n\n" not in body
    para_entries = [p for p in body.strip().split("\n\n") if p.strip()]
    assert all("\n" not in p.strip() for p in para_entries)
    # the Supplementary block: the declared construction
    sup37 = t37[t37.find("## Supplementary material"):]
    sup38 = t38[t38.find("## Supplementary material"):]
    expected_sup = sup37
    for old, new, _tag in PAPER_EDITS[13:14]:
        expected_sup = expected_sup.replace(old, new)
    assert sup38 == expected_sup, "Supplementary block drifted"
    print("  A7 frozen blocks: declarations/Data availability/figure "
          "byte-identical; References = the declared construction "
          "(36 -> 38 entries, uniform paragraph separation, the Aström/"
          "Aiello seam separated and the double blank normalised); "
          "Supplementary = the declared construction (pointer v6 -> v7, "
          "editing-history clauses removed)")

    # A8. cross-reference resolver
    v38_heads: set[str] = set()
    for h in headings(t38):
        m = re.match(r"^#{2,3} (\d+(?:\.\d+)?)", h)
        if m:
            v38_heads.add(m.group(1))
            v38_heads.add(m.group(1).split(".")[0])
    unresolved = sorted(
        r for r in section_refs(t38) if r not in v38_heads
    )
    assert not unresolved, f"unresolved refs: {unresolved}"
    print("  A8 cross-reference resolver: 0 unresolved Section constructs")

    # A9. the label counts
    for lab, cnt in (("Theorem 7.1", 11), ("Proposition 7.1", 9),
                     ("Remark 7.1", 2), ("Propositions 6.2 and 7.1", 1)):
        assert t38.count(lab) == cnt, f"label count {lab}: {t38.count(lab)}"
    for lab in ("Theorem 8.1", "Proposition 8.1", "Remark 8.1"):
        assert t38.count(lab) == 0
    print("  A9 labels: Theorem 7.1 x11, Proposition 7.1 x9, Remark 7.1 "
          "x2, the 'Propositions 6.2 and 7.1' list x1; zero stale 8.1")

    # A10. the artifact-class regression gates
    for phrase in ("One point is stated once", "at the outset",
                   "are relocated to the supplement",
                   "the relocated MPF", "relocated from Sections",
                   "is now established", "now registered"):
        assert phrase not in t38, f"artifact phrase survived: {phrase!r}"
    assert len(re.findall(r"\bnow\b", t38)) == 2  # 'now studies' + '*now with the gains'
    print("  A10 artifact gates: the removed diary/meta/editing-history "
          "phrases all absent; the two surviving 'now's are the "
          "legitimate ones ('now studies the review cadence', 'now with "
          "the mobilising gains')")

    print("== B. Supplement v7 (the artifact-class removal) ==")
    # B1. the reconstruction gate
    recon_s = s6
    for old, new, _tag in SUPP_EDITS:
        assert recon_s.count(old) == 1
        recon_s = recon_s.replace(old, new)
    assert recon_s == s7, "supp v7 != v6 + the 11 declared edits"
    d_lines = [
        i for i, (a, b) in enumerate(zip(s6.splitlines(), s7.splitlines()), 1)
        if a != b
    ]
    assert d_lines == [21, 73, 93, 103, 135, 163, 196, 215, 217, 229]
    print("  B1 reconstruction: supp v7 == v6 + exactly the 11 declared "
          "anchored edits on 10 lines (L163 carries two)")

    # B2. internal structure: the declared S11 retitle only
    exp_heads = [
        "## S11. MPF Material" if h == "## S11. Relocated MPF Material"
        else h
        for h in supp_s_headings(s6)
    ]
    assert supp_s_headings(s7) == exp_heads
    assert supp_object_labels(s7) == supp_object_labels(s6)
    print("  B2 supplement internal S-structure: S1-S12 unchanged except "
          "the declared S11 retitle; object-label inventory unchanged")

    # B3. numerics: the removed date stamp only
    sn6, sn7 = toks(s6), toks(s7)
    assert (sn7 - sn6) == Counter() and (sn6 - sn7) == SUPP_NUM_LOST
    print("  B3 supplement numerics: the removed "
          "'(verified 2026-09-03)' date stamp only")

    # B4. every supplement -> main-paper reference resolves in v38
    refs = supp_section_refs(s7)
    assert refs == {"2.3", "5", "6", "5.1", "8.2", "8.3", "9", "10.4"}
    unresolved = sorted(r for r in refs if r not in v38_heads)
    assert not unresolved, f"supp refs unresolved: {unresolved}"
    print("  B4 all eight supplement -> main-paper section references "
          "resolve against v38's headings")

    # B5. the S12 label-mapping targets exist in v38
    for lab in ("Remark 5.1", "Corollary 5.1", "Proposition 6.1",
                "Theorem 4.1", "Lemma 2.1", "Theorem 10.1"):
        assert lab in t38, f"S12 label target missing: {lab}"
    print("  B5 the S12 statement-label mapping's main-text targets all "
          "exist in v38")

    # B6. the pointer names the aligned supplement
    assert t38.count("paper4_supplementary_v7.md") == 1
    assert "paper4_supplementary_v6.md" not in t38
    assert SUPP7.exists() and "paper4_supplementary_v7.md" == SUPP7.name
    print("  B6 the paper's Supplementary paragraph names "
          "paper4_supplementary_v7.md, which exists; the stale pointer "
          "is absent")

    # B7. the artifact-class gates on the supplement
    for phrase in ("committed", "audit document", "audit `audits",
                   "relocated", "2026-09-03", "now established",
                   "is now verified", "where it belongs",
                   "tikhonov_unh_verification"):
        assert phrase not in s7, f"supp artifact survived: {phrase!r}"
    assert "the Hocherman, Trop, and Ghermandi (2025) synthesis" in s7
    print("  B7 supplement artifact gates: committed/audit-document/"
          "relocated/date-stamp/now-established/where-it-belongs all "
          "0-hit; the Hocherman citation now carries the three-author "
          "house form")

    # B8. mirror consistency with the main text's own statements
    assert ("the Section 9 records (gate log and fine-map table, "
            "Supplementary S9)") in t38
    assert "together with the MPF material of S11" in t38
    assert "Material from the main article's Section 8.3" in s7
    assert "## S11. MPF Material" in s7
    print("  B8 mirror consistency: the main text's Data availability "
          "and Supplementary paragraph agree with the supplement's own "
          "references")

    print("== C. the chain ==")
    # C1. references frozen across the chain; v38 = v37 + 2 insertions
    blocks = [refs_block(p.read_text(encoding="utf-8")) for p in
              (V32, V33, V34, V35, V36, V37)]
    assert all(b == blocks[0] for b in blocks)
    n_prior = sum(1 for ln in blocks[0].splitlines() if ln.strip())
    assert n_prior == 36
    assert rb38 == expected_rb
    print(f"  C1 references frozen v32==v33==v34==v35==v36==v37 "
          f"({n_prior} entries); v38 == v37 + the two declared "
          f"insertions (38 entries; the version-boundary event "
          f"Task 96 recommended)")

    # C2. prior checksums unchanged
    for name, want in FROZEN_MD5.items():
        got = md5(ROOT / "arena agent 1/paper rewrites" / name)
        assert got == want, f"checksum drift: {name}: {got} != {want}"
    print("  C2 v31/v32/v33/v34/v35/v36/v37 md+tex and supp v5/v6 "
          "checksums unchanged (version discipline; never overwritten)")

    print("== D. error gates re-verified on disk ==")
    hits = [b for b in REJECTION if b in t38]
    assert not hits, f"rejection hits in v38 md: {hits}"
    tex = (LATEX / "paper4_delay_dynamics_v38.tex").read_text(
        encoding="utf-8"
    )
    hits_tex = [b for b in REJECTION if b in flat(tex)]
    assert not hits_tex, f"rejection hits in v38 tex: {hits_tex}"
    print(f"  D1 rejection list: 0 hits in md and tex "
          f"({len(REJECTION)} banned strings, incl. the 9 artifact-class "
          f"regression gates)")

    assert flat(t38).count("if and only if") == 5
    print("  D2 'if and only if' x5 unchanged")

    m = md5(LATEX / "paper4_delay_dynamics_v38.tex")
    assert m == V38_TEX_MD5, f"v38 tex md5 drifted: {m}"
    print(f"  D3 v38 tex md5 {m} == the three consecutive byte-identical "
          "builds")

    print("\n  CROSS-VERSION REVIEW: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
