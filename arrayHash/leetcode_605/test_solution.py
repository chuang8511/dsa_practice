import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_canPlaceFlowers(self):
        solution = Solution()

        result = solution.canPlaceFlowers([1,0,0,0,1], 1)
        self.assertEqual(result, True)

        result = solution.canPlaceFlowers([1,0,0,0,1], 2)
        self.assertEqual(result, False)

        result = solution.canPlaceFlowers([0], 1)
        self.assertEqual(result, True)

        result = solution.canPlaceFlowers([1], 0)
        self.assertEqual(result, True)