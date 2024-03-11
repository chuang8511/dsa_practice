import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_successfulPairs(self):
        solution = Solution()

        result = solution.successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7)
        self.assertEqual(result, [4,0,3])

        result = solution.successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16)
        self.assertEqual(result, [2,0,2])

        result = solution.successfulPairs(spells = [3,1,2], potions = [8,5,5,8], success = 15)
        self.assertEqual(result, [4,0,2])


        # result = solution.successfulPairs([15,39,38,35,33,25,31,12,40,27,29,16,22,24,7,36,29,34,24,9,11,35,21,3,33,10,9,27,35,17,14,3,35,35,39,23,35,14,31,7], [25,19,30,37,14,30,38,22,38,38,26,33,34,23,40,28,15,29,36,39,39,37,32,38,8,17,39,20,4,39,39,7,30,35,29,23], 317)
        # self.assertEqual(result, [28,33,33,33,33,33,33,23,34,33,33,29,32,33,0,33,33,33,33,13,22,33,31,0,33,17,13,33,33,30,27,0,33,33,33,33,33,27,33,0])