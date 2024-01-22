import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_findDifference(self):
        solution = Solution()

        result = solution.findDifference([1,2,3], [2,4,6])
        self.assertEqual(result, [[1,3],[4,6]])

        result = solution.findDifference([1,2,3,3], [1,1,2,2])
        self.assertEqual(result, [[3],[]])