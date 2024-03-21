import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_findSubstring(self):
        solution = Solution()

        result = solution.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"])
        self.assertEqual(result, [0,9])

        result = solution.findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"])
        self.assertEqual(result, [])

        result = solution.findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"])
        self.assertEqual(result, [6,9,12])

        result = solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
        self.assertEqual(result, [8])

        result = solution.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
        self.assertEqual(result, [13])

        result = solution.findSubstring("aaaaaaaaaaaaaa", ["aa","aa"])
        self.assertEqual(result, [0,1,2,3,4,5,6,7,8,9,10])