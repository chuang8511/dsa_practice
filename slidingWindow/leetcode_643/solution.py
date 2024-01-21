class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        self.maxi = 0
        k_sum = 0
        for i in range(k):
            k_sum += nums[i]
        l, r = 0, k
        self.maxi = k_sum
        
        while r < len(nums):
            k_sum -= nums[l]
            l += 1
            k_sum += nums[r]
            r += 1
            self.maxi = max(self.maxi, k_sum)

        return self.maxi / k
