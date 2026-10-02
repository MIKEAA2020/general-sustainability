#!/usr/bin/env python3
"""Promote K.place-tail to fatal; semantic duplicate test; record the audit trail.

Implements the four approved decisions from review:
  C  -> promoted to fatal as K.place-tail (20 hits, 100% precision)
  B  -> report-only, AUTHORISH fixed for corporate authors (18 -> 15 hits)
  E  -> dropped (0-for-3)
  DFO 2016 -> merged, and byte-identity REPLACED by same_work()
"""
import base64
import json
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PARENT = "62a9f3421dc2f3acd35400035b44b5e197ba1cfe"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT,
        "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}

P = "arena agent 1/agent workspace/"
FILES = [
    (P + "p5/phase0_scan.py",        "/home/user/p5/phase0_scan.py"),
    (P + "p5/scan_continuations.py", "/home/user/p5/scan_continuations.py"),
    (P + "papers/OPEN_CONTENT_ITEMS.md",
     "/home/user/papers/OPEN_CONTENT_ITEMS.md"),
    (P + "papers/MERGE_PIPELINE_DIAGNOSIS.md",
     "/home/user/papers/MERGE_PIPELINE_DIAGNOSIS.md"),
]

MSG = r"""Promote K.place-tail to fatal; semantic duplicate test; record the audit trail

C -- PROMOTED TO FATAL as K.place-tail. 20 hits across 59 files, 100% precision,
every one a genuine detached publisher/city tail. It has ZERO live-head hits, so
it does not change the exit status today; it is a guard against future merges,
which is the point of promoting it.

B -- STAYS REPORT-ONLY. Its two false positives were both "U.S. Geological
Survey. National Water Information System, site 08168710, Comal Springs at New
Braunfels, Texas." in paper11 v64 and paper11b v2 -- a legitimate year-less
government data citation. AUTHORISH did not handle corporate authors with
initials ("U.S."), so it now defers to a CORPORATE list in phase0_scan, which
keeps the two rules in agreement. 18 hits -> 15. Re-measure before promoting;
promoting it now would fail live heads on a non-defect.

E -- DROPPED. 0-for-3: all three hits were "von Neumann, J. (1928)...", flagged
only for opening with a lowercase nobiliary particle.

ONE CORRECTION MADE WHILE PROMOTING C, WORTH RECORDING. The CORPORATE guard was
initially applied to K.place-tail as well, and that was wrong: it suppressed
five GENUINE tails -- "Cambridge University Press, Cambridge.", "Eurostat,
Luxembourg.", "OECD Publishing, Paris.", "Princeton University Press, Princeton,
NJ.", "Fisheries and Oceans Canada, Ottawa." -- because publisher names end in
the same words institutional authors do. PLACE_TAIL alone is 20/20. The guard
now applies ONLY to the no-year/no-author signal, where the USGS false positive
actually arose. A guard added to fix one signal can silently blind another.

BYTE-IDENTITY REPLACED BY same_work(). The DFO 2016 merge was approved on
judgment, but the judgment exposed the test, not the entry: byte-identity is a
proxy, and the wrong one. Two entries citing one report differ in citation style
and nothing else, so the proxy says "they differ" and leaves a human to notice
that the report number is identical. Identity is now decided semantically -- a
shared DOI, a shared report number, or the same year plus >=60% title-token
overlap:

    DFO, 2016. ... (NAFO Divs. 2J3KL) ... Rep.~2016/026.
    DFO (2016). ... (NAFO 2J3KL). \emph{...} 2016/026.

Not byte-identical. Same report, 2016/026. One work, merged.

L.dup-ref-key now fires only when two entries are the same WORK, so the finding
reads "merge these" instead of "check whether these conflict". Corpus findings
fell 32 -> 18. Two different Abaee 2026 papers correctly do NOT match.

THE LESSON, RECORDED AS A STANDING RULE IN OPEN_CONTENT_ITEMS.md. The gate's
clean verdict has now been wrong twice in two turns: once because --gate counted
FINDINGS and printed them as "failure(s)" while the prose counted FILES, and once
because K.split-refs could not see the Texas Water Development Board pair in
paper11 v64 that the report-only detector found immediately. Both times reading
caught what the gate did not. So:

  - a clean verdict must NAME THE CHECKS that produced it; "clean" from a single
    gate is not a claim to make or accept;
  - the report-only detector runs on live heads as a ROUTINE, not only after
    repairs;
  - the corpus is not audited until the reading pass and the detector pass
    agree. Neither alone is sufficient.

ALSO RECORDED: the unexplained count delta. Measured deltas account for 7 of the
11-finding drop -- 6 removed by the three live-head repairs, 1 by the rule I
rewrite, 2 more if the count predated the v46 repair -- leaving ~2 unaccounted.
The figure of 32 is not reproducible and must not be cited again; the reasons
why the count changed are now in the file rather than only in conversation.

VERIFIED, WITH EVERY CHECK NAMED:
  check 1  structural gate, fatal classes H/I/J/K/L: 0 findings across 15 heads
  check 2  report-only tail detector on live heads:  0 candidate fragments
  check 3  tectonic 0.15.0, all three modified papers: exit 0, 0 errors,
           0 undefined references (paper09 1,488,479 B; paper11 1,294,643 B;
           paper08 1,191,121 B)
  gate     LIVE HEADS failing 0 file(s)/0 finding(s);
           superseded, ignored 9 file(s)/34 finding(s); scanned 59 file(s)

CRediT: name left blank in both files. Neither declares \author; the
self-citations read "Abaee, A." but the preferred byline form is not asserted
anywhere in the manuscript, and the git identity is not a basis for guessing it.
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
