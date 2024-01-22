class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        all_sum = 0
        
        for num in nums:
            all_sum += num
        
        left_sum = 0
        right_sum = all_sum - nums[0]
        
        if left_sum == right_sum:
            return 0

        for idx in range(1, len(nums)):
            left_sum += nums[idx - 1]
            right_sum -= nums[idx]
            
            if left_sum == right_sum:
                return idx
        return -1