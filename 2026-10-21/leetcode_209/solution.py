class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        sumup = 0
        result = float('inf')

        for r in range(len(nums)):
            sumup += nums[r]
            while sumup >= target:
                result = min(result, r - l + 1)
                sumup -= nums[l]
                l += 1
        return 0 if result == float('inf') else result












if __name__ == "__main__":
    cases = [
        (7, [2,3,1,2,4,3], 2),
        (4, [1,4,4], 1),
        (11, [1,1,1,1,1,1,1,1], 0),
        (7, [5], 0)
    ]

    for target, number, expected in cases:
        result = Solution().minSubArrayLen(target, number)
        if result != expected:
            raise AssertionError(f"case: {target}, number: {number}, result: {result}")
    print("All tests passed")