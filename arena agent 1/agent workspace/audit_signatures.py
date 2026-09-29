#!/usr/bin/env python3
"""Content signatures: is the family's newest file the same paper as the lead?

A version number alone cannot tell me that paper1_assessment_separation_v63 is
a later draft of arv_v9 rather than a different manuscript. So pull each file
and compare title, section headings, and the density of formal statements.
"""
import base64
import json
import re
import urllib.parse
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
HDRS = {"Authorization": "Bearer " + PAT, "Accept": "application/vnd.github+json",
        "User-Agent": "family-audit"}


def get(path):
    r = urllib.request.Request("https://api.github.com/repos/%s/%s/%s"
                               % (OWNER, REPO, path), headers=HDRS)
    return json.loads(urllib.request.urlopen(r).read().decode())


def body(path):
    d = get("contents/%s?ref=%s" % (urllib.parse.quote(path), BRANCH))
    return base64.b64decode(d["content"]).decode("utf-8", "replace")


def signature(t):
    ti = re.search(r"\\title\s*(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}", t)
    title = " ".join(ti.group(1).split()) if ti else "(no \\title)"
    secs = [" ".join(s.split()) for s in re.findall(
        r"\\(?:section|subsection)\s*(?:\[[^\]]*\])?\s*\{((?:[^{}]|\{[^{}]*\})*)\}", t)]
    thm = len(re.findall(r"\\begin\{(theorem|lemma|proposition|corollary|definition)\}", t))
    words = len(re.findall(r"\b\w+\b", t))
    return title, secs, thm, words


TARGETS = [
    ("LEAD  P1 separation", "arena agent 1/agent workspace/fam/arv_v9.tex"),
    ("LATEST same family?", "arena agent 1/paper rewrites/latex/paper1_assessment_separation_v63.tex"),
    ("LEAD  P2 obstruction", "arena agent 1/agent workspace/fam/obstr_v55.tex"),
    ("LATEST P2", "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v56_Automatica_routes.tex"),
    ("LEAD  P3 ledgers", "arena agent 1/agent workspace/fam/p3_v32.tex"),
    ("LATEST P3", "paper3/latest-2026-09-19/manuscript/paper3_material_ledgers_v50.tex"),
    ("P3 supplement", "paper3/latest-2026-09-19/manuscript/paper3_supplementary_v18.tex"),
    ("P2 supplement", "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v29_supplementary.tex"),
]

tree = get("git/trees/%s?recursive=1" % BRANCH)["tree"]
by_path = {e["path"]: e for e in tree}

print("=" * 100)
for lab, path in TARGETS:
    t = body(path)
    title, secs, thm, words = signature(t)
    print("\n%s   [%s]" % (lab, path.split("/")[-1]))
    print("  size %6.0f KiB   words %6d   formal statements %3d"
          % (by_path[path]["size"] / 1024.0, words, thm))
    print("  title: %s" % title[:150])
    print("  sections (%d):" % len(secs))
    for s in secs[:11]:
        print("     - %s" % s[:96])
    if len(secs) > 11:
        print("     ... %d more" % (len(secs) - 11))

print("\n" + "=" * 100)
print("the A0xx module series (revised_articles/) -- not in the 3-paper inventory at all")
mods = [e for e in tree if e["path"].startswith("revised_articles/")
        and e["path"].endswith("_corrected.tex")]
tot = 0
for e in sorted(mods, key=lambda e: e["path"]):
    t = body(e["path"])
    title, secs, thm, words = signature(t)
    tot += e["size"]
    print("  %-52s %6.0f KiB  %6d words  %3d stmts  %s"
          % (e["path"].split("/")[-1][:52], e["size"] / 1024.0, words, thm,
             title[:58]))
print("  TOTAL %d modules, %.0f KiB" % (len(mods), tot / 1024.0))
