#!/usr/bin/env python3
"""paper09 v32: rebuild 6 detached bibliography tails; collapse 3 Declarations."""
import base64
import json
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PARENT = "8059d2b8a9d0a0336dbfc43f51f98b9aaf27df44"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT,
        "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}

P = "arena agent 1/agent workspace/"
FILES = [
    (P + "papers/paper09_cod_certification_v32.tex",
     "/home/user/papers/paper09_cod_certification_v32.tex"),
    (P + "papers/repair_paper09_v32.py",
     "/home/user/papers/repair_paper09_v32.py"),
]

MSG = r"""paper09 v32: rebuild 6 detached bibliography tails; collapse 3 Declarations

v32 IS A THREE-SOURCE MERGE (paper09 cod + paper09b ARV + paper10b Edwards) and
it carried three separate Declarations blocks, one per source, plus a
bibliography damaged by the old reference splitter.

PART 1 -- BIBLIOGRAPHY. The old splitter cut entries at "period + Word, ", which
is the shape of a publisher line. Six tails were detached from their heads, and
because the sort key was the first 24 alphanumeric characters, each tail was
then sorted INDEPENDENTLY of its head. "Aubin, J.-P., 1991. Viability Theory."
stayed under A while its publisher "Birkhaeuser, Boston." sorted under B, four
entries away. That is why this was never visible as adjacent damage.

Each tail is reattached to the head it was cut from, using the SOURCE papers
(paper09 v30/v31, paper09b v2, paper10b v1) as ground truth for the intact
entry. Nothing is guessed:

  L4103  Birkhaeuser, Boston.            -> Aubin 1991, \emph{Viability Theory}.
  L4105  Birkhaeuser, Boston.            -> DELETED: a second identical orphan
                                            with no head of its own. Two sources
                                            carried Aubin, the heads
                                            de-duplicated to one, both tails
                                            survived. This was the L.dup-ref.
  L4142  Edwards Aquifer Authority,      -> Edwards Aquifer Authority, 2024,
         San Antonio, TX.                   "Managing the Edwards Aquifer..."
  L4146  Edwards Aquifer Authority,      -> Edwards Aquifer Recovery
         San Antonio, TX.                   Implementation Program, 2021,
                                            \emph{Habitat Conservation Plan}.
  L4148  Fisheries and Oceans Canada,    -> DFO, 2009, "...Precautionary
         Ottawa.                            Approach."
  L4150  Geological Survey Circular      -> Alley et al. 1999, "...Ground-Water
         1186, Denver, CO.                  Resources}. U.S." -- the head ended
                                            in a dangling "U.S." that only made
                                            sense once the tail went back.
  L4243  Water Data for Texas, well      -> "Texas Water Development Board."
         6837203 (J-17)                     Found late: it opens with a title
                                            word, not a publisher token, so the
                                            detector never flagged it.

DFO 2016 appears twice in one paragraph in the two citation styles of the two
sources that carry it. Split into two entries and deliberately NOT merged --
conservative de-duplication -- so it stays visible as non-fatal L.dup-ref-key.

PART 2 -- DECLARATIONS. Three blocks, each belonging to a different constituent
and each carrying live content, so this is an integration, not a deletion:

  A COD      Data availability (wave_e_cod runners, N=20,000, B=2000), CRediT,
             competing interest, funding, Code availability
             (paperE2_cod_intervention_v29_*), AI declaration
  B ARV      Funding, competing interests, Data availability (calibration
             record), Code availability
             (applied_regime_viability_v9_verification.py,
             paper2_arv_record_figure_v1.py), AI declaration
  C Edwards  Data Availability Statement (J-17, recharge, pumpage, frozen
             protocol 2026-08-26, campaign_e4_elevation.py, e4_audit_layer.py),
             funding, competing interests, Code availability
             (paperE4_edwards_intervention_v16_verification.py), AI declaration

Collapsed to one \section*{Declarations}. Data availability and Code
availability keep all three statements under lead-ins naming each constituent,
because they describe different data and different scripts. Funding and
competing interests are stated once -- all three agreed. The AI declaration is
identical in all three and is stated once. CRediT is kept as the placeholder it
is: it must be written, not invented.

VERIFIED. Gate: 0 fatal findings (was 4). Reference list: 51 entries, 0 detached
tails (was 57 entries, 6 tails). One Declarations block, one real \end{document}
-- the other two occurrences are inside % comments describing why the file was
split and are not LaTeX. Compiles with tectonic 0.15.0: exit 0, PDF 1,487,432 B,
0 errors, 0 undefined references.
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
