import heapq
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        print(f"input: {costs}")
        res = 0
        if len(costs) >= 2 * candidates:
            first_candidates = costs[0:candidates]
            last_candidates = costs[-candidates:]
            heapq.heapify(first_candidates)
            heapq.heapify(last_candidates)

        while k > 0 and len(costs) >= 2 * candidates:
            print(f"cost: {costs}")
            print(f"len: {len(costs)}")
            # print(f"k: {k}")
            print(f"first_candidates: {first_candidates}")
            print(f"last_candidates: {last_candidates}")
            
            first_min = first_candidates[0]
            last_min = last_candidates[0]
            if first_min <= last_min:
                cost = heapq.heappop(first_candidates)
                res += cost
                costs.remove(cost)
                heapq.heappush(first_candidates, costs[candidates - 1])
            else:
                cost = heapq.heappop(last_candidates)
                res += cost
                costs.reverse()
                costs.remove(cost)
                costs.reverse()
                heapq.heappush(last_candidates, costs[-candidates])
            k -= 1
            print("=======")
        
        heapq.heapify(costs)

        while k > 0:
            cost = heapq.heappop(costs)
            res += cost
            k -= 1
        
        return res