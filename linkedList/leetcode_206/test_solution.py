import unittest
from solution import Solution
from linked_list import LinkedListBuilder

class TestSolution(unittest.TestCase):
    def test_reverseList(self):
        solution = Solution()

        builder = LinkedListBuilder()
        input_linked_list = builder.build([1,2,3,4,5])
        result = solution.reverseList(input_linked_list)
        result_arr = builder.debuild(result)
        self.assertEqual(result_arr, [5,4,3,2,1])

        input_linked_list = builder.build([1,2])
        result = solution.reverseList(input_linked_list)
        result_arr = builder.debuild(result)
        self.assertEqual(result_arr, [2,1])

        input_linked_list = builder.build([])
        result = solution.reverseList(input_linked_list)
        result_arr = builder.debuild(result)
        self.assertEqual(result_arr, [])
