import requests
import pytest


@pytest.mark.parametrize(
    "path",
    [
        "/",
        "/depressionquestionnaire",
        "/anxietyquestionnaire",
        "/depressionscore",
        "/anxietyscore",
    ],
)
def test_routes(path):
    response = requests.get(f"http://127.0.0.1:5000{path}")
    assert response.status_code == 200
    assert "HealthRecord" in response.text
