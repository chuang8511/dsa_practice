import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_tribonacci(self):
        solution = Solution()

        result = solution.tribonacci(4)
        self.assertEqual(result, 4)

        result = solution.tribonacci(25)
        self.assertEqual(result, 1389537)