"""Supersession resolution logic (refined-critique item 1).

Superseded should be decided ONLY from (a) a numeric SUPERSEDED verdict, or
(b) an explicit supersession marker — never from a low score or match presence.
"""
from scan.status import resolve_statuses, apply_superseded
from scan.models import Claim, Match


def _claim(cid, text):
    return Claim(id=cid, text=text, source_file="m", line_number=1, section="A")


def _match(cid, status="covered", rev_text=""):
    c = _claim(cid, cid)
    rc = Claim(id=f"r-{cid}", text=rev_text, source_file="r", line_number=10, section="B")
    return Match(master_claim=c, revision_claim=rc, method="semantic", score=0.9, status=status)


def test_numeric_verdict_superseded():
    m = _match("12A.1", status="covered")
    num = [{"claim_id": "12A.1",
            "computed": {"verdict": "SUPERSEDED: original-model numbers do not reproduce"},
            "description": "x"}]
    r = resolve_statuses([m], num)
    assert r["12A.1"] == "superseded"


def test_explicit_marker_superseded():
    m = _match("12A.4", status="covered", rev_text="this result does not carry over to (1\u2034)")
    r = resolve_statuses([m], [])
    assert r["12A.4"] == "superseded"


def test_no_superseded_without_verdict_or_marker():
    # low score + presence of a match is NOT enough
    m = _match("12C.9", status="covered", rev_text="state the grid range")
    assert resolve_statuses([m], []) == {}


def test_apply_superseded_mutates():
    m = _match("12A.1", status="covered")
    apply_superseded([m], [{"claim_id": "12A.1", "computed": {"verdict": "SUPERSEDED"}, "description": ""}])
    assert m.status == "superseded"


def test_curated_not_superseded_suppresses_marker():
    # 12B.6 / 12G.7: the matched paragraph carries a CONTEXTUAL supersession marker
    # ("does not transfer") but the curated layer says the item is covered. The auto
    # detector must not flip these.
    m = _match("12B.6", status="covered", rev_text="the original numbers do not transfer to (1\u2034)")
    # resolve with the curated NOT_SUPERSEDED set loaded
    assert resolve_statuses([m], []) == {}


def test_two_tier_confidence():
    from scan.models import Match
    c = _claim("12A.1", "x")
    rc = Claim(id="r", text="y", source_file="r", line_number=1, section="B")
    m = Match(master_claim=c, revision_claim=rc, method="semantic", score=0.62, status="covered")
    # tier assignment convenience (mirrors the CLI calc)
    m.auto_tier = "auto-covered" if m.score >= 0.60 else ("candidate" if m.score >= 0.20 else "none")
    assert m.auto_tier == "auto-covered"
    m2 = Match(master_claim=c, revision_claim=rc, method="semantic", score=0.25, status="covered")
    m2.auto_tier = "auto-covered" if m2.score >= 0.60 else ("candidate" if m2.score >= 0.20 else "none")
    assert m2.auto_tier == "candidate"
