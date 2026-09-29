import json, urllib.request, base64, re, urllib.error

TOK = re.search(r"github_pat_[A-Za-z0-9_]+", open('/var/tmp/lean/gs/.git/config').read()).group(0)
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


head = api("GET", f"/repos/{OWNER}/{REPO}/git/ref/heads/{BR}")["object"]["sha"]
print("head", head)

files = [
    ("lean/Formalizations.lean", "/var/tmp/lean/gs/lean/Formalizations.lean"),
    ("lean/Formalizations/P3_FreezeCount.lean", "/var/tmp/lean/gs/lean/Formalizations/P3_FreezeCount.lean"),
    ("arena agent 1/paper rewrites/latex/lean_README_v10.md", "/home/user/lean_README_v10.md"),
    ("arena agent 1/paper rewrites/latex/lean_audit_v34.md", "/home/user/lean_audit_v34.md"),
    ("arena agent 1/paper rewrites/latex/paper2_probabilistic_sufficiency_v12.tex",
     "/var/tmp/lean/gs/arena agent 1/paper rewrites/latex/paper2_probabilistic_sufficiency_v12.tex"),
]
tree = []
for path, src in files:
    c = open(src, 'rb').read()
    b = api("POST", f"/repos/{OWNER}/{REPO}/git/blobs",
            {"content": base64.b64encode(c).decode(), "encoding": "base64"})
    tree.append({"path": path, "mode": "100644", "type": "blob", "sha": b["sha"]})
    print("blob", path, len(c))

t = api("POST", f"/repos/{OWNER}/{REPO}/git/trees", {"base_tree": head, "tree": tree})
print("tree", t["sha"])

msg = """v34: prop:freeze's 2^{|supp b|} proved, and the paper edit applied

1. P3_FreezeCount: strictDrop_length_le -- for every horizon n, the number
of strict decreases of l |-> V_l(b) below n is at most 2^{|supp b|}. The
paper asserts this bound itself, so unlike the Sperner count in
prop:antichain (iii) it could not be skipped. Argument: every value is
b(T) for some T subset of supp(b) (VfamAdm_mem_range -- the max is
attained, and truncating a maximizer to the support preserves its mass);
two strict drops never repeat a value (strictDrop_value_inj, by
VfamAdm_antitone); there are 2^{|supp b|} subsets (subsetsOf_length, v13);
plus a pigeonhole lemma for lists, which the layer lacked. On the
CORRECTED family SfamAdm/VfamAdm.

2. A defect in our own layer, recorded not quietly fixed: v18's
prop_freeze_drop_count bounds the drops by 2^{|univX|} -- its docstring
claims 2^{|supp b|}. The comment over-claims, and lean_README had
propagated it into the prop:freeze row. Corrected in README v10 and
lean_audit_v34.md section 2; P3_Freeze_Noisy_v2.lean left untouched.

3. The paper edit, as paper2_probabilistic_sufficiency_v12.tex (v11
untouched): the three-symbol fix (W^{fb}_k, W_k, W^{bel}_k, with W^{bel}_k
explicitly the analogue of the BLIND W_k), the restated thm:support, a
replacement for the invalid converse (the printed argument treats a
feedback policy as a declared sequence), and the new rem:feedback-strict.
prop:deficit (ii) left untouched -- section 4 of the draft identifies it
as the one place a plausible relabelling would do damage, since its proof
cites prop:degen."""
c = api("POST", f"/repos/{OWNER}/{REPO}/git/commits", {"message": msg, "tree": t["sha"], "parents": [head]})
api("PATCH", f"/repos/{OWNER}/{REPO}/git/refs/heads/{BR}", {"sha": c["sha"]})
print("PUSHED", c["sha"])
