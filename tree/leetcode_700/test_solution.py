import unittest

from solution import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_searchBST(self):
        solution = Solution()
        builder = BuildTreeNode()

        tree = builder.build([4,2,7,1,3])
        result = solution.searchBST(tree, 2)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [2,1,3])

        tree = builder.build([4,2,7,1,3])
        result = solution.searchBST(tree, 5)
        result_arr = builder.tree_to_array(result)
        self.assertEqual(result_arr, [])