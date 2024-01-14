import unittest
from solution import Solution 

class TestSolution(unittest.TestCase):
    
    def test_merge_alternately(self):
        solution = Solution()

        # Test case 1: Equal lengths
        result = solution.mergeAlternately("abc", "def")
        self.assertEqual(result, "adbecf")

        # Test case 2: Unequal lengths
        result = solution.mergeAlternately("ab", "pqrs")
        self.assertEqual(result, "apbqrs")

        # Test case 3: Empty strings
        result = solution.mergeAlternately("", "xyz")
        self.assertEqual(result, "xyz")