from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_create_and_get_report():
    response = client.post("/reports", json={"id": 1, "description": "Anomaly"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["description"] == "Anomaly"

    response = client.get("/reports/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_get_nonexistent_report():
    response = client.get("/reports/999")
    assert response.status_code == 404
