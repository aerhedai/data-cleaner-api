from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_example():
    response = client.get("/example/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from the service layer!"}
