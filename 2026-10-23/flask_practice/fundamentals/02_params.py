"""Lesson 02 — path params and query params.

Run:  python fundamentals/02_params.py
Poke:
    curl http://127.0.0.1:5000/greet/sam
    curl "http://127.0.0.1:5000/add?a=3&b=4"
    curl "http://127.0.0.1:5000/add?a=oops"

Concepts:
- `<name>` in a route captures a path segment and passes it as a function arg.
- `<int:n>` converts it to int (and 404s automatically if it isn't an int).
- Query params (?a=3) come from `request.args`. They are ALWAYS strings until
  you convert them, and may be missing — handle both.
"""

from flask import Flask, request

app = Flask(__name__)


@app.get("/greet/<name>")
def greet(name):
    # `name` is a string captured from the URL path.
    return f"hello {name}"


@app.get("/double/<int:n>")
def double(n):
    # `n` is already an int because of the <int:...> converter.
    return f"{n * 2}"


@app.get("/add")
def add():
    # request.args is a dict-like of query params. .get avoids KeyError.
    a = request.args.get("a")
    b = request.args.get("b")
    try:
        total = int(a) + int(b)
    except (TypeError, ValueError):
        # TypeError if missing (None), ValueError if not a number.
        return "a and b must both be integers", 400
    return f"{total}"


if __name__ == "__main__":
    app.run(debug=True)

# TRY THIS:
# 1. Add /subtract that does a - b with the same validation.
# 2. Add an optional ?times=N to /double (default 2). Convert and validate it.
