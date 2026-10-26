from fastapi.testclient import TestClient

from app.api.dependencies import get_repository
from app.infrastructure.in_memory_repository import InMemoryTodoRepository
from app.main import app


def make_client() -> TestClient:
    repo = InMemoryTodoRepository()
    app.dependency_overrides[get_repository] = lambda: repo
    return TestClient(app)


def test_health():
    assert make_client().get("/health").json() == {"status": "ok"}


def test_create_list_complete():
    client = make_client()
    created = client.post("/todos", json={"title": "learn gitops"})
    assert created.status_code == 201
    todo_id = created.json()["id"]

    assert len(client.get("/todos").json()) == 1

    done = client.post(f"/todos/{todo_id}/complete")
    assert done.json()["done"] is True


def test_complete_missing_returns_404():
    assert make_client().post("/todos/999/complete").status_code == 404
