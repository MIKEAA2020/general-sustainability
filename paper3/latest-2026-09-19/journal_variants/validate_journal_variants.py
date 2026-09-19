#!/usr/bin/env python3
"""Validation gate for the journal-specific cuts and the JIE submission package."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent


def words(text):
    text = re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$", " ", text, flags=re.S)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!?\[[^]]*\]\([^)]*\)", " ", text)
    return len(re.findall(r"\b[\wÀ-ÿ][\wÀ-ÿ’'’-]*\b", text))


def body_words(path):
    text = path.read_text()
    marker = text.index("## References")
    return words(text[:marker])

rows = []
for name, limit in (("paper3_JIE_submission_v1.md", 6000), ("paper3_EE_submission_v1.md", 8000)):
    p = ROOT / name
    if not p.exists():
        raise SystemExit(f"missing {p}")
    text = p.read_text()
    n = body_words(p)
    required = ["material", "depletion"]
    if name == "paper3_JIE_submission_v1.md":
        required += ["supplementary material", "Abaee (2026a)", "Abaee (2026b)",
                     "10.6084/m9.figshare.33942469", "10.6084/m9.figshare.33942487"]
    missing = [x for x in required if x.lower() not in text.lower()]
    rows.append({"file": name, "body_words_math_excluded": n, "limit": limit,
                 "within_limit": n <= limit, "missing_required_terms": missing,
                 "lines": len(text.splitlines())})
    if n > limit:
        raise SystemExit(f"{name}: {n} body words exceeds {limit}")
    if missing:
        raise SystemExit(f"{name}: missing {missing}")

main_tex = ROOT / "rendered" / "paper3_JIE_submission_v1.tex"
supp = ROOT / "rendered" / "paper3_JIE_supplement_v1.tex"
cover = ROOT / "JIE_cover_letter_v1.md"
cover_tex = ROOT / "rendered" / "JIE_cover_letter_v1.tex"
for p in (main_tex, supp, cover, cover_tex):
    if not p.exists():
        raise SystemExit(f"missing {p}")

for p in (main_tex, supp):
    text = p.read_text()
    for term in ("Companion A", "Companion B", "full-length", "compressed journal",
                 "change log", "diary", "chat-artifact", "Route C prototype"):
        if term.lower() in text.lower():
            raise SystemExit(f"forbidden internal wording in {p.name}: {term}")

metadata = main_tex.read_text() + supp.read_text()
for term in ("Independent Researcher", "0000-0002-0019-1842", "amin\\_abaee@ut.ac.ir",
             "19 September 2026"):
    if term not in metadata:
        raise SystemExit(f"missing metadata: {term}")

for doi in ("10.6084/m9.figshare.33942451", "10.6084/m9.figshare.33942469",
            "10.6084/m9.figshare.33942487"):
    if doi not in (cover.read_text() + main_tex.read_text() + supp.read_text()):
        raise SystemExit(f"missing DOI: {doi}")

asset = ROOT / "assets" / "typed_ledger_readout.png"
svg = ROOT / "assets" / "typed_ledger_readout.svg"
if not asset.exists() or not svg.exists():
    raise SystemExit("missing diagram asset")
if not all(term in svg.read_text() for term in ("geo", "act")):
    raise SystemExit("Figure 1 compartment labels are missing")

logs = [ROOT / "rendered" / x for x in
        ("paper3_JIE_submission_v1.log", "paper3_JIE_supplement_v1.log", "JIE_cover_letter_v1.log")]
for p in logs:
    text = p.read_text()
    if re.search(r"(^|:)!|Emergency stop|Undefined control sequence|undefined references|Missing delimiter", text, re.I):
        raise SystemExit(f"compilation diagnostic in {p.name}")

out = {
    "journal_cuts": rows,
    "technical_supplement": {"file": str(supp.relative_to(ROOT)), "bytes": supp.stat().st_size,
                              "sha256": hashlib.sha256(supp.read_bytes()).hexdigest(),
                              "lines": len(supp.read_text().splitlines())},
    "diagram": {"file": str(asset.relative_to(ROOT)), "bytes": asset.stat().st_size,
                "sha256": hashlib.sha256(asset.read_bytes()).hexdigest()},
    "cover_letter": {"file": cover.name, "doi_links": 3},
    "status": "pass",
}
(ROOT / "journal_variants_validation.json").write_text(json.dumps(out, indent=2) + "\n")
for r in rows:
    print(f"{r['file']}: {r['body_words_math_excluded']}/{r['limit']} body words; PASS")
print(f"Supplementary Information: {out['technical_supplement']['lines']} lines; PASS")
print("metadata, DOI, figure and compilation checks: PASS")
