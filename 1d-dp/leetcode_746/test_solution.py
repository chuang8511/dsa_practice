import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_minCostClimbingStairs(self):
        solution = Solution()

        result = solution.minCostClimbingStairs([10,15,20])
        self.assertEqual(result, 15)

        result = solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
        self.assertEqual(result, 6)