class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        
        self.maxi = 0

        l, r = 0, 0
        zero_count = 1 if nums[l] == 0 else 0
        num_count = 1 if nums[l] == 1 else 0
        while l <= r and r < len(nums) - 1:
            r += 1
            if nums[r] == 0:
                zero_count += 1
                if zero_count > 1:
                    while l <= r and zero_count > 1:
                        if nums[l] == 0:
                            zero_count -= 1
                        else:
                            num_count -= 1
                        l += 1
                else:
                    self.maxi = max(self.maxi, num_count)
            else:
                num_count += 1
                self.maxi = max(self.maxi, num_count)
            
        return self.maxi if num_count != len(nums) else self.maxi - 1
    
# please refer to the simpler code.
# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         n = len(nums)

#         left = 0
#         zeros = 0
#         ans = 0

#         for right in range(n):
#             if nums[right] == 0:
#                 zeros += 1

#             while zeros > 1:
#                 if nums[left] == 0:
#                     zeros -= 1
#                 left += 1

#             ans = max(ans, right - left + 1 - zeros)

#         return ans - 1 if ans == n else ans