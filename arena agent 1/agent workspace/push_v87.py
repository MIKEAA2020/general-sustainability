#!/usr/bin/env python3
"""paper11 v64: reattach the detached DFO 2009 bibliography tail."""
import base64
import json
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PARENT = "86f7d15eaa1692902996a426bbb6dfe2a3a7a63b"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT,
        "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}

P = "arena agent 1/agent workspace/"
FILES = [
    (P + "papers/paper11_forecasting_baselines_v64.tex",
     "/home/user/papers/paper11_forecasting_baselines_v64.tex"),
    (P + "papers/repair_paper11_v64.py",
     "/home/user/papers/repair_paper11_v64.py"),
]

MSG = r"""paper11 v64: reattach the detached DFO 2009 bibliography tail

The gate reported one fatal finding:

    K.split-refs  L3688  detached tail: no year, and it is the
                         journal/publisher half of an entry whose head is
                         elsewhere

The tail is "Fisheries and Oceans Canada, Ottawa." Its head is the DFO 2009
entry four entries away at L3666. They are not adjacent because the old merge
splitter cut entries at "period + Word, " -- the shape of a publisher line --
and the sort key was the first 24 alphanumeric characters, so the head sorted
under D and the tail sorted under F, independently. The damage does not sit next
to itself, which is why it survived every read-through.

Ground truth is the source chain, where the entry is intact in all three
predecessors (v61 L2382-2383, v62 L2409-2410, v63 L2419-2421):

    DFO, 2009. A fishery decision-making framework incorporating the
    Precautionary Approach. Fisheries and Oceans Canada, Ottawa.

Two edits and nothing else: delete the orphan paragraph, append the tail to the
head. v64 already had one Declarations block and no duplicate references, so
there is no H or L work here.

VERIFIED. Gate: 0 fatal findings (was 1). The 7 remaining L.dup-ref-key warnings
are non-fatal by design -- same author and year with different text, i.e.
distinct works or formatting variants -- and are deliberately left for a human
rather than auto-merged. Compiles with tectonic 0.15.0: exit 0, PDF 1,294,630 B,
0 errors, 0 undefined references.

With this the three live heads that failed the gate are clean: paper01 v63
(8059d2b), paper09 v32 (86f7d15), paper11 v64 (this commit). The corpus goes
from 32 failing files to 9, and all 9 remaining are superseded versions.
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
