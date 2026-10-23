"""Lesson 05 — a full small CRUD service, the shape most tests ask for.

This is the pattern to be able to produce from a blank file in a few minutes:
create_app() + in-memory dict + 5 routes + validation + right status codes.

Run:  python fundamentals/05_crud.py
Test: pytest fundamentals/test_05_crud.py -q

A "task list" API:
    POST   /tasks            create            201
    GET    /tasks            list (?done=true) 200
    GET    /tasks/<id>       read              200 / 404
    PATCH  /tasks/<id>       toggle/update     200 / 404 / 400
    DELETE /tasks/<id>       delete            204 / 404
"""

from flask import Flask, jsonify, request


def create_app():
    # A factory: returns a fresh app with a fresh store. This is what lets each
    # test start clean — reuse this pattern everywhere.
    app = Flask(__name__)
    app.tasks = {}
    app.next_id = 1

    @app.post("/tasks")
    def create():
        body = request.get_json(silent=True) or {}
        title = body.get("title")
        if not isinstance(title, str) or not title.strip():
            return jsonify({"error": "title is required"}), 400
        task = {"id": app.next_id, "title": title, "done": False}
        app.tasks[app.next_id] = task
        app.next_id += 1
        return jsonify(task), 201

    @app.get("/tasks")
    def list_tasks():
        done = request.args.get("done")  # None, "true", or "false"
        tasks = list(app.tasks.values())
        if done in ("true", "false"):
            want = done == "true"
            tasks = [t for t in tasks if t["done"] is want]
        return jsonify(tasks), 200

    @app.get("/tasks/<int:task_id>")
    def read(task_id):
        task = app.tasks.get(task_id)
        return (jsonify(task), 200) if task else (jsonify({"error": "not found"}), 404)

    @app.patch("/tasks/<int:task_id>")
    def update(task_id):
        task = app.tasks.get(task_id)
        if task is None:
            return jsonify({"error": "not found"}), 404
        body = request.get_json(silent=True) or {}
        if "title" in body:
            if not isinstance(body["title"], str) or not body["title"].strip():
                return jsonify({"error": "title must be a non-empty string"}), 400
            task["title"] = body["title"]
        if "done" in body:
            if not isinstance(body["done"], bool):
                return jsonify({"error": "done must be a boolean"}), 400
            task["done"] = body["done"]
        return jsonify(task), 200

    @app.delete("/tasks/<int:task_id>")
    def delete(task_id):
        if task_id not in app.tasks:
            return jsonify({"error": "not found"}), 404
        del app.tasks[task_id]
        return "", 204

    return app


if __name__ == "__main__":
    create_app().run(debug=True)

# TRY THIS (then update test_05_crud.py to cover it):
# 1. Add a priority field (int 1-5), validated on create and patch.
# 2. Support ?sort=title on the list endpoint.
