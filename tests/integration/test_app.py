import pytest
import requests


@pytest.mark.parametrize(
    'path', ['/', '/depression', '/anxiety', '/scores/depression', '/scores/anxiety']
)
def test_routes(path):
    response = requests.get(f'http://127.0.0.1:5000{path}')
    assert response.status_code == 200
    assert 'HealthRecord' in response.text
