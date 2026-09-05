from scan.semantic_diff import diff_versions, build_status_map, semantic_changes
from scan.models import Claim, Match, ScanReport


def _m(cid, text, status):
    c = Claim(id=cid, text=text, source_file="m.md", line_number=1, section="A")
    return Match(master_claim=c, revision_claim=c, method="semantic", score=0.9, status=status)


def test_status_map_captures_change():
    old = [_m("12A.1", "the masking illusion", "covered")]
    new = [_m("12A.1", "the masking illusion is deficit-bounded", "superseded")]
    sm = build_status_map(old, new)
    assert sm[0][0] == "12A.1"
    assert (sm[0][1], sm[0][2]) == ("covered", "superseded")
    assert "reversed" in sm[0][3]


def test_diff_versions_summary():
    old = [_m("x", "a", "missing"), _m("y", "b", "covered")]
    new = [_m("x", "a", "covered"), _m("y", "b", "covered")]
    d = diff_versions(old, new)
    assert d["summary"]["n_status_changed"] == 1
    assert {t[0] for t in d["status_map"]} == {"x", "y"}


def test_semantic_changes_skips_identical():
    old = [_m("x", "exactly the same text", "covered")]
    new = [_m("x", "exactly the same text", "covered")]
    assert semantic_changes(old, new) == []


def test_diff_no_match_ids():
    old = [_m("a", "s", "covered")]
    new = [_m("b", "t", "missing")]
    d = diff_versions(old, new)
    assert {t[0] for t in d["status_map"]} == {"a", "b"}
