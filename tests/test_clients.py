from fastapi.testclient import TestClient


def test_get_clients(client: TestClient):
    response = client.get("/clients/search?name=Way")
    assert response.status_code == 200
    assert len(response.json()) > 0
    for customer in response.json():
        assert "Way" in customer["last_name"]


def test_get_client_details(client: TestClient):
    response = client.get("/clients/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    print(response.json()[0])
    client_id = response.json()[0]["customers_id"]
    response = client.get(f"/clients/{client_id}")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["customers_id"] == client_id


def test_get_client_sales(client: TestClient):
    response = client.get("/clients/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    print(response.json()[0])
    client_id = response.json()[0]["customers_id"]
    response = client.get(f"/clients/{client_id}/sales")
    assert response.status_code == 200
    assert len(response.json()) > 0
    for sale in response.json():
        assert sale["customer_id"] == client_id
