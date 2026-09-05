#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wave-5 P3 build: paper3_material_ledgers_v29.md from v28, plus the ONE allowed
append (S6) to paper3_supplementary_v7.md.

Owner directive (wave 5): evaluate the registered follow-ups left behind the
owner gate.  The verified finding for P3: the wave-4 theorem demotions were
status relabels on the unchanged 1-20 statement counter, and five of them landed
on the "Proposition" type-word (Theorems 4, 6, 17, 18, 20 -> Propositions
4, 6, 17, 18, 20) -- but the paper already carried a SEPARATE two-item
proposition stream (the layering Propositions 1-2 of Section 3.1).  The
propositions therefore now read 1, 2, 4, 6, 17, 18, 20, and every reference
still resolves uniquely, but the ordinal expectation is broken and nothing in
the paper declares the convention.  The same demotions also left the
supplementary's S4 statement inventory (and one S1-S5 token set) carrying the
pre-v28 status words, with the offset recorded only in the main-text version
log -- a supplementary-side reader gets no fence (P1's S7 token, by contrast,
is fenced inside its own supplementary by the S8 preamble).

Controlled fix (declaration, not re-letter -- a re-letter would break the
number resolution the relabels were chosen to preserve):
  1. Section 3.1 gains a one-sentence numbering note at the layering
     propositions (the site where the two streams first meet).
  2. S6 is appended to the supplementary: the status-word offset note plus the
     two-counter declaration (append-only, idempotent-with-verification).
  3. The main-text supplementary pointer now names S6.

Non-destructive: no statement, proof, table row, or number changes.
"""
import hashlib
import re
import sys

BASE = "arena agent 1/paper rewrites/"
SRC = BASE + "paper3_material_ledgers_v28.md"
DST = BASE + "paper3_material_ledgers_v29.md"
SUPP = BASE + "paper3_supplementary_v7.md"

with open(SRC, "r", encoding="utf-8") as f:
    src = f.read()
with open(SUPP, "r", encoding="utf-8") as f:
    supp = f.read()


def sub1(text, old, new, tag):
    n = text.count(old)
    if n != 1:
        sys.exit("FAIL [%s]: anchor occurs %d times (expected 1): %r" % (tag, n, old[:80]))
    return text.replace(old, new, 1)


def check(cond, msg):
    if not cond:
        sys.exit("FAIL [check]: " + msg)


# ---------------------------------------------------------------- Edit 1: numbering note
OLD1 = "The logical relations are the content of the next two propositions."
NEW1 = (
    "The logical relations are the content of the next two propositions. "
    "(Numbering note: the two layering propositions of this section carry their "
    "own counter, Propositions 1–2; every other numbered statement of this "
    "article runs on the single 1–20 sequence counter, whose status words "
    "reflect the audited demotions — \u201cProposition 4\u201d, \u201cProposition "
    "6\u201d, \u201cProposition 17\u201d, \u201cProposition 18\u201d, and "
    "\u201cProposition 20\u201d are the demoted Theorems 4, 6, 17, 18, and 20, "
    "not further members of the layering counter — so every label is unique and "
    "resolves directly; the supplementary\u2019s statement inventory and this "
    "offset are reconciled in its S6.)"
)

# ---------------------------------------------------------------- Edit 2: supplementary pointer
OLD2 = (
    "the statement inventory with the status of every statement in the main text "
    "(theorem with displayed proof, conditional theorem, definition, application "
    "record, or boundary statement); and the fisheries cohort record"
)
NEW2 = (
    "the statement inventory with the status of every statement in the main text "
    "(theorem with displayed proof, conditional theorem, definition, application "
    "record, or boundary statement) — read with the S6 statement-status naming "
    "offset, which maps this file\u2019s pre-v28 status words to the main text\u2019s "
    "demotion relabels; and the fisheries cohort record"
)

# ---------------------------------------------------------------- Version log
m = re.search(r"^\*Version log \(v28\)\.\*.*$", src, re.M)
if not m:
    sys.exit("FAIL [log]: v28 version log line not found")
VLOG = (
    "*Version log (v29).* Wave-5 owner-directed re-open pass (the registered "
    "follow-ups behind the owner gate, re-evaluated). One item implemented, the "
    "verified statement-numbering confusion: the v28 demotions relabelled "
    "Theorems 4, 6, 17, 18, and 20 as Propositions on the unchanged 1–20 "
    "counter, which put five propositions on the type-word of the paper\u2019s "
    "separate two-item layering stream (Propositions 1–2 of Section 3.1), so "
    "the propositions read 1, 2, 4, 6, 17, 18, 20 with every label unique but "
    "the convention undeclared. Controlled fix by declaration, not re-letter "
    "(a re-letter would break the number resolution the relabels were chosen to "
    "preserve, including the supplementary inventory): Section 3.1 gains a "
    "one-sentence numbering note at the site where the two counters first meet, "
    "and the supplementary gains S6 (appended, the one allowed edit) — the "
    "statement-status naming offset that maps this file\u2019s pre-v28 status "
    "words (S4\u2019s inventory: Theorems 2, 3, 4, 6, 17, 18, 20; Lemma 16) to "
    "the v28/v29 labels (Remark 2, Lemma 3, Proposition 4, Proposition 6, "
    "Proposition 17, Proposition 18, Proposition 20, Remark 16), with the "
    "two-counter declaration; the main-text supplementary pointer now names S6. "
    "The registered length remainder (the 21k→12k reduction) stays registered "
    "with its recorded reason (restructure-level cuts would remove content the "
    "auditors called the publishable core). No statement, proof, table row, "
    "recorded value, or verdict changes."
)

out = src
out = sub1(out, OLD1, NEW1, "numbering-note")
out = sub1(out, OLD2, NEW2, "supp-pointer")
out = sub1(out, m.group(0), VLOG, "vlog")

# ---------------------------------------------------------------- S6 append (idempotent)
S6 = """

## S6. Statement-Status Naming Offset (Appended at Main-Text v29)

*Appended at the wave-5 revision, when the main text stood at v29, to record the
naming offset between this file and the main text's statement labels. Nothing
above this section is edited; the note exists because the main text's v28
revision demoted eight audited inflations as status relabels on the unchanged
statement counter, and S1–S5 above (written before that revision) still carry
the pre-v28 status words.*

The main text's demotion map, status word changed and number unchanged:

| this file's label (S1–S5) | main text's label since v28 |
|---|---|
| Theorem 2 (registered-family support-saturated identity) | Remark 2 |
| Theorem 3 (flux reconstruction) | Lemma 3 |
| Theorem 4 (conservation reduction) | Proposition 4 |
| Theorem 6 (finite exhaustion under uniform drift) | Proposition 6 |
| Lemma 16 (specialization deficit identity) | Remark 16 |
| Theorem 17 (threshold-horizon bracket) | Proposition 17 |
| Theorem 18 (inverse-Gaussian passage) | Proposition 18 |
| Theorem 20 (geometric-Brownian passage) | Proposition 20 |

Every other label in S1–S5 (Theorems 1, 5, 7–15, Corollary 19, Definitions 1–6,
and the layering Propositions 1–2) is unchanged and matches the main text. No
statement content, hypothesis, proof, number, or recorded value changed in any
of these relabels; only the status word moved, per the audits' theorem-inflation
item, and every cross-reference in the main text was updated with it. Because the
numbers are unchanged, every reference in this file still resolves by number,
with this table as the status-word key.

One further numbering declaration, recorded here for the same reason: the main
text runs two statement counters. The 1–20 counter carries the results in order
of appearance (with the mixed status words above); the two layering propositions
of the main text's Section 3.1 ("conservation consistency implies accounting
consistency"; "barrier safety does not follow from accounting consistency")
carry their own counter, Propositions 1–2. The demotions of Theorems 4, 6, 17,
18, and 20 onto the word "Proposition" therefore produce the proposition list
1, 2, 4, 6, 17, 18, 20 — the first two are the layering pair, the rest are
demoted theorems keeping their sequence numbers. Each label is unique in the
main text and resolves directly; the main text declares this convention at the
layering site.
"""

if "## S6. Statement-Status Naming Offset" in supp:
    # idempotent re-run: verify the existing append is byte-identical, never re-append
    if not supp.rstrip("\n").endswith(S6.rstrip("\n")):
        sys.exit("FAIL [S6]: existing S6 tail diverges from the expected constant")
    print("S6 already present — verified byte-identical, no write to the supplementary")
else:
    # the append must land at end-of-file, after the current last paragraph
    tail_marker = "and its cohort-sensitivity record makes that scoping explicit."
    check(supp.count(tail_marker) == 1, "supplementary tail anchor not unique")
    supp_new = supp.rstrip("\n") + "\n" + S6
    with open(SUPP, "w", encoding="utf-8") as f:
        f.write(supp_new)
    print("OK  appended S6 to %s" % SUPP)

# ---------------------------------------------------------------- Checks (main text)
def body_of(t):
    return "\n".join(l for l in t.split("\n") if not l.startswith("*Version log"))


src_body, out_body = body_of(src), body_of(out)
check(out_body.count("Numbering note: the two layering propositions") == 1,
      "numbering note absent or duplicated")
check(out_body.count("S6") >= 2, "S6 pointer missing")
# the eight old status-words must not appear in the v29 body outside the version log
for old_name in ["**Theorem 2 (", "**Theorem 3 (", "**Theorem 4 (",
                 "**Theorem 6 (", "**Lemma 16 (", "**Theorem 17 (",
                 "**Theorem 18 (", "**Theorem 20 ("]:
    check(out_body.count(old_name) == 0, "old status header survives: " + old_name)
# demotion labels present with pinned body counts (v28 body values; the five
# labels named in the new numbering note each gain exactly one mention)
NOTE_LABELS = ("Proposition 4", "Proposition 6", "Proposition 17",
               "Proposition 18", "Proposition 20")
for lbl, cnt in [("Remark 2", 3), ("Lemma 3", 8), ("Proposition 4", 5),
                 ("Proposition 6", 1), ("Remark 16", 2), ("Proposition 17", 2),
                 ("Proposition 18", 2), ("Proposition 20", 1)]:
    exp = cnt + (1 if lbl in NOTE_LABELS else 0)
    a, b = src_body.count(lbl), out_body.count(lbl)
    check(a == cnt, "v28 body count of %r is %d (expected %d)" % (lbl, a, cnt))
    check(b == exp, "v29 body count of %r is %d (expected %d)" % (lbl, b, exp))
# layering propositions untouched
check(out_body.count("**Proposition 1.**") == 1 and out_body.count("**Proposition 2.**") == 1,
      "layering propositions changed")
# frozen needles unchanged
for needle in ["exhaustion-horizon", "$\\rho_P$", "74{,}000{,}000", "0.535",
               "$\\kappa_A K - \\gamma_U U$", "MCS 2026"]:
    a, b = src_body.count(needle), out_body.count(needle)
    check(a == b and a > 0, "frozen needle %r count %d -> %d" % (needle, a, b))

with open(DST, "w", encoding="utf-8") as f:
    f.write(out)

md5 = hashlib.md5(out.encode("utf-8")).hexdigest()
print("OK  wrote %s (%d lines, md5 %s)" % (DST, out.count("\n") + 1, md5))

# supplementary verification (fresh read)
with open(SUPP, "r", encoding="utf-8") as f:
    supp2 = f.read()
check(supp2.count("## S6. Statement-Status Naming Offset") == 1, "S6 not exactly once")
check(supp2.count("| Theorem 2 (registered-family support-saturated identity) | Remark 2 |") == 1,
      "S6 table row 1 missing")
check(supp2.count("| Theorem 20 (geometric-Brownian passage) | Proposition 20 |") == 1,
      "S6 table row 8 missing")
check(supp2.rstrip("\n").endswith("resolves directly; the main text declares this convention at the\nlayering site."),
      "S6 not at end of file")
print("OK  supplementary S6 verified (%d lines total)" % (supp2.count("\n") + 1))
