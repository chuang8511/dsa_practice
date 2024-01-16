import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_productExceptSelf(self):
        solution = Solution()

        result = solution.productExceptSelf([1,2,3,4])
        self.assertEqual(result, [24,12,8,6])

        result = solution.productExceptSelf([-1,1,0,-3,3])
        self.assertEqual(result, [0,0,9,0,0])