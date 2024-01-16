class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        res = [1] * length

        # product prefix
        for i in range(1, length):
            res[i] = nums[i-1] * res[i-1]

        postfix = 1
        for i in range(length - 1, -1, -1):            
            res[i] = res[i] * postfix
            postfix *= nums[i]
        
        return res