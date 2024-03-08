import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_totalCost(self):
        solution = Solution()

        # result = solution.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4)
        # self.assertEqual(result, 11)

        # result = solution.totalCost(costs = [1,2,4,1], k = 3, candidates = 3)
        # self.assertEqual(result, 4)

        result = solution.totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], k = 11, candidates = 2)
        self.assertEqual(result, 423)

        # result = solution.totalCost([25,65,41,31,14,20,59,42,43,57,73,45,30,77,17,38,20,11,17,65,55,85,74,32,84], k = 24, candidates = 8)
        # self.assertEqual(result, 1035)