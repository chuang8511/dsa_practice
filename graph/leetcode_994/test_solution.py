import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_orangesRotting(self):
        solution = Solution()

        result = solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
        self.assertEqual(result, 4)

        result = solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
        self.assertEqual(result, -1)

        result = solution.orangesRotting([[0,2]])
        self.assertEqual(result, 0)

        result = solution.orangesRotting([[1]])
        self.assertEqual(result, -1)

        result = solution.orangesRotting([[0]])
        self.assertEqual(result, 0)

        result = solution.orangesRotting([[2,1,1],[1,1,1],[0,1,2]])
        self.assertEqual(result, 2)
        