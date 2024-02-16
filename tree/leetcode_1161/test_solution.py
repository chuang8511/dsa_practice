import unittest

from solution import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_maxLevelSum(self):
        solution = Solution()
        builder = BuildTreeNode()

        tree = builder.build([1,7,0,7,-8,None,None])
        result = solution.maxLevelSum(tree)
        self.assertEqual(result, 2)

        tree = builder.build([989,None,10250,98693,-89388,None,None,None,-32127])
        result = solution.maxLevelSum(tree)
        self.assertEqual(result, 2)

        tree = builder.build([-100,-200,-300,-20,-5,-10,None])
        result = solution.maxLevelSum(tree)
        self.assertEqual(result, 3)