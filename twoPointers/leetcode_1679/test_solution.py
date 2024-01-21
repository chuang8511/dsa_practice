import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_maxOperations(self):
        solution = Solution()
        
        result = solution.maxOperations([1,2,3,4], 5)
        self.assertEqual(result, 2)

        result = solution.maxOperations([3,1,3,4,3], 6)
        self.assertEqual(result, 1)

        result = solution.maxOperations([2,2,2,3,1,1,4,1], 4)
        self.assertEqual(result, 2)

        result = solution.maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3)
        self.assertEqual(result, 4)