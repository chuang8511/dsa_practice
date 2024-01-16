import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_increasingTriplet(self):
        solution = Solution()

        i = 1
        print(f"test case {i}")
        i += 1
        result = solution.increasingTriplet([1,2,3,4,5])
        self.assertEqual(result, True)

        print(f"test case {i}")
        i += 1
        result = solution.increasingTriplet([5,4,3,2,1])
        self.assertEqual(result, False)

        print(f"test case {i}")
        i += 1
        result = solution.increasingTriplet([2,1,5,0,4,6])
        self.assertEqual(result, True)

        print(f"test case {i}")
        i += 1
        result = solution.increasingTriplet([2,4,-2,-3])
        self.assertEqual(result, False)