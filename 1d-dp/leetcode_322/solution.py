# dp [min_coin_count], index is the sum_num
# dp[0] = 0
# dp[1] = 1
# dp[2] = 1
# dp[3] = min(dp[1] + dp[2], dp[1] + dp[1] + dp[1])
# dp[11] = ...

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != float("inf") else -1
    




test_cases = [
    {
        "coins": [1,2,5],
        "amount": 11
    },
    {
        "coins": [2],
        "amount": 3
    },
    {
        "coins": [1],
        "amount": 0
    },
    {
        "coins": [1,2,5],
        "amount": 100
    },
]

solution = Solution()

for case in test_cases:
    print(solution.coinChange(case["coins"], case["amount"]))