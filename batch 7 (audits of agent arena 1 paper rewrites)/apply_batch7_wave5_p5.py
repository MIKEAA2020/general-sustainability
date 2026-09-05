#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wave-5 P5 build: paper5_sampled_governance_v22.md from v21.

Owner directive (wave 5): evaluate the registered follow-ups left behind the
owner gate.  Three v21 declines are re-opened -- each was declined only because
it was "not elevated to the wave-4 docket" or read as a title-level change,
and each has a bounded, presentation-only fix that does not touch the title:

  1. (grok §6 / claude "unify") "sampled governance" (§1) vs "sample-and-hold
     governance" (abstract/keywords/title) -- two names for one architecture.
     The harmonisation grok asked for ("pick one term after first definition")
     cannot be done without a title change (no retitle endorsed), so the
     controlled fix is the fence-and-declare pattern: an equivalence
     declaration at §1's naming sentence.
  2. (claude Title/Abstract note) the abstract's "thirty-plus" vs the three
     "more than thirty" sites -- harmonised to the dominant form.
  3. (claude §3.4 note) Figure 1's caption "four update pairs" -> claude's
     exact wording "four update × channel combinations" (the four are
     forward-Euler/exact x extractive/protective, as the caption's own next
     sentences say).

Non-destructive: three presentation edits + the version-log splice.  No
spectral record, crossing, verdict, or table value changes.
"""
import hashlib
import re
import sys

SRC = "arena agent 1/paper rewrites/paper5_sampled_governance_v21.md"
DST = "arena agent 1/paper rewrites/paper5_sampled_governance_v22.md"

with open(SRC, "r", encoding="utf-8") as f:
    src = f.read()


def sub1(text, old, new, tag):
    n = text.count(old)
    if n != 1:
        sys.exit("FAIL [%s]: anchor occurs %d times (expected 1): %r" % (tag, n, old[:80]))
    return text.replace(old, new, 1)


def check(cond, msg):
    if not cond:
        sys.exit("FAIL [check]: " + msg)


# ---------------------------------------------------------------- Edit 1: abstract count wording
OLD1 = "and a structured search across thirty-plus systems returns zero eligible cases."
NEW1 = "and a structured search across more than thirty systems returns zero eligible cases."

# ---------------------------------------------------------------- Edit 2: §1 term fence
OLD2 = (
    "This paper calls that architecture *sampled governance* — a governance "
    "loop in which state observation and control update occur at discrete "
    "review times, not continuously."
)
NEW2 = (
    "This paper calls that architecture *sampled governance* — a governance "
    "loop in which state observation and control update occur at discrete "
    "review times, not continuously. It is the same architecture the abstract, "
    "the keywords, and the title's second clause name *sample-and-hold "
    "governance*: one object under two names — *sampled governance* names the "
    "institutional loop, *sample-and-hold* its control-theoretic update law — "
    "and the two names are used interchangeably throughout this article."
)

# ---------------------------------------------------------------- Edit 3: Figure 1 caption
OLD3 = "review-interval ranges for the four update pairs, with crossing markers"
NEW3 = "review-interval ranges for the four update × channel combinations (forward-Euler and exact updates on the extractive and protective channels), with crossing markers"

# ---------------------------------------------------------------- Version log
m = re.search(r"^\*Version log \(v21\)\.\*.*$", src, re.M)
if not m:
    sys.exit("FAIL [log]: v21 version log line not found")
VLOG = (
    "*Version log (v22).* Wave-5 owner-directed re-open pass (the registered "
    "follow-ups behind the owner gate, re-evaluated): three v21 declines whose "
    "reasons were wave-scope, not merit. (1, grok §6 / claude unify note) The "
    "two architecture names are fenced as one object: Section 1's naming "
    "sentence now declares that *sampled governance* (§1) and *sample-and-hold "
    "governance* (abstract, keywords, title) name the same architecture — the "
    "institutional name for the loop, the control-theoretic name for its "
    "update law — used interchangeably; the title keeps both, since no retitle "
    "is endorsed, and the audits' reader-confusion concern is answered by the "
    "declaration. (2, claude Title/Abstract note) The abstract's "
    "\u201cthirty-plus\u201d is harmonised to the paper's dominant form "
    "\u201cmore than thirty\u201d (three existing sites unchanged). (3, claude "
    "§3.4 note) Figure 1's caption \u201cfour update pairs\u201d is renamed "
    "\u201cfour update × channel combinations\u201d with the four named "
    "(forward-Euler and exact updates on the extractive and protective "
    "channels) — claude's exact suggested wording, matching the caption's own "
    "next sentences. No spectral record, crossing, verdict, table row, or "
    "recorded value changes; the declined claim-level items (Lemma 2.2's "
    "application to seal predation, the Prop 2.1 demotion, the θ "
    "strong-resonance check) stay declined with their recorded reasons."
)

out = src
out = sub1(out, OLD1, NEW1, "abstract-thirty")
out = sub1(out, OLD2, NEW2, "term-fence")
out = sub1(out, OLD3, NEW3, "fig1-caption")
out = sub1(out, m.group(0), VLOG, "vlog")

# ---------------------------------------------------------------- Checks
def body_of(t):
    return "\n".join(l for l in t.split("\n") if not l.startswith("*Version log"))


src_body, out_body = body_of(src), body_of(out)

check(out_body.count("thirty-plus") == 0,
      "'thirty-plus' survives in body (%d)" % out_body.count("thirty-plus"))
check(out_body.count("more than thirty") == 4,
      "'more than thirty' count != 4 (%d)" % out_body.count("more than thirty"))
check(out_body.count("one object under two names") == 1, "term fence absent")
check(out_body.count("used interchangeably throughout this article") == 1,
      "interchangeability declaration absent")
check(out_body.count("four update × channel combinations") == 1, "caption fix absent")
check(out_body.count("four update pairs") == 0, "'four update pairs' survives")
# the two architecture names keep their sites (counts must not drop)
a, b = src_body.count("sample-and-hold"), out_body.count("sample-and-hold")
check(b >= a, "'sample-and-hold' count dropped %d -> %d" % (a, b))
a, b = src_body.count("sampled governance"), out_body.count("sampled governance")
check(b >= a, "'sampled governance' count dropped %d -> %d" % (a, b))
# title untouched
check(out.split("\n")[0] == src.split("\n")[0], "title changed")
# frozen needles unchanged
for needle in ["1.00035", "6.501", "47.536", "79.143", "2.306", "0.9967",
               "0.9838", "42 annually assessed stocks", "q = 0.1"]:
    a, b = src_body.count(needle), out_body.count(needle)
    check(a == b, "frozen needle %r count %d -> %d" % (needle, a, b))
# Rose / plan date untouched (resolved-by-clock)
for needle in ["Rose (2026)", "2026-09-01"]:
    a, b = src_body.count(needle), out_body.count(needle)
    check(a == b, "clock-resolved needle %r count %d -> %d" % (needle, a, b))
# tables byte-identical: every table row line of v21 survives in v22
src_table_lines = [l for l in src.split("\n") if l.strip().startswith("|")]
out_table_lines = [l for l in out.split("\n") if l.strip().startswith("|")]
missing = [l for l in src_table_lines if l not in out_table_lines]
check(not missing, "table line lost: %r" % (missing[:1],))
check(len(out_table_lines) == len(src_table_lines) + 0,
      "table line count changed %d -> %d" % (len(src_table_lines), len(out_table_lines)))

with open(DST, "w", encoding="utf-8") as f:
    f.write(out)

md5 = hashlib.md5(out.encode("utf-8")).hexdigest()
print("OK  wrote %s (%d lines, md5 %s)" % (DST, out.count("\n") + 1, md5))
