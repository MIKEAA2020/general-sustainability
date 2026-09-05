from scan.parser import parse_master, parse_revision
def test_master_parses_ids():
    cs = parse_master("data/MASTER_joint_assessment_and_implementation_plan.md")
    ids = {c.id for c in cs}
    assert "12A.1" in ids and "12G.2" in ids and "12G.7" in ids and "12G.1" in ids
    assert all(c.line_number > 0 for c in cs)
def test_revision_parses_paragraphs():
    cs = parse_revision("data/IMPLEMENTED_revision_ECOMOD.md")
    assert len(cs) > 20
    assert any(c.section != "Preamble" for c in cs)


def test_master_12g_items_are_informative_and_anchored():
    """12G items carry body text (not just a heading) and a real line number."""
    cs = parse_master("data/MASTER_joint_assessment_and_implementation_plan.md")
    by_id = {c.id: c for c in cs}
    g1 = by_id["12G.1"]
    # not a bare heading: should mention the substantive prediction content
    assert len(g1.text) > 80, f"12G.1 text too short (heading-only): {g1.text!r}"
    assert any(k in g1.text.lower() for k in ("prediction", "falsifiable", "lag", "oscillation"))
    # 12G lines must be realistic (the 12G section lives around L580-660)
    assert by_id["12G.1"].line_number > 500
    assert by_id["12G.7"].line_number > 500
