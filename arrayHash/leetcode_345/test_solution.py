import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_reverseVowels(self):

        solution = Solution()

        result = solution.reverseVowels("hello")
        self.assertEqual(result, "holle")

        result = solution.reverseVowels("leetcode")
        self.assertEqual(result, "leotcede")

        result = solution.reverseVowels("aA")
        self.assertEqual(result, "Aa")