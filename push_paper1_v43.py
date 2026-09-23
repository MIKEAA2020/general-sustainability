#!/usr/bin/env python3
import base64, json, urllib.request, urllib.error, urllib.parse, os, sys
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
OWNER, REPO = "MIKEAA2020", "general-sustainability"
BASE = "arena agent 1/paper rewrites/latex"
LATEX = "/home/user/arena agent 1/paper rewrites/latex"
FILES = [
    (f"{BASE}/paper1_assessment_separation_v43.tex", f"{LATEX}/paper1_assessment_separation_v43.tex"),
    (f"{BASE}/paper1_assessment_separation_v43.pdf", f"{LATEX}/paper1_assessment_separation_v43.pdf"),
    (f"{BASE}/paper1_v43_addendum.md", f"{LATEX}/paper1_v43_addendum.md"),
    (f"{BASE}/build_paper1_v43.py", "/home/user/build_paper1_v43.py"),
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
    content = base64.b64encode(open(local, "rb").read()).decode()
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{urllib.parse.quote(remote_path)}"
    st, cur = api("GET", url)
    sha = cur.get("sha") if st == 200 else None
    payload = {"message": f"Add {os.path.basename(local)} (paper1 v43: EMA Declarations + figshare data availability)", "content": content}
    if sha: payload["sha"] = sha
    st2, res = api("PUT", url, payload)
    if st2 in (200, 201):
        print(f"OK  {os.path.basename(local)}"); ok += 1
    else:
        print(f"FAIL {os.path.basename(local)}: {st2} {res.get('message','')}"); sys.exit(1)
print(f"\n{ok}/{len(FILES)} pushed OK")
