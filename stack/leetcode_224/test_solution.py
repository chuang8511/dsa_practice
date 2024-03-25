import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_calculate(self):
        solution = Solution()

        result = solution.calculate(s = "1 + 1")
        self.assertEqual(result, 2)

        result = solution.calculate(s = " 2-1 + 2 ")
        self.assertEqual(result, 3)

        result = solution.calculate(s = "(1+(4+5+2)-3)+(6+8)")
        self.assertEqual(result, 23)

        result = solution.calculate(s = "1")
        self.assertEqual(result, 1)

        result = solution.calculate(s = "1-(     -2)")
        self.assertEqual(result, 3)