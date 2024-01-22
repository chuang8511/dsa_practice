import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_equalPairs(self):
        solution = Solution()

        result = solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]])
        self.assertEqual(result, 1)

        result = solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])
        self.assertEqual(result, 3)