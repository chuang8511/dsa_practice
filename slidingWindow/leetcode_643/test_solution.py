import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_findMaxAverage(self):
        solution = Solution()

        result = solution.findMaxAverage([1,12,-5,-6,50,3], 4)
        self.assertEqual(result, 12.75000)

        result = solution.findMaxAverage([5], 1)
        self.assertEqual(result, 5.00000)