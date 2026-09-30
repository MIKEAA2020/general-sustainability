#!/usr/bin/env python3
"""Commit the v29o files on top of the REMOTE tip.

The local repo has diverged: local HEAD is a restore-era commit (863142e) that
is not on the remote, whose tip is 1052768b8e. Rather than force-push or merge
from a shallow clone with missing blobs, this builds one commit directly on the
remote tip through the Git data API.
"""
import base64
import json
import os
import urllib.error
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT, "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}

FILES = [
    ("arena agent 1/agent workspace/papers/paper07_sampled_governance_v50.tex",
     "/home/user/papers/paper07_sampled_governance_v50.tex"),
    ("arena agent 1/agent workspace/papers/paper08_governance_delay_v45.tex",
     "/home/user/papers/paper08_governance_delay_v45.tex"),
    ("arena agent 1/agent workspace/papers/PAPERS_7_8_BAR_REMEDIATION.md",
     "/home/user/papers/PAPERS_7_8_BAR_REMEDIATION.md"),
]

MSG = """Papers 7 and 8: prior-art sections added; paper 8's 18 results converted to theorem environments

WHY THESE TWO. Of the 15 current papers, 12 met the top-journal bar. Papers 7 and 8
did not, for the same fixable reason: NEITHER HAD A PRIOR-ART SECTION. Paper 8 had a
second defect -- its 18 numbered results were written as bold prose
(\textbf{Theorem 6.1 (...).}) rather than in labelled theorem environments.
Neither paper had ever been LaTeX-compiled before this turn.

COMPILE BASELINE ESTABLISHED FIRST:
    paper07 v49 -> 37 pp, 267,319 B, 0 errors, 0 undefined refs
    paper08 v43 -> 46 pp, 335,706 B, 0 errors, 0 undefined refs
Both compile cleanly. (An earlier run reported paper 7 as "2 pages" -- that was
purely \includegraphics aborting on missing figure stubs, not a structural defect.)

PAPER 8: 18 RESULTS CONVERTED TO THEOREM ENVIRONMENTS (v43 -> v45).
The source used no \newtheorem at all. Two dead ends before the working solution:
  1 \newtheorem{theorem}{Theorem}[section] FAILED. The preamble sets
    \setcounter{secnumdepth}{-1}, so the section counter never steps and every
    result rendered as "Theorem 0.1", "Corollary 0.2", ... -- 30 phantom results
    instead of 18.
  2 \newtheorem* FAILED. It wraps the optional argument in parentheses, giving
    "Corollary (2.1(Boundedness and global continuation))".
WORKING SOLUTION: a shared counter with a manually-set printed number --
    \newtheorem{theorem}{Theorem} plus [theorem]-shared lemma/proposition/
    corollary/remark, \newcommand{\resultnum}{}, \renewcommand{\thetheorem}{\resultnum},
    then \renewcommand{\resultnum}{6.1} before each \begin{theorem}...\label{thm:6-1}.
This reproduces the paper's existing manual numbering EXACTLY (verified 18/18
distinct results identical to baseline, zero "Theorem 0.x" artefacts) while making
\label/\ref work -- \ref{thm:6-1} prints "6.1".
\theoremstyle{definition} was chosen deliberately: the source wraps every statement
in \emph{...}, and under the default plain style that would flip the emphasis to
upright. Split: 5 theorems, 5 propositions, 4 corollaries, 2 lemmas, 2 remarks.
Statement ends were found by locating \emph{Proof.}; the four results without proofs
(Remark 5.1, Corollary 5.1, Proposition 6.1, Remark 7.1) end at the next heading.

BUG CAUGHT DURING THE CONVERSION. Applying all \begin{...} replacements first and
then all \end{...} insertions corrupted the text -- replacements change string
length, so the pre-computed insertion offsets were stale. It split a word: "for as
long as it ex|ists." with \end{theorem} wedged inside. FIX: perform each result's
replacement and insertion as ONE ATOMIC OPERATION, processed in reverse order.

PRIOR ART ADDED.
  Paper 7 (\subsection{Related work}, 4 strands): sampled-data control; periodic
  review as practice and the interval as a design variable; the continuous-delay
  literature and the substitution this paper questions; position.
  Paper 8 (\subsubsection{1.4 Related work}, 5 strands): delays in population
  dynamics; informational/knowledge delay; management delay as a cost; where this
  paper departs; certification.

ALL CITATIONS VERIFIED AGAINST CROSSREF (DOI lookup), NOT WRITTEN FROM MEMORY:
  Shertzer & Prager 2007, ICES JMS 64:149-159, doi:10.1093/icesjms/fsl005
  Brown, Fulton, Possingham & Richardson 2012, Ecol. Appl. 22:298-310, doi:10.1890/11-0419.1
  Karlsson & Gilek 2020, Ambio 49:1067-1075, doi:10.1007/s13280-019-01265-z
  Hocherman, Trop & Ghermandi 2025, Ambio 54:2042-2059, doi:10.1007/s13280-025-02211-y
  Butterworth 2007, ICES JMS 64:613-617, doi:10.1093/icesjms/fsm003
  Butterworth & Punt 1999, ICES JMS 56:985-998, doi:10.1006/jmsc.1999.0532
  Punt, Butterworth, de Moor, De Oliveira & Haddon 2016, Fish Fish. 17:303-334, doi:10.1111/faf.12104
  Adamson & Hilker 2020, Theor. Ecol. 13:425-434, doi:10.1007/s12080-020-00462-x
  Chen & Francis 1995, Optimal Sampled-Data Control Systems, Springer
Nine new entries for paper 7, four for paper 8, each inserted in correct
alphabetical position in the flat hand-formatted reference lists (neither file uses
\bibitem).

THE SUBSTANTIVE POSITIONING. Paper 8's novelty is now stated against the literature
rather than merely asserted. The governance-delay literature uniformly treats delay
as a cost -- more is worse, the question is how much is tolerable. Paper 8's central
finding is DIFFERENT IN KIND: under the mobilising rule, INTERMEDIATE delay
stabilises, within a window bracketed by two interval-certified subcritical Hopf
crossings. Because the window is bounded above, this localises the range over which
the literature's monotonicity holds rather than contradicting it. The 2025 review's
own methodological call -- that response lags must be decoupled from ecosystem lags
-- is met by construction, since these models carry governance delay and no
ecological delay. Paper 7's positioning is that its question is PRIOR to the delay
literature's: whether substituting a continuous lag for a sampled review is
admissible at all. Sections 3.3 and 4.1 show it is not.

RESULT:
    paper07_sampled_governance_v50.tex -> 38 pp (was 37), 274,064 B, 0 errors, 0 undefined
    paper08_governance_delay_v45.tex   -> 47 pp (was 46), 341,947 B, 0 errors, 0 undefined
Both verified by PDF text extraction: Related work heading present, new in-text
citations present, and paper 8's 18 results numbered identically to baseline.
"""


def api(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(BASE + path, data=data, headers=HDRS,
                                 method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print("HTTP %d on %s %s\n%s" % (e.code, method, path,
                                        e.read().decode()[:400]))
        raise


base = api("GET", "/branches/" + BRANCH)["commit"]["sha"]
print("base commit: %s" % base[:10])
base_tree = api("GET", "/git/commits/" + base)["tree"]["sha"]

tree = []
for path, local in FILES:
    blob = api("POST", "/git/blobs",
               {"content": base64.b64encode(open(local, "rb").read()).decode(),
                "encoding": "base64"})
    tree.append({"path": path, "mode": "100644", "type": "blob",
                 "sha": blob["sha"]})
    print("  blob %s  %7d B  %s" % (blob["sha"][:8],
                                    os.path.getsize(local), path.split("/")[-1]))

new_tree = api("POST", "/git/trees", {"base_tree": base_tree, "tree": tree})
commit = api("POST", "/git/commits",
             {"message": MSG, "tree": new_tree["sha"], "parents": [base]})
api("PATCH", "/git/refs/heads/" + BRANCH, {"sha": commit["sha"]})
print("pushed: %s" % commit["sha"][:10])
