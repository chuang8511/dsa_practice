# Wise & Deliveroo Interview Prep Plan

Started 2026-10-21, revised 2026-10-23. Tick the boxes as you go, then commit and push so any machine stays in sync.

Current practice lives in `2026-MM-DD/leetcode_N/solution.py`. Older topic folders (arrayHash, tree, graph, …) are earlier practice — ignore for progress tracking.

Already done this term: LC 80, 189, 128, 49, 167, 209, 560.

---

## The two tests at a glance

| | Deliveroo (confirmed from prep doc) | Wise (anecdotal, Glassdoor + guides) |
|---|---|---|
| First stage | HackerRank, **60 min, linear, 2 sections** | HackerRank screen: SQL, REST APIs, core algorithms |
| MCQ section | 15 MCQs, 20 min, **no AI** | OOP / general MCQs reported |
| Coding section | 40 min, **AI co-pilot ON (unguarded)** | 2 coding problems, mid-level |
| Later rounds | Take-home + live code review, system design, STAR | Real-world coding round, system design (financial systems), pair programming (e.g. circuit breaker), product-mindset round, values round |
| Style | Practical, real-world; AI fluency graded | Practical, clean, tested code; error handling & naming matter |

---

## Deliveroo — read this carefully, it changes how you prep

Straight from the prep doc:

- **60 minutes total, linear.** Once you submit a section you cannot go back. Unused time rolls forward, so banking minutes in section 1 helps section 2.
- **Section 1 — General Knowledge (20 min, NO AI): 15 MCQs** on general engineering, **system design**, and **testing techniques**. This is closed-book — you cannot lean on the assistant, so this is the part you must actually *study*.
- **Section 2 — Coding + AI Fluency (40 min, AI co-pilot in "unguarded" mode).** Real-world scenario, broad scope. They are explicitly grading three things:
  1. **Prompt engineering** — turning a fuzzy requirement into a clear prompt.
  2. **Critical evaluation** — spotting bugs/gaps in AI output and refining it.
  3. **Strategic co-creation** — directing the AI toward a better result, not just accepting the first answer.

**The "4 languages" are web frameworks: Golang, Spring Boot (Java), Django (Python), Flask (Python).** That is the biggest signal in the whole doc: the coding task is almost certainly **build/extend a small backend or API** (routes, request handling, validation, maybe persistence) — not a pure LeetCode algorithm. Prep for building a working endpoint, not just for solving a puzzle.

What this means for practice:
- You are **expected and rewarded** for using the AI. The skill is not "code it solo" — it's "drive the AI well and verify its work." Practice doing exactly that (see the AI-pairing drill below).
- Still learn the fundamentals: if you can't read the AI's code critically, you can't refine it.

---

## Wise — from research (anecdotal, confirm with recruiter)

- **HackerRank screen:** SQL, REST APIs, core algorithms. So unlike Deliveroo, **SQL is in scope — add it to practice.**
- **Real-world coding round:** practical problem, not competitive programming. Reported examples: circuit-breaker component, transaction processing, currency conversion with caching.
- **System design:** financial systems (e.g. design a payment system), mainly for senior roles.
- **Pair programming** round reported.
- **Product-mindset** and **values** rounds — behavioral/ownership framing.
- Reviewers look at tests, error handling, and naming. Process ~4 weeks, reported as slow.

---

## Which language / framework to pick — recommendation

**Primary: Flask (Python).** For a 40-minute timed task, Flask is the lightest to stand up — a handful of lines gives you a running route, and there's almost no project scaffolding to fight. Django makes you deal with settings, app layout, URL configs, migrations, and the ORM before you write any real logic; that overhead is a tax you can't afford in 40 minutes.

Caveats worth weighing:
- **If you're genuinely fast in Spring Boot from day-job Java, pick it** — fluency beats "lighter framework." But if the choice is "Python because it's easier," then Flask over Django, clearly.
- Because the AI co-pilot writes boilerplate for you, framework ceremony matters less than your ability to **read and correct** what it produces. Pick the stack whose output you can evaluate fastest. For you that's Python/Flask.
- **Decide before test day and drill it.** Don't discover Flask's request parsing or JSON responses mid-exam.

Minimum Flask you should be able to write from memory before the test:
- A `GET` and a `POST` route, reading JSON body and query params.
- Returning JSON with the right status code (200/201/400/404).
- Input validation and an error path (return 400 on bad input).
- A tiny in-memory store (dict) standing in for a DB, and one `pytest` test hitting the route via the test client.

---

## How to practice each component

**1. Medium DSA (both companies' HackerRank).** Keep the current workflow: one file per problem, tests inline or via `test_solution.py`, working solution in ≤25 min, then optimize and state complexity. Favor hash map, sliding window, intervals, heap, binary search, graph (BFS/DFS, topo sort, Dijkstra), stack, and DP/greedy basics.

**2. SQL (Wise only).** New — not yet covered. Drill: joins, `GROUP BY`/`HAVING`, aggregates, subqueries, window functions (`ROW_NUMBER`, `RANK`, running totals), self-joins, nth-highest, date filtering. Use HackerRank's SQL track or LeetCode's SQL 50. Save queries under `2026-MM-DD/sql_<topic>/query.sql` with a note on the problem.

**3. MCQ knowledge — closed-book, so actually study (Deliveroo §1).** Three buckets:
- *General engineering:* HTTP verbs/status codes, REST idempotency, concurrency (race conditions, locks, deadlock), DB indexing/transactions/isolation levels, caching, Big-O.
- *System design:* load balancing, queues, caching strategies, CAP, SQL vs NoSQL, sharding/replication, horizontal vs vertical scaling.
- *Testing:* test pyramid (unit/integration/e2e), test doubles (mock vs stub vs fake vs spy), TDD, coverage, flaky tests, black/white-box.
Make a one-page cheat-sheet per bucket and self-quiz. No AI allowed here, so this is pure recall.

**4. AI-assisted API building — the Deliveroo differentiator (§2).** This is the drill most people skip. Do timed 40-min "build a small API with an AI co-pilot" sessions:
- Pick a scenario (list below), open a scratch Flask project, and use an AI assistant exactly as you would in the test.
- Practice the loop: **crisp prompt → read the output critically → prompt a refinement → add a test → verify.** Keep a short log of prompts that worked well.
- Deliberately catch at least one AI mistake per session (missing validation, wrong status code, off-by-one, no error handling) and correct it. That's the graded skill.
- Scenarios: order-status endpoint, menu CRUD, basket/price calculator with discounts, rider-assignment endpoint, rate-limited endpoint, idempotent payment endpoint.

**5. Practical / design classes (both).** Wallet (deposit/withdraw/transfer with `Decimal` + validation), LRU cache, rate limiter (token bucket), circuit breaker, currency converter with TTL cache, in-memory KV store with TTL, retry-with-backoff. Keep them easy to extend — "add a feature" follow-ups are common.

**6. System design (both).** Practice out loud, 30–45 min, whiteboard-style: payment transfer (Wise), delivery-driver dispatch (Deliveroo). Drive requirements → API → data model → scaling → trade-offs. Keep trade-offs simple and defensible.

**7. Behavioral / STAR (both).** Write 6–8 stories (conflict, failure, ownership, mentoring, tough trade-off, impact). Wise has an explicit product-mindset + values round; Deliveroo ends on STAR.

---

## Daily routine (~2 hrs)

- **2 DSA problems** (one of which is SQL ~3×/week for Wise).
- **1 practical/design or AI-pairing session** — alternate days: practical class one day, 40-min AI-assisted Flask build the next.
- **10 min MCQ cheat-sheet review** (rotate engineering / design / testing).

Generate and run:
```
sh file_generator.sh 2026-MM-DD leetcode_<N>
sh t_e.sh 2026-MM-DD/leetcode_<N>
```

---

## 3-week plan

Legend: **DSA** = algorithm problem · **SQL** = Wise SQL drill · **API+AI** = timed 40-min Flask build with AI co-pilot · **Design** = practical class · **MCQ** = study block.

| Done | Day | Item 1 | Item 2 | Item 3 |
|---|---|---|---|---|
| [ ] | 1 | DSA 347 Top K Frequent | Design: Wallet (`Decimal`, validate, transfer) | MCQ: testing pyramid + test doubles |
| [ ] | 2 | DSA 56 Merge Intervals | API+AI: order-status GET/POST endpoint | MCQ: HTTP/REST + status codes |
| [ ] | 3 | DSA 253 Meeting Rooms II | SQL: joins + GROUP BY/HAVING | MCQ: DB indexing + transactions |
| [ ] | 4 | DSA 981 Time-Based KV Store | Design: 146 LRU Cache | MCQ: caching strategies |
| [ ] | 5 | DSA 200 Number of Islands | API+AI: menu CRUD + validation | MCQ: concurrency basics |
| [ ] | 6 | DSA 33 Search in Rotated Array | SQL: window functions (ROW_NUMBER, running total) | MCQ: load balancing + queues |
| [ ] | 7 | Review 3 weakest problems | System design mock: payment transfer (Wise) | — |
| [ ] | 8 | DSA 207 Course Schedule | Design: rate limiter (token bucket) | MCQ: CAP + SQL vs NoSQL |
| [ ] | 9 | DSA 994 Rotting Oranges | API+AI: basket price calc w/ discounts | MCQ: sharding + replication |
| [ ] | 10 | DSA 743 Network Delay Time | SQL: subqueries + nth-highest | MCQ: isolation levels |
| [ ] | 11 | DSA 322 Coin Change | Design: circuit breaker | MCQ: idempotency + retries |
| [ ] | 12 | DSA 739 Daily Temperatures | API+AI: idempotent payment endpoint | MCQ: review weak buckets |
| [ ] | 13 | DSA 300 Longest Increasing Subseq | Design: currency converter + TTL cache | STAR: write 3 stories |
| [ ] | 14 | Review weakest topics | System design mock: delivery dispatch (Deliveroo) | STAR: write 3 more stories |
| [ ] | 15 | DSA 215 Kth Largest | API+AI: rider-assignment endpoint (heap) | MCQ: full §1 self-quiz (15 Qs) |
| [ ] | 16 | DSA 98 Validate BST | SQL: self-joins + date filtering | MCQ: timed 15-MCQ mock |
| [ ] | 17 | DSA 139 Word Break | Design: in-memory KV store + TTL | STAR: refine stories out loud |
| [ ] | 18 | DSA 621 Task Scheduler | API+AI: rate-limited endpoint | System design: financial system Q |
| [ ] | 19 | **Full Deliveroo mock**: 20-min 15-MCQ (no AI) + 40-min Flask build (with AI) | | |
| [ ] | 20 | **Full Wise mock**: HackerRank-style — 1 SQL + 2 algos timed | Pair-programming sim: circuit breaker | |
| [ ] | 21 | Review everything; redo your 3 worst performers; reread cheat-sheets | | |

---

## Topic coverage this term

- [x] Two pointers (80, 167)
- [x] Array in-place (189)
- [x] Hash map / set (128, 49)
- [x] Sliding window (209)
- [x] Prefix sum / hash map (560)
- [ ] Intervals
- [ ] Heap
- [ ] Binary search
- [ ] Graph (BFS/DFS, topological sort, Dijkstra)
- [ ] Stack / monotonic stack
- [ ] Tree / BFS level order
- [ ] DP and greedy
- [ ] **SQL** (joins, aggregates, window fns, subqueries) — Wise
- [ ] Design classes (LRU, rate limiter, circuit breaker, wallet, currency, KV+TTL)
- [ ] **Flask API building + AI pairing** — Deliveroo §2
- [ ] **MCQ: engineering / system design / testing** — Deliveroo §1 (closed-book)
- [ ] System design (payment transfer, delivery dispatch)
- [ ] Behavioral STAR (6–8 stories)
