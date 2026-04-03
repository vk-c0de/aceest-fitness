def test_programs(client):
    resp = client.get("/api/programs")
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), list)

def test_fee(client):
    resp = client.post("/api/fee", json={"months": 12, "tier": "premium"})
    assert resp.status_code == 200
    assert resp.get_json()["fee"] > 0

