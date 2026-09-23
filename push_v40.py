#!/usr/bin/env python3
import base64, json, urllib.request, urllib.error, urllib.parse, os, sys
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
OWNER, REPO = "MIKEAA2020", "general-sustainability"
BASE = "arena agent 1/paper rewrites/latex"
FILES = [
    (f"{BASE}/paper2_obstruction_calculus_v40_Automatica_routes.tex", "/home/user/arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v40_Automatica_routes.tex"),
    (f"{BASE}/paper2_obstruction_calculus_v40_Automatica_routes.pdf", "/home/user/arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v40_Automatica_routes.pdf"),
    (f"{BASE}/paper2_obstruction_calculus_v40_Automatica_routes_supplementary.tex", "/home/user/arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v40_Automatica_routes_supplementary.tex"),
    (f"{BASE}/paper2_obstruction_calculus_v40_Automatica_routes_supplementary.pdf", "/home/user/arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v40_Automatica_routes_supplementary.pdf"),
    (f"{BASE}/paper2_v40_addendum.md", "/home/user/arena agent 1/paper rewrites/latex/paper2_v40_addendum.md"),
    (f"{BASE}/build_paper2_v40.py", "/home/user/build_paper2_v40.py"),
]
def api(method, url, data=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {PAT}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
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
    payload = {"message": f"Add {os.path.basename(local)} (v40: POMDP instance + checkability + recourse example)", "content": content}
    if sha: payload["sha"] = sha
    st2, res = api("PUT", url, payload)
    if st2 in (200, 201):
        print(f"OK  {os.path.basename(local)}"); ok += 1
    else:
        print(f"FAIL {os.path.basename(local)}: {st2} {res.get('message','')}"); sys.exit(1)
print(f"\n{ok}/{len(FILES)} pushed OK")
