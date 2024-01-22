import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_asteroidCollision(self):
        solution = Solution()

        result = solution.asteroidCollision([5,10,-5])
        self.assertEqual(result, [5,10])

        result = solution.asteroidCollision([8,-8])
        self.assertEqual(result, [])

        result = solution.asteroidCollision([10,2,-5])
        self.assertEqual(result, [10])

        result = solution.asteroidCollision([-2,-2,1,-2])
        self.assertEqual(result, [-2,-2,-2])

        result = solution.asteroidCollision([-2,2,1,-2])
        self.assertEqual(result, [-2])