import pdb
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            if k == 0 and nums[0] == 0:
                return 0
            else:
                return 1

        self.maxi = 0

        l, r = 0, 0
        zero_count = 1 if nums[l] == 0 else 0
        while r < len(nums) - 1:
            r += 1
            if nums[r] == 0:
                zero_count += 1
                if zero_count <= k:
                    length = r - l + 1
                    self.maxi = max(self.maxi, length)
                else:
                    while l <= r and zero_count > k:
                        if nums[l] == 0:
                            zero_count -= 1
                        l += 1    
            else:
                if zero_count <= k:
                    length = r - l + 1
                    self.maxi = max(self.maxi, length)
                elif zero_count > k and nums[l] == 0:
                        zero_count -= 1
                        l += 1
                
        return self.maxi