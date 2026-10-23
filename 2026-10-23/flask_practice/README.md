# Flask practice — Deliveroo §2 (AI-paired API building)

A reusable starter for the 40-minute "build a small API with an AI co-pilot" drill.
`_reference/` is a complete working example to learn the Flask idioms from. Each
other folder is a **scenario**: a brief plus a stub you build out — ideally with an
AI assistant, practicing the skill Deliveroo actually grades.

## One-time setup

```sh
cd 2026-10-23/flask_practice
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

The `.venv/` lives under `.gitignore`'d space — add `2026-10-23/flask_practice/.venv/`
to `.gitignore` if git starts tracking it.

## Run

```sh
# run the tests for a scenario (or _reference)
cd 2026-10-23/flask_practice
. .venv/bin/activate
pytest _reference -q
pytest order_status -q

# run a scenario's server to poke by hand
python order_status/app.py          # serves on http://127.0.0.1:5000
```

## The AI-pairing drill (do this timed, 40 min)

The test grades prompt engineering, critically evaluating AI output, and directing
the AI. So practice that loop, not solo coding:

1. **Read the BRIEF.** State your assumptions in one line before touching code.
2. **Prompt crisply.** Give the AI the contract: routes, inputs, outputs, status
   codes, edge cases. Vague prompt in → vague code out.
3. **Read the output critically — don't paste blind.** Hunt for the usual misses:
   no input validation, wrong status code (200 where 201/400/404 belongs),
   missing-key crashes, mutable shared state, no error path.
4. **Refine with a follow-up prompt.** "Add 400 on missing `item_id`", "return 404
   when the order doesn't exist", "add a test for the empty-body case."
5. **Add/confirm a test per route**, run `pytest`, make it green.
6. **Log one AI mistake you caught** at the bottom of the BRIEF. Catching and fixing
   AI errors *is* the graded skill — aim for at least one every session.

## Making a new scenario

Copy `_reference/` to a new folder, replace `app.py` with a stub and `test_app.py`
with the contract you want, and write a `BRIEF.md`. Scenario ideas from the plan:
menu CRUD, basket price calculator with discounts, rider-assignment endpoint (heap),
rate-limited endpoint, idempotent payment endpoint.
