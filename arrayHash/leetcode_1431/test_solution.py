import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_kidsWithCandies(self):
        solution = Solution()

        result = solution.kidsWithCandies([2,3,5,1,3], 3)
        self.assertEqual(result, [True,True,True,False,True])

        result = solution.kidsWithCandies([4,2,1,1,2], 1)
        self.assertEqual(result, [True,False,False,False,False])

        result = solution.kidsWithCandies([12,1,12], 10)
        self.assertEqual(result, [True,False,True])