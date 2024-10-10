class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]
            elif prices[r] <= prices[l]:
                l = r
            r += 1
        
        return profit

test_cases = [
    [7,1,5,3,6,4],
    [7,6,4,3,1]
]

solution = Solution()
for case in test_cases:
    print(solution.maxProfit(case))
