import unittest
from solution import Solution
from linked_list import LinkedListBuilder

class TestSolution(unittest.TestCase):
    def test_deleteMiddle(self):
        solution = Solution()

        builder = LinkedListBuilder()
        input_linked_list = builder.build([1,3,4,7,1,2,6])
        result = solution.deleteMiddle(input_linked_list)
        result_arr = builder.debuild(result)
        self.assertEqual(result_arr, [1,3,4,1,2,6])

        input_linked_list = builder.build([1,2,3,4])
        result = solution.deleteMiddle(input_linked_list)
        result_arr = builder.debuild(result)
        self.assertEqual(result_arr, [1,2,4])

        input_linked_list = builder.build([2,1])
        result = solution.deleteMiddle(input_linked_list)
        result_arr = builder.debuild(result)
        self.assertEqual(result_arr, [2])

        input_linked_list = builder.build([3,1,2])
        result = solution.deleteMiddle(input_linked_list)
        result_arr = builder.debuild(result)
        self.assertEqual(result_arr, [3,2])