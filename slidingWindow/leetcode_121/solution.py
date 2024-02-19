class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        self.max_profit = 0
        l, r = 0, 1
        
        while r < len(prices):
            profit = prices[r] - prices[l]
            self.max_profit = max(profit, self.max_profit)

            if prices[l] > prices[r]:
                l = r
            r += 1
        return self.max_profit
        