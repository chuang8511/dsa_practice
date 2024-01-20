import pdb
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        
        # pdb.set_trace()
        def dfs(node, max_node_num):
            if node.val >= max_node_num:
                res[0] += 1
            max_node_num = max(max_node_num, node.val)
            if node.left:
                dfs(node.left, max_node_num)
            if node.right:
                dfs(node.right, max_node_num)
        
        if root.left:
            dfs(root.left, root.val)
        
        if root.right:
            dfs(root.right, root.val)
        return res[0] + 1