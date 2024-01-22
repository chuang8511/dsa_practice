import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_largestAltitude(self):
        solution = Solution()

        result = solution.largestAltitude([-5,1,5,0,-7])
        self.assertEqual(result, 1)

        result = solution.largestAltitude([-4,-3,-2,-1,4,3,2])
        self.assertEqual(result, 0)