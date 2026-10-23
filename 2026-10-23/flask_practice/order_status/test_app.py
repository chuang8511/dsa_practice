"""Order Status API — the contract to build toward.

These express BRIEF.md as tests. They will FAIL against the stub — that's the
point. Make them pass (with your AI co-pilot), then add your own for the
stretch goals. This is your spec; read it before you prompt.
"""

import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def _create(client, items=("pizza",)):
    return client.post("/orders", json={"items": list(items)})


def test_create_returns_201_in_placed(client):
    resp = _create(client)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["status"] == "PLACED"
    assert data["items"] == ["pizza"]
    assert "id" in data


def test_create_rejects_bad_items(client):
    assert client.post("/orders", json={"items": []}).status_code == 400
    assert client.post("/orders", json={}).status_code == 400
    assert client.post("/orders", json={"items": "pizza"}).status_code == 400


def test_get_unknown_is_404(client):
    assert client.get("/orders/999").status_code == 404


def test_legal_transition(client):
    oid = _create(client).get_json()["id"]
    resp = client.post(f"/orders/{oid}/transition", json={"to": "COOKING"})
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "COOKING"


def test_illegal_transition_is_400(client):
    oid = _create(client).get_json()["id"]
    # PLACED -> DELIVERED is not allowed.
    assert client.post(f"/orders/{oid}/transition", json={"to": "DELIVERED"}).status_code == 400
    # unknown target status
    assert client.post(f"/orders/{oid}/transition", json={"to": "NOPE"}).status_code == 400


def test_transition_on_unknown_order_is_404(client):
    assert client.post("/orders/999/transition", json={"to": "COOKING"}).status_code == 404


def test_list_and_status_filter(client):
    a = _create(client).get_json()["id"]
    _create(client)
    client.post(f"/orders/{a}/transition", json={"to": "COOKING"})
    assert len(client.get("/orders").get_json()) == 2
    cooking = client.get("/orders?status=COOKING").get_json()
    assert len(cooking) == 1 and cooking[0]["id"] == a

def test_create_broken_json(client):
    resp = client.post("/orders")
    assert resp.status_code == 400

def test_transition_broken_json(client):
    items=("pizza",)
    oid = client.post("/orders", json={"items": list(items)}).get_json()["id"]
    transition_resp = client.post(f"/orders/{oid}/transition")
    assert transition_resp.status_code == 400

def test_get_order(client):
    items=("pizza",)
    oid = client.post("/orders", json={"items": list(items)}).get_json()["id"]
    resp = client.get(f"/orders/{oid}")
    assert resp.status_code == 200
    assert resp.get_json()["id"] == oid
    assert resp.get_json()["items"] == ["pizza"]

def test_delete_order(client):
    items=("pizza",)
    oid = client.post("/orders", json={"items": list(items)}).get_json()["id"]
    resp = client.delete(f"/orders/{oid}")
    assert resp.status_code == 204
    orders = client.get("/orders").get_json()
    assert len(orders) == 0

def test_delete_non_existing_order(client):
    resp = client.delete("/orders/999")
    assert resp.status_code == 404
