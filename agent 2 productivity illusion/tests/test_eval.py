"""Eval harness smoke test: run on the real master/revision and check the numbers
it reports are internally consistent and meet a floor (acceptance that the
matcher is useful as a support tool)."""
from scan.eval import run_eval


def test_eval_runs_and_reports_metrics():
    res = run_eval("data/MASTER_joint_assessment_and_implementation_plan.md",
                   "data/IMPLEMENTED_revision_ECOMOD.md", thresholds=(0.2, 0.55),
                   model_name=None, topk=3)
    assert res["n_claims"] == 22
    assert 0.0 <= res["recall@1"] <= 1.0
    assert 0.0 <= res["recall@3"] <= 1.0
    assert "0.2" in res["thresholds"]
    v = res["thresholds"]["0.2"]
    assert v["precision"] >= 0.9, "matcher should not confidently propose wrong paragraphs"
    assert v["recall"] > 0.5, "matcher should retrieve a majority of gold anchors"
    assert "gold_best_score" in res and "mean" in res["gold_best_score"]
    assert res["gold_best_score"]["mean"] > 0.0
