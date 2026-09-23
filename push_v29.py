#!/usr/bin/env python3
import base64, json, urllib.request, urllib.error, urllib.parse, os, sys

PAT = open("/home/user/uploads/github_pat.txt").read().strip()
OWNER = "MIKEAA2020"
REPO = "general-sustainability"
BASE = "arena agent 1/paper rewrites/latex"

FILES = [
    "paper2_obstruction_calculus_v29_Automatica_condensed.tex",
    "paper2_obstruction_calculus_v29_Automatica_condensed.pdf",
    "paper2_obstruction_calculus_v29_supplementary.tex",
    "paper2_obstruction_calculus_v29_supplementary.pdf",
]
LOCAL_DIR = "/home/user/arena agent 1/paper rewrites/latex"

def api(method, url, data=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {PAT}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "arena-push")
    body = None
    if data is not None:
        body = json.dumps(data).encode()
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, body) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode() or "{}")

ok = 0
for name in FILES + ["build_paper2_v29_automatica.py"]:
    local = os.path.join(LOCAL_DIR, name) if name in FILES else os.path.join("/home/user", name)
    content = base64.b64encode(open(local, "rb").read()).decode()
    remote_path = f"{BASE}/{name}"
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{urllib.parse.quote(remote_path)}"
    st, cur = api("GET", url)
    sha = cur.get("sha") if st == 200 else None
    payload = {"message": f"Add {name} (condensed Automatica-format v29 + supplementary)",
               "content": content}
    if sha:
        payload["sha"] = sha
    st2, res = api("PUT", url, payload)
    if st2 in (200, 201):
        print(f"OK  {name}  (blob sha {res['content']['sha'][:12]})")
        ok += 1
    else:
        print(f"FAIL {name}: {st2} {res.get('message','')}")
        sys.exit(1)

print(f"\n{ok}/{len(FILES)+1} pushed OK")
