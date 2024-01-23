import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_decodeString(self):
        solution = Solution()

        result = solution.decodeString("3[a]2[bc]")
        self.assertEqual(result, "aaabcbc")

        result = solution.decodeString("3[a2[c]]")
        self.assertEqual(result, "accaccacc")

        result = solution.decodeString("3[2[a]2[c]]")
        self.assertEqual(result, "aaccaaccaacc")

        result = solution.decodeString("2[abc]3[cd]ef")
        self.assertEqual(result, "abcabccdcdcdef")

        result = solution.decodeString("100[leetcode]")
        self.assertEqual(result, "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode")