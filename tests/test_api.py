import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client

def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code== 200
    assert isinstance(response.get_json(), list)

def test_get_inventory_item(client):
    response = client.get("/inventory/1")

    assert response.status_code== 200
    assert response.get_json()["id"] == 1

def test_get_inventory_item_not_found(client):
    response = client.get("/inventory/999")

    assert response.status_code== 404