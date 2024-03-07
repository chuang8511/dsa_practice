import unittest
from solution import Solution
from linked_list import LinkedListBuilder

class TestSolution(unittest.TestCase):
    def test_pairSum(self):
        solution = Solution()

        builder = LinkedListBuilder()
        input_linked_list = builder.build([5,4,2,1])
        result = solution.pairSum(input_linked_list)
        self.assertEqual(result, 6)

        builder = LinkedListBuilder()
        input_linked_list = builder.build([4,2,2,3])
        result = solution.pairSum(input_linked_list)
        self.assertEqual(result, 7)

        builder = LinkedListBuilder()
        input_linked_list = builder.build([1,100000])
        result = solution.pairSum(input_linked_list)
        self.assertEqual(result, 100001)