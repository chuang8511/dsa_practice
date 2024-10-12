class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        i = 0
        while i < len(nums) and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            l, r = (i + 1), (len(nums) - 1)
            while l < r:
                target = nums[i] * -1
                sum = nums[l] + nums[r]
                if target == sum:
                    sorted_triplets = [nums[i], nums[l], nums[r]]
                    result.append(sorted_triplets)
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1
                elif target < sum:
                    r -= 1
                else:
                    l += 1
            i += 1
        return result
    



test_cases = [
    [-1,0,1,2,-1,-4],
    [0,1,1],
    [0,0,0],
    [0,0,0,0],
    [-2,0,1,1,2]
]

solution = Solution()

for case in test_cases:
    print(solution.threeSum(case))