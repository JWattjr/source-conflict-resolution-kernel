import json


def _deploy(direct_deploy):
    return direct_deploy(
        "contracts/SourceConflictKernel.py",
        "The claim is true",
        [
            {"id": "one", "url": "https://one.example.org/claim", "tier": 1},
            {"id": "two", "url": "https://two.example.org/claim", "tier": 1},
        ],
        "2030-01-01T00:00:00Z",
        2,
    )


def test_resolves_confirmed_claim_and_validator(direct_vm, direct_deploy):
    contract = _deploy(direct_deploy)
    direct_vm.warp("2031-01-01T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 200, "body": "official evidence"})
    direct_vm.mock_llm(r".*", json.dumps({"observations": [
        {"id": "one", "stance": "SUPPORTS"},
        {"id": "two", "stance": "SUPPORTS"},
    ]}))
    assert contract.resolve()["outcome"] == "YES"
    assert direct_vm.run_validator()
    assert not direct_vm.run_validator(leader_result={"observations": [], "outcome": "NO"})


def test_conflict_is_explicit(direct_vm, direct_deploy):
    contract = _deploy(direct_deploy)
    direct_vm.warp("2031-01-01T00:00:00Z")
    direct_vm.mock_web(r".*", {"status": 200, "body": "evidence"})
    direct_vm.mock_llm(r".*", json.dumps({"observations": [
        {"id": "one", "stance": "SUPPORTS"},
        {"id": "two", "stance": "REFUTES"},
    ]}))
    result = contract.resolve()
    assert result["status"] == "CONTESTED"
    assert result["outcome"] == "UNRESOLVED"
