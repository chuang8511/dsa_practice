import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_minReorder(self):
        solution = Solution()

        result = solution.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])
        self.assertEqual(result, 3)

        result = solution.minReorder(5, [[1,0],[1,2],[3,2],[3,4]])
        self.assertEqual(result, 2)

        result = solution.minReorder(3, [[1,0],[2,0]])
        self.assertEqual(result, 0)