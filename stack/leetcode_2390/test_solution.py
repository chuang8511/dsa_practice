import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_removeStars(self):
        solution = Solution()

        result = solution.removeStars("leet**cod*e")
        self.assertEqual(result, "lecoe")

        result = solution.removeStars("erase*****")
        self.assertEqual(result, "")

        # result = solution.removeStars()
        # self.assertEqual(result, 0)