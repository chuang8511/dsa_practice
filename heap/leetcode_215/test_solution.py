import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_findKthLargest(self):
        solution = Solution()

        result = solution.findKthLargest([3,2,1,5,6,4], 2)
        self.assertEqual(result, 5)

        result = solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
        self.assertEqual(result, 4)