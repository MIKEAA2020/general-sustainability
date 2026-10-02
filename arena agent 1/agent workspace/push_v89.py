#!/usr/bin/env python3
"""Gate fails on live heads only; second tail signal report-only; CRediT template."""
import base64
import json
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PARENT = "71afe13195423728354df486e32163bea89fb840"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT,
        "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}

P = "arena agent 1/agent workspace/"
FILES = [
    (P + "p5/phase0_scan.py",        "/home/user/p5/phase0_scan.py"),
    (P + "p5/scan_continuations.py", "/home/user/p5/scan_continuations.py"),
    (P + "papers/paper09_cod_certification_v32.tex",
     "/home/user/papers/paper09_cod_certification_v32.tex"),
    (P + "papers/paper11_forecasting_baselines_v64.tex",
     "/home/user/papers/paper11_forecasting_baselines_v64.tex"),
    (P + "papers/paper08_governance_delay_v46.tex",
     "/home/user/papers/paper08_governance_delay_v46.tex"),
    (P + "papers/repair_paper11_v64_twdb.py",
     "/home/user/papers/repair_paper11_v64_twdb.py"),
    (P + "papers/repair_paper09_v32_dfo.py",
     "/home/user/papers/repair_paper09_v32_dfo.py"),
    (P + "papers/add_credit.py",     "/home/user/papers/add_credit.py"),
    (P + "papers/OPEN_CONTENT_ITEMS.md",
     "/home/user/papers/OPEN_CONTENT_ITEMS.md"),
    (P + "papers/MERGE_PIPELINE_DIAGNOSIS.md",
     "/home/user/papers/MERGE_PIPELINE_DIAGNOSIS.md"),
]

MSG = r"""Gate fails on live heads only; second tail signal report-only; CRediT template

THE GATE COUNTED TWO DIFFERENT THINGS AND PRINTED THEM AS ONE. --gate did
`bad += len(hits)` -- it counted FINDINGS -- and then printed them as
"N structural failure(s)", while the prose reports counted FILES. A run
reporting "32" and a count of "12 failing files" therefore looked like a
contradiction when they were different units. It now prints both, labelled.

THE GATE FAILED ON FILES NOBODY WILL EVER FIX. Merging always writes a NEW
version, so a superseded version is never re-merged and never repaired. Nine
dead files failing on every run is how a gate trains people to stop reading it.
It now fails only on LIVE HEADS -- the newest version of each paper family,
computed from the filename -- and reports superseded files as informational:

    LIVE HEADS failing  : 0 file(s), 0 finding(s)   <-- exit status
    superseded, ignored : 9 file(s), 21 finding(s)
    scanned             : 59 file(s)

CAVEAT, STATED RATHER THAN PAPERED OVER. The historical figure of 32 does not
fully reconcile. Measured deltas account for 7 of the 11-finding drop: 6 removed
by the three live-head repairs, 1 by the rule I rewrite, and 2 more if the count
predated the v46 repair -- leaving roughly 2 unexplained. Most likely it was
recorded from a partial run mid-turn. Treat the current numbers as the baseline
and disregard 32; it is not reproducible and should not be cited again.

SECOND TAIL SIGNAL, REPORT-ONLY. The shipped K.split-refs fires only when a
fragment has NO year AND opens with one of ~18 hardcoded journal names. Tails
carrying a year, or opening with a title word, are invisible to it. Three of the
seven tails repaired in paper09 v32 were invisible. p5/scan_continuations.py
asks the question the shipped rule does not -- could this fragment stand alone
as a reference? -- and runs report-only so the false-positive rate is measured
before anything is made fatal. Triage over 59 files:

  C:place-tail         20 hits   100% precision, all in superseded files.
                                Safe to promote to fatal.
  B:no-year+no-author  18 hits   ~89%. Two false positives, both
                                "U.S. Geological Survey. National Water
                                Information System..." -- a legitimate
                                year-less government data citation. AUTHORISH
                                does not handle corporate authors with
                                initials. Tighten before promoting.
  A:shipped-rule        8 hits   already fatal.
  E:continuation-word   3 hits   REMOVED. 0-for-3: all three were
                                "von Neumann, J. (1928)...", flagged only for
                                starting with a lowercase nobiliary particle.

IT FOUND A REAL DEFECT THE GATE HAD REPORTED CLEAN. paper11 v64 carried a
SECOND detached pair -- "Texas Water Development Board." (L3761) and "Water Data
for Texas, well 6837203 (J-17)..." (L3778) -- seventeen lines apart, because the
old splitter sorted head and tail independently. The earlier repair joined the
DFO 2009 tail and the gate then said v64 was clean; the same pair had already
been repaired in paper09 v32, which is why it looked done. Repaired.

CREDIT TEMPLATE. Who did what is a fact about people, not about the manuscript:
it cannot be inferred from the .tex and must not be invented. But a bare "to be
completed" placeholder gives the author nothing to fill in and gets skipped at
submission. Both files now carry the full 14-role CRediT taxonomy with blanks
marked. paper09 v32 had the placeholder and gets the template in its place;
paper08 v46 had no CRediT subsection at all and gets one. Neither file declares
\author -- the self-citations read "Abaee, A." but the full name appears nowhere
-- so the name is left as a blank rather than assumed.

OPEN_CONTENT_ITEMS.md tracks the four things a structural detector cannot see:
CRediT, the prose author-contributions paragraph v46 still lacks, the
supplement/declaration questions (all three now resolved and recorded), the
detector gap, and the count caveat.

VERIFIED. All 15 live heads: 0 fatal findings. paper09 (DFO 2016 pair merged to
one, same report 2016/026), paper11 (TWDB pair joined) and paper08 (CRediT
added) all recompile with tectonic 0.15.0: exit 0, 0 errors, 0 undefined
references.
"""


def main():
    r = urllib.request.urlopen(urllib.request.Request(
        BASE + "/commits/" + PARENT, headers=HDRS))
    base_tree = json.load(r)["commit"]["tree"]["sha"]
    print("parent %s" % PARENT)

    tree = []
    for repo_path, local_path in FILES:
        data = open(local_path, "rb").read()
        blob = json.loads(urllib.request.urlopen(urllib.request.Request(
            BASE + "/git/blobs", data=json.dumps(
                {"content": base64.b64encode(data).decode(),
                 "encoding": "base64"}).encode(),
            headers=dict(HDRS, **{"Content-Type": "application/json"}))).read())
        tree.append({"path": repo_path, "mode": "100644",
                     "type": "blob", "sha": blob["sha"]})
        print("  blob %-46s %8d B" % (repo_path.split("/")[-1], len(data)))

    new_tree = json.loads(urllib.request.urlopen(urllib.request.Request(
        BASE + "/git/trees", data=json.dumps(
            {"base_tree": base_tree, "tree": tree}).encode(),
        headers=dict(HDRS, **{"Content-Type": "application/json"}))).read())

    commit = json.loads(urllib.request.urlopen(urllib.request.Request(
        BASE + "/git/commits", data=json.dumps(
            {"message": MSG, "tree": new_tree["sha"], "parents": [PARENT]}).encode(),
        headers=dict(HDRS, **{"Content-Type": "application/json"}))).read())
    print("commit %s" % commit["sha"])

    urllib.request.urlopen(urllib.request.Request(
        BASE + "/git/refs/heads/" + BRANCH, data=json.dumps(
            {"sha": commit["sha"]}).encode(), method="PATCH",
        headers=dict(HDRS, **{"Content-Type": "application/json"}))).read()
    print("updated %s -> %s" % (BRANCH, commit["sha"]))


if __name__ == "__main__":
    main()
