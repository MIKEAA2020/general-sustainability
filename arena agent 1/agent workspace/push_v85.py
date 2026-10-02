#!/usr/bin/env python3
"""paper01 v63: collapse the duplicate Declarations, drop the paper02 block."""
import base64
import json
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PARENT = "d846f6cec4b0177d10de9595189e1d6e77475be5"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT,
        "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}

P = "arena agent 1/agent workspace/"
FILES = [
    (P + "papers/paper01_obstruction_calculus_v63.tex",
     "/home/user/papers/paper01_obstruction_calculus_v63.tex"),
    (P + "papers/repair_paper01_v63.py",
     "/home/user/papers/repair_paper01_v63.py"),
]

MSG = r"""paper01 v63: collapse the duplicate Declarations, drop the paper02 block

THE FILE CARRIED TWO DECLARATIONS BLOCKS, one per merge source:

  L2117  \section*{Declarations}    -- paper01's own, one line, \quad-joined
  L2120  \subsection*{Declarations} -- paper02's, \subsection*-itemised

THE SECOND IS CROSS-UNIT. Its Code availability names four paper02 scripts
(paper2_probabilistic_sufficiency_v14_verification.py,
paper2_belief_state_v2_verification.py, paper2_stochastic_selector_v2_verify.py,
paper2_belief_state_figures.py) and claims they "reproduce all values, bounds,
thresholds, figures, and tabulated entries verbatim". They cannot: paper01 v63's
label namespace is entirely `calc-` -- 39 labels across calc-prop, calc-thm,
calc-rem, calc-tab, calc-fig, calc-ex, calc-def, calc-op, calc-cor -- with no
`suff-` labels and no paper02 body. The claim is false in this file, so the
block is dropped.

ONE NAME THAT LOOKS LIKE THE SAME ERROR AND IS NOT. Block 1 names
`paper2_coverage_audit.py`, which reads as contamination but is not: the same
name appears in the BODY at L1775 ("The audit is reproduced by the script
\texttt{paper2\_coverage\_audit.py} ... which regenerates
Table~\ref{calc-tab:coverage} and Figure~\ref{calc-fig:coverage} verbatim"), and
those are paper01's own labels. paper02 v12 does not mention the script at all.
It is a STALE FILENAME left by the unit rename -- the same class as the paper08
v42/43/44 pointer, not cross-unit content. Renaming it is a source-level change
that would have to be made in the body too, so it is left alone and recorded.

NOTHING IS INVENTED. Block 1 is kept intact; the only thing folded in from block
2 is the one sentence block 1 lacked, the fuller AI declaration ("The author
reviewed and edited outputs and takes responsibility for the final work.").

VERIFIED. Gate: 0 fatal, 0 non-fatal findings (was 1 fatal). One Declarations
block, one \end{document}, zero paper02 script references, calc- labels intact.
Compiles with tectonic 0.15.0: exit 0, PDF 478,150 B, 0 errors, 0 undefined
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
    return commit["sha"]


if __name__ == "__main__":
    main()
