import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_minEatingSpeed(self):
        solution = Solution()

        result = solution.minEatingSpeed(piles = [3,6,7,11], h = 8)
        self.assertEqual(result, 4)

        result = solution.minEatingSpeed(piles = [30,11,23,4,20], h = 5)
        self.assertEqual(result, 30)

        result = solution.minEatingSpeed(piles = [30,11,23,4,20], h = 6)
        self.assertEqual(result, 23)