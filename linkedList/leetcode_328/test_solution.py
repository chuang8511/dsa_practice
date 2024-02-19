import unittest
from solution import Solution
from linked_list import LinkedListBuilder

class TestSolution(unittest.TestCase):
    def test_oddEvenList(self):
        solution = Solution()

        builder = LinkedListBuilder()
        input_linked_list = builder.build([1,2,3,4,5])
        result = solution.oddEvenList(input_linked_list)
        result_arr = builder.debuild(result)
        self.assertEqual(result_arr, [1,3,5,2,4])

        input_linked_list = builder.build([2,1,3,5,6,4,7])
        result = solution.oddEvenList(input_linked_list)
        result_arr = builder.debuild(result)
        self.assertEqual(result_arr, [2,3,6,7,1,5,4])