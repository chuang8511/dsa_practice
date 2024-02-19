import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_maxProfit(self):
        solution = Solution()

        result = solution.maxProfit([7,1,5,3,6,4])
        self.assertEqual(result, 5)

        result = solution.maxProfit([7,6,4,3,1])
        self.assertEqual(result, 0)

        # result = solution.maxProfit()
        # self.assertEqual(result, 0)