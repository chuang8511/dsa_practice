import unittest
from solution import SmallestInfiniteSet

class TestSolution(unittest.TestCase):
    def test_method(self):
        smallest = SmallestInfiniteSet()

        result = smallest.addBack(2)
        self.assertEqual(result, None)

        result = smallest.popSmallest()
        self.assertEqual(result, 1)

        result = smallest.popSmallest()
        self.assertEqual(result, 2)

        result = smallest.popSmallest()
        self.assertEqual(result, 3)

        result = smallest.addBack(1)
        self.assertEqual(result, None)

        result = smallest.popSmallest()
        self.assertEqual(result, 1)

        result = smallest.popSmallest()
        self.assertEqual(result, 4)

        result = smallest.popSmallest()
        self.assertEqual(result, 5)