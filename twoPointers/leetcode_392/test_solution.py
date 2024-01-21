import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_isSubsequence(self):
        solution = Solution()

        result = solution.isSubsequence("abc", "ahbgdc")
        self.assertEqual(result, True)

        result = solution.isSubsequence("axc", "ahbgdc")
        self.assertEqual(result, False)