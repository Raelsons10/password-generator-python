# Unit test for validating API files and routes.

from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_valid_password_creation():
    response = client.post("/create_password/generate_password", json={"length": 12})
    assert response.status_code == 200
    assert response.json()["length"] == 12
    assert len(response.json()["password"]) == 12

def test_valid_default():
    response = client.post("/create_password/generate_password", json={})
    assert response.status_code == 200  
    assert response.json()["length"] == 12  

def test_invalid_password_length():
    response = client.post("/create_password/generate_password", json={"length": 5})
    assert response.status_code == 422

def test_invalid_type():
    response = client.post("/create_password/generate_password", json={"length": "abc"})
    assert response.status_code == 422




