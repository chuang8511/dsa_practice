import pdb
import unittest

from solution import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_maxDepth(self):
        # pdb.set_trace()
        solution = Solution()
        builder = BuildTreeNode()

        tree = builder.build([3,9,20,None,None,15,7])
        result = solution.maxDepth(tree)
        self.assertEqual(result, 3)

        tree = builder.build([1,None,2])
        result = solution.maxDepth(tree)
        self.assertEqual(result, 2)