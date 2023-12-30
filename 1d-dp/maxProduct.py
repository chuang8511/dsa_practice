# product case
# Postive
# Negative
# Edge case: 0
# Set min & max info
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        cur_max, cur_min = 1, 1

        for n in nums:
            if n == 0: 
                cur_max, cur_min = 1, 1
                continue
            temp = cur_max * n
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(temp, cur_min * n, n)

            res = max(cur_max, res)
        return res