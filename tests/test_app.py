import pytest

import app as todo_app


@pytest.fixture()
def client(tmp_path):
    todo_app.DB = str(tmp_path / "test.db")
    todo_app.init_db()
    todo_app.app.config["TESTING"] = True

    with todo_app.app.test_client() as test_client:
        yield test_client


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_create_todo_requires_task(client):
    response = client.post("/api/v1/todos", json={"task": "   "})
    assert response.status_code == 400


def test_todo_crud_flow(client):
    create_response = client.post("/api/v1/todos", json={"task": "Ecrire le DAT"})
    assert create_response.status_code == 201

    list_response = client.get("/api/v1/todos")
    todos = list_response.get_json()
    assert list_response.status_code == 200
    assert len(todos) == 1

    todo_id = todos[0]["id"]

    update_response = client.put(f"/api/v1/todos/{todo_id}", json={"task": "Finaliser le DAT"})
    assert update_response.status_code == 200

    delete_response = client.delete(f"/api/v1/todos/{todo_id}")
    assert delete_response.status_code == 200

    final_list_response = client.get("/api/v1/todos")
    assert final_list_response.get_json() == []
