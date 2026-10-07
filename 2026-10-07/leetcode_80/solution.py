class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i


if __name__ == "__main__":
    cases = [
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
        ([1], 1, [1]),
        ([], 0, []),
    ]

    for nums, expected_k, expected_nums in cases:
        k = Solution().removeDuplicates(nums)
        if k != expected_k:
            raise AssertionError(f"fail at {nums}: got {k}, expected {expected_k}")
        if nums[:k] != expected_nums:
            raise AssertionError(f"fail at {nums}: got {nums[:k]}, expected {expected_nums}")

    print("All tests passed")

