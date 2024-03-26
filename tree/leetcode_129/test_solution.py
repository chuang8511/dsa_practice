import unittest

from solution import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_sumNumbers(self):
        solution = Solution()
        builder = BuildTreeNode()

        # tree = builder.build([1,2,3])
        # result = solution.sumNumbers(tree)
        # self.assertEqual(result, 25)

        tree = builder.build([4,9,0,5,1])
        result = solution.sumNumbers(tree)
        self.assertEqual(result, 1026)