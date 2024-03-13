import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_numTilings(self):
        solution = Solution()

        result = solution.numTilings(3)
        self.assertEqual(result, 5)

        result = solution.numTilings(1)
        self.assertEqual(result, 1)
    
        result = solution.numTilings(30)
        self.assertEqual(result, 312342182)