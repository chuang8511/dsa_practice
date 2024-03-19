class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        if len(nums) == 0:
            return [-1,-1]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2

            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        if l < len(nums) and nums[l] == target:
            temp = l
            while l < len(nums) and nums[l] == target:
                l += 1
            return [temp, l-1]
        else:
            return [-1, -1]