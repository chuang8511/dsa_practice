"""Order Status API — STUB. Build this out (with an AI co-pilot) per BRIEF.md.

Keep the create_app() + in-memory store pattern from ../_reference/app.py.
Delete these TODOs as you implement them.
"""

from flask import Flask, jsonify, request

# Transition rules in one place so adding a status later is a one-line change.
ALLOWED = {
    "PLACED": {"COOKING", "CANCELLED"},
    "COOKING": {"OUT_FOR_DELIVERY", "CANCELLED"},
    "OUT_FOR_DELIVERY": {"DELIVERED", "CANCELLED"},
    "DELIVERED": set(),
    "CANCELLED": set(),
}


def create_app():
    app = Flask(__name__)
    app.store = {}
    app.next_id = 1

    @app.post("/orders")
    def create():
        body = request.get_json(silent=True) or {}
        items = body.get("items")
        if not items or not isinstance(items, list):
            return jsonify({ "error": "items are missing "}), 400
        order = { "id": app.next_id, 
                  "items": body.get("items"), 
                  "status": "PLACED" }
        app.store[app.next_id] = order
        app.next_id += 1
        return jsonify(order), 201

    @app.get("/orders/<int:order_id>")
    def get(order_id):
        order = app.store.get(order_id)
        if order is None :
            return jsonify({ "error": "no order "}), 404
        return jsonify(order), 200

    @app.get("/orders")
    def get_orders():
        status = request.args.get('status')
        orders = list(app.store.values())
        if status:
            orders = [o for o in orders if o["status"] == status]
        return jsonify(orders), 200
    
    @app.post("/orders/<int:order_id>/transition")
    def update_order(order_id):
        order = app.store.get(order_id)
        if order is None:
            return jsonify({ "error": "no order "}), 404
        body = request.get_json(silent=True) or {}
        new_status = body.get("to")
        if not new_status or new_status not in ALLOWED[order.get('status')]:
            return jsonify({ "error": "bad request, not allowed transition"}), 400
        
        order["status"] = new_status
        app.store[order_id] = order
        return jsonify(order), 200
    
    @app.delete("/orders/<int:order_id>")
    def delete(order_id):
        if order_id not in app.store:
            return jsonify({"error": "not found"}), 404
        del app.store[order_id]
        return "", 204
        


    return app


if __name__ == "__main__":
    create_app().run(debug=True)
