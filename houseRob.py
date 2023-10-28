class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, n+2, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


test_cases = [
    [1,2,3,1],
    [2,7,9,3,1],
]
solution = Solution()

for test_case in test_cases:
    result = solution.rob(test_case)
    print(result)