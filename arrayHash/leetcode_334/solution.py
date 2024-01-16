class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        mini, mid = float("inf"), float("inf")

        for i in nums:
            if i <= mini:
                mini = i
            elif i <= mid:
                mid = i
            else:
                return True
        return False
