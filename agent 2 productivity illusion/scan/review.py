"""Automated LLM peer review with a structured rubric (blueprint item 9).

The reviewer is run as several independent PASSES, each with a different focus
(pass 1: numerical claims; pass 2: consistency; pass 3: missing/superseded
coverage). Running multiple passes with different prompts reduces single-model
bias. Each pass returns a rubric score (1-5) plus written findings.

Because an external LLM API may be unavailable in CI/offline, every pass first
tries `reviewer_fn` (a callable provided by the user, e.g. wrapping an LLM API);
if none is supplied it falls back to a deterministic, explainable heuristic that
scores the pass from the already-computed scan evidence. The rubric and findings
are identical in structure either way, so the report is stable.
"""
from typing import Callable, Optional, List

from .models import ScanReport

# rubric dimensions per pass, each with 1-5 scale
RUBRIC = {
    "numerical": [
        "All numeric claims that can be recomputed are verified within tolerance",
        "Pass/fail status matches the documented method-dependence caveats",
        "No numeric claim is asserted without an accompanying reproduction",
    ],
    "consistency": [
        "No two statements assert contradictory versions of the same quantity",
        "Negated vs asserted phrasing of the same mechanism is resolved explicitly",
        "Quantitative claims are internally consistent across sections",
    ],
    "coverage": [
        "All master items are covered, partially covered, or explicitly superseded",
        "No master item is silently dropped",
        "Superseded items are justified rather than merely absent",
    ],
}


def _heuristic_score(report: ScanReport, pass_name: str) -> tuple:
    """Deterministic fallback scorer using the already-computed scan evidence."""
    if pass_name == "numerical":
        checked = [n for n in report.numeric]
        failed = [n for n in checked if n.passed is False]
        total = len(checked)
        base = 4.0 if total >= 3 else 3.0
        base -= min(1.5, 0.8 * len(failed))
        findings = [
            f"{len(failed)} of {total} recomputable claims failed verification"
        ] if failed else [f"All {total} recomputable claims passed"]
        for n in failed:
            findings.append(f"  claim {n.claim_id}: expected {n.expected}, got {n.computed}")
        return max(1.0, base), " | ".join(findings)

    if pass_name == "consistency":
        issues = report.consistency
        base = 4.0 - min(1.5, 0.25 * len(issues))
        findings = ([f"{len(issues)} consistency issue(s) flagged"] if issues
                    else ["No rule-based contradictions detected"])
        for it in issues[:6]:
            findings.append(f"  L{it.line1} vs L{it.line2}: {it.note}")
        return max(1.0, base), " | ".join(findings)

    # coverage pass
    statuses = {m.status for m in report.matches}
    missing = [m for m in report.matches if m.status == "missing"]
    superseded = [m for m in report.matches if m.status == "superseded"]
    base = 4.5 - (1.5 if "missing" in statuses else 0.0) - (1.0 if "superseded" in statuses else 0.0)
    findings = []
    if missing:
        findings.append(f"{len(missing)} item(s) missing: " +
                        ", ".join(m.master_claim.id for m in missing[:5]))
    if superseded:
        findings.append(f"{len(superseded)} item(s) superseded: " +
                        ", ".join(m.master_claim.id for m in superseded[:5]))
    if not findings:
        findings.append("All master items covered or explicitly superseded")
    return max(1.0, base), " | ".join(findings)


def review(report: ScanReport, reviewer_fn: Optional[Callable[[str, dict], str]] = None) -> List[dict]:
    """Run the mult-pass peer review. Reviewer_fn(pass_name, context) -> findings str.

    If reviewer_fn is None, use the heuristic fallback. Return list of pass dicts.
    """
    passes = []
    for name in RUBRIC:
        context = {"pass": name, "rubric": RUBRIC[name], "report": report.model_dump()}
        try:
            if reviewer_fn is not None:
                findings = reviewer_fn(name, context)
                # heuristic score still anchors the 1-5 scale; LLM text augments findings
                score, _fallback = _heuristic_score(report, name)
            else:
                score, findings = _heuristic_score(report, name)
        except Exception as e:  # pragma: no cover - defensive
            score, findings = 1.0, f"reviewer_fn raised {e!r}; fallback used"
        passes.append({"pass": name, "score": round(score, 2), "rubric": RUBRIC[name],
                       "findings": findings})
    passes.sort(key=lambda p: p["score"])
    return passes
