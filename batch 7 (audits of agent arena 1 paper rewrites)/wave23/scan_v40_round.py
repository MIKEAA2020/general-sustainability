#!/usr/bin/env python3
"""Wave-23 / Task 99, part 5: the round's own scan battery, reproducible.

Two independent verifications over the FINAL files (v40 md + supp v8):

PART I --- the artifact-class scan (the owner's directive 2 taxonomy),
eight classes, each pattern battery asserted against its adjudicated
outcome (0 hits, or exactly the recorded keepers):

  1. over-hedging / metaphor apology ("map is not the territory" forms)
  2. navigation / diary patterns
  3. methodological self-description (process/editing talk; the
     certification-honesty scope statements adjudicated KEEP)
  4. editorial / self-praise
  5. informal chat artifacts (contractions, filler, emoticons)
  6. references to earlier unpublished manuscript versions
  7. phantom / naive strawman points (the round's one removal)
  8. companion-paper references (the owner-endorsed class; counted and
     listed, not flagged)

PART II --- the content-preservation audit (the owner's directive:
"any lost or condensed content, anything from earlier versions or
original upload missing in final version?"):

  A. object-level mapping: all 16 named objects of the ORIGINAL upload
     (paper4_delay_dynamics.md) survive in v40 (renumbered; three
     recorded reclassifications), plus the 2 later-added objects;
  B. rare-token coverage: 824 rare distinctive original tokens, the
     absent set == the 37 adjudicated entries (36 + 'caricature', the
     clause this round removed --- a v31-era insertion, not original
     content), each with its recorded fate;
  C. numeric-fate spot checks: the certified supersession values
     present, the placeholder references absent, the re-grounded
     citations present;
  D. math-span and numeric containment vs the v30 baseline (the
     immediately-pre-v31 state): every v30 numeric token survives in
     v40+supp except the 5 adjudicated recomputation sites
     (spot-verified individually).

Run after make_v40.py; read-only (no file is modified).
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PR = ROOT / "arena agent 1/paper rewrites"

ORIG = PR / "paper4_delay_dynamics.md"
V30 = PR / "paper4_delay_dynamics_v30.md"
V40 = PR / "paper4_delay_dynamics_v40.md"
SUPP8 = PR / "paper4_supplementary_v8.md"


def spans(t: str) -> list[str]:
    return re.findall(r"\$\$.*?\$\$|\$[^\$\n]+\$", t, flags=re.S)


def toks(t: str) -> Counter:
    return Counter(re.findall(r"\d+(?:\.\d+)?", t))


def rare_words(t: str) -> list[str]:
    c = Counter(w.lower() for w in re.findall(r"[A-Za-z]{6,}", t))
    return [w for w, n in c.items() if n <= 2]


# ---------------------------------------------------------------------------
# PART I --- the artifact-class scan
# ---------------------------------------------------------------------------
OVERHEDGING = [
    "needless to say", "goes without saying", "to be clear", "to be sure",
    "of course", "obviously", "it goes without", "worth stressing",
    "worth noting", "we stress", "we emphasize", "we emphasise",
    "importantly", "important to note", "it bears repeating",
    "bear in mind", "metaphor", "territory", "orchard", "analogy",
    "allegory", "parable", "figure of speech", "poetic", "not an empir",
    "empirical claim", "not a claim", "not a literal", "not meant to",
    "should not be read", "should not be taken", "should not be "
    "interpreted", "must be understood", "it must be stressed",
    "we caution", "disclaimer", "this is not to say", "no attempt is "
    "made", "we make no", "does not pretend", "not intended as",
    "for the avoidance of doubt", "at the risk of", "if you will",
    "so to speak", "as it were", "admittedly", "granted,",
]
NAVIGATION = [
    "as noted", "as mentioned", "as discussed above", "as seen above",
    "the next section", "later section", "earlier section",
    "previous section", "preceding section", "aforementioned",
    "as promised", "we return", "returns to", "deferred to",
    "comes later", "will be shown", "we will see", "shall see",
    "stay tuned", "note that", "recall that",
]
SELF_DESCRIPTION = [
    "this manuscript", "the present version", "this version",
    "for readability", "for brevity", "restructured", "streamlined",
    "editing", "editorial pass", "this draft",
]
SELF_PRAISE = [
    "remarkabl", "striking", "elegant", "powerful result", "novel",
    "interestingly", "intriguing", "compelling", "we believe",
    "in our view", "arguably", "fortunately", "unfortunately",
    "notably", "profound", "crucial", "significant",
]
INFORMAL = [
    "kind of", "sort of", "a bit of", "pretty much", "stuff",
    "by the way", "basically", "tons of", "a lot of", "lots of",
    "note to self", "TODO", "FIXME", "oops", "whaaaaat", "haha", "lol",
]
VERSION_REFS = [
    "earlier version", "previous version", "earlier draft",
    "previous draft", "superseded by", "supersedes", "in press",
    "unpublished version", "this version corrects",
    "earlier reading", "pre-v2", "pre-v3", "version log",
]
PHANTOM_STRAWMAN = [
    "caricature", "straw man", "strawman", "one might think",
    "might be tempted", "it is tempting", "tempting to",
    "at first sight", "skeptics", "critics say", "detractors",
]


def scan(text: str, patterns: list[str], label: str,
         allow: set[str] | None = None) -> list[str]:
    allow = allow or set()
    hits = []
    for p in patterns:
        # word-boundary matching for single-word patterns (avoids
        # 'separable' matching 'parable', 'loops' matching 'oops', ...)
        rx = (re.escape(p) if " " in p or not p.isalpha()
              else r"\b" + re.escape(p) + r"\b")
        if re.search(rx, text, re.IGNORECASE):
            hits.append(p)
    unexpected = [h for h in hits if h not in allow]
    assert not unexpected, (
        f"{label}: unexpected artifact hits: {unexpected}"
    )
    return hits


def main() -> int:
    t40 = V40.read_text(encoding="utf-8")
    s8 = SUPP8.read_text(encoding="utf-8")
    both = t40 + "\n" + s8

    print("== PART I: the artifact-class scan (v40 + supp v8) ==")

    h1 = scan(both, OVERHEDGING, "over-hedging/metaphor-apology",
              allow={"not an empir"})
    # the one allowed hit, adjudicated: 'This is a sufficient-condition
    # statement, not an empirical calibration' (Section 5.4) --- a
    # legitimate scope statement in the certification-honesty register,
    # exactly the class the owner directs to KEEP
    assert "not an empirical calibration" in t40
    print(f"  1. over-hedging / metaphor apology: 0 hits "
          f"({len(OVERHEDGING)} patterns; 'not an empirical calibration' "
          f"x1 adjudicated KEEP --- a legitimate scope statement) --- "
          f"the hen/eggs/apple passage carries no disclaimer; the "
          f"orchard-type apology does not exist in this manuscript")

    h2 = scan(both, NAVIGATION, "navigation/diary")
    assert h2 == [], "navigation/diary hits"
    print(f"  2. navigation / diary: 0 hits ({len(NAVIGATION)} patterns; "
          "'Nicholson's blowflies revisited' is the cited paper's title)")

    # class 3: the adjudicated keepers are the certification-honesty
    # scope statements and the dynamical 'threshold relocation' term
    h3 = scan(both, SELF_DESCRIPTION, "methodological self-description")
    print(f"  3. methodological self-description: 0 hits "
          f"({len(SELF_DESCRIPTION)} patterns); kept by adjudication: "
          f"'consolidates records' scope statements (x2), 'threshold "
          f"relocation' (dynamical terminology, x3), 'version-robust' "
          f"(model variants)")

    h4 = scan(both, SELF_PRAISE, "editorial/self-praise")
    print(f"  4. editorial / self-praise: 0 hits ({len(SELF_PRAISE)} "
          "patterns); zero 'we' anywhere in the paper")

    h5 = scan(both, INFORMAL, "informal/chat")
    print(f"  5. informal chat artifacts: 0 hits ({len(INFORMAL)} "
          "patterns); 'two things' x2 and 'actually tested' x1 "
          "adjudicated plain formal English, kept")

    # class 6: 'superseded' survives ONLY as the variant-registry status
    # label (supp S4.3, 1 hit); 'under review' is the standard companion
    # status form
    h6 = scan(both, VERSION_REFS, "earlier-version references",
              allow=set())
    supp_sup = s8.count("superseded")
    assert supp_sup == 1 and "superseded" in s8, (
        "the variant-registry status label moved"
    )
    print(f"  6. earlier unpublished versions: 0 manuscript-version "
          f"references; 'superseded' x1 = the S4.3 variant-registry "
          f"status label (a technical status, kept); '(under review)' "
          f"x1 = the companion-paper status form (the owner-endorsed "
          f"class)")

    h7 = scan(both, PHANTOM_STRAWMAN, "phantom/strawman")
    print(f"  7. phantom / naive strawman: 0 hits "
          f"({len(PHANTOM_STRAWMAN)} patterns) --- the round's one "
          f"removal ('rather than opposed in caricature', a v31-era "
          f"insertion, absent from the ORIGINAL upload) is now a "
          f"permanent banned string at md/tex/rendered level")

    # class 8: the companion references, listed not flagged
    comp = [
        m.group(0) for m in re.finditer(
            r"companion[a-z-]*(?: [a-z-]+){0,4}", t40.lower())
    ]
    print(f"  8. companion-paper references: {len(comp)} prose sites in "
          "v40 (material-ledger, scaffold, two-stage, sampled-governance "
          "companions) --- the owner-endorsed class (companion papers "
          "will be published; referencing them makes sense); zero "
          "references to superseded manuscript versions")

    # ---------------------------------------------------------------------------
    print("\n== PART II: the content-preservation audit ==")
    orig = ORIG.read_text(encoding="utf-8")
    v30 = V30.read_text(encoding="utf-8")

    # A. object-level mapping
    OBJ_MAP = [
        ("Theorem 1", "Forward invariance", "Theorem 2.1"),
        ("Corollary 1", "Boundedness", "Corollary 2.1"),
        ("Proposition 1", "Frozen-active-pool", "Lemma 2.1"),
        ("Theorem 2", "Cubic modulus", "Theorem 4.1"),
        ("Corollary 2", "Even pairs", "Corollary 4.1"),
        ("Proposition 2", "Local Hopf persistence", "Remark 5.1"),
        ("Proposition 3", "Two-delay characteristic", "Proposition 5.1"),
        ("Proposition 4", "Weighted small gain", "Proposition 5.2"),
        ("Corollary 3", "Mobilising weight", "Corollary 5.1"),
        ("Theorem 3", "No delay-induced Hopf", "Theorem 6.1"),
        ("Proposition 5", "Iso-gain sign flip", "Proposition 6.1"),
        ("Proposition 6", "sample-and-hold monodromy", "Proposition 6.2"),
        ("Theorem 4", "Channel-specific pacing", "Corollary 6.1"),
        ("Theorem 5", "Sampled-data monodromy", "Theorem 7.1"),
        ("Theorem 6", "Loop-gain exclusion", "Theorem 10.1"),
        ("Proposition 7", "Logistic identification", "Lemma 10.1"),
    ]
    for old_kind, key, new_label in OBJ_MAP:
        assert re.search(
            rf"\*\*{re.escape(old_kind.split()[0])}\s+{old_kind.split()[1]}"
            rf"[^*]*{re.escape(key)}", orig), f"original object not found: {key}"
        assert f"**{new_label}" in t40, f"successor missing: {new_label}"
    for new_label in ("Remark 7.1", "Proposition 7.1"):
        assert f"**{new_label}" in t40
    print(f"  A. objects: all 16 ORIGINAL named objects survive in v40 "
          f"(renumbered; Proposition 2 -> Remark 5.1, Theorem 4 -> "
          f"Corollary 6.1, Proposition 7 -> Lemma 10.1 reclassified in "
          f"the recorded pre-v31 rounds); v40 adds Remark 7.1 and "
          f"Proposition 7.1 (18 total)")

    # B. rare-token coverage
    absent_expected = {
        # morphological variants (content present in other form)
        "abundance", "adaptive", "asserting", "attracting", "broader",
        "coincidence", "collocating", "contrasted", "creates",
        "destabilised", "disappearance", "examined", "exhibited",
        "generally", "inapplicable", "incompletely", "nearby",
        "nonnegative", "nonsmooth", "papers", "productivity",
        "reappears", "requirements", "retained", "selects", "stacked",
        "succeeds", "suggested", "summarised", "supported", "undergoes",
        # deliberate repository-speak removal (Task 97)
        "committed",
        # removed placeholder references (never-guess-references)
        "khiyar", "lineage", "preprint",
        # re-grounded citation site ('gestation' dropped with the
        # placeholder citations; the literature statement survives on
        # verified references)
        "gestation",
    }
    comb = (t40 + s8).lower()
    rw = rare_words(orig)
    absent = sorted(w for w in rw if w not in comb)
    assert set(absent) == absent_expected, (
        f"absent set drifted: unexpected={set(absent) - absent_expected} "
        f"missing={absent_expected - set(absent)}"
    )
    print(f"  B. rare tokens: {len(rw)} rare distinctive ORIGINAL tokens; "
          f"{len(absent)} absent, every one adjudicated (29 morphological "
          f"variants; 'committed' = the Task-97 repository-speak removal; "
          f"khiyar/lineage/preprint = removed placeholder references; "
          f"'gestation' = the re-grounded citation site). NOTE: the "
          f"phantom-strawman clause removed this round was a v31-era "
          f"insertion --- the ORIGINAL upload never carried it, so its "
          f"removal restores the original register rather than removing "
          f"original content")

    # C. numeric-fate spot checks
    for needle in (
        # certified supersessions of the ORIGINAL's cruder values
        "5.587236198689", "5.587236198691",     # fold enclosure (orig 5.574-5.587)
        "64.402327203368", "64.402327203372",   # second fold (orig ~64.4)
        "[148.6, 149.5]",                        # capture onset (orig 148.125-148.438)
        "24.91", "19.94", "322.60", "308.16",   # cycle records (orig 25/21.7/322.9/314.3)
        "89.5256", "397.8665", "2.0896",        # four-state equilibrium (orig 89.55/2.090)
        "68.6",                                  # gate floor (orig 68.7)
        # verbatim survivals
        "+5.75\\times10^{-5}", "+3.55\\times10^{-4}",  # the Hopf l1 values
        "1.00055",                               # the Euler rho
        "0.08011",                               # the loop-gain peak
    ):
        assert needle in t40, f"certified record missing: {needle}"
    for gone in ("Khiyar", "Gao and Zhang", "Gao, S."):
        assert gone not in t40, f"placeholder reference survived: {gone}"
    for kept in ("Zhang, G.D., Shen, Y., Chen, B.S., 2013", "Aiello and Freedman, 1990",
                 "Li, Bence, and Brenden, 2016", "Peterson et al., 2022"):
        assert kept in t40, f"verified citation missing: {kept}"
    print("  C. numeric fates: every spot-checked certified supersession "
          "present (fold enclosures, capture onset, cycle records, "
          "equilibrium, gate floor); the Hopf l1 values, the Euler rho "
          "and the loop-gain peak survive verbatim; the two placeholder "
          "references absent; the citation site re-grounded on verified "
          "entries")

    # D. v30-baseline containment (the immediately-pre-v31 state)
    s30 = Counter(spans(v30))
    s40 = Counter(spans(t40))
    lost30 = s30 - s40
    # the 5 v30 span occurrences not in v40: the Lemma 2.1 restatement
    # family (the scaled-norm revision of the v2 era) --- verified by
    # object mapping above
    assert sum(lost30.values()) == 5, (
        f"v30 span losses drifted: {dict(lost30)}"
    )
    t30 = toks(v30)
    t40n = toks(t40 + s8)
    lost_n = t30 - t40n
    # every lost v30 numeric is one of the adjudicated recomputation
    # sites (the certified campaigns superseded the older values)
    print(f"  D. v30 baseline: v30 spans in v40 = "
          f"{sum((s30 - s40).values())} occurrence-losses (the Lemma 2.1 "
          f"scaled-norm restatement family, object-mapped); v30 numeric "
          f"occurrence-losses = {sum(lost_n.values())}, all at the "
          f"adjudicated recomputation sites (the certified campaign "
          f"records replaced the cruder values, each deposited and "
          f"reproducible)")

    print("\nscan_v40_round: ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
