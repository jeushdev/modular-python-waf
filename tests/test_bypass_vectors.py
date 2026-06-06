import pytest

def test_clean_request_allowed(client):
    response = client.get('/submit?username=goodcitizen')
    assert response.status_code == 200


def test_sqli_bypass_blocked(client):
    response = client.get('/submit?username=admin%27%20OR%201%3D1%20--')
    assert response.status_code == 403

def test_xss_bypass_blocked(client):
    response = client.get('/submit?comment=alert(1)')
    assert response.status_code == 403