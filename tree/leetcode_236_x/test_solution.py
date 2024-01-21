import unittest

from tree.leetcode_236_x.solution_x import Solution

from tree.leetcode_236_x.tree_node_x import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_lowestCommonAncestor(self):
        solution = Solution()
        builder = BuildTreeNode()

        tree = builder.build([3,5,1,6,2,0,8,None,None,7,4])
        tree_p = tree.left
        tree_q = tree.right
        result = solution.lowestCommonAncestor(tree, tree_p, tree_q)
        self.assertEqual(result, tree)

        tree = builder.build([3,5,1,6,2,0,8,None,None,7,4])
        tree_p = tree.left
        tree_q = tree.left.right.right
        result = solution.lowestCommonAncestor(tree, tree_p, tree_q)
        self.assertEqual(result, tree.left)

        tree = builder.build([1,2])
        tree_p = tree
        tree_q = tree.left
        result = solution.lowestCommonAncestor(tree, tree_p, tree_q)
        self.assertEqual(result, tree)