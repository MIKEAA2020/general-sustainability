"""Deeper granular loss check.

(1) Numeric-dust diff: which numeric findings/quantities are unique to v20
    (present as a number token) and absent from v21?
(2) Sentence-level condensation check at a LOWER coverage threshold.
"""
import re
from pathlib import Path

_WORD = re.compile(r"[a-z0-9]+")
NUM = re.compile(r"\d+(?:\.\d+)?(?:e-?\d+)?")


def norm(s):
    s = re.sub(r"[`*_#~^|\[\]{}]", " ", s)
    s = s.replace("\u2014", " ").replace("\u2013", " ").replace("\u2003", " ")
    return " ".join(_WORD.findall(s.lower()))


def sent(s):
    # split on sentence-ish boundaries
    return [x.strip() for x in re.split(r"(?<=[.:;]) ", s) if x.strip()]


def main():
    v20 = Path("data/revisions/IMPLEMENTED_revision_ECOMOD_v20.md").read_text()
    v21 = Path("data/revisions/IMPLEMENTED_revision_ECOMOD_v21.md").read_text()
    n20 = " ".join(((normalize if False else norm)(l) for l in v20.splitlines()))
    n21 = norm(v21)

    # --- numeric dust unique to v20 ---
    nums20 = set(NUM.findall(norm(v20)))
    nums21 = set(NUM.findall(norm(v21)))
    uniq20 = sorted(nums20 - nums21)
    print("=== Numeric tokens present in v20 but NOT in v21 ===")
    # filter out trivial/large/version numbers
    interesting = [u for u in uniq20 if len(u) >= 3 and not u.startswith(("00","0-"))][:120]
    print(", ".join(interesting[:120]))
    print("  total unique-to-v20 number tokens:", len(uniq20))

    # --- sentence-level coverage at lower threshold ---
    print("\n=== v20 sentences with LOW v21 token coverage (>=0.34) ===")
    v21tok = set(_WORD.findall(norm(v21)))
    found = []
    for line in v20.splitlines():
        s = norm(line)
        if len(s) < 24:
            continue
        for se in sent(s):
            if len(se) < 24:
                continue
            t = _WORD.findall(se)
            if not t:
                continue
            cov = len(set(t) & v21tok) / len(set(t))
            if cov < 0.45:
                found.append((cov, se))
    found.sort()
    seen = set()
    for cov, se in found[:90]:
        k = se[:50]
        if k in seen:
            continue
        seen.add(k)
        print(f"[{cov:.2f}] {se[:170]}")


if __name__ == "__main__":
    main()
