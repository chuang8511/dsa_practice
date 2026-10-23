# Flask + Python fundamentals — a hands-on path

Goal: be able to open a blank file and write a small, validated, tested Flask API
in a few minutes — no AI needed. Work through the lessons **in order**, typing
and running each. Don't just read them.

## Setup (once)

```sh
cd 2026-10-23/flask_practice
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Activate the venv (`. .venv/bin/activate`) in every new terminal before running.

## The lessons

| File | You learn | Do the "TRY THIS" at the bottom |
|---|---|---|
| `01_hello.py` | app, routes, returning a response + status | add `/ping`, change a status code |
| `02_params.py` | path params `<int:id>`, query params `request.args` | add `/subtract`, an optional param |
| `03_json.py` | `request.get_json`, `jsonify`, JSON errors | `/full-name`, count+average |
| `04_validation_errors.py` | validation, 400/404/409, `errorhandler` | `PUT`, 409 on duplicate |
| `05_crud.py` + `test_05_crud.py` | full CRUD with a factory + **pytest** | priority field, `?sort=` |

Run an app and poke it with the `curl` lines in that file's docstring:
```sh
python fundamentals/01_hello.py      # Ctrl-C to stop
```
Run the lesson-05 tests:
```sh
pytest fundamentals/test_05_crud.py -q
```

## Python bits that trip people up in these tests

- **`dict.get(key)`** returns `None` instead of raising — use it for optional fields.
- **Truthiness:** `not ""`, `not []`, `not None` are all `True`. `if not title:`
  rejects empty string, empty list, and missing in one check.
- **`isinstance(x, str)` / `isinstance(x, int)`** — validate types before using them.
  Careful: `isinstance(True, int)` is `True` in Python, so check bools first.
- **`int("3")` works, `int("x")` raises `ValueError`, `int(None)` raises `TypeError`** —
  wrap conversions in `try/except (TypeError, ValueError)`.
- **f-strings:** `f"hello {name}"`.
- **List/dict comprehensions:** `[t for t in tasks if t["done"]]`,
  `{k: v for k, v in d.items()}`.
- **`sum()`, `sorted(list, key=...)`, `enumerate()`, `zip()`** — know these cold.

## When you can do these from memory, you're ready

1. A GET route with a path param and a query-param filter.
2. A POST route that reads JSON, validates it, returns 201 or 400.
3. A 404 path for a missing resource.
4. A `create_app()` factory + a `pytest` test hitting it via `app.test_client()`.

Then go do the timed drill in `../order_status/BRIEF.md` — this time building it
yourself first, and only using the AI to speed up the parts you already understand.

## Where to look things up (allowed: you'll have docs, not just AI)

- Flask quickstart: https://flask.palletsprojects.com/en/stable/quickstart/
- Flask testing: https://flask.palletsprojects.com/en/stable/testing/
- Python stdlib you'll reach for: `collections` (defaultdict, Counter, deque),
  `heapq`, `decimal.Decimal` (money!), `datetime`.
