class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        set_nums = set(nums)
        for n in set_nums:
            if (n-1) not in set_nums:
                length = 1
                while (n+length) in set_nums:
                    length += 1
                longest = max(longest, length)
        return longest
                    





if __name__ == "__main__":
    cases = [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([1,0,1,2], 3)
    ]

    for input_, expected in cases:
        result = Solution().longestConsecutive(input_)
        if result != expected:
            raise AssertionError(f"case: {input_}, result: {result}, expect: {expected}")
    print("All tests passed")