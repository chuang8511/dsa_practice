import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_findPeakElement(self):
        solution = Solution()

        result = solution.findPeakElement(nums = [1,2,3,1])
        self.assertEqual(result, 2)

        result = solution.findPeakElement(nums = [1,2,1,3,5,6,4])
        self.assertEqual(result, 5)