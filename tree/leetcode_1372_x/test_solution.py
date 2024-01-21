import unittest

from tree.leetcode_1372_x.solution_x import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_longestZigZag(self):
        solution = Solution()
        builder = BuildTreeNode()

        tree = builder.build([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
        result = solution.longestZigZag(tree)
        self.assertEqual(result, 3)

        tree = builder.build([1,1,1,None,1,None,None,1,1,None,1])
        result = solution.longestZigZag(tree)
        self.assertEqual(result, 4)

        tree = builder.build([1])
        result = solution.longestZigZag(tree)
        self.assertEqual(result, 0)

        tree = builder.build([6,9,7,3,None,2,8,5,8,9,7,3,9,9,4,2,10,None,5,4,3,10,10,9,4,1,2,None,None,6,5,None,None,None,None,9,None,9,6,5,None,5,None,None,7,7,4,None,1,None,None,3,7,None,9,None,None,None,None,None,None,None,None,9,9,None,None,None,7,None,None,None,None,None,None,None,None,None,6,8,7,None,None,None,3,10,None,None,None,None,None,1,None,1,2])
        result = solution.longestZigZag(tree)
        self.assertEqual(result, 5)

        tree = builder.build([8,1,7,None,None,3,9,6,9,2,7,5,10,2,4,2,None,1,9,3,None,None,8,None,8,6,2,5,1,2,5,10,3,None,8,5,3,None,None,None,9,5,None,None,8,1,None,None,None,None,None,10,10,5,3,None,None,None,3,5,1,3,None,None,None,None,None,6,None,None,None,None,4,None,None,2,None,None,None,1,1,8,None,None,None,None,None,None,None,None,None,None,None,7,None,7])
        result = solution.longestZigZag(tree)
        self.assertEqual(result, 5)