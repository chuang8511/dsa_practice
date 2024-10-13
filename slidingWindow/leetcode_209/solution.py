# [2,3,1,2,4,3]
#            p p

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        l, r = 0, 0
        current_sum = nums[l]
        result = float("inf")
        while True:
            if current_sum >= target:
                result = min(r - l + 1, result)
                current_sum -= nums[l]
                l += 1
                if l == len(nums):
                    break
            else:
                r += 1
                if r == len(nums):
                    break
                current_sum += nums[r]
        
        if result == float("inf"):
            return 0
        return result
    

test_cases = [
    {
        "target": 7,
        "nums": [2,3,1,2,4,3]
    },
    {
        "target": 4,
        "nums": [1,4,4]
    },
    {
        "target": 11,
        "nums": [1,1,1,1,1,1,1,1]
    },
    {
        "target": 7,
        "nums": [5]
    },
    {
        "target": 6,
        "nums": [10,2,3]
    },
]

solution = Solution()

for case in test_cases:
    print(solution.minSubArrayLen(case["target"], case["nums"]))