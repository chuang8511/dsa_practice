#           
# -      -
#   -       _
#     -


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        def is_ascending(prices: list[int]) -> bool:
            for i in range(len(prices)):
                if i < len(prices) - 1 and not prices[i] <= prices[i+1]:
                    return False
            return True
        def is_descending(prices: list[int]) -> bool:
            for i in range(len(prices)):
                if i < len(prices) - 1 and not prices[i] >= prices[i+1]:
                    return False
            return True
        if is_ascending(prices):
            return prices[-1] - prices[0]
        if is_descending(prices):
            return 0

        profit = 0
        l, m, r = 0, 1, 2

        buy_price = None
        sell_price = None
        prices = [float("inf"), float("inf")] + prices + [float("-inf"), float("-inf")]
        while r < len(prices):            
            if prices[m] <= prices[l] and prices[m] <= prices[r]:
                buy_price = prices[m]
                l = m 
                m = l + 1
                r = m + 1
            elif prices[m] >= prices[l] and prices[m] >= prices[r] and buy_price is not None:
                sell_price = prices[m]
                l = m 
                m = l + 1
                r = m + 1
            else:
                l += 1
                m += 1
                r += 1
            if buy_price is not None and sell_price is not None:
                profit += sell_price - buy_price
                sell_price = None
                buy_price = None
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