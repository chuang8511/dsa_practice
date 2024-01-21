# test 1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: [TreeNode]) -> int:
        self.maxi = 0

        def dfs(node, cur_max, pre_direction):

            if node:
                self.maxi = max(self.maxi, cur_max)

                if pre_direction == "left":
                    dfs(node.right, cur_max + 1, "right")
                    dfs(node.left, 1, "left")
                elif pre_direction == "right":
                    dfs(node.left, cur_max + 1, "left")
                    dfs(node.right, 1, "right")

        if root.left:
            dfs(root.left, 1, "left")
        if root.right:
            dfs(root.right, 1, "right")

        return self.maxi