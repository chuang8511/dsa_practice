class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        operation = 0
        while l < r:
            if nums[l] + nums[r] == k:
                operation += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return operation




test_cases = [
    {
        "nums": [1,2,3,4],
        "k": 5
    },
    {
        "nums": [3,1,3,4,3],
        "k": 6
    }
]
solution = Solution()
for case in test_cases:
    print(case["nums"])
    print(solution.maxOperations(case["nums"], case["k"]))
    