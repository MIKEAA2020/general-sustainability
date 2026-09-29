#!/usr/bin/env python3
"""Which manuscript is actually the latest of its family?

The 3-paper plan names a "lead" version to build each paper from. The
repository holds 442 .tex files in 157 families, several of which have moved
past the version the plan names. Anything the plan prunes is fine to prune only
if the lead really is the newest content. Sizes come from one trees call, so no
file body is downloaded.
"""
import base64
import json
import re
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


import urllib.parse  # noqa: E402  (used above)

tree = get("git/trees/%s?recursive=1" % BRANCH)["tree"]
tex = [e for e in tree if e["path"].endswith(".tex")
       and not re.search(r"hyphen|texmf|tectonic", e["path"], re.I)]
print("tracked .tex: %d" % len(tex))


def fam_of(p):
    b = p.split("/")[-1]
    m = re.match(r"^(.*?)_v(\d+)", b)
    return (m.group(1), int(m.group(2))) if m else (b[:-4], -1)


fams = {}
for e in tex:
    s, v = fam_of(e["path"])
    cur = fams.get(s)
    if cur is None or (v, e["size"]) > (cur[0], cur[1]):
        fams[s] = (v, e["size"], e["path"])

# the leads named in FAMILY_CONSOLIDATION_PLAN.md
LEADS = {
    "P2 obstruction": ("obstr", 55, 143 * 1024),
    "minimax duals": ("minimax", 11, 41 * 1024),
    "P1 separation": ("arv", 9, 45 * 1024),
    "P5 sample-and-hold": ("p5", 47, 131 * 1024),
    "P4 governance delay": ("p4", 41, 190 * 1024),
    "E2 cod": ("paperE2_cod_intervention", 29, 110 * 1024),
    "ARV applied regime": ("applied_regime_viability", 9, 45 * 1024),
    "P3 typed ledgers": ("p3", 32, 163 * 1024),
    "E3 Edwards forecast": ("e3", 16, 65 * 1024),
    "E1 baselines": ("e1", 60, 137 * 1024),
    "E4 elevation": ("e4", 15, 61 * 1024),
    "welfare/support": ("ws", 17, 73 * 1024),
}
# where each family is continued under a different filename
CROSS = {
    "obstr": "paper2_obstruction_calculus",
    "minimax": "minimax_dual_certificates",
    "p5": "paper5_sampled_governance",
    "p4": "paper4_delay_dynamics",
    "p3": "paper3_material_ledgers",
    "e3": "paperE3_edwards_forecast_ladder",
    "e1": "paperE1_cod_forecast_ladder",
    "e4": "paperE4_edwards_intervention",
    "arv": "paper1_assessment_separation",
}

print("\n%-24s %-28s %8s   %s" % ("inventory lead", "family latest", "size", "verdict"))
print("-" * 100)
gaps = []
for lab, (stem, ver, sz) in sorted(LEADS.items()):
    v, s, p = fams.get(stem, (-1, 0, ""))
    cross = CROSS.get(stem)
    cv, cs, cp = fams.get(cross, (-1, 0, "")) if cross else (-1, 0, "")
    latest_v, latest_s, latest_p = max(((v, s, p), (cv, cs, cp)), key=lambda t: (t[0], t[1]))
    verdict = "OK"
    if latest_v > ver:
        verdict = "BEHIND by %d versions" % (latest_v - ver)
        gaps.append((lab, stem, ver, latest_v, latest_p, latest_s))
    elif cross and cv > ver:
        verdict = "BEHIND (cross-named)"
    print("%-24s %-28s %8.0f KiB  %s" % (
        "%s v%d" % (stem, ver), (latest_p.split("/")[-1][:28] if latest_p else "MISSING"),
        latest_s / 1024.0, verdict))

print("\n=== leads whose family has moved on ===")
for lab, stem, ver, lv, p, s in gaps:
    print("  %-22s lead v%-3d -> latest v%-3d  %7.0f KiB  %s"
          % (lab, ver, lv, s / 1024.0, p))
if not gaps:
    print("  none")
