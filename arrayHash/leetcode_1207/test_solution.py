import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_uniqueOccurrences(self):
        solution = Solution()

        result = solution.uniqueOccurrences([1,2,2,1,1,3])
        self.assertEqual(result, True)

        result = solution.uniqueOccurrences([1,2])
        self.assertEqual(result, False)

        result = solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
        self.assertEqual(result, True)