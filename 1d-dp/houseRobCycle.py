class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def collect_max_money(house_moneys):
            rob1, rob2 = 0, 0

            for n in house_moneys:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(collect_max_money(nums[0:-1]), collect_max_money(nums[1:]))