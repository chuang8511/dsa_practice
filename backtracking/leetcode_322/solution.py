# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:
#         if amount == 0:
#             return 0
        
#         self.result = float("inf")
#         def backtracking(current_coins: list[int], target_amount: int):
#             # print(f'current_coins: {current_coins}')
#             if target_amount == 0:
#                 self.result = min(self.result, len(current_coins))
#             else:
#                 for coin in coins:
#                     if target_amount > 0:
#                         backtracking(current_coins + [coin], target_amount - coin)

#         backtracking([], amount)
        
#         if self.result == float("inf"):
#             return -1
        
#         return self.result
    


# test_cases = [
#     {
#         "coins": [1,2,5],
#         "amount": 11
#     },
#     {
#         "coins": [2],
#         "amount": 3
#     },
#     {
#         "coins": [1],
#         "amount": 0
#     },
#     {
#         "coins": [1,2,5],
#         "amount": 100
#     },
# ]

# solution = Solution()

# for case in test_cases:
#     print(solution.coinChange(case["coins"], case["amount"]))