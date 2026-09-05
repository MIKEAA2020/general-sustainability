from scan.parser import parse_master, parse_revision
from scan.matcher import SemanticMatcher
def test_match_all_master_claims():
    mc = parse_master("data/MASTER_joint_assessment_and_implementation_plan.md")
    rc = parse_revision("data/IMPLEMENTED_revision_ECOMOD.md")
    m = SemanticMatcher(semantic_threshold=0.75, partial_threshold=0.55)
    matches = m.match_claims(mc, rc)
    assert len(matches) == len(mc)
    for mm in matches:
        assert mm.status in ("covered","partial","superseded","missing","ambiguous")
