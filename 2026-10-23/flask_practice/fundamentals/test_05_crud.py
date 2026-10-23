"""Lesson 05 tests — the test-client pattern, end to end.

Run:  pytest fundamentals/test_05_crud.py -q

Learn from this: the `client` fixture builds a fresh app per test (no shared
state), and you assert on `resp.status_code` and `resp.get_json()`.
"""

import importlib.util
from pathlib import Path

import pytest

# The lesson file starts with a digit, so load it by path rather than `import`.
_spec = importlib.util.spec_from_file_location(
    "crud_lesson", Path(__file__).with_name("05_crud.py")
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
create_app = _mod.create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def test_create_then_read(client):
    created = client.post("/tasks", json={"title": "write tests"})
    assert created.status_code == 201
    tid = created.get_json()["id"]
    got = client.get(f"/tasks/{tid}")
    assert got.status_code == 200
    assert got.get_json()["title"] == "write tests"
    assert got.get_json()["done"] is False


def test_create_requires_title(client):
    assert client.post("/tasks", json={}).status_code == 400
    assert client.post("/tasks", json={"title": "  "}).status_code == 400


def test_read_missing_is_404(client):
    assert client.get("/tasks/42").status_code == 404


def test_patch_marks_done(client):
    tid = client.post("/tasks", json={"title": "x"}).get_json()["id"]
    resp = client.patch(f"/tasks/{tid}", json={"done": True})
    assert resp.status_code == 200
    assert resp.get_json()["done"] is True


def test_patch_rejects_bad_done(client):
    tid = client.post("/tasks", json={"title": "x"}).get_json()["id"]
    assert client.patch(f"/tasks/{tid}", json={"done": "yes"}).status_code == 400


def test_list_filter_done(client):
    a = client.post("/tasks", json={"title": "a"}).get_json()["id"]
    client.post("/tasks", json={"title": "b"})
    client.patch(f"/tasks/{a}", json={"done": True})
    assert len(client.get("/tasks").get_json()) == 2
    done = client.get("/tasks?done=true").get_json()
    assert len(done) == 1 and done[0]["id"] == a


def test_delete(client):
    tid = client.post("/tasks", json={"title": "temp"}).get_json()["id"]
    assert client.delete(f"/tasks/{tid}").status_code == 204
    assert client.get(f"/tasks/{tid}").status_code == 404
