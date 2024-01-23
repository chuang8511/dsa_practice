import unittest
from solution import RecentCounter

class TestSolution(unittest.TestCase):
    def test_ping(self):
        recentCounter = RecentCounter()

        result = recentCounter.ping(1)
        self.assertEqual(result, 1)

        result = recentCounter.ping(100)
        self.assertEqual(result, 2)

        result = recentCounter.ping(3001)
        self.assertEqual(result, 3)

        result = recentCounter.ping(3002)
        self.assertEqual(result, 3)