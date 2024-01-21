import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_moveZeroes(self):
        solution = Solution()

        nums = [0,1,0,3,12]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [1,3,12,0,0])

        nums = [0]
        solution.moveZeroes(nums)
        self.assertEqual(nums, [0])