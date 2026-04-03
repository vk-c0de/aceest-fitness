def test_programs(client):
    response = client.get("/api/programs")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_fee(client):
    response = client.post("/api/fee", json={"months": 12, "tier": "premium"})
    assert response.status_code == 200
    assert response.get_json()["fee"] > 0
