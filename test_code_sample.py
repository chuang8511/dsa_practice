import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_method(self):
        solution = Solution()

        result = solution.test_method()
        self.assertEqual(result, 0)

        result = solution.test_method()
        self.assertEqual(result, 0)

        result = solution.test_method()
        self.assertEqual(result, 0)