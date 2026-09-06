#!/usr/bin/env python3
"""Supplementary builds for wave 8 (P1 v3, P3 v8, P4 v5).

Strips the internal-process narration from the three supplementary
files (wave/revision tags, "Appended at ...", "pre-v28"/"pre-v25"
version references, the S8 preamble's v20 tokens, the trailing
revision note), keeping every load-bearing mapping, status note, and
naming resolution. The P5 supplementary (v5) carries no process
narration and is unchanged. New files; the previous versions are
untouched.
"""
from __future__ import annotations
import hashlib
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites"


def rep(text, old, new, n=1):
    assert text.count(old) == n, f"needle x{text.count(old)} (want {n}): {old[:90]!r}"
    return text.replace(old, new)


def build(old_name, new_name, edits, verify_banned, verify_needles):
    t = (SRC / old_name).read_text()
    orig = t
    for old, new in edits:
        t = rep(t, old, new)
    for banned in verify_banned:
        assert banned not in t, banned
    for needle in verify_needles:
        assert needle in t, needle
    (SRC / new_name).write_text(t)

    def table_lines(x):
        return [l for l in x.split("\n") if l.lstrip().startswith("|")]

    ta, tb = table_lines(orig), table_lines(t)
    diff = [l for l in ta if l not in tb] + [l for l in tb if l not in ta]
    allowed = ("main text's label since v28", "main text's current label")
    assert len(diff) == 0 or (len(diff) == 2 and all(
        any(a in l for a in allowed) for l in diff)), diff
    print(f"{new_name}: {len(orig)} -> {len(t)} chars; MD5 "
          f"{hashlib.md5(t.encode()).hexdigest()}")


# ---------------- P1 supplementary v3 ----------------
build(
    "paper1_supplementary_v2.md", "paper1_supplementary_v3.md",
    [
        # S8 heading loses its process tag
        ("## S8. The 25-Check Enumeration (Wave-4 Deposit)",
         "## S8. The 25-Check Enumeration"),
        # S8 preamble: drop the wave-4/v20 narration, keep the naming notes
        ('*Appended at the wave-4 revision (main-text v20), on the joint audit\'s '
         '"which 25 checks?" item. The machine checks of the verification artifact '
         '(main-text Section 4.9; S7 above) are enumerated here one by one. Each '
         'entry quotes the check\'s recorded name verbatim from the committed '
         'results file (`research_program/paper1_instantiation/'
         'typed_false_positive_instantiation.json`, execution of 2026-08-28, '
         'deterministic, exact integer arithmetic at scale 40, exit 0) and states '
         'the main-text claim it maps to. Nothing is recomputed here and no value '
         'is new; every check\'s recorded pass status is True (25/25). Two naming '
         'notes: the artifact\'s own tokens "FP" and "FP0" name the discrepancy '
         'region $\\mathcal{Q}$ of the main text\'s v20 notation (formerly '
         '$\\mathrm{FP}_0$), and where S7\'s existing text says "Theorem 6" the '
         'v20 status relabel reads Remark 6 — the statement numbers are unchanged, '
         'so every reference resolves by number.*',
         '*The machine checks of the verification artifact (main-text Section 4.9; '
         'S7 above) are enumerated here one by one. Each entry quotes the check\'s '
         'recorded name verbatim from the committed results file '
         '(`research_program/paper1_instantiation/'
         'typed_false_positive_instantiation.json`, execution of 2026-08-28, '
         'deterministic, exact integer arithmetic at scale 40, exit 0) and states '
         'the main-text claim it maps to. Nothing is recomputed here and no value '
         'is new; every check\'s recorded pass status is True (25/25). Two naming '
         'notes: the artifact\'s own tokens "FP" and "FP0" name the discrepancy '
         'region $\\mathcal{Q}$ of the main text\'s notation, and where S7\'s text '
         'says "Theorem 6" the main text\'s status-word map reads Remark 6 — the '
         'statement numbers are unchanged, so every reference resolves by number.*'),
        # trailing revision note -> a plain notation note
        ('*Revision note (wave-7 build, v21).* Notation harmonised with the main '
         'text\'s v20/v21 declarations: S1\'s opening now names the object '
         '$\\mathfrak{S}$ (the named record; bare $S$ remains the typed safe set), '
         'and S6\'s conjectures C2 and C9 write the resource-increment rescue '
         'threshold as $\\kappa^*$ (the letter $r$ is the weight ratio $w_2/w_1$). '
         'No content, status, or value changes.',
         '*Notation note.* S1\'s opening names the object $\\mathfrak{S}$ (the '
         'named record; bare $S$ remains the typed safe set), and S6\'s conjectures '
         'C2 and C9 write the resource-increment rescue threshold as $\\kappa^*$ '
         '(the letter $r$ is the weight ratio $w_2/w_1$).'),
    ],
    ["wave-4", "wave-7", "main-text v20", "v20/v21", "Appended at", "Revision note",
     "formerly"],
    ["25/25", "typed_false_positive_instantiation.json", "$\\mathfrak{S}$",
     "$\\kappa^*$"],
)

# ---------------- P3 supplementary v8 ----------------
build(
    "paper3_supplementary_v7.md", "paper3_supplementary_v8.md",
    [
        # the zero-convention note loses the earlier-draft reference
        ("*The zero convention is load-bearing: an earlier draft of this record "
         "excluded below-reference stocks and understated the protocol.*",
         "*The zero convention is load-bearing: excluding below-reference stocks "
         "would understate the protocol.*"),
        # the retraction sentence loses "The earlier"
        ('The earlier "not reproducible" reading is fully retracted: the archived '
         'pull is internally consistent and carries exactly the cohort statistics '
         'the main text reports.',
         'The "not reproducible" reading is retracted: the archived pull is '
         'internally consistent and carries exactly the cohort statistics the '
         'main text reports.'),
        # S6 heading loses its append tag
        ("## S6. Statement-Status Naming Offset (Appended at Main-Text v29)",
         "## S6. Statement-Status Naming Offset"),
        # S6 preamble: present tense, no v28/wave narration
        ("*Appended at the wave-5 revision, when the main text stood at v29, to "
         "record the\nnaming offset between this file and the main text's "
         "statement labels. Nothing\nabove this section is edited; the note "
         "exists because the main text's v28\nrevision demoted eight audited "
         "inflations as status relabels on the unchanged\nstatement counter, and "
         "S1–S5 above (written before that revision) still carry\nthe pre-v28 "
         "status words.*",
         "*This section records the naming offset between this file and the main "
         "text's\nstatement labels. Nothing above this section is edited; S1–S5 "
         "above carry the\nsupplementary's own status words, and this table maps "
         "them to the main text's\ncurrent labels.*"),
        # the map sentence and column header
        ("The main text's demotion map, status word changed and number unchanged:",
         "The main text's status-word map (status word changed, number unchanged):"),
        ("| this file's label (S1–S5) | main text's label since v28 |",
         "| this file's label (S1–S5) | main text's current label |"),
        # the closing paragraph of S6
        ("only the status word moved, per the audits' theorem-inflation\n"
         "item, and every cross-reference in the main text was updated with it.",
         "only the status word differs; every reference resolves by number."),
        ('The demotions of Theorems 4, 6, 17,\n18, and 20 onto the word '
         '"Proposition" therefore produce the proposition list\n1, 2, 4, 6, 17, 18, '
         '20 — the first two are the layering pair, the rest are\ndemoted theorems '
         'keeping their sequence numbers.',
         "The main counter's Propositions 4, 6, 17,\n18, and 20 join the layering "
         "pair to produce the proposition list\n1, 2, 4, 6, 17, 18, 20 — the first "
         "two are the layering pair, the rest keep\ntheir main-sequence numbers."),
    ],
    ["wave-5", "v29", "v28", "Appended at", "earlier draft", "The earlier",
     "demotion map", "demoted", "audited inflations", "theorem-inflation"],
    ["v4.66", "454", "2.57", "3.39", "HERRVIa", "ANCHMEDGSA17",
     "main text's current label"],
)

# ---------------- P4 supplementary v5 ----------------
build(
    "paper4_supplementary_v4.md", "paper4_supplementary_v5.md",
    [
        # S11 heading loses its process tag
        ("## S11. Relocated MPF Material (Wave-4 Relocation)",
         "## S11. Relocated MPF Material"),
        # S11 preamble: present tense, no wave-4/v27/v26 narration
        ('*Appended at the wave-4 revision (main-text v27) to receive material '
         'relocated from the main article\'s Section 9.3 (the MPF paragraph) and '
         'Section 10.4, on the joint audit\'s routing of the MPF numerics to the '
         'supplement. Every value below is reproduced verbatim from the main '
         'text\'s v26; nothing is recomputed, and the main text retains '
         'one-sentence pointers carrying the key numbers '
         '($\\eta_{\\mathrm{crit}} \\approx 2.337$; inter-excursion-interval '
         'coefficient of variation $1.58$ and return-map anticorrelation '
         '$r = -0.47$; the more-than-$300$-parameterisation screen).*',
         '*Material relocated from the main article\'s Section 9.3 (the MPF '
         'paragraph) and Section 10.4. Every value below is reproduced verbatim '
         'from the main text; nothing is recomputed, and the main text retains '
         'one-sentence pointers carrying the key numbers '
         '($\\eta_{\\mathrm{crit}} \\approx 2.337$; inter-excursion-interval '
         'coefficient of variation $1.58$ and return-map anticorrelation '
         '$r = -0.47$; the more-than-$300$-parameterisation screen).*'),
        # the deposit pointer loses its wave tag
        ("this record is deposited here per the wave-4 relocation.",
         "this record is deposited here with the relocated material."),
        # S12 heading and its status note lose their wave tags
        ("## S12. Status and Label Notes (Wave-7 Append)",
         "## S12. Status and Label Notes"),
        ("**S3 status note (dated at the wave-7 build).**",
         "**S3 status note.**"),
        ("so S3's headline 'The fold certificate is not obtained' now reads as "
         "the status of the validated continuous fold theorem, which no "
         "main-text statement claims.",
         "so S3's headline 'The fold certificate is not obtained' is read as the "
         "status of the validated continuous fold theorem, which no main-text "
         "statement claims."),
        # the statement-label mapping loses its pre-v25 reference
        ("**Statement-label mapping.** S5, S6, S10, and S1.1 retain pre-v25 "
         "statement labels for the following objects; the main text's current "
         "labels are:",
         "**Statement-label mapping.** The following objects carry different "
         "labels in this file than in the main text:"),
        ("S10's heading ('Expanded Proofs: Corollary 3 and Proposition 5') refers "
         "to the objects the main text now labels Corollary 5.1 and Proposition "
         "6.1.",
         "S10's heading ('Expanded Proofs: Corollary 3 and Proposition 5') refers "
         "to the objects the main text labels Corollary 5.1 and Proposition 6.1."),
    ],
    ["wave-4", "wave-7", "pre-v25", "main-text v27", "main text's v26",
     "Appended at", "dated at", "now labels", "now reads"],
    ["$\\eta_{\\mathrm{crit}} \\approx 2.337$", "1.58", "$r = -0.47$",
     "Corollary 5.1", "Proposition 6.1", "$[5.587236198689, 5.587236198691]$"],
)

print("supplementary builds done")
