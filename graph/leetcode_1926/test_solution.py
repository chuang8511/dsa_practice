import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_nearestExit(self):
        solution = Solution()

        result = solution.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2])
        self.assertEqual(result, 1)

        result = solution.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1,0])
        self.assertEqual(result, 2)

        result = solution.nearestExit([[".","+"]], [0,0])
        self.assertEqual(result, -1)

        result = solution.nearestExit([["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+","+","."]], [0,1])
        self.assertEqual(result, -1)