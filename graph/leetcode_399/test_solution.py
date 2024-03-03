import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_calcEquation(self):
        solution = Solution()

        result = solution.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
        self.assertEqual(result, [6.00000,0.50000,-1.00000,1.00000,-1.00000])

        result = solution.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
        self.assertEqual(result, [3.75000,0.40000,5.00000,0.20000])

        result = solution.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]])
        self.assertEqual(result, [0.50000,2.00000,-1.00000,-1.00000])