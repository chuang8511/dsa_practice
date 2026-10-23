# Scenario: Order Status API (40 min, AI-paired)

Build a small Flask service that tracks food-delivery orders and their status.
Work with an AI assistant. Start a 40-minute timer.

## Requirements

Statuses move in one direction only:
`PLACED -> COOKING -> OUT_FOR_DELIVERY -> DELIVERED`. `CANCELLED` is reachable from
any non-terminal state. `DELIVERED` and `CANCELLED` are terminal.

Endpoints:

| Method | Path | Behavior |
|---|---|---|
| `POST` | `/orders` | Body `{"items": ["pizza", ...]}`. Create an order in `PLACED`. Return 201 with `{id, items, status}`. 400 if `items` missing/empty/not a list. |
| `GET` | `/orders/<id>` | Return the order. 404 if unknown. |
| `GET` | `/orders` | List all. Optional `?status=COOKING` filter. |
| `POST` | `/orders/<id>/transition` | Body `{"to": "COOKING"}`. Apply a transition. 404 unknown order; 400 if the transition is illegal (e.g. DELIVERED -> COOKING, or an unknown status). Return the updated order. |

Non-functional: validate all input, use correct status codes, don't crash on a
missing key or empty body, keep the transition rules in one place so a new status
is easy to add (an "add a feature" follow-up is likely).

## Suggested stretch (if time)

- `DELETE /orders/<id>` -> 204, 404 if absent.
- Idempotency: transitioning to the status it's already in is a no-op 200, not a 400.

## Your prompt-engineering notes (fill in as you go)

- Assumptions stated up front:
- Best prompt I used:
- **AI mistake I caught and fixed** (aim for ≥1):
