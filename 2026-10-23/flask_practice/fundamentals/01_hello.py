"""Lesson 01 — the smallest Flask app.

Run it:
    cd 2026-10-23/flask_practice
    . .venv/bin/activate
    python fundamentals/01_hello.py
Then in another terminal:
    curl http://127.0.0.1:5000/
    curl http://127.0.0.1:5000/health
Stop the server with Ctrl-C.

Concepts:
- `Flask(__name__)` creates the app.
- `@app.get("/path")` registers a function to handle GET requests to that path.
- Whatever you return becomes the response body. A plain string -> 200 text/html.
"""

from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return "hello from flask"


@app.get("/health")
def health():
    # Returning a tuple (body, status_code) lets you set the status explicitly.
    return "ok", 200


if __name__ == "__main__":
    # debug=True auto-reloads on edits and shows tracebacks in the browser.
    app.run(debug=True)

# TRY THIS:
# 1. Add a /ping route that returns "pong".
# 2. Make /health return status 503 instead and re-run; watch the curl output
#    change (use `curl -i` to see the status line).
