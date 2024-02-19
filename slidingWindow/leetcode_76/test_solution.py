import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_minWindow(self):
        solution = Solution()

        s = "ADOBECODEBANC"
        t = "ABC"
        result = solution.minWindow(s, t)
        self.assertEqual(result, "BANC")

        s = "a"
        t = "a"
        result = solution.minWindow(s, t)
        self.assertEqual(result, "a")

        s = "a"
        t = "aa"
        result = solution.minWindow(s, t)
        self.assertEqual(result, "")