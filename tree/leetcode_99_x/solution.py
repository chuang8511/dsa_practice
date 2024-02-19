# Definition for a binary tree node.
# !!! inorder traversal of the BST == sorted array
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: [TreeNode]) -> None:
        arr = []
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            arr.append(node)
            in_order(node.right)
        
        in_order(root)
        new_arr = sorted(arr, key=lambda node: node.val)
        for i in range(len(arr)):
            if arr[i].val != new_arr[i].val:
                arr[i].val, new_arr[i].val = new_arr[i].val, arr[i].val
                break