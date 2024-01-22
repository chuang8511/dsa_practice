import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_closeStrings(self):
        solution = Solution()

        result = solution.closeStrings("abc", "bca")
        self.assertEqual(result, True)

        result = solution.closeStrings(word1 = "a", word2 = "aa")
        self.assertEqual(result, False)

        result = solution.closeStrings(word1 = "cabbba", word2 = "abbccc")
        self.assertEqual(result, True)

        result = solution.closeStrings(word1 = "aaabbbbccddeeeeefffff", word2 = "aaaaabbcccdddeeeeffff")
        self.assertEqual(result, False)