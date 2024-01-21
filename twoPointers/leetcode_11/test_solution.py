import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_maxArea(self):
        solution = Solution()

        result = solution.maxArea([1,8,6,2,5,4,8,3,7])
        self.assertEqual(result, 49)

        result = solution.maxArea([1, 1])
        self.assertEqual(result, 1)