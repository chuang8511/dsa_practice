# memo
# In bst_swap, add another argument that can compare with the current node value
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def recoverTree(self, root: [TreeNode]) -> None:
        
#         def bst_swap(node, ):
#             if node:
#                 if node.left:
#                     if node.left.val > node.val:
#                         temp = node.val
#                         node.val = node.left.val
#                         node.left.val = temp
#                     bst_swap(node.left)
#                     bst_swap(node.right)
#                 if node.right:
#                     if node.right.val < node.val:
#                         temp = node.val
#                         node.val = node.right.val
#                         node.right.val = temp
#                     bst_swap(node.left)
#                     bst_swap(node.right)

#         bst_swap(root)