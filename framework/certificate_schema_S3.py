#!/usr/bin/env python3
"""S3.3 — machine-readable verdict-record schema + validator (Phase N, O26).

A minimal, honest validator for the negative-certificate record of S3.2: it
checks the required fields, the frozen output vocabulary {retained, not
retained, declined on class grounds}, the N0–N3 certificate levels, and the
band-basis vocabulary of Section 8. It does not re-derive any verdict — it
guards the *form* of a claim, not its truth. No external dependencies: the
record is JSON (YAML is a superset, so a JSON file validates with the stdlib).

Usage:
    python3 certificate_schema_S3.py record.json        # validate one record
    python3 certificate_schema_S3.py --example          # print a blank template
"""
import json, sys

REQUIRED_TOP = ["predictand", "data_vintage", "forecast_origins", "ladder",
    "rule_version", "band", "band_basis", "benchmark", "comparators",
    "horizons", "loss", "information_set", "verdicts",
    "operating_characteristics", "certificate_level", "expiry", "archives",
    "analyst", "date"]

VOCAB = {"retained", "not retained", "declined on class grounds"}
LEVELS = {"N0", "N1", "N2", "N3"}
BAND_BASES = {"pre-registered", "simulation-calibrated", "decision-based"}

TEMPLATE = {
    "predictand": "",
    "data_vintage": "",
    "forecast_origins": [],
    "ladder": [],
    "rule_version": "R2",
    "band": None,
    "band_basis": "",           # one of sorted(BAND_BASES)
    "benchmark": [],
    "comparators": {},          # module -> next-simpler rung or null
    "horizons": [],
    "loss": "",
    "information_set": "",      # pointer to the filled S3.1 canvas
    "verdicts": {},             # module -> verdict dict, validated below
    "operating_characteristics": {},
    "certificate_level": "",    # one of sorted(LEVELS)
    "expiry": [],
    "archives": {},
    "analyst": "",
    "date": "",
}

def validate(rec, errors=None):
    errors = [] if errors is None else errors
    if not isinstance(rec, dict):
        return ["record is not a JSON object"]
    for k in REQUIRED_TOP:
        if k not in rec:
            errors.append(f"missing required field: {k}")
    if rec.get("band_basis") and rec["band_basis"] not in BAND_BASES:
        errors.append(f"band_basis must be one of {sorted(BAND_BASES)}")
    if rec.get("certificate_level") and rec["certificate_level"] not in LEVELS:
        errors.append(f"certificate_level must be one of {sorted(LEVELS)}")
    verdicts = rec.get("verdicts")
    if isinstance(verdicts, dict):
        for mod, v in verdicts.items():
            if not isinstance(v, dict) or "verdict" not in v:
                errors.append(f"verdicts[{mod!r}] must be an object with a 'verdict' key")
                continue
            if v["verdict"] not in VOCAB:
                errors.append(f"verdicts[{mod!r}]->{v['verdict']!r} not in frozen vocabulary {sorted(VOCAB)}")
            if v["verdict"] == "declined on class grounds" and not v.get("class_grounds_reason"):
                errors.append(f"verdicts[{mod!r}]: declined modules must carry a class_grounds_reason (Section 3a)")
    elif verdicts is not None:
        errors.append("verdicts must be an object keyed by module name")
    return errors

def main():
    if "--example" in sys.argv:
        print(json.dumps(TEMPLATE, indent=2)); return
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    rec = json.load(open(sys.argv[1], encoding="utf-8"))
    errors = validate(rec)
    if errors:
        print(f"INVALID: {len(errors)} problem(s)")
        for e in errors: print("  -", e)
        sys.exit(1)
    print("VALID verdict record")

if __name__ == "__main__":
    main()
