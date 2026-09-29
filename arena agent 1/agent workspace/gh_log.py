import json, urllib.request, re, sys
_tok = open('/home/user/uploads/github_pat.txt').read()
TOK = re.search(r"github_pat_[A-Za-z0-9_]+", _tok).group(0)
OWNER, REPO, BR = "MIKEAA2020", "general-sustainability", "lean-audit-v4"
H = {"Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json"}

for path in sys.argv[1:]:
    url = (f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
           f"?path={urllib.parse.quote(path)}&sha={BR}&per_page=5")
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=H)))
    except urllib.error.HTTPError as e:
        print("FAIL", e.code, path); continue
    print(f"=== {path}  ({len(d)} commits returned)")
    for c in d:
        s = c["commit"]
        print(f"  {c['sha'][:8]}  {s['author']['date'][:10]}  {s['message'].splitlines()[0][:80]}")
    if not d:
        print("  (no commits for this path on branch)")
