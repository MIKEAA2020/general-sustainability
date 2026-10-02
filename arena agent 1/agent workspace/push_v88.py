#!/usr/bin/env python3
"""paper11 v64: reattach the detached DFO 2009 bibliography tail."""
import base64
import json
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PARENT = "7f89b2d046c9cf5744f86f0ec585720dfda975a2"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT,
        "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}

P = "arena agent 1/agent workspace/"
FILES = [
    (P + "papers/MERGE_PIPELINE_DIAGNOSIS.md",
     "/home/user/papers/MERGE_PIPELINE_DIAGNOSIS.md"),
    (P + "papers/repair_paper11_v64.py",
     "/home/user/papers/repair_paper11_v64.py"),
]

MSG = r"""Record the three terminal repairs and the detector gap they exposed

Completes MERGE_PIPELINE_DIAGNOSIS.md with the three live-head repairs
(paper01 v63 / 8059d2b, paper09 v32 / 86f7d15, paper11 v64 / 7f89b2d) and the
final corpus state.

With the scripts fixed, what remained was legacy damage in files that already
exist. The test for whether a file gets a script fix or a direct repair is
"will it be re-merged?" -- merging always produces a NEW version, so a current
head will not be re-merged and must be repaired directly.

RESULT: 59 .tex files scanned, 32 failing at the start of this work, 12 after
the script fix, 9 now -- and every one of the 9 is a superseded version. All 15
live heads are clean.

paper01 v63 -- two Declarations blocks, one per source. The second is
cross-unit: it names four paper02 scripts and claims they reproduce everything,
which they cannot, since paper01's namespace is entirely calc- (39 labels). One
name that looks like the same error is not: paper2_coverage_audit.py appears in
the BODY too, regenerating paper01's own calc- tables, and paper02 v12 does not
mention it. A stale filename from the unit rename, not contamination.

paper09 v32 -- a three-source merge with three Declarations blocks and six
detached bibliography tails. The tails sorted INDEPENDENTLY of their heads, so
the damage never sat next to itself. Each was reattached against the source
papers as ground truth; a seventh was found by reading because it opens with a
title word and the detector never flagged it. The three Declarations were
integrated, not reduced.

paper11 v64 -- one detached tail, four entries from its head, intact in all
three predecessors.

DETECTOR GAP, recorded because it will bite again. K.split-refs only fires when
a fragment has NO year. Tails carrying a year in the detached half, and tails
that open with a title word rather than a publisher token, are missed. Three of
the seven tails repaired here were invisible to the gate. The rule needs a
second signal: a fragment that is a plausible continuation of another entry
should be reported whether or not it has a year.
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
