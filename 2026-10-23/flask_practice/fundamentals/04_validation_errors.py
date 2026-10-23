"""Lesson 04 — validation, status codes, and clean error handling.

Run:  python fundamentals/04_validation_errors.py
Poke:
    curl -i -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{"name":"sam","age":30}'
    curl -i -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{"age":-1}'
    curl -i http://127.0.0.1:5000/users/999

Status codes you must know cold for the test:
    200 OK            201 Created        204 No Content
    400 Bad Request   404 Not Found      409 Conflict

Concepts:
- Validate every input BEFORE using it; return 400 with a helpful message.
- `abort(404)` is a quick way to bail out; or return (body, code) yourself.
- A `@app.errorhandler` turns raised errors into consistent JSON.
"""

from flask import Flask, abort, jsonify, request

app = Flask(__name__)
users = {}
next_id = 1


@app.errorhandler(404)
def not_found(err):
    # Make even framework 404s return JSON instead of HTML.
    return jsonify({"error": "not found"}), 404


def validate_user(body):
    """Return (ok, error_message). One place for the rules."""
    if not isinstance(body, dict):
        return False, "body must be a JSON object"
    name = body.get("name")
    age = body.get("age")
    if not isinstance(name, str) or not name.strip():
        return False, "name is required and must be a non-empty string"
    if not isinstance(age, int) or age < 0:
        return False, "age is required and must be a non-negative integer"
    return True, None


@app.post("/users")
def create_user():
    global next_id
    body = request.get_json(silent=True)
    ok, msg = validate_user(body)
    if not ok:
        return jsonify({"error": msg}), 400
    user = {"id": next_id, "name": body["name"], "age": body["age"]}
    users[next_id] = user
    next_id += 1
    return jsonify(user), 201


@app.get("/users/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user), 200


if __name__ == "__main__":
    app.run(debug=True)

# TRY THIS:
# 1. Add PUT /users/<id> that updates name/age (reuse validate_user); 404 if absent.
# 2. Reject a duplicate name with 409 Conflict.
