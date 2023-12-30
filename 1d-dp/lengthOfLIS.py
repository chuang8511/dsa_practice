class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    # time complexity: O(n^2)
        
        # print(nums)
        # longest_idx, longest_num = 0, nums[0]

        # for idx, num in enumerate(nums):
        #     if num < longest_num:
        #         longest_idx, longest_num = idx, num

        #     if num > longest_num:
        #         dp[idx] = dp[longest_idx] + 1
        #         longest_idx, longest_num = idx, num

        #     if num > nums[idx - 1]:
        #         dp[idx] = max(dp[idx - 1] + 1, dp[idx])

        # return max(dp)

    
# nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
solution = Solution()
res = solution.lengthOfLIS(nums)
print(res)