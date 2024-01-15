import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_reverseWords(self):
        solution = Solution()

        result = solution.reverseWords("the sky is blue")
        self.assertEqual(result, "blue is sky the")

        result = solution.reverseWords("  hello world  ")
        self.assertEqual(result, "world hello")

        result = solution.reverseWords("a good   example")
        self.assertEqual(result, "example good a")