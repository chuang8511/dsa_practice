import unittest
from solution import Solution 

class TestSolution(unittest.TestCase):
    def test_gcdOfStrings(self):
        solution = Solution()

        result = solution.gcdOfStrings("ABCABC", "ABC")
        self.assertEqual(result, "ABC")

        result = solution.gcdOfStrings("ABABAB", "ABAB")
        self.assertEqual(result, "AB")

        result = solution.gcdOfStrings("LEET", "CODE")
        self.assertEqual(result, "")
