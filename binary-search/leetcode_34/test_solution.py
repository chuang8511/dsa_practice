import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_searchRange(self):
        solution = Solution()

        result = solution.searchRange(nums = [5,7,7,8,8,10], target = 8)
        self.assertEqual(result, [3,4])

        result = solution.searchRange(nums = [5,7,7,8,8,10], target = 6)
        self.assertEqual(result, [-1,-1])

        result = solution.searchRange(nums = [], target = 0)
        self.assertEqual(result, [-1,-1])

        result = solution.searchRange(nums = [1], target = 1)
        self.assertEqual(result, [0,0])

        result = solution.searchRange(nums = [2,2], target = 3)
        self.assertEqual(result, [-1,-1])