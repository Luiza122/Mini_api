import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import SessionLocal, Base, engine

client = TestClient(app)

@pytest.fixture(scope="function")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_user(test_db):
    response = client.post(
        "/api/v1/usuarios/",
        json={"nome": "Luiza Dantas", "email": "luiza@example.com"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Luiza Dantas"
    assert data["email"] == "luiza@example.com"
    assert "id" in data

def test_get_users(test_db):
    # Create a user first
    client.post("/api/v1/usuarios/", json={"nome": "Test User", "email": "test@example.com"})
    
    response = client.get("/api/v1/usuarios/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"