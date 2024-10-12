from tree_node import TreeNode, BuildTreeNode

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node: TreeNode, left: int, right: int) -> bool:
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            
            next_left_check = valid(node.left, left, node.val)
            next_right_check = valid(node.right, node.val, right)

            return next_left_check and next_right_check
        return valid(root, float("-inf"), float("inf"))





test_cases = [
    [2,1,3],
    [5,1,4,None,None,3,6]
]

solution = Solution()
for case in test_cases:
    tree = BuildTreeNode().build(case)

    print(solution.isValidBST(tree))