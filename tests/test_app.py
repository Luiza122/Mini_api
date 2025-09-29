import pytest
from app import create_app
from app.core.config import TestConfig

@pytest.fixture()
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        yield client

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200

def test_crud_basico(client):
    # cria
    r = client.post("/usuarios", json={"nome": "Ana", "email": "ana@example.com"})
    assert r.status_code == 201
    data = r.get_json()
    uid = data["id"]

    # lista
    r = client.get("/usuarios")
    assert r.status_code == 200
    assert isinstance(r.get_json(), list)

    # busca id
    r = client.get(f"/usuarios/{uid}")
    assert r.status_code == 200

    # conflito por email
    r = client.post("/usuarios", json={"nome":"Outra", "email":"ana@example.com"})
    assert r.status_code == 409
