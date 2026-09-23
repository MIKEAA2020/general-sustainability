#!/usr/bin/env python3
import base64, json, urllib.request, urllib.error, urllib.parse, os, sys
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
OWNER, REPO = "MIKEAA2020", "general-sustainability"
BASE = "arena agent 1/paper rewrites"
LATEX = f"{BASE}/latex"
FILES = [
    (f"{LATEX}/paper1_assessment_separation_v44.tex", f"{LATEX}/paper1_assessment_separation_v44.tex"),
    (f"{LATEX}/paper1_assessment_separation_v44.pdf", f"{LATEX}/paper1_assessment_separation_v44.pdf"),
    (f"{LATEX}/figs_p1/fig_benchmark_v44.png", f"{LATEX}/figs_p1/fig_benchmark_v44.png"),
    (f"{LATEX}/build_paper1_v44.py", "/home/user/build_paper1_v44.py"),
    (f"{LATEX}/make_benchmark_v44.py", "/home/user/make_benchmark_v44.py"),
    (f"{LATEX}/paper1_readership_audit_v44.md", f"{LATEX}/paper1_readership_audit_v44.md"),
    (f"{BASE}/paper1_figshare_deposit.zip", "/home/user/paper1_figshare_deposit.zip"),
]
def api(method, url, data=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {PAT}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "arena-push")
    body = json.dumps(data).encode() if data is not None else None
    if body: req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, body) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode() or "{}")
ok = 0
for remote_path, local in FILES:
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{urllib.parse.quote(remote_path)}"
    st, cur = api("GET", url)
    payload = {"message": f"Add/update {os.path.basename(local)} (paper1 v44: readership augmentation + benchmark in master deposit)", "content": base64.b64encode(open(local, "rb").read()).decode()}
    if st == 200: payload["sha"] = cur.get("sha")
    st2, res = api("PUT", url, payload)
    if st2 in (200, 201):
        print(f"OK  {os.path.basename(local)}"); ok += 1
    else:
        print(f"FAIL {os.path.basename(local)}: {st2} {res.get('message','')}"); sys.exit(1)
print(f"\n{ok}/{len(FILES)} pushed OK")
