from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_orders():
    response = client.post("/orders/", json={"name": "Test Orders", "description": "A orders for testing"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Orders"

def test_read_orders():
    response = client.post("/orders/", json={"name": "Test Orders", "description": "A orders for testing"})
    item_id = response.json()["id"]
    response = client.get(f"/orders/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Orders"

def test_update_orders():
    response = client.post("/orders/", json={"name": "Test Orders", "description": "A orders for testing"})
    item_id = response.json()["id"]
    response = client.put(f"/orders/{item_id}", json={"name": "Updated Orders", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Orders"

def test_delete_orders():
    response = client.post("/orders/", json={"name": "Test Orders", "description": "A orders for testing"})
    item_id = response.json()["id"]
    response = client.delete(f"/orders/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Orders"
