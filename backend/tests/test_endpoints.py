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


def test_user_endpoints():
    response = client.post(
        "/users",
        json={"username": "mario", "email": "mario@example.com"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["role"] == "manutentore"
    response = client.get("/users/mario")
    assert response.status_code == 200


def test_settings_endpoints():
    settings = {
        "logo_path": None,
        "smtp": {"server": "smtp.example.com", "port": 25, "use_tls": False},
    }
    response = client.put("/settings", json=settings)
    assert response.status_code == 200
    data = response.json()
    assert data["smtp"]["server"] == "smtp.example.com"
    response = client.get("/settings")
    assert response.status_code == 200
    assert response.json()["smtp"]["port"] == 25
