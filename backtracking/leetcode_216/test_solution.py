import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_combinationSum3(self):
        solution = Solution()

        result = solution.combinationSum3(k = 3, n = 7)
        self.assertEqual(result, [[1,2,4]])

        result = solution.combinationSum3(3, 9)
        self.assertEqual(result, [[1,2,6],[1,3,5],[2,3,4]])

        result = solution.combinationSum3(4, 1)
        self.assertEqual(result, [])