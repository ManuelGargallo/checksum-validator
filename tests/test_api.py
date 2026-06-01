from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_validate_luhn_success():
    response = client.post("/api/v1/validate/luhn", json={"number": "79927398713"})
    assert response.status_code == 200
    assert response.json()["valid"] is True


def test_validate_luhn_formatted():
    response = client.post("/api/v1/validate/luhn", json={"number": "7992-7398-713"})
    assert response.status_code == 200
    assert response.json()["valid"] is True


def test_validate_luhn_batch():
    response = client.post(
        "/api/v1/validate/luhn/batch", json={"numbers": ["79927398713", "79927398714"]}
    )
    assert response.status_code == 200
    results = response.json()["results"]
    assert len(results) == 2
    assert results[0]["valid"] is True
    assert results[1]["valid"] is False


def test_generate_luhn():
    response = client.post("/api/v1/generate/luhn", json={"number": "7992739871"})
    assert response.status_code == 200
    assert response.json()["added_digit"] == "3"
    assert response.json()["new_number"] == "79927398713"


def test_invalid_input():
    response = client.post("/api/v1/validate/luhn", json={"number": "abc-123"})
    assert response.status_code == 422  # Pydantic validation error
