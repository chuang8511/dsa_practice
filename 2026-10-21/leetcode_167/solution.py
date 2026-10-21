class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        












if __name__ == "__main__":
    cases = [
        ([2,7,11,15], 9, [1,2]),
        ([2,3,4], 6, [1,3]),
        ([-1,0], -1, [1,2]),
    ]

    for nums, k, expected in cases:
        result = Solution().twoSum(nums, k)
        if result != expected:
            raise AssertionError(f"case: {nums}, k: {k}")
    print("All tests passed")