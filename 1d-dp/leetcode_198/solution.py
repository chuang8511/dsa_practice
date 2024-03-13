class Solution:
    def rob(self, nums: list[int]) -> int:
        nums += [0,0]
        for i in range(len(nums) - 4, -1, -1):
            nums[i] += max(nums[i+2], nums[i+3])

        return max(nums[0], nums[1])