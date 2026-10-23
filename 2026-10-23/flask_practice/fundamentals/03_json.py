"""Lesson 03 — JSON in and JSON out (the core of any API test).

Run:  python fundamentals/03_json.py
Poke (note -X POST and the JSON header):
    curl -i -X POST http://127.0.0.1:5000/echo \
         -H "Content-Type: application/json" -d '{"name": "sam", "age": 3}'
    curl -i -X POST http://127.0.0.1:5000/echo -d 'not json'

Concepts:
- `request.get_json(silent=True)` parses the JSON body. silent=True returns None
  on bad/missing JSON instead of raising — so you control the error response.
- `jsonify(obj)` turns a dict/list into a JSON response with the right header.
- Return `(jsonify(...), status_code)` to set the status.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.post("/echo")
def echo():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"error": "expected a JSON body"}), 400
    # Echo it back, adding a field, to prove we parsed it.
    return jsonify({"you_sent": body, "keys": list(body.keys())}), 200


@app.post("/sum")
def sum_numbers():
    body = request.get_json(silent=True) or {}
    nums = body.get("numbers")
    if not isinstance(nums, list) or not all(isinstance(x, (int, float)) for x in nums):
        return jsonify({"error": "'numbers' must be a list of numbers"}), 400
    return jsonify({"total": sum(nums)}), 200


if __name__ == "__main__":
    app.run(debug=True)

# TRY THIS:
# 1. Add POST /full-name that takes {"first","last"} and returns
#    {"full": "First Last"}, with 400 if either is missing or not a string.
# 2. Make /sum also return the count and average (guard against empty list).
