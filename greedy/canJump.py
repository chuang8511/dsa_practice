class Solution:
    def canJump(self, nums: list[int]) -> bool:
        latest_able_idx = len(nums) - 1
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] >= latest_able_idx - idx:
                latest_able_idx = idx
            else:
                continue
        return latest_able_idx == 0