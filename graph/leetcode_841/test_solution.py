import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_canVisitAllRooms(self):
        solution = Solution()

        result = solution.canVisitAllRooms([[1],[2],[3],[]])
        self.assertEqual(result, True)

        result = solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
        self.assertEqual(result, False)
