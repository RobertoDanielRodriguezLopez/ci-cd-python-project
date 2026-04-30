from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_build_word():
    payload = {
        "words": ["yoda", "best", "has"]
    }

    response = client.post("/build-word", json=payload)
    assert response.status_code == 200
    assert response.json() == {"result": "yes"}
