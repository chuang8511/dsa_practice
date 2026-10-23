from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        prefix = 0
        seen[0] = 1
        count = 0
        for x in nums:
            prefix += x
            count += seen[prefix - k]
            seen[prefix] += 1
        return count
                








if __name__ == "__main__":
    cases = [
        ([1,1,1], 2, 2),
        ([1,2,3], 3, 2),
        ([-1,-1,1], 0, 1)
    ]

    for nums, k, expected in cases:
        result = Solution().subarraySum(nums, k)
        if result != expected:
            raise AssertionError(f"case: {nums}, k: {k}, result: {result}")
    print("All tests passed")