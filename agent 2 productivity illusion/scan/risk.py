"""Scored, prioritised risk register.

risk_score = w_sev*severity + w_uncert*(1-score) + w_act*(type==actionable)
Criticality is mapped from the score; the register is sorted by score so the
next revision sees the highest-risk gaps first.
"""
from .models import RiskItem

SEV = {"missing": 1.0, "superseded": 0.85, "partial": 0.65, "ambiguous": 0.5, "covered": 0.15}
# numeric supersession / high-uncertainty matches get a severity bump
BUMP = {"superseded": 0.0}   # already high

def filter_risk(items, threshold=0.3):
    """Return (in_register, dropped) split by a risk-score threshold (refined-scan item 3)."""
    in_reg = [r for r in items if r.risk_score > threshold]
    dropped = [r for r in items if r.risk_score <= threshold]
    return in_reg, dropped


def ci_failure_ids(matches, config=None, numeric=None):
    """The ID set that should gate CI: missing/partial & actionable & high criticality.

    Refined-scan item 3/5: the pipeline is a support tool, so it only *blocks* on
    genuinely critical actionable gaps, never on auto-vs-curated discrepancies.
    """
    cfg = (config or {}).get("risk", {}) or {}
    high = cfg.get("block_on_criticality", "high")
    out = []
    for m in matches:
        if m.status not in ("missing", "partial"):
            continue
        if m.master_claim.type != "actionable":
            continue
        # compute the same criticality as compute_risk would
        sev = SEV.get(m.status, 0.5)
        if numeric and any(n.claim_id == m.master_claim.id and n.passed is False for n in numeric):
            sev = max(sev, 0.9)
        score = (cfg.get("severity_weight", 0.55) * sev +
                 cfg.get("uncertainty_weight", 0.30) * (1 - m.score) +
                 cfg.get("actionable_weight", 0.15) * 1.0)
        crit = "high" if score >= 0.7 else ("medium" if score >= 0.5 else "low")
        if crit == high:
            out.append(m.master_claim.id)
    return out


def compute_risk(matches, config=None, numeric=None):
    config = config or {}
    w_sev = config.get("risk", {}).get("severity_weight", 0.55)
    w_unc = config.get("risk", {}).get("uncertainty_weight", 0.30)
    w_act = config.get("risk", {}).get("actionable_weight", 0.15)
    numeric = numeric or []
    numeric_ids = {n.claim_id: n for n in numeric if n.passed is False}
    items = []
    for m in matches:
        sev = SEV.get(m.status, 0.5)
        # a superseded numeric claim is genuinely high risk (claim no longer holds)
        if m.master_claim.id in numeric_ids:
            sev = max(sev, 0.9)
        # item 3: an *actionable* item on the execute pipeline needs actual evidence;
        # being un-verbified or missing raises the risk even if the text is present.
        if m.pipeline == "execute" and m.status in ("missing", "superseded"):
            sev = max(sev, 0.85)
        score = (w_sev * sev + w_unc * (1 - m.score) +
                 w_act * (1.0 if m.master_claim.type == "actionable" else 0.0))
        criticality = "high" if score >= 0.7 else ("medium" if score >= 0.5 else "low")
        reason = (f"status={m.status}, score={m.score:.2f}, type={m.master_claim.type}")
        if m.master_claim.id in numeric_ids:
            n = numeric_ids[m.master_claim.id]
            reason += f"; NUMERIC check failed (expected {n.expected}, got {n.computed})"
        items.append(RiskItem(claim_id=m.master_claim.id, risk_score=round(score, 3),
                              status=m.status, criticality=criticality, reason=reason,
                              type=m.master_claim.type))
    return sorted(items, key=lambda r: -r.risk_score)
