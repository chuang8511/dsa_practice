import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_longestOnes(self):
        solution = Solution()

        result = solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
        self.assertEqual(result, 6)

        result = solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
        self.assertEqual(result, 10)

        result = solution.longestOnes([1,0,1,0], 0)
        self.assertEqual(result, 1)

        result = solution.longestOnes([0,0,0,0], 0)
        self.assertEqual(result, 0)