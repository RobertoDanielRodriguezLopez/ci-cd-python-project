from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_dictionary_add_and_get():
    payload = {
        "word": "apple",
        "definition": "a fruit"
    }

    post_response = client.post("/dictionary", json=payload)
    assert post_response.status_code == 200

    get_response = client.get("/dictionary/apple")
    assert get_response.status_code == 200
    assert get_response.json() == {"result": "a fruit"}
