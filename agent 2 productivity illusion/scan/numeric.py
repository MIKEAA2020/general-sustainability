"""Numerical claim verification: run registered verifiers, compare within tolerance."""
from .models import NumericResult

try:
    from model_sims.numeric_claims import run_numeric
except Exception:      # pragma: no cover - model_sims may be absent in some CI contexts
    run_numeric = lambda cid: None

def run_all_numeric_checks(master_claims, config):
    results = []
    ids = {c.id for c in master_claims}
    for cid in sorted(ids):
        res = run_numeric(cid)
        if res is not None:
            results.append(NumericResult(**res))
    return results
