import unittest

from solution import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_pathSum(self):
        solution = Solution()
        builder = BuildTreeNode()

        i = 0
        i += 1
        print(i)
        tree = builder.build([10,5,-3,3,2,None,11,3,-2,None,1])
        result = solution.pathSum(tree, 8)
        self.assertEqual(result, 3)

        i += 1
        print(i)
        tree = builder.build([5,4,8,11,None,13,4,7,2,None,None,5,1])
        result = solution.pathSum(tree, 22)
        self.assertEqual(result, 3)

        i += 1
        print(i)
        # tree = builder.build([])
        result = solution.pathSum(None, 1)
        self.assertEqual(result, 0)

        i += 1
        print(i)
        tree = builder.build([0,1,1])
        result = solution.pathSum(tree, 1)
        self.assertEqual(result, 4)