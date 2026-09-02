import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from mypkg.config import Settings
from mypkg.main import app


@pytest.fixture
def client() -> TestClient:
    """_summary_

    Returns:
        TestClient: _description_
    """
    return TestClient(app)


def test_health_check_returns_200_and_correct_payload(client: TestClient) -> None:
    """_summary_

    Args:
        client (TestClient): _description_
    """
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "environment" in data


def test_predict_endpoint_valid_payload(client: TestClient) -> None:
    """_summary_

    Args:
        client (TestClient): _description_
    """
    response = client.post("/predict", json={"features": [10.0, 5.5]})
    assert response.status_code == 200
    assert response.json() == {"prediction": 15.5}


def test_settings_fails_fast_on_missing_required_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """_summary_

    Args:
        monkeypatch (pytest.MonkeyPatch): _description_
    """
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    with pytest.raises(ValidationError):
        Settings(_env_file=None)
