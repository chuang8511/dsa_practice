"""Reference Flask API — the idioms to memorize before test day.

A tiny "notes" service backed by an in-memory dict. Shows: GET + POST routes,
reading JSON body and query params, input validation, correct status codes,
a 404 path, and a factory so tests get a fresh store each time.

Run:   python app.py        -> http://127.0.0.1:5000
Test:  pytest -q
"""

from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)
    # In-memory store standing in for a DB. Kept on `app` so each app instance
    # (each test) starts clean.
    app.store = {}
    app.next_id = 1

    @app.get("/notes")
    def list_notes():
        # Optional query-param filter: /notes?contains=foo
        needle = request.args.get("contains")
        notes = app.store.values()
        if needle:
            notes = [n for n in notes if needle in n["text"]]
        return jsonify(list(notes)), 200

    @app.get("/notes/<int:note_id>")
    def get_note(note_id):
        note = app.store.get(note_id)
        if note is None:
            return jsonify({"error": "note not found"}), 404
        return jsonify(note), 200

    @app.post("/notes")
    def create_note():
        body = request.get_json(silent=True) or {}
        text = body.get("text")
        # Validate: text must be a non-empty string.
        if not isinstance(text, str) or not text.strip():
            return jsonify({"error": "text is required and must be a non-empty string"}), 400
        note = {"id": app.next_id, "text": text}
        app.store[app.next_id] = note
        app.next_id += 1
        return jsonify(note), 201  # 201 Created, not 200

    @app.delete("/notes/<int:note_id>")
    def delete_note(note_id):
        if note_id not in app.store:
            return jsonify({"error": "note not found"}), 404
        del app.store[note_id]
        return "", 204

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
