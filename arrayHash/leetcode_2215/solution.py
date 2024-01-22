from collections import defaultdict
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ans = []
        set1, set2 = set(nums1), set(nums2)

        ans.append(list(set1 - set2))
        ans.append(list(set2 - set1))

        return ans