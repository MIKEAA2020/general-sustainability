from scan.review import review, RUBRIC
from scan.models import ScanReport, Match, NumericResult, ConsistencyIssue


def test_review_returns_all_passes():
    r = ScanReport(master_path="m", revision_path="r", timestamp="t", config={},
                   matches=[], numeric=[], consistency=[], risk=[])
    passes = review(r)
    assert len(passes) == 3
    assert {p["pass"] for p in passes} == set(RUBRIC)
    for p in passes:
        assert 1.0 <= p["score"] <= 5.0
        assert p["findings"]


def test_review_numeric_fail_lowers_score():
    num = [NumericResult(claim_id="12A.3", computed={"a": 9}, expected={"a": 5},
                         errors={"a": 4}, passed=False, description="d")]
    r = ScanReport(master_path="m", revision_path="r", timestamp="t", config={},
                   matches=[], numeric=num, consistency=[], risk=[])
    passes = review(r)
    num_pass = next(p for p in passes if p["pass"] == "numerical")
    assert num_pass["score"] < 4.0
    assert "12A.3" in num_pass["findings"]


def test_review_custom_reviewer_fn():
    r = ScanReport(master_path="m", revision_path="r", timestamp="t", config={},
                   matches=[], numeric=[], consistency=[], risk=[])
    calls = []

    def fn(pass_name, context):
        calls.append(pass_name)
        return "llm finding"
    passes = review(r, reviewer_fn=fn)
    assert set(calls) == set(RUBRIC)
    assert all("llm finding" in p["findings"] or "fallback" in p["findings"] for p in passes)
