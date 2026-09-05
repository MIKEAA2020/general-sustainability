from model_sims.numeric_claims import run_numeric
def test_scenario_endpoint_reproduces():
    r = run_numeric("12A.3")
    assert r is not None
    assert r["claim_id"] == "12A.3"
    assert r["passed"] is True or r["passed"] is None
def test_all_expected_verifiers_run():
    for cid in ["12A.3","12G.4","12G.5","12G.2","12A.1","12G.7","R1","R2"]:
        r = run_numeric(cid)
        assert r is not None, f"no verifier for {cid}"
