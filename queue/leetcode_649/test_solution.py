import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_predictPartyVictory(self):
        solution = Solution()

        result = solution.predictPartyVictory("RDD")
        self.assertEqual(result, "Dire")

        result = solution.predictPartyVictory("RD")
        self.assertEqual(result, "Radiant")

        result = solution.predictPartyVictory("RRDDD")
        self.assertEqual(result, "Radiant")

        result = solution.predictPartyVictory("RRR")
        self.assertEqual(result, "Radiant")

        result = solution.predictPartyVictory("DRRD")
        self.assertEqual(result, "Dire")
