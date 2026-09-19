#!/usr/bin/env python3
"""Validation gate for the journal-specific cuts and their delegated supplement."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent

def words(text):
    text = re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$", " ", text, flags=re.S)
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
    required = ["material", "Typed", "depletion", "Companion A", "full-length"]
    missing = [x for x in required if x.lower() not in text.lower()]
    rows.append({"file": name, "body_words_math_excluded": n, "limit": limit,
                 "within_limit": n <= limit, "missing_required_terms": missing,
                 "lines": len(text.splitlines())})
    if n > limit:
        raise SystemExit(f"{name}: {n} body words exceeds {limit}")
    if missing:
        raise SystemExit(f"{name}: missing {missing}")

asset = ROOT / "assets" / "typed_ledger_readout.png"
if not asset.exists():
    raise SystemExit("missing diagram asset")
supp = ROOT / "technical_supplement_v1.md"
if not supp.exists() or words(supp.read_text()) < 10000:
    raise SystemExit("technical supplement is missing or implausibly short")

out = {"journal_cuts": rows,
       "technical_supplement": {"file": supp.name, "bytes": supp.stat().st_size,
                                 "sha256": hashlib.sha256(supp.read_bytes()).hexdigest(),
                                 "lines": len(supp.read_text().splitlines())},
       "diagram": {"file": str(asset.relative_to(ROOT)), "bytes": asset.stat().st_size,
                   "sha256": hashlib.sha256(asset.read_bytes()).hexdigest()},
       "status": "pass"}
(ROOT / "journal_variants_validation.json").write_text(json.dumps(out, indent=2) + "\n")
for r in rows:
    print(f"{r['file']}: {r['body_words_math_excluded']}/{r['limit']} body words; PASS")
print(f"technical supplement: {out['technical_supplement']['lines']} lines; PASS")
print("diagram: PASS")
