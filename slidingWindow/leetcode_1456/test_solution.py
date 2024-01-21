import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_maxVowels(self):
        solution = Solution()

        result = solution.maxVowels("abciiidef", 3)
        self.assertEqual(result, 3)

        result = solution.maxVowels("aeiou", 2)
        self.assertEqual(result, 2)

        result = solution.maxVowels("leetcode", 3)
        self.assertEqual(result, 2)