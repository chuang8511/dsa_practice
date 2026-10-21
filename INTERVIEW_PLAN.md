# Wise & Deliveroo Interview Prep Plan

Started: 2026-10-21. Tick the boxes as you go, then commit and push so any machine stays in sync.

Current practice lives in the `2026-MM-DD/leetcode_N/solution.py` directories. The older topic folders are earlier practice.

Already done in this term: LC 80, 189, 128, 49, 167, 209.

## What to expect (anecdotal, from Glassdoor and third-party guides, researched 2026-10-21)

**Wise**
- HackerRank-style test (~90 min): OOP multiple-choice questions plus 2 coding problems (algorithms, sometimes SQL). Mid-level difficulty.
- Pair programming on a practical problem, not competitive programming. Reported examples: circuit-breaker component, transaction processing, currency conversion with caching.
- System design (e.g. payment system), mainly for senior roles.
- Reviewers look at tests, error handling and naming.

**Deliveroo**
- HackerRank-style test (60-90 min) and/or a take-home assignment.
- Live code review or pairing on the take-home: add a feature, discuss tests and improvements.
- Algorithms: LeetCode medium (DP, greedy), occasionally hard (e.g. LC 301).
- Practical system design (e.g. delivery-driver app). Simple, defensible trade-offs.
- Behavioral (STAR) round last.

**Takeaway:** medium-level DSA, plus clean, tested, extensible practical code, system design and behavioral stories.

## Daily routine

About 3 problems a day: 2 DSA and 1 practical/design problem.

For every problem:
1. Write tests first, including edge cases (empty input, duplicates, negatives, invalid input).
2. State your assumptions out loud.
3. Aim for a working solution in 25 min or less, then optimise and explain complexity.
4. For practical problems, keep the code easy to extend, since follow-up "add a feature" questions are common.

Generate and run:
```
sh file_generator.sh <type_of_problem> leetcode_<N>
sh t_e.sh <type_of_problem>/leetcode_<N>
```

## 14-day plan

| Done | Day | DSA 1 | DSA 2 | Practical / design |
|---|---|---|---|---|
| [ ] | 1 | 560 Subarray Sum Equals K | 347 Top K Frequent | Wallet class: deposit, withdraw, transfer, with `Decimal` and validation |
| [ ] | 2 | 56 Merge Intervals | 253 Meeting Rooms II | 146 LRU Cache |
| [ ] | 3 | 981 Time-Based KV Store | 33 Search in Rotated Array | 362 Hit Counter |
| [ ] | 4 | 200 Number of Islands | 994 Rotting Oranges | Currency converter: rates, caching, TTL |
| [ ] | 5 | 207 Course Schedule | 743 Network Delay Time | Rate limiter (token bucket) |
| [ ] | 6 | 20 Valid Parentheses | 739 Daily Temperatures | Circuit breaker |
| [ ] | 7 | Review: redo the 3 problems you struggled with most | | Mock system design: payment transfer |
| [ ] | 8 | 322 Coin Change | 300 Longest Increasing Subsequence | Transactions list: group by account, compute balances |
| [ ] | 9 | 55 Jump Game | 621 Task Scheduler | Order dispatch: match riders to orders with a heap |
| [ ] | 10 | 215 Kth Largest | 973 K Closest Points | Mini in-memory key-value store with TTL |
| [ ] | 11 | 98 Validate BST | 102 Level Order | 21 Merge Two Sorted Lists |
| [ ] | 12 | 139 Word Break | 72 Edit Distance | Retry with backoff (idempotent payment call) |
| [ ] | 13 | 301 Remove Invalid Parentheses | 322 or 518 again | Timed mock: 60-minute practical problem with tests |
| [ ] | 14 | Review: weakest topics | | System design mock (delivery app) plus behavioral stories |

## Topic coverage in this term

Update this as you go.

- [x] Two pointers (80, 167)
- [x] Array in-place (189)
- [x] Hash map / set (128, 49)
- [x] Sliding window (209)
- [ ] Prefix sum / hash map
- [ ] Intervals
- [ ] Heap
- [ ] Binary search
- [ ] Graph (BFS/DFS, topological sort, Dijkstra)
- [ ] Stack
- [ ] Tree
- [ ] DP and greedy
- [ ] Design problems (LRU, rate limiter, circuit breaker, wallet)
- [ ] System design (payment transfer, delivery app)
- [ ] Behavioral stories (STAR)
