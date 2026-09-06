#!/usr/bin/env python3
"""P2 v12 (wave-8 owner-directed presentation pass).

Changes:
  1. The version-log paragraph before the abstract is removed.
  2. The abstract is tightened from 345 to under 315 words and its
     opening question is recast declaratively: "The necessity side —
     when can one certify that no observation-based policy exists? —
     has lacked a comparable instrument." now reads "The necessity
     side — certifying that no observation-based policy exists — has
     lacked a comparable instrument." (no questions as italicised
     writing). Every mechanism, scope statement, and contrast is
     preserved; the cuts are phrasal (the dropped fibre gloss, the
     compressed Isaacs-condition parenthetical, connectives).
  3. The Introduction's italicised question is recast declaratively
     ("The question this paper addresses is the following. Under an
     incomplete observation structure, when can we *certify that no
     policy works* — ... ?" -> a statement of what the paper
     addresses).
  4. Definition-level version-history narration recast: the
     exists-strategy-for-all-realizations remark loses its "of the
     earlier version was circular ... replaced" clause (the
     quantifier-order rationale is kept, stated as mathematics, not
     as history); the EViab withdrawal loses "at this revision ...
     recorded in the version log" (the named-contrast-class status
     is kept); the symbol-table sentence loses "the fraktur
     information symbols of earlier versions are retired".
  5. Keywords 5 -> 7: "viability kernel" and "output feedback" added.
Fail-loud; byte-reproducible; writes paper2_obstruction_calculus_v12.md.
"""
from __future__ import annotations
import hashlib
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "arena agent 1/paper rewrites"
OLD = SRC / "paper2_obstruction_calculus_v11.md"
NEW = SRC / "paper2_obstruction_calculus_v12.md"

text = OLD.read_text()
orig = text


def rep(old: str, new: str, n: int = 1):
    global text
    assert text.count(old) == n, f"needle x{text.count(old)} (want {n}): {old[:90]!r}"
    text = text.replace(old, new)


# --- 1. remove the version-log paragraph ----------------------------------
m = re.search(r"\*Version log \(v11\)\.\*[^\n]*\n\n", text)
assert m, "version log paragraph not found"
text = text[:m.start()] + text[m.end():]
assert "*Version log" not in text

# --- 2. the abstract: replaced wholesale -----------------------------------
ABSTRACT_OLD = text.split("## Abstract\n", 1)[1].split("\n\n**Keywords:**", 1)[0]
assert ABSTRACT_OLD.startswith("Under perfect measurement"), ABSTRACT_OLD[:60]

ABSTRACT_NEW = """Under perfect measurement the viability kernel — the set of states from which some feedback keeps the system within its constraints — is characterized by tangency conditions; under incomplete observation, the sufficiency direction has a canonical answer in Veliov's output-feedback regulation condition and the estimation-tube reduction. The necessity side — certifying that no observation-based policy exists — has lacked a comparable instrument.

We develop an obstruction calculus — obstruction certificates for the nonviability of every observation-based policy, finitely checkable in the polyhedral and finite-fibre cases and closed-form but conditional elsewhere. The certificates are sound sufficient conditions for nonviability and do not exhaust the complement of the epistemic kernel (the observation-based counterpart of the viability kernel). Five mechanisms are established — two finitely checkable (the polyhedral common-action and finite-fibre certification forms), two closed-form conditional (the exit and timing bounds), and one minimal construction — with a sixth exhibited under a policy-class restriction. The central common-action obstruction shows that when the safe controls of compatible states intersect emptily, no observation-based policy is viable — though every compatible state is individually viable under full information. The further four mechanisms cover a finite-time exit certificate under an Isaacs-type drift condition (the disturbance, chosen along the realized control, forces violation within a computable time), an epistemic-emptiness construction where a constant observation merges states whose admissible controls differ, a delayed-information obstruction with an explicit timing bound, and a certification limit (an exact observation-only certifier exists exactly when safe-set membership is constant on the observation fibres). The exhibited sixth, a certainty-equivalence trap (a fixed state-feedback law applied to the uncorrected observation), can empty the epistemic kernel under a biased observation even when the perfect-information kernel is nonempty.

The calculus is positioned against barrier certificates and estimation tubes, and its consequences for monitoring design — the timing, coarseness, and bias of observation — are drawn."""

rep(ABSTRACT_OLD, ABSTRACT_NEW)
nwords = len(re.findall(r"\S+", ABSTRACT_NEW))
assert nwords < 315, nwords

# --- 3. the Introduction's italicised question -> declarative ---------------
rep("The question this paper addresses is the following. Under an incomplete "
    "observation structure, when can we *certify that no policy works* — that is, "
    "when is the viability problem infeasible for reasons of information rather "
    "than of dynamics?",
    "This paper addresses the necessity side: under an incomplete observation "
    "structure, it develops instruments for certifying that no observation-based "
    "policy is viable — establishing infeasibility for reasons of information "
    "rather than of dynamics.")

# --- 4. Definition-level version-history narration recasts -------------------
rep('(This is the standard exists-strategy-for-all-realizations form; the '
    'qualifier "for every admissible disturbance realization compatible with '
    'the record" of the earlier version was circular — the record is generated '
    'by the realization — and is replaced by the present quantifier order.)',
    '(This is the standard exists-strategy-for-all-realizations form; the '
    'quantifier order is load-bearing, because the record is generated by the '
    'realization — any qualifier conditioning the admissible realizations on '
    'the record would be circular.)')
rep("The existential — non-robust — counterpart $\\mathrm{EViab}_{\\mathcal{I}}"
    "(\\mathcal{V})$ is withdrawn as a Definition-level object at this revision "
    "(its coupled-record semantics, recorded in the version log, was never used "
    "by a theorem) and survives only as the named contrast class of the "
    "a-fortiori caveat below.",
    "The existential — non-robust — counterpart $\\mathrm{EViab}_{\\mathcal{I}}"
    "(\\mathcal{V})$ is retained as a named contrast class only, for the "
    "a-fortiori caveat below; its coupled-record semantics is used by no theorem.")
rep("the fraktur information symbols of earlier versions are retired, and no "
    "other letter serves either role",
    "and no other letter serves either role")

# --- 5. keywords 5 -> 7 ------------------------------------------------------
rep("**Keywords:** viability theory; obstruction certificates; robust viability; "
    "epistemic viability; constrained sustainability",
    "**Keywords:** viability theory; viability kernel; obstruction certificates; "
    "robust viability; epistemic viability; output feedback; constrained "
    "sustainability")

NEW.write_text(text)

# --- verification -------------------------------------------------------------
def abstract_words(t):
    lines = t.split("\n")
    a = next(i for i, l in enumerate(lines) if l.strip() == "## Abstract")
    b = next(i for i in range(a + 1, len(lines)) if lines[i].startswith("## "))
    body = [l for l in lines[a + 1:b] if l.strip() and not l.startswith("**Keywords")
            and not l.startswith("**Mathematics")]
    return sum(len(re.findall(r"\S+", l)) for l in body)

assert abstract_words(text) == nwords < 315, (abstract_words(text), nwords)
kw = next(l for l in text.split("\n") if l.startswith("**Keywords"))
assert len(kw.split(";")) == 7, kw
for needle in ["Veliov", "Isaacs-type", "certainty-equivalence trap",
               "$\\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V})$",
               "observation fibres"]:
    assert needle in text, needle
for banned in ["*Version log", "of the earlier version", "at this revision",
               "recorded in the version log", "earlier versions are retired",
               "when can one certify", "when can we *certify"]:
    assert banned not in text, banned


def table_lines(t):
    return [l for l in t.split("\n") if l.lstrip().startswith("|")]


assert table_lines(text) == table_lines(orig), "table rows changed"

print("P2 v12 written;", len(orig), "->", len(text), "chars")
print("abstract words:", nwords)
print("MD5:", hashlib.md5(text.encode()).hexdigest())
