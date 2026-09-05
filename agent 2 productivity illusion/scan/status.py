"""Status resolution (supersession pass).

Decided AFTER numeric verification. Supersession is set only when:
  (a) the numeric verifier returns an explicit SUPERSEDED verdict for the claim, or
  (b) the matched revision text carries an explicit supersession marker.

It is never inferred from a low semantic score or from the mere presence of a
match. This is the fix requested in the refined-scan critique (item 1).
"""
import re

from .matcher import SUPERSEDED_MARK


def _verdict_superseded(numeric_result) -> bool:
    if numeric_result is None:
        return False
    text = str(numeric_result.get("computed", {}).get("verdict", "")) + \
        " " + str(numeric_result.get("description", ""))
    return bool(SUPERSEDED_MARK.search(text))


def resolve_statuses(matches, numeric_results, not_superseded=None):
    """Return a dict claim_id -> 'superseded' for claims that are superseded.

    numeric_results is a list of NumericResult dicts (or the pydantic objects).
    `not_superseded` is a set of IDs whose matched paragraph carries a CONTEXTUAL
    supersession marker (the revision merely discusses supersession) that must not
    flip the item. These are decided by the curated layer, not the auto detector.
    """
    not_superseded = not_superseded or set()
    try:
        from .curated import NOT_SUPERSEDED
        not_superseded |= NOT_SUPERSEDED
    except Exception:
        pass
    verdicts = {}
    for n in numeric_results:
        cid = n.get("claim_id") if isinstance(n, dict) else n.claim_id
        if _verdict_superseded(n):
            verdicts[cid] = True
    out = {}
    for m in matches:
        cid = m.master_claim.id
        # curated NOT_SUPERSEDED wins; never auto-supersede these
        if cid in not_superseded:
            continue
        if cid in verdicts:
            out[cid] = "superseded"
            continue
        if m.revision_claim and SUPERSEDED_MARK.search(m.revision_claim.text):
            out[cid] = "superseded"
        elif SUPERSEDED_MARK.search(m.master_claim.text):
            out[cid] = "superseded"
    return out


def apply_superseded(matches, numeric_results):
    """Mutate `matches`: set status='superseded' where resolved. Returns matches."""
    resolved = resolve_statuses(matches, numeric_results)
    for m in matches:
        if m.master_claim.id in resolved and m.status != "superseded":
            m.status = "superseded"
    return matches
