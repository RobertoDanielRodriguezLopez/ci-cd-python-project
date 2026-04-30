from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_calculate_total():
    payload = {
        "costs": {"socks": 5, "shoes": 60},
        "items": ["socks", "shoes"],
        "tax": 0.09
    }

    response = client.post("/calculate-total", json=payload)
    assert response.status_code == 200
    assert response.json() == {"total": 70.85}
