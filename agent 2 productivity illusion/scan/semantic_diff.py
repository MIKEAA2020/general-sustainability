"""Semantic diff of structured statements (blueprint item 8).

Rather than a raw-text diff, we extract the structured statements (ID, text,
status) from two versions of the SAME document and describe how each statement's
treatment changed: e.g. ``masking is absent`` -> ``masking is deficit-bounded``.
This is what a textual diff would miss.

The unit of change is a claim ID (or a heading). Two passes are produced:
  * `status_map`   : ID -> status change (covered/partial/superseded/missing/ambiguous)
  * `semantic`     : free-text descriptions of the largest semantic shifts, scored
                     by a TF-IDF similarity drop between the old/new text.
"""
import re
from typing import List

import numpy as np

CHANGE_LABEL = {
    ("covered", "covered"): "unchanged (still covered)",
    ("covered", "partial"): "weakened: coverage reduced",
    ("covered", "superseded"): "reversed: now superseded",
    ("covered", "missing"): "dropped: no longer addressed",
    ("partial", "covered"): "strengthened: now fully covered",
    ("superseded", "covered"): "restored: no longer superseded",
    ("superseded", "partial"): "partially restored",
    ("missing", "covered"): "added: now covered",
    ("missing", "partial"): "added: partially covered",
    ("missing", "missing"): "still missing",
    ("superseded", "superseded"): "still superseded",
    ("partial", "partial"): "still partial",
    ("ambiguous", "ambiguous"): "still ambiguous",
}


def _similarity(a, b):
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        vec = TfidfVectorizer(lowercase=True, ngram_range=(1, 2))
        X = vec.fit_transform([a, b]).toarray()
        na, nb = np.linalg.norm(X[0]) + 1e-9, np.linalg.norm(X[1]) + 1e-9
        return float((X[0] @ X[1]) / (na * nb))
    except Exception:
        # token-overlap fallback
        sa, sb = set(re.findall(r"\w+", a.lower())), set(re.findall(r"\w+", b.lower()))
        if not sa or not sb:
            return 0.0
        return len(sa & sb) / len(sa | sb)


def build_status_map(old_matches, new_matches):
    """old/new are lists of Match. Return sorted list of (id, old_status, new_status, label)."""
    old = {m.master_claim.id: m.status for m in old_matches}
    new = {m.master_claim.id: m.status for m in new_matches}
    out = []
    for cid in sorted(set(old) | set(new)):
        o, n = old.get(cid, "missing"), new.get(cid, "missing")
        out.append((cid, o, n, CHANGE_LABEL.get((o, n), f"{o} -> {n}")))
    return out


def semantic_changes(old_matches, new_matches, top_n=10):
    """Highlight the largest semantic shifts per ID (where text materially changed)."""
    old = {m.master_claim.id: m.master_claim.text for m in old_matches}
    new = {m.master_claim.id: m.master_claim.text for m in new_matches}
    shifts = []
    for cid in sorted(set(old) & set(new)):
        if old[cid] == new[cid]:
            continue
        sim = _similarity(old[cid], new[cid])
        if sim < 0.85:  # materially different wording
            shifts.append({
                "claim_id": cid,
                "similarity": round(sim, 3),
                "old": old[cid][:160],
                "new": new[cid][:160],
            })
    shifts.sort(key=lambda d: d["similarity"])
    return shifts[:top_n]


def diff_versions(old_matches, new_matches) -> dict:
    return {
        "status_map": build_status_map(old_matches, new_matches),
        "semantic_changes": semantic_changes(old_matches, new_matches),
        "summary": {
            "n_status_changed": sum(1 for _, o, n, _ in build_status_map(old_matches, new_matches)
                                    if o != n),
            "n_semantic_shifts": len(semantic_changes(old_matches, new_matches)),
        },
    }
