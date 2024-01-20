import unittest

from solution import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_rightSideView(self):
        solution = Solution()
        builder = BuildTreeNode()

        tree = builder.build([1,2,3,None,5,None,4])
        result = solution.rightSideView(tree)
        self.assertEqual(result, [1,3,4])

        tree = builder.build([1,None,3])
        result = solution.rightSideView(tree)
        self.assertEqual(result, [1,3])

        tree = builder.build([])
        result = solution.rightSideView(tree)
        self.assertEqual(result, [])

        tree = builder.build([1,2])
        result = solution.rightSideView(tree)
        self.assertEqual(result, [1,2])