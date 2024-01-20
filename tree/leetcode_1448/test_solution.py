import unittest

from solution import Solution

from tree_node import BuildTreeNode

class TestSolution(unittest.TestCase):
    def test_goodNodes(self):
        solution = Solution()
        builder = BuildTreeNode()

        i = 0
        i += 1
        print(i)
        tree = builder.build([3,1,4,3,None,1,5])
        result = solution.goodNodes(tree)
        self.assertEqual(result, 4)

        i += 1
        print(i)
        tree = builder.build([3,3,None,4,2])
        result = solution.goodNodes(tree)
        self.assertEqual(result, 3)

        i += 1
        print(i)
        tree = builder.build([1])
        result = solution.goodNodes(tree)
        self.assertEqual(result, 1)

        i += 1
        print(i)
        tree = builder.build([9,None,3,6])
        result = solution.goodNodes(tree)
        self.assertEqual(result, 1)