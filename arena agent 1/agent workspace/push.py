import json, urllib.request, base64, re, urllib.error, sys

# token: persisted under /home/user/uploads (survives /var/tmp wipes)
_tok = open('/home/user/uploads/github_pat.txt').read()
TOK = re.search(r"github_pat_[A-Za-z0-9_]+", _tok).group(0)
OWNER, REPO, BR = "MIKEAA2020", "general-sustainability", "lean-audit-v4"
H = {"Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
     "X-GitHub-Api-Version": "2022-11-28"}


def api(m, p, b=None, retry=True):
    d = None if b is None else json.dumps(b).encode()
    r = urllib.request.Request(f"https://api.github.com{p}", data=d,
                               headers={**H, "Content-Type": "application/json"}, method=m)
    try:
        return json.load(urllib.request.urlopen(r))
    except urllib.error.HTTPError as e:
        print("ERR", m, p, e.code, e.read().decode()[:300])
        if retry and e.code == 422:
            return api(m, p, b, retry=False)
        raise


# usage: python3 push.py <msgfile> path=local  path=local ...
msgfile = sys.argv[1]
pairs = []
for a in sys.argv[2:]:
    rp, lp = a.split("=", 1)
    pairs.append((rp, lp))

head = api("GET", f"/repos/{OWNER}/{REPO}/git/ref/heads/{BR}")["object"]["sha"]
print("parent", head)
tree = []
for rp, lp in pairs:
    c = open(lp, 'rb').read()
    b = api("POST", f"/repos/{OWNER}/{REPO}/git/blobs",
            {"content": base64.b64encode(c).decode(), "encoding": "base64"})
    tree.append({"path": rp, "mode": "100644", "type": "blob", "sha": b["sha"]})
    print("blob", rp, len(c))
t = api("POST", f"/repos/{OWNER}/{REPO}/git/trees", {"base_tree": head, "tree": tree})
c = api("POST", f"/repos/{OWNER}/{REPO}/git/commits",
        {"message": open(msgfile).read(), "tree": t["sha"], "parents": [head]})
api("PATCH", f"/repos/{OWNER}/{REPO}/git/refs/heads/{BR}", {"sha": c["sha"]})
print("PUSHED", c["sha"])
