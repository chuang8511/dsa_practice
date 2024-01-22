import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_pivotIndex(self):
        solution = Solution()
        
        result = solution.pivotIndex([1,7,3,6,5,6])
        self.assertEqual(result, 3)

        result = solution.pivotIndex([1,2,3])
        self.assertEqual(result, -1)

        result = solution.pivotIndex([2,1,-1])
        self.assertEqual(result, 0)