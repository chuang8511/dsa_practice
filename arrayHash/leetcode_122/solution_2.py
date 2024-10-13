#                  -
# -        -    -
#   -    -    -
#     -
# Greedy Solution
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        start_price = prices[0]
        i = 1
        while i < len(prices):
            if start_price <= prices[i]:
                profit += prices[i] - start_price
            start_price = prices[i]
            i += 1
        return profit

test_cases = [
    [2,1,2,1,0,0,1],
    [2,1,2,0,1],
    [6,1,3,2,4,7],
    [7,1,5,3,6,4],
    [1,2,3,4,5],
    [7,6,4,3,1]
]


solution = Solution()

for case in test_cases:
    print(solution.maxProfit(case))