class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longestLength = 0
        for i in nums:
            # to make sure it is a start number
            if i - 1 not in numSet:
                length = 0
                while i + length in numSet:
                    length += 1
                
                longestLength = max(length, longestLength)
        return longestLength




test_cases = [
    [100,4,200,1,3,2],
    [0,3,7,2,5,8,4,6,0,1],
]
solution = Solution()

for test_case in test_cases:
    result = solution.longestConsecutive(test_case)
    print(result)