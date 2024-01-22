import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_longestSubarray(self):
        solution = Solution()

        result = solution.longestSubarray([1,1,0,1])
        self.assertEqual(result, 3)

        result = solution.longestSubarray([0,1,1,1,0,1,1,0,1])
        self.assertEqual(result, 5)

        result = solution.longestSubarray([1,1,1])
        self.assertEqual(result, 2)

        result = solution.longestSubarray([1])
        self.assertEqual(result, 0)