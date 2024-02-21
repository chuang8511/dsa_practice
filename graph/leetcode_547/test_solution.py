import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_findCircleNum(self):
        solution = Solution()

        result = solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
        self.assertEqual(result, 2)

        result = solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
        self.assertEqual(result, 3)

        result = solution.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
        self.assertEqual(result, 1)