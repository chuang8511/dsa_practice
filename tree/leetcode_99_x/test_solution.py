import unittest

from solution import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_recoverTree(self):
        solution = Solution()
        builder = BuildTreeNode()

        tree = builder.build([1,3,None,None,2])
        solution.recoverTree(tree)
        expected_val = builder.tree_to_array(tree)
        self.assertEqual(expected_val, [3,1,None,None,2])

        tree = builder.build([3,1,4,None,None,2])
        solution.recoverTree(tree)
        expected_val = builder.tree_to_array(tree)
        self.assertEqual(expected_val, [2,1,4,None,None,3])