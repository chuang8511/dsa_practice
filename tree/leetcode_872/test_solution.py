import unittest

from solution import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_leafSimilar(self):
        solution = Solution()
        builder = BuildTreeNode()

        tree = builder.build([3,5,1,6,2,9,8,None,None,7,4])
        tree_2 = builder.build([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
        result = solution.leafSimilar(tree, tree_2)
        self.assertEqual(result, True)

        tree = builder.build([1,2,3])
        tree_2 = builder.build([1,3,2])
        result = solution.leafSimilar(tree, tree_2)
        self.assertEqual(result, False)

        tree = builder.build([4,2,6,1,3,5,7])
        tree_2 = builder.build([4,2,6,None,3,5,7])
        result = solution.leafSimilar(tree, tree_2)
        self.assertEqual(result, False)

        tree = builder.build([4,2,6,None,3,5,7])
        tree_2 = builder.build([4,2,6,1,3,5,7])
        result = solution.leafSimilar(tree, tree_2)
        self.assertEqual(result, False)

        tree = builder.build([41,62,None,66,None,None,21,96,None,70,74])
        tree_2 = builder.build([55,None,84,None,29,116,None,7,74,None,70])
        result = solution.leafSimilar(tree, tree_2)
        self.assertEqual(result, True)