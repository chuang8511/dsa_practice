import unittest

from solution import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_deleteNode(self):
        solution = Solution()
        builder = BuildTreeNode()

        tree = builder.build([5,3,6,2,4,None,7])
        key = 3
        result = solution.deleteNode(tree, key)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [5,4,6,2,None,None,7])

        tree = builder.build([5,3,6,2,4,None,7])
        key = 0
        result = solution.deleteNode(tree, key)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [5,3,6,2,4,None,7])

        tree = builder.build([])
        key = 0
        result = solution.deleteNode(tree, key)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [])

        tree = builder.build([0])
        key = 0
        result = solution.deleteNode(tree, key)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [])

        tree = builder.build([5,3,6,2,4,None,7])
        key = 5
        result = solution.deleteNode(tree, key)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [6,3,7,2,4])

        tree = builder.build([5,3,6,2,4,None,7])
        key = 7
        result = solution.deleteNode(tree, key)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [5,3,6,2,4])

        tree = builder.build([2,1])
        key = 2
        result = solution.deleteNode(tree, key)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [1])