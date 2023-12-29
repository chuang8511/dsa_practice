# Need to solve it again!
# dp = { amount: min_count }
# dp[amount]
from collections import defaultdict
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = defaultdict(lambda: amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        if amount in dp and dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1

        # def collect_dp(collecting_amount, selected_coin, coin_count):
        #     collected_amount = collecting_amount + selected_coin
        #     coin_count += 1
        #     if collected_amount in dp:
        #         dp[collected_amount] = min(coin_count, dp[collected_amount])

        #         for coin in coins:
        #             collect_dp(collected_amount, coin, dp[collected_amount])

        #     if collected_amount > amount:
        #         return
            
        #     dp[collected_amount] = coin_count 

        # collect_dp(0, 0, 0)
        
        # if amount in dp:
        #     return dp[amount]
        # else:
        #     return -1

            
            




        # time limit
        # def collect_coins(amount, collected_coins_count, selected_coin):
        #     remaining_amount = amount - selected_coin
        #     # print(f"amount {amount}")
        #     # print(f"selected_coin {selected_coin}")
        #     # print(f"remaining_amount {remaining_amount}")
        #     # print(f"collected_coins_count {collected_coins_count}")
        #     # print("======================================")
        #     collected_coins_count += 1
        #     if remaining_amount == 0 and (res[0] == -1 or res[0] > collected_coins_count):
        #         res[0] = collected_coins_count
        #     elif remaining_amount < 0:
        #         return
        #     else:             
        #         for coin in coins:
        #             collect_coins(remaining_amount, collected_coins_count, coin)

        # for coin in coins:
        #     collect_coins(amount, 0, coin)

        # return res[0]
    

coins = [1, 2, 5]
amount = 11

solution = Solution()
res = solution.coinChange(coins, amount)
print(res)