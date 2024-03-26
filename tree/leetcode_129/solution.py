class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not (root.left or root.right):
            return root.val
        
        self.nums = []

        def is_leave(node):
            if node.left or node.right:
                return False
            return True
        
        def dfs(node, previous_string):
            if is_leave(node):
                num = int(previous_string + str(node.val))
                self.nums.append(num)
                return

            if node.left:
                dfs(node.left, previous_string + str(node.val))

            if node.right:
                dfs(node.right, previous_string + str(node.val))

        dfs(root, "")

        return sum(self.nums)