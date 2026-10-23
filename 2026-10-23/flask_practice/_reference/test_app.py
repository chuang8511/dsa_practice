"""Reference tests — how to exercise a Flask app via its test client.

The `client` fixture builds a fresh app (fresh store) per test, so tests don't
leak state into each other. This is the pattern to reuse in every scenario.
"""

import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def test_create_note_returns_201_and_body(client):
    resp = client.post("/notes", json={"text": "buy milk"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["text"] == "buy milk"
    assert "id" in data


def test_create_note_rejects_empty_text(client):
    resp = client.post("/notes", json={"text": "   "})
    assert resp.status_code == 400


def test_create_note_rejects_missing_body(client):
    resp = client.post("/notes", json={})
    assert resp.status_code == 400


def test_get_note_404_when_absent(client):
    assert client.get("/notes/999").status_code == 404


def test_list_and_filter(client):
    client.post("/notes", json={"text": "alpha"})
    client.post("/notes", json={"text": "beta"})
    assert len(client.get("/notes").get_json()) == 2
    filtered = client.get("/notes?contains=alph").get_json()
    assert len(filtered) == 1 and filtered[0]["text"] == "alpha"


def test_delete_note(client):
    created = client.post("/notes", json={"text": "temp"}).get_json()
    assert client.delete(f"/notes/{created['id']}").status_code == 204
    assert client.get(f"/notes/{created['id']}").status_code == 404
