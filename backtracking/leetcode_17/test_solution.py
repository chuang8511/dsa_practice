import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_letterCombinations(self):
        solution = Solution()

        result = solution.letterCombinations("23")
        self.assertEqual(result, ["ad","ae","af","bd","be","bf","cd","ce","cf"])

        result = solution.letterCombinations("")
        self.assertEqual(result, [])

        result = solution.letterCombinations("2")
        self.assertEqual(result, ["a","b","c"])