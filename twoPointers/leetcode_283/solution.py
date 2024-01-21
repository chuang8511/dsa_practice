class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # # solution 1
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.remove(0)
        #         nums.append(0)

        # solution 2
        idx = 0
        for n in nums:
            if n != 0:      
                nums[idx] = n
                idx += 1

        while idx < len(nums):
            nums[idx] = 0
            idx += 1