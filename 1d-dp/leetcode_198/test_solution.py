import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_rob(self):
        solution = Solution()

        result = solution.rob([1,2,3,1])
        self.assertEqual(result, 4)

        result = solution.rob([2,7,9,3,1])
        self.assertEqual(result, 12)