import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_maxScore(self):
        solution = Solution()

        result = solution.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3)
        self.assertEqual(result, 12)

        result = solution.maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1)
        self.assertEqual(result, 30)